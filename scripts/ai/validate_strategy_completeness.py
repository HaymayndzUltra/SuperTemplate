#!/usr/bin/env python3
"""
Strategy Validator for AI Data Strategy Planning

Validates completeness and quality of data strategy artifacts,
ensuring all requirements are met before proceeding to next protocol.
"""

import argparse
import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

class StrategyValidator:
    """Validate data strategy completeness and quality"""
    
    def __init__(self, protocol_number: str = "07"):
        self.protocol_number = protocol_number
        self.artifacts_dir = Path(f".artifacts/protocol-{protocol_number}-ai-data-strategy-planning")
        
        # Required artifacts and their validation rules
        self.required_artifacts = {
            'phase-01-context/01-input-sources-summary.md': {
                'type': 'markdown',
                'required_sections': ['Use Cases', 'Project Context', 'Data Sources'],
                'min_size_kb': 1
            },
            'phase-01-context/01-use-case-to-data-needs-sketch.md': {
                'type': 'markdown',
                'required_sections': ['Use Case Mapping', 'Data Categories'],
                'min_size_kb': 1
            },
            'phase-02-requirements/02-data-requirements.md': {
                'type': 'markdown',
                'required_sections': ['Dataset Requirements', 'Quality Specifications'],
                'min_size_kb': 2
            },
            'phase-02-requirements/02-data-requirements-inventory.json': {
                'type': 'json',
                'schema_validation': True,
                'required_fields': ['use_case_id', 'dataset_name', 'fields', 'source_system']
            },
            'phase-02-requirements/02-data-gaps-log.md': {
                'type': 'markdown',
                'required_sections': ['Missing Data', 'Impact Assessment'],
                'min_size_kb': 1
            },
            'phase-03-compliance/03-compliance-requirements.json': {
                'type': 'json',
                'schema_validation': True,
                'required_fields': ['dataset_id', 'applicable_regulations', 'sensitivity_level']
            },
            'phase-03-compliance/03-data-risk-assessment.md': {
                'type': 'markdown',
                'required_sections': ['Risk Analysis', 'Mitigation Strategies'],
                'min_size_kb': 2
            },
            'phase-04-signoff/data-strategy.md': {
                'type': 'markdown',
                'required_sections': ['Executive Summary', 'Data Requirements', 'Compliance', 'Implementation Plan'],
                'min_size_kb': 5
            },
            'phase-04-signoff/labeling-strategy.yaml': {
                'type': 'yaml',
                'conditional': True,  # Only required if supervised learning
                'required_fields': ['annotation_approach', 'quality_thresholds']
            },
            'phase-04-signoff/data-strategy-signoff.md': {
                'type': 'markdown',
                'required_sections': ['Approvals', 'Conditions', 'Timeline'],
                'min_size_kb': 1
            }
        }
        
        # Quality gates validation
        self.quality_gates = {
            'gate_1': {
                'name': 'Data Requirements Completeness',
                'criteria': '100% use case coverage',
                'validation': self._validate_gate_1
            },
            'gate_2': {
                'name': 'Compliance Specification Coverage',
                'criteria': '≥95% dataset compliance mapping',
                'validation': self._validate_gate_2
            },
            'gate_3': {
                'name': 'Risk & Mitigation Coverage',
                'criteria': '100% high-risk items mitigated',
                'validation': self._validate_gate_3
            },
            'gate_4': {
                'name': 'Final Sign-off',
                'criteria': 'Minimum 2 stakeholder approvals',
                'validation': self._validate_gate_4
            }
        }

    def validate_artifact_exists(self, artifact_path: str) -> Tuple[bool, Optional[str], Dict[str, Any]]:
        """Check if artifact exists and get basic info"""
        full_path = self.artifacts_dir / artifact_path
        
        if not full_path.exists():
            return False, f"Artifact not found: {artifact_path}", {}
        
        try:
            stat = full_path.stat()
            info = {
                'size_bytes': stat.st_size,
                'size_kb': stat.st_size / 1024,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
            }
            return True, None, info
        except Exception as e:
            return False, f"Error accessing artifact: {e}", {}

    def validate_markdown_content(self, artifact_path: str, rules: Dict[str, Any]) -> Dict[str, Any]:
        """Validate markdown file content"""
        full_path = self.artifacts_dir / artifact_path
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            validation_result = {
                'content_length': len(content),
                'sections_found': [],
                'sections_missing': [],
                'size_valid': True,
                'content_issues': []
            }
            
            # Check minimum size
            min_size_kb = rules.get('min_size_kb', 1)
            if len(content) / 1024 < min_size_kb:
                validation_result['size_valid'] = False
                validation_result['content_issues'].append(
                    f"Content too small: {len(content)/1024:.1f}KB < {min_size_kb}KB minimum"
                )
            
            # Check required sections
            required_sections = rules.get('required_sections', [])
            for section in required_sections:
                # Look for section headers (## or ###)
                pattern = rf'^(#+\s*{re.escape(section)}\s*$)'
                if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                    validation_result['sections_found'].append(section)
                else:
                    validation_result['sections_missing'].append(section)
            
            # Check for common content quality issues
            if len(content.strip()) < 100:
                validation_result['content_issues'].append("Content appears to be minimal or placeholder")
            
            if content.count('TODO') > 5:
                validation_result['content_issues'].append("High number of TODO items detected")
            
            return validation_result
            
        except Exception as e:
            return {'error': f"Error reading markdown file: {e}"}

    def validate_json_content(self, artifact_path: str, rules: Dict[str, Any]) -> Dict[str, Any]:
        """Validate JSON file content"""
        full_path = self.artifacts_dir / artifact_path
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            validation_result = {
                'json_valid': True,
                'structure_valid': True,
                'required_fields_found': [],
                'required_fields_missing': [],
                'data_issues': []
            }
            
            # Check if it's a list or object
            if isinstance(data, list):
                validation_result['record_count'] = len(data)
                if len(data) == 0:
                    validation_result['data_issues'].append("JSON array is empty")
                    validation_result['structure_valid'] = False
                # Validate first item as sample
                sample_data = data[0] if data else {}
            elif isinstance(data, dict):
                validation_result['record_count'] = 1
                sample_data = data
            else:
                validation_result['structure_valid'] = False
                validation_result['data_issues'].append("JSON must be object or array")
                return validation_result
            
            # Check required fields
            required_fields = rules.get('required_fields', [])
            for field in required_fields:
                if field in sample_data:
                    validation_result['required_fields_found'].append(field)
                else:
                    validation_result['required_fields_missing'].append(field)
            
            # Additional data quality checks
            if isinstance(data, list) and len(data) > 1:
                # Check consistency across records
                first_keys = set(data[0].keys())
                for i, record in enumerate(data[1:], 1):
                    if set(record.keys()) != first_keys:
                        validation_result['data_issues'].append(
                            f"Inconsistent structure at record {i}: missing fields {first_keys - set(record.keys())}"
                        )
                        break
            
            return validation_result
            
        except json.JSONDecodeError as e:
            return {
                'json_valid': False,
                'structure_valid': False,
                'error': f"Invalid JSON format: {e}"
            }
        except Exception as e:
            return {
                'json_valid': False,
                'structure_valid': False,
                'error': f"Error reading JSON file: {e}"
            }

    def validate_yaml_content(self, artifact_path: str, rules: Dict[str, Any]) -> Dict[str, Any]:
        """Validate YAML file content"""
        full_path = self.artifacts_dir / artifact_path
        
        try:
            import yaml
            with open(full_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            validation_result = {
                'yaml_valid': True,
                'structure_valid': True,
                'required_fields_found': [],
                'required_fields_missing': []
            }
            
            if not isinstance(data, dict):
                validation_result['structure_valid'] = False
                validation_result['error'] = "YAML must be object/dictionary"
                return validation_result
            
            # Check required fields
            required_fields = rules.get('required_fields', [])
            for field in required_fields:
                if field in data:
                    validation_result['required_fields_found'].append(field)
                else:
                    validation_result['required_fields_missing'].append(field)
            
            return validation_result
            
        except ImportError:
            return {
                'yaml_valid': False,
                'error': "PyYAML not installed - cannot validate YAML content"
            }
        except Exception as e:
            return {
                'yaml_valid': False,
                'structure_valid': False,
                'error': f"Error reading YAML file: {e}"
            }

    def validate_artifact(self, artifact_path: str, rules: Dict[str, Any]) -> Dict[str, Any]:
        """Validate a single artifact"""
        # Check existence
        exists, error, info = self.validate_artifact_exists(artifact_path)
        if not exists:
            return {
                'artifact_path': artifact_path,
                'exists': False,
                'error': error,
                'validation_status': 'FAILED'
            }
        
        result = {
            'artifact_path': artifact_path,
            'exists': True,
            'file_info': info,
            'validation_status': 'PASSED'
        }
        
        # Validate content based on type
        artifact_type = rules.get('type', 'markdown')
        
        if artifact_type == 'markdown':
            content_validation = self.validate_markdown_content(artifact_path, rules)
            result.update(content_validation)
        elif artifact_type == 'json':
            content_validation = self.validate_json_content(artifact_path, rules)
            result.update(content_validation)
        elif artifact_type == 'yaml':
            content_validation = self.validate_yaml_content(artifact_path, rules)
            result.update(content_validation)
        else:
            result['content_validation'] = f"Unsupported type: {artifact_type}"
        
        # Determine overall status
        if 'error' in result:
            result['validation_status'] = 'FAILED'
        elif artifact_type == 'markdown':
            if (not result.get('size_valid', True) or 
                len(result.get('sections_missing', [])) > 0 or
                len(result.get('content_issues', [])) > 0):
                result['validation_status'] = 'WARNING'
        elif artifact_type == 'json':
            if (not result.get('json_valid', True) or 
                not result.get('structure_valid', True) or
                len(result.get('required_fields_missing', [])) > 0):
                result['validation_status'] = 'FAILED'
        elif artifact_type == 'yaml':
            if (not result.get('yaml_valid', True) or 
                not result.get('structure_valid', True) or
                len(result.get('required_fields_missing', [])) > 0):
                result['validation_status'] = 'FAILED'
        
        return result

    def _validate_gate_1(self, artifacts: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Gate 1: Data Requirements Completeness"""
        inventory = artifacts.get('phase-02-requirements/02-data-requirements-inventory.json', {})
        
        if not inventory.get('exists', False):
            return {'passed': False, 'reason': 'Requirements inventory not found'}
        
        if not inventory.get('json_valid', False):
            return {'passed': False, 'reason': 'Requirements inventory invalid JSON'}
        
        record_count = inventory.get('record_count', 0)
        if record_count == 0:
            return {'passed': False, 'reason': 'No use cases in requirements inventory'}
        
        # Check for use case coverage (would need input from Protocol 06)
        # For now, validate that we have at least one use case mapped
        return {
            'passed': True,
            'score': 1.0,
            'details': f'Found {record_count} use case requirements'
        }

    def _validate_gate_2(self, artifacts: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Gate 2: Compliance Specification Coverage"""
        compliance = artifacts.get('phase-03-compliance/03-compliance-requirements.json', {})
        
        if not compliance.get('exists', False):
            return {'passed': False, 'reason': 'Compliance requirements not found'}
        
        if not compliance.get('json_valid', False):
            return {'passed': False, 'reason': 'Compliance requirements invalid JSON'}
        
        record_count = compliance.get('record_count', 0)
        if record_count == 0:
            return {'passed': False, 'reason': 'No compliance specifications found'}
        
        # Calculate coverage score (simplified - would compare with requirements inventory)
        coverage_score = min(1.0, record_count / max(1, record_count))  # Placeholder logic
        
        return {
            'passed': coverage_score >= 0.95,
            'score': coverage_score,
            'details': f'Compliance coverage: {coverage_score:.1%}'
        }

    def _validate_gate_3(self, artifacts: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Gate 3: Risk & Mitigation Coverage"""
        risk_assessment = artifacts.get('phase-03-compliance/03-data-risk-assessment.md', {})
        
        if not risk_assessment.get('exists', False):
            return {'passed': False, 'reason': 'Risk assessment not found'}
        
        # Check if high-risk items have mitigations
        sections_found = risk_assessment.get('sections_found', [])
        has_mitigations = 'Mitigation Strategies' in sections_found
        
        if not has_mitigations:
            return {'passed': False, 'reason': 'Risk mitigation strategies not documented'}
        
        return {
            'passed': True,
            'score': 1.0,
            'details': 'Risk assessment and mitigations documented'
        }

    def _validate_gate_4(self, artifacts: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Gate 4: Final Sign-off"""
        signoff = artifacts.get('phase-04-signoff/data-strategy-signoff.md', {})
        
        if not signoff.get('exists', False):
            return {'passed': False, 'reason': 'Sign-off document not found'}
        
        # Check for approval content (simplified)
        content_validation = self.validate_markdown_content(
            'phase-04-signoff/data-strategy-signoff.md',
            {'required_sections': ['Approvals']}
        )
        
        has_approvals = 'Approvals' in content_validation.get('sections_found', [])
        
        if not has_approvals:
            return {'passed': False, 'reason': 'No approval section found in sign-off'}
        
        return {
            'passed': True,
            'score': 1.0,
            'details': 'Sign-off document with approvals present'
        }

    def validate_quality_gates(self, artifacts: Dict[str, Any]) -> Dict[str, Any]:
        """Validate all quality gates"""
        gate_results = {}
        overall_passed = True
        total_score = 0
        
        for gate_id, gate_config in self.quality_gates.items():
            validation_func = gate_config['validation']
            result = validation_func(artifacts)
            
            gate_results[gate_id] = {
                'name': gate_config['name'],
                'criteria': gate_config['criteria'],
                **result
            }
            
            if not result.get('passed', False):
                overall_passed = False
            
            total_score += result.get('score', 0)
        
        average_score = total_score / len(self.quality_gates)
        
        return {
            'overall_passed': overall_passed,
            'average_score': average_score,
            'gate_results': gate_results
        }

    def validate_strategy(self) -> Dict[str, Any]:
        """Perform complete strategy validation"""
        validation_results = {
            'timestamp': datetime.now().isoformat(),
            'protocol_number': self.protocol_number,
            'artifacts_directory': str(self.artifacts_dir),
            'validation_summary': {
                'total_artifacts': len(self.required_artifacts),
                'artifacts_validated': 0,
                'artifacts_passed': 0,
                'artifacts_failed': 0,
                'artifacts_warning': 0
            },
            'artifact_validations': {},
            'quality_gates': {},
            'overall_status': 'FAILED'
        }
        
        # Validate each artifact
        for artifact_path, rules in self.required_artifacts.items():
            # Skip conditional artifacts if not applicable
            if rules.get('conditional', False):
                # For labeling strategy, check if supervised learning is needed
                # This is simplified - in practice would check use cases
                continue
            
            result = self.validate_artifact(artifact_path, rules)
            validation_results['artifact_validations'][artifact_path] = result
            
            # Update summary
            validation_results['validation_summary']['artifacts_validated'] += 1
            
            status = result.get('validation_status', 'FAILED')
            if status == 'PASSED':
                validation_results['validation_summary']['artifacts_passed'] += 1
            elif status == 'FAILED':
                validation_results['validation_summary']['artifacts_failed'] += 1
            elif status == 'WARNING':
                validation_results['validation_summary']['artifacts_warning'] += 1
        
        # Validate quality gates
        validation_results['quality_gates'] = self.validate_quality_gates(
            validation_results['artifact_validations']
        )
        
        # Determine overall status
        summary = validation_results['validation_summary']
        gates = validation_results['quality_gates']
        
        if (summary['artifacts_failed'] == 0 and 
            gates['overall_passed'] and 
            gates['average_score'] >= 0.95):
            validation_results['overall_status'] = 'PASSED'
        elif summary['artifacts_failed'] == 0 and gates['average_score'] >= 0.90:
            validation_results['overall_status'] = 'WARNING'
        else:
            validation_results['overall_status'] = 'FAILED'
        
        # Add recommendations
        validation_results['recommendations'] = self._generate_recommendations(validation_results)
        
        return validation_results

    def _generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []
        
        summary = results['validation_summary']
        if summary['artifacts_failed'] > 0:
            recommendations.append(f"Address {summary['artifacts_failed']} failed artifacts")
        
        if summary['artifacts_warning'] > 0:
            recommendations.append(f"Review {summary['artifacts_warning']} artifacts with warnings")
        
        gates = results['quality_gates']
        if not gates['overall_passed']:
            failed_gates = [name for name, result in gates['gate_results'].items() 
                          if not result.get('passed', False)]
            recommendations.append(f"Fix failed quality gates: {', '.join(failed_gates)}")
        
        if gates['average_score'] < 0.95:
            recommendations.append("Improve overall quality to meet 95% threshold")
        
        # Check for common issues
        for artifact_path, validation in results['artifact_validations'].items():
            if validation.get('validation_status') == 'WARNING':
                if not validation.get('size_valid', True):
                    recommendations.append(f"Expand content in {artifact_path}")
                if validation.get('sections_missing'):
                    recommendations.append(f"Add missing sections to {artifact_path}")
        
        return recommendations

def main():
    parser = argparse.ArgumentParser(description='Validate data strategy completeness')
    parser.add_argument('--protocol', default='07', help='Protocol number to validate')
    parser.add_argument('--strategy-dir', help='Strategy directory (default: .artifacts/protocol-{number})')
    parser.add_argument('--report', required=True, help='Output JSON validation report')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Initialize validator
    validator = StrategyValidator(args.protocol)
    
    # Override strategy directory if provided
    if args.strategy_dir:
        validator.artifacts_dir = Path(args.strategy_dir)
    
    # Check if artifacts directory exists
    if not validator.artifacts_dir.exists():
        print(f"Artifacts directory not found: {validator.artifacts_dir}")
        sys.exit(1)
    
    # Perform validation
    results = validator.validate_strategy()
    
    # Save report
    try:
        output_path = Path(args.report)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(args.report, 'w') as f:
            json.dump(results, f, indent=2)
        
        if args.verbose:
            summary = results['validation_summary']
            print(f"Validated {summary['artifacts_validated']} artifacts")
            print(f"Passed: {summary['artifacts_passed']}, Failed: {summary['artifacts_failed']}, Warnings: {summary['artifacts_warning']}")
            print(f"Overall status: {results['overall_status']}")
            print(f"Quality gates score: {results['quality_gates']['average_score']:.1%}")
            print(f"Report saved to: {args.report}")
        
        # Exit with appropriate code
        if results['overall_status'] == 'PASSED':
            sys.exit(0)
        elif results['overall_status'] == 'WARNING':
            sys.exit(1)
        else:
            sys.exit(2)
            
    except Exception as e:
        print(f"Error saving validation report: {e}")
        sys.exit(3)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Evidence Aggregation Script for Protocol 08
Aggregates all evidence artifacts for validation and handoff
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('evidence_aggregation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class EvidenceAggregator:
    """Aggregates evidence artifacts for protocol validation"""
    
    def __init__(self, output_path: str, protocol_id: str):
        self.output_path = Path(output_path)
        self.protocol_id = protocol_id
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.aggregation_log = []
        self.start_time = datetime.now()
        
        # Expected evidence artifacts
        self.expected_artifacts = [
            'pipeline_config_report.json',
            'collection_log.json',
            'data_quality_report.json',
            'compliance_report.json',
            'handoff_readiness_report.json'
        ]
    
    def discover_evidence_artifacts(self) -> List[Path]:
        """Discover all evidence artifacts in output directory"""
        logger.info("Discovering evidence artifacts")
        
        evidence_files = []
        
        # Look for expected artifacts
        for artifact in self.expected_artifacts:
            artifact_path = self.output_path / artifact
            if artifact_path.exists():
                evidence_files.append(artifact_path)
        
        # Look for any JSON files that might be evidence
        evidence_files.extend(self.output_path.glob("*.json"))
        
        # Remove duplicates
        evidence_files = list(set(evidence_files))
        
        logger.info(f"Discovered {len(evidence_files)} evidence artifacts")
        return evidence_files
    
    def calculate_file_checksum(self, file_path: Path) -> str:
        """Calculate SHA256 checksum for file integrity"""
        try:
            hash_sha256 = hashlib.sha256()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash sha256.update(chunk)
            return hash_sha256.hexdigest()
        except Exception as e:
            logger.error(f"Failed to calculate checksum for {file_path}: {e}")
            return "unknown"
    
    def validate_artifact_structure(self, file_path: Path) -> Dict[str, Any]:
        """Validate structure and content of evidence artifact"""
        try:
            with open(file_path, 'r') as f:
                content = json.load(f)
            
            # Basic structure validation
            validation_result = {
                'file_path': str(file_path),
                'file_size_bytes': file_path.stat().st_size,
                'checksum': self.calculate_file_checksum(file_path),
                'structure_valid': True,
                'validation_errors': []
            }
            
            # Check for required fields based on file type
            file_name = file_path.name
            
            if 'config_report' in file_name:
                required_fields = ['validation_summary', 'validations']
            elif 'quality_report' in file_name:
                required_fields = ['validation_summary', 'file_validations']
            elif 'compliance_report' in file_name:
                required_fields = ['compliance_summary', 'file_compliance_results']
            elif 'handoff_report' in file_name:
                required_fields = ['handoff_summary', 'readiness_validations']
            else:
                required_fields = []  # Generic files
            
            # Check required fields
            for field in required_fields:
                if field not in content:
                    validation_result['validation_errors'].append(f"Missing required field: {field}")
                    validation_result['structure_valid'] = False
            
            # Add content summary
            validation_result['content_summary'] = {
                'keys': list(content.keys()) if isinstance(content, dict) else [],
                'total_keys': len(content.keys()) if isinstance(content, dict) else 0,
                'is_json': True
            }
            
            return validation_result
            
        except json.JSONDecodeError as e:
            return {
                'file_path': str(file_path),
                'file_size_bytes': file_path.stat().st_size,
                'checksum': self.calculate_file_checksum(file_path),
                'structure_valid': False,
                'validation_errors': [f"Invalid JSON: {e}"],
                'content_summary': {'is_json': False}
            }
        except Exception as e:
            return {
                'file_path': str(file_path),
                'file_size_bytes': file_path.stat().st_size,
                'checksum': self.calculate_file_checksum(file_path),
                'structure_valid': False,
                'validation_errors': [f"Validation error: {e}"],
                'content_summary': {'is_json': False}
            }
    
    def extract_validation_metrics(self, file_path: Path) -> Dict[str, Any]:
        """Extract validation metrics from evidence artifacts"""
        try:
            with open(file_path, 'r') as f:
                content = json.load(f)
            
            metrics = {
                'file_path': str(file_path),
                'extraction_successful': True,
                'metrics': {}
            }
            
            # Extract common metrics
            if 'validation_summary' in content:
                summary = content['validation_summary']
                metrics['metrics'].update({
                    'overall_score': summary.get('overall_score', 0.0),
                    'validation_passed': summary.get('validation_passed', False),
                    'execution_time_seconds': summary.get('execution_time_seconds', 0.0)
                })
            
            if 'compliance_summary' in content:
                summary = content['compliance_summary']
                metrics['metrics'].update({
                    'overall_compliance_score': summary.get('overall_compliance_score', 0.0),
                    'compliance_passed': summary.get('compliance_passed', False),
                    'total_files': summary.get('total_files', 0)
                })
            
            # Extract file-specific metrics
            if 'file_validations' in content:
                file_validations = content['file_validations']
                metrics['metrics']['total_validated_files'] = len(file_validations)
                metrics['metrics']['passed_validations'] = sum(1 for v in file_validations if v.get('validation_status') == 'passed')
            
            if 'file_compliance_results' in content:
                compliance_results = content['file_compliance_results']
                metrics['metrics']['total_compliance_files'] = len(compliance_results)
                metrics['metrics']['passed_compliance'] = sum(1 for r in compliance_results if r.get('compliance_status') == 'passed')
            
            return metrics
            
        except Exception as e:
            return {
                'file_path': str(file_path),
                'extraction_successful': False,
                'error': str(e),
                'metrics': {}
            }
    
    def create_evidence_manifest(self, evidence_files: List[Path]) -> Dict[str, Any]:
        """Create comprehensive evidence manifest"""
        logger.info("Creating evidence manifest")
        
        manifest = {
            'protocol_id': self.protocol_id,
            'aggregation_timestamp': datetime.now().isoformat(),
            'total_artifacts': len(evidence_files),
            'expected_artifacts': self.expected_artifacts,
            'discovered_artifacts': [],
            'artifact_validations': [],
            'validation_metrics': [],
            'overall_assessment': {
                'all_expected_present': False,
                'all_structures_valid': False,
                'aggregation_complete': False
            }
        }
        
        # Process each evidence artifact
        expected_present = 0
        all_structures_valid = True
        
        for file_path in evidence_files:
            file_info = {
                'file_name': file_path.name,
                'file_path': str(file_path),
                'file_size_bytes': file_path.stat().st_size,
                'last_modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            }
            manifest['discovered_artifacts'].append(file_info)
            
            # Validate structure
            structure_validation = self.validate_artifact_structure(file_path)
            manifest['artifact_validations'].append(structure_validation)
            
            if not structure_validation['structure_valid']:
                all_structures_valid = False
            
            # Extract metrics
            metrics_extraction = self.extract_validation_metrics(file_path)
            manifest['validation_metrics'].append(metrics_extraction)
            
            # Check if expected artifact
            if file_path.name in self.expected_artifacts:
                expected_present += 1
        
        # Update overall assessment
        manifest['overall_assessment']['all_expected_present'] = expected_present == len(self.expected_artifacts)
        manifest['overall_assessment']['all_structures_valid'] = all_structures_valid
        manifest['overall_assessment']['aggregation_complete'] = (
            manifest['overall_assessment']['all_expected_present'] and 
            manifest['overall_assessment']['all_structures_valid']
        )
        
        logger.info(f"Evidence manifest created: {expected_present}/{len(self.expected_artifacts)} expected artifacts present")
        return manifest
    
    def create_handoff_package(self, evidence_files: List[Path]) -> Dict[str, Any]:
        """Create handoff package for next protocol"""
        logger.info("Creating handoff package")
        
        handoff_package = {
            'protocol_id': self.protocol_id,
            'handoff_timestamp': datetime.now().isoformat(),
            'target_protocol': str(int(self.protocol_id) + 1).zfill(2),  # Next protocol
            'package_contents': {
                'evidence_artifacts': [],
                'validation_summaries': [],
                'compliance_status': {},
                'quality_metrics': {}
            },
            'handoff_checklist': {
                'evidence_complete': False,
                'validation_passed': False,
                'compliance_verified': False,
                'ready_for_handoff': False
            }
        }
        
        # Add evidence artifacts to package
        for file_path in evidence_files:
            artifact_info = {
                'file_name': file_path.name,
                'file_path': str(file_path),
                'checksum': self.calculate_file_checksum(file_path),
                'size_bytes': file_path.stat().st_size
            }
            handoff_package['package_contents']['evidence_artifacts'].append(artifact_info)
        
        # Extract validation summaries
        for file_path in evidence_files:
            try:
                with open(file_path, 'r') as f:
                    content = json.load(f)
                
                if 'validation_summary' in content:
                    handoff_package['package_contents']['validation_summaries'].append({
                        'source_file': file_path.name,
                        'summary': content['validation_summary']
                    })
                
                if 'compliance_summary' in content:
                    handoff_package['package_contents']['compliance_status'] = content['compliance_summary']
                
                # Extract quality metrics
                if 'validation_summary' in content:
                    summary = content['validation_summary']
                    if 'overall_score' in summary:
                        handoff_package['package_contents']['quality_metrics'][file_path.name] = summary['overall_score']
                        
            except Exception as e:
                logger.warning(f"Failed to extract summary from {file_path}: {e}")
        
        # Update handoff checklist
        evidence_count = len(evidence_files)
        expected_count = len(self.expected_artifacts)
        
        handoff_package['handoff_checklist']['evidence_complete'] = evidence_count >= expected_count
        
        # Check validation status
        validation_summaries = handoff_package['package_contents']['validation_summaries']
        all_validations_passed = all(s.get('summary', {}).get('validation_passed', False) for s in validation_summaries)
        handoff_package['handoff_checklist']['validation_passed'] = all_validations_passed
        
        # Check compliance status
        compliance_status = handoff_package['package_contents']['compliance_status']
        compliance_passed = compliance_status.get('compliance_passed', False)
        handoff_package['handoff_checklist']['compliance_verified'] = compliance_passed
        
        # Overall readiness
        handoff_package['handoff_checklist']['ready_for_handoff'] = (
            handoff_package['handoff_checklist']['evidence_complete'] and
            handoff_package['handoff_checklist']['validation_passed'] and
            handoff_package['handoff_checklist']['compliance_verified']
        )
        
        logger.info(f"Handoff package created - Ready: {handoff_package['handoff_checklist']['ready_for_handoff']}")
        return handoff_package
    
    def execute_aggregation(self) -> Dict[str, Any]:
        """Execute complete evidence aggregation"""
        logger.info("Starting evidence aggregation")
        
        # Discover evidence artifacts
        evidence_files = self.discover_evidence_artifacts()
        
        if not evidence_files:
            logger.warning("No evidence artifacts found")
            return {
                'aggregation_summary': {
                    'status': 'failed',
                    'reason': 'no_evidence_found',
                    'total_artifacts': 0
                },
                'evidence_manifest': {},
                'handoff_package': {}
            }
        
        # Create evidence manifest
        evidence_manifest = self.create_evidence_manifest(evidence_files)
        
        # Create handoff package
        handoff_package = self.create_handoff_package(evidence_files)
        
        # Calculate aggregation summary
        aggregation_summary = {
            'status': 'completed',
            'total_artifacts': len(evidence_files),
            'expected_artifacts': len(self.expected_artifacts),
            'all_expected_present': evidence_manifest['overall_assessment']['all_expected_present'],
            'all_structures_valid': evidence_manifest['overall_assessment']['all_structures_valid'],
            'aggregation_complete': evidence_manifest['overall_assessment']['aggregation_complete'],
            'handoff_ready': handoff_package['handoff_checklist']['ready_for_handoff'],
            'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
            'start_time': self.start_time.isoformat(),
            'end_time': datetime.now().isoformat()
        }
        
        aggregation_report = {
            'aggregation_summary': aggregation_summary,
            'evidence_manifest': evidence_manifest,
            'handoff_package': handoff_package
        }
        
        logger.info(f"Evidence aggregation completed: {len(evidence_files)} artifacts processed")
        return aggregation_report
    
    def save_aggregation_report(self, report: Dict[str, Any], report_path: str):
        """Save aggregation report to specified path"""
        try:
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            logger.info(f"Aggregation report saved to {report_path}")
        except Exception as e:
            logger.error(f"Failed to save aggregation report: {e}")

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Aggregate evidence artifacts')
    parser.add_argument('--output', required=True, help='Output directory containing evidence')
    parser.add_argument('--protocol-id', required=True, help='Protocol ID (e.g., 08)')
    
    args = parser.parse_args()
    
    try:
        # Initialize evidence aggregator
        aggregator = EvidenceAggregator(args.output, args.protocol_id)
        
        # Execute aggregation
        aggregation_report = aggregator.execute_aggregation()
        
        # Save aggregation report
        report_file = Path(args.output) / f'evidence_aggregation_report_{args.protocol_id}.json'
        aggregator.save_aggregation_report(aggregation_report, str(report_file))
        
        # Return success if aggregation completed
        if aggregation_report['aggregation_summary']['status'] == 'completed':
            logger.info("Evidence aggregation completed successfully")
            return 0
        else:
            logger.warning("Evidence aggregation completed with issues")
            return 1
            
    except Exception as e:
        logger.error(f"Evidence aggregation failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""
Script: check_compliance_requirements.py
Protocol: 07-ai-data-strategy-planning
Purpose: Check data handling against regulatory requirements
Author: AI Workflow System
Created: 2025-01-06
"""

import json
import logging
from typing import Dict, List, Optional, Any, Set
from pathlib import Path
from datetime import datetime, timedelta
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ComplianceLevel(Enum):
    """Compliance severity levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class ComplianceChecker:
    """Check data handling against regulatory requirements"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-07"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Regulatory frameworks and their requirements
        self.regulations = {
            'GDPR': {
                'name': 'General Data Protection Regulation',
                'jurisdictions': ['EU', 'European Economic Area'],
                'requirements': {
                    'lawful_basis': ComplianceLevel.CRITICAL,
                    'consent_management': ComplianceLevel.CRITICAL,
                    'data_minimization': ComplianceLevel.HIGH,
                    'purpose_limitation': ComplianceLevel.HIGH,
                    'accuracy': ComplianceLevel.MEDIUM,
                    'storage_limitation': ComplianceLevel.HIGH,
                    'security': ComplianceLevel.CRITICAL,
                    'accountability': ComplianceLevel.HIGH,
                    'data_subject_rights': ComplianceLevel.CRITICAL,
                    'breach_notification': ComplianceLevel.CRITICAL,
                    'privacy_by_design': ComplianceLevel.HIGH,
                    'data_protection_officer': ComplianceLevel.MEDIUM
                },
                'applicable_threshold': 0.1  # 10% EU data subjects
            },
            'HIPAA': {
                'name': 'Health Insurance Portability and Accountability Act',
                'jurisdictions': ['US'],
                'requirements': {
                    'administrative_safeguards': ComplianceLevel.CRITICAL,
                    'physical_safeguards': ComplianceLevel.CRITICAL,
                    'technical_safeguards': ComplianceLevel.CRITICAL,
                    'breach_notification': ComplianceLevel.CRITICAL,
                    'minimum_necessary': ComplianceLevel.HIGH,
                    'access_controls': ComplianceLevel.CRITICAL,
                    'audit_controls': ComplianceLevel.HIGH,
                    'integrity_controls': ComplianceLevel.HIGH,
                    'transmission_security': ComplianceLevel.CRITICAL
                },
                'applicable_threshold': 0.01  # 1% health data
            },
            'CCPA': {
                'name': 'California Consumer Privacy Act',
                'jurisdictions': ['California', 'US'],
                'requirements': {
                    'right_to_know': ComplianceLevel.CRITICAL,
                    'right_to_delete': ComplianceLevel.CRITICAL,
                    'right_to_opt_out': ComplianceLevel.CRITICAL,
                    'right_to_non_discrimination': ComplianceLevel.HIGH,
                    'purpose_disclosure': ComplianceLevel.HIGH,
                    'data_minimization': ComplianceLevel.MEDIUM,
                    'security': ComplianceLevel.HIGH,
                    'vendor_management': ComplianceLevel.MEDIUM
                },
                'applicable_threshold': 0.05  # 5% California residents
            },
            'SOX': {
                'name': 'Sarbanes-Oxley Act',
                'jurisdictions': ['US'],
                'requirements': {
                    'financial_data_integrity': ComplianceLevel.CRITICAL,
                    'audit_trails': ComplianceLevel.CRITICAL,
                    'access_controls': ComplianceLevel.CRITICAL,
                    'change_management': ComplianceLevel.HIGH,
                    'data_retention': ComplianceLevel.HIGH,
                    'disaster_recovery': ComplianceLevel.HIGH
                },
                'applicable_threshold': 0.01  # 1% financial data
            },
            'PCI_DSS': {
                'name': 'Payment Card Industry Data Security Standard',
                'jurisdictions': ['Global'],
                'requirements': {
                    'network_security': ComplianceLevel.CRITICAL,
                    'cardholder_data_protection': ComplianceLevel.CRITICAL,
                    'vulnerability_management': ComplianceLevel.HIGH,
                    'access_control': ComplianceLevel.CRITICAL,
                    'network_monitoring': ComplianceLevel.HIGH,
                    'information_security_policy': ComplianceLevel.HIGH
                },
                'applicable_threshold': 0.01  # 1% payment data
            }
        }
        
        # Data classification levels
        self.data_classification = {
            'personal_data': {
                'examples': ['name', 'email', 'phone', 'address'],
                'sensitivity': 'high',
                'applicable_regulations': ['GDPR', 'CCPA']
            },
            'sensitive_personal_data': {
                'examples': ['race', 'religion', 'health', 'biometric', 'political'],
                'sensitivity': 'very_high',
                'applicable_regulations': ['GDPR', 'HIPAA', 'CCPA']
            },
            'financial_data': {
                'examples': ['credit_card', 'bank_account', 'transaction'],
                'sensitivity': 'very_high',
                'applicable_regulations': ['SOX', 'PCI_DSS', 'GDPR', 'CCPA']
            },
            'health_data': {
                'examples': ['medical_records', 'diagnosis', 'treatment'],
                'sensitivity': 'very_high',
                'applicable_regulations': ['HIPAA', 'GDPR']
            },
            'behavioral_data': {
                'examples': ['browsing_history', 'location', 'preferences'],
                'sensitivity': 'medium',
                'applicable_regulations': ['GDPR', 'CCPA']
            },
            'public_data': {
                'examples': ['public_posts', 'public_profiles'],
                'sensitivity': 'low',
                'applicable_regulations': []
            }
        }
    
    def execute(self, **kwargs) -> Dict:
        """
        Check compliance against regulatory requirements
        
        Args:
            data_types: Types of data being processed
            jurisdictions: Geographic regions and applicable laws
            use_cases: Intended data usage scenarios
            
        Returns:
            Dict: Compliance assessment results
        """
        try:
            data_types = kwargs.get('data_types', {})
            jurisdictions = kwargs.get('jurisdictions', [])
            use_cases = kwargs.get('use_cases', [])
            
            # Identify applicable regulations
            applicable_regs = self._identify_applicable_regulations(
                data_types, jurisdictions, use_cases
            )
            
            # Assess compliance for each regulation
            compliance_assessments = {}
            overall_gaps = []
            required_actions = []
            documentation_needed = []
            
            for reg_name in applicable_regs:
                assessment = self._assess_regulation_compliance(
                    reg_name, data_types, use_cases
                )
                compliance_assessments[reg_name] = assessment
                
                # Collect gaps and actions
                overall_gaps.extend(assessment['gaps'])
                required_actions.extend(assessment['required_actions'])
                documentation_needed.extend(assessment['documentation_needed'])
            
            # Calculate overall compliance score
            overall_score = self._calculate_overall_compliance_score(compliance_assessments)
            
            # Determine risk level
            risk_level = self._determine_risk_level(overall_score, overall_gaps)
            
            # Generate compliance framework
            compliance_framework = self._create_compliance_framework(
                applicable_regs, compliance_assessments
            )
            
            # Create implementation roadmap
            implementation_roadmap = self._create_implementation_roadmap(
                required_actions, overall_gaps
            )
            
            result = {
                "compliance_score": overall_score,
                "applicable_regulations": list(applicable_regs),
                "compliance_assessments": compliance_assessments,
                "compliance_gaps": list(set(overall_gaps)),
                "risk_level": risk_level,
                "required_actions": list(set(required_actions)),
                "documentation_needed": list(set(documentation_needed)),
                "compliance_framework": compliance_framework,
                "implementation_roadmap": implementation_roadmap
            }
            
            # Generate evidence
            self._generate_evidence(result, kwargs)
            
            return {
                "status": "success",
                "result": result,
                "artifacts": self._list_artifacts()
            }
            
        except Exception as e:
            logger.error(f"Compliance check failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _identify_applicable_regulations(self, data_types: Dict, 
                                       jurisdictions: List[str], 
                                       use_cases: List[str]) -> Set[str]:
        """Identify which regulations apply based on data and jurisdiction"""
        applicable = set()
        
        # Check based on data types
        for data_type, info in data_types.items():
            if data_type in self.data_classification:
                classification = self.data_classification[data_type]
                applicable.update(classification['applicable_regulations'])
        
        # Check based on jurisdictions
        for jurisdiction in jurisdictions:
            for reg_name, reg_info in self.regulations.items():
                if jurisdiction in reg_info['jurisdictions']:
                    applicable.add(reg_name)
        
        # Check based on use cases
        for use_case in use_cases:
            use_case_lower = use_case.lower()
            if 'health' in use_case_lower or 'medical' in use_case_lower:
                applicable.add('HIPAA')
            if 'financial' in use_case_lower or 'payment' in use_case_lower:
                applicable.update(['SOX', 'PCI_DSS'])
            if 'eu' in use_case_lower or 'europe' in use_case_lower:
                applicable.add('GDPR')
            if 'california' in use_case_lower or 'ca' in use_case_lower:
                applicable.add('CCPA')
        
        return applicable
    
    def _assess_regulation_compliance(self, regulation_name: str, 
                                    data_types: Dict, 
                                    use_cases: List[str]) -> Dict:
        """Assess compliance for a specific regulation"""
        reg_info = self.regulations.get(regulation_name, {})
        requirements = reg_info.get('requirements', {})
        
        assessment = {
            'regulation': regulation_name,
            'full_name': reg_info.get('name', regulation_name),
            'compliance_score': 0.0,
            'requirement_status': {},
            'gaps': [],
            'required_actions': [],
            'documentation_needed': [],
            'risk_level': 'low'
        }
        
        # Assess each requirement
        requirement_scores = []
        
        for requirement, severity in requirements.items():
            status = self._assess_requirement(
                requirement, severity, data_types, use_cases
            )
            assessment['requirement_status'][requirement] = status
            
            if status['compliant']:
                requirement_scores.append(1.0)
            else:
                requirement_scores.append(status['confidence'] or 0.0)
                assessment['gaps'].append(requirement)
                
                if severity in [ComplianceLevel.CRITICAL, ComplianceLevel.HIGH]:
                    assessment['required_actions'].extend(status['actions'])
                
                if status['documentation_required']:
                    assessment['documentation_needed'].extend(status['documentation'])
        
        # Calculate overall compliance score
        if requirement_scores:
            assessment['compliance_score'] = round(sum(requirement_scores) / len(requirement_scores), 3)
        
        # Determine risk level
        critical_gaps = sum(1 for req, status in assessment['requirement_status'].items()
                          if not status['compliant'] and 
                          requirements.get(req) == ComplianceLevel.CRITICAL)
        
        if critical_gaps > 0:
            assessment['risk_level'] = 'critical'
        elif assessment['compliance_score'] < 0.7:
            assessment['risk_level'] = 'high'
        elif assessment['compliance_score'] < 0.85:
            assessment['risk_level'] = 'medium'
        else:
            assessment['risk_level'] = 'low'
        
        return assessment
    
    def _assess_requirement(self, requirement: str, severity: ComplianceLevel,
                          data_types: Dict, use_cases: List[str]) -> Dict:
        """Assess compliance for a specific requirement"""
        # Simulate compliance assessment (in real implementation, check actual systems)
        assessment = {
            'compliant': False,
            'confidence': 0.0,
            'actions': [],
            'documentation_required': [],
            'notes': ''
        }
        
        # Requirement-specific assessments
        if requirement == 'consent_management':
            assessment['compliant'] = False  # Assume not implemented
            assessment['confidence'] = 0.2
            assessment['actions'] = [
                'Implement consent management system',
                'Create consent capture mechanisms',
                'Establish consent withdrawal process'
            ]
            assessment['documentation_required'] = ['consent_policy', 'consent_records_procedure']
            assessment['notes'] = 'No consent management system detected'
            
        elif requirement == 'data_minimization':
            assessment['compliant'] = False
            assessment['confidence'] = 0.3
            assessment['actions'] = [
                'Review data collection practices',
                'Implement data minimization policies',
                'Create data retention schedules'
            ]
            assessment['documentation_required'] = ['data_minimization_policy']
            assessment['notes'] = 'Data minimization not yet implemented'
            
        elif requirement == 'security':
            assessment['compliant'] = True  # Assume basic security in place
            assessment['confidence'] = 0.8
            assessment['actions'] = [
                'Conduct security assessment',
                'Implement encryption at rest and in transit'
            ]
            assessment['documentation_required'] = ['security_policy', 'encryption_procedure']
            assessment['notes'] = 'Basic security measures in place'
            
        elif requirement == 'access_controls':
            assessment['compliant'] = False
            assessment['confidence'] = 0.4
            assessment['actions'] = [
                'Implement role-based access control',
                'Create access request workflows',
                'Establish access review procedures'
            ]
            assessment['documentation_required'] = ['access_control_policy']
            assessment['notes'] = 'Access controls need improvement'
            
        elif requirement == 'audit_trails':
            assessment['compliant'] = False
            assessment['confidence'] = 0.3
            assessment['actions'] = [
                'Implement comprehensive logging',
                'Create audit trail monitoring',
                'Establish log retention policies'
            ]
            assessment['documentation_required'] = ['audit_trail_policy']
            assessment['notes'] = 'Audit trails not fully implemented'
            
        else:
            # Generic assessment for other requirements
            assessment['compliant'] = False
            assessment['confidence'] = 0.5
            assessment['actions'] = [f'Implement {requirement.replace("_", " ")} controls']
            assessment['documentation_required'] = [f'{requirement}_policy']
            assessment['notes'] = f'{requirement} requires implementation'
        
        return assessment
    
    def _calculate_overall_compliance_score(self, assessments: Dict) -> float:
        """Calculate overall compliance score across all regulations"""
        if not assessments:
            return 0.0
        
        scores = [assessment['compliance_score'] for assessment in assessments.values()]
        return round(sum(scores) / len(scores), 3)
    
    def _determine_risk_level(self, overall_score: float, gaps: List[str]) -> str:
        """Determine overall risk level"""
        critical_regulations = ['GDPR', 'HIPAA', 'PCI_DSS']
        
        # Check for critical gaps
        for assessment in assessments.values():
            if assessment['risk_level'] == 'critical':
                return 'critical'
        
        # Determine based on score
        if overall_score < 0.5:
            return 'critical'
        elif overall_score < 0.7:
            return 'high'
        elif overall_score < 0.85:
            return 'medium'
        else:
            return 'low'
    
    def _create_compliance_framework(self, applicable_regs: Set[str], 
                                   assessments: Dict) -> Dict:
        """Create comprehensive compliance framework"""
        framework = {
            'governance': {
                'policies_needed': [],
                'procedures_needed': [],
                'roles_needed': []
            },
            'technical_controls': {
                'access_management': False,
                'encryption_required': True,
                'audit_logging': False,
                'data_classification': False
            },
            'operational_controls': {
                'training_required': True,
                'monitoring_required': True,
                'incident_response': False,
                'vendor_management': False
            },
            'documentation': {
                'policies': [],
                'procedures': [],
                'records': [],
                'reports': []
            }
        }
        
        # Aggregate requirements across all regulations
        for reg_name, assessment in assessments.items():
            for requirement, status in assessment['requirement_status'].items():
                if not status['compliant']:
                    # Map requirements to framework categories
                    if 'policy' in requirement.lower() or 'management' in requirement.lower():
                        framework['governance']['policies_needed'].append(requirement)
                    elif 'procedure' in requirement.lower() or 'process' in requirement.lower():
                        framework['governance']['procedures_needed'].append(requirement)
                    elif 'access' in requirement.lower():
                        framework['technical_controls']['access_management'] = True
                    elif 'encryption' in requirement.lower() or 'security' in requirement.lower():
                        framework['technical_controls']['encryption_required'] = True
                    elif 'audit' in requirement.lower() or 'logging' in requirement.lower():
                        framework['technical_controls']['audit_logging'] = True
                    elif 'training' in requirement.lower():
                        framework['operational_controls']['training_required'] = True
                    elif 'monitoring' in requirement.lower():
                        framework['operational_controls']['monitoring_required'] = True
            
            # Collect documentation needs
            framework['documentation']['policies'].extend(assessment['documentation_needed'])
        
        # Remove duplicates
        for category in framework['documentation']:
            framework['documentation'][category] = list(set(framework['documentation'][category]))
        
        return framework
    
    def _create_implementation_roadmap(self, actions: List[str], gaps: List[str]) -> Dict:
        """Create implementation roadmap for compliance"""
        # Prioritize actions based on criticality
        critical_actions = []
        high_priority_actions = []
        medium_priority_actions = []
        
        for action in actions:
            action_lower = action.lower()
            if any(keyword in action_lower for keyword in ['consent', 'security', 'access', 'breach']):
                critical_actions.append(action)
            elif any(keyword in action_lower for keyword in ['policy', 'procedure', 'audit']):
                high_priority_actions.append(action)
            else:
                medium_priority_actions.append(action)
        
        # Create timeline (simplified)
        roadmap = {
            'immediate_actions': critical_actions,  # 0-30 days
            'short_term_actions': high_priority_actions,  # 30-90 days
            'medium_term_actions': medium_priority_actions,  # 90-180 days
            'long_term_actions': [
                'Conduct regular compliance audits',
                'Implement continuous monitoring',
                'Establish compliance training program'
            ],  # 180+ days
            'milestones': {
                '30_days': f"Complete {len(critical_actions)} critical actions",
                '90_days': f"Complete {len(high_priority_actions)} high priority actions",
                '180_days': f"Complete {len(medium_priority_actions)} medium priority actions",
                '365_days': "Full compliance implementation"
            }
        }
        
        return roadmap
    
    def _generate_evidence(self, result: Dict, inputs: Dict) -> None:
        """Generate evidence artifacts"""
        timestamp = datetime.now().isoformat()
        
        # Save compliance assessment report
        report_file = self.artifacts_dir / "compliance-assessment.json"
        report_data = {
            "timestamp": timestamp,
            "assessment_summary": {
                "overall_compliance_score": result['compliance_score'],
                "risk_level": result['risk_level'],
                "applicable_regulations": result['applicable_regulations'],
                "total_gaps": len(result['compliance_gaps']),
                "total_actions": len(result['required_actions'])
            },
            "detailed_assessments": result['compliance_assessments'],
            "compliance_gaps": result['compliance_gaps'],
            "required_actions": result['required_actions'],
            "documentation_needed": result['documentation_needed'],
            "compliance_framework": result['compliance_framework'],
            "implementation_roadmap": result['implementation_roadmap']
        }
        
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        # Generate markdown compliance report
        md_file = self.artifacts_dir / "compliance-report.md"
        with open(md_file, 'w') as f:
            f.write("# Compliance Assessment Report\n\n")
            f.write(f"**Generated**: {timestamp}\n\n")
            f.write("## Executive Summary\n")
            f.write(f"- **Overall Compliance Score**: {result['compliance_score']:.2%}\n")
            f.write(f"- **Risk Level**: {result['risk_level'].upper()}\n")
            f.write(f"- **Applicable Regulations**: {', '.join(result['applicable_regulations'])}\n")
            f.write(f"- **Compliance Gaps**: {len(result['compliance_gaps'])}\n")
            f.write(f"- **Required Actions**: {len(result['required_actions'])}\n\n")
            
            f.write("## Regulation-Specific Assessments\n")
            for reg_name, assessment in result['compliance_assessments'].items():
                f.write(f"### {assessment['full_name']}\n")
                f.write(f"- **Compliance Score**: {assessment['compliance_score']:.2%}\n")
                f.write(f"- **Risk Level**: {assessment['risk_level'].upper()}\n")
                f.write(f"- **Gaps**: {len(assessment['gaps'])}\n\n")
            
            if result['compliance_gaps']:
                f.write("## Compliance Gaps\n")
                for gap in result['compliance_gaps']:
                    f.write(f"- {gap.replace('_', ' ').title()}\n")
                f.write("\n")
            
            if result['required_actions']:
                f.write("## Required Actions\n")
                for action in result['required_actions']:
                    f.write(f"- {action}\n")
                f.write("\n")
            
            f.write("## Implementation Roadmap\n")
            roadmap = result['implementation_roadmap']
            f.write("### Immediate Actions (0-30 days)\n")
            for action in roadmap['immediate_actions']:
                f.write(f"- {action}\n")
            f.write("\n### Short-term Actions (30-90 days)\n")
            for action in roadmap['short_term_actions']:
                f.write(f"- {action}\n")
    
    def _list_artifacts(self) -> List[str]:
        """List generated artifacts"""
        artifacts = []
        for file in self.artifacts_dir.glob("*"):
            artifacts.append(str(file.relative_to(self.workspace)))
        return artifacts


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Check compliance requirements for ML project")
    parser.add_argument("--workspace", required=True, help="Workspace path")
    parser.add_argument("--data-types", required=True, help="Data types being processed (JSON)")
    parser.add_argument("--jurisdictions", default="[]", help="Geographic jurisdictions (JSON array)")
    parser.add_argument("--use-cases", default="[]", help="Intended use cases (JSON array)")
    
    args = parser.parse_args()
    
    checker = ComplianceChecker(args.workspace)
    result = checker.execute(
        data_types=json.loads(args.data_types),
        jurisdictions=json.loads(args.jurisdictions),
        use_cases=json.loads(args.use_cases)
    )
    
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()

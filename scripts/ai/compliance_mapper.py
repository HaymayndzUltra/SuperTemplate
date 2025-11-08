#!/usr/bin/env python3
"""
Compliance Mapper for AI Data Strategy Planning

Maps datasets to applicable privacy and compliance regulations,
generating required controls and documentation.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Set
from datetime import datetime

class ComplianceMapper:
    """Map datasets to compliance requirements and controls"""
    
    def __init__(self):
        # Regulation definitions
        self.regulations = {
            'GDPR': {
                'name': 'General Data Protection Regulation',
                'scope': 'EU citizens data',
                'key_requirements': [
                    'lawful_basis_for_processing',
                    'data_minimization',
                    'purpose_limitation',
                    'storage_limitation',
                    'accuracy',
                    'integrity_confidentiality',
                    'accountability',
                    'data_subject_rights'
                ],
                'data_types': ['personal_data', 'special_category_data', 'criminal_data'],
                'sensitivity_levels': ['high', 'very_high']
            },
            'HIPAA': {
                'name': 'Health Insurance Portability and Accountability Act',
                'scope': 'US health information',
                'key_requirements': [
                    'administrative_safeguards',
                    'physical_safeguards',
                    'technical_safeguards',
                    'organizational_requirements',
                    'policies_procedures',
                    'breach_notification'
                ],
                'data_types': ['phi', 'electronic_phi'],
                'sensitivity_levels': ['high', 'very_high']
            },
            'CCPA': {
                'name': 'California Consumer Privacy Act',
                'scope': 'California residents data',
                'key_requirements': [
                    'right_to_know',
                    'right_to_delete',
                    'right_to_opt_out',
                    'right_to_non_discrimination',
                    'business_transparency'
                ],
                'data_types': ['personal_information', 'sensitive_personal_information'],
                'sensitivity_levels': ['medium', 'high', 'very_high']
            },
            'SOX': {
                'name': 'Sarbanes-Oxley Act',
                'scope': 'Financial data and records',
                'key_requirements': [
                    'data_integrity',
                    'access_controls',
                    'audit_trails',
                    'retention_policies',
                    'segregation_of_duties'
                ],
                'data_types': ['financial_data', 'audit_records'],
                'sensitivity_levels': ['high', 'very_high']
            },
            'PCI_DSS': {
                'name': 'Payment Card Industry Data Security Standard',
                'scope': 'Payment card data',
                'key_requirements': [
                    'network_security',
                    'data_protection',
                    'vulnerability_management',
                    'access_control',
                    'monitoring_testing',
                    'information_security_policy'
                ],
                'data_types': ['cardholder_data', 'sensitive_authentication_data'],
                'sensitivity_levels': ['very_high']
            }
        }
        
        # Data type to regulation mapping
        self.data_type_regulations = {
            'personal_data': ['GDPR', 'CCPA'],
            'special_category_data': ['GDPR'],
            'health_data': ['HIPAA'],
            'phi': ['HIPAA'],
            'financial_data': ['SOX'],
            'payment_data': ['PCI_DSS'],
            'cardholder_data': ['PCI_DSS'],
            'biometric_data': ['GDPR', 'CCPA'],
            'geolocation_data': ['GDPR', 'CCPA'],
            'children_data': ['GDPR', 'CCPA'],
            'public_data': [],
            'synthetic_data': [],
            'aggregated_data': []
        }
        
        # Required controls by sensitivity
        self.sensitivity_controls = {
            'low': [
                'basic_access_control',
                'data_classification',
                'retention_policy'
            ],
            'medium': [
                'role_based_access',
                'encryption_at_rest',
                'audit_logging',
                'data_backup',
                'incident_response'
            ],
            'high': [
                'end_to_end_encryption',
                'strict_access_controls',
                'comprehensive_audit_trail',
                'data_loss_prevention',
                'regular_security_assessments',
                'privacy_impact_assessment'
            ],
            'very_high': [
                'advanced_encryption',
                'multi_factor_authentication',
                'real_time_monitoring',
                'privacy_by_design',
                'data_protection_officer',
                'regular_compliance_audits',
                'breach_detection_system'
            ]
        }

    def classify_data_type(self, dataset_info: Dict[str, Any]) -> List[str]:
        """Classify dataset into regulatory data types"""
        data_types = []
        fields = dataset_info.get('fields', [])
        description = dataset_info.get('description', '').lower()
        
        # Field-based classification
        field_patterns = {
            'personal_data': ['name', 'email', 'phone', 'address', 'id'],
            'health_data': ['medical', 'health', 'diagnosis', 'treatment', 'patient'],
            'financial_data': ['account', 'transaction', 'payment', 'credit', 'salary'],
            'biometric_data': ['fingerprint', 'face', 'iris', 'voice', 'dna'],
            'geolocation_data': ['location', 'gps', 'coordinates', 'address']
        }
        
        for data_type, patterns in field_patterns.items():
            if any(pattern in ' '.join(fields).lower() for pattern in patterns):
                data_types.append(data_type)
            elif any(pattern in description for pattern in patterns):
                data_types.append(data_type)
        
        # Default classification
        if not data_types:
            data_types.append('public_data')
            
        return list(set(data_types))

    def determine_sensitivity(self, dataset_info: Dict[str, Any], data_types: List[str]) -> str:
        """Determine sensitivity level based on data types and context"""
        # Base sensitivity from data types
        sensitivity_rules = {
            'special_category_data': 'very_high',
            'phi': 'very_high',
            'cardholder_data': 'very_high',
            'biometric_data': 'very_high',
            'financial_data': 'high',
            'personal_data': 'medium',
            'health_data': 'high',
            'geolocation_data': 'medium',
            'children_data': 'very_high',
            'public_data': 'low',
            'synthetic_data': 'low',
            'aggregated_data': 'low'
        }
        
        max_sensitivity = 'low'
        for data_type in data_types:
            type_sensitivity = sensitivity_rules.get(data_type, 'medium')
            if self._compare_sensitivity(type_sensitivity, max_sensitivity) > 0:
                max_sensitivity = type_sensitivity
        
        # Adjust based on volume and access
        volume = dataset_info.get('volume', 'medium')
        access_level = dataset_info.get('access_level', 'internal')
        
        if volume == 'large' and access_level == 'external':
            if self._compare_sensitivity(max_sensitivity, 'high') < 0:
                max_sensitivity = 'high'
        
        return max_sensitivity

    def _compare_sensitivity(self, s1: str, s2: str) -> int:
        """Compare two sensitivity levels, return >0 if s1 > s2"""
        levels = {'low': 1, 'medium': 2, 'high': 3, 'very_high': 4}
        return levels[s1] - levels[s2]

    def map_applicable_regulations(self, data_types: List[str], sensitivity: str) -> List[str]:
        """Map data types to applicable regulations"""
        regulations = set()
        
        for data_type in data_types:
            type_regs = self.data_type_regulations.get(data_type, [])
            regulations.update(type_regs)
        
        # Add regulations based on sensitivity
        if sensitivity in ['high', 'very_high']:
            # High sensitivity data often falls under multiple regulations
            regulations.add('GDPR')  # Default high-standard regulation
        
        return sorted(list(regulations))

    def generate_required_controls(self, regulations: List[str], sensitivity: str) -> Dict[str, Any]:
        """Generate required controls based on regulations and sensitivity"""
        base_controls = self.sensitivity_controls.get(sensitivity, [])
        
        # Regulation-specific controls
        regulation_controls = {
            'GDPR': [
                'data_protection_impact_assessment',
                'data_subject_rights_procedures',
                'data_breach_notification_72h',
                'privacy_by_design',
                'data_protection_officer'
            ],
            'HIPAA': [
                'hipaa_security_rule_compliance',
                'business_associate_agreements',
                'minimum_necessary_standard',
                'hipaa_breach_notification',
                'security_officer'
            ],
            'CCPA': [
                'consumer_rights_implementation',
                'do_not_sell_procedures',
                'privacy_policy_disclosure',
                'data_inventory_mapping',
                'ccpa_opt_out_mechanisms'
            ],
            'SOX': [
                'sox_compliance_controls',
                'financial_data_integrity',
                'audit_trail_immutable',
                'segregation_of_duties',
                'sox_retention_policies'
            ],
            'PCI_DSS': [
                'pci_dss_compliance',
                'card_data_encryption',
                'network_segmentation',
                'vulnerability_scanning',
                'pci_audit_logging'
            ]
        }
        
        # Combine controls
        all_controls = set(base_controls)
        for reg in regulations:
            all_controls.update(regulation_controls.get(reg, []))
        
        return {
            'base_controls': base_controls,
            'regulation_specific': {reg: regulation_controls.get(reg, []) for reg in regulations},
            'all_controls': sorted(list(all_controls)),
            'control_categories': self._categorize_controls(all_controls)
        }

    def _categorize_controls(self, controls: Set[str]) -> Dict[str, List[str]]:
        """Categorize controls by type"""
        categories = {
            'access_control': [],
            'encryption': [],
            'audit_monitoring': [],
            'policy_procedure': [],
            'technical': [],
            'administrative': []
        }
        
        control_patterns = {
            'access_control': ['access', 'authentication', 'authorization'],
            'encryption': ['encryption', 'crypto'],
            'audit_monitoring': ['audit', 'logging', 'monitoring', 'trail'],
            'policy_procedure': ['policy', 'procedure', 'agreement'],
            'technical': ['network', 'system', 'technical'],
            'administrative': ['officer', 'assessment', 'training']
        }
        
        for control in controls:
            categorized = False
            for category, patterns in control_patterns.items():
                if any(pattern in control.lower() for pattern in patterns):
                    categories[category].append(control)
                    categorized = True
                    break
            if not categorized:
                categories['technical'].append(control)  # Default
        
        return categories

    def assess_compliance_risk(self, regulations: List[str], sensitivity: str, 
                             dataset_info: Dict[str, Any]) -> Dict[str, Any]:
        """Assess compliance risk level"""
        risk_factors = {
            'regulation_complexity': len(regulations),
            'sensitivity_level': sensitivity,
            'data_volume': dataset_info.get('volume', 'medium'),
            'access_scope': dataset_info.get('access_level', 'internal'),
            'third_party_sharing': dataset_info.get('third_party_sharing', False)
        }
        
        # Calculate risk score
        risk_score = 0
        if len(regulations) >= 3:
            risk_score += 2
        elif len(regulations) >= 2:
            risk_score += 1
            
        sensitivity_scores = {'low': 0, 'medium': 1, 'high': 2, 'very_high': 3}
        risk_score += sensitivity_scores.get(sensitivity, 1)
        
        if risk_factors['data_volume'] == 'large':
            risk_score += 1
        if risk_factors['access_scope'] == 'external':
            risk_score += 1
        if risk_factors['third_party_sharing']:
            risk_score += 1
        
        # Determine risk level
        if risk_score >= 6:
            risk_level = 'very_high'
        elif risk_score >= 4:
            risk_level = 'high'
        elif risk_score >= 2:
            risk_level = 'medium'
        else:
            risk_level = 'low'
        
        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'risk_factors': risk_factors,
            'mitigation_priority': 'immediate' if risk_level in ['high', 'very_high'] else 'planned'
        }

    def process_dataset(self, dataset: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single dataset and map compliance requirements"""
        dataset_id = dataset.get('dataset_id', dataset.get('dataset_name', 'UNKNOWN'))
        
        # Classify data types
        data_types = self.classify_data_type(dataset)
        
        # Determine sensitivity
        sensitivity = self.determine_sensitivity(dataset, data_types)
        
        # Map applicable regulations
        regulations = self.map_applicable_regulations(data_types, sensitivity)
        
        # Generate required controls
        controls = self.generate_required_controls(regulations, sensitivity)
        
        # Assess compliance risk
        risk_assessment = self.assess_compliance_risk(regulations, sensitivity, dataset)
        
        return {
            'dataset_id': dataset_id,
            'dataset_name': dataset.get('dataset_name', dataset_id),
            'data_types': data_types,
            'sensitivity_level': sensitivity,
            'applicable_regulations': regulations,
            'required_controls': controls,
            'risk_assessment': risk_assessment,
            'recommendations': self._generate_dataset_recommendations(
                data_types, sensitivity, regulations, risk_assessment)
        }

    def _generate_dataset_recommendations(self, data_types: List[str], sensitivity: str,
                                        regulations: List[str], risk_assessment: Dict[str, Any]) -> List[str]:
        """Generate compliance recommendations for a dataset"""
        recommendations = []
        
        if risk_assessment['risk_level'] in ['high', 'very_high']:
            recommendations.append("Conduct privacy impact assessment before processing")
            recommendations.append("Implement enhanced monitoring and alerting")
        
        if 'GDPR' in regulations:
            recommendations.append("Establish data subject rights request procedures")
            
        if 'HIPAA' in regulations:
            recommendations.append("Execute business associate agreements with all partners")
            
        if sensitivity == 'very_high':
            recommendations.append("Consider data anonymization or pseudonymization")
            recommendations.append("Implement zero-trust security model")
        
        if len(regulations) > 2:
            recommendations.append("Appoint dedicated compliance officer for this dataset")
        
        return recommendations

    def process_datasets(self, datasets: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Process multiple datasets and generate comprehensive compliance mapping"""
        results = []
        regulation_summary = {}
        sensitivity_summary = {}
        
        for dataset in datasets:
            try:
                result = self.process_dataset(dataset)
                results.append(result)
                
                # Update summaries
                for reg in result['applicable_regulations']:
                    regulation_summary[reg] = regulation_summary.get(reg, 0) + 1
                
                sensitivity = result['sensitivity_level']
                sensitivity_summary[sensitivity] = sensitivity_summary.get(sensitivity, 0) + 1
                
            except Exception as e:
                print(f"Error processing dataset {dataset.get('dataset_id', 'unknown')}: {e}")
                continue
        
        # Generate overall assessment
        overall_risk = self._assess_overall_risk(results)
        
        return {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_datasets': len(datasets),
                'processed_datasets': len(results),
                'regulation_coverage': regulation_summary,
                'sensitivity_distribution': sensitivity_summary,
                'overall_risk_level': overall_risk
            },
            'dataset_compliance': results,
            'control_framework': self._generate_control_framework_summary(results)
        }

    def _assess_overall_risk(self, results: List[Dict[str, Any]]) -> str:
        """Assess overall compliance risk across all datasets"""
        if not results:
            return 'low'
        
        risk_levels = [r['risk_assessment']['risk_level'] for r in results]
        
        if any(level == 'very_high' for level in risk_levels):
            return 'very_high'
        elif any(level == 'high' for level in risk_levels):
            return 'high'
        elif any(level == 'medium' for level in risk_levels):
            return 'medium'
        else:
            return 'low'

    def _generate_control_framework_summary(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate summary of required controls across all datasets"""
        all_controls = set()
        control_frequency = {}
        
        for result in results:
            controls = result['required_controls']['all_controls']
            all_controls.update(controls)
            
            for control in controls:
                control_frequency[control] = control_frequency.get(control, 0) + 1
        
        # Prioritize controls by frequency
        prioritized_controls = sorted(
            control_frequency.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        return {
            'total_unique_controls': len(all_controls),
            'most_common_controls': prioritized_controls[:10],
            'control_frequency': control_frequency,
            'control_categories': self._categorize_controls(all_controls)
        }

def main():
    parser = argparse.ArgumentParser(description='Map compliance requirements to datasets')
    parser.add_argument('--datasets', required=True, help='Input JSON file with datasets')
    parser.add_argument('--output', required=True, help='Output JSON file with compliance mapping')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Load datasets
    try:
        with open(args.datasets, 'r') as f:
            data = json.load(f)
        datasets = data.get('datasets', []) if isinstance(data, dict) else data
    except Exception as e:
        print(f"Error loading datasets file: {e}")
        sys.exit(1)
    
    if not datasets:
        print("No datasets found in input file")
        sys.exit(1)
    
    # Map compliance requirements
    mapper = ComplianceMapper()
    results = mapper.process_datasets(datasets)
    
    # Save results
    try:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
            
        if args.verbose:
            print(f"Mapped compliance for {results['summary']['processed_datasets']} datasets")
            print(f"Overall risk level: {results['summary']['overall_risk_level']}")
            print(f"Total controls required: {results['control_framework']['total_unique_controls']}")
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error saving results: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

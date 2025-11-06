#!/usr/bin/env python3
"""
Validator for Protocol 17: AI Model Explainability & Interpretability

This script validates that all explainability requirements are met including:
- Global interpretability
- Local explanations (SHAP, LIME)
- Stakeholder communication materials
- Regulatory compliance documentation
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import pickle

class Protocol17Validator:
    """Validator for AI Model Explainability & Interpretability protocol."""
    
    def __init__(self, evidence_path: str):
        """
        Initialize validator.
        
        Args:
            evidence_path: Path to protocol 17 evidence directory
        """
        self.evidence_path = Path(evidence_path)
        self.validation_results = {
            'protocol': 'Protocol 17: AI Model Explainability & Interpretability',
            'gates': {},
            'overall_status': 'PENDING'
        }
    
    def validate_gate_1_explainability_coverage(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 1: Explainability Coverage
        
        Requirements:
        - Global interpretability documented
        - Local explanations available for all predictions
        - SHAP values calculated and validated
        - LIME explanations generated and tested
        """
        issues = []
        
        # Check for SHAP values
        shap_file = self.evidence_path / 'artifacts' / 'shap-values.pkl'
        
        if not shap_file.exists():
            issues.append("Missing shap-values.pkl file")
        else:
            try:
                # Validate SHAP file can be loaded
                with open(shap_file, 'rb') as f:
                    shap_data = pickle.load(f)
                
                if not isinstance(shap_data, (dict, list, tuple)):
                    issues.append("Invalid SHAP values format")
            except Exception as e:
                issues.append(f"Error loading SHAP values: {str(e)}")
        
        # Check for LIME explainer
        lime_file = self.evidence_path / 'artifacts' / 'lime-explainer.pkl'
        
        if not lime_file.exists():
            issues.append("Missing lime-explainer.pkl file")
        
        # Check for feature importance
        importance_file = self.evidence_path / 'artifacts' / 'feature-importance.json'
        
        if not importance_file.exists():
            issues.append("Missing feature-importance.json")
        else:
            try:
                with open(importance_file, 'r') as f:
                    importance_data = json.load(f)
                
                # Validate multiple importance methods
                required_methods = ['shap', 'permutation']
                for method in required_methods:
                    if method not in importance_data:
                        issues.append(f"Missing feature importance method: {method}")
            
            except json.JSONDecodeError:
                issues.append("Invalid JSON in feature-importance.json")
            except Exception as e:
                issues.append(f"Error validating feature importance: {str(e)}")
        
        # Check for explainability report
        report_file = self.evidence_path / 'reports' / 'explainability-report.md'
        
        if not report_file.exists():
            issues.append("Missing explainability-report.md")
        else:
            try:
                with open(report_file, 'r') as f:
                    content = f.read()
                
                # Check for required sections
                required_sections = [
                    'global interpretability',
                    'local explanations',
                    'shap',
                    'lime',
                    'feature importance'
                ]
                
                for section in required_sections:
                    if section.lower() not in content.lower():
                        issues.append(f"Missing section in explainability report: {section}")
            
            except Exception as e:
                issues.append(f"Error reading explainability report: {str(e)}")
        
        return len(issues) == 0, issues
    
    def validate_gate_2_stakeholder_communication(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 2: Stakeholder Communication
        
        Requirements:
        - Interpretation guide created
        - Model card completed
        - Explanation dashboard deployed
        - Stakeholder training conducted
        """
        issues = []
        
        # Check for interpretation guide
        guide_file = self.evidence_path / 'reports' / 'interpretation-guide.md'
        
        if not guide_file.exists():
            issues.append("Missing interpretation-guide.md")
        else:
            try:
                with open(guide_file, 'r') as f:
                    content = f.read()
                
                # Check for stakeholder-friendly language
                required_elements = [
                    'how to read',
                    'understanding',
                    'step',
                    'example',
                    'question'
                ]
                
                for element in required_elements:
                    if element.lower() not in content.lower():
                        issues.append(f"Interpretation guide missing element: {element}")
                
                # Check for regulatory compliance section
                if 'gdpr' not in content.lower() and 'regulatory' not in content.lower():
                    issues.append("Interpretation guide missing regulatory compliance section")
            
            except Exception as e:
                issues.append(f"Error reading interpretation guide: {str(e)}")
        
        # Check for model card
        model_card_file = self.evidence_path / 'reports' / 'model-card.md'
        
        if not model_card_file.exists():
            issues.append("Missing model-card.md")
        else:
            try:
                with open(model_card_file, 'r') as f:
                    content = f.read()
                
                # Check for required model card sections
                required_sections = [
                    'model details',
                    'intended use',
                    'training data',
                    'performance metrics',
                    'limitations',
                    'ethical considerations'
                ]
                
                for section in required_sections:
                    if section.lower() not in content.lower():
                        issues.append(f"Model card missing section: {section}")
            
            except Exception as e:
                issues.append(f"Error reading model card: {str(e)}")
        
        # Check for explanation dashboard
        dashboard_file = self.evidence_path / 'visualizations' / 'explainability-dashboard.html'
        
        if not dashboard_file.exists():
            issues.append("Missing explainability-dashboard.html")
        
        return len(issues) == 0, issues
    
    def validate_gate_3_regulatory_compliance(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 3: Regulatory Compliance
        
        Requirements:
        - GDPR Article 22 compliance verified
        - EU AI Act transparency requirements met
        - Documentation audit trail complete
        - Legal team approval obtained
        """
        issues = []
        
        # Check for regulatory compliance documentation
        compliance_file = self.evidence_path / 'documentation' / 'regulatory-compliance.md'
        
        if not compliance_file.exists():
            issues.append("Missing regulatory-compliance.md")
        else:
            try:
                with open(compliance_file, 'r') as f:
                    content = f.read()
                
                # Check for specific regulatory requirements
                regulations = [
                    'gdpr article 22',
                    'eu ai act',
                    'iso/iec 42001'
                ]
                
                for regulation in regulations:
                    if regulation.lower() not in content.lower():
                        issues.append(f"Missing regulatory compliance: {regulation}")
                
                # Check for approval documentation
                if 'approval' not in content.lower() and 'sign-off' not in content.lower():
                    issues.append("Missing legal team approval documentation")
            
            except Exception as e:
                issues.append(f"Error reading regulatory compliance: {str(e)}")
        
        # Check for audit trail
        explainability_report = self.evidence_path / 'reports' / 'explainability-report.md'
        
        if explainability_report.exists():
            try:
                with open(explainability_report, 'r') as f:
                    content = f.read()
                
                # Verify audit trail elements
                audit_elements = [
                    'version',
                    'date',
                    'methodology'
                ]
                
                for element in audit_elements:
                    if element.lower() not in content.lower():
                        issues.append(f"Audit trail missing element: {element}")
            
            except Exception as e:
                issues.append(f"Error validating audit trail: {str(e)}")
        
        return len(issues) == 0, issues
    
    def validate_deliverables(self) -> Tuple[bool, List[str]]:
        """Validate all required deliverables exist."""
        issues = []
        
        required_files = [
            'reports/explainability-report.md',
            'reports/interpretation-guide.md',
            'reports/model-card.md',
            'artifacts/shap-values.pkl',
            'artifacts/lime-explainer.pkl',
            'artifacts/feature-importance.json',
            'visualizations/explainability-dashboard.html',
            'visualizations/shap-summary.png',
            'visualizations/feature-importance.png',
            'documentation/regulatory-compliance.md'
        ]
        
        for file_path in required_files:
            full_path = self.evidence_path / file_path
            if not full_path.exists():
                issues.append(f"Missing required file: {file_path}")
        
        return len(issues) == 0, issues
    
    def validate_explanation_quality(self) -> Tuple[bool, List[str]]:
        """Validate quality of explanations."""
        issues = []
        
        # Check feature importance has reasonable values
        importance_file = self.evidence_path / 'artifacts' / 'feature-importance.json'
        
        if importance_file.exists():
            try:
                with open(importance_file, 'r') as f:
                    importance_data = json.load(f)
                
                # Validate SHAP importance
                if 'shap' in importance_data:
                    shap_importance = importance_data['shap']
                    
                    # Check that we have features
                    if len(shap_importance) == 0:
                        issues.append("SHAP importance has no features")
                    
                    # Check for reasonable values (not all zeros)
                    values = list(shap_importance.values())
                    if all(v == 0 for v in values):
                        issues.append("All SHAP importance values are zero")
                    
                    # Check for NaN or infinite values
                    if any(v != v for v in values):  # NaN check
                        issues.append("SHAP importance contains NaN values")
            
            except Exception as e:
                issues.append(f"Error validating explanation quality: {str(e)}")
        
        # Check that visualizations exist and are non-empty
        viz_files = [
            'visualizations/shap-summary.png',
            'visualizations/feature-importance.png'
        ]
        
        for viz_file in viz_files:
            full_path = self.evidence_path / viz_file
            if full_path.exists():
                # Check file size (should be > 1KB for a real visualization)
                file_size = full_path.stat().st_size
                if file_size < 1024:
                    issues.append(f"Visualization file too small (possibly empty): {viz_file}")
        
        return len(issues) == 0, issues
    
    def run_validation(self) -> Dict:
        """Run complete validation."""
        
        print(f"Validating Protocol 17: AI Model Explainability & Interpretability")
        print(f"Evidence path: {self.evidence_path}")
        print("-" * 80)
        
        # Validate deliverables
        deliverables_pass, deliverables_issues = self.validate_deliverables()
        self.validation_results['deliverables'] = {
            'status': 'PASS' if deliverables_pass else 'FAIL',
            'issues': deliverables_issues
        }
        
        # Validate Gate 1
        gate1_pass, gate1_issues = self.validate_gate_1_explainability_coverage()
        self.validation_results['gates']['gate_1_explainability_coverage'] = {
            'status': 'PASS' if gate1_pass else 'FAIL',
            'issues': gate1_issues
        }
        
        # Validate Gate 2
        gate2_pass, gate2_issues = self.validate_gate_2_stakeholder_communication()
        self.validation_results['gates']['gate_2_stakeholder_communication'] = {
            'status': 'PASS' if gate2_pass else 'FAIL',
            'issues': gate2_issues
        }
        
        # Validate Gate 3
        gate3_pass, gate3_issues = self.validate_gate_3_regulatory_compliance()
        self.validation_results['gates']['gate_3_regulatory_compliance'] = {
            'status': 'PASS' if gate3_pass else 'FAIL',
            'issues': gate3_issues
        }
        
        # Validate explanation quality
        quality_pass, quality_issues = self.validate_explanation_quality()
        self.validation_results['explanation_quality'] = {
            'status': 'PASS' if quality_pass else 'FAIL',
            'issues': quality_issues
        }
        
        # Overall status
        all_pass = (deliverables_pass and gate1_pass and gate2_pass and 
                   gate3_pass and quality_pass)
        self.validation_results['overall_status'] = 'PASS' if all_pass else 'FAIL'
        
        # Print results
        self._print_results()
        
        return self.validation_results
    
    def _print_results(self):
        """Print validation results."""
        
        print("\n" + "=" * 80)
        print("VALIDATION RESULTS")
        print("=" * 80)
        
        # Deliverables
        print("\nDeliverables:")
        print(f"  Status: {self.validation_results['deliverables']['status']}")
        if self.validation_results['deliverables']['issues']:
            for issue in self.validation_results['deliverables']['issues']:
                print(f"    ❌ {issue}")
        
        # Gates
        for gate_name, gate_result in self.validation_results['gates'].items():
            print(f"\n{gate_name.replace('_', ' ').title()}:")
            print(f"  Status: {gate_result['status']}")
            if gate_result['issues']:
                for issue in gate_result['issues']:
                    print(f"    ❌ {issue}")
        
        # Explanation quality
        if 'explanation_quality' in self.validation_results:
            print(f"\nExplanation Quality:")
            print(f"  Status: {self.validation_results['explanation_quality']['status']}")
            if self.validation_results['explanation_quality']['issues']:
                for issue in self.validation_results['explanation_quality']['issues']:
                    print(f"    ❌ {issue}")
        
        # Overall
        print("\n" + "=" * 80)
        print(f"OVERALL STATUS: {self.validation_results['overall_status']}")
        print("=" * 80)


def main():
    """Main entry point."""
    
    if len(sys.argv) < 2:
        print("Usage: python validate_explainability.py <evidence_path>")
        print("Example: python validate_explainability.py /path/to/evidence/protocol-17-explainability")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"Error: Evidence path does not exist: {evidence_path}")
        sys.exit(1)
    
    validator = Protocol17Validator(evidence_path)
    results = validator.run_validation()
    
    # Save results
    output_file = Path(evidence_path) / 'validation-results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nValidation results saved to: {output_file}")
    
    # Exit with appropriate code
    sys.exit(0 if results['overall_status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()

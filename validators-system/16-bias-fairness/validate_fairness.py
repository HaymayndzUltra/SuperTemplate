#!/usr/bin/env python3
"""
Validator for Protocol 16: AI Bias Detection & Fairness Audit

This script validates that all fairness requirements are met including:
- Demographic parity analysis
- Equal opportunity metrics
- Disparate impact calculations
- Mitigation plan completeness
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class Protocol16Validator:
    """Validator for AI Bias Detection & Fairness Audit protocol."""
    
    def __init__(self, evidence_path: str):
        """
        Initialize validator.
        
        Args:
            evidence_path: Path to protocol 16 evidence directory
        """
        self.evidence_path = Path(evidence_path)
        self.validation_results = {
            'protocol': 'Protocol 16: AI Bias Detection & Fairness Audit',
            'gates': {},
            'overall_status': 'PENDING'
        }
    
    def validate_gate_1_fairness_metrics(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 1: Fairness Metrics
        
        Requirements:
        - Demographic parity difference < 0.10
        - Equal opportunity difference < 0.10
        - Disparate impact ratio > 0.80 (four-fifths rule)
        - All protected groups analyzed
        """
        issues = []
        
        # Check for bias metrics file
        bias_metrics_file = self.evidence_path / 'metrics' / 'bias-metrics.json'
        
        if not bias_metrics_file.exists():
            issues.append("Missing bias-metrics.json file")
            return False, issues
        
        try:
            with open(bias_metrics_file, 'r') as f:
                bias_data = json.load(f)
            
            # Validate demographic parity
            if 'demographic_parity' in bias_data:
                dp_diff = bias_data['demographic_parity'].get('difference', 1.0)
                if dp_diff >= 0.10:
                    issues.append(f"Demographic parity difference ({dp_diff:.4f}) exceeds threshold (0.10)")
                
                if not bias_data['demographic_parity'].get('passes_threshold', False):
                    issues.append("Demographic parity does not pass threshold")
            else:
                issues.append("Missing demographic parity analysis")
            
            # Validate equal opportunity
            if 'equal_opportunity' in bias_data:
                eo_diff = bias_data['equal_opportunity'].get('difference', 1.0)
                if eo_diff >= 0.10:
                    issues.append(f"Equal opportunity difference ({eo_diff:.4f}) exceeds threshold (0.10)")
                
                if not bias_data['equal_opportunity'].get('passes_threshold', False):
                    issues.append("Equal opportunity does not pass threshold")
            else:
                issues.append("Missing equal opportunity analysis")
            
            # Validate disparate impact
            if 'disparate_impact' in bias_data:
                if not bias_data['disparate_impact'].get('passes_four_fifths', False):
                    issues.append("Model fails four-fifths rule (80% disparate impact threshold)")
                
                di_ratios = bias_data['disparate_impact'].get('di_ratios', {})
                for group, ratio in di_ratios.items():
                    if ratio < 0.80:
                        issues.append(f"Disparate impact ratio for {group} ({ratio:.4f}) below threshold (0.80)")
            else:
                issues.append("Missing disparate impact analysis")
            
            # Check for protected groups analysis
            demographic_analysis_file = self.evidence_path / 'metrics' / 'demographic-analysis.json'
            if not demographic_analysis_file.exists():
                issues.append("Missing demographic-analysis.json")
            else:
                with open(demographic_analysis_file, 'r') as f:
                    demo_data = json.load(f)
                
                required_attributes = ['gender', 'race', 'age']
                for attr in required_attributes:
                    if attr not in demo_data:
                        issues.append(f"Missing analysis for protected attribute: {attr}")
        
        except json.JSONDecodeError:
            issues.append("Invalid JSON in bias-metrics.json")
            return False, issues
        except Exception as e:
            issues.append(f"Error validating fairness metrics: {str(e)}")
            return False, issues
        
        return len(issues) == 0, issues
    
    def validate_gate_2_mitigation_plan(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 2: Mitigation Plan
        
        Requirements:
        - Bias sources identified
        - Mitigation strategies defined
        - Implementation timeline established
        - Success criteria documented
        """
        issues = []
        
        mitigation_file = self.evidence_path / 'reports' / 'mitigation-plan.md'
        
        if not mitigation_file.exists():
            issues.append("Missing mitigation-plan.md")
            return False, issues
        
        try:
            with open(mitigation_file, 'r') as f:
                content = f.read()
            
            # Check for required sections
            required_sections = [
                'bias sources',
                'mitigation strategies',
                'timeline',
                'success criteria',
                'implementation'
            ]
            
            for section in required_sections:
                if section.lower() not in content.lower():
                    issues.append(f"Missing required section in mitigation plan: {section}")
            
            # Check for specific mitigation methods
            mitigation_methods = [
                'reweighting',
                'threshold optimization',
                'fairness constraints'
            ]
            
            has_method = False
            for method in mitigation_methods:
                if method.lower() in content.lower():
                    has_method = True
                    break
            
            if not has_method:
                issues.append("No specific mitigation methods identified")
            
            # Validate success criteria are quantitative
            if 'success criteria' in content.lower():
                if '<' not in content and '>' not in content and '%' not in content:
                    issues.append("Success criteria should include quantitative thresholds")
        
        except Exception as e:
            issues.append(f"Error validating mitigation plan: {str(e)}")
            return False, issues
        
        return len(issues) == 0, issues
    
    def validate_gate_3_compliance_documentation(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 3: Compliance & Documentation
        
        Requirements:
        - GDPR compliance verified
        - EU AI Act requirements met
        - Stakeholder approval obtained
        - Audit trail complete
        """
        issues = []
        
        # Check for fairness audit report
        audit_report_file = self.evidence_path / 'reports' / 'fairness-audit-report.md'
        
        if not audit_report_file.exists():
            issues.append("Missing fairness-audit-report.md")
            return False, issues
        
        try:
            with open(audit_report_file, 'r') as f:
                content = f.read()
            
            # Check for compliance sections
            compliance_requirements = [
                'gdpr',
                'eu ai act',
                'iso/iec 42001'
            ]
            
            for requirement in compliance_requirements:
                if requirement.lower() not in content.lower():
                    issues.append(f"Missing compliance documentation: {requirement}")
            
            # Check for stakeholder approval
            if 'approval' not in content.lower() and 'sign-off' not in content.lower():
                issues.append("Missing stakeholder approval documentation")
            
            # Check for compliance checklist
            compliance_checklist_file = self.evidence_path / 'reports' / 'compliance-checklist.md'
            if not compliance_checklist_file.exists():
                issues.append("Missing compliance-checklist.md")
            
            # Check for dashboard
            dashboard_file = self.evidence_path / 'visualizations' / 'fairness-dashboard.html'
            if not dashboard_file.exists():
                issues.append("Missing fairness-dashboard.html")
        
        except Exception as e:
            issues.append(f"Error validating compliance documentation: {str(e)}")
            return False, issues
        
        return len(issues) == 0, issues
    
    def validate_deliverables(self) -> Tuple[bool, List[str]]:
        """Validate all required deliverables exist."""
        issues = []
        
        required_files = [
            'reports/fairness-audit-report.md',
            'reports/mitigation-plan.md',
            'reports/compliance-checklist.md',
            'metrics/bias-metrics.json',
            'metrics/demographic-analysis.json',
            'metrics/fairness-scores.json',
            'visualizations/fairness-dashboard.html',
            'visualizations/selection-rates.png',
            'visualizations/disparate-impact.png'
        ]
        
        for file_path in required_files:
            full_path = self.evidence_path / file_path
            if not full_path.exists():
                issues.append(f"Missing required file: {file_path}")
        
        return len(issues) == 0, issues
    
    def validate_fairness_thresholds(self) -> Tuple[bool, List[str]]:
        """Validate that all fairness metrics meet thresholds."""
        issues = []
        
        bias_metrics_file = self.evidence_path / 'metrics' / 'bias-metrics.json'
        
        if not bias_metrics_file.exists():
            issues.append("Cannot validate thresholds: bias-metrics.json missing")
            return False, issues
        
        try:
            with open(bias_metrics_file, 'r') as f:
                bias_data = json.load(f)
            
            # Create summary of threshold compliance
            threshold_summary = {
                'demographic_parity': {
                    'threshold': 0.10,
                    'actual': bias_data.get('demographic_parity', {}).get('difference', None),
                    'passes': bias_data.get('demographic_parity', {}).get('passes_threshold', False)
                },
                'equal_opportunity': {
                    'threshold': 0.10,
                    'actual': bias_data.get('equal_opportunity', {}).get('difference', None),
                    'passes': bias_data.get('equal_opportunity', {}).get('passes_threshold', False)
                },
                'disparate_impact': {
                    'threshold': 0.80,
                    'actual': bias_data.get('disparate_impact', {}).get('di_ratios', {}),
                    'passes': bias_data.get('disparate_impact', {}).get('passes_four_fifths', False)
                }
            }
            
            # Check each metric
            for metric_name, metric_data in threshold_summary.items():
                if not metric_data['passes']:
                    issues.append(f"{metric_name} does not meet fairness threshold")
        
        except Exception as e:
            issues.append(f"Error validating fairness thresholds: {str(e)}")
            return False, issues
        
        return len(issues) == 0, issues
    
    def run_validation(self) -> Dict:
        """Run complete validation."""
        
        print(f"Validating Protocol 16: AI Bias Detection & Fairness Audit")
        print(f"Evidence path: {self.evidence_path}")
        print("-" * 80)
        
        # Validate deliverables
        deliverables_pass, deliverables_issues = self.validate_deliverables()
        self.validation_results['deliverables'] = {
            'status': 'PASS' if deliverables_pass else 'FAIL',
            'issues': deliverables_issues
        }
        
        # Validate Gate 1
        gate1_pass, gate1_issues = self.validate_gate_1_fairness_metrics()
        self.validation_results['gates']['gate_1_fairness_metrics'] = {
            'status': 'PASS' if gate1_pass else 'FAIL',
            'issues': gate1_issues
        }
        
        # Validate Gate 2
        gate2_pass, gate2_issues = self.validate_gate_2_mitigation_plan()
        self.validation_results['gates']['gate_2_mitigation_plan'] = {
            'status': 'PASS' if gate2_pass else 'FAIL',
            'issues': gate2_issues
        }
        
        # Validate Gate 3
        gate3_pass, gate3_issues = self.validate_gate_3_compliance_documentation()
        self.validation_results['gates']['gate_3_compliance_documentation'] = {
            'status': 'PASS' if gate3_pass else 'FAIL',
            'issues': gate3_issues
        }
        
        # Validate fairness thresholds
        thresholds_pass, thresholds_issues = self.validate_fairness_thresholds()
        self.validation_results['fairness_thresholds'] = {
            'status': 'PASS' if thresholds_pass else 'FAIL',
            'issues': thresholds_issues
        }
        
        # Overall status
        all_pass = (deliverables_pass and gate1_pass and gate2_pass and 
                   gate3_pass and thresholds_pass)
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
        
        # Fairness thresholds
        if 'fairness_thresholds' in self.validation_results:
            print(f"\nFairness Thresholds:")
            print(f"  Status: {self.validation_results['fairness_thresholds']['status']}")
            if self.validation_results['fairness_thresholds']['issues']:
                for issue in self.validation_results['fairness_thresholds']['issues']:
                    print(f"    ❌ {issue}")
        
        # Overall
        print("\n" + "=" * 80)
        print(f"OVERALL STATUS: {self.validation_results['overall_status']}")
        print("=" * 80)


def main():
    """Main entry point."""
    
    if len(sys.argv) < 2:
        print("Usage: python validate_fairness.py <evidence_path>")
        print("Example: python validate_fairness.py /path/to/evidence/protocol-16-bias-fairness")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"Error: Evidence path does not exist: {evidence_path}")
        sys.exit(1)
    
    validator = Protocol16Validator(evidence_path)
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

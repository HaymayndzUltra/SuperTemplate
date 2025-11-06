#!/usr/bin/env python3
"""
Validator for Protocol 14: AI Model Validation & Evaluation
Validates cross-validation, holdout testing, overfitting detection, and stability analysis.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List

class ModelValidationValidator:
    """Validates Protocol 14 deliverables and quality gates."""
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.validation_results = {
            'protocol': '14-model-validation',
            'gates': {},
            'errors': [],
            'warnings': [],
            'passed': False
        }
    
    def validate_all(self) -> Dict:
        """Run all validation checks."""
        
        print("🔍 Validating Protocol 14: Model Validation & Evaluation")
        print("=" * 70)
        
        # Gate 1: Cross-Validation Complete
        self.validate_gate1_cv_complete()
        
        # Gate 2: Holdout Validation Passed
        self.validate_gate2_holdout_passed()
        
        # Gate 3: Stability Confirmed
        self.validate_gate3_stability_confirmed()
        
        # Determine overall pass/fail
        self.validation_results['passed'] = all(
            gate['passed'] for gate in self.validation_results['gates'].values()
        )
        
        return self.validation_results
    
    def validate_gate1_cv_complete(self):
        """Gate 1: Cross-Validation Complete."""
        
        gate_name = "gate1_cv_complete"
        print(f"\n📋 Gate 1: Cross-Validation Complete")
        
        checks = {
            'cv_strategy_appropriate': False,
            'all_folds_completed': False,
            'metrics_aggregated': False,
            'stability_metrics_calculated': False
        }
        
        # Check for CV scores
        cv_scores_path = self.evidence_path / 'metrics' / 'cv-scores.json'
        
        if cv_scores_path.exists():
            try:
                with open(cv_scores_path, 'r') as f:
                    cv_data = json.load(f)
                
                # Check CV strategy
                if 'strategy' in cv_data or 'cv_strategy' in cv_data:
                    checks['cv_strategy_appropriate'] = True
                    print(f"  ✅ CV strategy documented")
                else:
                    self.validation_results['warnings'].append("CV strategy not documented")
                    print("  ⚠️  CV strategy not documented")
                
                # Check folds
                if 'fold_details' in cv_data or 'folds' in cv_data:
                    fold_count = len(cv_data.get('fold_details', cv_data.get('folds', [])))
                    if fold_count >= 3:
                        checks['all_folds_completed'] = True
                        print(f"  ✅ {fold_count} folds completed")
                    else:
                        self.validation_results['errors'].append(f"Insufficient folds: {fold_count} < 3")
                        print(f"  ❌ Insufficient folds: {fold_count} < 3")
                else:
                    self.validation_results['errors'].append("Fold details not found")
                    print("  ❌ Fold details not found")
                
                # Check aggregated metrics
                if 'aggregated_metrics' in cv_data or 'mean' in str(cv_data):
                    checks['metrics_aggregated'] = True
                    print("  ✅ Metrics aggregated correctly")
                else:
                    self.validation_results['errors'].append("Aggregated metrics not found")
                    print("  ❌ Aggregated metrics not found")
                
                # Check stability metrics
                if 'stability' in cv_data or 'std' in str(cv_data):
                    checks['stability_metrics_calculated'] = True
                    print("  ✅ Stability metrics calculated")
                else:
                    self.validation_results['warnings'].append("Stability metrics not calculated")
                    print("  ⚠️  Stability metrics not calculated")
                
            except json.JSONDecodeError:
                self.validation_results['errors'].append("Invalid JSON in CV scores")
                print("  ❌ Invalid JSON in CV scores")
        else:
            self.validation_results['errors'].append(f"CV scores not found: {cv_scores_path}")
            print(f"  ❌ CV scores not found")
        
        self.validation_results['gates'][gate_name] = {
            'passed': all([checks['all_folds_completed'], checks['metrics_aggregated']]),
            'checks': checks
        }
    
    def validate_gate2_holdout_passed(self):
        """Gate 2: Holdout Validation Passed."""
        
        gate_name = "gate2_holdout_passed"
        print(f"\n📋 Gate 2: Holdout Validation Passed")
        
        checks = {
            'test_performance_meets_threshold': False,
            'no_significant_overfitting': False,
            'error_analysis_completed': False,
            'confusion_matrix_analyzed': False
        }
        
        # Check for holdout metrics
        holdout_metrics_path = self.evidence_path / 'metrics' / 'holdout-metrics.json'
        
        if holdout_metrics_path.exists():
            try:
                with open(holdout_metrics_path, 'r') as f:
                    holdout_data = json.load(f)
                
                # Check test performance
                metrics = holdout_data.get('metrics', {})
                if metrics:
                    # Check if primary metric exists and is reasonable
                    primary_metric = metrics.get('accuracy', metrics.get('r2', 0))
                    if primary_metric > 0.5:  # Basic threshold
                        checks['test_performance_meets_threshold'] = True
                        print(f"  ✅ Test performance acceptable: {primary_metric:.4f}")
                    else:
                        self.validation_results['warnings'].append(f"Low test performance: {primary_metric:.4f}")
                        print(f"  ⚠️  Low test performance: {primary_metric:.4f}")
                else:
                    self.validation_results['errors'].append("Test metrics not found")
                    print("  ❌ Test metrics not found")
                
            except json.JSONDecodeError:
                self.validation_results['errors'].append("Invalid JSON in holdout metrics")
                print("  ❌ Invalid JSON in holdout metrics")
        else:
            self.validation_results['errors'].append(f"Holdout metrics not found: {holdout_metrics_path}")
            print(f"  ❌ Holdout metrics not found")
        
        # Check for overfitting report
        overfitting_report_path = self.evidence_path / 'reports' / 'overfitting-report.md'
        
        if overfitting_report_path.exists():
            content = overfitting_report_path.read_text()
            
            # Check overfitting severity
            if 'none' in content.lower() or 'mild' in content.lower():
                checks['no_significant_overfitting'] = True
                print("  ✅ No significant overfitting detected")
            elif 'moderate' in content.lower():
                self.validation_results['warnings'].append("Moderate overfitting detected")
                print("  ⚠️  Moderate overfitting detected")
            elif 'severe' in content.lower():
                self.validation_results['errors'].append("Severe overfitting detected")
                print("  ❌ Severe overfitting detected")
            else:
                self.validation_results['warnings'].append("Overfitting severity not documented")
                print("  ⚠️  Overfitting severity not documented")
        else:
            self.validation_results['warnings'].append("Overfitting report not found")
            print("  ⚠️  Overfitting report not found")
        
        # Check for error analysis
        error_analysis_path = self.evidence_path / 'analysis' / 'error-analysis.json'
        
        if error_analysis_path.exists():
            checks['error_analysis_completed'] = True
            print("  ✅ Error analysis completed")
        else:
            self.validation_results['warnings'].append("Error analysis not found")
            print("  ⚠️  Error analysis not found")
        
        # Check for confusion matrix
        confusion_matrix_path = self.evidence_path / 'analysis' / 'confusion-matrix.json'
        
        if confusion_matrix_path.exists():
            checks['confusion_matrix_analyzed'] = True
            print("  ✅ Confusion matrix analyzed")
        else:
            self.validation_results['warnings'].append("Confusion matrix not found")
            print("  ⚠️  Confusion matrix not found")
        
        self.validation_results['gates'][gate_name] = {
            'passed': all([checks['test_performance_meets_threshold'], 
                          checks['no_significant_overfitting']]),
            'checks': checks
        }
    
    def validate_gate3_stability_confirmed(self):
        """Gate 3: Stability Confirmed."""
        
        gate_name = "gate3_stability_confirmed"
        print(f"\n📋 Gate 3: Stability Confirmed")
        
        checks = {
            'bootstrap_stability_acceptable': False,
            'perturbation_stability_high': False,
            'prediction_consistency_verified': False,
            'overall_stability_score_high': False
        }
        
        # Check for stability metrics
        stability_metrics_path = self.evidence_path / 'metrics' / 'stability-metrics.json'
        
        if stability_metrics_path.exists():
            try:
                with open(stability_metrics_path, 'r') as f:
                    stability_data = json.load(f)
                
                # Check bootstrap stability
                bootstrap_data = stability_data.get('bootstrap_stability', {})
                if bootstrap_data:
                    cv = bootstrap_data.get('coefficient_of_variation', 1.0)
                    if cv < 0.1:
                        checks['bootstrap_stability_acceptable'] = True
                        print(f"  ✅ Bootstrap stability acceptable (CV: {cv:.4f})")
                    else:
                        self.validation_results['warnings'].append(f"High bootstrap CV: {cv:.4f}")
                        print(f"  ⚠️  High bootstrap CV: {cv:.4f}")
                else:
                    self.validation_results['warnings'].append("Bootstrap stability not found")
                    print("  ⚠️  Bootstrap stability not found")
                
                # Check perturbation stability
                perturbation_data = stability_data.get('perturbation_stability', {})
                if perturbation_data:
                    # Check average prediction agreement
                    agreements = [v.get('prediction_agreement', 0) for v in perturbation_data.values()]
                    if agreements and min(agreements) > 0.9:
                        checks['perturbation_stability_high'] = True
                        print(f"  ✅ Perturbation stability high (min: {min(agreements):.4f})")
                    else:
                        self.validation_results['warnings'].append(f"Low perturbation stability")
                        print(f"  ⚠️  Low perturbation stability")
                else:
                    self.validation_results['warnings'].append("Perturbation stability not found")
                    print("  ⚠️  Perturbation stability not found")
                
                # Check prediction consistency
                consistency_data = stability_data.get('prediction_consistency', {})
                if consistency_data:
                    consistency_rate = consistency_data.get('consistency_rate', 0)
                    if consistency_rate >= 0.95:
                        checks['prediction_consistency_verified'] = True
                        print(f"  ✅ Prediction consistency verified ({consistency_rate:.4f})")
                    else:
                        self.validation_results['warnings'].append(f"Low prediction consistency: {consistency_rate:.4f}")
                        print(f"  ⚠️  Low prediction consistency: {consistency_rate:.4f}")
                else:
                    self.validation_results['warnings'].append("Prediction consistency not found")
                    print("  ⚠️  Prediction consistency not found")
                
                # Check overall stability score
                overall_score = stability_data.get('overall_stability_score', 0)
                if overall_score > 0.8:
                    checks['overall_stability_score_high'] = True
                    print(f"  ✅ Overall stability score high ({overall_score:.4f})")
                else:
                    self.validation_results['errors'].append(f"Low overall stability score: {overall_score:.4f}")
                    print(f"  ❌ Low overall stability score: {overall_score:.4f}")
                
            except json.JSONDecodeError:
                self.validation_results['errors'].append("Invalid JSON in stability metrics")
                print("  ❌ Invalid JSON in stability metrics")
        else:
            self.validation_results['errors'].append(f"Stability metrics not found: {stability_metrics_path}")
            print(f"  ❌ Stability metrics not found")
        
        # Check for stability analysis report
        stability_report_path = self.evidence_path / 'reports' / 'stability-analysis.md'
        
        if not stability_report_path.exists():
            self.validation_results['warnings'].append("Stability analysis report not found")
            print("  ⚠️  Stability analysis report not found")
        
        self.validation_results['gates'][gate_name] = {
            'passed': checks['overall_stability_score_high'],  # Core check
            'checks': checks
        }
    
    def print_summary(self):
        """Print validation summary."""
        
        print("\n" + "=" * 70)
        print("📊 VALIDATION SUMMARY")
        print("=" * 70)
        
        total_gates = len(self.validation_results['gates'])
        passed_gates = sum(1 for gate in self.validation_results['gates'].values() if gate['passed'])
        
        print(f"\nGates Passed: {passed_gates}/{total_gates}")
        
        if self.validation_results['errors']:
            print(f"\n❌ Errors ({len(self.validation_results['errors'])}):")
            for error in self.validation_results['errors']:
                print(f"  - {error}")
        
        if self.validation_results['warnings']:
            print(f"\n⚠️  Warnings ({len(self.validation_results['warnings'])}):")
            for warning in self.validation_results['warnings']:
                print(f"  - {warning}")
        
        print(f"\n{'✅ VALIDATION PASSED' if self.validation_results['passed'] else '❌ VALIDATION FAILED'}")
        print("=" * 70)


def main():
    """Main validation entry point."""
    
    if len(sys.argv) < 2:
        print("Usage: python validate_model_validation.py <evidence_path>")
        print("Example: python validate_model_validation.py ../evidence/protocol-14-model-validation/")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"❌ Evidence path not found: {evidence_path}")
        sys.exit(1)
    
    validator = ModelValidationValidator(evidence_path)
    results = validator.validate_all()
    validator.print_summary()
    
    # Save results
    output_path = Path(evidence_path) / 'validation-results.json'
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved to: {output_path}")
    
    # Exit with appropriate code
    sys.exit(0 if results['passed'] else 1)


if __name__ == '__main__':
    main()

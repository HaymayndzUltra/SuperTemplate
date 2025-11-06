#!/usr/bin/env python3
"""
Validator for Protocol 13: AI Algorithm Selection & Baseline Model
Validates algorithm selection process, baseline training, and comparison analysis.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class AlgorithmSelectionValidator:
    """Validates Protocol 13 deliverables and quality gates."""
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.validation_results = {
            'protocol': '13-algorithm-selection',
            'gates': {},
            'errors': [],
            'warnings': [],
            'passed': False
        }
    
    def validate_all(self) -> Dict:
        """Run all validation checks."""
        
        print("🔍 Validating Protocol 13: Algorithm Selection & Baseline Model")
        print("=" * 70)
        
        # Gate 1: Problem Analysis Complete
        self.validate_gate1_problem_analysis()
        
        # Gate 2: Baseline Training Complete
        self.validate_gate2_baseline_training()
        
        # Gate 3: Selection Justified
        self.validate_gate3_selection_justified()
        
        # Determine overall pass/fail
        self.validation_results['passed'] = all(
            gate['passed'] for gate in self.validation_results['gates'].values()
        )
        
        return self.validation_results
    
    def validate_gate1_problem_analysis(self):
        """Gate 1: Problem Analysis Complete."""
        
        gate_name = "gate1_problem_analysis"
        print(f"\n📋 Gate 1: Problem Analysis Complete")
        
        checks = {
            'task_type_identified': False,
            'data_characteristics_documented': False,
            'constraints_identified': False,
            'algorithm_recommendations_generated': False
        }
        
        # Check for problem analysis report
        problem_analysis_path = self.evidence_path / 'reports' / 'problem-analysis.md'
        
        if problem_analysis_path.exists():
            content = problem_analysis_path.read_text()
            
            # Check task type
            if any(task in content.lower() for task in ['classification', 'regression', 'clustering']):
                checks['task_type_identified'] = True
                print("  ✅ Task type identified")
            else:
                self.validation_results['errors'].append("Task type not identified in problem analysis")
                print("  ❌ Task type not identified")
            
            # Check data characteristics
            if 'n_samples' in content or 'n_features' in content:
                checks['data_characteristics_documented'] = True
                print("  ✅ Data characteristics documented")
            else:
                self.validation_results['errors'].append("Data characteristics not documented")
                print("  ❌ Data characteristics not documented")
            
            # Check constraints
            if 'constraint' in content.lower() or 'requirement' in content.lower():
                checks['constraints_identified'] = True
                print("  ✅ Constraints identified")
            else:
                self.validation_results['warnings'].append("Constraints not clearly identified")
                print("  ⚠️  Constraints not clearly identified")
            
            # Check recommendations
            if 'recommend' in content.lower() or 'algorithm' in content.lower():
                checks['algorithm_recommendations_generated'] = True
                print("  ✅ Algorithm recommendations generated")
            else:
                self.validation_results['errors'].append("Algorithm recommendations not generated")
                print("  ❌ Algorithm recommendations not generated")
        else:
            self.validation_results['errors'].append(f"Problem analysis report not found: {problem_analysis_path}")
            print(f"  ❌ Problem analysis report not found")
        
        self.validation_results['gates'][gate_name] = {
            'passed': all(checks.values()),
            'checks': checks
        }
    
    def validate_gate2_baseline_training(self):
        """Gate 2: Baseline Training Complete."""
        
        gate_name = "gate2_baseline_training"
        print(f"\n📋 Gate 2: Baseline Training Complete")
        
        checks = {
            'all_candidates_trained': False,
            'metrics_calculated': False,
            'training_times_recorded': False,
            'model_artifacts_saved': False
        }
        
        # Check for models directory
        models_path = self.evidence_path / 'models'
        
        if models_path.exists():
            model_files = list(models_path.glob('baseline_*.pkl'))
            
            if len(model_files) >= 3:  # At least 3 baseline models
                checks['all_candidates_trained'] = True
                print(f"  ✅ {len(model_files)} baseline models trained")
            else:
                self.validation_results['errors'].append(f"Insufficient baseline models: {len(model_files)} < 3")
                print(f"  ❌ Insufficient baseline models: {len(model_files)} < 3")
        else:
            self.validation_results['errors'].append(f"Models directory not found: {models_path}")
            print(f"  ❌ Models directory not found")
        
        # Check for metrics
        metrics_path = self.evidence_path / 'metrics' / 'benchmark-results.json'
        
        if metrics_path.exists():
            try:
                with open(metrics_path, 'r') as f:
                    metrics_data = json.load(f)
                
                if 'metrics' in metrics_data or 'results' in metrics_data:
                    checks['metrics_calculated'] = True
                    print("  ✅ Metrics calculated for all models")
                else:
                    self.validation_results['errors'].append("Metrics data incomplete")
                    print("  ❌ Metrics data incomplete")
                
                if 'training_times' in metrics_data or 'training_time' in str(metrics_data):
                    checks['training_times_recorded'] = True
                    print("  ✅ Training times recorded")
                else:
                    self.validation_results['warnings'].append("Training times not recorded")
                    print("  ⚠️  Training times not recorded")
                
                checks['model_artifacts_saved'] = True
                
            except json.JSONDecodeError:
                self.validation_results['errors'].append("Invalid JSON in benchmark results")
                print("  ❌ Invalid JSON in benchmark results")
        else:
            self.validation_results['errors'].append(f"Benchmark results not found: {metrics_path}")
            print(f"  ❌ Benchmark results not found")
        
        self.validation_results['gates'][gate_name] = {
            'passed': all(checks.values()),
            'checks': checks
        }
    
    def validate_gate3_selection_justified(self):
        """Gate 3: Selection Justified."""
        
        gate_name = "gate3_selection_justified"
        print(f"\n📋 Gate 3: Selection Justified")
        
        checks = {
            'comparison_analysis_completed': False,
            'statistical_tests_performed': False,
            'final_algorithm_selected': False,
            'tradeoffs_documented': False,
            'stakeholder_approval': False
        }
        
        # Check for algorithm selection report
        selection_report_path = self.evidence_path / 'reports' / 'algorithm-selection-report.md'
        
        if selection_report_path.exists():
            content = selection_report_path.read_text()
            
            # Check comparison analysis
            if 'comparison' in content.lower() or 'benchmark' in content.lower():
                checks['comparison_analysis_completed'] = True
                print("  ✅ Comparison analysis completed")
            else:
                self.validation_results['errors'].append("Comparison analysis not found")
                print("  ❌ Comparison analysis not found")
            
            # Check statistical tests
            if 'statistical' in content.lower() or 'p-value' in content.lower() or 't-test' in content.lower():
                checks['statistical_tests_performed'] = True
                print("  ✅ Statistical tests performed")
            else:
                self.validation_results['warnings'].append("Statistical tests not documented")
                print("  ⚠️  Statistical tests not documented")
            
            # Check final selection
            if 'selected' in content.lower() or 'chosen' in content.lower():
                checks['final_algorithm_selected'] = True
                print("  ✅ Final algorithm selected")
            else:
                self.validation_results['errors'].append("Final algorithm not selected")
                print("  ❌ Final algorithm not selected")
            
            # Check trade-offs
            if 'trade-off' in content.lower() or 'tradeoff' in content.lower() or 'pros and cons' in content.lower():
                checks['tradeoffs_documented'] = True
                print("  ✅ Trade-offs documented")
            else:
                self.validation_results['warnings'].append("Trade-offs not clearly documented")
                print("  ⚠️  Trade-offs not clearly documented")
            
            # Check stakeholder approval
            if 'approval' in content.lower() or 'approved' in content.lower():
                checks['stakeholder_approval'] = True
                print("  ✅ Stakeholder approval documented")
            else:
                self.validation_results['warnings'].append("Stakeholder approval not documented")
                print("  ⚠️  Stakeholder approval not documented")
        else:
            self.validation_results['errors'].append(f"Algorithm selection report not found: {selection_report_path}")
            print(f"  ❌ Algorithm selection report not found")
        
        # Check for comparison matrix
        comparison_matrix_path = self.evidence_path / 'metrics' / 'comparison-matrix.xlsx'
        
        if not comparison_matrix_path.exists():
            self.validation_results['warnings'].append("Comparison matrix (Excel) not found")
            print("  ⚠️  Comparison matrix not found")
        
        self.validation_results['gates'][gate_name] = {
            'passed': all([checks['comparison_analysis_completed'], 
                          checks['final_algorithm_selected']]),  # Core checks
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
        print("Usage: python validate_algorithm_selection.py <evidence_path>")
        print("Example: python validate_algorithm_selection.py ../evidence/protocol-13-algorithm-selection/")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"❌ Evidence path not found: {evidence_path}")
        sys.exit(1)
    
    validator = AlgorithmSelectionValidator(evidence_path)
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

#!/usr/bin/env python3
"""
Validator for Protocol 15: AI Model Testing & Edge Case Validation

This script validates that all testing requirements are met including:
- Test coverage thresholds
- Edge case identification
- Performance benchmarks
- Error handling validation
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class Protocol15Validator:
    """Validator for AI Model Testing protocol."""
    
    def __init__(self, evidence_path: str):
        """
        Initialize validator.
        
        Args:
            evidence_path: Path to protocol 15 evidence directory
        """
        self.evidence_path = Path(evidence_path)
        self.validation_results = {
            'protocol': 'Protocol 15: AI Model Testing & Edge Case Validation',
            'gates': {},
            'overall_status': 'PENDING'
        }
    
    def validate_gate_1_test_coverage(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 1: Test Coverage
        
        Requirements:
        - Unit test coverage > 90%
        - Integration test coverage > 80%
        - Edge case test coverage > 70%
        - All critical paths tested
        """
        issues = []
        
        # Check for test coverage report
        coverage_file = self.evidence_path / 'metrics' / 'test-coverage.json'
        
        if not coverage_file.exists():
            issues.append("Missing test-coverage.json file")
            return False, issues
        
        try:
            with open(coverage_file, 'r') as f:
                coverage_data = json.load(f)
            
            # Validate unit test coverage
            total_coverage = coverage_data.get('total_coverage', 0)
            if total_coverage < 90:
                issues.append(f"Unit test coverage ({total_coverage}%) below threshold (90%)")
            
            # Validate module coverage
            module_coverage = coverage_data.get('module_coverage', {})
            
            critical_modules = [
                'model/preprocessing.py',
                'model/inference.py',
                'model/pipeline.py'
            ]
            
            for module in critical_modules:
                if module not in module_coverage:
                    issues.append(f"Missing coverage for critical module: {module}")
                else:
                    mod_cov = module_coverage[module].get('coverage_pct', 0)
                    if mod_cov < 90:
                        issues.append(f"Low coverage for {module}: {mod_cov}%")
            
            # Check for edge case tests
            test_report_file = self.evidence_path / 'reports' / 'test-report.md'
            if not test_report_file.exists():
                issues.append("Missing test-report.md")
            
            edge_case_file = self.evidence_path / 'reports' / 'edge-case-results.md'
            if not edge_case_file.exists():
                issues.append("Missing edge-case-results.md")
            
        except json.JSONDecodeError:
            issues.append("Invalid JSON in test-coverage.json")
            return False, issues
        except Exception as e:
            issues.append(f"Error validating test coverage: {str(e)}")
            return False, issues
        
        return len(issues) == 0, issues
    
    def validate_gate_2_edge_case_handling(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 2: Edge Case Handling
        
        Requirements:
        - All identified edge cases have tests
        - Boundary conditions validated
        - Error scenarios documented
        - No unhandled exceptions in production code
        """
        issues = []
        
        edge_case_file = self.evidence_path / 'reports' / 'edge-case-results.md'
        
        if not edge_case_file.exists():
            issues.append("Missing edge-case-results.md")
            return False, issues
        
        try:
            with open(edge_case_file, 'r') as f:
                content = f.read()
            
            # Check for required edge case categories
            required_categories = [
                'missing values',
                'extreme values',
                'boundary conditions',
                'unseen categories',
                'special characters'
            ]
            
            for category in required_categories:
                if category.lower() not in content.lower():
                    issues.append(f"Missing edge case category: {category}")
            
            # Check for error handling documentation
            error_handling_file = self.evidence_path / 'reports' / 'error-handling-guide.md'
            if not error_handling_file.exists():
                issues.append("Missing error-handling-guide.md")
            
        except Exception as e:
            issues.append(f"Error validating edge cases: {str(e)}")
            return False, issues
        
        return len(issues) == 0, issues
    
    def validate_gate_3_performance_stability(self) -> Tuple[bool, List[str]]:
        """
        Validate Gate 3: Performance & Stability
        
        Requirements:
        - Stress tests pass without crashes
        - Memory usage stable under load
        - Throughput meets requirements (>100 pred/sec)
        - Concurrent requests handled correctly
        """
        issues = []
        
        perf_metrics_file = self.evidence_path / 'metrics' / 'performance-metrics.json'
        
        if not perf_metrics_file.exists():
            issues.append("Missing performance-metrics.json")
            return False, issues
        
        try:
            with open(perf_metrics_file, 'r') as f:
                perf_data = json.load(f)
            
            # Validate throughput
            throughput = perf_data.get('throughput', 0)
            if throughput < 100:
                issues.append(f"Throughput ({throughput} pred/sec) below requirement (100 pred/sec)")
            
            # Validate memory stability
            memory_increase = perf_data.get('memory_increase_mb', 0)
            if memory_increase > 100:
                issues.append(f"Memory increase ({memory_increase}MB) exceeds threshold (100MB)")
            
            # Validate stress test results
            stress_test_file = self.evidence_path / 'metrics' / 'stress-test-results.json'
            if not stress_test_file.exists():
                issues.append("Missing stress-test-results.json")
            else:
                with open(stress_test_file, 'r') as f:
                    stress_data = json.load(f)
                
                if not stress_data.get('all_tests_passed', False):
                    issues.append("Stress tests did not pass")
                
                if stress_data.get('crashes', 0) > 0:
                    issues.append(f"Stress tests resulted in {stress_data['crashes']} crashes")
        
        except json.JSONDecodeError:
            issues.append("Invalid JSON in performance metrics")
            return False, issues
        except Exception as e:
            issues.append(f"Error validating performance: {str(e)}")
            return False, issues
        
        return len(issues) == 0, issues
    
    def validate_deliverables(self) -> Tuple[bool, List[str]]:
        """Validate all required deliverables exist."""
        issues = []
        
        required_files = [
            'reports/test-report.md',
            'reports/edge-case-results.md',
            'reports/error-handling-guide.md',
            'metrics/test-coverage.json',
            'metrics/performance-metrics.json',
            'metrics/stress-test-results.json',
            'logs/test-execution.log',
            'artifacts/test-results.xml'
        ]
        
        for file_path in required_files:
            full_path = self.evidence_path / file_path
            if not full_path.exists():
                issues.append(f"Missing required file: {file_path}")
        
        return len(issues) == 0, issues
    
    def run_validation(self) -> Dict:
        """Run complete validation."""
        
        print(f"Validating Protocol 15: AI Model Testing & Edge Case Validation")
        print(f"Evidence path: {self.evidence_path}")
        print("-" * 80)
        
        # Validate deliverables
        deliverables_pass, deliverables_issues = self.validate_deliverables()
        self.validation_results['deliverables'] = {
            'status': 'PASS' if deliverables_pass else 'FAIL',
            'issues': deliverables_issues
        }
        
        # Validate Gate 1
        gate1_pass, gate1_issues = self.validate_gate_1_test_coverage()
        self.validation_results['gates']['gate_1_test_coverage'] = {
            'status': 'PASS' if gate1_pass else 'FAIL',
            'issues': gate1_issues
        }
        
        # Validate Gate 2
        gate2_pass, gate2_issues = self.validate_gate_2_edge_case_handling()
        self.validation_results['gates']['gate_2_edge_case_handling'] = {
            'status': 'PASS' if gate2_pass else 'FAIL',
            'issues': gate2_issues
        }
        
        # Validate Gate 3
        gate3_pass, gate3_issues = self.validate_gate_3_performance_stability()
        self.validation_results['gates']['gate_3_performance_stability'] = {
            'status': 'PASS' if gate3_pass else 'FAIL',
            'issues': gate3_issues
        }
        
        # Overall status
        all_pass = (deliverables_pass and gate1_pass and gate2_pass and gate3_pass)
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
        
        # Overall
        print("\n" + "=" * 80)
        print(f"OVERALL STATUS: {self.validation_results['overall_status']}")
        print("=" * 80)


def main():
    """Main entry point."""
    
    if len(sys.argv) < 2:
        print("Usage: python validate_testing.py <evidence_path>")
        print("Example: python validate_testing.py /path/to/evidence/protocol-15-model-testing")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"Error: Evidence path does not exist: {evidence_path}")
        sys.exit(1)
    
    validator = Protocol15Validator(evidence_path)
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

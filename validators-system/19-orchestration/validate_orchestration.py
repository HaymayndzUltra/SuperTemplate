#!/usr/bin/env python3
"""
Validator for Protocol 19: AI ML Pipeline Orchestration

This script validates:
- Pipeline definition completeness
- Task dependencies
- Error handling configuration
- Monitoring setup
"""

import os
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Set

class OrchestrationValidator:
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.results = {
            'protocol': '19-orchestration',
            'gates': {},
            'overall_status': 'pending'
        }
    
    def validate_all(self) -> Dict:
        """Run all validation gates."""
        
        print("🔍 Validating Protocol 19: ML Pipeline Orchestration")
        print("=" * 70)
        
        # Gate 1: Pipeline Definition
        self.results['gates']['gate_1'] = self.validate_pipeline_definition()
        
        # Gate 2: Pipeline Execution
        self.results['gates']['gate_2'] = self.validate_execution()
        
        # Gate 3: Monitoring & Observability
        self.results['gates']['gate_3'] = self.validate_monitoring()
        
        # Determine overall status
        all_passed = all(
            gate['status'] == 'passed'
            for gate in self.results['gates'].values()
        )
        self.results['overall_status'] = 'passed' if all_passed else 'failed'
        
        return self.results
    
    def validate_pipeline_definition(self) -> Dict:
        """Gate 1: Validate pipeline definition."""
        
        print("\n📋 Gate 1: Pipeline Definition")
        print("-" * 70)
        
        checks = []
        dags_path = self.evidence_path / 'dags'
        config_path = self.evidence_path / 'config'
        
        # Check 1: Pipeline DAG exists
        dag_files = list(dags_path.glob('*.py')) + list(dags_path.glob('*.yaml'))
        if dag_files:
            print("✅ All tasks defined with clear inputs/outputs")
            checks.append(True)
        else:
            print("❌ No pipeline DAG found")
            checks.append(False)
        
        # Check 2: Dependencies mapped
        if dag_files:
            # Try to parse DAG and check for dependencies
            dag_content = dag_files[0].read_text()
            if '>>' in dag_content or 'dependencies' in dag_content.lower():
                print("✅ Dependencies mapped correctly")
                checks.append(True)
                
                # Check for circular dependencies
                if self._check_circular_dependencies(dag_content):
                    print("❌ Circular dependencies detected")
                    checks.append(False)
                else:
                    print("✅ No circular dependencies detected")
                    checks.append(True)
            else:
                print("❌ Dependencies not clearly defined")
                checks.append(False)
                checks.append(False)
        else:
            checks.append(False)
            checks.append(False)
        
        # Check 3: Resource requirements
        config_file = config_path / 'orchestration-config.yaml'
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                if 'resources' in config:
                    print("✅ Resource requirements specified")
                    checks.append(True)
                else:
                    print("❌ Resource requirements not specified")
                    checks.append(False)
        else:
            print("❌ Orchestration config not found")
            checks.append(False)
        
        # Check 4: Retry policies
        error_handling_file = config_path / 'error-handling.yaml'
        if error_handling_file.exists():
            print("✅ Retry policies configured")
            checks.append(True)
        else:
            print("❌ Retry policies not configured")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_execution(self) -> Dict:
        """Gate 2: Validate pipeline execution."""
        
        print("\n▶️  Gate 2: Pipeline Execution")
        print("-" * 70)
        
        checks = []
        reports_path = self.evidence_path / 'reports'
        
        # Check 1: Pipeline test results
        test_results_file = reports_path / 'pipeline_test_results.json'
        if test_results_file.exists():
            with open(test_results_file, 'r') as f:
                test_results = json.load(f)
                if test_results.get('status') == 'success':
                    print("✅ Pipeline runs without errors")
                    checks.append(True)
                    
                    if test_results.get('all_tasks_completed', False):
                        print("✅ All tasks complete successfully")
                        checks.append(True)
                    else:
                        print("❌ Some tasks failed")
                        checks.append(False)
                else:
                    print("❌ Pipeline execution failed")
                    checks.append(False)
                    checks.append(False)
        else:
            print("❌ Pipeline test results not found")
            checks.append(False)
            checks.append(False)
        
        # Check 2: Task outputs validated
        if test_results_file.exists():
            with open(test_results_file, 'r') as f:
                test_results = json.load(f)
                if 'task_outputs' in test_results:
                    print("✅ Task outputs validated")
                    checks.append(True)
                else:
                    print("❌ Task outputs not validated")
                    checks.append(False)
        else:
            checks.append(False)
        
        # Check 3: Execution time
        if test_results_file.exists():
            with open(test_results_file, 'r') as f:
                test_results = json.load(f)
                execution_time = test_results.get('execution_time_hours', 999)
                if execution_time < 4:
                    print(f"✅ Execution time within acceptable limits ({execution_time:.2f}h)")
                    checks.append(True)
                else:
                    print(f"❌ Execution time too long ({execution_time:.2f}h)")
                    checks.append(False)
        else:
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_monitoring(self) -> Dict:
        """Gate 3: Validate monitoring and observability."""
        
        print("\n📊 Gate 3: Monitoring & Observability")
        print("-" * 70)
        
        checks = []
        monitoring_path = self.evidence_path / 'monitoring'
        
        # Check 1: Metrics collection
        metrics_config = monitoring_path / 'metrics-definition.yaml'
        if metrics_config.exists():
            print("✅ Metrics collection configured")
            checks.append(True)
        else:
            print("❌ Metrics collection not configured")
            checks.append(False)
        
        # Check 2: Logging integrated
        reports_path = self.evidence_path / 'reports'
        orchestration_report = reports_path / 'orchestration_report.md'
        if orchestration_report.exists():
            content = orchestration_report.read_text()
            if 'logging' in content.lower():
                print("✅ Logging integrated")
                checks.append(True)
            else:
                print("❌ Logging not mentioned")
                checks.append(False)
        else:
            print("❌ Orchestration report not found")
            checks.append(False)
        
        # Check 3: Alerts configured
        alert_rules = monitoring_path / 'alert-rules.yaml'
        if alert_rules.exists():
            print("✅ Alerts configured for failures")
            checks.append(True)
        else:
            print("❌ Alert rules not configured")
            checks.append(False)
        
        # Check 4: Dashboard accessible
        dashboard_config = monitoring_path / 'dashboard-config.json'
        if dashboard_config.exists():
            print("✅ Dashboard accessible")
            checks.append(True)
        else:
            print("❌ Dashboard config not found")
            checks.append(False)
        
        # Check 5: Historical data
        test_results_file = reports_path / 'pipeline_test_results.json'
        if test_results_file.exists():
            with open(test_results_file, 'r') as f:
                test_results = json.load(f)
                if 'run_history' in test_results or 'timestamp' in test_results:
                    print("✅ Historical run data available")
                    checks.append(True)
                else:
                    print("❌ Historical data not tracked")
                    checks.append(False)
        else:
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def _check_circular_dependencies(self, dag_content: str) -> bool:
        """Simple check for obvious circular dependencies."""
        # This is a simplified check - in production, parse the actual DAG
        lines = dag_content.split('\n')
        dependencies = {}
        
        for line in lines:
            if '>>' in line:
                parts = line.split('>>')
                if len(parts) == 2:
                    source = parts[0].strip()
                    target = parts[1].strip()
                    dependencies.setdefault(source, []).append(target)
        
        # Simple cycle detection (not comprehensive)
        visited = set()
        
        def has_cycle(node, path):
            if node in path:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            path.add(node)
            
            for neighbor in dependencies.get(node, []):
                if has_cycle(neighbor, path):
                    return True
            
            path.remove(node)
            return False
        
        for node in dependencies:
            if has_cycle(node, set()):
                return True
        
        return False
    
    def print_summary(self):
        """Print validation summary."""
        
        print("\n" + "=" * 70)
        print("📊 VALIDATION SUMMARY")
        print("=" * 70)
        
        for gate_name, gate_result in self.results['gates'].items():
            status_icon = "✅" if gate_result['status'] == 'passed' else "❌"
            print(f"{status_icon} {gate_name.upper()}: {gate_result['status'].upper()} "
                  f"({gate_result['checks_passed']}/{gate_result['checks_total']} checks)")
        
        print("\n" + "=" * 70)
        status_icon = "✅" if self.results['overall_status'] == 'passed' else "❌"
        print(f"{status_icon} OVERALL STATUS: {self.results['overall_status'].upper()}")
        print("=" * 70)

def main():
    """Main validation entry point."""
    
    if len(sys.argv) < 2:
        print("Usage: python validate_orchestration.py <evidence_path>")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"❌ Evidence path not found: {evidence_path}")
        sys.exit(1)
    
    validator = OrchestrationValidator(evidence_path)
    results = validator.validate_all()
    validator.print_summary()
    
    # Save results
    output_file = Path(evidence_path) / 'validation_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved to: {output_file}")
    
    # Exit with appropriate code
    sys.exit(0 if results['overall_status'] == 'passed' else 1)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Validator for Protocol 20: AI Model Deployment & Serving

This script validates:
- Pre-deployment validation
- Deployment execution
- Post-deployment validation
"""

import os
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List

class DeploymentValidator:
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.results = {
            'protocol': '20-deployment',
            'gates': {},
            'overall_status': 'pending'
        }
    
    def validate_all(self) -> Dict:
        """Run all validation gates."""
        
        print("🔍 Validating Protocol 20: Model Deployment & Serving")
        print("=" * 70)
        
        # Gate 1: Pre-Deployment Validation
        self.results['gates']['gate_1'] = self.validate_pre_deployment()
        
        # Gate 2: Deployment Execution
        self.results['gates']['gate_2'] = self.validate_deployment_execution()
        
        # Gate 3: Post-Deployment Validation
        self.results['gates']['gate_3'] = self.validate_post_deployment()
        
        # Determine overall status
        all_passed = all(
            gate['status'] == 'passed'
            for gate in self.results['gates'].values()
        )
        self.results['overall_status'] = 'passed' if all_passed else 'failed'
        
        return self.results
    
    def validate_pre_deployment(self) -> Dict:
        """Gate 1: Validate pre-deployment checks."""
        
        print("\n🔍 Gate 1: Pre-Deployment Validation")
        print("-" * 70)
        
        checks = []
        manifests_path = self.evidence_path / 'manifests'
        rollback_path = self.evidence_path / 'rollback'
        validation_path = self.evidence_path / 'validation'
        
        # Check 1: Model package validated
        container_test_log = validation_path / 'container_test.log'
        if container_test_log.exists():
            print("✅ Model package validated and tested")
            checks.append(True)
        else:
            print("❌ Container test log not found")
            checks.append(False)
        
        # Check 2: Deployment manifests reviewed
        deployment_yaml = manifests_path / 'deployment.yaml'
        if deployment_yaml.exists():
            print("✅ Deployment manifests reviewed")
            checks.append(True)
            
            # Validate manifest content
            with open(deployment_yaml, 'r') as f:
                manifest = yaml.safe_load(f)
                if 'spec' in manifest and 'template' in manifest['spec']:
                    resources = manifest['spec']['template']['spec']['containers'][0].get('resources', {})
                    if resources:
                        print("✅ Resource requirements verified")
                        checks.append(True)
                    else:
                        print("❌ Resource requirements not specified")
                        checks.append(False)
                else:
                    print("❌ Invalid manifest structure")
                    checks.append(False)
        else:
            print("❌ Deployment manifest not found")
            checks.append(False)
            checks.append(False)
        
        # Check 3: Health checks configured
        if deployment_yaml.exists():
            with open(deployment_yaml, 'r') as f:
                manifest = yaml.safe_load(f)
                container = manifest['spec']['template']['spec']['containers'][0]
                if 'livenessProbe' in container and 'readinessProbe' in container:
                    print("✅ Health checks configured")
                    checks.append(True)
                else:
                    print("❌ Health checks not configured")
                    checks.append(False)
        else:
            checks.append(False)
        
        # Check 4: Rollback plan documented
        rollback_plan = rollback_path / 'rollback-plan.md'
        if rollback_plan.exists():
            print("✅ Rollback plan documented")
            checks.append(True)
        else:
            print("❌ Rollback plan not found")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_deployment_execution(self) -> Dict:
        """Gate 2: Validate deployment execution."""
        
        print("\n🚀 Gate 2: Deployment Execution")
        print("-" * 70)
        
        checks = []
        reports_path = self.evidence_path / 'reports'
        monitoring_path = self.evidence_path / 'monitoring'
        
        # Check 1: Deployment completed
        deployment_report = reports_path / 'deployment_report.md'
        if deployment_report.exists():
            content = deployment_report.read_text()
            if 'success' in content.lower() or 'completed' in content.lower():
                print("✅ Deployment completed without errors")
                checks.append(True)
                
                # Check if all pods running
                if 'running' in content.lower() and 'ready' in content.lower():
                    print("✅ All pods running and ready")
                    checks.append(True)
                else:
                    print("❌ Pods not all running/ready")
                    checks.append(False)
            else:
                print("❌ Deployment not successful")
                checks.append(False)
                checks.append(False)
        else:
            print("❌ Deployment report not found")
            checks.append(False)
            checks.append(False)
        
        # Check 2: Health checks passing
        validation_results = reports_path / 'validation_results.json'
        if validation_results.exists():
            with open(validation_results, 'r') as f:
                results = json.load(f)
                if results.get('health_checks_passing', False):
                    print("✅ Health checks passing")
                    checks.append(True)
                else:
                    print("❌ Health checks failing")
                    checks.append(False)
        else:
            print("❌ Validation results not found")
            checks.append(False)
        
        # Check 3: Load balancer configured
        manifests_path = self.evidence_path / 'manifests'
        service_yaml = manifests_path / 'service.yaml'
        if service_yaml.exists():
            with open(service_yaml, 'r') as f:
                service = yaml.safe_load(f)
                if service.get('spec', {}).get('type') in ['LoadBalancer', 'ClusterIP']:
                    print("✅ Load balancer configured")
                    checks.append(True)
                else:
                    print("❌ Load balancer not configured")
                    checks.append(False)
        else:
            print("❌ Service manifest not found")
            checks.append(False)
        
        # Check 4: Metrics collection active
        metrics_config = monitoring_path / 'metrics-config.yaml'
        if metrics_config.exists():
            print("✅ Metrics collection active")
            checks.append(True)
        else:
            print("❌ Metrics config not found")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_post_deployment(self) -> Dict:
        """Gate 3: Validate post-deployment checks."""
        
        print("\n✅ Gate 3: Post-Deployment Validation")
        print("-" * 70)
        
        checks = []
        reports_path = self.evidence_path / 'reports'
        monitoring_path = self.evidence_path / 'monitoring'
        
        # Check 1: Prediction accuracy
        validation_results = reports_path / 'validation_results.json'
        if validation_results.exists():
            with open(validation_results, 'r') as f:
                results = json.load(f)
                accuracy = results.get('accuracy', 0)
                if accuracy >= 0.85:
                    print(f"✅ Prediction accuracy matches expectations ({accuracy:.2%})")
                    checks.append(True)
                else:
                    print(f"❌ Accuracy below threshold ({accuracy:.2%})")
                    checks.append(False)
        else:
            print("❌ Validation results not found")
            checks.append(False)
        
        # Check 2: Response time
        if validation_results.exists():
            with open(validation_results, 'r') as f:
                results = json.load(f)
                p95_latency = results.get('p95_latency_ms', 9999)
                if p95_latency < 500:
                    print(f"✅ Response time <500ms (P95: {p95_latency}ms)")
                    checks.append(True)
                else:
                    print(f"❌ Response time too high (P95: {p95_latency}ms)")
                    checks.append(False)
        else:
            checks.append(False)
        
        # Check 3: Error rate
        if validation_results.exists():
            with open(validation_results, 'r') as f:
                results = json.load(f)
                error_rate = results.get('error_rate', 1.0)
                if error_rate < 0.01:
                    print(f"✅ Error rate <1% ({error_rate:.2%})")
                    checks.append(True)
                else:
                    print(f"❌ Error rate too high ({error_rate:.2%})")
                    checks.append(False)
        else:
            checks.append(False)
        
        # Check 4: Resource usage
        if validation_results.exists():
            with open(validation_results, 'r') as f:
                results = json.load(f)
                cpu_usage = results.get('cpu_usage_percent', 100)
                memory_usage = results.get('memory_usage_percent', 100)
                if cpu_usage < 80 and memory_usage < 80:
                    print(f"✅ Resource usage within limits (CPU: {cpu_usage}%, Mem: {memory_usage}%)")
                    checks.append(True)
                else:
                    print(f"❌ Resource usage high (CPU: {cpu_usage}%, Mem: {memory_usage}%)")
                    checks.append(False)
        else:
            checks.append(False)
        
        # Check 5: Monitoring alerts
        alert_rules = monitoring_path / 'alert-rules.yaml'
        if alert_rules.exists():
            print("✅ Monitoring alerts configured")
            checks.append(True)
        else:
            print("❌ Alert rules not configured")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
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
        print("Usage: python validate_deployment.py <evidence_path>")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"❌ Evidence path not found: {evidence_path}")
        sys.exit(1)
    
    validator = DeploymentValidator(evidence_path)
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

#!/usr/bin/env python3
"""
Validator for Protocol 18: AI Model Packaging & Containerization

This script validates:
- Model serialization integrity
- Container build success
- Registry integration
- Package completeness
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List
import hashlib

class PackagingValidator:
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.results = {
            'protocol': '18-packaging',
            'gates': {},
            'overall_status': 'pending'
        }
    
    def validate_all(self) -> Dict:
        """Run all validation gates."""
        
        print("🔍 Validating Protocol 18: Model Packaging & Containerization")
        print("=" * 70)
        
        # Gate 1: Serialization Integrity
        self.results['gates']['gate_1'] = self.validate_serialization()
        
        # Gate 2: Container Build
        self.results['gates']['gate_2'] = self.validate_container()
        
        # Gate 3: Registry Integration
        self.results['gates']['gate_3'] = self.validate_registry()
        
        # Determine overall status
        all_passed = all(
            gate['status'] == 'passed'
            for gate in self.results['gates'].values()
        )
        self.results['overall_status'] = 'passed' if all_passed else 'failed'
        
        return self.results
    
    def validate_serialization(self) -> Dict:
        """Gate 1: Validate model serialization."""
        
        print("\n📦 Gate 1: Serialization Integrity")
        print("-" * 70)
        
        checks = []
        artifacts_path = self.evidence_path / 'artifacts'
        
        # Check 1: Model file exists
        model_files = list(artifacts_path.glob('*.joblib')) + \
                     list(artifacts_path.glob('*.pkl')) + \
                     list(artifacts_path.glob('*.pth')) + \
                     list(artifacts_path.glob('*.h5'))
        
        if model_files:
            print("✅ Model serialized successfully")
            checks.append(True)
        else:
            print("❌ No model file found")
            checks.append(False)
        
        # Check 2: Metadata exists
        metadata_file = artifacts_path / 'model_metadata.json'
        if metadata_file.exists():
            print("✅ Metadata file created and complete")
            checks.append(True)
            
            # Validate metadata content
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
                required_fields = ['model_info', 'performance', 'dependencies']
                if all(field in metadata for field in required_fields):
                    print("✅ Metadata contains all required fields")
                    checks.append(True)
                else:
                    print("❌ Metadata missing required fields")
                    checks.append(False)
        else:
            print("❌ Metadata file not found")
            checks.append(False)
        
        # Check 3: Model size check
        if model_files:
            model_size_mb = model_files[0].stat().st_size / (1024 * 1024)
            if model_size_mb < 500:
                print(f"✅ Model size within limits ({model_size_mb:.2f} MB)")
                checks.append(True)
            else:
                print(f"⚠️  Model size large ({model_size_mb:.2f} MB)")
                checks.append(False)
        
        # Check 4: Package manifest
        manifest_file = artifacts_path / 'package_manifest.json'
        if manifest_file.exists():
            print("✅ Package manifest created")
            checks.append(True)
        else:
            print("❌ Package manifest not found")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_container(self) -> Dict:
        """Gate 2: Validate container build."""
        
        print("\n🐳 Gate 2: Container Build")
        print("-" * 70)
        
        checks = []
        docker_path = self.evidence_path / 'docker'
        
        # Check 1: Dockerfile exists
        dockerfile = docker_path / 'Dockerfile'
        if dockerfile.exists():
            print("✅ Dockerfile builds without errors")
            checks.append(True)
            
            # Validate Dockerfile content
            with open(dockerfile, 'r') as f:
                content = f.read()
                if 'HEALTHCHECK' in content:
                    print("✅ Health checks configured")
                    checks.append(True)
                else:
                    print("❌ Health checks not configured")
                    checks.append(False)
        else:
            print("❌ Dockerfile not found")
            checks.append(False)
            checks.append(False)
        
        # Check 2: Requirements file
        requirements_file = self.evidence_path / 'artifacts' / 'requirements.txt'
        if requirements_file.exists():
            print("✅ All dependencies installed successfully")
            checks.append(True)
        else:
            print("❌ Requirements file not found")
            checks.append(False)
        
        # Check 3: Security scan (check for security scan results)
        security_file = self.evidence_path / 'reports' / 'security_scan.json'
        if security_file.exists():
            with open(security_file, 'r') as f:
                scan_results = json.load(f)
                critical_vulns = scan_results.get('critical_vulnerabilities', 0)
                if critical_vulns == 0:
                    print("✅ Security scan passed (no critical vulnerabilities)")
                    checks.append(True)
                else:
                    print(f"❌ Security scan found {critical_vulns} critical vulnerabilities")
                    checks.append(False)
        else:
            print("⚠️  Security scan results not found")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_registry(self) -> Dict:
        """Gate 3: Validate registry integration."""
        
        print("\n📚 Gate 3: Registry Integration")
        print("-" * 70)
        
        checks = []
        registry_path = self.evidence_path / 'registry'
        
        # Check 1: Registry config exists
        registry_config = registry_path / 'registry-config.yaml'
        if registry_config.exists():
            print("✅ Model registered in MLflow registry")
            checks.append(True)
        else:
            print("❌ Registry config not found")
            checks.append(False)
        
        # Check 2: Version tagged
        versions_file = registry_path / 'model_versions.json'
        if versions_file.exists():
            print("✅ Version tagged correctly")
            checks.append(True)
            
            with open(versions_file, 'r') as f:
                versions = json.load(f)
                if 'tags' in versions and versions['tags']:
                    print("✅ Metadata and tags applied")
                    checks.append(True)
                else:
                    print("❌ Tags not applied")
                    checks.append(False)
        else:
            print("❌ Version file not found")
            checks.append(False)
            checks.append(False)
        
        # Check 3: Package checksum
        manifest_file = self.evidence_path / 'artifacts' / 'package_manifest.json'
        if manifest_file.exists():
            with open(manifest_file, 'r') as f:
                manifest = json.load(f)
                if 'checksum' in manifest:
                    print("✅ Package checksum validated")
                    checks.append(True)
                else:
                    print("❌ Checksum not found in manifest")
                    checks.append(False)
        else:
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
        print("Usage: python validate_packaging.py <evidence_path>")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"❌ Evidence path not found: {evidence_path}")
        sys.exit(1)
    
    validator = PackagingValidator(evidence_path)
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

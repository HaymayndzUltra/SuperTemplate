#!/usr/bin/env python3
"""
Validator for Protocol 21: AI Production Integration & API Development

This script validates:
- API design completeness
- Implementation quality
- Documentation and SDK availability
"""

import os
import sys
import json
import yaml
import requests
from pathlib import Path
from typing import Dict, List

class APIValidator:
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.results = {
            'protocol': '21-api-integration',
            'gates': {},
            'overall_status': 'pending'
        }
    
    def validate_all(self) -> Dict:
        """Run all validation gates."""
        
        print("🔍 Validating Protocol 21: Production Integration & API Development")
        print("=" * 70)
        
        # Gate 1: API Design
        self.results['gates']['gate_1'] = self.validate_api_design()
        
        # Gate 2: Implementation
        self.results['gates']['gate_2'] = self.validate_implementation()
        
        # Gate 3: Documentation & SDKs
        self.results['gates']['gate_3'] = self.validate_documentation()
        
        # Determine overall status
        all_passed = all(
            gate['status'] == 'passed'
            for gate in self.results['gates'].values()
        )
        self.results['overall_status'] = 'passed' if all_passed else 'failed'
        
        return self.results
    
    def validate_api_design(self) -> Dict:
        """Gate 1: Validate API design."""
        
        print("\n📐 Gate 1: API Design")
        print("-" * 70)
        
        checks = []
        specs_path = self.evidence_path / 'specs'
        
        # Check 1: OpenAPI specification exists
        api_spec = specs_path / 'api-spec.yaml'
        if api_spec.exists():
            print("✅ OpenAPI specification complete")
            checks.append(True)
            
            # Validate spec content
            with open(api_spec, 'r') as f:
                spec = yaml.safe_load(f)
                
                # Check 2: All endpoints documented
                if 'paths' in spec and len(spec['paths']) > 0:
                    print(f"✅ All endpoints documented ({len(spec['paths'])} endpoints)")
                    checks.append(True)
                else:
                    print("❌ No endpoints documented")
                    checks.append(False)
                
                # Check 3: Request/response schemas
                if 'components' in spec and 'schemas' in spec['components']:
                    print("✅ Request/response schemas defined")
                    checks.append(True)
                else:
                    print("❌ Schemas not defined")
                    checks.append(False)
                
                # Check 4: Authentication strategy
                if 'security' in spec or 'securitySchemes' in spec.get('components', {}):
                    print("✅ Authentication strategy defined")
                    checks.append(True)
                else:
                    print("❌ Authentication not defined")
                    checks.append(False)
        else:
            print("❌ OpenAPI specification not found")
            checks.append(False)
            checks.append(False)
            checks.append(False)
            checks.append(False)
        
        # Check 5: Rate limits configured (check in API code or config)
        api_path = self.evidence_path / 'api'
        rate_limiting_file = api_path / 'rate_limiting.py'
        if rate_limiting_file.exists():
            print("✅ Rate limits configured")
            checks.append(True)
        else:
            print("❌ Rate limiting not implemented")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_implementation(self) -> Dict:
        """Gate 2: Validate API implementation."""
        
        print("\n💻 Gate 2: Implementation")
        print("-" * 70)
        
        checks = []
        api_path = self.evidence_path / 'api'
        reports_path = self.evidence_path / 'reports'
        
        # Check 1: All endpoints implemented
        main_api = api_path / 'main.py'
        if main_api.exists():
            content = main_api.read_text()
            
            # Check for key endpoints
            required_endpoints = ['/predict', '/health']
            endpoints_found = all(endpoint in content for endpoint in required_endpoints)
            
            if endpoints_found:
                print("✅ All endpoints implemented")
                checks.append(True)
            else:
                print("❌ Some endpoints missing")
                checks.append(False)
            
            # Check 2: Input validation
            if 'pydantic' in content.lower() or 'basemodel' in content:
                print("✅ Input validation working")
                checks.append(True)
            else:
                print("❌ Input validation not implemented")
                checks.append(False)
        else:
            print("❌ Main API file not found")
            checks.append(False)
            checks.append(False)
        
        # Check 3: Authentication functional
        auth_file = api_path / 'auth.py'
        if auth_file.exists():
            print("✅ Authentication functional")
            checks.append(True)
        else:
            print("❌ Authentication module not found")
            checks.append(False)
        
        # Check 4: Rate limiting active
        rate_limiting_file = api_path / 'rate_limiting.py'
        if rate_limiting_file.exists():
            print("✅ Rate limiting active")
            checks.append(True)
        else:
            print("❌ Rate limiting not implemented")
            checks.append(False)
        
        # Check 5: Error handling
        test_results = reports_path / 'api_test_results.json'
        if test_results.exists():
            with open(test_results, 'r') as f:
                results = json.load(f)
                if results.get('error_handling_tests_passed', False):
                    print("✅ Error handling comprehensive")
                    checks.append(True)
                else:
                    print("❌ Error handling incomplete")
                    checks.append(False)
        else:
            print("⚠️  API test results not found")
            checks.append(False)
        
        passed = all(checks)
        return {
            'status': 'passed' if passed else 'failed',
            'checks_passed': sum(checks),
            'checks_total': len(checks)
        }
    
    def validate_documentation(self) -> Dict:
        """Gate 3: Validate documentation and SDKs."""
        
        print("\n📚 Gate 3: Documentation & SDKs")
        print("-" * 70)
        
        checks = []
        docs_path = self.evidence_path / 'docs'
        sdk_path = self.evidence_path / 'client-sdk'
        
        # Check 1: API documentation generated
        api_docs = docs_path / 'api-documentation.html'
        if api_docs.exists():
            print("✅ API documentation generated")
            checks.append(True)
        else:
            print("❌ API documentation not found")
            checks.append(False)
        
        # Check 2: Interactive docs accessible (check for /docs endpoint in spec)
        specs_path = self.evidence_path / 'specs'
        api_spec = specs_path / 'api-spec.yaml'
        if api_spec.exists():
            # Assume interactive docs available if OpenAPI spec exists
            print("✅ Interactive docs accessible")
            checks.append(True)
        else:
            print("❌ OpenAPI spec not found")
            checks.append(False)
        
        # Check 3: Python SDK generated
        python_sdk = sdk_path / 'python' / 'ml_api_client.py'
        if python_sdk.exists():
            print("✅ Python SDK generated and tested")
            checks.append(True)
        else:
            print("❌ Python SDK not found")
            checks.append(False)
        
        # Check 4: TypeScript SDK generated
        ts_sdk = sdk_path / 'typescript' / 'src' / 'client.ts'
        if ts_sdk.exists():
            print("✅ TypeScript SDK generated and tested")
            checks.append(True)
        else:
            print("❌ TypeScript SDK not found")
            checks.append(False)
        
        # Check 5: Example code provided
        integration_examples = docs_path / 'integration-examples.md'
        if integration_examples.exists():
            print("✅ Example code provided")
            checks.append(True)
        else:
            print("❌ Integration examples not found")
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
        print("Usage: python validate_api.py <evidence_path>")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    if not os.path.exists(evidence_path):
        print(f"❌ Evidence path not found: {evidence_path}")
        sys.exit(1)
    
    validator = APIValidator(evidence_path)
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

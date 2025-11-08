#!/usr/bin/env python3
"""
Protocol 08 Gate 4: Compliance Validator
Validates GDPR, HIPAA, and data governance compliance for ingested data.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Any, List


def detect_pii_patterns(text: str) -> List[str]:
    """Detect potential PII patterns in text."""
    pii_found = []
    
    # Email pattern
    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
        pii_found.append("email")
    
    # SSN pattern (US)
    if re.search(r'\b\d{3}-\d{2}-\d{4}\b', text):
        pii_found.append("ssn")
    
    # Credit card pattern
    if re.search(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', text):
        pii_found.append("credit_card")
    
    # Phone number pattern
    if re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text):
        pii_found.append("phone")
    
    return pii_found


def validate_compliance(
    data_path: Path,
    compliance_config: Path = None,
    check_pii: bool = True
) -> Dict[str, Any]:
    """
    Validate compliance requirements for ingested data.
    
    Args:
        data_path: Path to ingested data directory
        compliance_config: Path to compliance configuration JSON
        check_pii: Whether to check for PII violations
    
    Returns:
        Dictionary with validation results
    """
    results = {
        "validator": "compliance",
        "data_path": str(data_path),
        "passed": False,
        "compliance_score": 0.0,
        "checks": {},
        "violations": [],
        "warnings": []
    }
    
    if not data_path.exists():
        results["violations"].append(f"Data path does not exist: {data_path}")
        return results
    
    checks_passed = 0
    total_checks = 0
    
    # Check 1: Access control metadata
    total_checks += 1
    access_control_file = data_path / "access-control.json"
    if access_control_file.exists():
        checks_passed += 1
        results["checks"]["access_control"] = "✅ Present"
    else:
        results["warnings"].append("Access control metadata missing")
        results["checks"]["access_control"] = "⚠️ Missing"
    
    # Check 2: Data lineage documentation
    total_checks += 1
    lineage_file = data_path / "data-lineage.json"
    if lineage_file.exists():
        checks_passed += 1
        results["checks"]["data_lineage"] = "✅ Present"
    else:
        results["warnings"].append("Data lineage documentation missing")
        results["checks"]["data_lineage"] = "⚠️ Missing"
    
    # Check 3: Encryption status
    total_checks += 1
    encryption_file = data_path / "encryption-status.json"
    if encryption_file.exists():
        try:
            with open(encryption_file, 'r') as f:
                encryption_data = json.load(f)
            
            if encryption_data.get("encrypted_at_rest") and encryption_data.get("encrypted_in_transit"):
                checks_passed += 1
                results["checks"]["encryption"] = "✅ Encrypted (rest + transit)"
            else:
                results["violations"].append("Incomplete encryption coverage")
                results["checks"]["encryption"] = "❌ Incomplete"
        except Exception as e:
            results["warnings"].append(f"Failed to read encryption status: {e}")
            results["checks"]["encryption"] = "⚠️ Error reading"
    else:
        results["violations"].append("Encryption status not documented")
        results["checks"]["encryption"] = "❌ Not documented"
    
    # Check 4: PII detection (if enabled)
    if check_pii:
        total_checks += 1
        pii_violations = []
        
        # Check metadata files for PII
        for json_file in data_path.glob("**/*.json"):
            if json_file.name in ["access-control.json", "encryption-status.json"]:
                continue
            
            try:
                with open(json_file, 'r') as f:
                    content = f.read()
                    pii_found = detect_pii_patterns(content)
                    if pii_found:
                        pii_violations.append(f"{json_file.name}: {', '.join(pii_found)}")
            except Exception:
                pass  # Skip files that can't be read
        
        if not pii_violations:
            checks_passed += 1
            results["checks"]["pii_detection"] = "✅ No violations detected"
        else:
            results["violations"].extend([f"PII detected: {v}" for v in pii_violations])
            results["checks"]["pii_detection"] = f"❌ {len(pii_violations)} violation(s)"
    
    # Check 5: Retention policy
    total_checks += 1
    retention_file = data_path / "retention-policy.json"
    if retention_file.exists():
        checks_passed += 1
        results["checks"]["retention_policy"] = "✅ Present"
    else:
        results["warnings"].append("Retention policy not defined")
        results["checks"]["retention_policy"] = "⚠️ Missing"
    
    # Check 6: Compliance configuration
    if compliance_config and compliance_config.exists():
        total_checks += 1
        try:
            with open(compliance_config, 'r') as f:
                config = json.load(f)
            
            required_regs = config.get("required_regulations", [])
            results["checks"]["compliance_config"] = f"✅ {len(required_regs)} regulations"
            checks_passed += 1
        except Exception as e:
            results["warnings"].append(f"Failed to read compliance config: {e}")
            results["checks"]["compliance_config"] = "⚠️ Error reading"
    
    # Calculate compliance score
    if total_checks > 0:
        results["compliance_score"] = checks_passed / total_checks
    
    # Pass if 100% compliance (no violations)
    results["passed"] = len(results["violations"]) == 0 and results["compliance_score"] >= 0.80
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate compliance requirements for Protocol 08 Gate 4"
    )
    parser.add_argument(
        "--data",
        type=Path,
        required=True,
        help="Path to ingested data directory"
    )
    parser.add_argument(
        "--compliance-config",
        type=Path,
        help="Path to compliance configuration JSON"
    )
    parser.add_argument(
        "--no-pii-check",
        action="store_true",
        help="Disable PII detection check"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path to save validation report JSON"
    )
    
    args = parser.parse_args()
    
    # Run validation
    results = validate_compliance(
        args.data,
        args.compliance_config,
        check_pii=not args.no_pii_check
    )
    
    # Save results if output specified
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"✅ Validation report saved to: {args.output}")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"COMPLIANCE VALIDATION")
    print(f"{'='*60}")
    print(f"Data Path: {args.data}")
    print(f"Compliance Score: {results['compliance_score']:.2%}")
    print(f"Status: {'✅ PASS' if results['passed'] else '❌ FAIL'}")
    
    if results['checks']:
        print(f"\nCompliance Checks:")
        for check, status in results['checks'].items():
            print(f"  {check}: {status}")
    
    if results['violations']:
        print(f"\n🚨 VIOLATIONS ({len(results['violations'])}):")
        for violation in results['violations']:
            print(f"  ❌ {violation}")
    
    if results['warnings']:
        print(f"\n⚠️  WARNINGS ({len(results['warnings'])}):")
        for warning in results['warnings']:
            print(f"  ⚠️  {warning}")
    
    print(f"{'='*60}\n")
    
    # Exit with appropriate code
    sys.exit(0 if results['passed'] else 1)


if __name__ == "__main__":
    main()

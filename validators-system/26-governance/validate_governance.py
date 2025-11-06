#!/usr/bin/env python3
"""
Validator for Protocol 26: AI Model Governance & Audit Trail
Validates model registry, audit trails, RBAC, and compliance reporting.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple


def validate_model_registry(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate model registry and versioning."""
    errors = []
    
    governance_policy = evidence_path / "governance-policy.md"
    if not governance_policy.exists():
        errors.append("Missing governance-policy.md")
        return False, errors
    
    content = governance_policy.read_text()
    
    # Check registry requirements
    required_elements = [
        "model versioning",
        "model lineage",
        "metadata tracking",
        "model approval",
        "model retirement"
    ]
    
    for element in required_elements:
        if element.lower() not in content.lower():
            errors.append(f"Missing registry element: {element}")
    
    return len(errors) == 0, errors


def validate_audit_trail(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate audit trail and change log."""
    errors = []
    
    audit_log = evidence_path / "audit-log.json"
    if not audit_log.exists():
        errors.append("Missing audit-log.json")
        return False, errors
    
    try:
        with open(audit_log, 'r') as f:
            audit_data = json.load(f)
        
        # Check audit log structure
        required_fields = [
            "timestamp",
            "user",
            "action",
            "resource",
            "status"
        ]
        
        if isinstance(audit_data, list) and len(audit_data) > 0:
            first_entry = audit_data[0]
            for field in required_fields:
                if field not in first_entry:
                    errors.append(f"Missing audit field: {field}")
        elif isinstance(audit_data, dict):
            if "entries" not in audit_data:
                errors.append("Audit log missing 'entries' array")
        else:
            errors.append("Invalid audit log format")
            
    except json.JSONDecodeError:
        errors.append("Invalid JSON in audit-log.json")
    
    return len(errors) == 0, errors


def validate_compliance_reporting(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate compliance reporting and RBAC."""
    errors = []
    
    compliance_report = evidence_path / "compliance-report.md"
    if not compliance_report.exists():
        errors.append("Missing compliance-report.md")
        return False, errors
    
    content = compliance_report.read_text()
    
    # Check compliance elements
    required_elements = [
        "RBAC",
        "access control",
        "role definition",
        "permission matrix",
        "compliance status",
        "audit findings"
    ]
    
    for element in required_elements:
        if element.lower() not in content.lower():
            errors.append(f"Missing compliance element: {element}")
    
    # Check for regulatory frameworks
    frameworks = ["GDPR", "ISO", "SOC"]
    framework_found = any(fw in content for fw in frameworks)
    if not framework_found:
        errors.append("No regulatory framework compliance documented")
    
    return len(errors) == 0, errors


def validate_protocol_26(protocol_path: str) -> Dict:
    """Main validation function for Protocol 26."""
    
    protocol_path = Path(protocol_path)
    evidence_path = protocol_path.parent.parent / "evidence" / "protocol-26-governance"
    
    results = {
        "protocol_id": "26",
        "protocol_name": "AI Model Governance & Audit Trail",
        "validation_status": "PASS",
        "gates": {},
        "overall_score": 0.0,
        "errors": []
    }
    
    # Gate 1: Model Registry
    gate1_pass, gate1_errors = validate_model_registry(evidence_path)
    results["gates"]["gate_1_registry"] = {
        "name": "Model Registry & Versioning",
        "status": "PASS" if gate1_pass else "FAIL",
        "errors": gate1_errors
    }
    
    # Gate 2: Audit Trail
    gate2_pass, gate2_errors = validate_audit_trail(evidence_path)
    results["gates"]["gate_2_audit"] = {
        "name": "Immutable Audit Trail",
        "status": "PASS" if gate2_pass else "FAIL",
        "errors": gate2_errors
    }
    
    # Gate 3: Compliance Reporting
    gate3_pass, gate3_errors = validate_compliance_reporting(evidence_path)
    results["gates"]["gate_3_compliance"] = {
        "name": "RBAC & Compliance Reporting",
        "status": "PASS" if gate3_pass else "FAIL",
        "errors": gate3_errors
    }
    
    # Calculate overall score
    gates_passed = sum([gate1_pass, gate2_pass, gate3_pass])
    results["overall_score"] = (gates_passed / 3) * 100
    
    # Determine overall status
    if gates_passed < 3:
        results["validation_status"] = "FAIL"
        results["errors"] = gate1_errors + gate2_errors + gate3_errors
    
    return results


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: validate_governance.py <protocol_path>")
        sys.exit(1)
    
    result = validate_protocol_26(sys.argv[1])
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result["validation_status"] == "PASS" else 1)

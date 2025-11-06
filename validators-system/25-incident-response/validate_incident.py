#!/usr/bin/env python3
"""
Validator for Protocol 25: AI Incident Response & Model Rollback
Validates incident classification, response procedures, and rollback automation.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple


def validate_incident_classification(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate incident classification system."""
    errors = []
    
    playbook = evidence_path / "incident-playbook.md"
    if not playbook.exists():
        errors.append("Missing incident-playbook.md")
        return False, errors
    
    content = playbook.read_text()
    
    # Check severity levels
    severity_levels = ["P0", "P1", "P2", "P3", "P4"]
    for level in severity_levels:
        if level not in content:
            errors.append(f"Missing severity level: {level}")
    
    # Check required sections
    required_sections = [
        "incident classification",
        "response time",
        "escalation path",
        "notification procedure"
    ]
    
    for section in required_sections:
        if section.lower() not in content.lower():
            errors.append(f"Missing section: {section}")
    
    return len(errors) == 0, errors


def validate_rollback_automation(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate automated rollback procedures."""
    errors = []
    
    rollback_script = evidence_path / "rollback-script.sh"
    if not rollback_script.exists():
        errors.append("Missing rollback-script.sh")
        return False, errors
    
    content = rollback_script.read_text()
    
    # Check rollback components
    required_components = [
        "#!/bin/bash",
        "backup",
        "restore",
        "health_check",
        "rollback"
    ]
    
    for component in required_components:
        if component not in content:
            errors.append(f"Missing rollback component: {component}")
    
    # Check execution time requirement (< 2 minutes)
    if "timeout" not in content.lower():
        errors.append("Missing timeout configuration for 2-minute requirement")
    
    return len(errors) == 0, errors


def validate_postmortem_process(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate post-incident review process."""
    errors = []
    
    postmortem_template = evidence_path / "postmortem-template.md"
    if not postmortem_template.exists():
        errors.append("Missing postmortem-template.md")
        return False, errors
    
    content = postmortem_template.read_text()
    
    # Check postmortem sections
    required_sections = [
        "incident summary",
        "timeline",
        "root cause",
        "impact",
        "resolution",
        "action items",
        "lessons learned"
    ]
    
    for section in required_sections:
        if section.lower() not in content.lower():
            errors.append(f"Missing postmortem section: {section}")
    
    return len(errors) == 0, errors


def validate_protocol_25(protocol_path: str) -> Dict:
    """Main validation function for Protocol 25."""
    
    protocol_path = Path(protocol_path)
    evidence_path = protocol_path.parent.parent / "evidence" / "protocol-25-incident-response"
    
    results = {
        "protocol_id": "25",
        "protocol_name": "AI Incident Response & Model Rollback",
        "validation_status": "PASS",
        "gates": {},
        "overall_score": 0.0,
        "errors": []
    }
    
    # Gate 1: Incident Classification
    gate1_pass, gate1_errors = validate_incident_classification(evidence_path)
    results["gates"]["gate_1_classification"] = {
        "name": "Incident Classification System",
        "status": "PASS" if gate1_pass else "FAIL",
        "errors": gate1_errors
    }
    
    # Gate 2: Rollback Automation
    gate2_pass, gate2_errors = validate_rollback_automation(evidence_path)
    results["gates"]["gate_2_rollback"] = {
        "name": "Automated Rollback (< 2 min)",
        "status": "PASS" if gate2_pass else "FAIL",
        "errors": gate2_errors
    }
    
    # Gate 3: Postmortem Process
    gate3_pass, gate3_errors = validate_postmortem_process(evidence_path)
    results["gates"]["gate_3_postmortem"] = {
        "name": "Post-Incident Review Process",
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
        print("Usage: validate_incident.py <protocol_path>")
        sys.exit(1)
    
    result = validate_protocol_25(sys.argv[1])
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result["validation_status"] == "PASS" else 1)

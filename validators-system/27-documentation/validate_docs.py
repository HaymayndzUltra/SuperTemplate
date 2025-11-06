#!/usr/bin/env python3
"""
Validator for Protocol 27: AI Documentation & Knowledge Transfer
Validates model cards, runbooks, training materials, and knowledge base.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple


def validate_model_card(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate model card documentation."""
    errors = []
    
    model_card = evidence_path / "model-card.md"
    if not model_card.exists():
        errors.append("Missing model-card.md")
        return False, errors
    
    content = model_card.read_text()
    
    # Check required model card sections
    required_sections = [
        "model details",
        "intended use",
        "training data",
        "performance metrics",
        "fairness metrics",
        "limitations",
        "ethical considerations",
        "caveats and recommendations"
    ]
    
    for section in required_sections:
        if section.lower() not in content.lower():
            errors.append(f"Missing model card section: {section}")
    
    return len(errors) == 0, errors


def validate_runbook(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate operational runbook."""
    errors = []
    
    runbook = evidence_path / "runbook.md"
    if not runbook.exists():
        errors.append("Missing runbook.md")
        return False, errors
    
    content = runbook.read_text()
    
    # Check runbook sections
    required_sections = [
        "deployment",
        "troubleshooting",
        "monitoring",
        "common issues",
        "escalation",
        "rollback procedure",
        "health checks"
    ]
    
    for section in required_sections:
        if section.lower() not in content.lower():
            errors.append(f"Missing runbook section: {section}")
    
    return len(errors) == 0, errors


def validate_training_materials(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate training materials and knowledge transfer."""
    errors = []
    
    training_guide = evidence_path / "training-guide.md"
    if not training_guide.exists():
        errors.append("Missing training-guide.md")
        return False, errors
    
    content = training_guide.read_text()
    
    # Check training components
    required_components = [
        "learning objectives",
        "prerequisites",
        "training modules",
        "hands-on exercises",
        "assessment",
        "certification",
        "resources"
    ]
    
    for component in required_components:
        if component.lower() not in content.lower():
            errors.append(f"Missing training component: {component}")
    
    # Check for architecture diagrams reference
    if "diagram" not in content.lower() and "architecture" not in content.lower():
        errors.append("Missing architecture diagram reference")
    
    return len(errors) == 0, errors


def validate_protocol_27(protocol_path: str) -> Dict:
    """Main validation function for Protocol 27."""
    
    protocol_path = Path(protocol_path)
    evidence_path = protocol_path.parent.parent / "evidence" / "protocol-27-documentation"
    
    results = {
        "protocol_id": "27",
        "protocol_name": "AI Documentation & Knowledge Transfer",
        "validation_status": "PASS",
        "gates": {},
        "overall_score": 0.0,
        "errors": []
    }
    
    # Gate 1: Model Card
    gate1_pass, gate1_errors = validate_model_card(evidence_path)
    results["gates"]["gate_1_model_card"] = {
        "name": "Model Card Documentation",
        "status": "PASS" if gate1_pass else "FAIL",
        "errors": gate1_errors
    }
    
    # Gate 2: Operational Runbook
    gate2_pass, gate2_errors = validate_runbook(evidence_path)
    results["gates"]["gate_2_runbook"] = {
        "name": "Operational Runbook",
        "status": "PASS" if gate2_pass else "FAIL",
        "errors": gate2_errors
    }
    
    # Gate 3: Training Materials
    gate3_pass, gate3_errors = validate_training_materials(evidence_path)
    results["gates"]["gate_3_training"] = {
        "name": "Training & Knowledge Transfer",
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
        print("Usage: validate_docs.py <protocol_path>")
        sys.exit(1)
    
    result = validate_protocol_27(sys.argv[1])
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result["validation_status"] == "PASS" else 1)

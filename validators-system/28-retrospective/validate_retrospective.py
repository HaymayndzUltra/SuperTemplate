#!/usr/bin/env python3
"""
Validator for Protocol 28: AI Project Retrospective & Continuous Improvement
Validates retrospective process, lessons learned, and improvement tracking.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple


def validate_retrospective_report(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate retrospective meeting report."""
    errors = []
    
    retro_report = evidence_path / "retrospective-report.md"
    if not retro_report.exists():
        errors.append("Missing retrospective-report.md")
        return False, errors
    
    content = retro_report.read_text()
    
    # Check retrospective sections (Starfish format)
    required_sections = [
        "keep doing",
        "less of",
        "more of",
        "stop doing",
        "start doing",
        "action items",
        "participants"
    ]
    
    for section in required_sections:
        if section.lower() not in content.lower():
            errors.append(f"Missing retrospective section: {section}")
    
    return len(errors) == 0, errors


def validate_lessons_learned(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate lessons learned documentation."""
    errors = []
    
    lessons_learned = evidence_path / "lessons-learned.md"
    if not lessons_learned.exists():
        errors.append("Missing lessons-learned.md")
        return False, errors
    
    content = lessons_learned.read_text()
    
    # Check lessons learned structure
    required_elements = [
        "what went well",
        "what didn't go well",
        "what we learned",
        "best practices",
        "anti-patterns",
        "recommendations"
    ]
    
    for element in required_elements:
        if element.lower() not in content.lower():
            errors.append(f"Missing lessons learned element: {element}")
    
    # Check for metrics review
    metrics_keywords = ["metric", "performance", "success rate", "kpi"]
    metrics_found = any(keyword in content.lower() for keyword in metrics_keywords)
    if not metrics_found:
        errors.append("Missing success metrics review")
    
    return len(errors) == 0, errors


def validate_improvement_backlog(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate continuous improvement backlog."""
    errors = []
    
    improvement_backlog = evidence_path / "improvement-backlog.md"
    if not improvement_backlog.exists():
        errors.append("Missing improvement-backlog.md")
        return False, errors
    
    content = improvement_backlog.read_text()
    
    # Check backlog structure
    required_fields = [
        "priority",
        "owner",
        "status",
        "description",
        "acceptance criteria"
    ]
    
    for field in required_fields:
        if field.lower() not in content.lower():
            errors.append(f"Missing backlog field: {field}")
    
    # Check for tracking mechanism
    tracking_keywords = ["tracked", "jira", "github", "issue", "ticket"]
    tracking_found = any(keyword in content.lower() for keyword in tracking_keywords)
    if not tracking_found:
        errors.append("Missing improvement tracking mechanism")
    
    return len(errors) == 0, errors


def validate_protocol_28(protocol_path: str) -> Dict:
    """Main validation function for Protocol 28."""
    
    protocol_path = Path(protocol_path)
    evidence_path = protocol_path.parent.parent / "evidence" / "protocol-28-retrospective"
    
    results = {
        "protocol_id": "28",
        "protocol_name": "AI Project Retrospective & Continuous Improvement",
        "validation_status": "PASS",
        "gates": {},
        "overall_score": 0.0,
        "errors": []
    }
    
    # Gate 1: Retrospective Report
    gate1_pass, gate1_errors = validate_retrospective_report(evidence_path)
    results["gates"]["gate_1_retrospective"] = {
        "name": "Retrospective Meeting Report",
        "status": "PASS" if gate1_pass else "FAIL",
        "errors": gate1_errors
    }
    
    # Gate 2: Lessons Learned
    gate2_pass, gate2_errors = validate_lessons_learned(evidence_path)
    results["gates"]["gate_2_lessons"] = {
        "name": "Lessons Learned & Best Practices",
        "status": "PASS" if gate2_pass else "FAIL",
        "errors": gate2_errors
    }
    
    # Gate 3: Improvement Backlog
    gate3_pass, gate3_errors = validate_improvement_backlog(evidence_path)
    results["gates"]["gate_3_improvement"] = {
        "name": "Continuous Improvement Backlog",
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
        print("Usage: validate_retrospective.py <protocol_path>")
        sys.exit(1)
    
    result = validate_protocol_28(sys.argv[1])
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result["validation_status"] == "PASS" else 1)

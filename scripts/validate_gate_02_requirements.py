#!/usr/bin/env python3
"""Gate 2 validator for Protocol 02: Requirement Completeness Gate.

Validates MVP features, optional backlog, and technical constraints completeness ≥ 0.9.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def validate_requirements(
    discovery_form_path: Path,
    scope_clarification_path: Path,
    threshold: float = 0.9,
) -> dict:
    """Validate requirement completeness.
    
    Args:
        discovery_form_path: Path to client-discovery-form.md
        scope_clarification_path: Path to scope-clarification.md
        threshold: Minimum completeness score (default 0.9)
        
    Returns:
        Validation result with status and notes
    """
    issues = []
    
    # Check discovery form
    if not discovery_form_path.exists():
        issues.append(f"Missing discovery form: {discovery_form_path}")
    else:
        content = discovery_form_path.read_text(encoding="utf-8").lower()
        
        # Check for MVP and backlog sections
        has_mvp = bool(re.search(r'mvp|minimum viable|must.?have', content))
        has_backlog = bool(re.search(r'backlog|optional|nice.?to.?have', content))
        
        if not has_mvp:
            issues.append("Missing MVP feature classification")
        if not has_backlog:
            issues.append("Missing optional backlog items")
    
    # Check scope clarification
    if not scope_clarification_path.exists():
        issues.append(f"Missing scope clarification: {scope_clarification_path}")
    else:
        content = scope_clarification_path.read_text(encoding="utf-8").lower()
        
        # Check for technical elements
        has_stack = bool(re.search(r'stack|technology|framework|language', content))
        has_constraints = bool(re.search(r'constraint|limitation|requirement', content))
        has_integrations = bool(re.search(r'integration|api|third.?party', content))
        
        if not has_stack:
            issues.append("Missing technology stack information")
        if not has_constraints:
            issues.append("Missing technical constraints")
        if not has_integrations:
            issues.append("Missing integration requirements")
    
    # Calculate completeness score
    total_checks = 6  # mvp, backlog, stack, constraints, integrations, both files exist
    passed_checks = total_checks - len(issues)
    score = passed_checks / total_checks
    
    if score < threshold:
        return {
            "status": "fail",
            "completeness": score,
            "notes": "; ".join(issues),
        }
    
    return {
        "status": "pass",
        "completeness": score,
        "notes": f"Requirements validated with {score:.2%} completeness",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 2: Requirement Completeness")
    parser.add_argument(
        "--form",
        type=Path,
        default=Path(".artifacts/protocol-02/client-discovery-form.md"),
        help="Path to client-discovery-form.md",
    )
    parser.add_argument(
        "--scope",
        type=Path,
        default=Path(".artifacts/protocol-02/scope-clarification.md"),
        help="Path to scope-clarification.md",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.9,
        help="Minimum completeness score (default: 0.9)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_requirements(args.form, args.scope, args.threshold)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

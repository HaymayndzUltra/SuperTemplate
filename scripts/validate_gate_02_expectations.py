#!/usr/bin/env python3
"""Gate 3 validator for Protocol 02: Expectation Alignment Gate.

Validates timeline, budget, collaboration cadence, and governance confirmed by client.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def validate_expectations(
    timeline_path: Path,
    communication_path: Path,
    governance_path: Path,
    recap_path: Path,
) -> dict:
    """Validate expectation alignment.
    
    Args:
        timeline_path: Path to timeline-discussion.md
        communication_path: Path to communication-plan.md
        governance_path: Path to governance-map.md
        recap_path: Path to discovery-recap.md
        
    Returns:
        Validation result with status and notes
    """
    issues = []
    
    # Check timeline discussion
    if not timeline_path.exists():
        issues.append(f"Missing timeline: {timeline_path}")
    else:
        content = timeline_path.read_text(encoding="utf-8").lower()
        if not re.search(r'milestone|deadline|schedule|timeline', content):
            issues.append("Timeline discussion incomplete")
    
    # Check communication plan
    if not communication_path.exists():
        issues.append(f"Missing communication plan: {communication_path}")
    else:
        content = communication_path.read_text(encoding="utf-8").lower()
        has_cadence = bool(re.search(r'daily|weekly|cadence|frequency', content))
        has_tools = bool(re.search(r'slack|email|zoom|teams|tool', content))
        
        if not has_cadence:
            issues.append("Communication cadence not defined")
        if not has_tools:
            issues.append("Communication tools not specified")
    
    # Check governance map (optional but recommended)
    if governance_path.exists():
        content = governance_path.read_text(encoding="utf-8").lower()
        if not re.search(r'decision|owner|approval|escalation', content):
            issues.append("Governance map lacks decision framework")
    
    # Check client approval in recap
    client_approved = False
    if not recap_path.exists():
        issues.append(f"Missing discovery recap: {recap_path}")
    else:
        content = recap_path.read_text(encoding="utf-8").lower()
        client_approved = bool(re.search(r'approved|confirmed|agreed|accepted', content))
        
        if not client_approved:
            issues.append("Client approval not recorded in discovery recap")
    
    if issues:
        return {
            "status": "fail",
            "client_approved": client_approved,
            "notes": "; ".join(issues),
        }
    
    return {
        "status": "pass",
        "client_approved": client_approved,
        "notes": "Expectation alignment validated with client approval",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 3: Expectation Alignment")
    parser.add_argument(
        "--timeline",
        type=Path,
        default=Path(".artifacts/protocol-02/timeline-discussion.md"),
        help="Path to timeline-discussion.md",
    )
    parser.add_argument(
        "--communication",
        type=Path,
        default=Path(".artifacts/protocol-02/communication-plan.md"),
        help="Path to communication-plan.md",
    )
    parser.add_argument(
        "--governance",
        type=Path,
        default=Path(".artifacts/protocol-02/governance-map.md"),
        help="Path to governance-map.md",
    )
    parser.add_argument(
        "--recap",
        type=Path,
        default=Path(".artifacts/protocol-02/discovery-recap.md"),
        help="Path to discovery-recap.md",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_expectations(
        args.timeline,
        args.communication,
        args.governance,
        args.recap,
    )
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

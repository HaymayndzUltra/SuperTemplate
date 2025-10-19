#!/usr/bin/env python3
"""Gate 1 validator for Protocol 02: Objective Alignment Gate.

Validates business objectives, user goals, and success metrics with coverage ≥ 95%.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def validate_objectives(context_notes_path: Path, threshold: float = 0.95) -> dict:
    """Validate objective alignment in client context notes.
    
    Args:
        context_notes_path: Path to client-context-notes.md
        threshold: Minimum coverage score (default 0.95)
        
    Returns:
        Validation result with status and notes
    """
    if not context_notes_path.exists():
        return {
            "status": "fail",
            "coverage": 0.0,
            "notes": f"Missing artifact: {context_notes_path}",
        }
    
    content = context_notes_path.read_text(encoding="utf-8").lower()
    
    # Check for required elements
    required_elements = {
        "objectives": [r"objective", r"goal", r"purpose"],
        "users": [r"user", r"audience", r"stakeholder"],
        "kpis": [r"kpi", r"metric", r"success", r"measure"],
    }
    
    found_elements = {}
    for category, patterns in required_elements.items():
        found_elements[category] = any(re.search(pattern, content) for pattern in patterns)
    
    coverage = sum(found_elements.values()) / len(required_elements)
    
    if coverage < threshold:
        missing = [cat for cat, found in found_elements.items() if not found]
        return {
            "status": "fail",
            "coverage": coverage,
            "notes": f"Coverage {coverage:.2%} < {threshold:.0%}. Missing: {', '.join(missing)}",
        }
    
    return {
        "status": "pass",
        "coverage": coverage,
        "notes": f"Objective alignment validated with {coverage:.2%} coverage",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 1: Objective Alignment")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(".artifacts/protocol-02/client-context-notes.md"),
        help="Path to client-context-notes.md",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.95,
        help="Minimum coverage score (default: 0.95)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_objectives(args.input, args.threshold)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

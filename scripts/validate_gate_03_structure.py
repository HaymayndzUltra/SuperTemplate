#!/usr/bin/env python3
"""Gate 2 validator for Protocol 03: Structural Integrity.

Validates brief structure, traceability map, and completeness with coverage ≥ 100%.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def validate_brief_structure(
    brief_path: Path,
    traceability_path: Path,
    output_path: Path,
) -> dict:
    """Validate project brief structural integrity.
    
    Args:
        brief_path: Path to PROJECT-BRIEF.md
        traceability_path: Path to traceability-map.json
        output_path: Output path for structure report
        
    Returns:
        Validation result with status and notes
    """
    if not brief_path.exists():
        return {
            "status": "fail",
            "coverage": 0.0,
            "notes": f"Missing project brief: {brief_path}",
        }
    
    # Required sections
    required_sections = [
        "executive summary",
        "business objectives",
        "functional scope",
        "technical architecture",
        "delivery plan",
        "communication plan",
        "risks",
        "assumptions",
    ]
    
    content = brief_path.read_text(encoding="utf-8").lower()
    
    found_sections = []
    missing_sections = []
    
    for section in required_sections:
        # Look for section headers
        pattern = rf"(?:^|\n)(?:#+\s*)?{re.escape(section)}"
        if re.search(pattern, content, re.IGNORECASE):
            found_sections.append(section)
        else:
            missing_sections.append(section)
    
    coverage = len(found_sections) / len(required_sections)
    
    # Check traceability
    has_traceability = False
    traceability_issues = []
    
    if not traceability_path.exists():
        traceability_issues.append(f"Missing traceability map: {traceability_path}")
    else:
        try:
            traceability = json.loads(traceability_path.read_text(encoding="utf-8"))
            has_traceability = len(traceability) > 0
            
            if not has_traceability:
                traceability_issues.append("Traceability map is empty")
        except json.JSONDecodeError:
            traceability_issues.append("Invalid traceability map JSON")
    
    # Generate structure report
    report = {
        "coverage": coverage,
        "required_sections": required_sections,
        "found_sections": found_sections,
        "missing_sections": missing_sections,
        "has_traceability": has_traceability,
        "traceability_issues": traceability_issues,
        "status": "pass" if coverage == 1.0 and has_traceability else "fail",
    }
    
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    
    issues = missing_sections + traceability_issues
    
    if coverage < 1.0 or issues:
        return {
            "status": "fail",
            "coverage": coverage,
            "notes": f"Coverage {coverage:.0%}; Issues: {'; '.join(issues)}",
        }
    
    return {
        "status": "pass",
        "coverage": coverage,
        "notes": f"All {len(required_sections)} sections present with traceability",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 2: Structural Integrity")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(".artifacts/protocol-03/PROJECT-BRIEF.md"),
        help="Path to PROJECT-BRIEF.md",
    )
    parser.add_argument(
        "--traceability",
        type=Path,
        default=Path(".artifacts/protocol-03/traceability-map.json"),
        help="Path to traceability-map.json",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path(".artifacts/protocol-03/brief-structure-report.json"),
        help="Output path for structure report",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_brief_structure(args.input, args.traceability, args.report)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

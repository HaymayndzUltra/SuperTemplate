#!/usr/bin/env python3
"""Gate 5 validator for Protocol 01: Final Validation & Approval Readiness.

Validates readability ≥ 90, zero factual discrepancies, empathy coverage ≥ 3 tokens.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_final_proposal(
    proposal_path: Path,
    validation_report_path: Path,
    min_readability: int = 90,
    min_empathy: int = 3,
) -> dict:
    """Validate final proposal quality.
    
    Args:
        proposal_path: Path to PROPOSAL.md
        validation_report_path: Path to proposal-validation-report.json
        min_readability: Minimum readability score (default 90)
        min_empathy: Minimum empathy tokens (default 3)
        
    Returns:
        Validation result with status and notes
    """
    if not proposal_path.exists():
        return {
            "status": "fail",
            "notes": f"Missing proposal: {proposal_path}",
        }
    
    # Check validation report exists
    if not validation_report_path.exists():
        return {
            "status": "fail",
            "notes": f"Missing validation report: {validation_report_path}",
        }
    
    try:
        report = json.loads(validation_report_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {
            "status": "fail",
            "notes": f"Invalid validation report JSON: {exc}",
        }
    
    # Check validation criteria
    issues = []
    
    readability = report.get("readability_score", 0)
    if readability < min_readability:
        issues.append(f"Readability {readability} < {min_readability}")
    
    discrepancies = report.get("factual_discrepancies", [])
    if discrepancies:
        issues.append(f"Found {len(discrepancies)} factual discrepancies")
    
    empathy_tokens = report.get("empathy_coverage", 0)
    if empathy_tokens < min_empathy:
        issues.append(f"Empathy tokens {empathy_tokens} < {min_empathy}")
    
    # Check overall status
    overall_status = report.get("status", "pending")
    if overall_status != "pass":
        issues.append(f"Overall validation status: {overall_status}")
    
    if issues:
        return {
            "status": "fail",
            "notes": "; ".join(issues),
        }
    
    return {
        "status": "pass",
        "readability": readability,
        "empathy_coverage": empathy_tokens,
        "notes": "All final validation checks passed",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 5: Final Validation")
    parser.add_argument(
        "--proposal",
        type=Path,
        default=Path(".artifacts/protocol-01/PROPOSAL.md"),
        help="Path to PROPOSAL.md",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path(".artifacts/protocol-01/proposal-validation-report.json"),
        help="Path to validation report",
    )
    parser.add_argument(
        "--min-readability",
        type=int,
        default=90,
        help="Minimum readability score (default: 90)",
    )
    parser.add_argument(
        "--min-empathy",
        type=int,
        default=3,
        help="Minimum empathy tokens (default: 3)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_final_proposal(
        args.proposal,
        args.report,
        args.min_readability,
        args.min_empathy,
    )
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

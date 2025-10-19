#!/usr/bin/env python3
"""Gate 1 validator for Protocol 01: Job Post Intake Validation.

Validates that jobpost-analysis.json captures objectives, deliverables,
tone signals, and risk notes with completeness score ≥ 0.9.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_jobpost_analysis(analysis_path: Path, threshold: float = 0.9) -> dict:
    """Validate job post analysis completeness.
    
    Args:
        analysis_path: Path to jobpost-analysis.json
        threshold: Minimum completeness score (default 0.9)
        
    Returns:
        Validation result with status and notes
    """
    if not analysis_path.exists():
        return {
            "status": "fail",
            "score": 0.0,
            "notes": f"Missing artifact: {analysis_path}",
        }
    
    try:
        data = json.loads(analysis_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {
            "status": "fail",
            "score": 0.0,
            "notes": f"Invalid JSON: {exc}",
        }
    
    # Check required fields
    required_fields = ["objectives", "deliverables", "tone_signals", "risks"]
    present_fields = [field for field in required_fields if field in data and data[field]]
    
    score = len(present_fields) / len(required_fields)
    
    if score < threshold:
        missing = [f for f in required_fields if f not in present_fields]
        return {
            "status": "fail",
            "score": score,
            "notes": f"Completeness {score:.2f} < {threshold}. Missing: {', '.join(missing)}",
        }
    
    return {
        "status": "pass",
        "score": score,
        "notes": f"Job post analysis complete with score {score:.2f}",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 1: Job Post Intake")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(".artifacts/protocol-01/jobpost-analysis.json"),
        help="Path to jobpost-analysis.json",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.9,
        help="Minimum completeness score (default: 0.9)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_jobpost_analysis(args.input, args.threshold)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Gate 1 validator for Protocol 03: Discovery Evidence Verification.

Validates all prerequisite artifacts, resolves inconsistencies, validation score ≥ 0.95.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_discovery_evidence(
    discovery_dir: Path,
    output_path: Path,
    threshold: float = 0.95,
) -> dict:
    """Validate discovery artifacts for project brief creation.
    
    Args:
        discovery_dir: Directory containing Protocol 02 artifacts
        output_path: Output path for validation report
        threshold: Minimum validation score (default 0.95)
        
    Returns:
        Validation result with status and notes
    """
    required_artifacts = [
        "client-discovery-form.md",
        "scope-clarification.md",
        "communication-plan.md",
        "timeline-discussion.md",
        "discovery-recap.md",
    ]
    
    issues = []
    found_artifacts = 0
    
    for artifact in required_artifacts:
        artifact_path = discovery_dir / artifact
        
        if not artifact_path.exists():
            issues.append(f"Missing required artifact: {artifact}")
        elif artifact_path.stat().st_size == 0:
            issues.append(f"Empty artifact: {artifact}")
        else:
            found_artifacts += 1
    
    score = found_artifacts / len(required_artifacts)
    
    # Generate validation report
    report = {
        "validation_score": score,
        "required_artifacts": required_artifacts,
        "found_artifacts": found_artifacts,
        "issues": issues,
        "status": "PASS" if score >= threshold and not issues else "FAIL",
    }
    
    # Write report
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    
    if score < threshold or issues:
        return {
            "status": "fail",
            "validation_score": score,
            "notes": f"Score {score:.2%} < {threshold:.0%}; Issues: {'; '.join(issues)}",
        }
    
    return {
        "status": "pass",
        "validation_score": score,
        "notes": f"Discovery evidence validated with {score:.2%} score",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 1: Discovery Evidence")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(".artifacts/protocol-02"),
        help="Directory containing Protocol 02 artifacts",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(".artifacts/protocol-03/project-brief-validation-report.json"),
        help="Output path for validation report",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.95,
        help="Minimum validation score (default: 0.95)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_discovery_evidence(args.input, args.output, args.threshold)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

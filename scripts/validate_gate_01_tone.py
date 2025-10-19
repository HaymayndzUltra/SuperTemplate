#!/usr/bin/env python3
"""Gate 2 validator for Protocol 01: Tone Strategy Confidence.

Validates tone classification confidence ≥ 0.8 with mapped strategy labels.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_tone_mapping(tone_map_path: Path, threshold: float = 0.8) -> dict:
    """Validate tone mapping confidence and strategy.
    
    Args:
        tone_map_path: Path to tone-map.json
        threshold: Minimum confidence score (default 0.8)
        
    Returns:
        Validation result with status and notes
    """
    if not tone_map_path.exists():
        return {
            "status": "fail",
            "confidence": 0.0,
            "notes": f"Missing artifact: {tone_map_path}",
        }
    
    try:
        data = json.loads(tone_map_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {
            "status": "fail",
            "confidence": 0.0,
            "notes": f"Invalid JSON: {exc}",
        }
    
    # Check required fields
    confidence = data.get("confidence", 0.0)
    strategy = data.get("strategy", "")
    
    issues = []
    if confidence < threshold:
        issues.append(f"Confidence {confidence:.2f} < {threshold}")
    
    if not strategy or not isinstance(strategy, str):
        issues.append("Strategy not populated")
    
    if issues:
        return {
            "status": "fail",
            "confidence": confidence,
            "notes": "; ".join(issues),
        }
    
    return {
        "status": "pass",
        "confidence": confidence,
        "strategy": strategy,
        "notes": f"Tone classification confidence {confidence:.2f} with strategy '{strategy}'",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 2: Tone Strategy")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(".artifacts/protocol-01/tone-map.json"),
        help="Path to tone-map.json",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="Minimum confidence score (default: 0.8)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_tone_mapping(args.input, args.threshold)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

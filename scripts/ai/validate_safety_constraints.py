#!/usr/bin/env python3
"""
Script: validate_safety_constraints.py
Protocol: 15 - AI Model Testing & Edge Case Validation
Purpose: Summarize edge-case execution results and flag gate readiness.
"""

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def evaluate(results: Dict[str, Any]) -> Dict[str, Any]:
    total = len(results.get("results", []))
    failures = [r for r in results.get("results", []) if r.get("status") == "fail"]
    critical_failures = [r for r in failures if r.get("severity") == "critical"]
    coverage = total >= 20
    return {
        "total": total,
        "coverage_pass": coverage,
        "failure_count": len(failures),
        "critical_failure_count": len(critical_failures),
        "gate1": "pass" if coverage else "fail",
        "gate2": "pass" if not critical_failures else "warning",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate safety constraints")
    parser.add_argument("--results", required=True, help="JSON results from edge-case run")
    parser.add_argument("--report", required=True, help="Markdown report output")
    args = parser.parse_args()

    results = json.loads(Path(args.results).read_text(encoding="utf-8"))
    summary = evaluate(results)

    report = Path(args.report)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        "# Edge Case Safety Report\n\n" +
        json.dumps({"summary": summary, "sample_failures": results.get("failures", [])[:5]}, indent=2),
        encoding="utf-8"
    )
    print(f"Safety report generated: {report}")


if __name__ == "__main__":
    main()

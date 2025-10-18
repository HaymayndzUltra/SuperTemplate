#!/usr/bin/env python3
"""Compute aggregate metrics from protocol and script analysis artifacts."""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def load_protocol_scores() -> list[dict]:
    path = REPO_ROOT / "documentation" / "protocol-scores.json"
    return json.loads(path.read_text(encoding="utf-8"))


def compute_protocol_summary(scores: list[dict]) -> dict:
    totals = {
        "completeness": 0,
        "realism": 0,
        "clarity": 0,
        "adaptability": 0,
        "freelance_alignment": 0,
    }
    for record in scores:
        for key in totals:
            totals[key] += record[key]

    count = len(scores)
    averages = {key: totals[key] / count for key in totals}
    overall = sum(
        (record["completeness"] + record["realism"] + record["clarity"] + record["adaptability"] + record["freelance_alignment"])
        for record in scores
    )
    return {
        "protocol_count": count,
        "totals": totals,
        "averages": averages,
        "overall_score": overall,
        "average_score": overall / count,
    }


def load_script_inventory_summary() -> dict:
    path = REPO_ROOT / "documentation" / "script-inventory-report.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    summary = {}
    for line in lines:
        if line.startswith("- Total scripts analyzed:"):
            summary["total_scripts"] = int(line.split("**")[1])
        elif line.startswith("- Registered in"):
            segment = line.split("**")[1]
            summary["registered_scripts"] = int(segment)
        elif line.startswith("- Unregistered scripts"):
            segment = line.split("**")[1]
            summary["unregistered_scripts"] = int(segment)
    return summary


def load_script_reference_summary() -> dict:
    path = REPO_ROOT / "documentation" / "protocol-script-reference-report.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    summary = {}
    for line in lines:
        if line.startswith("- Protocol files scanned:"):
            summary["protocol_files"] = int(line.split("**")[1])
        elif line.startswith("- Unique script references:"):
            summary["references"] = int(line.split("**")[1])
        elif line.startswith("- Missing script files:"):
            summary["missing_references"] = int(line.split("**")[1])
    return summary


def main() -> None:
    protocol_scores = load_protocol_scores()
    protocol_summary = compute_protocol_summary(protocol_scores)
    script_inventory = load_script_inventory_summary()
    script_references = load_script_reference_summary()

    report = {
        "protocol_summary": protocol_summary,
        "script_inventory": script_inventory,
        "script_references": script_references,
    }

    output_path = REPO_ROOT / "documentation" / "analysis-scorecard.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

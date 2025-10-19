#!/usr/bin/env python3
"""Generate protocol scorecard metrics from automation inventory data.

The scorecard consumes the same protocol markdown set (01-23) and calculates
coverage and completeness indicators, emitting a consolidated JSON report that
can be published under ``documentation/`` for telemetry compliance.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Dict, Sequence

import inventory_protocols

DEFAULT_OUTPUT = Path("documentation/protocol-scorecard.json")


def _compute_score(inventory: inventory_protocols.ProtocolInventory) -> Dict[str, object]:
    completeness = inventory.coverage
    status = "on-track" if completeness >= 0.9 else "at-risk" if completeness >= 0.6 else "critical"
    return {
        "protocol": inventory.protocol,
        "title": inventory.title,
        "coverage": round(inventory.coverage, 3),
        "missing_scripts": inventory.missing_scripts,
        "existing_scripts": inventory.existing_scripts,
        "completeness": round(completeness, 3),
        "status": status,
    }


def _summary(scores):
    total = len(scores)
    avg = sum(item["coverage"] for item in scores) / total if total else 1.0
    critical = sum(1 for item in scores if item["status"] == "critical")
    at_risk = sum(1 for item in scores if item["status"] == "at-risk")
    on_track = total - critical - at_risk
    return {
        "protocols": total,
        "average_coverage": round(avg, 3),
        "on_track": on_track,
        "at_risk": at_risk,
        "critical": critical,
    }


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate protocol scorecard report.")
    parser.add_argument(
        "--protocol-dir",
        type=Path,
        default=Path(".cursor/ai-driven-workflow"),
        help="Directory containing protocol markdown files (default: .cursor/ai-driven-workflow)",
    )
    parser.add_argument(
        "--scripts-dir",
        type=Path,
        default=Path("scripts"),
        help="Directory containing automation scripts (default: scripts)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"JSON output path (default: {DEFAULT_OUTPUT})",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    inventories = [
        inventory_protocols.build_inventory(path, args.scripts_dir)
        for path in inventory_protocols.discover_protocol_files(args.protocol_dir)
    ]

    scores = [_compute_score(item) for item in inventories]
    report = {
        "summary": _summary(scores),
        "protocols": scores,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(
        "Generated protocol scorecard:\n"
        f"  Protocols: {report['summary']['protocols']}\n"
        f"  Average coverage: {report['summary']['average_coverage']:.3f}\n"
        f"  Critical: {report['summary']['critical']} | At risk: {report['summary']['at_risk']} | On track: {report['summary']['on_track']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

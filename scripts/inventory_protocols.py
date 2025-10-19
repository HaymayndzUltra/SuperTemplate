#!/usr/bin/env python3
"""Protocol automation inventory CLI.

This tool scans protocol markdown files (01-23) under ``.cursor/ai-driven-workflow``
for ``python scripts/...`` references, verifies whether the referenced scripts exist
in the repository ``scripts/`` directory, and emits JSON/CSV inventory reports.

Example usage::

    python scripts/inventory_protocols.py \
        --output-json documentation/protocol-script-inventory.json \
        --output-csv documentation/protocol-script-inventory.csv

The generated reports satisfy Wave 1 telemetry requirements by providing an
authoritative mapping between protocols and automation assets.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Sequence

SCRIPT_PATTERN = re.compile(r"python\s+scripts/([\w_\-/]+\.(?:py|sh))")
PROTOCOL_GLOB = "[0-2][0-9]-*.md"


@dataclass
class ProtocolInventory:
    protocol: str
    title: str
    script_count: int
    missing_count: int
    existing_scripts: List[str]
    missing_scripts: List[str]
    coverage: float

    def to_dict(self) -> dict:
        data = asdict(self)
        data["coverage"] = round(self.coverage, 3)
        return data


def discover_protocol_files(protocol_dir: Path) -> List[Path]:
    files = sorted(protocol_dir.glob(PROTOCOL_GLOB))
    return [f for f in files if f.is_file() and 1 <= int(f.name.split("-", 1)[0]) <= 23]


def extract_title(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "(untitled)"


def extract_scripts(markdown_text: str) -> List[str]:
    scripts = set()
    for match in SCRIPT_PATTERN.finditer(markdown_text):
        scripts.add(match.group(1))
    return sorted(scripts)


def build_inventory(protocol_path: Path, scripts_dir: Path) -> ProtocolInventory:
    text = protocol_path.read_text(encoding="utf-8")
    title = extract_title(text)
    referenced_scripts = extract_scripts(text)
    existing, missing = [], []
    for script in referenced_scripts:
        script_path = scripts_dir / script
        if script_path.exists():
            existing.append(script)
        else:
            missing.append(script)
    script_count = len(referenced_scripts)
    coverage = (len(existing) / script_count) if script_count else 1.0
    return ProtocolInventory(
        protocol=protocol_path.name,
        title=title,
        script_count=script_count,
        missing_count=len(missing),
        existing_scripts=existing,
        missing_scripts=missing,
        coverage=coverage,
    )


def write_json_report(inventories: Sequence[ProtocolInventory], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump([item.to_dict() for item in inventories], f, indent=2)


def write_csv_report(inventories: Sequence[ProtocolInventory], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "protocol",
        "title",
        "script_count",
        "missing_count",
        "coverage",
        "existing_scripts",
        "missing_scripts",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in inventories:
            writer.writerow(
                {
                    "protocol": item.protocol,
                    "title": item.title,
                    "script_count": item.script_count,
                    "missing_count": item.missing_count,
                    "coverage": f"{item.coverage:.3f}",
                    "existing_scripts": ";".join(item.existing_scripts),
                    "missing_scripts": ";".join(item.missing_scripts),
                }
            )


def summarise(inventories: Iterable[ProtocolInventory]) -> str:
    inventories = list(inventories)
    total_protocols = len(inventories)
    total_scripts = sum(item.script_count for item in inventories)
    total_missing = sum(item.missing_count for item in inventories)
    average_coverage = (
        sum(item.coverage for item in inventories) / total_protocols if total_protocols else 1.0
    )
    return (
        f"Protocols analysed: {total_protocols}\n"
        f"Referenced scripts: {total_scripts}\n"
        f"Missing scripts: {total_missing}\n"
        f"Average coverage: {average_coverage:.3f}"
    )


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate protocol automation inventory reports.")
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
        "--output-json",
        type=Path,
        default=Path("documentation/protocol-script-inventory.json"),
        help="Path to write JSON report (default: documentation/protocol-script-inventory.json)",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=Path("documentation/protocol-script-inventory.csv"),
        help="Path to write CSV report (default: documentation/protocol-script-inventory.csv)",
    )
    parser.add_argument(
        "--no-json",
        action="store_true",
        help="Skip writing JSON output",
    )
    parser.add_argument(
        "--no-csv",
        action="store_true",
        help="Skip writing CSV output",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    protocol_dir = args.protocol_dir
    scripts_dir = args.scripts_dir

    if not protocol_dir.exists():
        print(f"error: protocol directory not found: {protocol_dir}", file=sys.stderr)
        return 1
    if not scripts_dir.exists():
        print(f"error: scripts directory not found: {scripts_dir}", file=sys.stderr)
        return 1

    protocol_files = discover_protocol_files(protocol_dir)
    if not protocol_files:
        print("error: no protocol files discovered", file=sys.stderr)
        return 1

    inventories = [build_inventory(path, scripts_dir) for path in protocol_files]

    if not args.no_json:
        write_json_report(inventories, args.output_json)
    if not args.no_csv:
        write_csv_report(inventories, args.output_csv)

    print(summarise(inventories))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

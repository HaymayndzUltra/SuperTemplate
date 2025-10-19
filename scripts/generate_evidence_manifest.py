#!/usr/bin/env python3
"""Generate protocol evidence manifest stubs.

This helper consumes the protocol automation inventory and produces
schema-compliant manifests for a single protocol. The CLI is intentionally
flexible so teams can seed artifacts and validator rows while Phase 2
automation is still under construction.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import List, Sequence

import inventory_protocols

DEFAULT_OUTPUT_DIR = Path("documentation/sample-manifests")


def _parse_artifact(value: str) -> dict:
    try:
        path, status, description = value.split("::", 2)
    except ValueError as exc:  # pragma: no cover - defensive parsing guard
        raise argparse.ArgumentTypeError(
            "artifact must use format path::status::description"
        ) from exc
    return {
        "path": path,
        "status": status,
        "description": description,
    }


def _parse_validator(value: str) -> dict:
    try:
        name, command, status, notes = value.split("::", 3)
    except ValueError as exc:  # pragma: no cover - defensive parsing guard
        raise argparse.ArgumentTypeError(
            "validator must use format name::command::status::notes"
        ) from exc
    return {
        "name": name,
        "command": command,
        "status": status,
        "notes": notes,
    }


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate evidence manifest for a protocol.")
    parser.add_argument("protocol", help="Protocol identifier (e.g., 01, 04)")
    parser.add_argument(
        "--protocol-dir",
        type=Path,
        default=Path(".cursor/ai-driven-workflow"),
        help="Directory containing protocol markdown files",
    )
    parser.add_argument(
        "--scripts-dir",
        type=Path,
        default=Path("scripts"),
        help="Directory containing automation scripts",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory for manifest outputs (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--artifact",
        action="append",
        type=_parse_artifact,
        default=[],
        help="Artifact entry formatted as path::status::description. Repeatable.",
    )
    parser.add_argument(
        "--validator",
        action="append",
        type=_parse_validator,
        default=[],
        help="Validator entry formatted as name::command::status::notes. Repeatable.",
    )
    parser.add_argument(
        "--notes",
        default="",
        help="Optional notes field for the manifest.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    inventories: List[inventory_protocols.ProtocolInventory] = [
        inventory_protocols.build_inventory(path, args.scripts_dir)
        for path in inventory_protocols.discover_protocol_files(args.protocol_dir)
    ]
    lookup = {item.protocol.split("-", 1)[0]: item for item in inventories}

    protocol = args.protocol
    if protocol not in lookup:
        raise SystemExit(f"Unknown protocol id: {protocol}")

    inventory = lookup[protocol]
    referenced = sorted(set(inventory.existing_scripts + inventory.missing_scripts))
    manifest = {
        "protocol_id": protocol,
        "protocol_title": inventory.title,
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }
    manifest["automation_coverage"] = {
        "referenced_scripts": referenced,
        "missing_scripts": inventory.missing_scripts,
        "coverage": round(inventory.coverage, 3),
    }
    manifest["artifacts"] = args.artifact
    manifest["validators"] = args.validator
    manifest["notes"] = args.notes

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f"protocol-{protocol}.manifest.json"
    output_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote manifest: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

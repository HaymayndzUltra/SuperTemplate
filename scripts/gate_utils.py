"""Shared utilities for protocol gate validation scripts."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List

import inventory_protocols

ARTIFACTS_ROOT = Path(".artifacts")


@dataclass
class ManifestData:
    protocol_id: str
    protocol_title: str
    coverage: float
    referenced_scripts: List[str]
    missing_scripts: List[str]


def load_manifest_data(protocol_id: str) -> ManifestData:
    protocol_dir = Path(".cursor/ai-driven-workflow")
    scripts_dir = Path("scripts")
    inventories = [
        inventory_protocols.build_inventory(path, scripts_dir)
        for path in inventory_protocols.discover_protocol_files(protocol_dir)
    ]
    lookup = {item.protocol.split("-", 1)[0]: item for item in inventories}
    if protocol_id not in lookup:
        raise ValueError(f"Unknown protocol id: {protocol_id}")
    item = lookup[protocol_id]
    referenced = sorted(set(item.existing_scripts + item.missing_scripts))
    return ManifestData(
        protocol_id=protocol_id,
        protocol_title=item.title,
        coverage=item.coverage,
        referenced_scripts=referenced,
        missing_scripts=item.missing_scripts,
    )


def write_manifest(
    manifest_path: Path,
    data: ManifestData,
    artifacts: List[dict],
    validators: List[dict],
    notes: str = "",
) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "protocol_id": data.protocol_id,
        "protocol_title": data.protocol_title,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "automation_coverage": {
            "referenced_scripts": data.referenced_scripts,
            "missing_scripts": data.missing_scripts,
            "coverage": round(data.coverage, 3),
        },
        "artifacts": artifacts,
        "validators": validators,
        "notes": notes,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

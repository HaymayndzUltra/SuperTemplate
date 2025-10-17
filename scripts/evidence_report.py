#!/usr/bin/env python3
"""Generate a consolidated evidence report from a workflow run."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def load_manifest(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Evidence manifest not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def generate_report(manifest_path: Path, output: Path) -> None:
    manifest = load_manifest(manifest_path)
    report_lines = ["# Evidence Report", ""]
    for entry in manifest:
        report_lines.append(f"- **{entry['category']}**: {entry['description']} ({entry['path']})")
    output.write_text("\n".join(report_lines), encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Path to evidence manifest JSON")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("evidence_report.md"),
        help="Output markdown file",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse_args()
    generate_report(args.manifest, args.output)

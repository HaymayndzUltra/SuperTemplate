#!/usr/bin/env python3
"""Aggregate frontend (Jest) and backend (pytest) coverage results."""
from __future__ import annotations

import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FRONT_SUMMARY = ROOT / "frontend" / "coverage" / "coverage-summary.json"
BACK_COVERAGE = ROOT / "coverage" / "backend-coverage.xml"
OUTPUT_DIR = ROOT / "coverage"
OUTPUT_FILE = OUTPUT_DIR / "coverage-summary.json"


def _read_frontend_lines() -> tuple[int, int]:
    if not FRONT_SUMMARY.exists():
        return 0, 0
    data = json.loads(FRONT_SUMMARY.read_text(encoding="utf-8"))
    lines = data.get("total", {}).get("lines", {})
    covered = int(lines.get("covered") or 0)
    total = int(lines.get("total") or 0)
    return covered, total


def _read_backend_lines() -> tuple[int, int]:
    if not BACK_COVERAGE.exists():
        return 0, 0
    root = ET.parse(BACK_COVERAGE).getroot()
    covered_attr = root.attrib.get("lines-covered") or root.attrib.get("lines_covered")
    total_attr = root.attrib.get("lines-valid") or root.attrib.get("lines_valid")
    if covered_attr is not None and total_attr is not None:
        covered = int(float(covered_attr))
        total = int(float(total_attr))
        return covered, total

    # Fallback to line-rate if explicit counts are unavailable
    rate = float(root.attrib.get("line-rate", 0))
    total = int(float(root.attrib.get("lines-valid", 0)))
    covered = int(round(rate * total))
    return covered, total


def main() -> int:
    frontend_covered, frontend_total = _read_frontend_lines()
    backend_covered, backend_total = _read_backend_lines()

    total_covered = frontend_covered + backend_covered
    total_lines = frontend_total + backend_total

    if total_lines == 0:
        raise SystemExit("No coverage data found to aggregate.")

    pct = round((total_covered / total_lines) * 100, 2)

    summary = {
        "total": {
            "lines": {
                "total": total_lines,
                "covered": total_covered,
                "skipped": 0,
                "pct": pct,
            }
        },
        "components": {
            "frontend": {
                "covered": frontend_covered,
                "total": frontend_total,
            },
            "backend": {
                "covered": backend_covered,
                "total": backend_total,
            },
        },
    }

    OUTPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(
        f"[COVERAGE] Aggregated coverage: {total_covered}/{total_lines} lines -> {pct:.2f}%",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

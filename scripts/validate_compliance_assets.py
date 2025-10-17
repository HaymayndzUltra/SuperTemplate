#!/usr/bin/env python3
"""Validate that compliance docs and gate config match generator output."""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path
from types import SimpleNamespace

# Import via proper package path (scripts should be run from repo root)
# If running from elsewhere, use: python -m scripts.validate_compliance_assets
from project_generator.core.generator import ProjectGenerator
from project_generator.core.industry_config import IndustryConfig
from project_generator.core.validator import ProjectValidator

DEFAULT_STACK = dict(
    name="portfolio-dashboard",
    industry="saas",
    project_type="fullstack",
    frontend="nextjs",
    backend="fastapi",
    database="postgres",
    auth="auth0",
    deploy="vercel",
    compliance="gdpr",
)


def build_generator() -> ProjectGenerator:
    args = SimpleNamespace(
        **DEFAULT_STACK,
        features="",
        output_dir=".",
        no_git=True,
        no_install=True,
        include_cursor_assets=False,
        no_cursor_assets=True,
        minimal_cursor=False,
        rules_manifest=None,
        rules_mode="auto",
        include_project_rules=False,
        workers=2,
        category="example",
        skip_system_checks=True,
        force=False,
    )
    validator = ProjectValidator()
    config = IndustryConfig(args.industry)
    return ProjectGenerator(args, validator, config)


def compare_file(path: Path, expected: str, write: bool) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if current == expected:
        print(f"[COMPLIANCE] {path} is up to date.")
        return True
    if write:
        path.write_text(expected, encoding="utf-8")
        print(f"[COMPLIANCE] Updated {path} from generator output.")
        return True

    print(f"[COMPLIANCE] Drift detected in {path} (run with --write to update).")
    diff = difflib.unified_diff(
        current.splitlines(),
        expected.splitlines(),
        fromfile=str(path),
        tofile="generator",
    )
    for line in diff:
        print(line)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Rewrite compliance assets instead of exiting with an error when drift is detected.",
    )
    args = parser.parse_args()

    generator = build_generator()
    compliance_doc = generator._generate_compliance_documentation().strip() + "\n"
    gates_yaml = generator._generate_gates_config()

    compliance_path = ROOT / "docs" / "COMPLIANCE.md"
    gates_path = ROOT / "gates_config.yaml"

    ok_doc = compare_file(compliance_path, compliance_doc, args.write)
    ok_gates = compare_file(gates_path, gates_yaml, args.write)
    return 0 if ok_doc and ok_gates else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Brief-driven project orchestration that generates separate frontend and backend projects
with curated Cursor rules per domain.

Usage:
  python scripts/generate_from_brief.py \
    --brief docs/briefs/project1/brief.md \
    --output-root ../_generated \
    --force --yes
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List
import sys
import shlex

from project_generator.core.brief_parser import BriefParser


FRONTEND_RULES = {
    "nextjs": ["nextjs.mdc", "nextjs-formatting.mdc", "nextjs-rsc-and-client.mdc", "typescript.mdc"],
    "angular": ["angular.mdc", "typescript.mdc"],
    "nuxt": ["vue.mdc", "typescript.mdc"],
    "expo": ["expo.mdc", "react-native.mdc", "typescript.mdc"],
}

BACKEND_RULES = {
    "fastapi": ["fastapi.mdc", "python.mdc", "rest-api.mdc", "open-api.mdc"],
    "django": ["django.mdc", "python.mdc", "rest-api.mdc", "open-api.mdc"],
    "nestjs": ["nodejs.mdc", "typescript.mdc", "rest-api.mdc", "open-api.mdc"],
    "go": ["golang.mdc", "nethttp.mdc", "rest-api.mdc", "open-api.mdc"],
}

DB_ADDONS = {
    "mongodb": ["mongodb.mdc"],
    "firebase": ["firebase.mdc"],
}

COMPLIANCE_RULES = {
    "hipaa": "industry-compliance-hipaa.mdc",
    "gdpr": "industry-compliance-gdpr.mdc",
    "sox": "industry-compliance-sox.mdc",
    "pci": "industry-compliance-pci.mdc",
}


def write_rules_manifest(manifest_path: Path, names: List[str]) -> None:
    # Deduplicate while preserving order
    seen = set()
    ordered: List[str] = []
    for n in names:
        if n not in seen:
            seen.add(n)
            ordered.append(n)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(ordered, indent=2), encoding="utf-8")


def build_fe_manifest(frontend: str, compliance: List[str]) -> List[str]:
    rules = list(FRONTEND_RULES.get(frontend, []))
    # Domain rules (focused)
    rules += [
        "accessibility.mdc",
        "nextjs-a11y.mdc" if frontend == "nextjs" else None,
    ]
    return [r for r in rules if r]


def build_be_manifest(backend: str, database: str, compliance: List[str]) -> List[str]:
    rules = list(BACKEND_RULES.get(backend, []))
    rules += DB_ADDONS.get(database, [])
    # Domain rules common to backends (focused)
    rules += [
        "performance.mdc",
        "observability.mdc",
    ]
    return rules


def run_argv(argv: list[str], cwd: Path | None = None) -> int:
    try:
        out = subprocess.run(argv, cwd=str(cwd) if cwd else None, check=False, text=True)
        return out.returncode
    except Exception as e:
        print(f"[ERROR] command failed: {argv}: {e}")
        return 1


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate separate FE/BE projects from brief.md with curated rules")
    p.add_argument("--brief", required=True, help="Path to brief.md")
    p.add_argument("--output-root", default=".", help="Root directory for generated projects (default: current repo)")
    p.add_argument("--force", action="store_true", help="Overwrite existing project directories")
    p.add_argument("--yes", action="store_true", help="Run non-interactively")
    p.add_argument("--workers", type=int, default=8)
    # Passthrough flags to child generator
    p.add_argument("--in-place", action="store_true", help="Generate into --output-root as-is (no redirect)")
    p.add_argument("--no-subdir", action="store_true", help="Place scaffold directly under --output-root (no <name>/ subfolder)")
    p.add_argument("--no-cursor-assets", dest="no_cursor_assets", action="store_true", help="Do not emit .cursor assets in generated projects")
    p.add_argument("--include-cursor-assets", dest="include_cursor_assets", action="store_true", help="Force emitting .cursor assets in generated projects")
    # Post-scaffold rule generation control (default: off when template has root .cursor)
    p.add_argument("--no-post-run-generate-rules", dest="no_post_generate_rules", action="store_true", help="Do not run Generate Cursor Rules after scaffolding")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = (repo_root / output_root).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    spec = BriefParser(args.brief).parse()

    # Use the same Python interpreter that launched this script
    python_bin = shlex.quote(os.environ.get("PYTHON", sys.executable or "python3"))

    # FE/BE detection
    fe_name = f"{spec.name}-frontend" if spec.frontend != "none" else None
    be_name = f"{spec.name}-backend" if spec.backend != "none" else None

    # Determine compliance fallback if not provided
    comp_list = list(spec.compliance)
    if not comp_list:
        if spec.industry == "ecommerce":
            comp_list = ["pci", "gdpr"]
        elif spec.industry == "finance":
            comp_list = ["sox", "pci"]
        elif spec.industry == "healthcare":
            comp_list = ["hipaa"]
        else:
            comp_list = ["gdpr"]

    # If both FE and BE present, run a single fullstack generation into output_root
    if fe_name and be_name:
        fs_argv = [
            python_bin,
            "scripts/generate_client_project.py",
            "--name", str(spec.name),
            "--industry", spec.industry,
            "--project-type", "fullstack",
            "--frontend", spec.frontend,
            "--backend", spec.backend,
            "--database", spec.database,
            "--auth", spec.auth,
            "--deploy", spec.deploy,
            "--output-dir", str(output_root),
            "--workers", str(args.workers),
            "--skip-system-checks",
            "--yes",
            "--in-place",
            "--no-subdir",
        ]
        if spec.features:
            fs_argv.extend(["--features", ",".join(spec.features)])
        if comp_list:
            fs_argv.extend(["--compliance", ",".join(comp_list)])
        if args.no_cursor_assets and not args.include_cursor_assets:
            fs_argv.append("--no-cursor-assets")
        if args.include_cursor_assets:
            fs_argv.append("--include-cursor-assets")
        if args.force:
            fs_argv.append("--force")
        print(f"\n[FULLSTACK] {' '.join(shlex.quote(x) for x in fs_argv)}")
        code = run_argv(fs_argv, cwd=repo_root)
        if code != 0:
            raise SystemExit(code)
        # In template mode (root .cursor present), skip post rules
        return

    # FE-only
    if fe_name and not be_name:
        fe_dir = output_root / fe_name
        if fe_dir.exists() and args.force:
            import shutil
            shutil.rmtree(fe_dir)
        manifest = build_fe_manifest(spec.frontend, comp_list)
        # Write manifest OUTSIDE the target project directory to avoid being deleted by generator --force
        fe_manifest_path = output_root / "_rules_manifests" / f"{fe_name}.json"
        write_rules_manifest(fe_manifest_path, manifest)
        fe_argv = [
            python_bin,
            "scripts/generate_client_project.py",
            "--name", fe_name,
            "--industry", spec.industry,
            "--project-type", "web",
            "--frontend", spec.frontend,
            "--backend", "none",
            "--database", "none",
            "--auth", spec.auth,
            "--deploy", spec.deploy,
            "--output-dir", str(output_root),
            "--workers", str(args.workers),
            "--rules-manifest", str(fe_manifest_path),
            "--skip-system-checks",
            "--yes",
        ]
        if spec.features:
            fe_argv.extend(["--features", ",".join(spec.features)])
        if args.in_place:
            fe_argv.append("--in-place")
        if args.no_cursor_assets:
            fe_argv.append("--no-cursor-assets")
        if args.include_cursor_assets:
            fe_argv.append("--include-cursor-assets")
        if args.force:
            fe_argv.append("--force")
        print(f"\n[FE] {' '.join(shlex.quote(x) for x in fe_argv)}")
        code = run_argv(fe_argv, cwd=repo_root)
        if code != 0:
            raise SystemExit(code)
        # Post-scaffold: run Generate Cursor Rules unless disabled or assets suppressed
        if not args.no_post_generate_rules and not args.no_cursor_assets:
            rules_argv = [
                python_bin,
                "scripts/run_generate_rules.py",
                "--project-dir", str(output_root / fe_name),
                "--overwrite",
            ]
            print(f"[FE][Rules] {' '.join(shlex.quote(x) for x in rules_argv)}")
            rc = run_argv(rules_argv, cwd=repo_root)
            if rc != 0:
                raise SystemExit(rc)

    # BE project (if any)
    # BE-only
    if be_name and not fe_name:
        be_dir = output_root / be_name
        if be_dir.exists() and args.force:
            import shutil
            shutil.rmtree(be_dir)
        manifest = build_be_manifest(spec.backend, spec.database, comp_list)
        # Write manifest OUTSIDE the target project directory to avoid being deleted by generator --force
        be_manifest_path = output_root / "_rules_manifests" / f"{be_name}.json"
        write_rules_manifest(be_manifest_path, manifest)
        be_argv = [
            python_bin,
            "scripts/generate_client_project.py",
            "--name", be_name,
            "--industry", spec.industry,
            "--project-type", "api",
            "--frontend", "none",
            "--backend", spec.backend,
            "--database", spec.database,
            "--auth", spec.auth,
            "--deploy", spec.deploy,
            "--output-dir", str(output_root),
            "--workers", str(args.workers),
            "--rules-manifest", str(be_manifest_path),
            "--skip-system-checks",
            "--yes",
        ]
        if spec.features:
            be_argv.extend(["--features", ",".join(spec.features)])
        if comp_list:
            be_argv.extend(["--compliance", ",".join(comp_list)])
        if args.in_place:
            be_argv.append("--in-place")
        if args.no_cursor_assets:
            be_argv.append("--no-cursor-assets")
        if args.include_cursor_assets:
            be_argv.append("--include-cursor-assets")
        if args.force:
            be_argv.append("--force")
        print(f"\n[BE] {' '.join(shlex.quote(x) for x in be_argv)}")
        code = run_argv(be_argv, cwd=repo_root)
        if code != 0:
            raise SystemExit(code)
        # Post-scaffold: run Generate Cursor Rules unless disabled or assets suppressed
        if not args.no_post_generate_rules and not args.no_cursor_assets:
            rules_argv = [
                python_bin,
                "scripts/run_generate_rules.py",
                "--project-dir", str(output_root / be_name),
                "--overwrite",
            ]
            print(f"[BE][Rules] {' '.join(shlex.quote(x) for x in rules_argv)}")
            rc = run_argv(rules_argv, cwd=repo_root)
            if rc != 0:
                raise SystemExit(rc)

    print("\n✅ Generation complete.")


if __name__ == "__main__":
    main()


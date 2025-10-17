#!/usr/bin/env python3
"""
Write a minimal project context report to .cursor/ai-governor/project.json.
- Detects root .cursor (isolation hint)
- Attempts to read generator-config.json if present for stack
- Accepts overrides via CLI flags

Usage:
  python scripts/write_context_report.py --project-name myapp --industry healthcare \
    --frontend nextjs --backend fastapi --database postgres --auth auth0 --deploy aws \
    --compliance hipaa,gdpr --output .cursor/ai-governor/project.json
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Dict, Any, List


def main() -> int:
    ap = argparse.ArgumentParser(description="Write context report JSON")
    ap.add_argument("--project-name", default=None)
    ap.add_argument("--industry", default=None)
    ap.add_argument("--frontend", default=None)
    ap.add_argument("--backend", default=None)
    ap.add_argument("--database", default=None)
    ap.add_argument("--auth", default=None)
    ap.add_argument("--deploy", default=None)
    ap.add_argument("--compliance", default=None)
    ap.add_argument("--output", default=".cursor/ai-governor/project.json")
    args = ap.parse_args()

    root = Path.cwd()
    has_root_cursor = (root / ".cursor").exists()

    # Try to load generator-config.json if exists
    gen_cfg_path = root / "generator-config.json"
    gen_cfg: Dict[str, Any] = {}
    if gen_cfg_path.exists():
        try:
            gen_cfg = json.loads(gen_cfg_path.read_text(encoding="utf-8"))
        except Exception:
            gen_cfg = {}

    project_name = args.project_name or gen_cfg.get("name") or root.name
    industry = args.industry or gen_cfg.get("industry")
    stack = {
        "frontend": args.frontend or gen_cfg.get("frontend"),
        "backend": args.backend or gen_cfg.get("backend"),
        "database": args.database or gen_cfg.get("database"),
        "auth": args.auth or gen_cfg.get("auth"),
        "deploy": args.deploy or gen_cfg.get("deploy"),
    }

    compliance_list: List[str] = []
    src = args.compliance or gen_cfg.get("compliance")
    if isinstance(src, str) and src:
        compliance_list = [c.strip() for c in src.split(',') if c.strip()]
    elif isinstance(src, list):
        compliance_list = [str(c).strip() for c in src]

    report = {
        "project_name": project_name,
        "industry": industry,
        "stack": stack,
        "compliance": compliance_list,
        "isolation": {
            "root_cursor_present": bool(has_root_cursor),
            "default_output_root": str((root / ".." / "_generated").resolve()),
            "nested_rules_emission": "off_by_default",
        },
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"[OK] wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

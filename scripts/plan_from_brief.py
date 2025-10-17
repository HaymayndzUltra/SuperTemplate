#!/usr/bin/env python3
"""
Generate PLAN.md and tasks.json from a brief.md.
No deploy. No code edits. Outputs are artifacts only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List
import sys

# Import via proper package path (scripts should be run from repo root)
# If running from elsewhere, use: python -m scripts.plan_from_brief
from project_generator.core.brief_parser import BriefParser
from scripts.lifecycle_tasks import build_plan


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate FE/BE plan artifacts from brief.md")
    p.add_argument("--brief", required=True, help="Path to brief.md")
    p.add_argument("--out", default="PLAN.md", help="Path to write PLAN.md (tasks.json will be co-located)")
    return p.parse_args()
def render_plan_md(spec, plan: Dict[str, List[Dict]]) -> str:
    lines: List[str] = []
    lines.append(f"# PLAN — {spec.name}\n")
    lines.append(
        f"Industry: {spec.industry} | Type: {spec.project_type} | Frontend: {spec.frontend} | Backend: {spec.backend}\n"
    )
    lines.append("## Lanes\n")
    for lane in ("backend", "frontend"):
        lines.append(f"### Lane: {lane}\n")
        for t in plan[lane]:
            bdeps = ", ".join(t["blocked_by"]) if t["blocked_by"] else "-"
            lines.append(f"- [{t['id']}] {t['title']} (blocked_by: {bdeps})")
        lines.append("")
    lines.append("## Conflicts & Guardrails\n")
    lines.append(
        "- Ports: FE 3000, BE 8000 (configurable)\n- Migrations vs seed/tests: lock sequencing\n- Secrets: no plaintext; env-injection only\n"
    )
    lines.append("## Next Triggers\n")
    lines.append(
        "- RUN_BE and RUN_FE in parallel (≤3 concurrent per lane)\n- CSAN if blocked\n- QA for completed scope\n- PR: artifacts + acceptance (STOP, no deploy)\n"
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    spec = BriefParser(args.brief).parse()
    plan = build_plan(spec)

    # Write tasks.json
    tasks_json_path = Path(args.out).with_suffix(".tasks.json")
    tasks_json_path.write_text(json.dumps(plan, indent=2), encoding="utf-8")

    # Write PLAN.md
    plan_md = render_plan_md(spec, plan)
    Path(args.out).write_text(plan_md, encoding="utf-8")

    print(f"Wrote {args.out} and {tasks_json_path}")


if __name__ == "__main__":
    main()

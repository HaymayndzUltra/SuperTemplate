#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BRIEFS_DIR = ROOT / "docs" / "briefs"

P1_FILES = [
    "requirements_summary.md",
    "questions.md",
    "stack_compliance_inference.md",
]

P2_FILES = [
    "PRD.md",
    "ARCHITECTURE.md",
    "API_PLAN.md",
    "UI_MAP.md",
    "SECURITY_COMPLIANCE_PLAN.md",
    "ESTIMATES.md",
]

FRONTMATTER_RE = re.compile(r"^---[\s\S]*?---\s*", re.M)


def parse_brief(brief_path: Path) -> dict:
    if not brief_path.exists():
        return {}
    text = brief_path.read_text(encoding="utf-8", errors="ignore")
    m = FRONTMATTER_RE.match(text)
    fm = {}
    if m:
        block = m.group(0)
        for line in block.splitlines():
            if ":" in line and not line.strip().startswith("---"):
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def ensure(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def scaffold_phase_1(pdir: Path, fm: dict):
    ensure(
        pdir / "requirements_summary.md",
        "# Requirements Summary\n\n- Fill goals, scope, constraints per brief.\n",
    )
    ensure(
        pdir / "questions.md",
        "# Open Questions\n\n- List unknowns for client sign-off.\n",
    )
    ensure(
        pdir / "stack_compliance_inference.md",
        "# Stack & Compliance Inference (Dry)\n\n- FE/BE/DB/Auth/Deploy with rationale.\n- HIPAA controls candidates.\n",
    )


def scaffold_phase_2(pdir: Path, fm: dict):
    ensure(
        pdir / "PRD.md",
        "# Product Requirements Document\n\n- Summarize features and success criteria.\n",
    )
    ensure(
        pdir / "ARCHITECTURE.md",
        "# Architecture\n\n- Overview + DB outline.\n",
    )
    ensure(
        pdir / "API_PLAN.md",
        "# API Plan\n\n- List representative endpoints.\n",
    )
    ensure(
        pdir / "UI_MAP.md",
        "# UI Map\n\n- Pages and core components.\n",
    )
    ensure(
        pdir / "SECURITY_COMPLIANCE_PLAN.md",
        "# Security & Compliance Plan\n\n- HIPAA controls: encryption, RBAC, audit logging, session timeout, no PHI in logs.\n",
    )
    ensure(
        pdir / "ESTIMATES.md",
        "# Estimates & Milestones\n\n- Timeline and risks.\n",
    )


def main():
    ap = argparse.ArgumentParser(description="Scaffold Phase artifacts under docs/briefs/<project>/")
    ap.add_argument("--project", required=True, help="Project key, e.g., acme-telehealth")
    ap.add_argument("--phase", type=int, choices=[1, 2], required=True)
    args = ap.parse_args()

    pdir = BRIEFS_DIR / args.project
    brief = pdir / "brief.md"
    fm = parse_brief(brief)

    if args.phase == 1:
        scaffold_phase_1(pdir, fm)
    elif args.phase == 2:
        scaffold_phase_2(pdir, fm)

    print(json.dumps({"project": args.project, "phase": args.phase, "dir": str(pdir)}, indent=2))


if __name__ == "__main__":
    main()
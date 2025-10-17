#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from typing import Dict, Any, List, Optional


def load_policies(repo_root: Path) -> List[Dict[str, Any]]:
    policy_path = repo_root / ".cursor" / "ai-driven-workflow" / "policy-dsl" / "project-selection.json"
    if not policy_path.exists():
        return []
    try:
        return json.loads(policy_path.read_text(encoding="utf-8"))
    except Exception:
        return []


def match_policy(policies: List[Dict[str, Any]], industry: str, project_type: str) -> Optional[Dict[str, Any]]:
    best = None
    best_priority = -1
    for p in policies:
        conds = set(c.strip().lower() for c in p.get("conditions", []))
        if not conds:
            continue
        required = {f"industry:{industry}", f"project_type:{project_type}"}
        if required.issubset(conds):
            prio = int(p.get("priority", 0))
            if prio > best_priority:
                best_priority = prio
                best = p
    return best


def choose_stack(args: argparse.Namespace, repo_root: Path) -> Dict[str, str]:
    industry = (args.industry or "").lower().strip() or "healthcare"
    project_type = (args.project_type or "").lower().strip() or "fullstack"

    defaults = {
        ("healthcare", "fullstack"): dict(frontend="nextjs", backend="fastapi", database="postgres", auth="auth0", compliance="hipaa"),
        ("finance", "api"): dict(backend="go", database="postgres", auth="cognito", compliance="sox,pci"),
        ("ecommerce", "fullstack"): dict(frontend="nextjs", backend="django", database="postgres", auth="firebase", compliance="pci,gdpr"),
        ("saas", "api"): dict(backend="django", database="postgres", auth="auth0"),
        ("enterprise", "web"): dict(frontend="nextjs", database="none", auth="cognito"),
    }

    policies = load_policies(repo_root)
    picked: Dict[str, str] = {}
    policy = match_policy(policies, industry, project_type)
    if policy and isinstance(policy.get("recommend"), dict):
        picked.update({k: str(v) for k, v in policy["recommend"].items()})
    picked.update(defaults.get((industry, project_type), {}))

    for key in ["frontend", "backend", "database", "auth", "deploy", "compliance"]:
        val = getattr(args, key, None)
        if val:
            picked[key] = str(val)

    if not picked.get("deploy"):
        picked["deploy"] = "aws"

    return {
        "industry": industry,
        "project_type": project_type,
        "frontend": picked.get("frontend", "nextjs" if project_type != "api" else "none"),
        "backend": picked.get("backend", "django" if project_type != "web" else "none"),
        "database": picked.get("database", "postgres"),
        "auth": picked.get("auth", "auth0"),
        "deploy": picked.get("deploy", "aws"),
        "compliance": picked.get("compliance", ""),
    }


def build_commands(name: str, ctx: Dict[str, str], output_dir: Path, workers: int, include_cursor_assets: bool, force: bool, dry_run: bool) -> Dict[str, List[str]]:
    cursor_flag = "--include-cursor-assets" if include_cursor_assets else "--no-cursor-assets"
    force_flag = " --force" if force else ""
    dry_flag = " --dry-run" if dry_run else ""

    base_cmd = (
        f"python scripts/generate_client_project.py"
        f" --name {name}"
        f" --industry {ctx['industry']}"
        f" --project-type {ctx['project_type']}"
        f" --frontend {ctx['frontend']}"
        f" --backend {ctx['backend']}"
        f" --database {ctx['database']}"
        f" --auth {ctx['auth']}"
        f"{' --compliance ' + ctx['compliance'] if ctx['compliance'] else ''}"
        f" --deploy {ctx['deploy']}"
        f" --output-dir {str(output_dir)}"
        f" --workers {workers}"
        f" {cursor_flag} --yes"
        f"{dry_flag}{force_flag}"
    ).strip()

    cmds = {
        "rules": [
            "Apply instructions from .cursor/rules/master-rules/1-master-rule-context-discovery.mdc",
            "Apply instructions from .cursor/rules/master-rules/2-master-rule-ai-collaboration-guidelines.mdc",
            "Apply instructions from .cursor/rules/master-rules/F8-security-and-compliance-overlay.mdc",
        ],
        "bootstrap": [
            "python scripts/doctor.py",
            "./scripts/generate_client_project.py --list-templates | cat",
        ],
        "generate": [
            base_cmd,
        ],
        "tests": [],
    }

    if ctx.get("backend") == "fastapi":
        cmds["tests"].append("scripts/setup_template_tests.sh fastapi")
    if ctx.get("backend") == "django":
        cmds["tests"].append("scripts/setup_template_tests.sh django")
    if ctx.get("frontend") == "nextjs":
        cmds["tests"].append("scripts/setup_template_tests.sh next")
    if ctx.get("frontend") == "angular":
        cmds["tests"].append("scripts/setup_template_tests.sh angular")

    return cmds


def print_plan(name: str, ctx: Dict[str, str], cmds: Dict[str, List[str]], print_triggers: bool) -> None:
    print("=== Project Trigger Plan ===")
    print(f"name: {name}")
    print("context:")
    for k in ["industry", "project_type", "frontend", "backend", "database", "auth", "deploy", "compliance"]:
        print(f"  {k}: {ctx.get(k) or 'none'}")
    print()

    if print_triggers:
        print("# Triggers to apply (in order):")
        for t in cmds["rules"]:
            print(f"- {t}")
        print()

    print("# Commands:")
    for section in ["bootstrap", "generate", "tests"]:
        for c in cmds[section]:
            print(c)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Emit a guided trigger/command plan for project generation.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--industry", default=None)
    parser.add_argument("--project-type", dest="project_type", default=None)
    parser.add_argument("--frontend", default=None)
    parser.add_argument("--backend", default=None)
    parser.add_argument("--database", default=None)
    parser.add_argument("--auth", default=None)
    parser.add_argument("--deploy", default=None)
    parser.add_argument("--compliance", default=None)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--output-dir", dest="output_dir", default="../_generated")
    parser.add_argument("--include-cursor-assets", dest="include_cursor_assets", action="store_true")
    parser.add_argument("--no-cursor-assets", dest="include_cursor_assets", action="store_false")
    parser.set_defaults(include_cursor_assets=False)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true")
    parser.add_argument("--print-triggers", dest="print_triggers", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = (repo_root / output_dir).resolve()
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass

    ctx = choose_stack(args, repo_root)
    cmds = build_commands(
        name=args.name,
        ctx=ctx,
        output_dir=output_dir,
        workers=args.workers,
        include_cursor_assets=bool(args.include_cursor_assets),
        force=bool(args.force),
        dry_run=bool(args.dry_run),
    )
    print_plan(args.name, ctx, cmds, print_triggers=bool(args.print_triggers))


if __name__ == "__main__":
    main()
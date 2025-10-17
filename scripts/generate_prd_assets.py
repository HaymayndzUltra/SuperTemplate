#!/usr/bin/env python3
"""Generate PRD and architecture summaries from planning artifacts."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent

PROTOCOL_PATH = Path("ai-driven-workflow/1-create-prd.md")

def iso_utc_now() -> str:
    return datetime.now(tz=timezone.utc).replace(microsecond=False).isoformat().replace("+00:00", "Z")


def read_plan_summary(path: Path) -> str:
    if not path.exists():
        return "Plan summary unavailable; see planning logs."
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        return stripped
    return "Plan summary unavailable; see planning logs."


def load_tasks(path: Path) -> dict[str, list[dict]]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    if isinstance(data, dict):
        return {k: v for k, v in data.items() if isinstance(v, list)}
    return {}


def extract_template_sections(protocol_path: Path) -> dict[str, str]:
    text = protocol_path.read_text(encoding="utf-8", errors="ignore") if protocol_path.exists() else ""
    marker = "```markdown"
    start = text.find(marker)
    if start == -1:
        return {}
    remainder = text[start + len(marker):]
    end = remainder.rfind("```")
    if end == -1:
        return {}
    block = remainder[:end]
    return {"template": dedent(block).strip()}


def build_task_section(tasks: dict[str, list[dict]]) -> str:
    if not tasks:
        return "- Derived from PLAN.tasks.json (no structured task data available)."
    lines: list[str] = []
    for area, items in sorted(tasks.items()):
        lines.append(f"- **{area.title()} Focus:**")
        if not items:
            lines.append("  - No tasks captured for this area yet.")
            continue
        for item in items[:5]:
            title = item.get("title") or item.get("summary") or "Unnamed task"
            ident = item.get("id") or "?"
            estimate = item.get("estimate")
            suffix = f" (estimate: {estimate})" if estimate else ""
            lines.append(f"  - [{ident}] {title}{suffix}")
        if len(items) > 5:
            lines.append(f"  - … {len(items) - 5} additional tasks omitted for brevity.")
    return "\n".join(lines)


def render_prd(args: argparse.Namespace, plan_summary: str, task_section: str) -> str:
    template_section = extract_template_sections(PROTOCOL_PATH).get("template")
    if not template_section:
        template_section = dedent(
            """
            # PRD: [Feature Name]

            ## 1. Overview
            - **Business Goal:** [Description of the need and problem solved]
            - **Detected Architecture:**
              - **Primary Component:** `[Frontend App | Backend Service | ...]`

            ## 2. Functional Specifications
            - **User Stories:** [For UI] or **API Contract:** [For Services]

            ## 3. Technical Specifications
            - **Inter-Service Communication:** [Details of API calls]
            - **Security & Authentication:** [Security model]

            ## 4. Out of Scope
            - [What this feature will NOT do]
            """
        ).strip()

    frontend = args.frontend or "TBD"
    backend = args.backend or "TBD"
    database = args.database or "TBD"
    auth = args.auth or "Role-based access as defined in compliance matrix"

    replacements = {
        "[Feature Name]": args.name,
        "[Description of the need and problem solved]": plan_summary,
        "`[Frontend App | Backend Service | ...]`": f"Frontend ({frontend}) + Backend ({backend}) + Database ({database})",
        "[For UI] or **API Contract:** [For Services]": "User stories derived from the validated task graph:",
        "[Details of API calls]": f"{backend} services expose REST endpoints consumed by the {frontend} frontend.",
        "[Security model]": auth,
        "[What this feature will NOT do]": "See PLAN.md for items explicitly deferred beyond the initial scaffold.",
    }

    body = template_section
    for needle, replacement in replacements.items():
        body = body.replace(needle, replacement)

    nested_tasks = "\n".join(f"  {line}" for line in task_section.splitlines())
    body = body.replace(
        "User stories derived from the validated task graph:",
        f"User stories derived from the validated task graph:\n{nested_tasks}",
    )

    signoff_block = dedent(
        f"""
        ---
        signoff_stage: PRD + Architecture OK
        signoff_approver: lifecycle-automation
        signoff_timestamp: {iso_utc_now()}
        ---
        """
    ).strip()

    industry_line = f"- **Industry Alignment:** {args.industry}" if args.industry else "- **Industry Alignment:** Unspecified"
    project_type_line = f"- **Project Type:** {args.project_type}" if args.project_type else "- **Project Type:** Unspecified"

    overview_block = f"- **Business Goal:** {plan_summary}\n{industry_line}\n{project_type_line}"
    body = body.replace(f"- **Business Goal:** {plan_summary}", overview_block)

    return f"{signoff_block}\n\n{body.strip()}\n"


def render_architecture(args: argparse.Namespace, task_section: str) -> str:
    frontend = args.frontend or "TBD"
    backend = args.backend or "TBD"
    database = args.database or "TBD"
    auth = args.auth or "TBD"
    deploy = args.deploy or "TBD"

    mermaid = dedent(
        f"""
        ```mermaid
        flowchart LR
          UI[{frontend}] --> API[{backend}]
          API --> DB[({database})]
        ```
        """
    ).strip()

    lines = dedent(
        f"""
        # Architecture Summary: {args.name}

        ## Primary Components
        - Frontend: {frontend}
        - Backend: {backend}
        - Database: {database}
        - Authentication: {auth}
        - Deployment Target: {deploy}

        ## Integration Flows
        - {frontend} consumes RESTful APIs exposed by {backend}.
        - {backend} persists canonical data to {database}.
        - Authentication is handled via {auth} to enforce least-privilege access.

        ## Supporting Tasks
        {task_section}

        ## System Diagram
        {mermaid}
        """
    ).strip()
    if args.industry:
        lines += f"\n\n## Compliance & Domain Notes\n- Architecture tuned for {args.industry} requirements."
    return lines + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate PRD and architecture assets from planning artifacts.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--tasks", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--frontend")
    parser.add_argument("--backend")
    parser.add_argument("--database")
    parser.add_argument("--auth")
    parser.add_argument("--deploy")
    parser.add_argument("--industry")
    parser.add_argument("--project-type")
    args = parser.parse_args()

    plan_summary = read_plan_summary(Path(args.plan))
    tasks = load_tasks(Path(args.tasks))
    task_section = build_task_section(tasks)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    prd_content = render_prd(args, plan_summary, task_section)
    (output_dir / "PRD.md").write_text(prd_content, encoding="utf-8")

    architecture_content = render_architecture(args, task_section)
    (output_dir / "ARCHITECTURE.md").write_text(architecture_content, encoding="utf-8")

    evidence_dir = output_dir / "evidence"
    evidence_dir.mkdir(exist_ok=True)
    (evidence_dir / "prd_generation.json").write_text(
        json.dumps(
            {
                "protocol": str(PROTOCOL_PATH),
                "plan": args.plan,
                "tasks": args.tasks,
                "generated_at": iso_utc_now(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

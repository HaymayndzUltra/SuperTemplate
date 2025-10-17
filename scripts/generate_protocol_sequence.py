#!/usr/bin/env python3
"""Generate protocol command files based on brief analysis."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from scripts.analyze_brief import BASE_PROTOCOLS

SCRIPT_REGISTRY_PATH = Path("scripts/script-registry.json")
PROTOCOL_DOCS: Dict[str, Tuple[str, Path]] = {
    "0-bootstrap": ("Bootstrap & Context Engineering", Path("unified_workflow/phases/0-bootstrap.md")),
    "1-prd-creation": ("Implementation-Ready PRD", Path("unified_workflow/phases/1-prd-creation.md")),
    "2-task-generation": ("Task Generation & Delivery Plan", Path("unified_workflow/phases/2-task-generation.md")),
    "3-implementation": ("Execution & Evidence Capture", Path("unified_workflow/phases/3-implementation.md")),
    "4-quality-audit": ("Quality Audit & Release Readiness", Path("unified_workflow/phases/4-quality-audit.md")),
    "5-retrospective": ("Retrospective & Continuous Improvement", Path("unified_workflow/phases/5-retrospective.md")),
    "6-operations": ("Operations, Deployment & Observability", Path("unified_workflow/phases/6-operations.md")),
}

DEFAULT_EXTRA_SCRIPTS = {
    "6-operations": {
        "deployment": "scripts/deploy_backend.sh",
        "rollback": "scripts/rollback_backend.sh",
        "performance": "scripts/collect_perf.py",
    },
    "ml-experiments": {
        "model-tracking": "scripts/run_workflow.py --phase ml",
    },
}


@dataclass
class CommandArtifact:
    slug: str
    title: str
    doc_path: Path
    scripts: Dict[str, str]
    index: int

    @property
    def filename(self) -> str:
        return f"{self.index:02d}-{self.slug}.md"

    def to_markdown(self, analysis: dict) -> str:
        brief_meta = analysis.get("metadata", {})
        stack = brief_meta.get("stack") or {}
        stack_summary = ", ".join(f"{k}: {v}" for k, v in stack.items()) if stack else "n/a"
        compliance = brief_meta.get("compliance") or []
        compliance_summary = ", ".join(compliance) if compliance else "None"

        lines = [
            f"# {self.index:02d}. {self.title}",
            "",
            "## Purpose",
            f"Use the protocol at `{self.doc_path}` to complete this phase. Follow the unified template and capture evidence for the orchestrator.",
            "",
            "## Context Snapshot",
            f"- Project Type: {brief_meta.get('project_type') or 'Unknown'}",
            f"- Complexity: {brief_meta.get('complexity') or 'Unspecified'}",
            f"- Lifecycle: {brief_meta.get('lifecycle') or 'Unspecified'}",
            f"- Stack: {stack_summary}",
            f"- Compliance Signals: {compliance_summary}",
            "",
            "## Automation Hooks",
        ]

        if self.scripts:
            for name, script in self.scripts.items():
                exists = Path(script.split()[0]).exists()
                status = "✅" if exists else "⚠️"
                lines.append(f"- {status} `{script}` ({name.replace('-', ' ').title()})")
        else:
            lines.append("- ⚠️ No automation scripts mapped; follow manual protocol instructions.")

        lines.extend(
            [
                "",
                "## Execution Guidance",
                "1. Review the linked protocol document and confirm prerequisites.",
                "2. Execute the automation hooks above (or their equivalents) to accelerate the phase.",
                "3. Record artifacts with `scripts/evidence_manager.py` and update task state as needed.",
                "4. Run the phase quality gate before handing off to the next protocol.",
                "",
                "## Evidence & Quality Gates",
                "- Ensure quality gate scripts report success before advancing.",
                "- Attach logs, reports, and approvals to the evidence manifest.",
                "- Document deviations or skipped automation in the orchestrator report.",
            ]
        )

        return "\n".join(lines)


def load_analysis(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry(path: Path) -> Dict[str, Dict[str, str]]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_scripts(protocol: str, registry: Dict[str, Dict[str, str]]) -> Dict[str, str]:
    registry_key = {
        "0-bootstrap": "bootstrap",
        "1-prd-creation": "prd",
        "2-task-generation": "task-generation",
        "3-implementation": "execution",
        "4-quality-audit": "quality",
        "5-retrospective": "retrospective",
        "6-operations": "operations",
        "ml-experiments": "ml",
    }.get(protocol, protocol)

    scripts = registry.get(registry_key, {}).copy()
    scripts.update(DEFAULT_EXTRA_SCRIPTS.get(protocol, {}))
    return scripts


def build_commands(analysis: dict, output_dir: Path, registry: Dict[str, Dict[str, str]]) -> List[CommandArtifact]:
    protocols: List[str] = analysis.get("detected_protocols") or BASE_PROTOCOLS
    artifacts: List[CommandArtifact] = []

    for index, protocol in enumerate(protocols):
        slug = protocol
        title, doc_path = PROTOCOL_DOCS.get(protocol, (protocol.replace("-", " ").title(), Path("templates/protocol-template.md")))
        scripts = resolve_scripts(protocol, registry)
        artifact = CommandArtifact(slug=slug, title=title, doc_path=doc_path, scripts=scripts, index=index)
        artifacts.append(artifact)

        content = artifact.to_markdown(analysis)
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / artifact.filename).write_text(content, encoding="utf-8")

    return artifacts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate protocol command files from brief analysis")
    parser.add_argument("--analysis", required=True, help="Path to analysis JSON from scripts/analyze_brief.py")
    parser.add_argument("--output-dir", default=".cursor/commands/generated", help="Directory to place generated command files")
    parser.add_argument("--summary", action="store_true", help="Print summary of generated commands")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    analysis_path = Path(args.analysis)
    if not analysis_path.exists():
        raise FileNotFoundError(f"Analysis JSON not found: {analysis_path}")

    registry = load_registry(SCRIPT_REGISTRY_PATH)
    analysis = load_analysis(analysis_path)

    output_dir = Path(args.output_dir)
    artifacts = build_commands(analysis, output_dir, registry)

    if args.summary:
        print(json.dumps(
            [
                {
                    "file": str(output_dir / artifact.filename),
                    "title": artifact.title,
                    "scripts": artifact.scripts,
                }
                for artifact in artifacts
            ],
            indent=2,
        ))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Analyze PROJECT-BRIEF.md and output structured metadata."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Set

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - fallback when PyYAML is unavailable
    yaml = None

BASE_PROTOCOLS = [
    "0-bootstrap",
    "1-prd-creation",
    "2-task-generation",
    "3-implementation",
    "4-quality-audit",
    "5-retrospective",
]

OPERATIONS_KEYWORDS = {
    "deployment",
    "deploy",
    "monitoring",
    "observability",
    "uptime",
    "slo",
    "incident",
    "operations",
    "devops",
    "sre",
}

COMPLIANCE_KEYWORDS = {
    "hipaa": "HIPAA",
    "soc2": "SOC2",
    "pci": "PCI",
    "gdpr": "GDPR",
    "iso27001": "ISO27001",
}

ML_KEYWORDS = {
    "machine learning",
    "ml",
    "model",
    "training",
    "inference",
    "dataset",
}

COMPLEXITY_KEYWORDS = {
    "simple": "simple",
    "prototype": "mvp",
    "mvp": "mvp",
    "production": "production",
    "enterprise": "enterprise",
    "complex": "complex",
}


@dataclass
class BriefAnalysis:
    brief_path: str
    metadata: Dict[str, object]
    detected_protocols: List[str]
    flags: Dict[str, object]

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True)


def extract_frontmatter(content: str) -> Dict[str, object]:
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    frontmatter = parts[1]
    if yaml is not None:
        try:
            data = yaml.safe_load(frontmatter) or {}
            if not isinstance(data, dict):
                return {}
            return data
        except yaml.YAMLError:
            return {}
    return _parse_simple_frontmatter(frontmatter)


def _parse_simple_frontmatter(frontmatter: str) -> Dict[str, object]:
    data: Dict[str, object] = {}
    current_list_key: Optional[str] = None
    for raw_line in frontmatter.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("-") and current_list_key:
            data.setdefault(current_list_key, []).append(line.lstrip("-").strip())
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if not value:
                data[key] = []
                current_list_key = key
                continue
            current_list_key = None
            # Handle comma-separated lists
            if "," in value:
                data[key] = [item.strip() for item in value.split(",") if item.strip()]
            else:
                data[key] = value
    return data


def strip_frontmatter(content: str) -> str:
    if not content.startswith("---"):
        return content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    return parts[2]


def detect_stack(frontmatter: Dict[str, object]) -> Dict[str, str]:
    stack: Dict[str, str] = {}
    for key in ["stack", "frontend", "backend", "database", "infrastructure", "language"]:
        value = frontmatter.get(key)
        if isinstance(value, str):
            stack[key] = value
        elif isinstance(value, list):
            stack[key] = ", ".join(str(v) for v in value)
        elif isinstance(value, dict) and key == "stack":
            for stack_key, stack_value in value.items():
                stack[stack_key] = str(stack_value)
    return stack


def detect_compliance(frontmatter: Dict[str, object], body: str) -> List[str]:
    compliance: Set[str] = set()
    value = frontmatter.get("compliance")
    if isinstance(value, list):
        compliance.update(str(item).upper() for item in value)
    elif isinstance(value, str):
        compliance.add(value.upper())
    body_lower = body.lower()
    for keyword, label in COMPLIANCE_KEYWORDS.items():
        if keyword in body_lower:
            compliance.add(label)
    return sorted(compliance)


def detect_operations(body: str) -> bool:
    body_lower = body.lower()
    return any(keyword in body_lower for keyword in OPERATIONS_KEYWORDS)


def detect_ml(body: str) -> bool:
    body_lower = body.lower()
    return any(keyword in body_lower for keyword in ML_KEYWORDS)


def detect_complexity(frontmatter: Dict[str, object], body: str) -> Optional[str]:
    value = frontmatter.get("complexity")
    if isinstance(value, str) and value:
        return value.lower()
    body_lower = body.lower()
    for keyword, level in COMPLEXITY_KEYWORDS.items():
        if re.search(r"\\b" + re.escape(keyword) + r"\\b", body_lower):
            return level
    return None


def detect_lifecycle(frontmatter: Dict[str, object], body: str) -> Optional[str]:
    lifecycle = frontmatter.get("lifecycle")
    if isinstance(lifecycle, str):
        return lifecycle.lower()
    body_lower = body.lower()
    for keyword, level in COMPLEXITY_KEYWORDS.items():
        if keyword in body_lower:
            return level
    return None


def determine_protocols(frontmatter: Dict[str, object], body: str) -> List[str]:
    phases = frontmatter.get("phases")
    if isinstance(phases, list) and phases:
        return [str(phase) for phase in phases]

    protocols = BASE_PROTOCOLS.copy()
    if detect_operations(body):
        protocols.append("6-operations")
    if detect_ml(body):
        protocols.append("ml-experiments")
    return protocols


def analyze_brief(path: Path) -> BriefAnalysis:
    content = path.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(content)
    body = strip_frontmatter(content)

    project_type = frontmatter.get("project_type") or frontmatter.get("type")
    title = frontmatter.get("name") or path.stem

    stack = detect_stack(frontmatter)
    compliance = detect_compliance(frontmatter, body)
    complexity = detect_complexity(frontmatter, body)
    lifecycle = detect_lifecycle(frontmatter, body)
    operations = detect_operations(body)
    ml_detected = detect_ml(body)

    metadata: Dict[str, object] = {
        "title": title,
        "project_type": project_type,
        "stack": stack,
        "complexity": complexity,
        "lifecycle": lifecycle,
        "compliance": compliance,
    }

    flags: Dict[str, object] = {
        "operations": operations,
        "ml": ml_detected,
        "custom_phases": frontmatter.get("phases") or None,
    }

    protocols = determine_protocols(frontmatter, body)

    return BriefAnalysis(
        brief_path=str(path),
        metadata=metadata,
        detected_protocols=protocols,
        flags={key: value for key, value in flags.items() if value},
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze a project brief and output workflow metadata")
    parser.add_argument("--brief", default="PROJECT-BRIEF.md", help="Path to project brief")
    parser.add_argument("--output", help="Optional output path for analysis JSON")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON result to stdout")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    brief_path = Path(args.brief)
    if not brief_path.exists():
        raise FileNotFoundError(f"Brief not found: {brief_path}")

    analysis = analyze_brief(brief_path)
    output_json = analysis.to_json()

    if args.output:
        Path(args.output).write_text(output_json, encoding="utf-8")
    if args.pretty or not args.output:
        print(output_json)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validator 10 - Meta-Reflection"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

from validator_utils import (
    BaseProtocolValidator,
    DimensionResult,
    collect_section_text,
    normalize_score,
    run_cli,
)


class ReflectionValidator(BaseProtocolValidator):
    slug = "reflection"
    name = "Meta-Reflection Validator"
    dimension_weights = {
        "retrospective_analysis": 0.30,
        "continuous_improvement": 0.25,
        "system_evolution": 0.20,
        "knowledge_capture": 0.15,
        "future_planning": 0.10,
    }
    pass_threshold = 0.85
    warning_threshold = 0.7

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        reflection_text = collect_section_text(content, ["RETROSPECTIVE", "IMPROVEMENT", "REFLECTION", "LESSONS", "FUTURE"])
        evidence_text = collect_section_text(content, ["EVIDENCE", "SUMMARY"])
        combined_text = "\n".join(filter(None, [reflection_text, evidence_text]))
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 10.1 - Retrospective Analysis
        retrospective_keywords = ["analysis", "review", "metrics", "performance", "success", "failure"]
        retrospective_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in retrospective_keywords)]
        retrospective_findings = {
            "retrospective_lines": retrospective_lines[:10],
            "count": len(retrospective_lines),
        }
        retrospective_issues = []
        if len(retrospective_lines) >= 3:
            retrospective_status = "pass"
        elif retrospective_lines:
            retrospective_status = "warning"
        else:
            retrospective_status = "fail"
            retrospective_issues.append("Retrospective analysis not documented.")
        retrospective_score = normalize_score(retrospective_status, pass_value=1.0, warning_value=0.5)
        dimensions["retrospective_analysis"] = DimensionResult(
            retrospective_status,
            retrospective_score,
            retrospective_findings,
            retrospective_issues,
            [],
        )

        # Dimension 10.2 - Continuous Improvement
        improvement_keywords = ["improvement", "action", "plan", "remediation", "follow-up", "fix"]
        improvement_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in improvement_keywords)]
        improvement_findings = {
            "improvement_lines": improvement_lines[:10],
            "count": len(improvement_lines),
        }
        improvement_issues = []
        if len(improvement_lines) >= 3:
            improvement_status = "pass"
        elif improvement_lines:
            improvement_status = "warning"
        else:
            improvement_status = "fail"
            improvement_issues.append("Continuous improvement plan missing.")
        improvement_score = normalize_score(improvement_status, pass_value=1.0, warning_value=0.5)
        dimensions["continuous_improvement"] = DimensionResult(
            improvement_status,
            improvement_score,
            improvement_findings,
            improvement_issues,
            [],
        )

        # Dimension 10.3 - System Evolution
        evolution_keywords = ["version", "change", "update", "history", "impact", "rollback"]
        evolution_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in evolution_keywords)]
        evolution_findings = {
            "evolution_lines": evolution_lines[:10],
            "count": len(evolution_lines),
        }
        evolution_issues = []
        if len(evolution_lines) >= 2:
            evolution_status = "pass"
        elif evolution_lines:
            evolution_status = "warning"
        else:
            evolution_status = "fail"
            evolution_issues.append("System evolution history not captured.")
        evolution_score = normalize_score(evolution_status, pass_value=1.0, warning_value=0.5)
        dimensions["system_evolution"] = DimensionResult(
            evolution_status,
            evolution_score,
            evolution_findings,
            evolution_issues,
            [],
        )

        # Dimension 10.4 - Knowledge Capture
        knowledge_keywords = ["lesson", "best practice", "anti-pattern", "knowledge", "catalog", "wiki"]
        knowledge_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in knowledge_keywords)]
        knowledge_findings = {
            "knowledge_lines": knowledge_lines[:10],
            "count": len(knowledge_lines),
        }
        knowledge_issues = []
        if len(knowledge_lines) >= 2:
            knowledge_status = "pass"
        elif knowledge_lines:
            knowledge_status = "warning"
        else:
            knowledge_status = "fail"
            knowledge_issues.append("Knowledge capture guidance missing.")
        knowledge_score = normalize_score(knowledge_status, pass_value=1.0, warning_value=0.5)
        dimensions["knowledge_capture"] = DimensionResult(
            knowledge_status,
            knowledge_score,
            knowledge_findings,
            knowledge_issues,
            [],
        )

        # Dimension 10.5 - Future Planning
        future_keywords = ["future", "roadmap", "next", "timeline", "priority", "upcoming"]
        future_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in future_keywords)]
        future_findings = {
            "future_lines": future_lines[:10],
            "count": len(future_lines),
        }
        future_issues = []
        if len(future_lines) >= 2:
            future_status = "pass"
        elif future_lines:
            future_status = "warning"
        else:
            future_status = "fail"
            future_issues.append("Future planning not specified.")
        future_score = normalize_score(future_status, pass_value=1.0, warning_value=0.5)
        dimensions["future_planning"] = DimensionResult(
            future_status,
            future_score,
            future_findings,
            future_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate meta-reflection guidance")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = ReflectionValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())

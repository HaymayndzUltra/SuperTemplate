#!/usr/bin/env python3
"""Validator 9 - Cognitive Reasoning"""
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


class ReasoningValidator(BaseProtocolValidator):
    slug = "reasoning"
    name = "Cognitive Reasoning Validator"
    dimension_weights = {
        "reasoning_patterns": 0.25,
        "decision_trees": 0.25,
        "problem_solving": 0.20,
        "learning_mechanisms": 0.15,
        "meta_cognition": 0.15,
    }
    pass_threshold = 0.85
    warning_threshold = 0.7

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        reasoning_text = collect_section_text(content, ["REASONING", "COGNITIVE", "THINKING", "STRATEGY"])
        workflow_text = collect_section_text(content, ["WORKFLOW", "STEP"])
        combined_text = "\n".join(filter(None, [reasoning_text, workflow_text]))
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 9.1 - Reasoning Patterns
        pattern_keywords = ["pattern", "heuristic", "playbook", "framework", "loop"]
        pattern_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in pattern_keywords)]
        pattern_findings = {
            "pattern_lines": pattern_lines[:10],
            "count": len(pattern_lines),
        }
        pattern_issues = []
        if len(pattern_lines) >= 3:
            pattern_status = "pass"
        elif pattern_lines:
            pattern_status = "warning"
        else:
            pattern_status = "fail"
            pattern_issues.append("Reasoning patterns not documented.")
        pattern_score = normalize_score(pattern_status, pass_value=1.0, warning_value=0.5)
        dimensions["reasoning_patterns"] = DimensionResult(
            pattern_status,
            pattern_score,
            pattern_findings,
            pattern_issues,
            [],
        )

        # Dimension 9.2 - Decision Trees
        decision_keywords = ["if", "choose", "option", "branch", "decision"]
        decision_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in decision_keywords) and ("if" in line.lower() or "option" in line.lower())]
        decision_findings = {
            "decision_lines": decision_lines[:10],
            "count": len(decision_lines),
        }
        decision_issues = []
        if len(decision_lines) >= 3:
            decision_status = "pass"
        elif decision_lines:
            decision_status = "warning"
        else:
            decision_status = "fail"
            decision_issues.append("Decision trees or options not defined.")
        decision_score = normalize_score(decision_status, pass_value=1.0, warning_value=0.5)
        dimensions["decision_trees"] = DimensionResult(
            decision_status,
            decision_score,
            decision_findings,
            decision_issues,
            [],
        )

        # Dimension 9.3 - Problem-Solving Logic
        problem_keywords = ["issue", "problem", "root cause", "mitigation", "solution", "diagnose"]
        problem_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in problem_keywords)]
        problem_findings = {
            "problem_lines": problem_lines[:10],
            "count": len(problem_lines),
        }
        problem_issues = []
        if len(problem_lines) >= 3:
            problem_status = "pass"
        elif problem_lines:
            problem_status = "warning"
        else:
            problem_status = "fail"
            problem_issues.append("Problem-solving guidance missing.")
        problem_score = normalize_score(problem_status, pass_value=1.0, warning_value=0.5)
        dimensions["problem_solving"] = DimensionResult(
            problem_status,
            problem_score,
            problem_findings,
            problem_issues,
            [],
        )

        # Dimension 9.4 - Learning Mechanisms
        learning_keywords = ["feedback", "improve", "learn", "retrospective", "capture", "update"]
        learning_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in learning_keywords)]
        learning_findings = {
            "learning_lines": learning_lines[:10],
            "count": len(learning_lines),
        }
        learning_issues = []
        if len(learning_lines) >= 2:
            learning_status = "pass"
        elif learning_lines:
            learning_status = "warning"
        else:
            learning_status = "fail"
            learning_issues.append("Learning mechanisms not described.")
        learning_score = normalize_score(learning_status, pass_value=1.0, warning_value=0.5)
        dimensions["learning_mechanisms"] = DimensionResult(
            learning_status,
            learning_score,
            learning_findings,
            learning_issues,
            [],
        )

        # Dimension 9.5 - Meta-Cognition
        meta_keywords = ["reflect", "self", "monitor", "awareness", "adjust", "improve"]
        meta_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in meta_keywords)]
        meta_findings = {
            "meta_lines": meta_lines[:10],
            "count": len(meta_lines),
        }
        meta_issues = []
        if len(meta_lines) >= 2:
            meta_status = "pass"
        elif meta_lines:
            meta_status = "warning"
        else:
            meta_status = "fail"
            meta_issues.append("Meta-cognition guidance absent.")
        meta_score = normalize_score(meta_status, pass_value=1.0, warning_value=0.5)
        dimensions["meta_cognition"] = DimensionResult(
            meta_status,
            meta_score,
            meta_findings,
            meta_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate cognitive reasoning guidance")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = ReasoningValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())

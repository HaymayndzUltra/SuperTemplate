#!/usr/bin/env python3
"""Validator 9 - Cognitive Reasoning validation."""

import re
from pathlib import Path
from typing import Dict

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolReasoningValidator(ProtocolValidatorBase):
    """Validates reasoning patterns, decision trees, problem solving, learning, and meta-cognition."""

    VALIDATOR_NAME = "protocol_reasoning"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.DIMENSIONS = (
            ("reasoning_patterns", 0.25, self._validate_reasoning_patterns),
            ("decision_trees", 0.25, self._validate_decision_trees),
            ("problem_solving", 0.20, self._validate_problem_solving),
            ("learning_mechanisms", 0.15, self._validate_learning_mechanisms),
            ("meta_cognition", 0.15, self._validate_meta_cognition),
        )

    def _validate_reasoning_patterns(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._extract_section(content, "WORKFLOW") + "\n" + self._extract_section(content, "PREREQUISITES")
        evidence: Dict[str, bool] = {
            "pattern_keywords": self._has_keywords(section, ["pattern", "heuristic", "framework", "model"]),
            "pattern_application": self._has_keywords(section, ["apply", "use", "leverage"]),
            "pattern_documented": bool(re.search(r"pattern", section, re.IGNORECASE)),
            "pattern_evolution": self._has_keywords(section, ["refine", "improve", "update"]),
        }

        return self._build_dimension_result(
            "Reasoning Patterns",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_decision_trees(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._extract_section(content, "WORKFLOW")
        evidence: Dict[str, bool] = {
            "decision_points": self._has_keywords(section, ["decision", "choose", "option"]),
            "criteria": self._has_keywords(section, ["if", "when", "threshold"]),
            "outcomes": self._has_keywords(section, ["result", "outcome", "branch"]),
            "logging": self._has_keywords(section, ["log", "record", "document"]),
        }

        return self._build_dimension_result(
            "Decision Trees",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_problem_solving(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._extract_section(content, "WORKFLOW") + "\n" + self._extract_section(content, "QUALITY GATES")
        evidence: Dict[str, bool] = {
            "problem_identification": self._has_keywords(section, ["problem", "issue", "risk"]),
            "root_cause": self._has_keywords(section, ["root cause", "analysis", "why"]),
            "solution_generation": self._has_keywords(section, ["solve", "solution", "remediation"]),
            "validation": self._has_keywords(section, ["validate", "confirm", "test"]),
        }

        return self._build_dimension_result(
            "Problem-Solving Logic",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_learning_mechanisms(self, protocol_id: str, content: str) -> DimensionResult:
        section = content
        evidence: Dict[str, bool] = {
            "feedback_loops": self._has_keywords(section, ["feedback", "loop", "review"]),
            "improvement_tracking": self._has_keywords(section, ["track", "measure", "metric"]),
            "knowledge_base": self._has_keywords(section, ["knowledge", "repository", "wiki"]),
            "adaptation": self._has_keywords(section, ["adapt", "adjust", "update"]),
        }

        return self._build_dimension_result(
            "Learning Mechanisms",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_meta_cognition(self, protocol_id: str, content: str) -> DimensionResult:
        section = content
        evidence: Dict[str, bool] = {
            "self_awareness": self._has_keywords(section, ["limitation", "assumption", "aware"]),
            "self_monitoring": self._has_keywords(section, ["monitor", "track", "observe"]),
            "self_correction": self._has_keywords(section, ["correct", "adjust", "fix"]),
            "self_improvement": self._has_keywords(section, ["improve", "refine", "enhance"]),
        }

        return self._build_dimension_result(
            "Meta-Cognition",
            evidence,
            evidence={"checks": evidence},
        )


def main() -> None:
    run_validator_cli(ProtocolReasoningValidator)


if __name__ == "__main__":
    main()

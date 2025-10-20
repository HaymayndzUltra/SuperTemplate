#!/usr/bin/env python3
"""Validator 10 - Meta-Reflection validation."""

from pathlib import Path
from typing import Dict

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolReflectionValidator(ProtocolValidatorBase):
    """Validates retrospective analysis, continuous improvement, evolution, knowledge capture, and planning."""

    VALIDATOR_NAME = "protocol_reflection"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.DIMENSIONS = (
            ("retrospective_analysis", 0.30, self._validate_retrospective),
            ("continuous_improvement", 0.25, self._validate_improvement),
            ("system_evolution", 0.20, self._validate_evolution),
            ("knowledge_capture", 0.15, self._validate_knowledge),
            ("future_planning", 0.10, self._validate_future_planning),
        )

    def _validate_retrospective(self, protocol_id: str, content: str) -> DimensionResult:
        evidence: Dict[str, bool] = {
            "execution_review": self._has_keywords(content, ["retrospective", "review", "reflection"]),
            "performance_metrics": self._has_keywords(content, ["metric", "score", "performance"]),
            "issue_identification": self._has_keywords(content, ["issue", "gap", "problem"]),
            "success_factors": self._has_keywords(content, ["success", "worked", "effective"]),
        }

        return self._build_dimension_result(
            "Retrospective Analysis",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_improvement(self, protocol_id: str, content: str) -> DimensionResult:
        evidence: Dict[str, bool] = {
            "improvement_opportunities": self._has_keywords(content, ["improvement", "opportunity", "enhance"]),
            "improvement_plans": self._has_keywords(content, ["plan", "action", "remediation"]),
            "improvement_tracking": self._has_keywords(content, ["track", "monitor", "progress"]),
            "improvement_evidence": self._has_keywords(content, ["evidence", "result", "proof"]),
        }

        return self._build_dimension_result(
            "Continuous Improvement",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_evolution(self, protocol_id: str, content: str) -> DimensionResult:
        evidence: Dict[str, bool] = {
            "version_history": self._has_keywords(content, ["version", "changelog", "history"]),
            "change_rationale": self._has_keywords(content, ["why", "because", "rationale"]),
            "impact_assessment": self._has_keywords(content, ["impact", "effect", "risk"]),
            "rollback": self._has_keywords(content, ["rollback", "revert", "undo"]),
        }

        return self._build_dimension_result(
            "System Evolution",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_knowledge(self, protocol_id: str, content: str) -> DimensionResult:
        evidence: Dict[str, bool] = {
            "lessons_learned": self._has_keywords(content, ["lesson", "learning", "insight"]),
            "best_practices": self._has_keywords(content, ["best practice", "recommended", "tip"]),
            "anti_patterns": self._has_keywords(content, ["avoid", "anti-pattern", "do not"]),
            "knowledge_base": self._has_keywords(content, ["knowledge base", "wiki", "repository"]),
        }

        return self._build_dimension_result(
            "Knowledge Capture",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_future_planning(self, protocol_id: str, content: str) -> DimensionResult:
        evidence: Dict[str, bool] = {
            "roadmap": self._has_keywords(content, ["roadmap", "plan", "next phase"]),
            "priorities": self._has_keywords(content, ["priority", "focus", "important"]),
            "resources": self._has_keywords(content, ["resource", "budget", "capacity"]),
            "timeline": self._has_keywords(content, ["timeline", "schedule", "when"]),
        }

        return self._build_dimension_result(
            "Future Planning",
            evidence,
            evidence={"checks": evidence},
        )


def main() -> None:
    run_validator_cli(ProtocolReflectionValidator)


if __name__ == "__main__":
    main()

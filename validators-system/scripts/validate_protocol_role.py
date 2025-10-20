#!/usr/bin/env python3
"""Validator 2 - AI Role and Mission validation."""

import re
from pathlib import Path
from typing import Dict

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolRoleValidator(ProtocolValidatorBase):
    """Validates AI role definition, mission, constraints, outputs, and behavior."""

    VALIDATOR_NAME = "protocol_role"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.DIMENSIONS = (
            ("role_definition", 0.25, self._validate_role_definition),
            ("mission_statement", 0.25, self._validate_mission_statement),
            ("constraints_guidelines", 0.20, self._validate_constraints),
            ("output_expectations", 0.15, self._validate_output_expectations),
            ("behavioral_guidance", 0.15, self._validate_behavioral_guidance),
        )

    def _get_role_section(self, content: str) -> str:
        return self._extract_section(content, "AI ROLE AND MISSION")

    def _validate_role_definition(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_role_section(content)
        evidence: Dict[str, bool] = {}
        evidence["role_title"] = bool(re.search(r"you are a \*\*[^*]+\*\*", section, re.IGNORECASE))
        evidence["role_description"] = len(section) > 120
        evidence["domain_expertise"] = self._has_keywords(section, ["expertise", "domain", "specialist", "experience"])
        evidence["behavioral_traits"] = self._has_keywords(section, ["tone", "style", "approach", "persona"])

        return self._build_dimension_result(
            "Role Definition",
            evidence,
            evidence={"section_present": bool(section), "checks": evidence},
        )

    def _validate_mission_statement(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_role_section(content)
        evidence: Dict[str, bool] = {}
        mission_match = re.search(r"mission\s+is\s+to\s+([^\n]+)", section, re.IGNORECASE)
        evidence["mission_clarity"] = bool(mission_match)
        evidence["scope_boundaries"] = self._has_keywords(section, ["scope", "within", "out of scope", "boundaries"])
        evidence["success_criteria"] = self._has_keywords(section, ["success", "complete", "done when", "approval"])
        evidence["value_proposition"] = self._has_keywords(section, ["value", "why", "impact", "benefit"])

        return self._build_dimension_result(
            "Mission Statement",
            evidence,
            evidence={"mission_excerpt": mission_match.group(0) if mission_match else "", "checks": evidence},
        )

    def _validate_constraints(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_role_section(content)
        markers = self._count_markers(section)
        evidence: Dict[str, bool] = {
            "critical_constraints": markers["critical"] > 0,
            "must_rules": markers["must"] > 0,
            "guidelines": markers["guideline"] > 0,
            "prohibitions": self._has_keywords(section, ["never", "do not", "avoid"]),
        }

        return self._build_dimension_result(
            "Constraints & Guidelines",
            evidence,
            evidence={"markers": markers},
        )

    def _validate_output_expectations(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_role_section(content)
        evidence: Dict[str, bool] = {
            "format": self._has_keywords(section, ["markdown", "json", "yaml", "text block"]),
            "structure": self._has_keywords(section, ["section", "structure", "include", "must contain"]),
            "location": bool(re.search(r"\.artifacts/[^`\s]+", section)),
            "validation": self._has_keywords(section, ["quality", "validate", "check", "score"]),
        }

        return self._build_dimension_result(
            "Output Expectations",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_behavioral_guidance(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_role_section(content)
        evidence: Dict[str, bool] = {
            "communication_style": self._has_keywords(section, ["communicate", "tone", "style", "voice"]),
            "decision_making": self._has_keywords(section, ["decide", "prioritize", "choose", "decision"]),
            "error_handling": self._has_keywords(section, ["if", "when stuck", "halt", "escalate"]),
            "user_interaction": self._has_keywords(section, ["ask", "confirm", "reviewer", "client"]),
        }

        return self._build_dimension_result(
            "Behavioral Guidance",
            evidence,
            evidence={"checks": evidence},
        )


def main() -> None:
    run_validator_cli(ProtocolRoleValidator)


if __name__ == "__main__":
    main()

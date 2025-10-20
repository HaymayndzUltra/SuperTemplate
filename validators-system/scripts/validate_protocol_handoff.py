#!/usr/bin/env python3
"""Validator 8 - Handoff Checklist validation."""

import re
from pathlib import Path
from typing import Dict

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolHandoffValidator(ProtocolValidatorBase):
    """Validates checklist completeness, verification, sign-off, documentation, and support."""

    VALIDATOR_NAME = "protocol_handoff"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.DIMENSIONS = (
            ("checklist_completeness", 0.30, self._validate_checklist),
            ("verification_procedures", 0.25, self._validate_verification),
            ("stakeholder_signoff", 0.20, self._validate_signoff),
            ("documentation_requirements", 0.15, self._validate_documentation),
            ("transition_support", 0.10, self._validate_support),
        )

    def _get_handoff_section(self, content: str) -> str:
        return self._extract_section(content, "HANDOFF CHECKLIST")

    def _validate_checklist(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_handoff_section(content)
        checkboxes = re.findall(r"\[ \]|\[x\]", section, re.IGNORECASE)
        evidence: Dict[str, bool] = {
            "checklist_present": bool(section),
            "items_listed": len(checkboxes) >= 5,
            "descriptions": self._has_keywords(section, ["validate", "ensure", "confirm"]),
            "dependencies": self._has_keywords(section, ["before", "after", "next"]),
        }

        return self._build_dimension_result(
            "Checklist Completeness",
            evidence,
            evidence={"checkbox_count": len(checkboxes)},
        )

    def _validate_verification(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_handoff_section(content)
        evidence: Dict[str, bool] = {
            "verification_steps": self._has_keywords(section, ["verify", "validation", "confirm"]),
            "verification_scripts": self._has_keywords(section, ["script", "command", "run"]),
            "pass_fail": self._has_keywords(section, ["pass", "fail", "criteria"]),
            "evidence_requirements": self._has_keywords(section, ["evidence", "attach", "store"]),
        }

        return self._build_dimension_result(
            "Verification Procedures",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_signoff(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_handoff_section(content)
        evidence: Dict[str, bool] = {
            "stakeholder_list": self._has_keywords(section, ["stakeholder", "reviewer", "approver"]),
            "approval_process": self._has_keywords(section, ["sign-off", "approval", "authorize"]),
            "approval_evidence": self._has_keywords(section, ["record", "evidence", "signature"]),
            "approval_timing": self._has_keywords(section, ["before", "after", "when"]),
        }

        return self._build_dimension_result(
            "Stakeholder Sign-off",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_documentation(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_handoff_section(content)
        evidence: Dict[str, bool] = {
            "doc_list": self._has_keywords(section, ["documentation", "docs", "package", "deliverable"]),
            "doc_quality": self._has_keywords(section, ["complete", "final", "quality"]),
            "doc_location": self._has_keywords(section, ["stored", "location", "repository"]),
            "doc_updates": self._has_keywords(section, ["update", "latest", "current"]),
        }

        return self._build_dimension_result(
            "Documentation Requirements",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_support(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_handoff_section(content)
        evidence: Dict[str, bool] = {
            "knowledge_transfer": self._has_keywords(section, ["knowledge", "brief", "onboard"]),
            "support_period": self._has_keywords(section, ["support", "duration", "window"]),
            "contact_info": self._has_keywords(section, ["contact", "reach", "email"]),
            "escalation": self._has_keywords(section, ["escalate", "issue", "problem"]),
        }

        return self._build_dimension_result(
            "Transition Support",
            evidence,
            evidence={"checks": evidence},
        )


def main() -> None:
    run_validator_cli(ProtocolHandoffValidator)


if __name__ == "__main__":
    main()

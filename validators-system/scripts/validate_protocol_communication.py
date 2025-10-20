#!/usr/bin/env python3
"""Validator 6 - Communication Protocol validation."""

import re
from pathlib import Path
from typing import Dict

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolCommunicationValidator(ProtocolValidatorBase):
    """Validates communication announcements, interactions, errors, progress, and evidence callouts."""

    VALIDATOR_NAME = "protocol_communication"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.DIMENSIONS = (
            ("status_announcements", 0.25, self._validate_status_announcements),
            ("user_interaction", 0.25, self._validate_user_interaction),
            ("error_messaging", 0.20, self._validate_error_messaging),
            ("progress_tracking", 0.15, self._validate_progress_tracking),
            ("evidence_communication", 0.15, self._validate_evidence_communication),
        )

    def _get_communication_section(self, content: str) -> str:
        return self._extract_section(content, "COMMUNICATION PROTOCOLS")

    def _validate_status_announcements(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_communication_section(content)
        announcements = re.findall(r"\[(MASTER RAY™|PHASE|STATUS)[^\]]+\]", section)
        phase_markers = [item for item in announcements if "PHASE" in item.upper()]
        start_markers = [item for item in announcements if "START" in item.upper()]
        complete_markers = [item for item in announcements if "COMPLETE" in item.upper()]

        evidence: Dict[str, bool] = {
            "announcements_present": bool(announcements),
            "all_phases": len(phase_markers) >= 3,
            "start_events": bool(start_markers),
            "completion": bool(complete_markers),
        }

        return self._build_dimension_result(
            "Status Announcements",
            evidence,
            evidence={"announcements": announcements},
        )

    def _validate_user_interaction(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_communication_section(content)
        prompts = re.findall(r">\s*\"[^\"]+\"", section)
        evidence: Dict[str, bool] = {
            "confirmation": self._has_keywords(section, ["confirm", "approval", "acknowledge"]),
            "clarification": self._has_keywords(section, ["clarify", "specify", "provide"]),
            "decision_points": self._has_keywords(section, ["choose", "option", "select"]),
            "feedback_requests": self._has_keywords(section, ["feedback", "does this", "review"]),
        }

        return self._build_dimension_result(
            "User Interaction",
            evidence,
            evidence={"examples": prompts[:5]},
        )

    def _validate_error_messaging(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_communication_section(content)
        error_prompts = re.findall(r"\[RAY ERROR\][^\n]*", section)
        evidence: Dict[str, bool] = {
            "error_template": bool(error_prompts),
            "severity": self._has_keywords(section, ["critical", "warning", "alert"]),
            "context": self._has_keywords(section, ["issue", "encountered", "during"]),
            "resolution": self._has_keywords(section, ["resolve", "fix", "rerun", "remediate"]),
        }

        return self._build_dimension_result(
            "Error Messaging",
            evidence,
            evidence={"templates": error_prompts[:3]},
        )

    def _validate_progress_tracking(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_communication_section(content)
        percent_mentions = re.findall(r"\b\d{1,3}%\b", section)
        evidence: Dict[str, bool] = {
            "progress_indicators": bool(percent_mentions) or "progress" in section.lower(),
            "time_estimates": self._has_keywords(section, ["ETA", "minutes", "hours", "timeline"]),
            "current_activity": self._has_keywords(section, ["currently", "in progress", "working on"]),
            "next_steps": self._has_keywords(section, ["next", "upcoming", "then"]),
        }

        return self._build_dimension_result(
            "Progress Tracking",
            evidence,
            evidence={"percentages": percent_mentions},
        )

    def _validate_evidence_communication(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_communication_section(content)
        artifact_mentions = re.findall(r"\.artifacts/[^`\s]+", section)
        evidence: Dict[str, bool] = {
            "artifacts_listed": bool(artifact_mentions),
            "locations": bool(artifact_mentions),
            "format_described": self._has_keywords(section, ["json", "markdown", "report", "log"]),
            "status": self._has_keywords(section, ["pass", "ready", "available", "stored"]),
        }

        return self._build_dimension_result(
            "Evidence Communication",
            evidence,
            evidence={"artifacts": artifact_mentions[:10]},
        )


def main() -> None:
    run_validator_cli(ProtocolCommunicationValidator)


if __name__ == "__main__":
    main()

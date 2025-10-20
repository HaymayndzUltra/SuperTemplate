#!/usr/bin/env python3
"""Validator 6 - Communication Protocol"""
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


class CommunicationValidator(BaseProtocolValidator):
    slug = "communication"
    name = "Communication Protocol Validator"
    dimension_weights = {
        "status_announcements": 0.25,
        "user_interaction": 0.25,
        "error_messaging": 0.20,
        "progress_tracking": 0.15,
        "evidence_communication": 0.15,
    }
    pass_threshold = 0.9
    warning_threshold = 0.75

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        communication_text = collect_section_text(content, ["COMMUNICATION", "STATUS", "ANNOUNCEMENT", "INTERACTION"])
        workflow_text = collect_section_text(content, ["WORKFLOW"])
        evidence_text = collect_section_text(content, ["EVIDENCE", "SUMMARY"])
        combined_text = "\n".join(filter(None, [communication_text, workflow_text]))
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 6.1 - Status Announcements
        status_keywords = ["[MASTER RAY", "PHASE", "status", "announce", "broadcast"]
        status_lines = [line for line in combined_text.splitlines() if any(keyword.lower() in line.lower() for keyword in status_keywords)]
        status_findings = {
            "status_lines": status_lines[:10],
            "count": len(status_lines),
        }
        status_issues = []
        if not status_lines:
            status_issues.append("No status announcements documented.")
        if len(status_lines) >= 3:
            status_status = "pass"
        elif status_lines:
            status_status = "warning"
        else:
            status_status = "fail"
        status_score = normalize_score(status_status)
        dimensions["status_announcements"] = DimensionResult(
            status_status,
            status_score,
            status_findings,
            status_issues,
            [],
        )

        # Dimension 6.2 - User Interaction
        interaction_keywords = ["reply", "confirm", "ask", "request", "choose", "feedback"]
        interaction_lines = [line for line in communication_text.splitlines() if any(keyword in line.lower() for keyword in interaction_keywords)]
        interaction_findings = {
            "interaction_lines": interaction_lines[:10],
            "count": len(interaction_lines),
        }
        interaction_issues = []
        if not interaction_lines:
            interaction_issues.append("No user interaction prompts.")
        if len(interaction_lines) >= 3:
            interaction_status = "pass"
        elif interaction_lines:
            interaction_status = "warning"
        else:
            interaction_status = "fail"
        interaction_score = normalize_score(interaction_status)
        dimensions["user_interaction"] = DimensionResult(
            interaction_status,
            interaction_score,
            interaction_findings,
            interaction_issues,
            [],
        )

        # Dimension 6.3 - Error Messaging
        error_keywords = ["if", "error", "blocked", "halt", "issue", "problem"]
        error_lines = [line for line in communication_text.splitlines() if any(keyword in line.lower() for keyword in error_keywords) and ("stop" in line.lower() or "halt" in line.lower() or "error" in line.lower())]
        error_findings = {
            "error_lines": error_lines[:10],
            "count": len(error_lines),
        }
        error_issues = []
        if not error_lines:
            error_issues.append("No error messaging templates described.")
        if len(error_lines) >= 2:
            error_status = "pass"
        elif error_lines:
            error_status = "warning"
        else:
            error_status = "fail"
        error_score = normalize_score(error_status)
        dimensions["error_messaging"] = DimensionResult(
            error_status,
            error_score,
            error_findings,
            error_issues,
            [],
        )

        # Dimension 6.4 - Progress Tracking
        progress_keywords = ["progress", "%", "percent", "remaining", "current", "next"]
        progress_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in progress_keywords)]
        progress_findings = {
            "progress_lines": progress_lines[:10],
            "count": len(progress_lines),
        }
        progress_issues = []
        if not progress_lines:
            progress_issues.append("No progress tracking communication found.")
        if len(progress_lines) >= 2:
            progress_status = "pass"
        elif progress_lines:
            progress_status = "warning"
        else:
            progress_status = "fail"
        progress_score = normalize_score(progress_status)
        dimensions["progress_tracking"] = DimensionResult(
            progress_status,
            progress_score,
            progress_findings,
            progress_issues,
            [],
        )

        # Dimension 6.5 - Evidence Communication
        evidence_lines = [line for line in (communication_text + "\n" + evidence_text).splitlines() if ".artifacts" in line or "evidence" in line.lower() or "upload" in line.lower()]
        evidence_findings = {
            "evidence_lines": evidence_lines[:10],
            "count": len(evidence_lines),
        }
        evidence_issues = []
        if not evidence_lines:
            evidence_issues.append("No communication about evidence artifacts.")
        if len(evidence_lines) >= 2:
            evidence_status = "pass"
        elif evidence_lines:
            evidence_status = "warning"
        else:
            evidence_status = "fail"
        evidence_score = normalize_score(evidence_status)
        dimensions["evidence_communication"] = DimensionResult(
            evidence_status,
            evidence_score,
            evidence_findings,
            evidence_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate protocol communication guidance")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = CommunicationValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())

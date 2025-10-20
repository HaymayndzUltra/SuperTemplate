#!/usr/bin/env python3
"""Validator 3 - Workflow Algorithm validation."""

import re
from pathlib import Path
from typing import Dict

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolWorkflowValidator(ProtocolValidatorBase):
    """Validates workflow structure, steps, markers, halt conditions, and evidence."""

    VALIDATOR_NAME = "protocol_workflow"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.DIMENSIONS = (
            ("workflow_structure", 0.20, self._validate_structure),
            ("step_definitions", 0.25, self._validate_steps),
            ("action_markers", 0.15, self._validate_markers),
            ("halt_conditions", 0.20, self._validate_halt_conditions),
            ("evidence_tracking", 0.20, self._validate_evidence),
        )

    def _get_workflow_section(self, content: str) -> str:
        return self._extract_section(content, "WORKFLOW")

    def _validate_structure(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_workflow_section(content)
        subsections = self._extract_subsections(section)
        evidence: Dict[str, bool] = {
            "section_present": bool(section),
            "step_headings": any(title.lower().startswith("step") for title in subsections),
            "sequential_flow": bool(re.search(r"step\s+1", section.lower())),
            "completeness": len(subsections) >= 3,
        }

        return self._build_dimension_result(
            "Workflow Structure",
            evidence,
            evidence={"steps": list(subsections.keys())},
        )

    def _validate_steps(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_workflow_section(content)
        subsections = self._extract_subsections(section)
        has_numbered_actions = any(re.search(r"^\s*\d+\.\s+", body, re.MULTILINE) for body in subsections.values())
        has_action_descriptions = any(len(body.splitlines()) > 2 for body in subsections.values())
        has_outputs = any(self._has_keywords(body, ["evidence", "output", "artifact"]) for body in subsections.values())

        evidence: Dict[str, bool] = {
            "numbering": has_numbered_actions,
            "action_details": has_action_descriptions,
            "step_outputs": has_outputs,
            "substeps_present": len(subsections) > 0,
        }

        return self._build_dimension_result(
            "Step Definitions",
            evidence,
            evidence={"step_count": len(subsections)},
        )

    def _validate_markers(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_workflow_section(content)
        markers = self._count_markers(section)
        evidence: Dict[str, bool] = {
            "critical": markers["critical"] > 0,
            "must": markers["must"] > 0,
            "guideline": markers["guideline"] > 0,
            "optional": markers["optional"] > 0,
        }

        return self._build_dimension_result(
            "Action Markers",
            evidence,
            evidence={"markers": markers},
        )

    def _validate_halt_conditions(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_workflow_section(content)
        evidence: Dict[str, bool] = {
            "halt_keywords": self._has_keywords(section, ["halt", "stop", "pause", "await"]),
            "error_handling": self._has_keywords(section, ["if", "fails", "error", "issue"]),
            "validation_gates": self._has_keywords(section, ["validation", "gate", "threshold"]),
            "rollback": self._has_keywords(section, ["rollback", "redo", "re-run", "retry"]),
        }

        return self._build_dimension_result(
            "Halt Conditions",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_evidence(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_workflow_section(content)
        artifacts = re.findall(r"\.artifacts/[^`\s]+", section)
        evidence: Dict[str, bool] = {
            "artifact_references": bool(artifacts),
            "artifact_formats": self._has_keywords(section, ["json", "markdown", "yaml", "report"]),
            "storage_paths": bool(artifacts),
            "validation_notes": self._has_keywords(section, ["validate", "confirmation", "review", "approval"]),
        }

        return self._build_dimension_result(
            "Evidence Tracking",
            evidence,
            evidence={"artifacts": artifacts},
        )


def main() -> None:
    run_validator_cli(ProtocolWorkflowValidator)


if __name__ == "__main__":
    main()

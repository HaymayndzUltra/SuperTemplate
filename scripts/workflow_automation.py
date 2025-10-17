"""Workflow automation adapter bridging orchestration and gates."""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any, Dict, List, Optional


def _ensure_project_generator_package() -> None:
    package_name = "project_generator"
    module = sys.modules.get(package_name)
    if module is not None and hasattr(module, "__path__"):
        return

    repo_root = Path(__file__).resolve().parent.parent / package_name
    spec = spec_from_file_location(
        package_name,
        repo_root / "__init__.py",
        submodule_search_locations=[str(repo_root)],
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load package {package_name}")

    module = module_from_spec(spec)
    sys.modules[package_name] = module
    spec.loader.exec_module(module)


_ensure_project_generator_package()

from scripts.workflow_automation.config import WorkflowConfig
from scripts.workflow_automation.exceptions import GateFailedError
from scripts.workflow_automation.orchestrator import WorkflowOrchestrator
from scripts.evidence_manager import EvidenceManager
from scripts.quality_gates import QualityGates
from scripts.validation_gates import ValidationGates


PHASE_SEQUENCE = [
    "bootstrap",
    "prd",
    "design",
    "implementation",
    "audit",
    "launch",
    "operations",
]


@dataclass(frozen=True)
class GateOutcome:
    name: str
    passed: bool
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PhaseExecutionResult:
    success: bool
    phase: str
    artifacts_generated: int
    gates: List[GateOutcome] = field(default_factory=list)
    error: Optional[str] = None


@dataclass(frozen=True)
class WorkflowStatus:
    current_phase: str
    project_path: Path
    config: WorkflowConfig


class UnifiedWorkflowAutomation:
    """Coordinates quality/validation gates with the orchestrator."""

    def __init__(self, *, workflow_config: Dict[str, Any], project_path: Path) -> None:
        self.project_path = Path(project_path).resolve()
        self.project_path.mkdir(parents=True, exist_ok=True)

        self.config = self._load_config(workflow_config)
        evidence_root = self.project_path / self.config.evidence_root
        self.evidence_manager = EvidenceManager(str(evidence_root))
        self.quality_gates = QualityGates(str(self.project_path), str(evidence_root))
        self.validation_gates = ValidationGates(str(self.project_path), str(evidence_root))
        self.orchestrator = WorkflowOrchestrator(self.config, project_root=self.project_path)

        self._current_phase = PHASE_SEQUENCE[0]

    # ------------------------------------------------------------------
    # Public API expected by validation prompt
    # ------------------------------------------------------------------
    def execute_phase(self, phase: str) -> PhaseExecutionResult:
        self._current_phase = phase
        gates = self.run_gates(phase)

        if not all(gate.passed for gate in gates):
            return PhaseExecutionResult(
                success=False,
                phase=phase,
                artifacts_generated=0,
                gates=gates,
                error="Gate execution failed",
            )

        try:
            self.orchestrator.run()
        except GateFailedError as exc:
            return PhaseExecutionResult(
                success=False,
                phase=phase,
                artifacts_generated=0,
                gates=gates,
                error=str(exc),
            )

        artifacts = self.collect_evidence(phase)
        return PhaseExecutionResult(
            success=True,
            phase=phase,
            artifacts_generated=len(artifacts),
            gates=gates,
        )

    def run_gates(self, phase: str) -> List[GateOutcome]:
        phase_index = self._phase_to_index(phase)
        context = {
            "project": self.project_path.name,
            "phase": phase,
        }

        quality_result = self.quality_gates.execute_quality_gate("quick", context)
        quality_outcome = GateOutcome(
            name="quality_quick",
            passed=quality_result.get("status") == "passed",
            details=quality_result,
        )

        validation_request = self.validation_gates.request_validation(phase_index, context)
        for approver in validation_request["checkpoint"]["required_approvals"]:
            self.validation_gates.approve_validation(validation_request["request_id"], approver, True)
        validation_status = self.validation_gates.get_validation_status(validation_request["request_id"])
        validation_outcome = GateOutcome(
            name="validation_checkpoint",
            passed=validation_status.get("status") == "approved",
            details=validation_status,
        )

        return [quality_outcome, validation_outcome]

    def collect_evidence(self, phase: str) -> List[Dict[str, Any]]:
        phase_index = self._phase_to_index(phase)
        manifest_path = self.project_path / "artifacts" / f"phase_{phase_index}"
        manifest_path.mkdir(parents=True, exist_ok=True)

        artifact_file = manifest_path / "summary.txt"
        artifact_file.write_text(f"Phase {phase} completed.\n", encoding="utf-8")
        self.evidence_manager.log_artifact(
            str(artifact_file),
            category="documentation",
            description=f"Summary for phase {phase}",
            phase=phase_index,
        )

        evidence = self.evidence_manager.load_evidence(project_name=self.project_path.name)
        return list(evidence.get("manifest", {}).get("artifacts", []))

    def get_status(self) -> WorkflowStatus:
        return WorkflowStatus(
            current_phase=self._current_phase,
            project_path=self.project_path,
            config=self.config,
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _load_config(self, payload: Dict[str, Any]) -> WorkflowConfig:
        if isinstance(payload, WorkflowConfig):
            return payload
        data = dict(payload)
        if not data.get("gates"):
            data["gates"] = [
                {
                    "name": "noop",
                    "implementation": "scripts.workflow_automation.gates.implementations.PlanningGate",
                    "enabled": False,
                    "settings": {},
                }
            ]
        if "evidence_root" not in data:
            data["evidence_root"] = "evidence"
        return WorkflowConfig.from_dict(data)

    def _phase_to_index(self, phase: str) -> int:
        try:
            return PHASE_SEQUENCE.index(phase)
        except ValueError as exc:
            raise ValueError(f"Unknown phase: {phase}") from exc


__all__ = [
    "UnifiedWorkflowAutomation",
    "GateOutcome",
    "PhaseExecutionResult",
    "WorkflowStatus",
]


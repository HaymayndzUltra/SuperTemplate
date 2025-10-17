"""Wrappers that expose workflow1 scripts through the unified automation layer."""
from __future__ import annotations

import logging
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class ScriptExecutionResult:
    """Execution result returned by workflow1 script wrappers."""

    success: bool
    command: Tuple[str, ...]
    stdout: str
    stderr: str
    returncode: int
    duration_seconds: float
    working_directory: Path
    expected_outputs: Tuple[Path, ...]


class ScriptExecutionError(RuntimeError):
    """Raised when a workflow1 script exits with a non-zero status."""

    def __init__(self, wrapper: "Workflow1ScriptWrapper", result: ScriptExecutionResult) -> None:
        message = (
            f"Script '{wrapper.script_path}' failed with return code {result.returncode}.\n"
            f"Command: {' '.join(result.command)}\n"
            f"Stdout:\n{result.stdout}\n"
            f"Stderr:\n{result.stderr}"
        )
        super().__init__(message)
        self.wrapper = wrapper
        self.result = result


class Workflow1ScriptWrapper:
    """Reusable helper that runs a workflow1 script with rich diagnostics."""

    def __init__(
        self,
        *,
        script_relative_path: str,
        interpreter: str,
        description: str,
        repository_root: Optional[Path] = None,
    ) -> None:
        self.repository_root = Path(repository_root or Path(__file__).resolve().parents[3]).resolve()
        self.script_path = (self.repository_root / script_relative_path).resolve()
        self.description = description
        self.interpreter = interpreter

        if not self.script_path.exists():
            raise FileNotFoundError(f"Workflow1 script missing: {self.script_path}")
        if interpreter not in {"python", "bash"}:
            raise ValueError("interpreter must be 'python' or 'bash'")

    def _build_command(self, args: Sequence[str]) -> List[str]:
        command: List[str]
        if self.interpreter == "python":
            command = [sys.executable, str(self.script_path)]
        else:
            command = ["bash", str(self.script_path)]
        command.extend(args)
        return command

    def execute(
        self,
        *,
        args: Optional[Sequence[str]] = None,
        env: Optional[Mapping[str, str]] = None,
        expected_outputs: Optional[Iterable[Path]] = None,
        check: bool = True,
        timeout: Optional[float] = None,
    ) -> ScriptExecutionResult:
        """Execute the wrapped script with optional environment overrides."""

        command = self._build_command(list(args or []))
        merged_env: MutableMapping[str, str] = os.environ.copy()
        if env is not None:
            merged_env.update(env)

        LOGGER.info("Executing workflow1 script", extra={"command": command, "cwd": str(self.script_path.parent)})
        start = time.perf_counter()
        completed = subprocess.run(
            command,
            cwd=str(self.script_path.parent),
            env=merged_env,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )
        duration = time.perf_counter() - start

        script_dir = self.script_path.parent
        outputs: Tuple[Path, ...] = tuple(
            (path if path.is_absolute() else (script_dir / path)).resolve()
            for path in (expected_outputs or [])
        )

        result = ScriptExecutionResult(
            success=completed.returncode == 0,
            command=tuple(command),
            stdout=completed.stdout,
            stderr=completed.stderr,
            returncode=completed.returncode,
            duration_seconds=duration,
            working_directory=self.script_path.parent,
            expected_outputs=outputs,
        )

        log_payload = {
            "script": str(self.script_path),
            "command": command,
            "returncode": completed.returncode,
            "duration_seconds": duration,
        }
        if result.success:
            LOGGER.info("Workflow1 script completed", extra=log_payload)
        else:
            LOGGER.error("Workflow1 script failed", extra={**log_payload, "stderr": completed.stderr})
            if check:
                raise ScriptExecutionError(self, result)

        return result


class Phase2DesignWrappers:
    """Entry points for Phase 2 design automation."""

    def __init__(self, *, repository_root: Optional[Path] = None) -> None:
        self.repository_root = Path(repository_root or Path(__file__).resolve().parents[3]).resolve()
        base = "workflow1/codex-phase2-design/scripts"
        self._architecture = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/generate_architecture_pack.py",
            interpreter="python",
            description="Generate architecture evidence pack",
            repository_root=self.repository_root,
        )
        self._contracts = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/generate_contract_assets.py",
            interpreter="python",
            description="Generate contract-first evidence pack",
            repository_root=self.repository_root,
        )

    def generate_architecture_pack(self, project: str) -> ScriptExecutionResult:
        args = ["--project", project]
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase2-design"
            / "evidence"
            / "phase2"
            / "outputs"
            / project
            / "architecture",
        ]
        return self._architecture.execute(args=args, expected_outputs=outputs)

    def generate_contract_assets(self, project: str, service: str) -> ScriptExecutionResult:
        args = ["--project", project, "--service", service]
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase2-design"
            / "evidence"
            / "phase2"
            / "outputs"
            / project
            / "contracts",
        ]
        return self._contracts.execute(args=args, expected_outputs=outputs)


class Phase3QualityWrappers:
    """Entry points for Phase 3 quality rail automation."""

    def __init__(self, *, repository_root: Optional[Path] = None) -> None:
        self.repository_root = Path(repository_root or Path(__file__).resolve().parents[3]).resolve()
        base = "workflow1/codex-phase3-quality-rails/scripts"
        self._feature_flags = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/configure_feature_flags.py",
            interpreter="python",
            description="Configure feature flag manifest",
            repository_root=self.repository_root,
        )
        self._quality_gates = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/run_quality_gates.sh",
            interpreter="bash",
            description="Execute phase 3 quality gates",
            repository_root=self.repository_root,
        )

    def configure_feature_flags(self, project: str, flags: Optional[Sequence[str]] = None) -> ScriptExecutionResult:
        args = ["--project", project]
        for flag in flags or []:
            args.extend(["--flag", flag])
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase3-quality-rails"
            / "evidence"
            / "phase3"
            / "outputs"
            / project
            / "quality-rails"
            / "feature_flags.json",
        ]
        return self._feature_flags.execute(args=args, expected_outputs=outputs)

    def run_quality_gates(self, project: str, bootstrap: bool = False) -> ScriptExecutionResult:
        args = ["--project", project]
        if bootstrap:
            args.append("--bootstrap")
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase3-quality-rails"
            / "evidence"
            / "phase3"
            / "outputs"
            / project
            / "quality-rails",
        ]
        return self._quality_gates.execute(args=args, expected_outputs=outputs)


class Phase4IntegrationWrappers:
    """Entry points for Phase 4 integration automation."""

    def __init__(self, *, repository_root: Optional[Path] = None) -> None:
        self.repository_root = Path(repository_root or Path(__file__).resolve().parents[3]).resolve()
        base = "workflow1/codex-phase4-integration/scripts"
        self._observability = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/generate_observability_pack.py",
            interpreter="python",
            description="Generate observability evidence pack",
            repository_root=self.repository_root,
        )
        self._staging_smoke = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/run_staging_smoke.sh",
            interpreter="bash",
            description="Execute staging smoke suite",
            repository_root=self.repository_root,
        )

    def generate_observability_pack(self, project: str) -> ScriptExecutionResult:
        args = ["--project", project]
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase4-integration"
            / "evidence"
            / "phase4"
            / "outputs"
            / project
            / "observability",
        ]
        return self._observability.execute(args=args, expected_outputs=outputs)

    def run_staging_smoke(
        self,
        project: str,
        *,
        result: str = "pass",
        report: Optional[Path] = None,
    ) -> ScriptExecutionResult:
        args = ["--project", project, "--result", result]
        default_report = (
            self.repository_root
            / "workflow1"
            / "codex-phase4-integration"
            / "evidence"
            / "phase4"
            / "outputs"
            / project
            / "integration"
            / "staging_smoke_report.txt"
        )
        report_path = Path(report) if report is not None else default_report
        if report is not None:
            args.extend(["--report", str(report_path)])
        outputs = [report_path]
        return self._staging_smoke.execute(args=args, expected_outputs=outputs)


class Phase5LaunchWrappers:
    """Entry points for Phase 5 launch automation."""

    def __init__(self, *, repository_root: Optional[Path] = None) -> None:
        self.repository_root = Path(repository_root or Path(__file__).resolve().parents[3]).resolve()
        base = "workflow1/codex-phase5-launch/scripts"
        self._rollback = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/rehearse_rollback.sh",
            interpreter="bash",
            description="Rehearse production rollback",
            repository_root=self.repository_root,
        )
        self._dr_restore = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/verify_dr_restore.sh",
            interpreter="bash",
            description="Verify disaster recovery restore",
            repository_root=self.repository_root,
        )

    def rehearse_rollback(self, project: str) -> ScriptExecutionResult:
        args = ["--project", project]
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase5-launch"
            / "evidence"
            / "phase5"
            / "outputs"
            / project
            / "launch",
        ]
        return self._rollback.execute(args=args, expected_outputs=outputs)

    def verify_disaster_recovery(self, project: str) -> ScriptExecutionResult:
        args = ["--project", project]
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase5-launch"
            / "evidence"
            / "phase5"
            / "outputs"
            / project
            / "launch",
        ]
        return self._dr_restore.execute(args=args, expected_outputs=outputs)


class Phase6OperationsWrappers:
    """Entry points for Phase 6 operations automation."""

    def __init__(self, *, repository_root: Optional[Path] = None) -> None:
        self.repository_root = Path(repository_root or Path(__file__).resolve().parents[3]).resolve()
        base = "workflow1/codex-phase6-operations/scripts"
        self._monitor_slo = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/monitor_slo.py",
            interpreter="python",
            description="Record SLO metrics",
            repository_root=self.repository_root,
        )
        self._schedule_retros = Workflow1ScriptWrapper(
            script_relative_path=f"{base}/schedule_retros.py",
            interpreter="python",
            description="Schedule retrospectives",
            repository_root=self.repository_root,
        )

    def monitor_slo(
        self,
        project: str,
        *,
        availability: float = 99.9,
        latency: float = 280.0,
        error_rate: float = 0.8,
    ) -> ScriptExecutionResult:
        args = [
            "--project",
            project,
            "--availability",
            str(availability),
            "--latency",
            str(latency),
            "--error-rate",
            str(error_rate),
        ]
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase6-operations"
            / "evidence"
            / "phase6"
            / "outputs"
            / project
            / "operations"
            / "slo_status.json",
        ]
        return self._monitor_slo.execute(args=args, expected_outputs=outputs)

    def schedule_retros(
        self,
        project: str,
        *,
        start: Optional[str] = None,
        cadence: int = 14,
        count: int = 4,
    ) -> ScriptExecutionResult:
        args = ["--project", project, "--cadence", str(cadence), "--count", str(count)]
        if start is not None:
            args.extend(["--start", start])
        outputs = [
            self.repository_root
            / "workflow1"
            / "codex-phase6-operations"
            / "evidence"
            / "phase6"
            / "outputs"
            / project
            / "operations"
            / "retro_schedule.json",
        ]
        return self._schedule_retros.execute(args=args, expected_outputs=outputs)

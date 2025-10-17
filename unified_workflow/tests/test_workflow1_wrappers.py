"""Tests for workflow1 automation wrappers."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

import pytest

WRAPPERS_PATH = Path(__file__).resolve().parents[1] / "automation" / "workflow1" / "wrappers.py"
SPEC = importlib.util.spec_from_file_location("workflow1_wrappers", WRAPPERS_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load workflow1 wrappers module")
workflow1_wrappers = importlib.util.module_from_spec(SPEC)
sys.modules.setdefault("workflow1_wrappers", workflow1_wrappers)
SPEC.loader.exec_module(workflow1_wrappers)

Phase2DesignWrappers = workflow1_wrappers.Phase2DesignWrappers
Phase3QualityWrappers = workflow1_wrappers.Phase3QualityWrappers
Phase4IntegrationWrappers = workflow1_wrappers.Phase4IntegrationWrappers
Phase6OperationsWrappers = workflow1_wrappers.Phase6OperationsWrappers
ScriptExecutionError = workflow1_wrappers.ScriptExecutionError
Workflow1ScriptWrapper = workflow1_wrappers.Workflow1ScriptWrapper


@pytest.fixture(name="repository_root")
def fixture_repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def test_python_script_wrapper_executes_successfully(repository_root: Path) -> None:
    wrapper = Workflow1ScriptWrapper(
        script_relative_path="workflow1/codex-phase2-design/scripts/generate_architecture_pack.py",
        interpreter="python",
        description="test wrapper",
        repository_root=repository_root,
    )

    completed = SimpleNamespace(returncode=0, stdout="ok", stderr="")
    with mock.patch("subprocess.run", return_value=completed) as run_mock:
        result = wrapper.execute(args=["--project", "demo"])

    assert result.success is True
    assert result.command[0].endswith("python")
    assert "--project" in result.command
    assert run_mock.call_args.kwargs["cwd"] == str(wrapper.script_path.parent)


def test_script_wrapper_raises_on_failure(repository_root: Path) -> None:
    wrapper = Workflow1ScriptWrapper(
        script_relative_path="workflow1/codex-phase3-quality-rails/scripts/run_quality_gates.sh",
        interpreter="bash",
        description="quality gates",
        repository_root=repository_root,
    )

    completed = SimpleNamespace(returncode=1, stdout="", stderr="boom")
    with mock.patch("subprocess.run", return_value=completed):
        with pytest.raises(ScriptExecutionError):
            wrapper.execute(args=["--project", "demo"])


def test_quality_wrapper_passes_bootstrap_flag(repository_root: Path) -> None:
    wrappers = Phase3QualityWrappers(repository_root=repository_root)

    with mock.patch.object(wrappers._quality_gates, "execute", return_value="ok") as execute_mock:
        wrappers.run_quality_gates("demo", bootstrap=True)

    execute_args = execute_mock.call_args.kwargs["args"]
    assert "--bootstrap" in execute_args


def test_staging_smoke_wrapper_allows_custom_report(repository_root: Path) -> None:
    wrappers = Phase4IntegrationWrappers(repository_root=repository_root)
    custom_report = Path("reports/custom.txt")

    with mock.patch.object(wrappers._staging_smoke, "execute", return_value="ok") as execute_mock:
        wrappers.run_staging_smoke("demo", result="fail", report=custom_report)

    expected_args = execute_mock.call_args.kwargs["args"]
    assert expected_args[:4] == ["--project", "demo", "--result", "fail"]
    assert expected_args[-2:] == ["--report", str(custom_report)]


def test_schedule_retros_wrapper_supports_overrides(repository_root: Path) -> None:
    wrappers = Phase6OperationsWrappers(repository_root=repository_root)

    with mock.patch.object(wrappers._schedule_retros, "execute", return_value="ok") as execute_mock:
        wrappers.schedule_retros("demo", start="2024-10-01", cadence=10, count=2)

    args = execute_mock.call_args.kwargs["args"]
    assert ["--project", "demo"] == args[:2]
    assert "--start" in args
    assert "--cadence" in args
    assert "--count" in args


def test_design_contract_wrapper_passes_service(repository_root: Path) -> None:
    wrappers = Phase2DesignWrappers(repository_root=repository_root)

    with mock.patch.object(wrappers._contracts, "execute", return_value="ok") as execute_mock:
        wrappers.generate_contract_assets("demo", "payments")

    args = execute_mock.call_args.kwargs["args"]
    assert args == ["--project", "demo", "--service", "payments"]

"""Unit tests validating adapter module re-exports."""

from __future__ import annotations

from typing import List

import pytest


def _get_all_attribute_names(module: object) -> List[str]:
    """Return the module's public attribute list based on ``__all__``."""

    all_attr = getattr(module, "__all__", None)
    if all_attr is None:
        pytest.fail("Adapter module is missing an __all__ attribute")
    return list(all_attr)


def test_project_generator_adapter_exports() -> None:
    """Ensure project generator adapter exposes canonical classes."""

    from project_generator.core.brief_parser import BriefParser
    from project_generator.core.generator import ProjectGenerator
    from project_generator.core.industry_config import IndustryConfig
    from project_generator.core.validator import ProjectValidator
    from project_generator.templates.registry import TemplateRegistry
    from unified_workflow.automation.adapters import project_generator_adapter as adapter

    exported = _get_all_attribute_names(adapter)
    expected_names = [
        "ProjectGenerator",
        "ProjectValidator",
        "IndustryConfig",
        "BriefParser",
        "TemplateRegistry",
    ]

    assert len(exported) == len(expected_names)
    assert set(exported) == set(expected_names)
    assert adapter.ProjectGenerator is ProjectGenerator
    assert adapter.ProjectValidator is ProjectValidator
    assert adapter.IndustryConfig is IndustryConfig
    assert adapter.BriefParser is BriefParser
    assert adapter.TemplateRegistry is TemplateRegistry


def test_workflow_automation_adapter_exports() -> None:
    """Validate workflow automation adapter re-exports core orchestrator types."""

    from scripts.workflow_automation import WorkflowConfig, WorkflowOrchestrator
    from scripts.workflow_automation.exceptions import GateFailedError, WorkflowError
    from unified_workflow.automation.adapters import workflow_automation_adapter as adapter

    exported = _get_all_attribute_names(adapter)
    expected_names = [
        "WorkflowConfig",
        "WorkflowOrchestrator",
        "GateFailedError",
        "WorkflowError",
    ]

    assert len(exported) == len(expected_names)
    assert set(exported) == set(expected_names)
    assert adapter.WorkflowConfig is WorkflowConfig
    assert adapter.WorkflowOrchestrator is WorkflowOrchestrator
    assert adapter.GateFailedError is GateFailedError
    assert adapter.WorkflowError is WorkflowError


def test_lifecycle_tasks_adapter_exports() -> None:
    """Confirm lifecycle tasks adapter provides module and helper access."""

    from scripts import lifecycle_tasks
    from unified_workflow.automation.adapters import lifecycle_tasks_adapter as adapter

    exported = _get_all_attribute_names(adapter)
    expected_names = ["lifecycle_tasks", "build_plan"]

    assert len(exported) == len(expected_names)
    assert set(exported) == set(expected_names)
    assert adapter.lifecycle_tasks is lifecycle_tasks
    assert adapter.build_plan is lifecycle_tasks.build_plan

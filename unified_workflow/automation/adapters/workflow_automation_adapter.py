"""Adapter for workflow_automation imports.

This adapter ensures proper import resolution for workflow_automation
components (from scripts package) without requiring sys.path manipulation.
"""

from __future__ import annotations

# workflow_automation is under scripts/ package
from scripts.workflow_automation import WorkflowConfig, WorkflowOrchestrator
from scripts.workflow_automation.exceptions import GateFailedError, WorkflowError

__all__ = [
    'WorkflowConfig',
    'WorkflowOrchestrator',
    'GateFailedError',
    'WorkflowError',
]


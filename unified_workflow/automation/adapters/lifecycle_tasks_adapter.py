"""Adapter for lifecycle_tasks imports.

This adapter ensures proper import resolution for lifecycle_tasks
without requiring sys.path manipulation.
"""

from __future__ import annotations

# lifecycle_tasks is under scripts/ package
from scripts import lifecycle_tasks

# Re-export the build_plan function and other utilities
build_plan = lifecycle_tasks.build_plan

__all__ = ['lifecycle_tasks', 'build_plan']


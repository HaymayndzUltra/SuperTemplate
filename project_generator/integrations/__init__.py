"""Project generator integration package."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

from .ai_governor import AIGovernorIntegration
from .git import add_and_commit, get_current_branch, init_repository

__all__ = [
    "AIGovernorIntegration",
    "add_and_commit",
    "get_current_branch",
    "init_repository",
]


def describe_integrations(project_root: Path) -> Dict[str, Optional[str]]:
    """Provide a simple summary of supported integrations.

    Args:
        project_root: Root directory where integrations should operate.

    Returns:
        Dictionary describing the availability of integrations for diagnostics.
    """
    governor = AIGovernorIntegration(project_root).governor_root
    repository = project_root / ".git"

    return {
        "ai_governor_root": str(governor) if governor else None,
        "git_repository": str(repository) if repository.exists() else None,
    }

"""
Git integration utilities
"""

import subprocess
from pathlib import Path
from typing import Optional


def init_repository(path: Path) -> bool:
    """Initialize a git repository"""
    try:
        subprocess.run(['git', 'init'], cwd=path, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def add_and_commit(path: Path, message: str) -> bool:
    """Add all files and commit"""
    try:
        subprocess.run(['git', 'add', '.'], cwd=path, check=True, capture_output=True)
        subprocess.run(
            ['git', 'commit', '-m', message],
            cwd=path,
            check=True,
            capture_output=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_current_branch(path: Path) -> Optional[str]:
    """Get the current git branch"""
    try:
        result = subprocess.run(
            ['git', 'branch', '--show-current'],
            cwd=path,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None
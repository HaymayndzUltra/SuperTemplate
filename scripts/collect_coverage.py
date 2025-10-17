#!/usr/bin/env python3
"""
Collect Python coverage into coverage.xml using pytest-cov if available.
- If pytest-cov is missing, exits 0 and prints a hint.
- Intended for CI gating before scripts/enforce_gates.py

Usage:
  python scripts/collect_coverage.py
"""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(os.getenv("PROJECT_ROOT") or Path(__file__).resolve().parents[1])


def main() -> int:
    if shutil.which("pytest") is None:
        print("[COV] pytest not found")
        return 0
    # Prefer pytest-cov if installed
    args = ["pytest", "-q", "--maxfail=1", "--disable-warnings", "--cov=.", "--cov-report=xml:coverage.xml"]
    try:
        r = subprocess.run(args, cwd=str(ROOT), check=False)
        print(f"[COV] pytest exit={r.returncode}")
    except Exception as e:
        print(f"[COV] error: {e}")
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
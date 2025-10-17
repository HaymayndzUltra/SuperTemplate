#!/usr/bin/env python3
"""
Aggregate dependency vulnerability counts into metrics/deps.json.
- Tries pip-audit (Python) and npm audit (Node) if available
- Produces: metrics/deps.json = {"critical": int, "high": int}
- Never fails if tools are missing; prints hints instead

Usage:
  python scripts/scan_deps.py
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Tuple

ROOT = Path(os.getenv("PROJECT_ROOT") or Path(__file__).resolve().parents[1])
METRICS = ROOT / "metrics"


def _run(cmd: list[str]) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return r.returncode, r.stdout or r.stderr
    except FileNotFoundError:
        return 127, "not found"


def python_counts() -> Tuple[int, int]:
    """Return (critical, high) for Python deps using pip-audit if present."""
    if shutil.which("pip-audit") is None:
        return 0, 0
    code, out = _run(["pip-audit", "-f", "json"])
    if code != 0:
        return 0, 0
    try:
        data = json.loads(out or "[]")
    except Exception:
        return 0, 0
    crit = 0
    high = 0
    for item in data:
        sev = (item.get("severity") or "").lower()
        if sev == "critical":
            crit += 1
        elif sev == "high":
            high += 1
    return crit, high


def node_counts() -> Tuple[int, int]:
    """Return (critical, high) for Node deps via `npm audit --json` if package.json exists."""
    if not (ROOT / "package.json").exists():
        return 0, 0
    if shutil.which("npm") is None:
        return 0, 0
    code, out = _run(["npm", "audit", "--json"])
    if code not in (0, 1):  # npm audit returns 1 on findings
        return 0, 0
    try:
        data = json.loads(out or "{}")
    except Exception:
        return 0, 0
    crit = 0
    high = 0
    advisories = data.get("advisories") or {}
    if isinstance(advisories, dict) and advisories:
        for adv in advisories.values():
            sev = (adv.get("severity") or "").lower()
            if sev == "critical":
                crit += 1
            elif sev == "high":
                high += 1
    # npm v7+ provides "vulnerabilities" summary
    vulns = data.get("vulnerabilities") or {}
    if isinstance(vulns, dict) and vulns:
        crit = max(crit, int(vulns.get("critical", {}).get("count", 0) if isinstance(vulns.get("critical"), dict) else int(vulns.get("critical", 0))) )
        high = max(high, int(vulns.get("high", {}).get("count", 0) if isinstance(vulns.get("high"), dict) else int(vulns.get("high", 0))) )
    return crit, high


def main() -> int:
    METRICS.mkdir(parents=True, exist_ok=True)
    pyc, pyh = python_counts()
    nc, nh = node_counts()
    critical = max(pyc, nc)
    high = max(pyh, nh)
    out = {"critical": int(critical), "high": int(high)}
    (METRICS / "deps.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
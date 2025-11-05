#!/usr/bin/env python3
"""Prerequisite validation for Protocol 18 Performance Optimization & Tuning."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/performance")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/monitoring"),
    Path(".artifacts/deployment"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_18_baseline.py",
    "scripts/validate_gate_18_diagnostics.py",
    "scripts/validate_gate_18_optimization.py",
    "scripts/validate_gate_18_governance.py",
    "scripts/aggregate_evidence_18.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/performance/performance-intake-report.json": json.dumps(
        {"metrics": [], "alerts": [], "impact": "pending"}, indent=2
    )
    + "\n",
    ".artifacts/performance/baseline-metrics.csv": (
        "service,metric,value,timestamp\n"
    ),
    ".artifacts/performance/hypothesis-log.md": (
        "# Performance Hypotheses\n\n## Hypothesis 1\n- Observation: \n- Root cause: \n- Validation plan: \n"
    ),
    ".artifacts/performance/profiling-report.md": (
        "# Profiling Report\n\n## Critical Transactions\n\nProfiling data pending.\n"
    ),
    ".artifacts/performance/load-test-results.json": json.dumps(
        {"scenarios": [], "throughput": 0, "latency": {}}, indent=2
    )
    + "\n",
    ".artifacts/performance/capacity-analysis.md": (
        "# Capacity Analysis\n\n## Current Utilization\n\nAnalysis pending.\n"
    ),
}


def _ensure_file(path: Path, payload: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(payload, encoding="utf-8")
        return "created"
    return "exists"


def _check_scripts(scripts: List[str]) -> List[str]:
    missing: List[str] = []
    for script in scripts:
        if not Path(script).exists():
            missing.append(script)
    return missing


def main() -> int:
    artifacts: List[Dict[str, str]] = []

    for directory in RELATED_DIRECTORIES:
        directory.mkdir(parents=True, exist_ok=True)

    for path, payload in ARTIFACT_TEMPLATES.items():
        status = _ensure_file(Path(path), payload)
        artifacts.append({"artifact": path, "status": status})

    missing_scripts = _check_scripts(RELATED_SCRIPTS)
    report = {
        "protocol": "18",
        "protocol_name": "Performance Optimization & Tuning",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "workspace": str(WORKSPACE_ROOT),
        "artifacts": artifacts,
        "missing_scripts": missing_scripts,
        "status": "pass" if not missing_scripts else "warning",
    }

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

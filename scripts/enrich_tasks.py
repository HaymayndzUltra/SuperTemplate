#!/usr/bin/env python3
"""
Enrich tasks.json with personas and acceptance criteria.
- Idempotent: does not duplicate existing acceptance items
- Portable: works with list or dict-of-lists structures

Usage:
  python scripts/enrich_tasks.py --input tasks.json [--output tasks.json]
  # If --output omitted, updates input in-place.

Exit codes:
  0 success, 2 on invalid/missing input
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

PERSONA_BY_AREA: Dict[str, str] = {
    "backend": "code-architect",
    "frontend": "system-integrator",
    "devops": "system-integrator",
    "qa": "qa",
    "db": "code-architect",
    "docs": "system-integrator",
}

ACCEPTANCE_TEMPLATES: Dict[str, List[str]] = {
    "backend": [
        "unit/integration tests added or updated",
        "OpenAPI/endpoint docs updated",
        "lint passes",
    ],
    "frontend": [
        "renders without console errors",
        "unit/E2E tests added",
        "a11y/lint passes",
    ],
    "devops": [
        "configuration validated locally",
        "no secrets checked-in",
        "CI workflow runs locally",
    ],
    "qa": [
        "test plan documented",
        "smoke tests pass",
    ],
    "db": [
        "migration created and applied",
        "rollback validated",
        "query p95 under budget (seed data)",
    ],
    "docs": [
        "README updated",
        "examples added",
    ],
}


def _dedup_preserve(seq: List[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for s in seq:
        key = s.strip().lower()
        if not key:
            continue
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
    return out


def _coerce_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def _enrich_task(task: Dict[str, Any]) -> Tuple[bool, bool, Dict[str, Any]]:
    """Return (persona_changed, acceptance_changed, task)."""
    area = (task.get("area") or "").strip().lower()
    persona_before = task.get("persona")

    # Persona enrichment
    if not persona_before:
        task["persona"] = PERSONA_BY_AREA.get(area, "system-integrator")
        persona_changed = True
    else:
        persona_changed = False

    # Acceptance enrichment
    acceptance_before = _coerce_list(task.get("acceptance"))
    template = ACCEPTANCE_TEMPLATES.get(area) or []
    acceptance_after = _dedup_preserve(acceptance_before + template)
    if acceptance_after != acceptance_before:
        task["acceptance"] = acceptance_after
        acceptance_changed = True
    else:
        acceptance_changed = False

    # Ensure blocked_by and state fields exist
    if "blocked_by" not in task:
        task["blocked_by"] = []
    if not task.get("state"):
        task["state"] = "pending"

    return persona_changed, acceptance_changed, task


def _iter_tasks(root: Any) -> List[Dict[str, Any]]:
    tasks: List[Dict[str, Any]] = []
    if isinstance(root, list):
        tasks = [t for t in root if isinstance(t, dict)]
    elif isinstance(root, dict):
        for _, v in root.items():
            if isinstance(v, list):
                tasks.extend(t for t in v if isinstance(t, dict))
    return tasks


def main() -> int:
    p = argparse.ArgumentParser(description="Enrich tasks with personas and acceptance")
    p.add_argument("--input", default="tasks.json")
    p.add_argument("--output", default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"[ERR] input not found: {in_path}")
        return 2

    try:
        data = json.loads(in_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERR] failed to parse JSON: {e}")
        return 2

    persona_changes = 0
    acceptance_changes = 0

    # Enrich in-place for any recognized task objects
    if isinstance(data, list):
        for i, item in enumerate(data):
            if not isinstance(item, dict):
                continue
            pc, ac, enriched = _enrich_task(item)
            data[i] = enriched
            persona_changes += int(pc)
            acceptance_changes += int(ac)
    elif isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, list):
                for i, item in enumerate(v):
                    if not isinstance(item, dict):
                        continue
                    pc, ac, enriched = _enrich_task(item)
                    v[i] = enriched
                    persona_changes += int(pc)
                    acceptance_changes += int(ac)
    else:
        print("[ERR] tasks.json must be a list or a dict of lists")
        return 2

    print(f"[OK] personas set: {persona_changes}, acceptance updated: {acceptance_changes}")

    if args.dry_run:
        return 0

    out_path = Path(args.output) if args.output else in_path
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"[OK] wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
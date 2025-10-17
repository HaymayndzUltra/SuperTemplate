#!/usr/bin/env python3
"""
Validate tasks.json DAG and references.
- Supports list of tasks or dict-of-lists keyed by lane
- Checks:
  * unique task ids
  * blocked_by reference existence
  * cycle detection via Kahn topo sort
  * enum validation for state/persona

Usage:
  python scripts/validate_tasks.py --input tasks.json
Exit codes:
  0 success; 2 validation error or bad input
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

ALLOWED_STATES: Set[str] = {"pending", "in_progress", "blocked", "completed", "cancelled"}
ALLOWED_PERSONAS: Set[str] = {"system-integrator", "code-architect", "qa"}


def _collect_tasks(root: Any) -> List[Dict[str, Any]]:
    tasks: List[Dict[str, Any]] = []
    if isinstance(root, list):
        tasks = [t for t in root if isinstance(t, dict)]
    elif isinstance(root, dict):
        for _, v in root.items():
            if isinstance(v, list):
                tasks.extend(t for t in v if isinstance(t, dict))
    return tasks


def _as_list(v: Any) -> List[str]:
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x) for x in v]
    return [str(v)]


def validate(tasks: List[Dict[str, Any]]) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    # Check ids
    ids: List[str] = []
    for t in tasks:
        tid = str(t.get("id") or "").strip()
        if not tid:
            errors.append("task missing id")
        ids.append(tid)
    # Uniqueness
    seen: Set[str] = set()
    dups: Set[str] = set()
    for tid in ids:
        if not tid:
            continue
        if tid in seen:
            dups.add(tid)
        seen.add(tid)
    if dups:
        errors.append(f"duplicate task ids: {sorted(dups)}")

    id_set: Set[str] = set(i for i in ids if i)

    # blocked_by references
    for t in tasks:
        tid = t.get("id")
        for dep in _as_list(t.get("blocked_by")):
            if dep and dep not in id_set:
                errors.append(f"{tid}: blocked_by references unknown id '{dep}'")

    # Enum checks
    for t in tasks:
        tid = t.get("id")
        st = t.get("state")
        persona = t.get("persona")
        if st is not None and str(st) not in ALLOWED_STATES:
            errors.append(f"{tid}: invalid state '{st}' (allowed: {sorted(ALLOWED_STATES)})")
        if persona is not None and str(persona) not in ALLOWED_PERSONAS:
            errors.append(f"{tid}: invalid persona '{persona}' (allowed: {sorted(ALLOWED_PERSONAS)})")

    # Build graph edges dep -> tid (dep must precede tid)
    from collections import defaultdict, deque

    indegree: Dict[str, int] = {tid: 0 for tid in id_set}
    adj: Dict[str, List[str]] = defaultdict(list)

    for t in tasks:
        tid = t.get("id")
        deps = _as_list(t.get("blocked_by"))
        for dep in deps:
            if dep and dep in id_set and tid in id_set:
                adj[dep].append(tid)
                indegree[tid] += 1

    # Kahn topo
    q = deque([n for n, d in indegree.items() if d == 0])
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        for v in adj.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if visited != len(id_set):
        errors.append("cycle detected in tasks graph (topological sort incomplete)")

    ok = len(errors) == 0
    return ok, errors


def main() -> int:
    p = argparse.ArgumentParser(description="Validate tasks DAG and references")
    p.add_argument("--input", default="tasks.json")
    args = p.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"[ERR] input not found: {in_path}")
        return 2

    try:
        root = json.loads(in_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERR] failed to parse JSON: {e}")
        return 2

    tasks = _collect_tasks(root)
    if not tasks:
        print("[ERR] no tasks found in input (expect list or dict-of-lists)")
        return 2

    ok, errors = validate(tasks)
    if ok:
        print("[OK] tasks DAG valid; ids unique; references resolved; enums valid")
        return 0

    print("[FAIL] tasks validation errors:")
    for e in errors:
        print(f" - {e}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""
Update a task's state by id in tasks.json with validation and log note.

Usage:
  python scripts/update_task_state.py --id FE-DSN --state completed [--note "done"] [--input tasks.json] [--output tasks.json]

Exit codes:
  0 success; 2 invalid input; 3 not found or no-op
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

ALLOWED_STATES = {"pending", "in_progress", "blocked", "completed", "cancelled"}


def _collect(root: Any) -> Tuple[List[Dict[str, Any]], bool]:
    if isinstance(root, list):
        return [t for t in root if isinstance(t, dict)], False
    tasks: List[Dict[str, Any]] = []
    if isinstance(root, dict):
        for _, v in root.items():
            if isinstance(v, list):
                tasks.extend(t for t in v if isinstance(t, dict))
        return tasks, True
    return [], False


def _apply(root: Any, target_id: str, new_state: str, note: str | None) -> Tuple[bool, Any]:
    changed = False
    if isinstance(root, list):
        for t in root:
            if isinstance(t, dict) and str(t.get("id")) == target_id:
                if t.get("state") == new_state:
                    return False, root
                t["state"] = new_state
                if note:
                    history = t.get("history") or []
                    if isinstance(history, list):
                        history.append({"event": "state_change", "to": new_state, "note": note})
                        t["history"] = history
                changed = True
                break
        return changed, root
    if isinstance(root, dict):
        for k, v in root.items():
            if isinstance(v, list):
                for t in v:
                    if isinstance(t, dict) and str(t.get("id")) == target_id:
                        if t.get("state") == new_state:
                            return False, root
                        t["state"] = new_state
                        if note:
                            history = t.get("history") or []
                            if isinstance(history, list):
                                history.append({"event": "state_change", "to": new_state, "note": note})
                                t["history"] = history
                        changed = True
                        break
        return changed, root
    return False, root


def main() -> int:
    p = argparse.ArgumentParser(description="Update a task state by id")
    p.add_argument("--id", required=True)
    p.add_argument("--state", required=True)
    p.add_argument("--note", default=None)
    p.add_argument("--input", default="tasks.json")
    p.add_argument("--output", default=None)
    args = p.parse_args()

    if args.state not in ALLOWED_STATES:
        print(f"[ERR] invalid state: {args.state} (allowed: {sorted(ALLOWED_STATES)})")
        return 2

    path = Path(args.input)
    if not path.exists():
        print(f"[ERR] input not found: {path}")
        return 2

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERR] failed to parse JSON: {e}")
        return 2

    changed, new_root = _apply(data, args.id, args.state, args.note)
    if not changed:
        print(f"[NOOP] task not found or already in state: {args.id}")
        return 3

    out_path = Path(args.output) if args.output else path
    out_path.write_text(json.dumps(new_root, indent=2), encoding="utf-8")
    print(f"[OK] updated {args.id} -> {args.state}; wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

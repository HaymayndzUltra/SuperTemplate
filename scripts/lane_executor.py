#!/usr/bin/env python3
"""
Lane executor: iterate tasks by lane respecting dependencies and concurrency cap.
- Reads tasks.json (list or dict-of-lists)
- Picks unblocked tasks up to --cap per lane
- Prints execution order suggestion; DOES NOT run commands
- Persists suggestion to .cursor/ai-governor/run-history/plan-<ts>.json
- Records git commit if repo present

Usage:
  python scripts/lane_executor.py --lane backend --cap 3 --input tasks.json
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
HIST = ROOT / ".cursor" / "ai-governor" / "run-history"


def _collect(root: Any) -> List[Dict[str, Any]]:
    if isinstance(root, list):
        return [t for t in root if isinstance(t, dict)]
    tasks: List[Dict[str, Any]] = []
    if isinstance(root, dict):
        for _, v in root.items():
            if isinstance(v, list):
                for t in v:
                    if isinstance(t, dict):
                        tasks.append(t)
    return tasks


def _filter_lane(tasks: List[Dict[str, Any]], lane: str) -> List[Dict[str, Any]]:
    if not lane:
        return tasks
    return [t for t in tasks if (t.get("area") or "").lower().startswith(lane.lower())]


def _ready(tasks: List[Dict[str, Any]], completed_ids: Set[str]) -> List[Dict[str, Any]]:
    r: List[Dict[str, Any]] = []
    for t in tasks:
        if (t.get("state") or "pending") == "completed":
            continue
        deps = [str(d) for d in (t.get("blocked_by") or [])]
        if all(d in completed_ids for d in deps):
            r.append(t)
    return r


def _git_commit() -> str:
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout.strip()
    except Exception:
        pass
    return ""


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", default="", help="lane filter: backend|frontend|devops|db|qa|docs")
    ap.add_argument("--cap", type=int, default=3)
    ap.add_argument("--input", default="tasks.json")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    tasks = _collect(data)
    lane_tasks = _filter_lane(tasks, args.lane)

    completed_ids: Set[str] = {str(t.get("id")) for t in lane_tasks if (t.get("state") or "pending") == "completed"}

    order: List[Dict[str, Any]] = []
    remaining = [t for t in lane_tasks if str(t.get("id")) not in completed_ids]

    # Simple topological suggestion with cap
    while remaining:
        ready = _ready(remaining, completed_ids)
        if not ready:
            break  # blocked; caller should inspect
        batch = ready[: max(1, min(args.cap, len(ready)))]
        for t in batch:
            order.append(t)
            completed_ids.add(str(t.get("id")))
        remaining = [t for t in remaining if str(t.get("id")) not in completed_ids]

    suggestion = {
        "lane": args.lane or "all",
        "cap": args.cap,
        "commit": _git_commit(),
        "suggested_order": [t.get("id") for t in order],
        "blocked": [t.get("id") for t in remaining],
    }

    HIST.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    out = HIST / f"plan-{args.lane or 'all'}-{ts}.json"
    out.write_text(json.dumps(suggestion, indent=2), encoding="utf-8")
    print(json.dumps(suggestion, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""
Scan scaffold to propose task updates (add/complete) and optionally apply.
- Detects: Next.js pages (app/*, pages/*), FastAPI routers (APIRouter path ops), DB migrations, tests
- Respects excludes via CLI

Usage:
  python scripts/sync_from_scaffold.py --input tasks.json --output tasks.json \
    --exclude "node_modules, .git, .venv" [--apply]

Behavior:
  - Without --apply: prints a diff plan (add/complete) and exits 0
  - With --apply: updates tasks.json accordingly
Exit codes: 0 success; 2 invalid input
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

NEXT_HINT_DIRS = ["app", "pages"]
FASTAPI_HINTS = ["APIRouter(", "@router."]
MIGRATION_DIRS = ["migrations", "alembic", "alembic/versions"]
TEST_HINT_DIRS = ["tests", "__tests__"]

ADD_PREFIX = "ADD"
COMPLETE_PREFIX = "COMPLETE"


def _walk_files(root: Path, excludes: Set[str]) -> List[Path]:
    files: List[Path] = []
    for base, dirs, fnames in os.walk(root):
        # prune excludes
        dirs[:] = [d for d in dirs if os.path.join(base, d).find(".git") == -1]
        skip = False
        for ex in excludes:
            if ex and ex in base:
                skip = True
                break
        if skip:
            continue
        for f in fnames:
            files.append(Path(base) / f)
    return files


def _collect_tasks(root: Any) -> Tuple[List[Dict[str, Any]], bool]:
    if isinstance(root, list):
        return [t for t in root if isinstance(t, dict)], False
    tasks: List[Dict[str, Any]] = []
    if isinstance(root, dict):
        for _, v in root.items():
            if isinstance(v, list):
                tasks.extend(t for t in v if isinstance(t, dict))
        return tasks, True
    return [], False


def _index_by_id(tasks: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    idx: Dict[str, Dict[str, Any]] = {}
    for t in tasks:
        tid = str(t.get("id") or "").strip()
        if tid:
            idx[tid] = t
    return idx


def _detect(frontend_paths: List[Path], backend_paths: List[Path], migration_paths: List[Path], test_paths: List[Path]) -> Dict[str, Dict[str, Any]]:
    proposals: Dict[str, Dict[str, Any]] = {}

    # FE pages → ensure FE tasks exist
    for p in frontend_paths:
        rel = str(p)
        # Use simple id from filename
        name = Path(rel).stem.replace("_", "-").upper()
        tid = f"FE-{name}"[:20]
        proposals[tid] = {
            "id": tid,
            "title": f"FE: implement page {rel}",
            "area": "frontend",
            "blocked_by": [],
        }

    # BE fastapi routers → ensure BE tasks exist
    for p in backend_paths:
        rel = str(p)
        name = Path(rel).stem.replace("_", "-").upper()
        tid = f"BE-{name}"[:20]
        proposals[tid] = {
            "id": tid,
            "title": f"BE: implement endpoint(s) in {rel}",
            "area": "backend",
            "blocked_by": [],
        }

    # DB migrations → ensure schema tasks exist
    for p in migration_paths:
        rel = str(p)
        name = Path(rel).stem.replace("_", "-").upper()
        tid = f"DB-{name}"[:20]
        proposals[tid] = {
            "id": tid,
            "title": f"DB: migration present {rel}",
            "area": "db",
            "blocked_by": [],
        }

    # Tests → ensure QA tasks exist
    for p in test_paths:
        rel = str(p)
        name = Path(rel).stem.replace("_", "-").upper()
        tid = f"QA-{name}"[:20]
        proposals[tid] = {
            "id": tid,
            "title": f"QA: tests present {rel}",
            "area": "qa",
            "blocked_by": [],
        }

    return proposals


def _matches_fastapi(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False
    return any(h in text for h in FASTAPI_HINTS)


def main() -> int:
    ap = argparse.ArgumentParser(description="Sync tasks from scaffold (propose or apply)")
    ap.add_argument("--input", default="tasks.json")
    ap.add_argument("--output", default=None)
    ap.add_argument("--root", default=".")
    ap.add_argument("--exclude", default="node_modules,.git,.venv")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"[ERR] input not found: {in_path}")
        return 2

    try:
        tasks_root = json.loads(in_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERR] failed to parse JSON: {e}")
        return 2

    tasks, is_dict = _collect_tasks(tasks_root)
    idx = _index_by_id(tasks)

    excludes = {e.strip() for e in args.exclude.split(',') if e.strip()}
    files = _walk_files(Path(args.root), excludes)

    # Collect hints
    fe_files: List[Path] = [p for p in files if any(f"/{d}/" in str(p) for d in NEXT_HINT_DIRS)]
    be_files: List[Path] = [p for p in files if p.suffix in (".py",) and _matches_fastapi(p)]
    db_files: List[Path] = [p for p in files if any(f"/{d}/" in str(p) for d in MIGRATION_DIRS)]
    qa_files: List[Path] = [p for p in files if any(f"/{d}/" in str(p) for d in TEST_HINT_DIRS)]

    proposals = _detect(fe_files, be_files, db_files, qa_files)

    add_list: List[Dict[str, Any]] = []
    complete_list: List[str] = []

    # Simple completion heuristic: if a proposed task id already exists and has state pending/in_progress, do not auto-complete.
    for tid, t in proposals.items():
        if tid not in idx:
            add_list.append(t)
        else:
            # if tests present for BE/FE ids, allow completion toggle by heuristic (very conservative: off by default)
            pass

    print("[DIFF] Proposals:")
    if not add_list:
        print(" - no additions")
    for t in add_list:
        print(f" - {ADD_PREFIX}: {t['id']} :: {t['title']} [{t['area']}]")
    if not complete_list:
        print(" - no completes")
    for tid in complete_list:
        print(f" - {COMPLETE_PREFIX}: {tid}")

    if not args.apply:
        return 0

    # Apply additions into tasks_root at top-level list or to a default lane
    if isinstance(tasks_root, list):
        tasks_root.extend(add_list)
    elif isinstance(tasks_root, dict):
        # choose lane by area; default bucket 'backend' exists or create 'misc'
        lanes = tasks_root
        for t in add_list:
            lane = t.get("area") or "misc"
            bucket = lanes.get(lane) or []
            bucket.append(t)
            lanes[lane] = bucket
    else:
        print("[ERR] tasks.json must be a list or dict-of-lists to apply changes")
        return 2

    out_path = Path(args.output) if args.output else in_path
    out_path.write_text(json.dumps(tasks_root, indent=2), encoding="utf-8")
    print(f"[OK] applied: +{len(add_list)}, ✓{len(complete_list)}; wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
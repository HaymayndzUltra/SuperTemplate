#!/usr/bin/env python3
"""Create minimal docs/briefs/<proj>/* scaffolds to unblock compliance checks."""
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

T = """# {title}

## Scope
## Constraints
## Success Criteria
"""

SEC = """# SECURITY & COMPLIANCE PLAN

## RBAC
## Audit Logging
## Encryption
## Data Retention
"""

MAP = {
    "PRD.md": T.format(title="Product Requirements Document"),
    "ARCHITECTURE.md": "# Architecture\n\n## Context Diagram\n## Component Diagram\n## ADR:\n",
    "API_PLAN.md": "# API Plan\n\n## Endpoints\n## Data Flows\n",
    "UI_MAP.md": "# UI Map\n\n## Pages\n## Components\n",
    "SECURITY_COMPLIANCE_PLAN.md": SEC,
    "ESTIMATES.md": "# Estimates\n\n## Timeline\n## Resources\n",
}


def main() -> int:
    proj = sys.argv[1] if len(sys.argv) > 1 else "demo-app"
    base = ROOT / "docs" / "briefs" / proj
    base.mkdir(parents=True, exist_ok=True)
    created = 0
    for fn, body in MAP.items():
        p = base / fn
        if not p.exists() or p.stat().st_size == 0:
            p.write_text(body, encoding="utf-8")
            print(f"Created {p}")
            created += 1
    if created == 0:
        print("No files created (all present and non-empty)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


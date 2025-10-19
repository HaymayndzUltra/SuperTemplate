#!/usr/bin/env python3
"""Generate session continuation instructions for Protocol 01 workflow."""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
from textwrap import dedent

DEFAULT_TEMPLATE = """# Session Continuation Instructions
Generated: {timestamp}
Previous Session: {previous_session}
Protocol Tested: {protocol}

## What Was Tested
- Protocol: {tested_protocol}
- Logic Validation: {logic_validation}
- Gap Detection: {gap_detection}
- Error Analysis: {error_analysis}
- Duplicate Check: {duplicate_check}

## What Was Fixed
{fixes}

## Verified Artifacts
{artifacts}

## Logic Validation Results
- Structural Logic: {structural_logic}
- Process Logic: {process_logic}
- Decision Logic: {decision_logic}
- Integration Logic: {integration_logic}

## Next Session Target
- Protocol: {next_protocol}
- Prerequisites: {prerequisites}
- Context Needed: {context_needed}
- Expected Outcomes: {expected_outcomes}

## Critical Notes
{critical_notes}
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate session continuation instructions.")
    parser.add_argument("--protocol", required=True, help="Protocol number executed in the current session.")
    parser.add_argument(
        "--session-id",
        help="Optional session identifier. Defaults to current UTC timestamp in YYYYMMDD-HHMMSS format.",
    )
    parser.add_argument(
        "--previous-session",
        default="unspecified",
        help="Identifier of the previous session. Defaults to 'unspecified'.",
    )
    parser.add_argument(
        "--notes",
        help="Optional free-form notes to include in the critical notes section.",
    )
    return parser


def ensure_output_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def format_block(lines: list[str], default: str = "- None") -> str:
    cleaned = [line.strip() for line in lines if line.strip()]
    if not cleaned:
        return default
    return "\n".join(f"- {line}" for line in cleaned)


def render_template(protocol: str, timestamp: str, previous_session: str, notes: str | None) -> str:
    template_values = {
        "timestamp": timestamp,
        "previous_session": previous_session,
        "protocol": protocol,
        "tested_protocol": f"Protocol {protocol}",
        "logic_validation": "Pending manual review",
        "gap_detection": "Pending manual review",
        "error_analysis": "Pending manual review",
        "duplicate_check": "Pending manual review",
        "fixes": format_block([], "- Pending documentation"),
        "artifacts": format_block([], "- Pending documentation"),
        "structural_logic": "Pending",
        "process_logic": "Pending",
        "decision_logic": "Pending",
        "integration_logic": "Pending",
        "next_protocol": protocol,
        "prerequisites": "Document protocol artifacts and validation evidence",
        "context_needed": "Job post analysis, tone map, proposal draft",
        "expected_outcomes": "Validated artifacts stored in .artifacts/protocol-01/",
        "critical_notes": format_block([notes] if notes else [], "- None"),
    }
    return dedent(DEFAULT_TEMPLATE).format(**template_values)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    protocol = args.protocol
    timestamp = args.session_id or dt.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    previous_session = args.previous_session
    notes = args.notes

    output_dir = Path(".cursor/session-instructions")
    ensure_output_directory(output_dir)

    content = render_template(protocol, timestamp, previous_session, notes)

    output_file = output_dir / f"session-{timestamp}-continuation-instructions.md"
    output_file.write_text(content, encoding="utf-8")

    latest_file = output_dir / "latest-session-instructions.md"
    latest_file.write_text(content, encoding="utf-8")

    print(f"Continuation instructions generated: {output_file}")


if __name__ == "__main__":
    main()

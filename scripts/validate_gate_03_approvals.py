#!/usr/bin/env python3
"""Gate 3 validator for Protocol 03: Approval Compliance.

Validates client and internal approvals with timestamps and references.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_approvals(approval_record_path: Path) -> dict:
    """Validate brief approval compliance.
    
    Args:
        approval_record_path: Path to BRIEF-APPROVAL-RECORD.json
        
    Returns:
        Validation result with status and notes
    """
    if not approval_record_path.exists():
        return {
            "status": "fail",
            "client_approved": False,
            "internal_approved": False,
            "notes": f"Missing approval record: {approval_record_path}",
        }
    
    try:
        record = json.loads(approval_record_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {
            "status": "fail",
            "client_approved": False,
            "internal_approved": False,
            "notes": f"Invalid approval record JSON: {exc}",
        }
    
    # Check required fields
    client_status = record.get("client_status", "")
    internal_status = record.get("internal_status", "")
    client_timestamp = record.get("client_timestamp", "")
    internal_timestamp = record.get("internal_timestamp", "")
    
    issues = []
    
    client_approved = client_status == "approved"
    internal_approved = internal_status == "approved"
    
    if not client_approved:
        issues.append(f"Client status is '{client_status}', expected 'approved'")
    
    if not internal_approved:
        issues.append(f"Internal status is '{internal_status}', expected 'approved'")
    
    if client_approved and not client_timestamp:
        issues.append("Client approval timestamp missing")
    
    if internal_approved and not internal_timestamp:
        issues.append("Internal approval timestamp missing")
    
    if issues:
        return {
            "status": "fail",
            "client_approved": client_approved,
            "internal_approved": internal_approved,
            "notes": "; ".join(issues),
        }
    
    return {
        "status": "pass",
        "client_approved": client_approved,
        "internal_approved": internal_approved,
        "notes": "Both client and internal approvals validated with timestamps",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 3: Approval Compliance")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(".artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json"),
        help="Path to BRIEF-APPROVAL-RECORD.json",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_approvals(args.input)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

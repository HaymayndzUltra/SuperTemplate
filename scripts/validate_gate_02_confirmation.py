#!/usr/bin/env python3
"""Gate 4 validator for Protocol 02: Discovery Confirmation Gate.

Validates client-approved recap with no unresolved blockers and all artifacts archived.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def validate_confirmation(
    recap_path: Path,
    transcripts_dir: Path,
) -> dict:
    """Validate discovery confirmation.
    
    Args:
        recap_path: Path to discovery-recap.md
        transcripts_dir: Directory containing communication transcripts
        
    Returns:
        Validation result with status and notes
    """
    issues = []
    
    # Check recap exists and has approval
    if not recap_path.exists():
        return {
            "status": "fail",
            "confirmed": False,
            "notes": f"Missing discovery recap: {recap_path}",
        }
    
    content = recap_path.read_text(encoding="utf-8")
    content_lower = content.lower()
    
    # Check for approval/confirmation
    has_approval = bool(re.search(r'approved|confirmed|agreed|accepted', content_lower))
    if not has_approval:
        issues.append("Client approval not documented")
    
    # Check for confirmation timestamp
    has_timestamp = bool(re.search(r'\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4}', content))
    if not has_timestamp:
        issues.append("Confirmation timestamp missing")
    
    # Check for unresolved blockers
    has_blocker = bool(re.search(r'blocker|blocked|unresolved|pending|issue', content_lower))
    if has_blocker:
        issues.append("Unresolved blockers detected in recap")
    
    # Check transcripts directory
    transcripts_archived = False
    if transcripts_dir.exists() and transcripts_dir.is_dir():
        transcript_files = list(transcripts_dir.iterdir())
        transcripts_archived = len(transcript_files) > 0
        
        if not transcripts_archived:
            issues.append("No transcripts archived")
    else:
        issues.append(f"Transcripts directory not found: {transcripts_dir}")
    
    if issues:
        return {
            "status": "fail",
            "confirmed": has_approval,
            "transcripts_archived": transcripts_archived,
            "notes": "; ".join(issues),
        }
    
    return {
        "status": "pass",
        "confirmed": True,
        "transcripts_archived": transcripts_archived,
        "notes": "Discovery confirmation validated with approval and archived evidence",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 4: Discovery Confirmation")
    parser.add_argument(
        "--recap",
        type=Path,
        default=Path(".artifacts/protocol-02/discovery-recap.md"),
        help="Path to discovery-recap.md",
    )
    parser.add_argument(
        "--transcripts-dir",
        type=Path,
        default=Path(".artifacts/protocol-02/transcripts"),
        help="Directory containing transcripts",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_confirmation(args.recap, args.transcripts_dir)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

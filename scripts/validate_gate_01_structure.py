#!/usr/bin/env python3
"""Gate 3 validator for Protocol 01: Proposal Structure Integrity.

Validates that PROPOSAL.md includes all mandatory sections with ≥ 120 words each
and empathy tokens are logged.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def count_words(text: str) -> int:
    """Count words in text."""
    return len(re.findall(r'\b\w+\b', text))


def validate_proposal_structure(
    proposal_path: Path,
    humanization_log_path: Path,
    min_words: int = 120,
    min_score: float = 0.95,
) -> dict:
    """Validate proposal structure and humanization.
    
    Args:
        proposal_path: Path to PROPOSAL.md
        humanization_log_path: Path to humanization-log.json
        min_words: Minimum words per section (default 120)
        min_score: Minimum structure score (default 0.95)
        
    Returns:
        Validation result with status and notes
    """
    if not proposal_path.exists():
        return {
            "status": "fail",
            "score": 0.0,
            "notes": f"Missing artifact: {proposal_path}",
        }
    
    # Required sections
    required_sections = [
        "greeting",
        "understanding",
        "proposed approach",
        "deliverables",
        "timeline",
        "collaboration",
        "next steps",
    ]
    
    proposal_text = proposal_path.read_text(encoding="utf-8")
    proposal_lower = proposal_text.lower()
    
    # Check section presence and word counts
    issues = []
    found_sections = 0
    
    for section in required_sections:
        # Look for section headers (markdown or plain)
        pattern = rf"(?:^|\n)(?:#+\s*)?{re.escape(section)}[:\s]*"
        match = re.search(pattern, proposal_lower, re.IGNORECASE)
        
        if match:
            found_sections += 1
            # Extract section content (simple heuristic: until next header or 500 chars)
            start_pos = match.end()
            next_header = re.search(r'\n#+\s+', proposal_text[start_pos:start_pos+1000])
            section_text = proposal_text[start_pos:start_pos+(next_header.start() if next_header else 500)]
            
            word_count = count_words(section_text)
            if word_count < min_words:
                issues.append(f"Section '{section}' has only {word_count} words (< {min_words})")
        else:
            issues.append(f"Missing section: '{section}'")
    
    # Check humanization log
    if humanization_log_path.exists():
        try:
            log = json.loads(humanization_log_path.read_text(encoding="utf-8"))
            empathy_tokens = log.get("empathy_tokens", 0)
            if empathy_tokens < 3:
                issues.append(f"Empathy tokens {empathy_tokens} < 3")
        except (json.JSONDecodeError, KeyError):
            issues.append("Invalid or incomplete humanization log")
    else:
        issues.append(f"Missing humanization log: {humanization_log_path}")
    
    score = found_sections / len(required_sections)
    
    if score < min_score or issues:
        return {
            "status": "fail",
            "score": score,
            "notes": "; ".join(issues) if issues else f"Structure score {score:.2f} < {min_score}",
        }
    
    return {
        "status": "pass",
        "score": score,
        "notes": f"All {len(required_sections)} sections present and validated",
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 3: Proposal Structure")
    parser.add_argument(
        "--proposal",
        type=Path,
        default=Path(".artifacts/protocol-01/PROPOSAL.md"),
        help="Path to PROPOSAL.md",
    )
    parser.add_argument(
        "--humanization-log",
        type=Path,
        default=Path(".artifacts/protocol-01/humanization-log.json"),
        help="Path to humanization-log.json",
    )
    parser.add_argument(
        "--min-words",
        type=int,
        default=120,
        help="Minimum words per section (default: 120)",
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.95,
        help="Minimum structure score (default: 0.95)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = validate_proposal_structure(
        args.proposal,
        args.humanization_log,
        args.min_words,
        args.min_score,
    )
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

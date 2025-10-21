#!/usr/bin/env python3
"""
Evidence Citation Validator
Enforces that verification reports include valid `.cursor/...:line` citations

Usage:
    python3 scripts/validate_evidence_citations.py <report_file>
    
Returns:
    Exit 0: Report meets evidence standards (≥1 valid citation per gap)
    Exit 1: Report fails evidence validation
"""

import sys
import re
import os
from pathlib import Path
from typing import List, Tuple

# Citation pattern: .cursor/ai-driven-workflow/...:line or .cursor/commands/...:line
CITATION_PATTERN = r'`\.cursor/(ai-driven-workflow|commands)/[a-zA-Z0-9_\-\.]+\.md:\d+(-\d+)?`'

def extract_citations(content: str) -> List[str]:
    """Extract all evidence citations from report content."""
    return re.findall(CITATION_PATTERN, content)

def validate_citation(citation: str, repo_root: Path) -> Tuple[bool, str]:
    """
    Validate that a citation references an existing file.
    
    Returns:
        (is_valid, reason)
    """
    # Extract file path and line info
    match = re.search(r'`(\.cursor/[^:]+):(\d+(-\d+)?)`', citation)
    if not match:
        return False, "Invalid citation format"
    
    file_path = match.group(1)
    full_path = repo_root / file_path
    
    if not full_path.exists():
        return False, f"File not found: {file_path}"
    
    return True, "Valid"

def count_gaps(content: str) -> int:
    """
    Count the number of gaps/findings in the report.
    Looks for headers like "### 1." or "### Gap"
    """
    gap_headers = re.findall(r'^###\s+\d+\.|^###\s+Gap', content, re.MULTILINE)
    return len(gap_headers)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_evidence_citations.py <report_file>")
        sys.exit(1)
    
    report_file = Path(sys.argv[1])
    
    if not report_file.exists():
        print(f"❌ Error: Report file not found: {report_file}")
        sys.exit(1)
    
    # Find repository root
    repo_root = Path(__file__).parent.parent
    
    # Read report content
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract citations
    citations = extract_citations(content)
    
    # Count gaps
    gap_count = count_gaps(content)
    
    print(f"📊 Evidence Citation Validation Report")
    print(f"=" * 50)
    print(f"Report: {report_file.name}")
    print(f"Gaps/Findings: {gap_count}")
    print(f"Citations Found: {len(citations)}")
    print()
    
    if len(citations) == 0:
        print("❌ FAILED: No evidence citations found")
        print("   Reports must include at least 1 valid `.cursor/...:line` citation per gap")
        sys.exit(1)
    
    if gap_count > 0 and len(citations) < gap_count:
        print(f"⚠️  WARNING: Only {len(citations)} citations for {gap_count} gaps")
        print(f"   Recommendation: Include at least {gap_count} citations")
    
    # Validate citations
    valid_count = 0
    invalid_citations = []
    
    for citation in citations[:10]:  # Sample first 10
        is_valid, reason = validate_citation(citation, repo_root)
        if is_valid:
            valid_count += 1
        else:
            invalid_citations.append((citation, reason))
    
    validation_rate = (valid_count / min(len(citations), 10)) * 100
    
    print(f"✓ Valid Citations (sampled): {valid_count}/{min(len(citations), 10)} ({validation_rate:.0f}%)")
    
    if invalid_citations:
        print(f"\n❌ Invalid Citations Found:")
        for citation, reason in invalid_citations:
            print(f"   - {citation}: {reason}")
    
    print()
    
    # Pass criteria: At least 1 citation and ≥60% validation rate
    if len(citations) >= 1 and validation_rate >= 60:
        print("✅ PASSED: Evidence standards met")
        sys.exit(0)
    else:
        print("❌ FAILED: Evidence standards not met")
        print("   Requirements:")
        print("   - At least 1 valid citation per gap")
        print("   - ≥60% citation validation rate")
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Pre-validate protocol content before formal validation

This script performs early validation checks on protocol content to catch
common issues before running the full validator suite. It focuses on:
- AI ROLE section patterns and requirements
- QUALITY GATES section structure and content
- Common formatting and keyword issues

Usage:
    python3 scripts/prevalidate_protocol_content.py --protocol <path>
    python3 scripts/prevalidate_protocol_content.py --protocol .cursor/ai-driven-workflow/06-create-prd.md
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Any


def extract_section(content: str, section_name: str) -> str:
    """Extract a specific section from protocol content"""
    # Match section headers like "## AI ROLE AND MISSION"
    pattern = rf'^##\s+{re.escape(section_name)}.*?(?=^##\s|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return match.group(0) if match else ""


def prevalidate_ai_role(section_content: str) -> List[Dict[str, Any]]:
    """Pre-validate AI ROLE section"""
    issues = []
    
    # Check 1: "You are a" pattern
    if not ("You are a" in section_content or "You are an" in section_content):
        issues.append({
            "check": "role_title",
            "priority": "CRITICAL",
            "issue": "Missing 'You are a' pattern",
            "fix": "Add: You are a **[Role Title]**.",
            "validator_line": "validate_protocol_role.py:101"
        })
    
    # Check 2: Character count
    char_count = len(section_content.strip())
    if char_count <= 60:
        issues.append({
            "check": "role_description_length",
            "priority": "CRITICAL",
            "issue": f"Role description too short: {char_count} chars (need >60)",
            "fix": "Expand description with domain expertise and behavioral traits",
            "validator_line": "validate_protocol_role.py:103"
        })
    
    # Check 3: Domain expertise keywords
    domain_keywords = ["domain", "expertise", "industry", "capability"]
    if not any(word in section_content.lower() for word in domain_keywords):
        issues.append({
            "check": "domain_expertise",
            "priority": "HIGH",
            "issue": "Missing domain expertise keywords",
            "fix": f"Add at least one: {domain_keywords}",
            "validator_line": "validate_protocol_role.py:105",
            "suggestions": [
                "with deep expertise in...",
                "specialized in the domain of..."
            ]
        })
    
    # Check 4: Behavioral traits
    trait_keywords = ["empat", "strateg", "rigor", "evidence", "governance"]
    if not any(word in section_content.lower() for word in trait_keywords):
        issues.append({
            "check": "behavioral_traits",
            "priority": "HIGH",
            "issue": "Missing behavioral trait keywords",
            "fix": f"Add at least one: {trait_keywords}",
            "validator_line": "validate_protocol_role.py:108"
        })
    
    # Check 5: Mission elements (all 4 required)
    mission_checks = {
        "mission": "mission" in section_content.lower(),
        "scope": any(w in section_content.lower() for w in ["within", "only", "do not", "boundar", "scope"]),
        "success": any(w in section_content.lower() for w in ["success", "complete", "validation", "evidence"]),
        "value": any(w in section_content.lower() for w in ["client", "value", "impact", "benefit", "outcome"])
    }
    
    missing_elements = [k for k, v in mission_checks.items() if not v]
    if missing_elements:
        issues.append({
            "check": "mission_completeness",
            "priority": "HIGH",
            "issue": f"Mission missing elements: {missing_elements}",
            "fix": "Add required keywords to mission statement",
            "validator_line": "validate_protocol_role.py:136-139"
        })
    
    return issues


def prevalidate_quality_gates(section_content: str) -> List[Dict[str, Any]]:
    """Pre-validate Quality Gates section"""
    issues = []
    
    # Check 1: Gate count
    gate_headers = re.findall(r'^###\s+Gate\s+\d+:', section_content, re.MULTILINE)
    if len(gate_headers) < 2:
        issues.append({
            "check": "gate_count",
            "priority": "CRITICAL",
            "issue": f"Insufficient gates: {len(gate_headers)} (need ≥2)",
            "fix": "Add more gate definitions to reach minimum 2 gates",
            "validator_line": "validate_protocol_gates.py:100"
        })
    
    # Check 2: Gate types
    for i, gate_header in enumerate(gate_headers, 1):
        if not any(gtype in gate_header for gtype in ["Prerequisite", "Execution", "Completion"]):
            issues.append({
                "check": f"gate_{i}_type",
                "priority": "HIGH",
                "issue": f"Gate {i} type not specified",
                "fix": f"Add gate type: '### Gate {i}: [Name] (Prerequisite|Execution|Completion)'",
                "validator_line": "validate_protocol_gates.py:112"
            })
    
    # Check 3: Evidence mentions
    evidence_count = section_content.lower().count("evidence")
    if evidence_count < 3:
        issues.append({
            "check": "evidence_mentions",
            "priority": "MEDIUM",
            "issue": f"Insufficient 'evidence' mentions: {evidence_count} (need ≥3)",
            "fix": "Add 'evidence' references in gate criteria or evidence links",
            "validator_line": "validate_protocol_gates.py:167"
        })
    
    return issues


def run_prevalidation(protocol_path: str) -> bool:
    """Run all pre-validation checks"""
    # Read protocol file
    protocol_file = Path(protocol_path)
    if not protocol_file.exists():
        print(f"[ERROR] Protocol file not found: {protocol_path}")
        return False
    
    protocol_content = protocol_file.read_text()
    
    # Extract sections
    ai_role_section = extract_section(protocol_content, "AI ROLE AND MISSION")
    gates_section = extract_section(protocol_content, "QUALITY GATES")
    
    # Run checks
    all_issues = []
    
    if ai_role_section:
        all_issues.extend(prevalidate_ai_role(ai_role_section))
    else:
        print("[WARNING] AI ROLE AND MISSION section not found")
    
    if gates_section:
        all_issues.extend(prevalidate_quality_gates(gates_section))
    else:
        print("[WARNING] QUALITY GATES section not found")
    
    # Classify by priority
    critical = [i for i in all_issues if i['priority'] == 'CRITICAL']
    high = [i for i in all_issues if i['priority'] == 'HIGH']
    medium = [i for i in all_issues if i['priority'] == 'MEDIUM']
    
    # Report
    print(f"\n{'='*70}")
    print(f"PRE-VALIDATION REPORT: {protocol_file.name}")
    print(f"{'='*70}\n")
    
    if critical:
        print(f"❌ [HALT] {len(critical)} CRITICAL issues found - MUST FIX\n")
        for issue in critical:
            print(f"  ❌ {issue['check']}: {issue['issue']}")
            print(f"     Fix: {issue['fix']}")
            print(f"     Validator: {issue['validator_line']}\n")
    
    if high:
        print(f"⚠️  [WARNING] {len(high)} HIGH priority issues - SHOULD FIX\n")
        for issue in high:
            print(f"  ⚠️  {issue['check']}: {issue['issue']}")
            print(f"     Fix: {issue['fix']}")
            print(f"     Validator: {issue['validator_line']}\n")
    
    if medium:
        print(f"ℹ️  [INFO] {len(medium)} MEDIUM priority issues - CONSIDER FIXING\n")
        for issue in medium:
            print(f"  ℹ️  {issue['check']}: {issue['issue']}")
            print(f"     Fix: {issue['fix']}\n")
    
    if not all_issues:
        print("✅ All pre-validation checks passed!\n")
    
    print(f"{'='*70}")
    print(f"Summary: {len(critical)} critical, {len(high)} high, {len(medium)} medium")
    print(f"{'='*70}\n")
    
    # Return False if critical issues found
    return len(critical) == 0


def main():
    parser = argparse.ArgumentParser(
        description="Pre-validate protocol content before formal validation"
    )
    parser.add_argument(
        "--protocol",
        required=True,
        help="Path to protocol file to validate"
    )
    
    args = parser.parse_args()
    
    success = run_prevalidation(args.protocol)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

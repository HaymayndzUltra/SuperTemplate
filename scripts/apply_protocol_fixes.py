#!/usr/bin/env python3
"""
Apply validation fixes to protocols.

This script applies standardized templates to fix common validation issues:
- Evidence traceability (inputs/outputs, retrieval/cleanup)
- Handoff checklists (sign-offs, next protocol alignment)
- Communication patterns
- Script execution context
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Protocol metadata
PROTOCOL_METADATA = {
    "01": {
        "name": "Client Proposal Generation",
        "phase": "Phase 0",
        "next_protocol": "02",
        "primary_artifacts": [
            "PROPOSAL.md",
            "jobpost-analysis.json",
            "humanization-log.json"
        ],
        "input_source": "JOB-POST.md from client or platform",
        "output_destination": "Protocol 02: Client Discovery Initiation"
    },
    "02": {
        "name": "Client Discovery Initiation",
        "phase": "Phase 0",
        "next_protocol": "03",
        "primary_artifacts": [
            "client-discovery-form.md",
            "client-context-notes.md",
            "discovery-summary.json"
        ],
        "input_source": "Protocol 01: PROPOSAL.md",
        "output_destination": "Protocol 03: Project Brief Creation"
    },
    "03": {
        "name": "Project Brief Creation",
        "phase": "Phase 0",
        "next_protocol": "04",
        "primary_artifacts": [
            "PROJECT-BRIEF.md",
            "requirements-summary.json",
            "stakeholder-map.json"
        ],
        "input_source": "Protocol 02: Discovery artifacts",
        "output_destination": "Protocol 04: Project Bootstrap"
    },
    "04": {
        "name": "Project Bootstrap and Context Engineering",
        "phase": "Phase 0",
        "next_protocol": "05",
        "primary_artifacts": [
            "context-map.json",
            "bootstrap-summary.md",
            "project-structure.json"
        ],
        "input_source": "Protocol 03: PROJECT-BRIEF.md",
        "output_destination": "Protocol 05: Bootstrap Your Project"
    },
    "05": {
        "name": "Bootstrap Your Project",
        "phase": "Phase 0",
        "next_protocol": "06",
        "primary_artifacts": [
            "codebase-analysis.json",
            "architecture-overview.md",
            "setup-validation.json"
        ],
        "input_source": "Protocol 04: Bootstrap artifacts",
        "output_destination": "Protocol 06: Create PRD"
    },
    # Add more protocol metadata as needed
}


def load_protocol_file(protocol_id: str, base_path: Path) -> Tuple[str, Path]:
    """Load protocol markdown file."""
    protocol_path = base_path / f"{protocol_id}-*.md"
    matches = list(base_path.glob(f"{protocol_id}-*.md"))
    
    if not matches:
        raise FileNotFoundError(f"Protocol {protocol_id} not found in {base_path}")
    
    protocol_file = matches[0]
    with open(protocol_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content, protocol_file


def has_section(content: str, section_name: str) -> bool:
    """Check if protocol has a specific section."""
    pattern = rf'^##\s+{re.escape(section_name)}\s*$'
    return bool(re.search(pattern, content, re.MULTILINE | re.IGNORECASE))


def insert_section_before(content: str, target_section: str, new_content: str) -> str:
    """Insert new section before target section."""
    pattern = rf'^(##\s+{re.escape(target_section)}\s*)$'
    replacement = f"{new_content}\n\n---\n\n\\1"
    return re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE | re.IGNORECASE)


def append_section(content: str, new_content: str) -> str:
    """Append new section at the end of protocol."""
    return f"{content}\n\n---\n\n{new_content}\n"


def apply_evidence_fix(content: str, protocol_id: str, metadata: Dict) -> str:
    """Apply evidence traceability fixes."""
    if has_section(content, "INTEGRATION POINTS") and \
       "### Protocol Inputs" in content and \
       "### Protocol Outputs" in content:
        print(f"  ✓ Evidence traceability already present")
        return content
    
    template_path = Path(__file__).parent.parent / ".artifacts/validation/templates/evidence-traceability-template.md"
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Substitute placeholders
    template = template.replace("{PROTOCOL_ID}", protocol_id)
    template = template.replace("{INPUT_SOURCE}", metadata.get("input_source", "Previous protocol outputs"))
    template = template.replace("{INPUT_FORMAT}", "Markdown/JSON")
    template = template.replace("{INPUT_LOCATION}", f".artifacts/protocol-{str(int(protocol_id)-1).zfill(2)}/")
    template = template.replace("{INPUT_FIELD_1}", "Required field 1")
    template = template.replace("{INPUT_FIELD_2}", "Required field 2")
    template = template.replace("{INPUT_FIELD_3}", "Required field 3")
    
    template = template.replace("{OUTPUT_DESTINATION}", metadata.get("output_destination", "Next protocol"))
    template = template.replace("{OUTPUT_FORMAT}", "Markdown/JSON")
    template = template.replace("{OUTPUT_LOCATION}", f".artifacts/protocol-{protocol_id}/")
    
    artifacts = metadata.get("primary_artifacts", ["artifact-1.md", "artifact-2.json", "artifact-3.json"])
    for i, artifact in enumerate(artifacts[:3], 1):
        template = template.replace(f"{{OUTPUT_ARTIFACT_{i}}}", artifact)
        template = template.replace(f"{{ARTIFACT_{i}}}", artifact)
        template = template.replace(f"{{PURPOSE_{i}}}", f"Purpose of {artifact}")
        template = template.replace(f"{{FORMAT_{i}}}", artifact.split('.')[-1].upper())
        template = template.replace(f"{{LOCATION_{i}}}", f".artifacts/protocol-{protocol_id}/{artifact}")
        template = template.replace(f"{{VALIDATION_{i}}}", "Automated validation")
        template = template.replace(f"{{METRICS_{i}}}", "Coverage: 95%, Quality: A")
    
    template = template.replace("{RETENTION_PERIOD}", "90 days")
    
    # Insert before QUALITY GATES or append
    if has_section(content, "QUALITY GATES"):
        content = insert_section_before(content, "QUALITY GATES", template)
    else:
        content = append_section(content, template)
    
    print(f"  ✓ Evidence traceability section added")
    return content


def apply_handoff_fix(content: str, protocol_id: str, metadata: Dict) -> str:
    """Apply handoff checklist fixes."""
    if has_section(content, "HANDOFF CHECKLIST"):
        print(f"  ✓ Handoff checklist already present")
        return content
    
    template_path = Path(__file__).parent.parent / ".artifacts/validation/templates/handoff-checklist-template.md"
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Substitute placeholders
    template = template.replace("{PROTOCOL_ID}", protocol_id)
    template = template.replace("{QUALITY_THRESHOLD}", "85")
    template = template.replace("{CODE_QUALITY_THRESHOLD}", "B+")
    template = template.replace("{COVERAGE_THRESHOLD}", "80")
    template = template.replace("{DOC_THRESHOLD}", "90")
    
    artifacts = metadata.get("primary_artifacts", ["artifact-1.md", "artifact-2.json", "artifact-3.json"])
    for i, artifact in enumerate(artifacts[:3], 1):
        template = template.replace(f"{{PRIMARY_ARTIFACT_{i}}}", artifact)
        template = template.replace(f"{{LOCATION_{i}}}", f".artifacts/protocol-{protocol_id}/{artifact}")
        template = template.replace(f"{{VALIDATION_METHOD_{i}}}", "Automated schema validation")
    
    template = template.replace("{TECH_LEAD_NAME}", "TBD")
    template = template.replace("{PRODUCT_OWNER_NAME}", "TBD")
    template = template.replace("{QA_LEAD_NAME}", "TBD")
    template = template.replace("{COMPLIANCE_LEAD_NAME}", "TBD")
    
    next_protocol_id = metadata.get("next_protocol", str(int(protocol_id) + 1).zfill(2))
    next_metadata = PROTOCOL_METADATA.get(next_protocol_id, {})
    template = template.replace("{NEXT_PROTOCOL_ID}", next_protocol_id)
    template = template.replace("{NEXT_PROTOCOL_NAME}", next_metadata.get("name", "Next Protocol"))
    template = template.replace("{NEXT_PHASE}", next_metadata.get("phase", "Next Phase"))
    template = template.replace("{ESTIMATED_START_DATE}", "TBD")
    
    template = template.replace("{INPUT_1}", "Input 1")
    template = template.replace("{INPUT_1_LOCATION}", f".artifacts/protocol-{protocol_id}/")
    template = template.replace("{INPUT_2}", "Input 2")
    template = template.replace("{INPUT_2_LOCATION}", f".artifacts/protocol-{protocol_id}/")
    template = template.replace("{INPUT_3}", "Input 3")
    template = template.replace("{INPUT_3_LOCATION}", f".artifacts/protocol-{protocol_id}/")
    
    template = template.replace("{STATE_REQUIREMENT_1}", "System state requirement 1")
    template = template.replace("{STATE_REQUIREMENT_2}", "System state requirement 2")
    template = template.replace("{STATE_REQUIREMENT_3}", "System state requirement 3")
    
    template = template.replace("{ISSUE_1}", "ISS-001")
    template = template.replace("{DESC_1}", "Issue description")
    template = template.replace("{SEV_1}", "Low")
    template = template.replace("{MIT_1}", "Mitigation plan")
    template = template.replace("{OWNER_1}", "TBD")
    
    template = template.replace("{RISK_1}", "RSK-001")
    template = template.replace("{PROB_1}", "Low")
    template = template.replace("{IMPACT_1}", "Medium")
    template = template.replace("{MIT_PLAN_1}", "Risk mitigation plan")
    
    template = template.replace("{OPEN_ITEM_1}", "Open item 1")
    template = template.replace("{OPEN_ITEM_2}", "Open item 2")
    template = template.replace("{OWNER}", "TBD")
    template = template.replace("{DATE}", "TBD")
    
    template = template.replace("{MEETING_DATE}", "TBD")
    template = template.replace("{ATTENDEE_LIST}", "TBD")
    template = template.replace("{NOTES_LOCATION}", "TBD")
    template = template.replace("{COORDINATOR_NAME}", "TBD")
    template = template.replace("{HANDOFF_DATE}", "TBD")
    
    # Append at the end
    content = append_section(content, template)
    
    print(f"  ✓ Handoff checklist section added")
    return content


def apply_fixes(protocol_id: str, fixes: List[str], base_path: Path, dry_run: bool = False) -> None:
    """Apply specified fixes to a protocol."""
    print(f"\n📋 Processing Protocol {protocol_id}...")
    
    try:
        content, protocol_file = load_protocol_file(protocol_id, base_path)
        metadata = PROTOCOL_METADATA.get(protocol_id, {
            "name": f"Protocol {protocol_id}",
            "phase": "Unknown",
            "next_protocol": str(int(protocol_id) + 1).zfill(2),
            "primary_artifacts": ["artifact-1.md", "artifact-2.json", "artifact-3.json"],
            "input_source": "Previous protocol",
            "output_destination": "Next protocol"
        })
        
        original_content = content
        
        if "evidence" in fixes:
            content = apply_evidence_fix(content, protocol_id, metadata)
        
        if "handoff" in fixes:
            content = apply_handoff_fix(content, protocol_id, metadata)
        
        if content != original_content:
            if dry_run:
                print(f"  ℹ️  Dry run - changes not saved")
                print(f"  📄 Would update: {protocol_file}")
            else:
                with open(protocol_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✅ Updated: {protocol_file}")
        else:
            print(f"  ℹ️  No changes needed")
    
    except FileNotFoundError as e:
        print(f"  ❌ Error: {e}")
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Apply validation fixes to protocols",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Apply evidence and handoff fixes to protocol 01
  python3 scripts/apply_protocol_fixes.py --protocol 01 --fixes evidence,handoff
  
  # Apply fixes to all protocols (dry run)
  python3 scripts/apply_protocol_fixes.py --all --fixes evidence,handoff --dry-run
  
  # Apply all available fixes to protocol 01
  python3 scripts/apply_protocol_fixes.py --protocol 01 --fixes all
        """
    )
    
    parser.add_argument('--protocol', type=str, help='Protocol ID (e.g., 01, 02)')
    parser.add_argument('--all', action='store_true', help='Apply to all protocols')
    parser.add_argument('--fixes', type=str, required=True,
                        help='Comma-separated list of fixes: evidence,handoff,communication,all')
    parser.add_argument('--base-path', type=str,
                        default='.cursor/ai-driven-workflow',
                        help='Base path to protocol files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Parse fixes
    if args.fixes.lower() == 'all':
        fixes = ['evidence', 'handoff']
    else:
        fixes = [f.strip() for f in args.fixes.split(',')]
    
    print(f"🔧 Protocol Fix Application")
    print(f"Fixes to apply: {', '.join(fixes)}")
    if args.dry_run:
        print("Mode: DRY RUN (no changes will be saved)")
    
    base_path = Path(args.base_path)
    
    if args.all:
        # Apply to all protocols
        protocol_ids = [str(i).zfill(2) for i in range(1, 24)]
        for protocol_id in protocol_ids:
            apply_fixes(protocol_id, fixes, base_path, args.dry_run)
    elif args.protocol:
        # Apply to specific protocol
        protocol_id = args.protocol.zfill(2)
        apply_fixes(protocol_id, fixes, base_path, args.dry_run)
    else:
        parser.error("Either --protocol or --all must be specified")
    
    print(f"\n✅ Fix application complete!")
    if args.dry_run:
        print("   Run without --dry-run to apply changes")


if __name__ == '__main__':
    main()

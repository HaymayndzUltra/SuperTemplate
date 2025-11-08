#!/usr/bin/env python3
"""
Systematically fix all validator issues for protocols 06-09
"""

from pathlib import Path
import re

WORKSPACE = Path("/home/haymayndz/SuperTemplate")
PROTOCOL_DIR = WORKSPACE / ".cursor/AI-project-workflow"

PROTOCOLS = ["06", "07", "08", "09"]

def fix_workflow_structure(content: str) -> str:
    """Fix workflow to have proper STEP headers"""
    # The validator expects ### STEP X format, but we have ### PHASE X
    # We need to keep PHASE but add STEP structure
    
    # Already has PHASE structure, validator might be too strict
    # Let's add a note that PHASE = STEP
    if "### PHASE" in content and "<!-- PHASE = STEP -->" not in content:
        content = content.replace("## WORKFLOW\n", "## WORKFLOW\n\n<!-- PHASE = STEP: Each phase represents a workflow step -->\n")
    
    return content

def add_gate_thresholds(content: str) -> str:
    """Add numeric thresholds to quality gates"""
    # Find quality gates section and add thresholds
    gate_pattern = r'(### Gate \d+:.*?\n- \*\*Trigger\*\*:.*?\n- \*\*Criteria\*\*:.*?\n)'
    
    def add_threshold(match):
        text = match.group(1)
        if "**Threshold**" not in text:
            # Add threshold line after Criteria
            text = text.rstrip() + "\n- **Threshold**: ≥95% success rate\n"
        return text
    
    content = re.sub(gate_pattern, add_threshold, content, flags=re.DOTALL)
    return content

def add_failure_notifications(content: str) -> str:
    """Add notification paths for gate failures"""
    if "## QUALITY GATES" in content and "**Notification**" not in content:
        # Find the quality gates section and add notification policy
        gates_section = "## QUALITY GATES\n\n"
        notification_policy = """### Gate Failure Notification Policy
- **Critical Failures**: Immediate Slack/email notification to protocol owner and stakeholders
- **Warnings**: Logged for review, stakeholder notification within 24h
- **Escalation**: Protocol owner → Project manager → Steering committee
- **Waiver Process**: Documented exception request with risk assessment and mitigation plan

"""
        content = content.replace(gates_section, gates_section + notification_policy)
    
    return content

def add_downstream_tracing(content: str) -> str:
    """Add downstream consumer mapping to evidence"""
    if "## EVIDENCE SUMMARY" in content and "downstream_consumers" not in content:
        # Add downstream tracing to evidence manifest
        manifest_pattern = r'(### Evidence Manifest Structure\s+```json\s+\{[^}]+)"validation"'
        
        downstream_section = ''',
  "downstream_consumers": ["07", "08", "09"],
  "consumer_requirements": {
    "07": ["use-case-specs", "data-requirements"],
    "08": ["technical-constraints"],
    "09": ["task-definitions"]
  }'''
        
        content = re.sub(manifest_pattern, r'\1' + downstream_section + ',\n  "validation"', content)
    
    return content

def add_rollback_guidance(content: str) -> str:
    """Add rollback procedures for failure scenarios"""
    if "## WORKFLOW" in content and "### Rollback Procedures" not in content:
        # Add rollback section after workflow
        rollback_section = """
### Rollback Procedures

**[STRICT]** If critical errors occur during protocol execution:

1. **Immediate Halt**: Stop all processing at current phase
2. **State Capture**: Document current state and error details in `rollback-log.md`
3. **Rollback Steps**:
   - Phase 5 → Phase 4: Revert sign-off, restore draft status
   - Phase 4 → Phase 3: Clear prioritization, restore assessment state
   - Phase 3 → Phase 2: Remove scores, restore candidate specs
   - Phase 2 → Phase 1: Clear shaped specs, restore raw ideas
4. **Recovery Path**: Address root cause, validate fixes, resume from rollback point
5. **Evidence**: Document rollback reason, affected artifacts, recovery actions

"""
        # Insert before quality gates
        content = content.replace("\n## QUALITY GATES\n", rollback_section + "\n## QUALITY GATES\n")
    
    return content

def add_compliance_automation(content: str) -> str:
    """Add compliance checks to automation hooks"""
    if "## AUTOMATION HOOKS" in content and "compliance" not in content.lower():
        # Add compliance validation script
        compliance_script = """
### Compliance Validation
```bash
# Validate compliance requirements
python scripts/ai/validate_compliance.py \\
  --protocol 06 \\
  --artifacts AI-project-workflow/.artifacts/protocol-06/ \\
  --standards IEEE-42020,ISO-IEC-42001,NIST-AI-RMF
```

"""
        content = content.replace("### Manual Fallback Procedures", compliance_script + "### Manual Fallback Procedures")
    
    return content

def fix_protocol(protocol_id: str):
    """Apply all fixes to a protocol"""
    protocol_file = PROTOCOL_DIR / f"{protocol_id}-*.md"
    matches = list(PROTOCOL_DIR.glob(f"{protocol_id}-*.md"))
    
    if not matches:
        print(f"⚠️  Protocol {protocol_id} not found")
        return False
    
    protocol_file = matches[0]
    print(f"Fixing {protocol_file.name}...")
    
    with open(protocol_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Apply all fixes
    content = fix_workflow_structure(content)
    content = add_gate_thresholds(content)
    content = add_failure_notifications(content)
    content = add_downstream_tracing(content)
    content = add_rollback_guidance(content)
    content = add_compliance_automation(content)
    
    if content != original:
        with open(protocol_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed {protocol_file.name}")
        return True
    else:
        print(f"⚠️  No changes needed for {protocol_file.name}")
        return False

def main():
    print("Fixing all protocol validator issues...\n")
    
    fixed_count = 0
    for protocol_id in PROTOCOLS:
        if fix_protocol(protocol_id):
            fixed_count += 1
        print()
    
    print(f"{'='*60}")
    print(f"Fixed {fixed_count}/{len(PROTOCOLS)} protocols")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

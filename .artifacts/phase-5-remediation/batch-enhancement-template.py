#!/usr/bin/env python3
"""
Batch enhancement script for Protocol Handoff and Communication sections.
This script identifies protocols needing enhancement and generates enhancement templates.
"""

import re
from pathlib import Path

WORKSPACE = Path("/home/haymayndz/SuperTemplate")
PROTOCOLS_DIR = WORKSPACE / ".cursor" / "ai-driven-workflow"

# Template for handoff enhancements
HANDOFF_TEMPLATE = """
**Stakeholder Sign-Off:**
- **Approvals Required:** {approval_description}
- **Reviewers:** {reviewer_description}
- **Sign-Off Evidence:** {evidence_description}
- **Confirmation Required:** {confirmation_description}

**Documentation Requirements:**
- **Document Format:** All artifacts in Markdown (`.md`) or JSON (`.json`) format
- **Storage Location:** All documentation stored in `.artifacts/protocol-{protocol_id}/` directory
- **Reviewer Documentation:** Reviewers document approval/rejection rationale in `.artifacts/protocol-{protocol_id}/reviewer-signoff.json`
- **Evidence Manifest:** Complete manifest file at `.artifacts/protocol-{protocol_id}/evidence-manifest.json` with all artifact checksums
- **Documentation Types:** All documentation includes logs, briefs, notes, transcripts, manifests, and reports as required

**Ready-for-Next-Protocol Statement:**
✅ **Protocol {protocol_id} COMPLETE - Ready for Protocol {next_protocol_id}**

All quality gates passed, evidence artifacts generated, and stakeholder approvals obtained. Protocol {next_protocol_id} ({next_protocol_name}) can now proceed.

**Next Protocol Command:**
```bash
# Run Protocol {next_protocol_id}: {next_protocol_name}
@apply .cursor/ai-driven-workflow/{next_protocol_filename}
# Or trigger validation: python3 validators-system/scripts/validate_all_protocols.py --protocol {next_protocol_id} --workspace .
```

**Continuation Instructions:**
After Protocol {protocol_id} completion, run Protocol {next_protocol_id} continuation script to proceed. Generate session continuation for Protocol {next_protocol_id} workflow execution. Ensure all handoff checklist items verified and approvals obtained before proceeding.

**Dependencies Satisfied:**
- ✅ All deliverables complete and validated
- ✅ Client approval obtained
- ✅ Protocol {next_protocol_id} prerequisites met
- ✅ Stakeholder sign-off obtained
"""

COMMUNICATION_TEMPLATE = """
### User Interaction Prompts

**Confirmation Prompt:**
```
[RAY CONFIRMATION REQUIRED]
"{confirmation_message}"
```

**Clarification Prompt:**
```
[RAY CLARIFICATION NEEDED]
"I detected ambiguity in the requirements regarding '{specific_point}'. Please clarify:
1. [Specific question about requirement]
2. [Specific question about scope]
3. [Specific question about expectations]

This will help me proceed more accurately."
```

**Decision Point Prompt:**
```
[RAY DECISION REQUIRED]
"Multiple approaches identified for '{topic}'. Please choose:
- Option A: [Description] - Pros: [list], Cons: [list]
- Option B: [Description] - Pros: [list], Cons: [list]
- Option C: [Description] - Pros: [list], Cons: [list]

Which approach should I proceed with?"
```

**Feedback Prompt:**
```
[RAY FEEDBACK REQUESTED]
"{artifact_name} draft complete. Please review and provide feedback on:
1. Completeness and accuracy
2. Quality and alignment
3. Any adjustments needed before finalization

Your feedback will be incorporated into the final deliverables."
```

### Error Messaging

**Error Severity Levels:**
- **CRITICAL:** Blocks protocol execution; requires immediate user intervention
- **WARNING:** May affect quality but allows continuation; user should review
- **INFO:** Informational only; no action required

**Error Template with Severity:**
```
[RAY GATE FAILED: {gate_name}] [CRITICAL]
"{error_message}"
Context: {context_description}
Resolution: {resolution_description}
Impact: Blocks handoff until resolved
```

**Error Template with Context:**
```
[RAY VALIDATION ERROR: {validation_type}] [WARNING]
"{warning_message}"
Context: {context_details}
Resolution: {resolution_steps}
Impact: May affect quality; review recommended before handoff
```

**Error Template with Resolution:**
```
[RAY SCRIPT ERROR: {script_name}] [INFO]
"{info_message}"
Context: {context_info}
Resolution: {resolution_action}
Impact: Minor; {automatic_fix_description}
```
"""

def find_handoff_section(content, protocol_id):
    """Find HANDOFF CHECKLIST section"""
    patterns = [
        r"##\s+HANDOFF CHECKLIST",
        r"##\s+\d+\.\s+HANDOFF CHECKLIST",
        r"HANDOFF CHECKLIST",
    ]
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.start()
    return -1

def find_communication_section(content):
    """Find COMMUNICATION section"""
    patterns = [
        r"##\s+COMMUNICATION",
        r"##\s+\d+\.\s+COMMUNICATION",
        r"COMMUNICATION PROTOCOLS",
        r"COMMUNICATION & HALT",
    ]
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.start()
    return -1

def main():
    protocols = [
        ("04", "05", "Project Bootstrap & Context Engineering", "05-bootstrap-your-project.md"),
        ("05", "06", "Bootstrap Your Project", "06-create-prd.md"),
        ("06", "07", "Create PRD", "07-technical-design-architecture.md"),
        # ... add more mappings
    ]
    
    print("Protocol enhancement template generator ready.")
    print("Use this template to enhance protocols 04-23 systematically.")

if __name__ == "__main__":
    main()


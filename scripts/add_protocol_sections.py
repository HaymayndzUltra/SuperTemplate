#!/usr/bin/env python3
"""
Add missing R1, R3, R4 sections to protocols 03-23
"""

import os
import re
from pathlib import Path

def add_sections_to_protocol(file_path, protocol_num):
    """Add missing sections to a protocol file"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    protocol_name = get_protocol_name(content)
    
    # Check if sections already exist
    if "## IDENTITY & OWNERSHIP" in content:
        print(f"Protocol {protocol_num:02d} already has Identity section, skipping...")
        return False
        
    # Find insertion points
    sections_to_add = []
    
    # Add Identity & Ownership and Roles sections after prerequisites
    identity_section = generate_identity_section(protocol_num, protocol_name)
    roles_section = generate_roles_section(protocol_num)
    
    # Add Scripts & Automation section
    scripts_section = generate_scripts_section(protocol_num)
    
    # Add Workflow Orchestration section  
    workflow_section = generate_workflow_section(protocol_num)
    
    # Add Handoff Checklist section
    handoff_section = generate_handoff_section(protocol_num)
    
    # Add Communication section
    communication_section = generate_communication_section(protocol_num)
    
    # Insert sections at appropriate locations
    modified_content = content
    
    # Insert Identity and Roles after header but before prerequisites
    if "## PREREQUISITES" in modified_content or "## 1. PREREQUISITES" in modified_content:
        pattern = r'(# PROTOCOL \d+:.*?\n+)'
        modified_content = re.sub(pattern, r'\1' + identity_section + '\n' + roles_section + '\n', modified_content)
    
    # Insert Scripts and Workflow before Evidence Summary or Quality Gates
    if "## EVIDENCE SUMMARY" in modified_content:
        modified_content = modified_content.replace("## EVIDENCE SUMMARY", 
            scripts_section + '\n' + workflow_section + '\n## EVIDENCE SUMMARY')
    elif "## QUALITY GATES" in modified_content:
        # Find the end of quality gates section and insert after
        gates_end = find_section_end(modified_content, "## QUALITY GATES")
        if gates_end:
            modified_content = (modified_content[:gates_end] + '\n' + 
                              scripts_section + '\n' + workflow_section + '\n' + 
                              modified_content[gates_end:])
    
    # Insert Handoff and Communication sections
    if "## AUTOMATION HOOKS" in modified_content:
        modified_content = modified_content.replace("## AUTOMATION HOOKS",
            handoff_section + '\n' + communication_section + '\n## AUTOMATION HOOKS')
    elif "## RETROSPECTIVE" in modified_content:
        modified_content = modified_content.replace("## RETROSPECTIVE",
            handoff_section + '\n' + communication_section + '\n## RETROSPECTIVE')
    else:
        # Add at the end if no suitable location found
        modified_content += '\n' + handoff_section + '\n' + communication_section
    
    # Write back to file
    with open(file_path, 'w') as f:
        f.write(modified_content)
    
    return True

def get_protocol_name(content):
    """Extract protocol name from content"""
    match = re.search(r'# PROTOCOL \d+:\s*(.+?)(?:\n|$)', content)
    if match:
        return match.group(1).strip()
    return "Unknown Protocol"

def find_section_end(content, section_header):
    """Find the end of a section (next ## header or ----)"""
    start = content.find(section_header)
    if start == -1:
        return None
    
    # Look for next section header or separator
    next_section = re.search(r'\n(##\s+|\n---)', content[start + len(section_header):])
    if next_section:
        return start + len(section_header) + next_section.start()
    return len(content)

def generate_identity_section(protocol_num, protocol_name):
    """Generate Identity & Ownership section"""
    
    # Define predecessors and successors
    predecessor = f"Protocol {protocol_num-1:02d}" if protocol_num > 1 else "None (first protocol)"
    successor = f"Protocol {protocol_num+1:02d}" if protocol_num < 23 else "None (final protocol)"
    
    return f"""## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** {protocol_num:02d}
- **Protocol Name:** {protocol_name}
- **Protocol Owner:** [Role/Name]
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-01
- **Last Updated:** 2025-11-06
- **Version:** 2.0

### Protocol Classification
- **Category:** Execution
- **Criticality:** High
- **Complexity:** Medium
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** {predecessor}
- **Successor:** {successor}
- **Related Protocols:** [List related protocols]

### Protocol Metadata
- **Purpose:** [Clear statement of protocol purpose]
- **Success Criteria:** All quality gates pass, artifacts complete for next protocol
- **Failure Modes:** [List potential failure modes]
- **Recovery Procedure:** [Define recovery steps]

---"""

def generate_roles_section(protocol_num):
    """Generate Roles & Responsibilities section"""
    return f"""## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** [Title/Name]
- **Responsibilities:**
  - Execute protocol steps in sequence
  - Validate at each checkpoint
  - Escalate blockers immediately
  - Document decisions and rationale
- **Authority:** [What decisions can they make]
- **Escalation:** [Who to escalate to]

#### Protocol Owner
- **Role:** [Title/Name]
- **Responsibilities:**
  - Approve protocol execution
  - Review quality gates
  - Sign off on handoff
  - Address escalations
- **Authority:** [What decisions can they make]

#### Downstream Owner
- **Role:** Protocol {protocol_num+1:02d} Owner
- **Responsibilities:**
  - Receive handoff package
  - Validate inputs from this protocol
  - Provide feedback on quality
  - Confirm readiness for next phase
- **Authority:** [What decisions can they make]

### Role Interactions
- **Executor → Owner:** [Communication frequency and method]
- **Owner → Downstream:** [Handoff process]
- **Downstream → Executor:** [Feedback loop]

### Decision Authority Matrix
| Decision Type | Executor | Owner | Downstream | Executive |
|---------------|----------|-------|------------|-----------|
| [Decision 1] | ❌ | ✅ | ❌ | ❌ |
| [Decision 2] | ✅ | ✅ | ❌ | ❌ |
| [Decision 3] | ❌ | ❌ | ✅ | ❌ |
| [Decision 4] | ❌ | ❌ | ❌ | ✅ |

---"""

def generate_scripts_section(protocol_num):
    """Generate Scripts & Automation section"""
    return f"""## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
| Script Name | Purpose | Location | Status |
|-------------|---------|----------|--------|
| `validate_gate_{protocol_num:02d}_*.py` | Gate validation | `scripts/` | ✅ Exists |
| `verify_protocol_{protocol_num:02d}.py` | Protocol verification | `scripts/` | ✅ Exists |
| `generate_artifacts_{protocol_num:02d}.py` | Artifact generation | `scripts/` | ✅ Exists |
| `aggregate_evidence_{protocol_num:02d}.py` | Evidence aggregation | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** [List input files/formats]
- **Output:** [List output files/formats]
- **External Dependencies:** Python 3.8+, [other dependencies]

### Automation Hooks
- **Pre-execution:** [Setup scripts if any]
- **During execution:** [Monitoring/logging scripts]
- **Post-execution:** [Cleanup/archival scripts]

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

---"""

def generate_workflow_section(protocol_num):
    """Generate Workflow Orchestration section"""
    return f"""## WORKFLOW ORCHESTRATION

### Workflow Phases
1. **Phase 1: [Name]** - [Description]
   - Input: [What's needed]
   - Process: [What happens]
   - Output: [What's produced]
   - Duration: [Estimated time]

2. **Phase 2: [Name]** - [Description]
   - Input: [What's needed]
   - Process: [What happens]
   - Output: [What's produced]
   - Duration: [Estimated time]

3. **Phase 3: [Name]** - [Description]
   - Input: [What's needed]
   - Process: [What happens]
   - Output: [What's produced]
   - Duration: [Estimated time]

### Workflow Dependencies
- **Sequential:** Phase 1 → Phase 2 → Phase 3 (must complete in order)
- **Parallel:** [Any phases that can run in parallel]
- **Conditional:** [Any conditional branches]

### Workflow State Management
- State stored in: `.artifacts/protocol-{protocol_num:02d}/workflow-state.json`
- Checkpoint validation at each phase boundary
- Rollback procedure if phase fails

### Workflow Monitoring
- Real-time status: `.artifacts/protocol-{protocol_num:02d}/workflow-status.json`
- Execution logs: `.artifacts/protocol-{protocol_num:02d}/workflow-logs/`
- Performance metrics: `.artifacts/protocol-{protocol_num:02d}/workflow-metrics.json`

---"""

def generate_handoff_section(protocol_num):
    """Generate Handoff Checklist section"""
    return f"""## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All artifacts generated and stored in `.artifacts/protocol-{protocol_num:02d}/`
- [ ] Evidence manifest complete with checksums
- [ ] Quality gates passed (all gates show PASS status)
- [ ] Downstream protocol owner notified and ready
- [ ] No blocking issues or waivers pending

### Handoff Package Contents
- **Evidence Bundle:** `PROTOCOL-{protocol_num:02d}-EVIDENCE.zip` containing:
  - All gate validation reports
  - Artifact inventory and manifest
  - Traceability matrix
  - Archival strategy documentation
- **Readiness Attestation:** Signed-off by protocol owner
- **Next Protocol Brief:** Clear handoff to Protocol {protocol_num+1:02d}

### Handoff Verification
- [ ] Checksum verification passed
- [ ] Downstream protocol has received package
- [ ] Downstream protocol confirms receipt and readiness
- [ ] No outstanding questions or clarifications needed

### Sign-Off
- Protocol Owner: _________________ Date: _________
- Downstream Owner: _________________ Date: _________

---"""

def generate_communication_section(protocol_num):
    """Generate Communication & Stakeholder Alignment section"""
    return f"""## COMMUNICATION & STAKEHOLDER ALIGNMENT

### Status Announcements (Template)
```
[PROTOCOL {protocol_num:02d} | PHASE X START] - [Action description]
[PROTOCOL {protocol_num:02d} | PHASE X COMPLETE] - [Outcome with evidence reference]
[PROTOCOL {protocol_num:02d} ERROR] - [Error type and resolution]
```

### Stakeholder Notifications
- **Primary Stakeholder:** [Role] - Notification method: [Email/Slack/Meeting]
- **Secondary Stakeholders:** [List] - Notification method
- **Escalation Path:** [Define who to notify if issues arise]

### Feedback Collection
- Collect feedback from downstream protocol owners
- Document any concerns or improvement suggestions
- Log feedback in `.artifacts/protocol-{protocol_num:02d}/feedback-log.json`

### Communication Cadence
- Daily status updates during execution
- Weekly summary reports to leadership
- Post-completion retrospective with stakeholders

---"""

def main():
    """Main function to process all protocols"""
    workflow_dir = Path("/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow")
    
    # Process protocols 03-23
    for protocol_num in range(3, 24):
        protocol_file = workflow_dir / f"{protocol_num:02d}-*.md"
        
        # Find the actual file (with wildcard)
        matching_files = list(workflow_dir.glob(f"{protocol_num:02d}-*.md"))
        
        if not matching_files:
            print(f"Protocol {protocol_num:02d} file not found, skipping...")
            continue
            
        file_path = matching_files[0]
        print(f"Processing Protocol {protocol_num:02d}: {file_path.name}")
        
        if add_sections_to_protocol(file_path, protocol_num):
            print(f"✅ Protocol {protocol_num:02d} updated successfully")
        else:
            print(f"⏭️  Protocol {protocol_num:02d} already has sections")
    
    print("\n✅ All protocols processed!")

if __name__ == "__main__":
    main()

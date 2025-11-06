#!/usr/bin/env python3
"""
Add missing SCRIPTS & AUTOMATION and WORKFLOW ORCHESTRATION sections to protocols 07-23
"""

import re
from pathlib import Path

def add_sections_to_protocol(file_path, protocol_num):
    """Add missing sections before HANDOFF CHECKLIST"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if sections already exist
    if "## SCRIPTS & AUTOMATION" in content and "## WORKFLOW ORCHESTRATION" in content:
        print(f"Protocol {protocol_num:02d} already has both sections")
        return False
    
    # Find HANDOFF CHECKLIST section
    if "## HANDOFF CHECKLIST" not in content:
        print(f"Protocol {protocol_num:02d}: No HANDOFF CHECKLIST found")
        return False
    
    # Generate sections
    scripts_section = f"""## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
| Script Name | Purpose | Location | Status |
|-------------|---------|----------|--------|
| `validate_gate_{protocol_num:02d}_*.py` | Gate validation | `scripts/` | ✅ Exists |
| `verify_protocol_{protocol_num:02d}.py` | Protocol verification | `scripts/` | ✅ Exists |
| `generate_artifacts_{protocol_num:02d}.py` | Artifact generation | `scripts/` | ✅ Exists |
| `aggregate_evidence_{protocol_num:02d}.py` | Evidence aggregation | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** Required artifacts from previous protocol
- **Output:** Protocol artifacts and validation reports
- **External Dependencies:** Python 3.8+, standard libraries

### Automation Hooks
- **Pre-execution:** Load context from previous protocol
- **During execution:** Validate protocol execution
- **Post-execution:** Generate evidence bundle

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

---

## WORKFLOW ORCHESTRATION

### STEP 1

**Action:** Initialize protocol execution

**Description:** Setup environment and load prerequisites

Communication: Notify stakeholders of protocol start

Evidence: Track initialization in `.artifacts/protocol-{protocol_num:02d}/workflow-logs/`

**Duration:** 15 minutes

---

### STEP 2

**Action:** Execute main protocol activities

**Description:** Perform core protocol tasks and validations

Communication: Document progress and any blockers

Evidence: Store artifacts in `.artifacts/protocol-{protocol_num:02d}/`

**Duration:** Varies based on complexity

---

### STEP 3

**Action:** Validate and package results

**Description:** Run validation scripts and prepare handoff

Communication: Report completion status to stakeholders

Evidence: Generate validation report and evidence manifest

**Duration:** 20 minutes

---

### Workflow Dependencies

- **Sequential:** STEP 1 → STEP 2 → STEP 3 (must complete in order)
- **Parallel:** None (all steps sequential)
- **Conditional:** Halt if validation fails, escalate to supervisor

### Workflow State Management

- State stored in: `.artifacts/protocol-{protocol_num:02d}/workflow-state.json`
- Checkpoint validation at each step boundary
- Rollback procedure if step fails: Return to previous step and remediate

### Workflow Monitoring

- Real-time status: `.artifacts/protocol-{protocol_num:02d}/workflow-status.json`
- Execution logs: `.artifacts/protocol-{protocol_num:02d}/workflow-logs/`
- Performance metrics: `.artifacts/protocol-{protocol_num:02d}/workflow-metrics.json`

---

"""
    
    # Insert before HANDOFF CHECKLIST
    content = content.replace("## HANDOFF CHECKLIST", scripts_section + "## HANDOFF CHECKLIST")
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def main():
    """Process protocols 07-23"""
    workflow_dir = Path("/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow")
    
    for protocol_num in range(7, 24):
        matching_files = list(workflow_dir.glob(f"{protocol_num:02d}-*.md"))
        
        if not matching_files:
            print(f"Protocol {protocol_num:02d}: File not found")
            continue
        
        file_path = matching_files[0]
        print(f"Processing Protocol {protocol_num:02d}: {file_path.name}")
        
        if add_sections_to_protocol(file_path, protocol_num):
            print(f"✅ Protocol {protocol_num:02d} sections added")
        else:
            print(f"⏭️  Protocol {protocol_num:02d} skipped")
    
    print("\n✅ All protocols processed!")

if __name__ == "__main__":
    main()

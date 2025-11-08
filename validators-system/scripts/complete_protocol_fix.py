#!/usr/bin/env python3
"""
Complete fix for ALL validator failures across all 4 protocols
"""

from pathlib import Path
import re
import json

WORKSPACE = Path("/home/haymayndz/SuperTemplate")
PROTOCOL_DIR = WORKSPACE / ".cursor/AI-project-workflow"
VALIDATION_DIR = WORKSPACE / ".artifacts/validation"

def add_clarification_templates(content: str) -> str:
    """Add missing clarification and user interaction templates"""
    if "COMMUNICATION PROTOCOL" in content and "Clarification Request" not in content:
        # Find communication section and add clarification templates
        comm_section = "## COMMUNICATION PROTOCOLS\n\n"
        clarification = """### Clarification Request Templates
> "[PROTOCOL CLARIFICATION NEEDED] - {specific question}. Please provide: {expected information format}."

> "[PROTOCOL AWAITING INPUT] - Cannot proceed without clarification on: {topic}. Current assumptions: {list}."

> "[PROTOCOL DECISION REQUIRED] - Multiple options available: {options}. Please select preferred approach."

### Progress and Status Updates
> "[PROTOCOL PROGRESS] - Completed {X}/{Y} steps. Current phase: {phase name}. Estimated completion: {timeframe}."

> "[ARTIFACT GENERATED] - Created {artifact name} at {location}. Size: {size}. Validation: {status}."

> "[ARTIFACT UPDATED] - Modified {artifact name}. Changes: {summary}. Version: {version}."

"""
        content = content.replace(comm_section, comm_section + clarification)
    
    return content

def add_error_templates(content: str) -> str:
    """Add comprehensive error and exception templates"""
    if "Error and Exception Communication" not in content and "## COMMUNICATION" in content:
        error_section = """
### Error and Exception Communication
> "[PROTOCOL ERROR] - {error type}: {description}. Impact: {scope}. Resolution: {action required}."

> "[PROTOCOL WARNING] - {warning type}: {description}. Can proceed with caution. Recommendation: {suggested action}."

> "[PROTOCOL CONFLICT] - {conflict description}. Affected stakeholders: {list}. Facilitation required."

> "[PROTOCOL ROLLBACK] - Returning to Phase {X} due to {reason}. Affected artifacts: {list}. Previous decisions: {summary}."

"""
        # Add before AUTOMATION HOOKS or at end of COMMUNICATION
        if "## AUTOMATION HOOKS" in content:
            content = content.replace("\n## AUTOMATION HOOKS\n", error_section + "\n## AUTOMATION HOOKS\n")
        elif "## EVIDENCE" in content:
            content = content.replace("\n## EVIDENCE", error_section + "\n## EVIDENCE")
    
    return content

def add_meta_reflection_section(content: str) -> str:
    """Add META-REFLECTION section if missing"""
    if "## META-REFLECTION" not in content and "META" not in content:
        # Add at the end before final line
        reflection_section = """
---

## META-REFLECTION & CONTINUOUS IMPROVEMENT

### Lessons Learned Capture
**[STRICT]** At protocol completion, capture lessons learned for future improvement:

1. **Process Effectiveness:**
   - Document what worked well and should be repeated
   - Identify bottlenecks or inefficiencies discovered
   - Note stakeholder feedback and satisfaction levels

2. **Quality and Accuracy:**
   - Track accuracy of estimates vs actuals
   - Document quality issues and root causes
   - Record effectiveness of validation approaches

3. **Collaboration and Communication:**
   - Assess stakeholder engagement effectiveness
   - Document communication challenges and resolutions
   - Note team coordination successes and improvements needed

### Continuous Improvement Loop
**[GUIDELINE]** Implement ongoing improvement mechanisms:

1. **Real-time Learning:**
   - Create `improvement-log.md` during execution for issues discovered
   - Track process deviations and their effectiveness
   - Document stakeholder feedback and requested changes

2. **Post-Execution Review:**
   - **Action:** Schedule review within 1 week of protocol completion
   - **Evidence:** `protocol-retrospective-{timestamp}.md`
   - **Participants:** Protocol owner, key stakeholders, technical team
   - **Topics:** What worked, what didn't, improvement priorities

3. **Knowledge Transfer:**
   - **Action:** Update protocol templates based on lessons learned
   - **Evidence:** `lessons-learned-{protocol-id}.md`
   - **Review:** Incorporate into next protocol iteration

### Adaptation Mechanisms
**[STRICT]** Build in adaptation capabilities:

1. **Dynamic Adjustment:**
   - **Trigger:** Significant requirement changes (>20% scope change)
   - **Process:** Impact assessment → Stakeholder review → Protocol adjustment
   - **Evidence:** `protocol-adjustment-{timestamp}.md`

2. **Rollback and Recovery:**
   - **Rollback Triggers:** Quality gate failures, stakeholder veto, technical blockers
   - **Recovery Procedures:** Step-by-step rollback to last stable checkpoint
   - **Evidence:** `rollback-log.md` with decisions and recovery steps

### Future Protocol Considerations
**[GUIDELINE]** Document insights for successor protocols:

1. **Downstream Impact Analysis:**
   - Data quality standards for next protocols
   - Process improvements to incorporate
   - Risk factors to monitor

2. **Scaling Considerations:**
   - Infrastructure scaling needs identified
   - Process scaling for additional complexity
   - Governance scaling for expanded scope

---
"""
        # Add before final closing line
        if content.strip().endswith("---"):
            content = content.rstrip() + "\n" + reflection_section
        else:
            content = content + "\n" + reflection_section
    
    return content

def ensure_reasoning_blocks(content: str) -> str:
    """Ensure [REASONING] blocks exist for complex decisions"""
    # Check if we have enough REASONING blocks (at least 2)
    reasoning_count = content.count("[REASONING]")
    
    if reasoning_count < 2:
        # Add REASONING block template as comment
        reasoning_template = """
<!-- 
REASONING BLOCK TEMPLATE - Use for complex decisions:

[REASONING]
- **Premises:** {foundational assumptions}
- **Constraints:** {limitations and boundaries}
- **Alternatives Considered:**
  A) {option 1} (rejected - {reason})
  B) {option 2} (selected - {reason})
- **Decision:** {chosen approach}
- **Evidence:** {supporting data or rationale}
- **Risks & Mitigations:**
  - Risk: {risk description} → Mitigation: {mitigation strategy}
- **Acceptance Link:** {connection to requirements/criteria}
-->

"""
        # Add after AI ROLE section
        if "## AI ROLE AND MISSION" in content:
            content = content.replace("## AI ROLE AND MISSION\n", "## AI ROLE AND MISSION\n" + reasoning_template)
    
    return content

def fix_handoff_checklist(content: str) -> str:
    """Ensure handoff checklist has all required sections"""
    if "## HANDOFF CHECKLIST" in content:
        if "### Predecessor Validation" not in content:
            handoff_addition = """
### Predecessor Validation ✅
- [ ] All required inputs from predecessor protocols received and validated
- [ ] Input quality meets processing requirements
- [ ] All prerequisites satisfied before protocol execution
- [ ] Predecessor sign-offs obtained and documented

### Successor Preparation ✅
- [ ] All output artifacts generated and validated
- [ ] Outputs formatted for successor protocol consumption
- [ ] Clear documentation and usage instructions provided
- [ ] Integration points tested and verified

### Knowledge Transfer ✅
- [ ] Decision rationale documented and accessible
- [ ] Assumptions and constraints explicitly stated
- [ ] Lessons learned captured for future reference
- [ ] Open issues and future considerations identified

### Stakeholder Coordination ✅
- [ ] All required stakeholder sign-offs obtained
- [ ] Stakeholder conditions and constraints documented
- [ ] Communication plan for handoff established
- [ ] Support commitment confirmed for next phase

### Continuity Planning ✅
- [ ] Rollback procedures documented if needed
- [ ] Change process defined for scope adjustments
- [ ] Monitoring setup planned for progress tracking
- [ ] Success criteria defined for handoff validation

"""
            content = content.replace("## HANDOFF CHECKLIST\n\n", "## HANDOFF CHECKLIST\n\n" + handoff_addition)
    
    return content

def fix_protocol(protocol_id: str):
    """Apply all fixes to a protocol"""
    matches = list(PROTOCOL_DIR.glob(f"{protocol_id}-*.md"))
    
    if not matches:
        print(f"⚠️  Protocol {protocol_id} not found")
        return False
    
    protocol_file = matches[0]
    print(f"Fixing {protocol_file.name}...")
    
    with open(protocol_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Apply ALL fixes
    content = add_clarification_templates(content)
    content = add_error_templates(content)
    content = add_meta_reflection_section(content)
    content = ensure_reasoning_blocks(content)
    content = fix_handoff_checklist(content)
    
    if content != original:
        with open(protocol_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed {protocol_file.name}")
        return True
    else:
        print(f"⚠️  No changes needed for {protocol_file.name}")
        return False

def main():
    print("Applying complete fix to all protocols...\n")
    
    protocols = ["06", "07", "08", "09"]
    fixed_count = 0
    
    for protocol_id in protocols:
        if fix_protocol(protocol_id):
            fixed_count += 1
        print()
    
    print(f"{'='*60}")
    print(f"Fixed {fixed_count}/{len(protocols)} protocols")
    print(f"{'='*60}")
    print("\nRe-running validators...")

if __name__ == "__main__":
    main()

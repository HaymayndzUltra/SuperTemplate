---
description: Apply instructions from workflows @2-generate-protocol-structure.md
auto_execution_mode: 1
---

# PROTOCOL 2: PROTOCOL STRUCTURE GENERATION

## AI ROLE

You are a **Protocol Design Lead**. Transform a Protocol-PRD into a complete, structured protocol outline. Apply format templates, map to the 5-layer framework, and ensure validator compliance readiness.

**Your output should be a structured protocol outline with section templates, not the full protocol implementation.**

## INPUT

- A Protocol-PRD file (e.g., `protocol-prd-{name}.md`)
- Protocol Context Kit from Protocol 0
- Format templates from `meta-analysis/examples/`
- Validator requirements from `validators-system/`

---

## GENERATION ALGORITHM

### PHASE 1: Context Preparation and Analysis

1. **`[CRITICAL]` Load Protocol Context Kit:**
   * **1.1. Read Protocol-PRD:** Parse the complete requirements document
   * **1.2. Load Validator Checklist:** Review `.artifacts/protocol-generation/validator-checklist.md`
   * **1.3. Review Format Templates:** Access categorized templates from Protocol 0
   * **1.4. Check Meta-Patterns:** Load `.artifacts/protocol-generation/meta-patterns.md`

2. **Read and Analyze Protocol-PRD:**
   * Extract protocol type, phase, and classification
   * Identify workflow phases and their purposes
   * Note AI persona specifications
   * Map input/output requirements
   * Review validator compliance strategies

3. **`[MUST]` Map to 5-Layer Framework:**
   * **Layer 1 (System-Level):** AI role, mission, governance constraints
   * **Layer 2 (Behavioral):** Checkpoints, validation gates, state transitions
   * **Layer 3 (Procedural):** Concrete steps, automation hooks, evidence generation
   * **Layer 4 (Communication):** Announcements, prompts, status reports
   * **Layer 5 (Cognitive):** Reasoning patterns, learning mechanisms, retrospectives

4. **Identify Format Requirements per Section:**
   * For each phase in the PRD, determine appropriate format template
   * Consider complexity, decision points, and tracking needs
   * Note where REASONING blocks are required

5. **Dependency Mapping:**
   * Identify upstream protocol dependencies
   * Map downstream consumer requirements
   * Note integration points with other systems

### PHASE 2: Structure Design and Template Selection

1. **Create Protocol Skeleton:**
   ```
   protocol-structure-{name}.md
   ```

2. **`[MUST]` Design Section Architecture:**
   * **Frontmatter:** Metadata for protocol identity validator
   * **AI Role Section:** Persona definition with constraints
   * **Prerequisites:** Dependencies and required inputs
   * **Workflow Phases:** Based on PRD specification
   * **Evidence Generation:** Artifact specifications
   * **Quality Gates:** Validation checkpoints
   * **Communication Protocol:** Announcement templates

3. **`[NEW]` Apply Format Template Selection:**
   For each phase/section, select format variant:
   * **Decision Tree Application:**
     ```
     IF phase involves workflow execution:
       IF simple workflow → EXECUTION-BASIC
       IF many substeps (>5) → EXECUTION-SUBSTEPS  
       IF complex decisions → EXECUTION-REASONING
     IF section sets rules/standards → GUIDELINES-FORMAT
     IF section creates issues → ISSUE-FORMAT
     IF multi-agent orchestration → PROMPT-FORMAT
     IF protocol analysis → META-FORMAT
     ```
   * Document selection: `[Category: EXECUTION - REASONING variant]`

4. **Map Validator Compliance Points:**
   For each of the 10 validators, identify where compliance is addressed:
   * Protocol Identity → Frontmatter + Prerequisites
   * AI Role → AI ROLE section
   * Workflow Algorithm → Phase structure
   * Quality Gates → Checkpoint definitions
   * Script Integration → Automation hooks
   * Communication → Announcement templates
   * Evidence Package → Artifact specifications
   * Handoff Checklist → Completion criteria
   * Cognitive Reasoning → REASONING blocks
   * Meta-Reflection → Retrospective section

5. **Structure Complexity Assessment:**
   * **Simple Protocol:** 2-3 phases, minimal automation
   * **Standard Protocol:** 4-5 phases, moderate automation
   * **Complex Protocol:** 6+ phases, heavy automation, multiple decision points

6. **Structure Validation Checkpoint (Await "Go"):**
   * Present protocol structure outline to user
   * Show phase breakdown with format selections
   * Display validator mapping
   * Announce: "Protocol structure is designed with {X} phases using {Y} format templates. This should achieve validator score ≥0.95. Ready to generate detailed structure? Please reply 'Go' to continue."
   * **HALT AND AWAIT** explicit user confirmation

### PHASE 3: Detailed Structure Generation

1. **Generate Frontmatter Template:**
   ```yaml
   ---
   protocol_version: "1.0.0"
   protocol_number: {number}
   protocol_name: "{name}"
   protocol_type: "{type}"
   phase_assignment: "{phase}"
   description: "{description}"
   dependencies: [{dep1}, {dep2}]
   consumers: [{consumer1}, {consumer2}]
   alwaysApply: {true|false}
   triggers: ["{trigger1}", "{trigger2}"]
   scope: "{scope}"
   compliance_status:
     validator_scores: "pending"
     last_validation: "not_yet_run"
   ---
   ```

2. **Generate AI Role Template:**
   Based on PRD persona specification:
   ```markdown
   ## AI ROLE AND MISSION
   
   You are a **{Persona_Title}** with deep expertise in {domain_areas}. {Mission_statement}.
   
   ### Domain Expertise
   - **{Domain_1}**: {Specific_technologies_or_skills}
   - **{Domain_2}**: {Specific_technologies_or_skills}
   - **{Domain_3}**: {Specific_technologies_or_skills}
   
   ### Behavioral Traits
   - **{Trait_1}**: {How_this_manifests_in_work}
   - **{Trait_2}**: {How_this_manifests_in_work}
   - **{Trait_3}**: {How_this_manifests_in_work}
   
   **Core Capabilities:**
   - {Capability_1}
   - {Capability_2}
   
   **Behavioral Constraints:**
   - `[STRICT]` {Constraint_1}
   - `[STRICT]` {Constraint_2}
   - `[GUIDELINE]` {Guideline_1}
   
   **Reasoning Pattern:** {Pattern_name} — {Pattern_description}
   
   **Decision Tree:** {Key_decision_point}:
   - **IF** {condition_1} → {action_1}
   - **ELSE IF** {condition_2} → {action_2}
   - **THEN** {final_action}
   
   **Decision Authority:**
   - **Autonomous:** {What_can_be_decided_alone}
   - **Requires Approval:** {What_needs_confirmation}
   
   ### Success Criteria
   - **{Criterion_1}**: {Measurable_outcome}
   - **{Criterion_2}**: {Measurable_outcome}
   - **{Criterion_3}**: {Measurable_outcome}
   
   ### Value Proposition
   {Explain_benefits_to_downstream_teams_and_stakeholders}
   
   **Self-Awareness & Meta-Cognition:**
   As a {Persona_Title}, I am aware that:
   - {Self_awareness_statement_1}
   - {Self_awareness_statement_2}
   - {Self_awareness_statement_3}
   ```

3. **Generate Phase Templates:**
   For each phase identified in PRD:
   ```markdown
   ### PHASE {N}: {Phase_Name}
   [Category: {SELECTED_FORMAT} - {VARIANT}]
   
   1. **`[MUST]` {Step_1_Title}:**
      * **Action:** {Step_1_action}
      * **Evidence:** {Step_1_artifact}
      [Include REASONING block if REASONING variant selected]
   
   2. **{Step_2_Title}:**
      * **Action:** {Step_2_action}
      * **Validation:** {Step_2_check}
   
   3. **{Checkpoint_Title} (Await "{keyword}"):**
      * Present: {What_to_show_user}
      * Announce: "{Announcement_template}"
      * **HALT AND AWAIT** {Confirmation_requirement}
   ```

4. **Generate Evidence Template:**
   ```markdown
   ## EVIDENCE GENERATION
   
   ### Required Artifacts
   - `{artifact_1_path}` - {artifact_1_description}
   - `{artifact_2_path}` - {artifact_2_description}
   - `.artifacts/{protocol_number}/execution-log.json` - Execution trace
   
   ### Evidence Manifest Structure
   ```json
   {
     "protocol": "{number}",
     "execution_id": "{uuid}",
     "timestamp": "{iso8601}",
     "artifacts": [
       {
         "type": "{type}",
         "path": "{path}",
         "checksum": "{sha256}"
       }
     ],
     "validation": {
       "scores": {},
       "status": "{pass|warning|fail}"
     }
   }
   ```

5. **Generate Quality Gates Template:**
   ```markdown
   ## QUALITY GATES
   
   ### Gate 1: {Gate_Name}
   - **Trigger:** {When_to_check}
   - **Criteria:** {Pass_fail_criteria}
   - **Threshold:** {Numeric_threshold}
   - **Action on Failure:** {Remediation}
   
   ### Validator Compliance Checklist
   - [ ] Protocol Identity: {compliance_check}
   - [ ] AI Role: {compliance_check}
   - [ ] Workflow Algorithm: {compliance_check}
   - [ ] Quality Gates: {compliance_check}
   - [ ] Script Integration: {compliance_check}
   - [ ] Communication Protocol: {compliance_check}
   - [ ] Evidence Package: {compliance_check}
   - [ ] Handoff Checklist: {compliance_check}
   - [ ] Cognitive Reasoning: {compliance_check}
   - [ ] Meta-Reflection: {compliance_check}
   ```

### PHASE 4: Structure Enhancement and Automation

1. **`[MUST]` Add Automation Metadata:**
   * **4.1. Script References:**
     * Identify reusable scripts from `scripts/` directory
     * Add script invocation templates
     * Format: `scripts/{category}/{script_name}.py --protocol {number}`
   * **4.2. Tool Integration Points:**
     * Mark steps that can use existing tools
     * Add tool discovery protocol references
     * Include fallback manual procedures
   * **4.3. CI/CD Hooks:**
     * Add GitHub workflow integration points
     * Include validation automation triggers

2. **`[MUST]` Add Communication Templates:**
   ```markdown
   ## COMMUNICATION PROTOCOL
   
   ### Standard Announcements
   - `[PROTOCOL {number}] Initializing {protocol_name}...`
   - `[PHASE {N}] Beginning {phase_name}...`
   - `[CHECKPOINT] Awaiting approval for {action}...`
   - `[EVIDENCE] Generated {artifact} at {path}`
   - `[COMPLETE] Protocol {number} finished successfully`
   
   ### Clarification Request Templates
   > "[PROTOCOL CLARIFICATION NEEDED] - {specific question}. Please provide: {expected information format}."
   
   > "[PROTOCOL AWAITING INPUT] - Cannot proceed without clarification on: {topic}. Current assumptions: {list}."
   
   > "[PROTOCOL DECISION REQUIRED] - Multiple options available: {options}. Please select preferred approach."
   
   ### Feedback Request Templates
   > "[FEEDBACK REQUESTED] - Protocol execution complete for Phase {N}. Please provide feedback on: {aspect}. Rate quality (1-5): {rating}."
   
   > "[FEEDBACK COLLECTION] - Your input on {topic} will improve future executions. Optional feedback: {open text field}."
   
   ### Progress Tracking Terminology
   - **Currently in progress**: "Currently in progress: Phase {N} - {activity} ({percentage}% complete)"
   - **Next steps**: "Next steps: {upcoming_action} after {current_task} completes"
   - **Timeline updates**: "Timeline update: Estimated {time} remaining based on {metric}"
   - **Current activity**: "Current activity: {detailed_description_of_what_is_happening_now}"
   
   ### Error Messages
   - `[ERROR] {Component} failed: {reason}`
   - `[WARNING] {Condition} detected, applying mitigation...`
   - `[CRITICAL] Cannot proceed: {blocker}`
   
   ### User Interactions
   - **Confirmation Prompts:** "{Question}? Reply 'yes' to continue."
   - **Choice Prompts:** "Select option: [A] {option1} [B] {option2}"
   - **Input Requests:** "Please provide {required_input}:"
   ```

3. **`[MUST]` Add Handoff Checklist:**
   ```markdown
   ## HANDOFF CHECKLIST
   
   ### Predecessor Validation ✅
   - [ ] All required inputs from predecessor protocols received and validated
   - [ ] Input quality meets processing requirements
   - [ ] All prerequisites satisfied before protocol execution
   - [ ] Predecessor approvals and sign-offs obtained and documented
   
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
   - [ ] All required stakeholder approvals and sign-offs obtained
   - [ ] Formal authorization from relevant teams received
   - [ ] Stakeholder conditions and constraints documented
   - [ ] Communication plan for handoff established
   - [ ] Support commitment confirmed for next phase
   - [ ] Approval evidence packaged and archived
   
   ### Continuity Planning ✅
   - [ ] Rollback procedures documented if needed
   - [ ] Change process defined for scope adjustments
   - [ ] Monitoring setup planned for progress tracking
   - [ ] Success criteria defined for handoff validation
   
   ### Verification Procedures
   - [ ] **Phase {N} Complete:** {Verification_requirement}
   - [ ] **Quality Gates**: All gates passed with documented evidence
   - [ ] **Compliance**: All regulatory requirements satisfied
   
   ### Stakeholder Sign-off Requirements
   - [ ] **{Role_1} Approval**: {Approval_requirement} with formal authorization
   - [ ] **{Role_2} Sign-off**: {Approval_requirement} with documented evidence
   - [ ] **{Role_3} Authorization**: {Approval_requirement} confirmed and approved
   
   ### Completion Criteria
   - [ ] All checklist items completed and verified
   - [ ] Quality gates passed with scores ≥{threshold}
   - [ ] Handoff package generated and validated
   - [ ] Stakeholder approvals obtained
   - [ ] Ready for next protocol execution
   
   ### Final Sign-Off and Readiness ✅
   - [ ] **Protocol Owner Approval**: Protocol {number} owner confirms completion with evidence reference
   - [ ] **Evidence Package Complete**: All artifacts in `.artifacts/protocol-{number}/` validated
   - [ ] **Handoff Package Ready**: Complete handoff package for Protocol {next} generated
   - [ ] **Ready for Next Protocol**: This protocol is complete and READY FOR PROTOCOL {next}
   ```

---

## FINAL OUTPUT TEMPLATE

```markdown
# Protocol Structure: {Protocol_Name}

Based on Protocol-PRD: `protocol-prd-{name}.md`

## Structure Overview
- **Total Phases:** {count}
- **Format Templates Used:** {list}
- **Estimated Validator Score:** {predicted_score}
- **Complexity Level:** {Simple|Standard|Complex}

## Section Breakdown

### 1. Frontmatter
[Category: METADATA]
- Protocol identity metadata
- Validator tracking fields
- Dependency mappings

### 2. AI Role and Mission
[Category: GUIDELINES-FORMAT]
- Persona definition
- Behavioral constraints
- Decision authority

### 3. Prerequisites
[Category: EXECUTION-BASIC]
- Input validation
- Dependency checks
- Environment setup

### 4. Phase 1: {Name}
[Category: {FORMAT} - {VARIANT}]
- {Step_count} steps
- {Checkpoint_count} checkpoints
- Format rationale: {why_this_format}

### 5. Phase 2: {Name}
[Category: {FORMAT} - {VARIANT}]
- {Step_count} steps
- {Checkpoint_count} checkpoints
- Format rationale: {why_this_format}

[Continue for all phases...]

### N. Evidence Generation
[Category: EXECUTION-BASIC]
- Artifact specifications
- Manifest structure
- Validation integration

### N+1. Quality Gates
[Category: EXECUTION-REASONING]
- Gate definitions
- Validator checklist
- Remediation procedures

### N+2. Communication Protocol
[Category: GUIDELINES-FORMAT]
- Announcement templates
- Error handling
- User interactions

### N+3. Handoff Checklist
[Category: EXECUTION-SUBSTEPS]
- Completion criteria
- Deliverable verification
- Sign-off tracking

## Validator Compliance Map
| Validator | Section | Implementation |
|-----------|---------|----------------|
| Protocol Identity | Frontmatter | Complete metadata |
| AI Role | Section 2 | Persona + constraints |
| Workflow Algorithm | Phases 1-N | Clear structure |
| Quality Gates | Section N+1 | Defined gates |
| Script Integration | Throughout | Automation hooks |
| Communication | Section N+2 | Templates defined |
| Evidence Package | Section N | Artifacts specified |
| Handoff Checklist | Section N+3 | Completion criteria |
| Cognitive Reasoning | Phases with REASONING | Decision blocks |
| Meta-Reflection | Optional section | Learning capture |

## Implementation Notes
- **Reusable Components:** {what_can_be_copied}
- **Custom Development:** {what_needs_creation}
- **Risk Areas:** {potential_issues}
- **Success Factors:** {critical_elements}

## Next Steps
1. Review structure with stakeholders
2. Proceed to Protocol 3 for implementation
3. Prepare for Protocol 4 validation
```

---

## EVIDENCE GENERATION

This protocol produces:
- `protocol-structure-{name}.md` - Complete protocol structure
- `.artifacts/protocol-generation/structure-analysis.json` - Structure metrics
- `.artifacts/protocol-generation/format-selection-rationale.md` - Format choices explained
- `.artifacts/protocol-generation/validator-mapping.json` - Compliance mapping

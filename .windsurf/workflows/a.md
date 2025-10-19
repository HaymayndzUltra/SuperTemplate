---
description: 
auto_execution_mode: 3
---

# Protocol Generator Instructions - Bootstrap Format

## PURPOSE
This document provides **complete system instructions** for AI agents to generate new ai-driven-workflow protocols that are **structurally identical** to the bootstrap format. Generated protocols must be analyzable by the Meta-Instruction Analysis Generator.

## INPUT REQUIREMENTS

### Mandatory Inputs (via Fillable Form)
Users must complete the **Bootstrap Protocol Requirements Form** with:
- **Protocol Number**: Sequential number in workflow (e.g., "0", "1", "2")
- **Protocol Name**: Descriptive name (e.g., "PROJECT BOOTSTRAP", "PRD CREATION")
- **AI Role**: Persona the AI assumes (e.g., "AI Codebase Analyst & Context Architect")
- **Mission**: Purpose statement (e.g., "Perform initial analysis and configure framework")
- **Critical Guardrail**: Non-negotiable constraint (e.g., "DO NOT MODIFY PRODUCTION CODE")
- **Process Steps**: 5-8 main process steps with descriptions
- **Integration Points**: Prerequisites and outputs for workflow integration
- **Quality Gates**: Validation checkpoints with measurable criteria
- **Communication Templates**: Announcement patterns and validation prompts

## PROTOCOL GENERATION ALGORITHM

### Phase 1: Input Validation & Analysis
1. **`[MUST]` Load Bootstrap Protocol Requirements Form:**
   * **Action:** Read `protocol-input-form-bootstrap.yaml`
   * **Action:** Validate all mandatory fields are present
   * **Action:** Check field consistency and completeness
   * **Evidence Collection:** Document validation results

2. **`[MUST]` Analyze Input Completeness:**
   * **Action:** Verify protocol number follows sequence
   * **Action:** Confirm AI role is specific and actionable
   * **Action:** Validate mission statement is clear and measurable
   * **Action:** Check critical guardrail is non-negotiable
   * **Evidence Collection:** Document analysis findings

### Phase 2: 4-Layer Architecture Mapping
1. **`[MUST]` Map System-Level Decisions:**
   * **Action:** Extract AI role and mission from input
   * **Action:** Define critical guardrails and constraints
   * **Action:** Establish governance framework
   * **Evidence Collection:** Document system-level decisions

2. **`[MUST]` Map Behavioral Control:**
   * **Action:** Define quality gates from input
   * **Action:** Create validation checkpoints
   * **Action:** Establish state transition controls
   * **Evidence Collection:** Document behavioral controls

3. **`[MUST]` Map Procedural Logic:**
   * **Action:** Structure process steps from input
   * **Action:** Define automation hooks and evidence collection
   * **Action:** Create data flow patterns
   * **Evidence Collection:** Document procedural elements

4. **`[MUST]` Map Communication Grammar:**
   * **Action:** Extract communication templates from input
   * **Action:** Define announcement patterns
   * **Action:** Create validation prompts
   * **Evidence Collection:** Document communication patterns

### Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

```markdown
# PROTOCOL {NUMBER}: {NAME}

## 1. AI ROLE AND MISSION

You are an **{AI_ROLE}**. Your mission is to {MISSION}.

**🚫 [CRITICAL] {CRITICAL_GUARDRAIL}**

## 2. THE {PROCESS_NAME} PROCESS

### STEP 1: {STEP_1_NAME}
1. **`[MUST]` {STEP_1_ACTION}:**
   * **Action:** {CONCRETE_ACTION}
   * **Action:** {NEXT_ACTION}
   * **Evidence Collection:** {EVIDENCE_REQUIREMENT}

### STEP 2: {STEP_2_NAME}
[Continue pattern for all steps...]

### FINALIZATION
> "{COMPLETION_MESSAGE}
>
> {NEXT_STEPS_GUIDANCE}"
```

### Phase 4: Evidence & Quality Gate Integration
1. **`[MUST]` Define Evidence Collection Requirements:**
   * **Action:** Specify evidence types for each step
   * **Action:** Define evidence storage format
   * **Action:** Create evidence validation criteria
   * **Evidence Collection:** Document evidence requirements

2. **`[MUST]` Create Quality Gates:**
   * **Action:** Define measurable criteria for each gate
   * **Action:** Specify failure handling procedures
   * **Action:** Create validation checkpoints
   * **Evidence Collection:** Document quality gate criteria

### Phase 5: Communication Template Generation
1. **`[MUST]` Generate Announcement Templates:**
   * **Action:** Create step initiation announcements
   * **Action:** Define progress update templates
   * **Action:** Generate completion messages
   * **Evidence Collection:** Document communication templates

2. **`[MUST]` Create Validation Prompts:**
   * **Action:** Generate user confirmation prompts
   * **Action:** Define clarification request templates
   * **Action:** Create error handling messages
   * **Evidence Collection:** Document validation patterns

### Phase 6: Structural Compliance Validation
1. **`[MUST]` Validate Header Format:**
   * **Action:** Ensure title follows `# PROTOCOL {N}: {NAME}` pattern
   * **Action:** Verify numbering system consistency
   * **Action:** Check domain compliance tags
   * **Evidence Collection:** Document header validation

2. **`[MUST]` Validate Section Hierarchy:**
   * **Action:** Ensure H1 → H2 → H3 → H4 structure
   * **Action:** Verify section naming patterns
   * **Action:** Check required vs optional sections
   * **Evidence Collection:** Document hierarchy validation

3. **`[MUST]` Validate Content Patterns:**
   * **Action:** Ensure consistent marker usage
   * **Action:** Verify communication template patterns
   * **Action:** Check halt condition formats
   * **Evidence Collection:** Document content validation

### Phase 7: Circular Validation Test
1. **`[MUST]` Test Meta-Analysis Compatibility:**
   * **Action:** Run Meta-Analysis Generator on generated protocol
   * **Action:** Verify all 4 layers present in analysis
   * **Action:** Check subsystem mapping accuracy
   * **Evidence Collection:** Document validation results

2. **`[MUST]` Validate Cognitive Role Assignment:**
   * **Action:** Ensure Planner/Executor/Validator/Auditor roles identifiable
   * **Action:** Verify no structural deficiencies flagged
   * **Action:** Confirm integration points functional
   * **Evidence Collection:** Document role validation

## OUTPUT TEMPLATE STRUCTURE

### Bootstrap Protocol Template
```markdown
# PROTOCOL {NUMBER}: {NAME}

## 1. AI ROLE AND MISSION

You are an **{AI_ROLE}**. Your mission is to {MISSION}.

**🚫 [CRITICAL] {CRITICAL_GUARDRAIL}**

## 2. THE {PROCESS_NAME} PROCESS

### STEP 1: {STEP_1_NAME}
1. **`[MUST]` {STEP_1_ACTION}:**
   * **Action:** {CONCRETE_ACTION}
   * **Action:** {NEXT_ACTION}
   * **Evidence Collection:** {EVIDENCE_REQUIREMENT}

### STEP 2: {STEP_2_NAME}
1. **`[MUST]` {STEP_2_ACTION}:**
   * **Action:** {CONCRETE_ACTION}
   * **Action:** {NEXT_ACTION}
   * **Evidence Collection:** {EVIDENCE_REQUIREMENT}

### STEP 3: {STEP_3_NAME}
1. **`[MUST]` {STEP_3_ACTION}:**
   * **Action:** {CONCRETE_ACTION}
   * **Action:** {NEXT_ACTION}
   * **Evidence Collection:** {EVIDENCE_REQUIREMENT}

### STEP 4: {STEP_4_NAME}
1. **`[MUST]` {STEP_4_ACTION}:**
   * **Action:** {CONCRETE_ACTION}
   * **Action:** {NEXT_ACTION}
   * **Evidence Collection:** {EVIDENCE_REQUIREMENT}

### STEP 5: {STEP_5_NAME}
1. **`[MUST]` {STEP_5_ACTION}:**
   * **Action:** {CONCRETE_ACTION}
   * **Action:** {NEXT_ACTION}
   * **Evidence Collection:** {EVIDENCE_REQUIREMENT}

### FINALIZATION
> "{COMPLETION_MESSAGE}
>
> {NEXT_STEPS_GUIDANCE}"
```

## QUALITY ACCEPTANCE CRITERIA

### Structural Compliance
- [ ] Protocol header matches bootstrap format: `# PROTOCOL {N}: {NAME}`
- [ ] All required sections present: AI Role, Process Steps, Finalization
- [ ] Heading hierarchy preserved: H1 → H2 → H3 structure
- [ ] Markers used correctly: `[MUST]`, `[GUIDELINE]`, `[CRITICAL]`, `[STRICT]`
- [ ] Line-referenceable structure for meta-analysis

### Content Quality
- [ ] AI role clearly defined with specific persona
- [ ] Mission statement is actionable and specific
- [ ] Critical guardrail is non-negotiable and clear
- [ ] Process steps are concrete and executable
- [ ] Evidence collection requirements specified
- [ ] Quality gates have measurable criteria
- [ ] Communication templates provided
- [ ] Integration points documented

### Meta-Validation (Circular Validation)
- [ ] Generated protocol → Meta-Analysis Generator → Valid analysis output
- [ ] Analysis contains all 4 layers (System, Behavioral, Procedural, Communication)
- [ ] Subsystems properly mappable from protocol structure
- [ ] Cognitive roles (Planner/Executor/Validator/Auditor) identifiable
- [ ] No structural deficiencies flagged

## USAGE PROTOCOL

### Step 1: User Fills Input Form
User completes `protocol-input-form-bootstrap.yaml` with all required information.

### Step 2: AI Validates Input
1. Load filled form
2. Validate completeness
3. Check consistency
4. Request clarification if needed

### Step 3: AI Generates Protocol
1. Execute Phase 1-7 of generation algorithm
2. Populate bootstrap protocol template
3. Ensure structural compliance
4. Generate communication templates

### Step 4: AI Validates Output
1. Run Meta-Analysis Generator on generated protocol
2. Verify all 4 layers present in analysis
3. Check subsystem mapping
4. Validate cognitive role assignment

### Step 5: AI Delivers Protocol
1. Output protocol markdown file
2. Provide meta-analysis validation report
3. Include integration instructions
4. Suggest next steps

## EDGE CASE HANDLING

### Missing Input Fields
- **Issue**: Required form fields incomplete
- **Solution**: Request specific missing information from user
- **Approach**: Provide clear examples of what's needed

### Complex Multi-Phase Protocols
- **Issue**: Protocol has many phases (>8)
- **Solution**: Group related phases into logical subsections
- **Approach**: Use nested headings to maintain readability

### Integration Conflicts
- **Issue**: Protocol integrates with non-existent protocol
- **Solution**: Flag dependency issue, suggest protocol creation order
- **Approach**: Validate protocol sequence consistency

### Circular Validation Failures
- **Issue**: Generated protocol fails meta-analysis validation
- **Solution**: Identify structural gap, regenerate with fixes
- **Approach**: Use meta-analysis feedback to guide regeneration

## ANTI-PATTERNS TO AVOID

### ❌ DON'T:
- Generate protocols without filled input form
- Skip structural compliance validation
- Omit required sections for bootstrap format
- Use inconsistent marker syntax
- Break heading hierarchy
- Create protocols without quality gates
- Ignore integration points with existing workflow
- Skip circular validation with Meta-Analysis Generator
- Generate creative prose instead of executable instructions
- Assume protocol structure without referencing bootstrap format

### ✅ DO:
- Validate input form completeness before generation
- Follow exact structural template from bootstrap protocol
- Include all required sections in correct order
- Use consistent marker syntax throughout
- Maintain strict heading hierarchy
- Define clear quality gates with measurable criteria
- Document all integration points
- Validate with Meta-Analysis Generator before delivery
- Generate concrete, executable instructions
- Reference bootstrap protocol for pattern consistency

## VALIDATION CHECKLIST

### Pre-Generation Validation
- [ ] Input form completely filled
- [ ] All mandatory fields present
- [ ] Integration points reference valid protocols
- [ ] Protocol number follows sequence
- [ ] AI role clearly defined
- [ ] Mission statement actionable

### Generation Validation
- [ ] Protocol structure matches bootstrap format template
- [ ] All required sections present
- [ ] Heading hierarchy correct
- [ ] Markers used consistently
- [ ] Communication templates included
- [ ] Quality gates defined

### Post-Generation Validation
- [ ] Circular validation passed (Protocol → Meta-Analysis → Valid)
- [ ] All 4 layers present in meta-analysis
- [ ] Subsystems properly mapped
- [ ] Cognitive roles identifiable
- [ ] Integration po
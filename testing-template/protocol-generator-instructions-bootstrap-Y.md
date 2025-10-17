# Bootstrap Protocol Generator System Instructions

## PURPOSE
This document provides **complete system instructions** for AI agents to generate new ai-driven-workflow protocols that are **structurally identical** to the bootstrap protocol format in `.cursor/ai-driven-workflow/0-bootstrap-your-project.md`. The generated protocols must be analyzable by the Meta-Instruction Analysis Generator, ensuring circular validation compatibility.

## INPUT REQUIREMENTS

### Mandatory Inputs (via Fillable Form)
Users must complete the **Bootstrap Protocol Requirements Form** (see `protocol-input-form-bootstrap.yaml`) with:

- **Protocol Number**: Sequential number in workflow (e.g., 0, 1, 2)
- **Protocol Name**: Descriptive name (e.g., "project-bootstrap", "context-engineering")
- **AI Role**: Persona the AI assumes (e.g., "AI Codebase Analyst", "Context Architect")
- **Mission**: 1-2 sentence mission statement
- **Critical Guardrail**: Primary constraint or limitation
- **Steps**: Execution steps with actions, communications, and halt conditions
- **Finalization**: Completion message and handoff instructions

### Optional Inputs
- **Context**: Additional background about protocol's role in larger workflow
- **Automation Hooks**: Scripts or tools to integrate
- **Focus Areas**: Specific aspects to emphasize

## PROTOCOL GENERATION ALGORITHM

### Phase 1: Input Validation & Analysis
1. **Parse filled form** - Load and validate all required fields
2. **Validate completeness** - Ensure all mandatory sections populated
3. **Check consistency** - Verify step sequence and logical flow
4. **Extract patterns** - Identify structural patterns from input

### Phase 2: 4-Layer Architecture Mapping
Based on input, map content to the 4-layer meta-architecture:

**Layer 1: System-Level Decisions**
- Extract from: Protocol mission, AI role, critical guardrail
- Generate: Mission statement, role definition, governance constraints

**Layer 2: Behavioral Control**
- Extract from: Halt conditions, validation checkpoints, user confirmations
- Generate: Human-in-the-loop gates, state transition controls

**Layer 3: Procedural Logic**
- Extract from: Step actions, automation hooks, evidence collection
- Generate: Concrete procedures, tool invocations, data flow

**Layer 4: Communication Grammar**
- Extract from: Communication templates, announcements, validation prompts
- Generate: Communication templates, narrative structures

### Phase 3: Protocol Structure Generation
Generate protocol following this exact bootstrap structure:

```markdown
# PROTOCOL [NUMBER]: [NAME]

## 1. AI ROLE AND MISSION

You are a **[AI Role]**. Your mission is to [mission statement].

**🚫 [CRITICAL] [Critical guardrail/constraint].**

## 2. [MAIN PROCESS SECTION]

### STEP 1: [Step Name]

1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific instruction]
   * **Action:** [Additional instruction if needed]
   * **Communication:** 
     > "[Example announcement or prompt]"
   * **Halt condition:** [When to stop and await confirmation]

2. **`[GUIDELINE]` [Optional Action Title]:**
   * **Action:** [Recommended instruction]
   * **Example:**
     ```bash
     # Code example if applicable
     ```

### STEP 2: [Next Step Name]
[Repeat pattern for all steps]

### FINALIZATION
[Completion message and handoff instructions]
```

### Phase 4: Evidence & Quality Gate Integration
For each step in the input:
1. **Generate evidence collection requirements**
   - Map what artifacts must be collected
   - Define storage locations (e.g., `.cursor/bootstrap/`, `.cursor/context-kit/`)
   
2. **Create validation checkpoints**
   - Define pass/fail criteria
   - Specify validation methods
   - Include automation hooks

3. **Define success criteria**
   - Measurable outcomes
   - Validation scripts
   - User confirmation points

### Phase 5: Communication Template Generation
Based on input communication requirements:
1. **Generate status announcements** - Standard prefixes for progress reporting
2. **Create validation prompts** - User confirmation dialog templates
3. **Define error handling** - Failure scenario messages
4. **Build narrative flow** - Conversational guidance text

### Phase 6: Structural Compliance Validation
Ensure generated protocol:
1. **Matches bootstrap protocol format** - Header, sections, subsections
2. **Contains all required sections** - Role, Mission, Steps, Finalization
3. **Uses correct markers** - `[MUST]`, `[GUIDELINE]`, `[CRITICAL]`, `[STRICT]`
4. **Maintains heading hierarchy** - H1 → H2 → H3 consistency
5. **Includes line-referenceable structure** - Clear section boundaries for meta-analysis

### Phase 7: Circular Validation Test
**CRITICAL**: Generated protocol must pass Meta-Analysis Generator validation:

1. **Run Meta-Analysis Generator** on generated protocol
2. **Validate analysis output** contains:
   - Layer 1: System-Level Decisions ✓
   - Layer 2: Behavioral Control ✓
   - Layer 3: Procedural Logic ✓
   - Layer 4: Communication Grammar ✓
3. **Check subsystem mapping** - ASCII diagram properly reflects protocol structure
4. **Verify cognitive roles** - Planner/Executor/Validator/Auditor identifiable
5. **If validation fails** - Regenerate with structural adjustments

## OUTPUT TEMPLATE STRUCTURE

### Template Overview
```markdown
# PROTOCOL [NUMBER]: [NAME]

## 1. AI ROLE AND MISSION
[Role definition with guardrails]

## 2. [MAIN PROCESS SECTION]

### STEP 1: [Step Name]
[Instructions with MUST/GUIDELINE markers]

### STEP 2: [Step Name]
[Continue pattern]

### FINALIZATION
[Completion validation]
```

### Required Elements
Every generated protocol MUST include:

1. **Header Section**
   - Protocol number and name
   - Clear visual separation

2. **AI Role and Mission**
   - Explicit persona assignment
   - Clear mission statement
   - Critical guardrails/constraints

3. **Main Process Section**
   - Numbered steps with clear titles
   - `[MUST]` for mandatory actions
   - `[GUIDELINE]` for recommended actions
   - Communication examples
   - Halt/validation points

4. **Finalization**
   - Completion validation items
   - Next protocol transition command

## QUALITY ACCEPTANCE CRITERIA

### Structural Compliance
- [ ] Protocol header matches format: `# PROTOCOL [NUMBER]: [NAME]`
- [ ] All required sections present (Role, Mission, Steps, Finalization)
- [ ] Heading hierarchy preserved (H1 → H2 → H3)
- [ ] Markers used correctly (`[MUST]`, `[GUIDELINE]`, `[CRITICAL]`)
- [ ] Line-referenceable structure for meta-analysis

### Content Quality
- [ ] AI role clearly defined with specific persona
- [ ] Mission statement is actionable and specific
- [ ] Steps are concrete and executable
- [ ] Evidence collection requirements specified
- [ ] Communication templates provided

### Meta-Validation (Circular Validation)
- [ ] Generated protocol → Meta-Analysis Generator → Valid analysis output
- [ ] Analysis contains all 4 layers (System, Behavioral, Procedural, Communication)
- [ ] Subsystems properly mappable from protocol structure
- [ ] Cognitive roles (Planner/Executor/Validator/Auditor) identifiable
- [ ] No structural deficiencies flagged

### Workflow Integration
- [ ] Protocol number follows sequence
- [ ] Steps flow logically from one to the next
- [ ] Finalization transitions to next protocol
- [ ] Automation hooks integrate with existing scripts

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

### Output Naming Convention
- **Format**: `[number]-[protocol-name].md`
- **Examples**:
  - `0-project-bootstrap.md`
  - `1-context-engineering.md`
  - `2-template-discovery.md`

### File Location
- **Primary**: `.cursor/ai-driven-workflow/[number]-[protocol-name].md`
- **Validation**: `meta-analysis/session-NN/analysis-[number]-[protocol-name].md`

## EDGE CASE HANDLING

### Missing Input Fields
- **Issue**: Required form fields incomplete
- **Solution**: Request specific missing information from user
- **Approach**: Provide clear examples of what's needed

### Complex Multi-Step Protocols
- **Issue**: Protocol has many steps (>7)
- **Solution**: Group related steps into logical subsections
- **Approach**: Use nested headings to maintain readability

### Missing Finalization
- **Issue**: No completion or handoff instructions
- **Solution**: Generate default finalization based on protocol purpose
- **Approach**: Create generic handoff to next logical protocol

### Circular Validation Failures
- **Issue**: Generated protocol fails meta-analysis validation
- **Solution**: Identify structural gap, regenerate with fixes
- **Approach**: Use meta-analysis feedback to guide regeneration

## ANTI-PATTERNS TO AVOID

### ❌ DON'T:
- Generate protocols without filled input form
- Skip structural compliance validation
- Omit required sections (Role, Mission, Steps, Finalization)
- Use inconsistent marker syntax (`[MUST]` vs `MUST:`)
- Break heading hierarchy (H1 → H3, skipping H2)
- Create protocols without clear step progression
- Ignore automation hooks in existing workflow
- Skip circular validation with Meta-Analysis Generator
- Generate creative prose instead of executable instructions
- Assume protocol structure without referencing bootstrap patterns

### ✅ DO:
- Validate input form completeness before generation
- Follow exact structural template from bootstrap protocol
- Include all required sections in correct order
- Use consistent marker syntax throughout
- Maintain strict heading hierarchy
- Define clear step progression
- Document all automation hooks
- Validate with Meta-Analysis Generator before delivery
- Generate concrete, executable instructions
- Reference bootstrap protocol for pattern consistency

## VALIDATION CHECKLIST

### Pre-Generation Validation
- [ ] Input form completely filled
- [ ] All mandatory fields present
- [ ] Step sequence logical and complete
- [ ] Protocol number follows sequence
- [ ] AI role clearly defined
- [ ] Mission statement actionable

### Generation Validation
- [ ] Protocol structure matches bootstrap template
- [ ] All required sections present
- [ ] Heading hierarchy correct
- [ ] Markers used consistently
- [ ] Communication templates included
- [ ] Step progression clear

### Post-Generation Validation
- [ ] Circular validation passed (Protocol → Meta-Analysis → Valid)
- [ ] All 4 layers present in meta-analysis
- [ ] Subsystems properly mapped
- [ ] Cognitive roles identifiable
- [ ] Step flow functional
- [ ] Finalization complete

### Delivery Validation
- [ ] File naming convention followed
- [ ] Location correct (.cursor/ai-driven-workflow/)
- [ ] Meta-analysis validation report included
- [ ] Integration instructions provided
- [ ] Next steps suggested

---

## INTEGRATION WITH META-ANALYSIS GENERATOR

### Circular Validation Loop
```
User Input Form → Bootstrap Protocol Generator → Generated Protocol
                                                      ↓
                                              Meta-Analysis Generator
                                                      ↓
                                              Validation Report
                                                      ↓
                                              [Pass] → Deliver Protocol
                                              [Fail] → Regenerate with Fixes
```

### Validation Criteria
Generated protocol must produce meta-analysis with:
1. **Layer 1 (System-Level Decisions)**:
   - Mission statement extraction ✓
   - Role definition extraction ✓
   - Governance constraints extraction ✓

2. **Layer 2 (Behavioral Control)**:
   - Halt condition extraction ✓
   - Validation checkpoint extraction ✓
   - State transition controls ✓

3. **Layer 3 (Procedural Logic)**:
   - Step-by-step procedures ✓
   - Tool invocations ✓
   - Data flow patterns ✓

4. **Layer 4 (Communication Grammar)**:
   - Announcement templates ✓
   - Validation prompts ✓
   - Narrative structures ✓

### Success Indicators
- Meta-analysis contains all 5 required sections
- ASCII diagram properly reflects protocol structure
- Commentary maps real dependencies
- Cognitive roles properly assigned
- Inference summary captures protocol essence

---

**This system instruction document enables any AI agent to generate new ai-driven-workflow protocols that are structurally identical to the bootstrap protocol format, ensuring consistency, analyzability, and seamless workflow integration through circular validation with the Meta-Instruction Analysis Generator.**

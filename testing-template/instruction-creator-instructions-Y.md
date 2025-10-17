# Instruction Creator Meta-System Instructions

## PURPOSE
This document provides **complete system instructions** for AI agents to analyze any target protocol and generate specialized protocol-generator-instructions files that are perfectly aligned to that specific protocol's structure. This enables format-flexible protocol generation across different structural patterns.

## INPUT REQUIREMENTS

### Mandatory Inputs
Users must provide:
- **Target Protocol Path**: Path to the protocol file to analyze (e.g., `.cursor/ai-driven-workflow/0-bootstrap-your-project.md`)
- **Target Protocol Name**: Short name for generated files (e.g., "bootstrap", "prd", "tasks")

### Optional Inputs
- **Custom Output Directory**: Where to place generated files (default: `generators/`)
- **Validation Mode**: Whether to run circular validation test (default: true)

## PROTOCOL ANALYSIS ALGORITHM

### Phase 1: Target Protocol Structure Analysis
1. **Read Target Protocol Completely**
   - Load the entire target protocol file
   - Parse markdown structure and hierarchy
   - Extract all section headers and content patterns

2. **Extract Structural Elements**
   - **Header Format**: Analyze title pattern (e.g., `# PROTOCOL [N]: [NAME]`)
   - **Section Hierarchy**: Map H1 → H2 → H3 → H4 structure
   - **Section Names**: Identify all major sections and their patterns
   - **Required vs Optional**: Determine which sections are mandatory
   - **Content Patterns**: Extract action formats, communication templates, validation patterns

3. **Identify Unique Characteristics**
   - **Markers Used**: Extract action markers (`[MUST]`, `[GUIDELINE]`, `[CRITICAL]`, etc.)
   - **Evidence Collection**: Identify evidence collection patterns and storage locations
   - **Automation Hooks**: Locate automation script references and execution patterns
   - **Validation Checkpoints**: Extract quality gate structures and validation criteria
   - **Communication Templates**: Identify announcement formats and prompt patterns

### Phase 2: Format Classification
Based on structural analysis, classify the target protocol into one of these formats:

**Format A: 00A/00B Structure (6-Section)**
```markdown
# PROTOCOL [N]: [NAME] ([DOMAIN] COMPLIANT)
## 1. AI ROLE AND MISSION
## 2. [MAIN WORKFLOW SECTION]
## 3. INTEGRATION POINTS
## 4. QUALITY GATES
## 5. COMMUNICATION PROTOCOLS
## 6. HANDOFF CHECKLIST
```

**Format B: Bootstrap Structure (Step-Based)**
```markdown
# PROTOCOL [N]: [NAME]
## 1. AI ROLE AND MISSION
## 2. [MAIN PROCESS SECTION]
### STEP 1-7: [Various Steps]
## FINALIZATION
```

**Format C: PRD Structure (Phase-Based)**
```markdown
# PROTOCOL [N]: [NAME]
## AI ROLE
## PHASE 1-4: [Various Phases]
## FINAL PRD TEMPLATE
```

**Format D: Custom Structure**
- Unique section patterns not matching A, B, or C
- Requires custom template generation

### Phase 3: Reusable Component Extraction
Extract the following reusable components from the existing `protocol-generator-instructions.md`:

1. **7-Phase Generation Algorithm** (Core Reusable)
   - Phase 1: Input Validation & Analysis
   - Phase 2: 4-Layer Architecture Mapping
   - Phase 3: Protocol Structure Generation (Format-Specific)
   - Phase 4: Evidence & Quality Gate Integration
   - Phase 5: Communication Template Generation
   - Phase 6: Structural Compliance Validation
   - Phase 7: Circular Validation Test

2. **4-Layer Architecture Mapping** (Core Reusable)
   - Layer 1: System-Level Decisions
   - Layer 2: Behavioral Control
   - Layer 3: Procedural Logic
   - Layer 4: Communication Grammar

3. **Validation Methodology** (Adaptable)
   - Pre-Generation Validation
   - Generation Validation
   - Post-Generation Validation
   - Delivery Validation

### Phase 4: Format-Specific Template Generation
Generate specialized template structure based on target protocol format:

**For Format A (00A/00B Structure):**
```markdown
## Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

# PROTOCOL [NUMBER]: [NAME] ([DOMAIN] COMPLIANT)

## [NUMBER]. AI ROLE AND MISSION
You are a **[AI Role]**. Your mission is to [purpose statement].
**🚫 [CRITICAL] [Primary guardrail/constraint].**

## [NUMBER]. [PRIMARY SECTION NAME]
### STEP [N]: [Phase Name]
1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific instruction]
   * **Communication:** 
     > "[Example announcement or prompt]"
   * **Halt condition:** [When to stop and await confirmation]

## [NUMBER]. INTEGRATION POINTS
**Inputs From:**
- Protocol [N]: [What data/artifacts are consumed]

**Outputs To:**
- Protocol [N]: [What artifacts are provided]

## [NUMBER]. QUALITY GATES
**Gate [N]: [Gate Name]**
- **Criteria:** [Validation requirements]
- **Evidence:** [What must be collected]
- **Failure Handling:** [What to do if gate fails]

## [NUMBER]. COMMUNICATION PROTOCOLS
**Status Announcements:**
```
[PHASE N START] - [Message template]
[PHASE N COMPLETE] - [Message template]
```

## [NUMBER]. HANDOFF CHECKLIST
Before completing this protocol, validate:
- [ ] [Checklist item 1]
- [ ] [Checklist item 2]

Upon completion, execute:
```
[PROTOCOL COMPLETE] - Ready for Protocol [N+1]
```
```

**For Format B (Bootstrap Structure):**
```markdown
## Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

# PROTOCOL [NUMBER]: [NAME]

## 1. AI ROLE AND MISSION
You are a **[AI Role]**. Your mission is to [purpose statement].
**🚫 [CRITICAL] [Primary guardrail/constraint].**

## 2. [MAIN PROCESS SECTION]
### STEP 1: [Step Name]
1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific instruction]
   * **Communication:** 
     > "[Example announcement or prompt]"
   * **Halt condition:** [When to stop and await confirmation]

### STEP 2: [Step Name]
[Continue pattern for all steps]

## FINALIZATION
[Completion message and handoff instructions]
```

**For Format C (PRD Structure):**
```markdown
## Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

# PROTOCOL [NUMBER]: [NAME]

## AI ROLE
You are a **[AI Role]**. Your mission is to [purpose statement].
**🚫 [CRITICAL] [Primary guardrail/constraint].**

## PHASE 1: [Phase Name]
**Goal:** [Phase goal statement]

### 1.1 [Subsection Name]
1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific instruction]
   * **Communication:** 
     > "[Example announcement or prompt]"
   * **Halt condition:** [When to stop and await confirmation]

## PHASE 2: [Phase Name]
[Continue pattern for all phases]

## FINAL PRD TEMPLATE
[Template structure for final output]
```

### Phase 5: Input Form Adaptation
Generate format-specific input forms based on target protocol structure:

**For Format A (00A/00B):**
```yaml
protocol_number: ""
protocol_name: ""
domain_compliance: ""
ai_role: ""
mission: ""
critical_guardrail: ""
phases:
  - phase_number: 1
    phase_name: ""
    steps:
      - step_number: 1
        step_name: ""
        actions: []
integration_points:
  inputs_from: []
  outputs_to: []
quality_gates:
  - gate_number: 1
    gate_name: ""
    criteria: ""
    evidence: ""
    failure_handling: ""
communication:
  status_announcements: []
  validation_prompts: []
  error_handling: []
handoff_checklist: []
```

**For Format B (Bootstrap):**
```yaml
protocol_number: ""
protocol_name: ""
ai_role: ""
mission: ""
critical_guardrail: ""
steps:
  - step_number: 1
    step_name: ""
    actions: []
finalization: ""
```

**For Format C (PRD):**
```yaml
protocol_number: ""
protocol_name: ""
ai_role: ""
mission: ""
critical_guardrail: ""
prerequisites: ""
phases:
  - phase_number: 1
    phase_name: ""
    goal: ""
    subsections: []
final_template: ""
```

### Phase 6: Specialized Generator Instructions Creation
Create the complete `protocol-generator-instructions-{target-name}.md` file:

1. **Header and Purpose**
   - Adapt purpose statement to target format
   - Include format-specific compliance requirements

2. **Input Requirements**
   - Include format-specific input form
   - Adapt mandatory vs optional fields

3. **Protocol Generation Algorithm**
   - Include all 7 phases (reusable core)
   - Adapt Phase 3 to target format structure
   - Include format-specific validation criteria

4. **Output Template Structure**
   - Include complete format-specific template
   - Provide format-specific examples

5. **Quality Acceptance Criteria**
   - Adapt structural compliance to target format
   - Include format-specific validation checklist

6. **Usage Protocol**
   - Adapt to target format requirements
   - Include format-specific naming conventions

### Phase 7: Circular Validation Integration
Ensure generated instruction creator maintains circular validation compatibility:

1. **Meta-Analysis Compatibility**
   - Generated protocols must be analyzable by Meta-Analysis Generator
   - All 4 layers must be extractable from generated protocols
   - Cognitive roles must be identifiable

2. **Validation Criteria**
   - Generated protocols → Meta-Analysis Generator → Valid analysis output
   - Analysis contains all 4 layers (System, Behavioral, Procedural, Communication)
   - Subsystems properly mappable from protocol structure

## OUTPUT GENERATION

### Generated Files
1. **`protocol-generator-instructions-{target-name}.md`**
   - Complete specialized generator instructions
   - Format-specific template and validation
   - Circular validation compatibility

2. **`protocol-input-form-{target-name}.yaml`**
   - Format-specific input form
   - Captures all target format requirements
   - Aligned with generated instructions

### File Naming Convention
- **Format**: `protocol-generator-instructions-{target-name}.md`
- **Examples**:
  - `protocol-generator-instructions-bootstrap.md`
  - `protocol-generator-instructions-prd.md`
  - `protocol-generator-instructions-tasks.md`

### File Location
- **Primary**: `generators/protocol-generator-instructions-{target-name}.md`
- **Input Form**: `generators/protocol-input-form-{target-name}.yaml`

## USAGE PROTOCOL

### Step 1: User Provides Target Protocol
User specifies target protocol path and name:
```
apply instruction from instruction-creator to protocol-0-bootstrap
```

### Step 2: AI Analyzes Target Protocol
1. Load target protocol file
2. Execute Phase 1-2 analysis algorithm
3. Classify format and extract patterns
4. Extract reusable components

### Step 3: AI Generates Specialized Instructions
1. Execute Phase 3-6 generation algorithm
2. Create format-specific template
3. Generate aligned input form
4. Ensure circular validation compatibility

### Step 4: AI Validates Output
1. Verify generated instructions completeness
2. Test format-specific template accuracy
3. Validate input form alignment
4. Confirm circular validation compatibility

### Step 5: AI Delivers Specialized Generator
1. Output specialized generator instructions
2. Provide format-specific input form
3. Include usage instructions
4. Suggest next steps

## QUALITY ACCEPTANCE CRITERIA

### Analysis Quality
- [ ] Target protocol structure accurately extracted
- [ ] Format classification correct
- [ ] All structural patterns identified
- [ ] Unique characteristics captured

### Generation Quality
- [ ] Specialized instructions complete and accurate
- [ ] Format-specific template matches target exactly
- [ ] Input form captures all target requirements
- [ ] Circular validation compatibility maintained

### Integration Quality
- [ ] Generated protocols match target format exactly
- [ ] Meta-analysis generator compatibility verified
- [ ] All 4 layers extractable from generated protocols
- [ ] Cognitive roles identifiable in generated protocols

## EDGE CASE HANDLING

### Unrecognized Format
- **Issue**: Target protocol doesn't match known formats
- **Solution**: Create custom format classification
- **Approach**: Extract all structural patterns and create custom template

### Missing Sections
- **Issue**: Target protocol missing expected sections
- **Solution**: Mark sections as optional in generated instructions
- **Approach**: Provide fallback patterns for missing sections

### Complex Nested Structure
- **Issue**: Target protocol has deep nesting (>4 levels)
- **Solution**: Flatten structure while preserving hierarchy
- **Approach**: Map deep nesting to manageable template levels

## ANTI-PATTERNS TO AVOID

### ❌ DON'T:
- Assume all protocols follow the same structure
- Skip format classification step
- Generate instructions without analyzing target structure
- Ignore unique characteristics of target protocol
- Break circular validation compatibility
- Create generic instructions that don't match target format

### ✅ DO:
- Analyze target protocol structure completely
- Classify format accurately
- Extract all unique characteristics
- Generate format-specific instructions
- Maintain circular validation compatibility
- Test generated instructions with target format

## VALIDATION CHECKLIST

### Pre-Analysis Validation
- [ ] Target protocol file exists and readable
- [ ] Target protocol name provided
- [ ] Output directory accessible

### Analysis Validation
- [ ] Protocol structure completely extracted
- [ ] Format classification accurate
- [ ] All patterns identified
- [ ] Unique characteristics captured

### Generation Validation
- [ ] Specialized instructions complete
- [ ] Format-specific template accurate
- [ ] Input form aligned with target
- [ ] Circular validation compatibility maintained

### Delivery Validation
- [ ] Generated files follow naming convention
- [ ] Files placed in correct location
- [ ] Usage instructions provided
- [ ] Next steps suggested

---

**This instruction creator meta-system enables any AI agent to generate specialized protocol-generator instructions for any protocol format, ensuring format flexibility, consistency, and circular validation compatibility across all generated protocols.**

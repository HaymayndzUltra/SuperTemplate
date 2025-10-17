# PRD Protocol Generator System Instructions

## PURPOSE
This document provides **complete system instructions** for AI agents to generate new ai-driven-workflow protocols that are **structurally identical** to the PRD protocol format in `.cursor/ai-driven-workflow/1-create-prd.md`. The generated protocols must be analyzable by the Meta-Instruction Analysis Generator, ensuring circular validation compatibility.

## INPUT REQUIREMENTS

### Mandatory Inputs (via Fillable Form)
Users must complete the **PRD Protocol Requirements Form** (see `protocol-input-form-prd.yaml`) with:

- **Protocol Number**: Sequential number in workflow (e.g., 1, 2, 3)
- **Protocol Name**: Descriptive name (e.g., "implementation-ready-prd", "feature-specification")
- **AI Role**: Persona the AI assumes (e.g., "Product Manager", "Requirements Analyst")
- **Mission**: 1-2 sentence mission statement
- **Critical Guardrail**: Primary constraint or limitation
- **Prerequisites**: What must be completed before this protocol
- **Phases**: Execution phases with goals, subsections, and questions
- **Final Template**: Template structure for final output

### Optional Inputs
- **Context**: Additional background about protocol's role in larger workflow
- **Automation Hooks**: Scripts or tools to integrate
- **Focus Areas**: Specific aspects to emphasize

## PROTOCOL GENERATION ALGORITHM

### Phase 1: Input Validation & Analysis
1. **Parse filled form** - Load and validate all required fields
2. **Validate completeness** - Ensure all mandatory sections populated
3. **Check consistency** - Verify phase sequence and logical flow
4. **Extract patterns** - Identify structural patterns from input

### Phase 2: 4-Layer Architecture Mapping
Based on input, map content to the 4-layer meta-architecture:

**Layer 1: System-Level Decisions**
- Extract from: Protocol mission, AI role, critical guardrail
- Generate: Mission statement, role definition, governance constraints

**Layer 2: Behavioral Control**
- Extract from: Prerequisites, validation checkpoints, user confirmations
- Generate: Human-in-the-loop gates, state transition controls

**Layer 3: Procedural Logic**
- Extract from: Phase steps, automation hooks, evidence collection
- Generate: Concrete procedures, tool invocations, data flow

**Layer 4: Communication Grammar**
- Extract from: Question templates, announcements, validation prompts
- Generate: Communication templates, narrative structures

### Phase 3: Protocol Structure Generation
Generate protocol following this exact PRD structure:

```markdown
# PROTOCOL [NUMBER]: [NAME]

## AI ROLE

You are a **[AI Role]**. [Mission statement].

**🚫 [CRITICAL] [Critical guardrail/constraint].**

### 📚 MANDATORY PREREQUISITE

**BEFORE ANY INTERROGATION**, you MUST familiarize yourself with the project's overall architecture. If the user has a master `README.md` or an architecture guide, you should consult it to understand the communication constraints, technology stacks, and established patterns.

You MUST follow the phases below in order and use the **Architectural Decision Matrix** to guide the implementation strategy.

---

## 🎯 ARCHITECTURAL DECISION MATRIX (EXAMPLE)

This is a generic template. You should adapt your questions to help the user define a similar matrix for their own project.

| **Need Type** | **Likely Implementation Target** | **Key Constraints** | **Communication Patterns** | **Guiding Principle** |
|---|---|---|---|---|
| **User Interface / Component** | Frontend Application | Responsive Design, Theming, i18n | API calls (e.g., Read-only REST), Direct calls to backend services | **[GUIDELINE] Avoid Over-Engineering:** Start with standard components and simple state management. |
| **Business Logic / Processing** | Backend Microservices | Scalability, Inter-service RPC | Full CRUD to a central API, async messaging | **Avoid Over-Engineering:** Implement the simplest logic that meets the need. Defer complex patterns until required. |
| **Data CRUD / DB Management** | Central REST API | Exclusive DB access, OpenAPI spec | Direct DB queries (SQL/NoSQL) | **Avoid Over-Engineering:** Use standard CRUD. Avoid complex queries or premature optimization. |
| **Static Assets / Templates** | Object Storage (e.g., S3/R2) | Caching strategy, Versioning | Direct SDK/API access to storage | **Avoid Over-Engineering:** Use a simple file structure. Defer complex processing pipelines. |

---

## PHASE 1: [Phase Name]

**Goal:** [Phase goal statement]

### 1.1 [Subsection Name]
**Ask this crucial first question:**
1. **"[Question text]?"**

Based on the answer, proceed to the relevant section below.

### 1.2 [Subsection Name]
Ask these questions and **AWAIT ANSWERS** before proceeding:

1. **"[Question text]?"**
2. **"[Question text]?"**

Proceed to **Section 1.4: [Next Section Name]**.

## PHASE 2: [Phase Name]

### 2A. For a [Implementation Target]

1. **"[Question text]?"**
2. **"[Question text]?"**

### 2B. For a [Implementation Target]

1. **"[Question text]?"**
2. **"[Question text]?"**

---

## PHASE 3: [Phase Name]

Verify that the proposed interactions respect the project's known communication rules.

**✅ Example of Allowed Flows:**
- UI → Central API: GET only
- UI → Backend Services: GET/POST only
- Backend Services → Central API: Full CRUD

**❌ Example of Prohibited Flows:**
- UI → Database: Direct access is forbidden

---

## PHASE 4: [Phase Name]

1. **Summarize the Architecture:**
   ```
   🏗️ **FEATURE ARCHITECTURE SUMMARY**

   📍 **Primary Component**: [Detected Layer]
   🔗 **Communications**: [Validated Flows]
   💡 **Guiding Principle**: Avoid Over-Engineering. The proposed solution is the simplest and most direct path to meeting the requirements.
   ```
2. **Final Validation:**
   "Is this summary correct? Shall I proceed with generating the full PRD?"

### Phase 4.5: Automation Enhancement - PRD Asset Generation

1. **`[MUST]` Execute PRD Asset Generation:**
   ```bash
   python scripts/generate_prd_assets.py --prd prd-{feature-name}.md --output .artifacts/prd-assets/
   ```
   *   **Action:** Generate user stories, data schemas, API contracts from PRD.
   *   **Action:** Create implementation-ready artifacts for Protocol 2.

2. **`[MUST]` Announce Asset Generation:**
   ```
   [AUTOMATION] PRD Assets Generated: {asset_count} artifacts created
   ```
   *   **Action:** Display generated artifacts and their purposes.

3. **`[MUST]` Execute PRD Validation Gate:**
   ```bash
   python scripts/validate_prd_gate.py --prd prd-{feature-name}.md --output .artifacts/prd-validation.json
   ```
   *   **Action:** Validate PRD completeness, measurability, and traceability.
   *   **Action:** Check architectural constraints and communication patterns.

4. **`[MUST]` Announce Validation Results:**
   ```
   [AUTOMATION] PRD Validation: {status} - {score}/100
   ```
   *   **Pass Criteria:** Validation score ≥ 85
   *   **Fail Action:** Address validation issues before proceeding

5. **`[MUST]` Gate: PRD Automation Complete**
   *   **Validation:** All automation scripts executed successfully
   *   **Pass Criteria:** Assets generated, PRD validation ≥ 85
   *   **Fail Action:** Address automation failures before proceeding
   *   **[STRICT]** Do not release the PRD unless every validation artifact is archived in `.artifacts/`.

---

## FINAL PRD TEMPLATE (EXAMPLE)

```markdown
# PRD: [Feature Name]

## 1. Overview
- **Business Goal:** [Description of the need and problem solved]
- **Detected Architecture:**
  - **Primary Component:** `[Frontend App | Backend Service | ...]`

## 2. Functional Specifications
- **User Stories:** [For UI] or **API Contract:** [For Services]
- **Data Flow Diagram:**
  ```
  [A simple diagram showing the interaction between components]
  ```

## 3. Technical Specifications
- **Inter-Service Communication:** [Details of API calls]
- **Security & Authentication:** [Security model for the chosen layer]

## 4. Out of Scope
- [What this feature will NOT do]
```
```

### Phase 4: Evidence & Quality Gate Integration
For each phase in the input:
1. **Generate evidence collection requirements**
   - Map what artifacts must be collected
   - Define storage locations (e.g., `.artifacts/prd-assets/`, `.artifacts/prd-validation.json`)
   
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
1. **Generate question templates** - Standard question formats for user interviews
2. **Create validation prompts** - User confirmation dialog templates
3. **Define error handling** - Failure scenario messages
4. **Build narrative flow** - Conversational guidance text

### Phase 6: Structural Compliance Validation
Ensure generated protocol:
1. **Matches PRD protocol format** - Header, sections, subsections
2. **Contains all required sections** - Role, Prerequisites, Phases, Final Template
3. **Uses correct markers** - `[MUST]`, `[GUIDELINE]`, `[CRITICAL]`, `[STRICT]`
4. **Maintains heading hierarchy** - H1 → H2 → H3 → H4 consistency
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

## AI ROLE
[Role definition with guardrails]

## PHASE 1: [Phase Name]
[Instructions with questions and validation]

## PHASE 2: [Phase Name]
[Continue pattern]

## FINAL PRD TEMPLATE
[Template structure for final output]
```

### Required Elements
Every generated protocol MUST include:

1. **Header Section**
   - Protocol number and name
   - Clear visual separation

2. **AI Role**
   - Explicit persona assignment
   - Clear mission statement
   - Critical guardrails/constraints
   - Mandatory prerequisites

3. **Architectural Decision Matrix**
   - Implementation target mapping
   - Communication patterns
   - Guiding principles

4. **Phased Execution**
   - Numbered phases with clear goals
   - Subsection organization
   - Question templates
   - Validation checkpoints

5. **Final Template**
   - Complete PRD structure
   - Implementation-ready format

## QUALITY ACCEPTANCE CRITERIA

### Structural Compliance
- [ ] Protocol header matches format: `# PROTOCOL [NUMBER]: [NAME]`
- [ ] All required sections present (Role, Prerequisites, Phases, Final Template)
- [ ] Heading hierarchy preserved (H1 → H2 → H3 → H4)
- [ ] Markers used correctly (`[MUST]`, `[GUIDELINE]`, `[CRITICAL]`)
- [ ] Line-referenceable structure for meta-analysis

### Content Quality
- [ ] AI role clearly defined with specific persona
- [ ] Mission statement is actionable and specific
- [ ] Phases are concrete and executable
- [ ] Question templates provided
- [ ] Final template complete and implementation-ready

### Meta-Validation (Circular Validation)
- [ ] Generated protocol → Meta-Analysis Generator → Valid analysis output
- [ ] Analysis contains all 4 layers (System, Behavioral, Procedural, Communication)
- [ ] Subsystems properly mappable from protocol structure
- [ ] Cognitive roles (Planner/Executor/Validator/Auditor) identifiable
- [ ] No structural deficiencies flagged

### Workflow Integration
- [ ] Protocol number follows sequence
- [ ] Prerequisites reference valid protocols
- [ ] Phases flow logically from one to the next
- [ ] Final template enables next protocol
- [ ] Automation hooks integrate with existing scripts

## USAGE PROTOCOL

### Step 1: User Fills Input Form
User completes `protocol-input-form-prd.yaml` with all required information.

### Step 2: AI Validates Input
1. Load filled form
2. Validate completeness
3. Check consistency
4. Request clarification if needed

### Step 3: AI Generates Protocol
1. Execute Phase 1-7 of generation algorithm
2. Populate PRD protocol template
3. Ensure structural compliance
4. Generate question templates

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
  - `1-implementation-ready-prd.md`
  - `2-feature-specification.md`
  - `3-requirements-analysis.md`

### File Location
- **Primary**: `.cursor/ai-driven-workflow/[number]-[protocol-name].md`
- **Validation**: `meta-analysis/session-NN/analysis-[number]-[protocol-name].md`

## EDGE CASE HANDLING

### Missing Input Fields
- **Issue**: Required form fields incomplete
- **Solution**: Request specific missing information from user
- **Approach**: Provide clear examples of what's needed

### Complex Multi-Phase Protocols
- **Issue**: Protocol has many phases (>4)
- **Solution**: Group related phases into logical subsections
- **Approach**: Use nested headings to maintain readability

### Missing Question Templates
- **Issue**: No questions provided for user interviews
- **Solution**: Generate default question templates based on phase goals
- **Approach**: Create generic questions that can be customized

### Circular Validation Failures
- **Issue**: Generated protocol fails meta-analysis validation
- **Solution**: Identify structural gap, regenerate with fixes
- **Approach**: Use meta-analysis feedback to guide regeneration

## ANTI-PATTERNS TO AVOID

### ❌ DON'T:
- Generate protocols without filled input form
- Skip structural compliance validation
- Omit required sections (Role, Prerequisites, Phases, Final Template)
- Use inconsistent marker syntax (`[MUST]` vs `MUST:`)
- Break heading hierarchy (H1 → H3, skipping H2)
- Create protocols without clear phase progression
- Ignore automation hooks in existing workflow
- Skip circular validation with Meta-Analysis Generator
- Generate creative prose instead of executable instructions
- Assume protocol structure without referencing PRD patterns

### ✅ DO:
- Validate input form completeness before generation
- Follow exact structural template from PRD protocol
- Include all required sections in correct order
- Use consistent marker syntax throughout
- Maintain strict heading hierarchy
- Define clear phase progression
- Document all automation hooks
- Validate with Meta-Analysis Generator before delivery
- Generate concrete, executable instructions
- Reference PRD protocol for pattern consistency

## VALIDATION CHECKLIST

### Pre-Generation Validation
- [ ] Input form completely filled
- [ ] All mandatory fields present
- [ ] Phase sequence logical and complete
- [ ] Protocol number follows sequence
- [ ] AI role clearly defined
- [ ] Mission statement actionable

### Generation Validation
- [ ] Protocol structure matches PRD template
- [ ] All required sections present
- [ ] Heading hierarchy correct
- [ ] Markers used consistently
- [ ] Question templates included
- [ ] Phase progression clear

### Post-Generation Validation
- [ ] Circular validation passed (Protocol → Meta-Analysis → Valid)
- [ ] All 4 layers present in meta-analysis
- [ ] Subsystems properly mapped
- [ ] Cognitive roles identifiable
- [ ] Phase flow functional
- [ ] Final template complete

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
User Input Form → PRD Protocol Generator → Generated Protocol
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
   - Prerequisite extraction ✓
   - Validation checkpoint extraction ✓
   - State transition controls ✓

3. **Layer 3 (Procedural Logic)**:
   - Phase-by-phase procedures ✓
   - Question templates ✓
   - Data flow patterns ✓

4. **Layer 4 (Communication Grammar)**:
   - Question templates ✓
   - Validation prompts ✓
   - Narrative structures ✓

### Success Indicators
- Meta-analysis contains all 5 required sections
- ASCII diagram properly reflects protocol structure
- Commentary maps real dependencies
- Cognitive roles properly assigned
- Inference summary captures protocol essence

---

**This system instruction document enables any AI agent to generate new ai-driven-workflow protocols that are structurally identical to the PRD protocol format, ensuring consistency, analyzability, and seamless workflow integration through circular validation with the Meta-Instruction Analysis Generator.**

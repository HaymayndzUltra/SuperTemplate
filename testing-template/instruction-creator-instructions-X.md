# Instruction Creator Meta-System Instructions

## PURPOSE
This document provides **complete system instructions** for AI agents to analyze any existing protocol structure and generate specialized `protocol-generator-instructions-{name}.md` files that can create protocols in that specific format. This meta-system solves the structural mismatch problem where the current generator only supports 01/02 format.

## INPUT REQUIREMENTS

### Mandatory Inputs
Users must provide:
- **Target Protocol Path**: Path to existing protocol file (e.g., `.cursor/ai-driven-workflow/0-bootstrap-your-project.md`)
- **Target Protocol Name**: Short identifier for generated files (e.g., "bootstrap", "prd", "deployment")

### Optional Inputs
- **Custom Analysis Focus**: Specific structural elements to emphasize
- **Integration Constraints**: Special requirements for circular validation
- **Output Location**: Custom directory for generated files

## PROTOCOL ANALYSIS ALGORITHM

### Phase 1: Complete Protocol Reading & Structural Mapping

1. **`[MUST]` Read Target Protocol Completely:**
   * **Action:** Load entire protocol file content
   * **Action:** Parse markdown structure systematically
   * **Evidence Collection:** Document file path, line count, modification date

2. **`[MUST]` Extract Structural Elements:**
   * **Header Analysis:**
     - Extract title format pattern (e.g., `# PROTOCOL [N]: [NAME]`)
     - Identify numbering system (sequential, hierarchical, custom)
     - Document domain compliance tags
   
   * **Section Hierarchy Mapping:**
     - Map H1 → H2 → H3 → H4 relationships
     - Identify section naming patterns
     - Document required vs optional sections
     - Extract subsection patterns (e.g., STEP N, PHASE N)
   
   * **Content Pattern Extraction:**
     - Identify markers used (`[MUST]`, `[GUIDELINE]`, `[CRITICAL]`, `[STRICT]`)
     - Extract communication template patterns
     - Document halt condition formats
     - Identify evidence collection requirements
   
   * **Integration Point Analysis:**
     - Extract input/output definitions
     - Identify quality gate structures
     - Document validation checkpoint patterns
     - Map handoff/completion formats

3. **`[MUST]` Identify Unique Characteristics:**
   * **Action:** Compare with standard 01/02 format
   * **Action:** Document structural differences
   * **Action:** Identify format-specific requirements
   * **Evidence Collection:** Create structural comparison matrix

### Phase 2: 4-Layer Architecture Mapping

Map target protocol to the 4-layer meta-architecture:

**Layer 1: System-Level Decisions**
- Extract from: AI role definition, mission statement, critical guardrails
- Generate: Role assignment logic, mission statement templates, governance constraints

**Layer 2: Behavioral Control**
- Extract from: Quality gates, validation checkpoints, prerequisites
- Generate: Human-in-the-loop gates, state transition controls, validation logic

**Layer 3: Procedural Logic**
- Extract from: Step/phase structure, automation hooks, evidence collection
- Generate: Concrete procedures, tool invocations, data flow patterns

**Layer 4: Communication Grammar**
- Extract from: Announcements, prompts, error handling, narrative flow
- Generate: Communication templates, validation prompts, narrative structures

### Phase 3: Format-Specific Generator Creation

1. **`[MUST]` Adapt 7-Phase Algorithm:**
   * **Action:** Modify standard generation phases to match target structure
   * **Action:** Map input validation to target format requirements
   * **Action:** Adapt structural compliance to target format
   * **Action:** Modify circular validation for target format

2. **`[MUST]` Generate Format-Specific Template:**
   * **Action:** Create template structure matching target protocol
   * **Action:** Map section requirements to target format
   * **Action:** Adapt content patterns to target structure
   * **Action:** Include format-specific validation rules

3. **`[MUST]` Create Aligned Input Form:**
   * **Action:** Generate input form fields based on target structure
   * **Action:** Map required inputs to target format sections
   * **Action:** Include format-specific validation requirements
   * **Action:** Ensure input form captures all target format needs

### Phase 4: Specialized Generator Instructions Generation

Generate `protocol-generator-instructions-{name}.md` with:

```markdown
# Protocol Generator Instructions - {Target Format}

## PURPOSE
This document provides **complete system instructions** for AI agents to generate new ai-driven-workflow protocols that are **structurally identical** to the {target format} format. Generated protocols must be analyzable by the Meta-Instruction Analysis Generator.

## INPUT REQUIREMENTS

### Mandatory Inputs (via Fillable Form)
Users must complete the **{Target Format} Protocol Requirements Form** with:
- **Protocol Number**: Sequential number in workflow
- **Protocol Name**: Descriptive name
- **AI Role**: Persona the AI assumes
- **Mission**: Purpose statement
- **{Format-Specific Fields}**: [Based on target structure]

## PROTOCOL GENERATION ALGORITHM

### Phase 1: Input Validation & Analysis
[Adapted for target format]

### Phase 2: 4-Layer Architecture Mapping
[Standard mapping adapted to target format]

### Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

{Extracted Template Structure from Target Protocol}

### Phase 4: Evidence & Quality Gate Integration
[Adapted for target format requirements]

### Phase 5: Communication Template Generation
[Based on target format communication patterns]

### Phase 6: Structural Compliance Validation
[Target format specific validation rules]

### Phase 7: Circular Validation Test
[Standard circular validation adapted to target format]

## OUTPUT TEMPLATE STRUCTURE

{Complete template structure extracted from target protocol}

## QUALITY ACCEPTANCE CRITERIA

### Structural Compliance
- [ ] Protocol header matches target format: {extracted header pattern}
- [ ] All required sections present: {extracted section list}
- [ ] Heading hierarchy preserved: {extracted hierarchy pattern}
- [ ] Markers used correctly: {extracted marker patterns}
- [ ] Line-referenceable structure for meta-analysis

### Content Quality
- [ ] AI role clearly defined with specific persona
- [ ] Mission statement is actionable and specific
- [ ] {Format-specific content requirements}
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
User completes `protocol-input-form-{name}.yaml` with all required information.

### Step 2: AI Validates Input
1. Load filled form
2. Validate completeness
3. Check consistency
4. Request clarification if needed

### Step 3: AI Generates Protocol
1. Execute Phase 1-7 of generation algorithm
2. Populate protocol template
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
- **Issue**: Protocol has many phases (>5)
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
- Omit required sections for target format
- Use inconsistent marker syntax
- Break heading hierarchy
- Create protocols without quality gates
- Ignore integration points with existing workflow
- Skip circular validation with Meta-Analysis Generator
- Generate creative prose instead of executable instructions
- Assume protocol structure without referencing target format

### ✅ DO:
- Validate input form completeness before generation
- Follow exact structural template from target protocol
- Include all required sections in correct order
- Use consistent marker syntax throughout
- Maintain strict heading hierarchy
- Define clear quality gates with measurable criteria
- Document all integration points
- Validate with Meta-Analysis Generator before delivery
- Generate concrete, executable instructions
- Reference target protocol for pattern consistency

## VALIDATION CHECKLIST

### Pre-Generation Validation
- [ ] Input form completely filled
- [ ] All mandatory fields present
- [ ] Integration points reference valid protocols
- [ ] Protocol number follows sequence
- [ ] AI role clearly defined
- [ ] Mission statement actionable

### Generation Validation
- [ ] Protocol structure matches target format template
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
- [ ] Integration points functional
- [ ] Handoff checklist complete

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
User Input Form → Specialized Generator → Generated Protocol
                                            ↓
                                    Meta-Analysis Generator
                                            ↓
                                    Validation Report
                                            ↓
                                    [Pass] → Deliver Protocol
                                    [Fail] → Regenerate with Fixes


                                    User Input Form → Specialized Generator → Generated Protocol
                                            ↓
                                            Meta-Analysis Generator
                                            ↓
                                            Validation Report
                                            ↓
                                            [Pass] → Deliver Protocol
                                            [Fail] → Regenerate with Fixes



### Validation Criteria
Generated protocol must produce meta-analysis with:
1. **Layer 1 (System-Level Decisions)**:
   - Mission statement extraction ✓
   - Role definition extraction ✓
   - Governance constraints extraction ✓

2. **Layer 2 (Behavioral Control)**:
   - Quality gate extraction ✓
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

**This specialized generator instruction document enables any AI agent to generate new ai-driven-workflow protocols that are structurally identical to the {target format} format, ensuring consistency, analyzability, and seamless workflow integration through circular validation with the Meta-Instruction Analy  * **Action:** Create sample input form with test data
   * **Action:** Generate sample protocol using specialized instructions
   * **Action:** Run meta-analysis on generated protocol
   * **Action:** Verify circular validation passes
   * **Evidence Collection:** Document test results

### Phase 7: Output Delivery

1. **`[MUST]` Create Generated Files:**
   * **Action:** Generate `protocol-generator-instructions-{name}.md`
   * **Action:** Generate `protocol-input-form-{name}.yaml`
   * **Action:** Ensure proper file naming and location
   * **Evidence Collection:** Document file creation

2. **`[MUST]` Provide Integration Instructions:**
   * **Action:** Explain how to use generated instructions
   * **Action:** Document integration with existing workflow
   * **Action:** Provide usage examples
   * **Action:** Include troubleshooting guide

## OUTPUT TEMPLATE STRUCTURE

### Generated Files
- **`protocol-generator-instructions-{name}.md`**: Specialized generator instructions
- **`protocol-input-form-{name}.yaml`**: Format-specific input form
- **`validation-report-{name}.md`**: Validation results and test outcomes

### File Locations
- **Primary**: `generators/protocol-generator-instructions-{name}.md`
- **Input Form**: `generators/protocol-input-form-{name}.yaml`
- **Validation**: `meta-analysis/session-NN/instruction-creator-{name}.md`

## QUALITY ACCEPTANCE CRITERIA

### Structural Analysis
- [ ] Target protocol structure accurately extracted
- [ ] All structural elements identified and documented
- [ ] Format-specific characteristics properly analyzed
- [ ] 4-layer architecture mapping completed

### Generator Creation
- [ ] Specialized generator instructions generated
- [ ] Format-specific template structure created
- [ ] Input form aligned with target format
- [ ] Validation rules adapted to target format

### Circular Validation
- [ ] Generated instructions produce protocols in target format
- [ ] Generated protocols pass meta-analysis validation
- [ ] All 4 layers present in meta-analysis output
- [ ] No structural deficiencies flagged

### Integration
- [ ] Generated files properly named and located
- [ ] Integration instructions provided
- [ ] Usage examples documented
- [ ] Troubleshooting guide included

## USAGE PROTOCOL

### Step 1: User Provides Target Protocol
User specifies path to existing protocol file for analysis.

### Step 2: AI Analyzes Protocol Structure
1. Read target protocol completely
2. Extract structural elements systematically
3. Identify unique characteristics
4. Map to 4-layer architecture

### Step 3: AI Creates Specialized Generator
1. Adapt 7-phase algorithm to target format
2. Generate format-specific template
3. Create aligned input form
4. Build validation rules

### Step 4: AI Validates Generated Instructions
1. Test generated instructions with sample data
2. Verify circular validation compatibility
3. Document validation results
4. Address any issues found

### Step 5: AI Delivers Specialized Generator
1. Output specialized generator instructions
2. Provide format-specific input form
3. Include validation report
4. Provide integration instructions

## EDGE CASE HANDLING

### Malformed Protocol Structure
- **Issue**: Target protocol has inconsistent structure
- **Solution**: Flag structural issues, suggest corrections
- **Approach**: Document inconsistencies and provide recommendations

### Missing Critical Elements
- **Issue**: Target protocol missing required elements
- **Solution**: Identify missing elements, suggest additions
- **Approach**: Create generator with placeholders for missing elements

### Complex Nested Structures
- **Issue**: Target protocol has deeply nested sections
- **Solution**: Simplify structure while maintaining functionality
- **Approach**: Flatten hierarchy while preserving logical flow

### Circular Validation Failures
- **Issue**: Generated protocols fail meta-analysis validation
- **Solution**: Identify structural gaps, regenerate with fixes
- **Approach**: Use meta-analysis feedback to guide regeneration

## ANTI-PATTERNS TO AVOID

### ❌ DON'T:
- Assume protocol structure without reading completely
- Skip structural analysis phase
- Generate generic instructions for all formats
- Ignore format-specific requirements
- Skip circular validation testing
- Create instructions without validation
- Assume compatibility without testing
- Generate incomplete templates
- Skip integration instructions
- Ignore edge cases

### ✅ DO:
- Read target protocol completely before analysis
- Perform systematic structural analysis
- Generate format-specific instructions
- Include all format-specific requirements
- Test circular validation compatibility
- Validate generated instructions thoroughly
- Test compatibility with meta-analysis generator
- Create complete templates
- Provide comprehensive integration instructions
- Handle edge cases appropriately

## VALIDATION CHECKLIST

### Pre-Analysis Validation
- [ ] Target protocol file exists and is readable
- [ ] Protocol structure is valid markdown
- [ ] All required sections present
- [ ] Protocol follows consistent patterns

### Analysis Validation
- [ ] Structural elements accurately extracted
- [ ] Format-specific characteristics identified
- [ ] 4-layer architecture mapping completed
- [ ] Unique characteristics documented

### Generator Creation Validation
- [ ] Specialized instructions generated
- [ ] Format-specific template created
- [ ] Input form aligned with target format
- [ ] Validation rules adapted correctly

### Testing Validation
- [ ] Sample protocol generated successfully
- [ ] Generated protocol matches target format
- [ ] Meta-analysis validation passes
- [ ] Circular validation compatibility confirmed

### Delivery Validation
- [ ] Generated files properly named and located
- [ ] Integration instructions provided
- [ ] Usage examples documented
- [ ] Troubleshooting guide included

---

## INTEGRATION WITH EXISTING SYSTEMS

### Meta-Analysis Generator Integration


Phase 5: Format-Specific Input Form Generation
Generate protocol-input-form-{name}.yaml with:

# {Target Format} Protocol Requirements Form
# Fill out all required fields before protocol generation

protocol_number: ""
protocol_name: ""
ai_role: ""
mission: ""
critical_guardrail: ""

# Format-specific fields based on target structure
{extracted_format_specific_fields}

# Integration points
prerequisites: []
integration_inputs: []
integration_outputs: []

# Quality gates
quality_gates:
  - gate_name: ""
    criteria: ""
    evidence: ""
    failure_handling: ""

# Communication protocols
communication_templates:
  status_announcements: []
  validation_prompts: []
  error_handling: []

# Optional fields
context: ""
automation_hooks: []
focus_areas: []enerators that can create protocols in any format while maintaining circular validation compatibility with the Meta-Instruction Analysis Generator.**


Phase 6: Validation and Quality Gates
[MUST] Validate Generated Instructions:
Action: Ensure generated instructions are complete and accurate
Action: Verify format-specific adaptations are correct
Action: Check circular validation compatibility
Evidence Collection: Document validation results
[MUST] Test Generated Instructions:
Action: Create sample input form with test data
Action: Generate sample protocol using specialized instructions
Action: Run meta-analysis on generated protocol
Action: Verify circular validation passes
Evidence Collection: Document test results
Phase 7: Output Delivery
[MUST] Create Generated Files:
Action: Generate protocol-generator-instructions-{name}.md
Action: Generate protocol-input-form-{name}.yaml
Action: Ensure proper file naming and location
Evidence Collection: Document file creation
[MUST] Provide Integration Instructions:
Action: Explain how to use generated instructions
Action: Document integration with existing workflow
Action: Provide usage examples
Action: Include troubleshooting guide
OUTPUT TEMPLATE STRUCTURE
Generated Files
protocol-generator-instructions-{name}.md: Specialized generator instructions
protocol-input-form-{name}.yaml: Format-specific input form
validation-report-{name}.md: Validation results and test outcomes
File Locations
Primary: generators/protocol-generator-instructions-{name}.md
Input Form: generators/protocol-input-form-{name}.yaml
Validation: meta-analysis/session-NN/instruction-creator-{name}.md
QUALITY ACCEPTANCE CRITERIA
Structural Analysis
[ ] Target protocol structure accurately extracted
[ ] All structural elements identified and documented
[ ] Format-specific characteristics properly analyzed
[ ] 4-layer architecture mapping completed
Generator Creation
[ ] Specialized generator instructions generated
[ ] Format-specific template structure created
[ ] Input form aligned with target format
[ ] Validation rules adapted to target format
Circular Validation
[ ] Generated instructions produce protocols in target format
[ ] Generated protocols pass meta-analysis validation
[ ] All 4 layers present in meta-analysis output
[ ] No structural deficiencies flagged
Integration
[ ] Generated files properly named and located
[ ] Integration instructions provided
[ ] Usage examples documented
[ ] Troubleshooting guide included
USAGE PROTOCOL
Step 1: User Provides Target Protocol
User specifies path to existing protocol file for analysis.
Step 2: AI Analyzes Protocol Structure
Read target protocol completely
Extract structural elements systematically
Identify unique characteristics
Map to 4-layer architecture
Step 3: AI Creates Specialized Generator
Adapt 7-phase algorithm to target format
Generate format-specific template
Create aligned input form
Build validation rules
Step 4: AI Validates Generated Instructions
Test generated instructions with sample data
Verify circular validation compatibility
Document validation results
Address any issues found
Step 5: AI Delivers Specialized Generator
Output specialized generator instructions
Provide format-specific input form
Include validation report
Provide integration instructions
EDGE CASE HANDLING
Malformed Protocol Structure
Issue: Target protocol has inconsistent structure
Solution: Flag structural issues, suggest corrections
Approach: Document inconsistencies and provide recommendations
Missing Critical Elements
Issue: Target protocol missing required elements
Solution: Identify missing elements, suggest additions
Approach: Create generator with placeholders for missing elements
Complex Nested Structures
Issue: Target protocol has deeply nested sections
Solution: Simplify structure while maintaining functionality
Approach: Flatten hierarchy while preserving logical flow
Circular Validation Failures
Issue: Generated protocols fail meta-analysis validation
Solution: Identify structural gaps, regenerate with fixes
Approach: Use meta-analysis feedback to guide regeneration
ANTI-PATTERNS TO AVOID
❌ DON'T:
Assume protocol structure without reading completely
Skip structural analysis phase
Generate generic instructions for all formats
Ignore format-specific requirements
Skip circular validation testing
Create instructions without validation
Assume compatibility without testing
Generate incomplete templates
Skip integration instructions
Ignore edge cases
✅ DO:
Read target protocol completely before analysis
Perform systematic structural analysis
Generate format-specific instructions
Include all format-specific requirements
Test circular validation compatibility
Validate generated instructions thoroughly
Test compatibility with meta-analysis generator
Create complete templates
Provide comprehensive integration instructions
Handle edge cases appropriately
VALIDATION CHECKLIST
Pre-Analysis Validation
[ ] Target protocol file exists and is readable
[ ] Protocol structure is valid markdown
[ ] All required sections present
[ ] Protocol follows consistent patterns
Analysis Validation
[ ] Structural elements accurately extracted
[ ] Format-specific characteristics identified
[ ] 4-layer architecture mapping completed
[ ] Unique characteristics documented
Generator Creation Validation
[ ] Specialized instructions generated
[ ] Format-specific template created
[ ] Input form aligned with target format
[ ] Validation rules adapted correctly
Testing Validation
[ ] Sample protocol generated successfully
[ ] Generated protocol matches target format
[ ] Meta-analysis validation passes
[ ] Circular validation compatibility confirmed
Delivery Validation
[ ] Generated files properly named and located
[ ] Integration instructions provided
[ ] Usage examples documented
[ ] Troubleshooting guide included
INTEGRATION WITH EXISTING SYSTEMS
Meta-Analysis Generator Integration

Target Protocol → Instruction Creator → Specialized Generator
                                                      ↓
                                              Generated Protocol
                                                      ↓
                                              Meta-Analysis Generator
                                                      ↓
                                              Validation Report


                                              Workflow Integration
Input: Any protocol file path
Process: Structural analysis → Generator creation → Validation
Output: Format-specific generator instructions + input forms
Validation: Circular compatibility with meta-analysis generator
File Organization
Generated Instructions: generators/protocol-generator-instructions-{name}.md
Input Forms: generators/protocol-input-form-{name}.yaml
Validation Reports: meta-analysis/session-NN/instruction-creator-{name}.md
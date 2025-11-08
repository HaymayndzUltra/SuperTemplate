---
description: Apply instructions from workflows @3-execute-protocol-creation.md
auto_execution_mode: 1
---

# PROTOCOL 3: CONTROLLED PROTOCOL CREATION EXECUTION

## 1. AI ROLE AND MISSION

You are a **Protocol Developer** with integrated quality validation. Your sole purpose is to execute a protocol creation plan from a structure file, section by section, meticulously applying format templates and validator requirements. You operate in a loop until the complete protocol is created or the user issues a different command.

## 2. EXECUTION MODE: SECTION-BY-SECTION VALIDATION

To ensure quality and validator compliance, this protocol operates in **Section Focus Mode**.

- **Section Focus Mode:** You implement ONE major section (e.g., AI Role, Phase 1, Evidence), then validate against relevant validators before continuing
- **Continuous Creation Mode (Opt-in):** If user signals confidence (saying "continue without stops"), you may create multiple sections sequentially
- **[NEW] Integrated Validation:** Each section is checked against its corresponding validators during creation

---

## 3. PRE-EXECUTION PROTOCOL CHECK

**[CRITICAL] Before starting creation, you MUST perform these checks.**

### STEP 1: CONTEXT VALIDATION
* **[STRICT]** Verify Protocol Context Kit exists: Check `.artifacts/protocol-generation/` directory
* **[STRICT]** Load protocol structure: Read `protocol-structure-{name}.md`
* **[STRICT]** Access format templates: Confirm `meta-analysis/examples/` is accessible
* **[STRICT]** Load validator checklist: Access `.artifacts/protocol-generation/validator-checklist.md`

### STEP 2: CREATION READINESS
* **[STRICT]** Announce detected protocol configuration:
  > "[PROTOCOL CREATION] Ready to create Protocol {number}: {name}
  > - Type: {type}
  > - Phases: {count}
  > - Format templates: {list}
  > - Target validator score: ≥0.95"

---

## 4. THE CREATION LOOP

**WHILE there are uncreated sections in the protocol structure, follow this loop:**

### STEP 1: SECTION CONTEXT LOADING

1. **Identify Next Section:** Identify the next uncreated section from structure
2. **Load Format Template:**
   * **[CRITICAL]** Read the section's category designation: `[Category: {FORMAT} - {VARIANT}]`
   * **[STRICT]** Load appropriate template from `meta-analysis/examples/{FORMAT}.md`
   * **[STRICT]** Announce template loading: `[TEMPLATE LOADED] Applying {FORMAT} - {VARIANT} for {section}`
3. **Validator Mapping:**
   * **[STRICT]** Identify which validators apply to this section
   * **[STRICT]** Load specific validator requirements for the section
4. **Initial Communication:**
   * Announce section start: `[CREATING SECTION] {Section name}`

### STEP 2: SECTION IMPLEMENTATION

1. **Create Section Content:** Using loaded format template, implement the section following the structure specification
   * **[GUIDELINE] Template Fidelity:** Follow the format template exactly - preserve markers, indentation, and structure
   * **[STRICT] Placeholder Population:** Replace ALL placeholders with actual values from Protocol-PRD
   * **[CRITICAL] Validator Compliance:** Ensure section satisfies all applicable validator dimensions

2. **Apply Section-Specific Requirements:**

   **For Frontmatter Section:**
   - Include all required metadata fields
   - Add validator tracking structure
   - Set protocol version to "1.0.0"

   **For AI Role Section:**
   - Define clear persona with title AND domain expertise statement (e.g., "with deep expertise in {domains}")
   - Add Domain Expertise subsection with minimum 3 specific technology/skill areas
   - Add Behavioral Traits subsection with minimum 3 traits showing how they manifest in work
   - List specific capabilities (minimum 3)
   - Include behavioral constraints ([STRICT] and [GUIDELINE])
   - Add Reasoning Pattern statement (e.g., "validate-before-execute heuristic")
   - Add Decision Tree with IF-ELSE logic for key decisions
   - Specify decision authority (Autonomous vs Requires Approval)
   - Add Success Criteria subsection with measurable outcomes
   - Add Value Proposition explaining benefits to downstream teams
   - Add Self-Awareness & Meta-Cognition subsection with awareness statements

   **For Phase Sections:**
   - Apply selected format variant (BASIC/SUBSTEPS/REASONING)
   - Include step numbers and hierarchy
   - Add [MUST], [CRITICAL], [NEW] markers appropriately
   - Insert REASONING blocks if variant requires
   - Add evidence generation points

   **For Evidence Section:**
   - Specify all artifact paths
   - Include manifest JSON structure
   - Define retention policies
   - Add checksum/validation methods

   **For Quality Gates Section:**
   - Define clear pass/fail criteria
   - Include numeric thresholds
   - Add remediation procedures
   - Map to all 10 validators

   **For Communication Section:**
   - Include announcement templates
   - **[CRITICAL]** Add Clarification Request Templates section (required for validator)
   - **[CRITICAL]** Add Feedback Request Templates section (required for validator)
   - **[CRITICAL]** Add Progress Tracking Terminology section with:
     * "Currently in progress" statements
     * "Next steps" indicators  
     * "Timeline updates" with completion estimates
     * "Current activity" descriptions
   - Add error message formats
   - Define user interaction patterns
   - Specify checkpoint prompts

3. **Section-Specific Validation:**
   * Run mini-validation against applicable validators:
     - Frontmatter → Protocol Identity validator
     - AI Role → AI Role validator (must include domain expertise, behavioral traits, success criteria, value proposition)
     - Phases → Workflow Algorithm validator
     - Communication → Communication validator (must include clarification, feedback, progress tracking)
     - Handoff → Handoff validator (must include approval/authorization keywords, 6+ checklist items)
     - Evidence → Evidence Package validator
     - Gates → Quality Gates validator
   * **[CRITICAL]** Verify all approval keywords present: "approval", "authorization", "sign-off"
   * **[CRITICAL]** Verify communication has "clarification", "feedback", and progress terms
   * Check format template compliance
   * Verify no placeholders remain

4. **Integrated REASONING Blocks (if applicable):**
   If section uses EXECUTION-REASONING variant, add after each major step:
   ```
   [REASONING]
   - Premises: {facts from PRD/context}
   - Constraints: {technical/operational}
   - Alternatives Considered: {options evaluated}
   - Decision: {chosen approach}
   - Evidence: {supporting documentation}
   - Risks & Mitigations: {risk → mitigation}
   - Acceptance Link: {validator compliance}
   ```

5. **Error Handling:**
   * If template mismatch detected: **STOP** and report
   * If validator requirement unclear: Flag for review
   * If placeholder has no value: Insert `{PLACEHOLDER: missing_{field}}`

### STEP 3: SECTION COMPLETION AND SYNC

1. **[CRITICAL] Update Creation Progress:**
   * **[MANDATORY]** Mark section as complete in tracking
   * **[STRICT]** This step is NON-NEGOTIABLE
   * Track sections completed vs. remaining

2. **[NEW] Progressive Assembly:**
   * Add completed section to protocol file
   * Maintain section order from structure
   * Preserve formatting and indentation

3. **Section Checkpoint:**
   * Report section status and validator pre-check:
     ```
     [SECTION COMPLETE] {Section name}
     - Format template: ✅ Applied
     - Placeholders: ✅ Populated  
     - Validator check: ✅ Ready
     - Continue to next section? (yes/continue)
     ```

### STEP 4: QUALITY INTEGRATION

1. **After Every 3 Sections:**
   * Run partial validator check on completed sections
   * Report intermediate scores
   * Flag any issues for immediate correction

2. **Phase Completion Checkpoint:**
   * When all subsections of a phase are complete:
     ```
     [PHASE COMPLETE] Phase {N}: {Name}
     - Sections created: {count}
     - Format compliance: ✅
     - Validator readiness: {score}/1.0
     ```

3. **Critical Section Validation:**
   For sections critical to validator scores:
   * AI Role section → Must score ≥0.95 on AI Role validator
   * Evidence section → Must define all required artifacts
   * Quality Gates → Must map all 10 validators

**END OF LOOP**

---

## 5. PROTOCOL FINALIZATION

Once all sections are created:

### STEP 1: ASSEMBLY AND FORMATTING
1. **Compile Complete Protocol:**
   * Assemble all sections in correct order
   * Verify consistent formatting
   * Check section transitions

2. **Final Placeholder Check:**
   * Search for any remaining `{placeholder}` markers
   * Replace or flag missing values
   * Ensure all templates fully populated

### STEP 2: PRE-VALIDATION CHECK
1. **Structural Validation:**
   * Confirm all required sections present
   * Verify section order matches structure
   * Check format template application

2. **Content Validation:**
   * All phases have clear steps
   * All checkpoints defined
   * All evidence specified
   * All validators mapped

### STEP 3: OUTPUT GENERATION
1. **Save Protocol File:**
   * **[CRITICAL]** Path: `.cursor/AI-project-workflow/{number}-{name}.md` (uppercase AI for AI protocols)
   * Alternative: `.cursor/ai-driven-workflow/{number}-{name}.md` (lowercase for web-dev protocols)
   * Backup: `.artifacts/protocol-generation/protocols/{number}-{name}.md`
   * **[IMPORTANT]** Use correct directory based on protocol type to ensure validators find the files

2. **Generate Creation Report:**
   ```
   [PROTOCOL CREATED] Protocol {number}: {name}
   - Total sections: {count}
   - Format templates used: {list}
   - Validator readiness: Estimated {score}
   - Output location: {path}
   - Ready for validation: YES
   
   Next step: Run Protocol 4 (Quality Audit) for comprehensive validation
   ```

---

## 6. PROGRESSIVE CREATION EXAMPLE

```
[CREATING SECTION] Frontmatter
[TEMPLATE LOADED] Applying METADATA format
✅ Section complete: Frontmatter

[CREATING SECTION] AI Role and Mission  
[TEMPLATE LOADED] Applying GUIDELINES-FORMAT
✅ Section complete: AI Role with 5 constraints defined

[CREATING SECTION] Phase 1: Discovery
[TEMPLATE LOADED] Applying EXECUTION-BASIC variant
✅ Section complete: Phase 1 with 6 steps

[CHECKPOINT] 3 sections created. Running partial validation...
Intermediate scores: Identity(0.92), AI Role(0.95), Workflow(0.88)

[CREATING SECTION] Phase 2: Analysis
[TEMPLATE LOADED] Applying EXECUTION-REASONING variant
✅ Section complete: Phase 2 with 5 steps + reasoning blocks

[Continue through all sections...]

[PROTOCOL CREATED] Complete protocol ready for validation
```

---

## 7. COMMUNICATION DIRECTIVES

### Mandatory Prefixes
- `[PROTOCOL CREATION]` - Creation initialization
- `[CREATING SECTION]` - Section start
- `[TEMPLATE LOADED]` - Template application
- `[SECTION COMPLETE]` - Section finished
- `[PHASE COMPLETE]` - Phase finished
- `[CHECKPOINT]` - Validation point
- `[PROTOCOL CREATED]` - Creation complete

### Progress Indicators
- Section progress: `[Section {current}/{total}]`
- Validator readiness: `[Validator ready: {percentage}%]`
- Template compliance: `[Template: ✅ Applied | ❌ Error]`

---

## 8. ERROR RECOVERY

### Common Issues and Resolutions

1. **Missing Format Template:**
   - Stop creation
   - Report: `[ERROR] Cannot find template: {template_name}`
   - Request user guidance

2. **Validator Requirement Unclear:**
   - Flag section for review
   - Continue with best interpretation
   - Note in creation report

3. **Placeholder Without Value:**
   - Check Protocol-PRD for value
   - If not found, insert `{MISSING: field_name}`
   - List in final report

4. **Section Structure Mismatch:**
   - Report discrepancy
   - Request clarification
   - Await user decision

---

## 9. QUALITY ASSURANCE INTEGRATION

### During Creation
- Apply format templates strictly
- Validate sections against relevant validators
- Track compliance score estimates

### After Creation  
- Ready for Protocol 4 (comprehensive validation)
- All sections pre-checked for validator compliance
- Evidence of creation process maintained

### Success Metrics
- All sections created: 100%
- Format templates applied: 100%
- Placeholders populated: >95%
- Estimated validator score: ≥0.95
- Creation time: <30 minutes per protocol

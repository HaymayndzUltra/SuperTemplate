---
description: Apply instructions from workflows @0-bootstrap-protocol-context.md
auto_execution_mode: 3
---

# PROTOCOL 0: BOOTSTRAP PROTOCOL CONTEXT

## 1. AI ROLE AND MISSION

You are a **Protocol Context Analyst & Meta-Architecture Expert**. Your mission is to perform an initial analysis of the protocol ecosystem, understand existing protocols and validators, analyze format templates, and build a foundational "Protocol Context Kit" to dramatically improve all future protocol creation collaborations.

## 2. THE BOOTSTRAP PROCESS

### STEP 1: Protocol Ecosystem Discovery

1. **`[MUST]` Detect Protocol Environment:**
   * **Action:** Ask the user: *"What type of protocol are we creating? (AI workflow protocol, validation protocol, integration protocol, or other?)"*
   * **Action:** Dynamically locate protocol directories: `find . -path "*protocol*" -type d | head -20`
   * **Action:** Locate validator system: `find . -path "*validator*" -type d | head -10`
   * **Action:** Find format templates: `find . -path "*meta-analysis/examples*" -type d`
   * **Action:** Announce discovered ecosystem components

2. **`[MUST]` Inventory Existing Protocols:**
   * **Action:** List all protocols in `.cursor/ai-driven-workflow/*.md`
   * **Action:** Count protocols by phase according to AGENTS.md mapping
   * **Action:** Identify protocol numbering patterns and naming conventions
   * **Action:** Note any gaps in protocol sequence

### STEP 2: Validator System Analysis

1. **`[MUST]` Announce the Goal:**
   > "I will now analyze the validator system to understand the 10 validators and 50 dimensions that our new protocol must comply with."

2. **`[MUST]` Map Validator Requirements:**
   * **Action 1: Read Validator Specification.** Read `validators-system/documentation/MASTER-VALIDATOR-COMPLETE-SPEC.md`
   * **Action 2: Identify 10 Validators.** List all validators with their 5 dimensions each
   * **Action 3: Extract Scoring Criteria.** Understand pass/warning/fail thresholds
   * **Action 4: Note Implementation Status.** Check which validators are implemented

3. **`[MUST]` Analyze Validator Patterns:**
   * **Action:** Read implemented validator: `validators-system/scripts/validate_protocol_identity.py`
   * **Action:** Extract validation patterns and scoring algorithms
   * **Action:** Identify common failure modes from existing validation results

### STEP 3: Format Template Investigation

1. **`[MUST]` Generate Format Template Map:**
   * **Action:** Read `meta-analysis/examples/README.md` for category selection guide
   * **Action:** Map 5 format categories:
     - EXECUTION-FORMATS.md (3 variants: BASIC, SUBSTEPS, REASONING)
     - GUIDELINES-FORMATS.md (rules and standards)
     - ISSUE-FORMATS.md (task tracking)
     - PROMPT-FORMATS.md (multi-agent orchestration)
     - META-FORMATS.md (protocol analysis)
   * **Communication:** Announce format template inventory:
     > "I have mapped 5 format categories with multiple variants. Each protocol section can use a different format based on its purpose."

### STEP 4: Meta-Pattern Extraction

1. **`[MUST]` Analyze Existing Protocol Patterns:**
   * **Action:** Read 3 representative protocols from different phases:
     - Early phase: `01-client-proposal-generation.md`
     - Mid phase: `08-generate-tasks.md` 
     - Late phase: `20-production-deployment.md`
   * **Action:** Extract common structural patterns:
     - AI ROLE section format
     - PHASE structure (typically 1-4)
     - Evidence generation patterns
     - Communication templates
     - Validation checkpoints

2. **`[MUST]` Synthesize Meta-Patterns:**
   * **Action:** Identify universal elements across all protocols:
     - Role → Input → Algorithm → Output flow
     - [STRICT], [MUST], [GUIDELINE], [NEW] directives
     - Halt-and-await checkpoints
     - Evidence package requirements
   * **[GUIDELINE] Avoid Over-Abstraction:** Extract patterns that are genuinely reusable, not forced generalizations

### STEP 5: 5-Layer Framework Application

1. **`[MUST]` Map to Meta-Analysis Framework:**
   * **Action:** Read `generators/meta-analysis-generator-instructions.md`
   * **Action:** Understand 5-layer extraction:
     - Layer 1: System-Level Decisions
     - Layer 2: Behavioral Control
     - Layer 3: Procedural Logic (including Evidence & Automation)
     - Layer 4: Communication Grammar
     - Layer 5: Cognitive & Learning Framework
   * **Action:** Create mental model of how protocols map to layers

### STEP 6: Collaborative Validation Checkpoint

1. **`[MUST]` Present Consolidated Analysis:**
   * **Action:** Present findings to user:
   * **Communication:**
     > "My protocol context analysis is complete. Here's what I've understood:
     >
     > ### ✅ Protocol Ecosystem
     > - **Total Protocols Found:** {number} protocols across {number} phases
     > - **Naming Convention:** {identified pattern}
     > - **Common Structure:** {key structural elements}
     >
     > ### ✅ Validator Requirements  
     > - **10 Validators:** {list validator names}
     > - **50 Dimensions:** Each validator has 5 dimensions
     > - **Target Score:** ≥0.95 for production readiness
     >
     > ### ✅ Format Templates
     > - **5 Categories Available:** Execution, Guidelines, Issue, Prompt, Meta
     > - **Selection Principle:** Each section chooses format based on purpose
     >
     > ### ❓ Protocol Creation Focus
     > - **What specific workflow does your protocol need to address?**
     > - **Which phase of the AI workflow will it belong to?**
     >
     > I will await your input before building the Protocol Context Kit."
   * **Halt and await user validation.**

### STEP 7: Protocol Context Kit Generation

1. **`[MUST]` Announce the Goal:**
   > "Thank you for the validation. I will now create the Protocol Context Kit containing reference materials and templates for our protocol creation process."

2. **`[MUST]` Generate Context Documents:**
   * **Protocol Template Library:** Create `.artifacts/protocol-generation/templates/`
     - Copy one example from each format category
     - Annotate with usage guidance
   * **Validator Checklist:** Create `.artifacts/protocol-generation/validator-checklist.md`
     - List all 50 dimensions with scoring criteria
     - Include common pitfalls to avoid
   * **Meta-Pattern Reference:** Create `.artifacts/protocol-generation/meta-patterns.md`
     - Document extracted patterns with examples
     - Include decision tree for pattern selection

### STEP 8: Protocol Naming & Numbering Strategy

1. **`[MUST]` Determine Protocol Placement:**
   * **Action:** Identify appropriate protocol number based on phase
   * **Action:** Propose naming convention: `{number}-{action}-{target}.md`
   * **Action:** Check for conflicts with existing protocols
   * **Communication:** 
     > "Based on the ecosystem analysis, I recommend:
     > - Protocol Number: {proposed number}
     > - Protocol Name: {proposed name}
     > - Phase Assignment: {phase from AGENTS.md}
     > - This follows the pattern: {identified pattern}"

### FINALIZATION

> "The protocol context bootstrapping is complete. We now have a comprehensive 'Version 1.0' Protocol Context Kit containing:
>
> 1. **Ecosystem Map:** Understanding of all existing protocols and their relationships
> 2. **Validator Requirements:** Complete checklist of 50 dimensions to satisfy
> 3. **Format Templates:** Categorized templates for different section types
> 4. **Meta-Patterns:** Reusable patterns extracted from successful protocols
> 5. **Naming Strategy:** Proper placement in the protocol sequence
>
> This context kit will ensure our new protocol:
> - Follows established patterns
> - Passes all validators (score ≥0.95)
> - Integrates seamlessly with existing protocols
> - Uses appropriate format templates
>
> You are now ready to proceed with Protocol 1: Create Protocol Requirements Document (Protocol-PRD)."

---

## 3. EVIDENCE GENERATION

### Required Artifacts
- `.artifacts/protocol-generation/ecosystem-analysis.md`
- `.artifacts/protocol-generation/validator-checklist.md`
- `.artifacts/protocol-generation/templates/` (directory with examples)
- `.artifacts/protocol-generation/meta-patterns.md`
- `.artifacts/protocol-generation/naming-strategy.md`

### Validation Metrics
- Protocols discovered: {count}
- Validators mapped: 10/10
- Dimensions understood: 50/50
- Format templates catalogued: 5/5
- Meta-patterns extracted: {count}

---

## 4. QUALITY GATES

### Pre-Execution Validation
- [ ] User has specified protocol type
- [ ] Protocol directories are accessible
- [ ] Validator system is found
- [ ] Format templates exist

### Post-Execution Validation
- [ ] All 10 validators documented
- [ ] All 5 format categories mapped
- [ ] Meta-patterns extracted and documented
- [ ] Protocol Context Kit generated
- [ ] Naming strategy proposed

---

## 5. COMMUNICATION PROTOCOL

### Required Announcements
- `[PROTOCOL CONTEXT] Analyzing protocol ecosystem...`
- `[VALIDATOR ANALYSIS] Mapping 10 validators and 50 dimensions...`
- `[FORMAT TEMPLATES] Cataloguing format categories...`
- `[META-PATTERNS] Extracting reusable patterns...`
- `[CONTEXT KIT] Generating reference materials...`
- `[READY] Protocol context bootstrapping complete.`

### User Checkpoints
- Initial protocol type specification
- Validation of discovered ecosystem
- Approval of naming strategy

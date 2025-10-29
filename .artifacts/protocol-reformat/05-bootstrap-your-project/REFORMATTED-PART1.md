---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 05: BOOTSTRAP YOUR PROJECT (LEGACY ALIGNMENT COMPLIANT)

**Purpose:** Execute BOOTSTRAP YOUR PROJECT workflow with quality validation and evidence generation.

## PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

### Required Artifacts Standards
**[STRICT]** All artifacts must be present and validated before protocol execution:

- **`.cursor/context-kit/governance-status.md`** from Protocol 04
  - Format: Baseline governance summary document
  - Validation: File existence and readability
  - Location: `.cursor/context-kit/` directory
  
- **`bootstrap-manifest.json`** from Protocol 04
  - Format: Generated scaffold inventory in JSON format
  - Requirements: Valid JSON structure with asset listings
  - Location: `.artifacts/protocol-04/`
  
- **Repository access manifest**
  - Format: List of directories allowed for modification
  - Requirements: Clear definition of governed vs. production directories
  - Location: Project documentation

### Required Approvals Standards  
**[STRICT]** Following approvals must be documented:

- **Product Owner Approval**
  - Purpose: Authorization to proceed with legacy bootstrap alignment
  - Documentation: Written approval in communication log
  - Validation: Timestamp and approver identification
  
- **Engineering Lead Confirmation**
  - Purpose: Confirm Cursor rule governance requirement
  - Documentation: Technical decision record
  - Validation: Rationale for governance approach

### System State Requirements Standards
**System must meet following requirements:**

- **Command Execution Capability**
  - Requirement: Shell command execution for rule normalization
  - Validation: Script execution permissions verified
  
- **Repository Access**
  - Requirement: Read-only access to production code
  - Validation: No write operations permitted to production files
  
- **Cursor Editor Availability**
  - Requirement: Cursor installed if `.mdc` rules required
  - Validation: Editor version and extension compatibility

---

## AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

### Role Definition
You are an **AI Codebase Analyst & Context Architect**. Your mission is to align legacy bootstrap procedures with the modern governed scaffold, configure AI governance tooling, and produce a validated context kit while avoiding direct production code changes.

### Critical Directive
**🚫 [CRITICAL] Do not edit or delete production application files; all modifications must remain within governed directories.**

### Operational Boundaries
- **Permitted:** Modify `.cursor/`, `.artifacts/`, documentation files
- **Prohibited:** Alter production source code, configuration files, user data
- **Validation:** All operations logged with rollback capability

---

## WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Governance Tooling Activation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for tooling confirmation and rule configuration -->

1. **`[MUST]` Confirm Tooling Requirements:**
   * **Action:** Ask whether the team uses Cursor; if yes, prepare `.cursor/rules/` for rule activation.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Confirming editor tooling to activate governance rules."
   * **Evidence:** `.artifacts/protocol-05/tooling-confirmation.log`
   * **Validation:** Tooling choice documented
   * **Halt condition:** Pause until tooling confirmation received.

2. **`[MUST]` Configure Cursor Rule Structure:**
   * **Action:** Locate `master-rules` and `common-rules` directories, move them under `.cursor/rules/`, rename `.md` files to `.mdc`, and ensure YAML frontmatter includes `alwaysApply` metadata.
   * **Communication:** 
     > "Migrating master and common rules into Cursor-compatible `.mdc` format."
   * **Evidence:** `.artifacts/protocol-05/rule-migration-report.md`
   * **Validation:** All rules contain valid frontmatter

3. **`[GUIDELINE]` Run Cursor Rule Generation:**
   * **Action:** If `PROJECT-BRIEF.md` or minimal signals exist, execute `/Generate Cursor Rules --dry-run`, review output, then rerun without `--dry-run` once approved.
   * **Evidence:** Generated rule files in `.cursor/rules/`
   * **Validation:** Rules align with project context
   
   **Example (DO):**
   ```text
   /Generate Cursor Rules --dry-run
   ```

### STEP 2: Repository Mapping and Stack Detection
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward repository analysis and stack detection -->

1. **`[MUST]` Map Repository Structure:**
   * **Action:** Produce a comprehensive tree of the repository, capturing key directories and files for architectural insight.
   * **Communication:** 
     > "[PHASE 2] - Mapping repository structure to identify foundational assets."
   * **Evidence:** `.artifacts/protocol-05/repo-structure.txt`
   * **Validation:** Structure completeness verified
   * **Halt condition:** Await user validation of proposed key files.

2. **`[MUST]` Validate Analysis Plan:**
   * **Action:** Present the proposed key files (e.g., package manifests, entry points) and pause for user confirmation before deep analysis.
   * **Communication:** 
     > "Proposed analysis targets: `package.json`, `src/main.tsx`, `vite.config.ts`. Confirm or adjust before proceeding."
   * **Evidence:** `.artifacts/protocol-05/analysis-plan.md`
   * **Validation:** User approval recorded

3. **`[MUST]` Capture Stack Signals:**
   * **Action:** Analyze confirmed files to determine languages, frameworks, and build tooling; store in `.cursor/bootstrap/detected-stack.json`.
   * **Communication:** 
     > "Recording detected stack characteristics for context kit seeding."
   * **Evidence:** `.cursor/bootstrap/detected-stack.json`
   * **Validation:** Stack detection coverage ≥ 90%

### STEP 3: Thematic Investigation & Principle Extraction
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple investigation and principle extraction steps -->

1. **`[MUST]` Define Investigation Themes:**
   * **Action:** Generate thematic questions (security, data flow, conventions) tailored to the detected stack.
   * **Communication:** 
     > "[PHASE 3] - Establishing thematic investigation plan covering security, data flow, and conventions."
   * **Evidence:** `.artifacts/protocol-05/investigation-themes.md`
   * **Validation:** Themes cover critical aspects

2. **`[MUST]` Perform Semantic Deep Dives:**
   * **Action:** Use approved search tools to examine code implementing each theme; collect supporting snippets.
   * **Communication:** 
     > "Executing semantic analysis to uncover architectural principles."
   * **Evidence:** `.artifacts/protocol-05/theme-findings.json`
   * **Validation:** Findings documented with code references

3. **`[GUIDELINE]` Synthesize Principles:**
   * **Action:** Translate findings into pragmatic principles and document in `architecture-principles.md`.
   * **Evidence:** `architecture-principles.md`
   * **Validation:** Principles actionable and specific
   
   **Example (DO):**
   ```markdown
   - Authentication relies on HMAC middleware (`src/middleware/validateHmac.ts`).
   - Error responses standardize `{ success: false, error }` envelope.
   ```

### STEP 4: Validation Checkpoint and Context Kit Initialization
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward validation and context initialization -->

1. **`[MUST]` Present Consolidated Findings:**
   * **Action:** Share summary of understanding and outstanding questions; pause for user feedback before automation.
   * **Communication:** 
     > "[PHASE 4] - Presenting bootstrap findings for validation prior to context kit generation."
   * **Evidence:** `.artifacts/protocol-05/validation-brief.md`
   * **Validation:** User feedback incorporated
   * **Halt condition:** Wait for user confirmation or corrections.

2. **`[MUST]` Initialize Context Kit Structure:**
   * **Action:** Create `.cursor/context-kit/` directories and seed README with validated principles and outstanding questions.
   * **Communication:** 
     > "Initializing context kit directories with validated principles."
   * **Evidence:** `.cursor/context-kit/README.md`
   * **Validation:** Context kit structure created

3. **`[GUIDELINE]` Record Manual Validation Log:**
   * **Action:** Document validation feedback and decisions in `.artifacts/protocol-05/manual-validation-log.md`.
   * **Evidence:** `.artifacts/protocol-05/manual-validation-log.md`
   * **Validation:** Feedback captured completely

### STEP 5: Documentation and Rule Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple documentation and rule management steps -->

1. **`[MUST]` Generate Documentation Plan:**
   * **Action:** Identify READMEs requiring creation or updates; capture mapping in `documentation-plan.md`.
   * **Communication:** 
     > "[PHASE 5] - Planning README updates aligned with validated principles."
   * **Evidence:** `.artifacts/protocol-05/documentation-plan.md`
   * **Validation:** Plan covers all necessary documentation

2. **`[MUST]` Produce or Update READMEs:**
   * **Action:** Create targeted READMEs capturing architecture, workflows, and conventions; obtain user approval for each.
   * **Communication:** 
     > "Publishing README updates; awaiting approval for each document."
   * **Evidence:** `.artifacts/protocol-05/readme-updates/`
   * **Validation:** Each README approved by user

3. **`[MUST]` Normalize and Audit Rules:**
   * **Action:** Run `python scripts/normalize_project_rules.py --target .cursor/rules/` and `python scripts/rules_audit_quick.py --output .artifacts/protocol-05/rule-audit-report.md`; update context kit with audit link.
   * **Communication:** 
     > "Normalizing project rules and recording audit evidence."
   * **Evidence:** `.artifacts/protocol-05/rule-audit-report.md`
   * **Validation:** Audit severity ≤ Medium

4. **`[GUIDELINE]` Offer Optional Scaffold Generation:**
   * **Action:** If `brief.md` detected, offer `/Generate Project --brief <path>` to create scaffold in sibling directory; document decision.
   * **Evidence:** Decision documented in execution log
   * **Validation:** User decision recorded

### STEP 6: Project Rule Finalization and Template Discovery
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward rule generation and template inventory -->

1. **`[MUST]` Generate Rule Updates from READMEs:**
   * **Action:** Create or update project rules reflecting README guidance; link each rule to its source doc.
   * **Communication:** 
     > "[PHASE 6] - Translating documentation into enforceable project rules."
   * **Evidence:** `.cursor/rules/project-rules/*.mdc`
   * **Validation:** Rules traceable to documentation

2. **`[MUST]` Validate Rules Post-Update:**
   * **Action:** Re-run rule audit and capture results in `rule-audit-final.md`; ensure no critical findings.
   * **Communication:** 
     > "Revalidating project rules after updates."
   * **Evidence:** `.artifacts/protocol-05/rule-audit-final.md`
   * **Validation:** No critical audit findings

3. **`[GUIDELINE]` Inventory Template Packs:**
   * **Action:** List available template packs using TemplateRegistry and store in `.cursor/context-kit/template-inventory.md`.
   * **Evidence:** `.cursor/context-kit/template-inventory.md`
   * **Validation:** Template inventory complete
   
   **Example (DO):**
   ```bash
   python -c "from project_generator.template_registry import TemplateRegistry; print(TemplateRegistry.list_all())" \
     > .cursor/context-kit/template-inventory.md
   ```

---

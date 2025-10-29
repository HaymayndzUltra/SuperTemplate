---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 04: PROJECT BOOTSTRAP AND CONTEXT ENGINEERING (GOVERNANCE COMPLIANT)

**Purpose:** Execute PROJECT BOOTSTRAP AND CONTEXT ENGINEERING workflow with quality validation and evidence generation.

**Version**: v2.0.0  
**Phase**: Phase 0: Foundation & Discovery  
**Purpose**: Bootstrap project with context engineering, environment setup, and tooling configuration

## PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

### Required Artifacts Standards
**[STRICT]** All artifacts must be present and validated before protocol execution:

- **PROJECT-BRIEF.md** from Protocol 03
  - Format: Validated project summary document
  - Validation: Structure and content completeness
  - Location: Project root or designated documentation path
  
- **project-brief-validation-report.json** from Protocol 03
  - Format: JSON validation report showing alignment evidence
  - Requirements: Status field = "PASS", score ≥ 0.95
  - Location: `.artifacts/protocol-03/`
  
- **BRIEF-APPROVAL-RECORD.json** from Protocol 03
  - Format: JSON record of client/internal approvals
  - Requirements: All required signatures present
  - Location: `.artifacts/protocol-03/`

### Required Approvals Standards
**[STRICT]** Following approvals must be documented:

- **Delivery Lead Authorization**
  - Purpose: Permission to bootstrap repository
  - Documentation: Recorded in approval log
  - Validation: Signature verification required
  
- **DevOps Confirmation**
  - Purpose: Confirm bootstrap environment isolation from production
  - Documentation: Environment separation attestation
  - Validation: Infrastructure team sign-off

### System State Requirements Standards
**[STRICT]** System must meet following requirements:

- **Script Access**
  - Requirement: Read/execute access to `scripts/` directory
  - Validation: Permission check on critical scripts
  
- **Write Permissions**
  - Requirement: Write access to `.cursor/` and `.artifacts/` directories
  - Validation: Directory permission verification
  
- **Environment Health**
  - Requirement: `scripts/doctor.py` returning success (exit code 0)
  - Validation: Pre-execution environment check

---

## AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

### Role Definition
You are an **AI Codebase Analyst & Context Architect**. Your mission is to convert the approved Project Brief into a governed project scaffold, validated environment baseline, and initialized context kit without touching production code.

### Critical Directive
**🚫 [CRITICAL] Never modify existing production application code or delete repository assets outside governed directories.**

### Operational Boundaries
- **Permitted:** Modify `.cursor/`, `.artifacts/`, and generated scaffold files
- **Prohibited:** Alter existing application code, production configs, or user data
- **Validation:** All operations logged and reversible

---

## WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Brief Intake and Verification
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for validating and generating bootstrap plan -->

1. **`[MUST]` Validate Project Brief Assets:**
   * **Action:** Run `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-04/brief-validation-report.json` to ensure structure and approvals are intact.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating Project Brief and approval evidence."
   * **Evidence:** `.artifacts/protocol-04/brief-validation-report.json`
   * **Validation:** Exit code 0 and validation score ≥ 0.95
   * **Halt condition:** Stop if validation fails or approvals missing.

2. **`[MUST]` Generate Bootstrap Plan (Dry Run):**
   * **Action:** Execute `python scripts/generate_from_brief.py --brief PROJECT-BRIEF.md --dry-run --yes` to preview scaffold operations.
   * **Communication:** 
     > "Previewing scaffold generation plan and mapping assets."
   * **Evidence:** `.artifacts/protocol-04/bootstrap-dry-run.log`
   * **Validation:** Review log for expected operations

3. **`[GUIDELINE]` Extract Technical Signals:**
   * **Action:** Produce `technical-baseline.json` summarizing stacks, services, and integration dependencies gleaned from the brief.
   * **Evidence:** `.artifacts/protocol-04/technical-baseline.json`
   * **Validation:** JSON schema compliance
   
   **Example (DO):**
   ```json
   {
     "frontend": "Next.js",
     "backend": "FastAPI",
     "datastore": "PostgreSQL"
   }
   ```

### STEP 2: Environment and Governance Preparation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward environment validation and governance setup -->

1. **`[MUST]` Run Environment Doctor:**
   * **Action:** Execute `python scripts/doctor.py --strict` to confirm toolchain readiness; store output in `.artifacts/protocol-04/environment-report.json`.
   * **Communication:** 
     > "[PHASE 2] - Validating local environment and dependencies."
   * **Evidence:** `.artifacts/protocol-04/environment-report.json`
   * **Validation:** All checks passing (green status)
   * **Halt condition:** Stop if doctor script reports missing dependencies.

2. **`[MUST]` Normalize Governance Rules:**
   * **Action:** Run `python scripts/normalize_project_rules.py --target .cursor/rules/` followed by `python scripts/rules_audit_quick.py --output .artifacts/protocol-04/rule-audit-report.md`.
   * **Communication:** 
     > "Normalizing governance rules and auditing metadata integrity."
   * **Evidence:** `.artifacts/protocol-04/rule-audit-report.md`
   * **Validation:** No critical issues in audit report

3. **`[GUIDELINE]` Snapshot Existing Context Kit:**
   * **Action:** Archive current `.cursor/context-kit/` into `.artifacts/protocol-04/pre-bootstrap-context.zip` for rollback options.
   * **Evidence:** `.artifacts/protocol-04/pre-bootstrap-context.zip`
   * **Validation:** Archive integrity check
   
   **Example (DO):**
   ```bash
   zip -r .artifacts/protocol-04/pre-bootstrap-context.zip .cursor/context-kit/
   ```

### STEP 3: Scaffold Generation and Verification
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple scaffold generation and validation steps -->

1. **`[MUST]` Generate Governed Scaffold:**
   * **Action:** Run `python scripts/generate_from_brief.py --brief PROJECT-BRIEF.md --output-root . --in-place --no-subdir --no-cursor-assets --force --yes` to materialize scaffold.
   * **Communication:** 
     > "[PHASE 3] - Generating governed scaffold artifacts."
   * **Evidence:** `.artifacts/protocol-04/bootstrap-manifest.json`
   * **Validation:** Manifest completeness and accuracy
   * **Halt condition:** Stop if generator exits with non-zero status.

2. **`[MUST]` Verify Scaffold Integrity:**
   * **Action:** Execute `python scripts/validate_scaffold.py --manifest .artifacts/protocol-04/bootstrap-manifest.json` to ensure generated assets match registry expectations.
   * **Communication:** 
     > "Validating scaffold integrity and template compliance."
   * **Evidence:** `.artifacts/protocol-04/scaffold-validation-report.json`
   * **Validation:** Compliance score ≥ 98%

3. **`[GUIDELINE]` Inspect Generated Structure:**
   * **Action:** Review directories for completeness, confirm `generator-config.json` accuracy, and document observations in `scaffold-review-notes.md`.
   * **Evidence:** `.artifacts/protocol-04/scaffold-review-notes.md`
   * **Validation:** Manual review checklist complete
   
   **Example (DO):**
   ```markdown
   - ✅ templates/bootstrap/app/ created
   - ✅ generator-config.json includes service mappings
   - ⚠️ Review README auto-generated content with product owner
   ```

### STEP 4: Context Kit Initialization
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward context initialization and validation -->

1. **`[MUST]` Initialize Evidence Manager:**
   * **Action:** Run `python scripts/evidence_manager.py init --path .artifacts/protocol-04/` to establish evidence tracking baseline.
   * **Communication:** 
     > "[PHASE 4] - Initializing evidence tracking and context kit."
   * **Evidence:** `.artifacts/protocol-04/evidence-manifest.json`
   * **Validation:** Manifest initialization successful

2. **`[MUST]` Validate Workflow Integration:**
   * **Action:** Execute `python scripts/validate_workflows.py --mode bootstrap --output .artifacts/protocol-04/workflow-validation-report.json`.
   * **Communication:** 
     > "Running workflow validation to ensure protocol readiness."
   * **Evidence:** `.artifacts/protocol-04/workflow-validation-report.json`
   * **Validation:** Status = "pass" in report
   * **Halt condition:** Stop if validation fails and resolve issues.

3. **`[GUIDELINE]` Update Context Kit Documentation:**
   * **Action:** Document stack summary, governance status, and next steps in `.cursor/context-kit/governance-status.md`.
   * **Evidence:** `.cursor/context-kit/governance-status.md`
   * **Validation:** Document completeness check
   
   **Example (DO):**
   ```markdown
   ## Bootstrap Summary
   - Stack: Next.js + FastAPI + PostgreSQL
   - Governance: Rules normalized 2024-05-10
   - Next: Protocol 05 legacy alignment
   ```

---

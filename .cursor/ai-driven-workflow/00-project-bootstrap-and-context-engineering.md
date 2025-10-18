---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 00: PROJECT BOOTSTRAP AND CONTEXT ENGINEERING (GOVERNANCE COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `PROJECT-BRIEF.md` from Protocol 01 (validated project summary)
- [ ] `project-brief-validation-report.json` from Protocol 01 (evidence of alignment)
- [ ] `BRIEF-APPROVAL-RECORD.json` from Protocol 01 (client/internal approvals)

### Required Approvals
- [ ] Delivery lead authorization to bootstrap repository
- [ ] DevOps confirmation that bootstrap environment is isolated from production

### System State Requirements
- [ ] Access to bootstrap scripts under `scripts/`
- [ ] Write permissions to `.cursor/` and `.artifacts/` directories
- [ ] Environment doctor check (`scripts/doctor.py`) returning success

---

## 00. AI ROLE AND MISSION

You are an **AI Codebase Analyst & Context Architect**. Your mission is to convert the approved Project Brief into a governed project scaffold, validated environment baseline, and initialized context kit without touching production code.

**🚫 [CRITICAL] Never modify existing production application code or delete repository assets outside governed directories.**

---

## 00. PROJECT BOOTSTRAP WORKFLOW

### STEP 1: Brief Intake and Verification

1. **`[MUST]` Validate Project Brief Assets:**
   * **Action:** Run `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-00/brief-validation-report.json` to ensure structure and approvals are intact.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating Project Brief and approval evidence."
   * **Halt condition:** Stop if validation fails or approvals missing.
   * **Evidence:** `.artifacts/protocol-00/brief-validation-report.json`

2. **`[MUST]` Generate Bootstrap Plan (Dry Run):**
   * **Action:** Execute `python scripts/generate_from_brief.py --brief PROJECT-BRIEF.md --dry-run --yes` to preview scaffold operations.
   * **Communication:** 
     > "Previewing scaffold generation plan and mapping assets."
   * **Evidence:** `.artifacts/protocol-00/bootstrap-dry-run.log`

3. **`[GUIDELINE]` Extract Technical Signals:**
   * **Action:** Produce `technical-baseline.json` summarizing stacks, services, and integration dependencies gleaned from the brief.
   * **Example:**
     ```json
     {
       "frontend": "Next.js",
       "backend": "FastAPI",
       "datastore": "PostgreSQL"
     }
     ```

### STEP 2: Environment and Governance Preparation

1. **`[MUST]` Run Environment Doctor:**
   * **Action:** Execute `python scripts/doctor.py --strict` to confirm toolchain readiness; store output in `.artifacts/protocol-00/environment-report.json`.
   * **Communication:** 
     > "[PHASE 2] - Validating local environment and dependencies."
   * **Halt condition:** Stop if doctor script reports missing dependencies.
   * **Evidence:** `.artifacts/protocol-00/environment-report.json`

2. **`[MUST]` Normalize Governance Rules:**
   * **Action:** Run `python scripts/normalize_project_rules.py --target .cursor/rules/` followed by `python scripts/rules_audit_quick.py --output .artifacts/protocol-00/rule-audit-report.md`.
   * **Communication:** 
     > "Normalizing governance rules and auditing metadata integrity."
   * **Evidence:** `.artifacts/protocol-00/rule-audit-report.md`

3. **`[GUIDELINE]` Snapshot Existing Context Kit:**
   * **Action:** Archive current `.cursor/context-kit/` into `.artifacts/protocol-00/pre-bootstrap-context.zip` for rollback options.
   * **Example:**
     ```bash
     zip -r .artifacts/protocol-00/pre-bootstrap-context.zip .cursor/context-kit/
     ```

### STEP 3: Scaffold Generation and Verification

1. **`[MUST]` Generate Governed Scaffold:**
   * **Action:** Run `python scripts/generate_from_brief.py --brief PROJECT-BRIEF.md --output-root . --in-place --no-subdir --no-cursor-assets --force --yes` to materialize scaffold.
   * **Communication:** 
     > "[PHASE 3] - Generating governed scaffold artifacts."
   * **Halt condition:** Stop if generator exits with non-zero status.
   * **Evidence:** `.artifacts/protocol-00/bootstrap-manifest.json`

2. **`[MUST]` Verify Scaffold Integrity:**
   * **Action:** Execute `python scripts/validate_scaffold.py --manifest .artifacts/protocol-00/bootstrap-manifest.json` to ensure generated assets match registry expectations.
   * **Communication:** 
     > "Validating scaffold integrity and template compliance."
   * **Evidence:** `.artifacts/protocol-00/scaffold-validation-report.json`

3. **`[GUIDELINE]` Inspect Generated Structure:**
   * **Action:** Review directories for completeness, confirm `generator-config.json` accuracy, and document observations in `scaffold-review-notes.md`.
   * **Example:**
     ```markdown
     - ✅ templates/bootstrap/app/ created
     - ✅ generator-config.json includes service mappings
     - ⚠️ Review README auto-generated content with product owner
     ```

### STEP 4: Context Kit Initialization

1. **`[MUST]` Initialize Evidence Manager:**
   * **Action:** Run `python scripts/evidence_manager.py init --path .artifacts/protocol-00/` to establish evidence tracking baseline.
   * **Communication:** 
     > "[PHASE 4] - Initializing evidence tracking and context kit."
   * **Evidence:** `.artifacts/protocol-00/evidence-manifest.json`

2. **`[MUST]` Validate Workflow Integration:**
   * **Action:** Execute `python scripts/validate_workflows.py --mode bootstrap --output .artifacts/protocol-00/workflow-validation-report.json`.
   * **Communication:** 
     > "Running workflow validation to ensure protocol readiness."
   * **Halt condition:** Stop if validation fails and resolve issues.
   * **Evidence:** `.artifacts/protocol-00/workflow-validation-report.json`

3. **`[GUIDELINE]` Update Context Kit Documentation:**
   * **Action:** Document stack summary, governance status, and next steps in `.cursor/context-kit/governance-status.md`.
   * **Example:**
     ```markdown
     ## Bootstrap Summary
     - Stack: Next.js + FastAPI + PostgreSQL
     - Governance: Rules normalized 2024-05-10
     - Next: Protocol 0 legacy alignment
     ```

---

## 00. INTEGRATION POINTS

### Inputs From:
- **Protocol 01**: `PROJECT-BRIEF.md`, `project-brief-validation-report.json`, `BRIEF-APPROVAL-RECORD.json` - Authoritative planning inputs.

### Outputs To:
- **Protocol 0**: `.cursor/context-kit/governance-status.md`, `.artifacts/protocol-00/bootstrap-manifest.json` - Legacy bootstrap alignment inputs.
- **Protocol 02**: `.cursor/context-kit/`, `.artifacts/protocol-00/technical-baseline.json` - Task generation context.

### Artifact Storage Locations:
- `.artifacts/protocol-00/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 00. QUALITY GATES

### Gate 1: Brief Validation Gate
- **Criteria**: Project Brief validation report status = PASS and approvals present.
- **Evidence**: `.artifacts/protocol-00/brief-validation-report.json`
- **Pass Threshold**: Validation score ≥ 0.95.
- **Failure Handling**: Request updated brief, remediate missing approvals, rerun validation.
- **Automation**: `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-00/brief-validation-report.json`

### Gate 2: Environment & Rule Integrity Gate
- **Criteria**: Environment doctor passes and rule audit reports no critical issues.
- **Evidence**: `.artifacts/protocol-00/environment-report.json`, `.artifacts/protocol-00/rule-audit-report.md`
- **Pass Threshold**: Doctor script exit code 0 and audit severity ≤ Medium.
- **Failure Handling**: Remediate missing dependencies or rule errors, document fixes, rerun gate.
- **Automation**: `python scripts/rules_audit_quick.py --output .artifacts/protocol-00/rule-audit-report.md`

### Gate 3: Scaffold Validation Gate
- **Criteria**: Scaffold manifest matches registry, validation report status = PASS.
- **Evidence**: `.artifacts/protocol-00/bootstrap-manifest.json`, `.artifacts/protocol-00/scaffold-validation-report.json`
- **Pass Threshold**: Validator returns compliance ≥ 98%.
- **Failure Handling**: Regenerate scaffold with corrected parameters, rerun validation.
- **Automation**: `python scripts/validate_scaffold.py --manifest .artifacts/protocol-00/bootstrap-manifest.json`

### Gate 4: Context Validation Gate
- **Criteria**: Evidence manager initialized, workflow validation success, governance status updated.
- **Evidence**: `.artifacts/protocol-00/evidence-manifest.json`, `.artifacts/protocol-00/workflow-validation-report.json`, `.cursor/context-kit/governance-status.md`
- **Pass Threshold**: Workflow validator returns `pass` and documentation updated.
- **Failure Handling**: Address validation errors, refresh context kit documentation, rerun gate.
- **Automation**: `python scripts/validate_workflows.py --mode bootstrap --output .artifacts/protocol-00/workflow-validation-report.json`

---

## 00. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Validating Project Brief inputs before bootstrap."
[MASTER RAY™ | PHASE 2 START] - "Preparing environment and governance rules for scaffold generation."
[MASTER RAY™ | PHASE 3 START] - "Generating governed scaffold based on approved brief."
[MASTER RAY™ | PHASE 4 START] - "Initializing context kit and workflow validation."
[PHASE COMPLETE] - "Bootstrap complete; artifacts stored in .artifacts/protocol-00/."
[RAY ERROR] - "Issue encountered during [phase]; see relevant report for remediation details."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Bootstrap operations complete. Evidence available:
> - brief-validation-report.json
> - environment-report.json
> - bootstrap-manifest.json
> - workflow-validation-report.json
>
> Confirm readiness to activate Protocol 0: Bootstrap Your Project (Legacy Alignment)."
```

### Error Handling:
```
[RAY GATE FAILED: Environment & Rule Integrity]
> "Quality gate 'Environment & Rule Integrity' failed.
> Criteria: doctor.py success and rule audit without critical issues.
> Actual: Missing Docker installation detected.
> Required action: Install Docker, rerun doctor.py, update environment-report.json.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 00. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_00.py

# Quality gate automation
python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-00/brief-validation-report.json
python scripts/rules_audit_quick.py --output .artifacts/protocol-00/rule-audit-report.md
python scripts/validate_scaffold.py --manifest .artifacts/protocol-00/bootstrap-manifest.json
python scripts/validate_workflows.py --mode bootstrap --output .artifacts/protocol-00/workflow-validation-report.json

# Evidence aggregation
python scripts/aggregate_evidence_00.py --output .artifacts/protocol-00/
```

### CI/CD Integration:
```yaml
name: Protocol 00 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 00 Gates
        run: python scripts/run_protocol_00_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Manually review Project Brief sections and approvals; log observations in `manual-brief-review.md`.
2. Conduct environment checklist using shared spreadsheet; store export in `.artifacts/protocol-00/manual-environment-check.xlsx`.
3. Document manual validation results in `.artifacts/protocol-00/manual-validation-log.md`.

---

## 00. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 0:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 0: Bootstrap Your Project (Legacy Alignment)

**Evidence Package:**
- `bootstrap-manifest.json` - Record of generated scaffold assets
- `governance-status.md` - Context kit summary for legacy protocol alignment

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/0-bootstrap-your-project.md
```

---

## 00. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `brief-validation-report.json` | `.artifacts/protocol-00/` | Confirmation of brief integrity | Protocol 0 |
| `environment-report.json` | `.artifacts/protocol-00/` | Toolchain validation evidence | Protocol 0 |
| `bootstrap-manifest.json` | `.artifacts/protocol-00/` | Generated scaffold inventory | Protocols 0 & 02 |
| `scaffold-validation-report.json` | `.artifacts/protocol-00/` | Scaffold compliance verification | Protocol 02 |
| `workflow-validation-report.json` | `.artifacts/protocol-00/` | Context validation evidence | Protocol 0 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

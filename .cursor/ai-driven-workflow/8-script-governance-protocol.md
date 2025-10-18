# PROTOCOL 8: SCRIPT GOVERNANCE (AUTOMATION QUALITY COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `.artifacts/quality-audit/QUALITY-AUDIT-PACKAGE.zip` from Protocol 4 – baseline quality expectations
- [ ] `.cursor/context-kit/quality-audit-summary.json` – latest audit findings to align governance focus
- [ ] Existing `script-registry.json` (if present) in `.cursor/context-kit/` – prior inventory snapshot

### Required Approvals
- [ ] Automation owner approval to perform read-only validation on `/scripts/`
- [ ] Security lead acknowledgement for accessing script metadata

### System State Requirements
- [ ] Repository `/scripts/` directory accessible with read permissions
- [ ] Static analysis tools (`pylint`, `shellcheck`, `yamllint`) installed or containerized equivalents configured
- [ ] Write permissions to `.artifacts/scripts/` and `.cursor/context-kit/`

---

## 8. AI ROLE AND MISSION

You are an **Automation Compliance Auditor**. Your mission is to validate, audit, and enforce consistency across operational scripts without modifying them, ensuring automation integrity for downstream protocols.

**🚫 [CRITICAL] DO NOT modify or execute scripts directly; only validate, analyze, and report compliance results.**

---

## 8. SCRIPT GOVERNANCE EXECUTION WORKFLOW

### STEP 1: Script Discovery and Inventory Baseline

1. **`[MUST]` Index Scripts Across Repository:**
   * **Action:** Enumerate `.py`, `.sh`, `.ps1`, and `.yml` files under `/scripts/`, capturing metadata (path, description, last modified).
   * **Communication:** 
     > "[PHASE 1 START] - Beginning script discovery and indexing..."
   * **Halt condition:** Stop if `/scripts/` directory missing or inaccessible.
   * **Evidence:** `.artifacts/scripts/script-index.json` with completeness score.

2. **`[MUST]` Validate Inventory Completeness:**
   * **Action:** Compare discovered files against existing registry (if available) ensuring ≥95% alignment.
   * **Communication:** 
     > "[PHASE 1] Inventory completeness evaluated. Deviations recorded."
   * **Halt condition:** Pause if completeness <95% without documented rationale.
   * **Evidence:** `.artifacts/scripts/inventory-validation-report.json` summarizing matches and gaps.

3. **`[GUIDELINE]` Categorize Scripts by Function:**
   * **Action:** Group scripts into categories (deployment, validation, reporting) for governance insights.
   * **Example:**
     ```python
     categories = classify_scripts(script_index)
     save(categories, ".artifacts/scripts/script-categories.json")
     ```

### STEP 2: Documentation and Static Compliance Checks

1. **`[MUST]` Assess Documentation Quality:**
   * **Action:** Ensure each script includes purpose statement, usage instructions, and artifact output description.
   * **Communication:** 
     > "[PHASE 2 START] - Auditing script documentation completeness..."
   * **Halt condition:** Halt if any critical script lacks documentation.
   * **Evidence:** `.artifacts/scripts/documentation-audit.csv` capturing compliance per script.

2. **`[MUST]` Run Static Analysis Toolchain:**
   * **Action:** Execute read-only static analysis (`pylint`, `shellcheck`, `yamllint`) capturing warnings and severity levels.
   * **Communication:** 
     > "[AUTOMATION] Executing static analysis suite across script inventory..."
   * **Halt condition:** Pause if tool execution fails or generates blocking severity findings.
   * **Evidence:** `.artifacts/scripts/static-analysis-report.json` aggregated by tool and script.

3. **`[MUST]` Confirm Artifact Output Compliance:**
   * **Action:** Validate each script’s expected outputs align with `.artifacts/` storage conventions and JSON schema rules.
   * **Communication:** 
     > "[PHASE 2] Verifying artifact output compliance and schema adherence..."
   * **Halt condition:** Stop if artifact paths or schemas deviate without mitigation plan.
   * **Evidence:** `.artifacts/scripts/artifact-compliance-report.json` including schema validation results.

4. **`[GUIDELINE]` Extend Protocol 4 Gates:**
   * **Action:** Map relevant Protocol 4 quality gate expectations to scripts to ensure consistency.
   * **Example:**
     ```markdown
     - Gate Alignment: Pre-Audit Automation → Scripts: run_protocol_4_pre_audit.py
     - Evidence: static-analysis-report.json (severity <= medium)
     ```

### STEP 3: Governance Reporting and Feedback Loop

1. **`[MUST]` Generate Compliance Scorecard:**
   * **Action:** Consolidate inventory, documentation, static analysis, and artifact compliance into `script-compliance.json`.
   * **Communication:** 
     > "[PHASE 3 START] - Compiling script governance scorecard for downstream consumers..."
   * **Halt condition:** Pause if data model validation fails.
   * **Evidence:** `.cursor/context-kit/script-compliance.json` with compliance index.

2. **`[MUST]` Publish Remediation Backlog:**
   * **Action:** Create backlog entries for non-compliant scripts and notify owners.
   * **Communication:** 
     > "[PHASE 3] Script remediation backlog prepared. Owners notified."
   * **Halt condition:** Stop if backlog cannot be linked to issue tracker.
   * **Evidence:** `.artifacts/scripts/remediation-backlog.csv` containing action items.

3. **`[GUIDELINE]` Share Insights with Quality Audit:**
   * **Action:** Provide summary to Protocol 4 to influence upcoming audits.
   * **Example:**
     ```markdown
     ### Script Governance Highlights
     - Coverage: 98% scripts documented
     - Blocking Issues: None
     - Recommendations: Automate schema validation nightly
     ```

---

## 8. INTEGRATION POINTS

### Inputs From:
- **Protocol 4**: `quality-audit-summary.json` – establishes baseline quality expectations
- **Protocol 3**: `automation-task-tracker.csv` – links script ownership to tasks

### Outputs To:
- **Protocol 4**: `artifact-compliance-report.json`, `script-compliance.json` – informs future audits
- **Protocol 5**: `remediation-backlog.csv` – retrospective review of automation improvements
- **Protocol 12**: `script-categories.json` – supports monitoring automation classification

### Artifact Storage Locations:
- `.artifacts/scripts/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 8. QUALITY GATES

### Gate 1: Inventory Accuracy Gate
- **Criteria**: All scripts indexed; completeness ≥ 95%; metadata populated.
- **Evidence**: `script-index.json`, `inventory-validation-report.json`.
- **Pass Threshold**: Completeness ≥ 0.95.
- **Failure Handling**: Re-run discovery; resolve permissions; document exceptions.
- **Automation**: `python scripts/validate_gate_8_inventory.py --threshold 0.95`

### Gate 2: Documentation & Static Compliance Gate
- **Criteria**: Documentation coverage ≥ 95%; no blocker severity findings from static analysis.
- **Evidence**: `documentation-audit.csv`, `static-analysis-report.json`.
- **Pass Threshold**: Documentation coverage ≥ 0.95; blocker count = 0.
- **Failure Handling**: Notify script owners; remediate documentation or code issues before proceeding.
- **Automation**: `python scripts/validate_gate_8_static.py --report .artifacts/scripts/static-analysis-report.json`

### Gate 3: Artifact Governance Gate
- **Criteria**: Artifact output paths verified; schema validation success ≥ 98%.
- **Evidence**: `artifact-compliance-report.json`, schema validation logs.
- **Pass Threshold**: Compliance score ≥ 0.98.
- **Failure Handling**: Flag non-compliant scripts; update schemas or script instructions; rerun validation.
- **Automation**: `python scripts/validate_gate_8_artifacts.py --threshold 0.98`

### Gate 4: Governance Reporting Gate
- **Criteria**: Scorecard generated; remediation backlog created; insights shared with Protocol 4.
- **Evidence**: `script-compliance.json`, `remediation-backlog.csv`, governance summary note.
- **Pass Threshold**: Scorecard validation = true; backlog coverage 100% of non-compliant scripts.
- **Failure Handling**: Rebuild scorecard; ensure backlog entries mapped to owners; resend summary.
- **Automation**: `python scripts/validate_gate_8_reporting.py`

---

## 8. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[PHASE 1 START] - Beginning script discovery and indexing...
[PHASE 1 COMPLETE] - Inventory baseline captured. Evidence: script-index.json.
[PHASE 2 START] - Auditing script documentation completeness...
[PHASE 2 COMPLETE] - Documentation and static analysis results available.
[PHASE 3 START] - Compiling script governance scorecard for downstream consumers...
[PHASE 3 COMPLETE] - Governance scorecard delivered. Evidence: script-compliance.json.
[ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[USER CONFIRMATION REQUIRED]
> "Script governance validation is complete.
> - script-compliance.json
> - remediation-backlog.csv
>
> Please review and confirm readiness to inform Protocol 4 and 5."
```

### Error Handling:
```
[GATE FAILED: Documentation & Static Compliance Gate]
> "Quality gate 'Documentation & Static Compliance Gate' failed.
> Criteria: Documentation coverage ≥ 95%, blocker findings = 0
> Actual: {result}
> Required action: Engage script owners to remediate documentation or fix static analysis issues.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 8. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_8.py

# Quality gate automation
python scripts/validate_gate_8_inventory.py --threshold 0.95
python scripts/validate_gate_8_artifacts.py --threshold 0.98

# Evidence aggregation
python scripts/aggregate_evidence_8.py --output .artifacts/scripts/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 8 Validation
on:
  schedule:
    - cron: '0 3 * * 1'
  workflow_dispatch:
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 8 Gates
        run: python scripts/run_protocol_8_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform manual script inventory using `find` command and update spreadsheet.
2. Inspect documentation within scripts and annotate compliance results manually.
3. Document results in `.artifacts/protocol-8/manual-validation-log.md`

---

## 8. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 4 & 5:
**[PROTOCOL COMPLETE]** Ready for Protocol 4: Quality Audit Orchestrator and Protocol 5: Implementation Retrospective

**Evidence Package:**
- `script-compliance.json` - Governance summary for audit alignment
- `remediation-backlog.csv` - Actions for retrospective review

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/4-quality-audit.md
```

---

## 8. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `script-index.json` | `.artifacts/scripts/` | Inventory of automation assets | Protocol 8 Gates |
| `documentation-audit.csv` | `.artifacts/scripts/` | Documentation compliance snapshot | Protocol 8 Gates |
| `static-analysis-report.json` | `.artifacts/scripts/` | Static analysis findings | Protocol 4 |
| `remediation-backlog.csv` | `.artifacts/scripts/` | Follow-up actions | Protocol 5 |
| `script-compliance.json` | `.cursor/context-kit/` | Governance scorecard | Protocol 4 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

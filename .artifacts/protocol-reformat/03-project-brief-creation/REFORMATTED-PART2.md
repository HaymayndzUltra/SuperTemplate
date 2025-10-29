---

## 5. INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### Inputs From:
**[STRICT]** The following inputs must be validated before execution:
- **Protocol 01**: `PROPOSAL.md`, `proposal-summary.json` - Alignment baseline and commitments.
- **Protocol 02**: `client-discovery-form.md`, `scope-clarification.md`, `communication-plan.md`, `timeline-discussion.md`, `discovery-recap.md` - Validated discovery intelligence.

### Outputs To:
**[STRICT]** The following outputs must be generated for downstream protocols:
- **Protocol 04**: `PROJECT-BRIEF.md`, `project-brief-validation-report.json` - Context kit enrichment for bootstrap activities.
- **Protocol 06**: `technical-baseline.json` (extracted from brief) - Inputs for technical design.

### Artifact Storage Locations:
**[STRICT]** All artifacts must be stored in standardized locations:
- `.artifacts/protocol-03/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and criteria -->

### Gate 1: Discovery Evidence Verification
**[STRICT]** This gate validates prerequisite artifact completeness.
- **Criteria**: All prerequisite artifacts validated, discrepancies resolved, validation report status = PASS.
- **Evidence**: `.artifacts/protocol-03/project-brief-validation-report.json`
- **Pass Threshold**: Validation score ≥ 0.95.
- **Failure Handling**: Re-open discovery with client, update artifacts, rerun validation.
- **Automation**: `python scripts/validate_discovery_inputs.py --input .artifacts/protocol-02/ --output .artifacts/protocol-03/project-brief-validation-report.json`

### Gate 2: Structural Integrity
**[STRICT]** This gate validates brief structure and content completeness.
- **Criteria**: Every brief section populated, traceability map references source artifacts, glossary present.
- **Evidence**: `.artifacts/protocol-03/PROJECT-BRIEF.md`, `.artifacts/protocol-03/traceability-map.json`
- **Pass Threshold**: Structural validator returns `pass` with coverage ≥ 100%.
- **Failure Handling**: Fill missing sections, update traceability, rerun validator.
- **Automation**: `python scripts/validate_brief_structure.py --input .artifacts/protocol-03/PROJECT-BRIEF.md --report .artifacts/protocol-03/brief-structure-report.json`

### Gate 3: Approval Compliance
**[STRICT]** This gate validates approval collection and recording.
- **Criteria**: Client and internal approvals recorded with timestamps and references.
- **Evidence**: `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`
- **Pass Threshold**: Approval record includes `client_status = approved` and `internal_status = approved`.
- **Failure Handling**: Escalate to account lead, reconcile feedback, update record, rerun gate.
- **Automation**: `python scripts/verify_brief_approvals.py --input .artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### Status Announcements:
**[STRICT]** Use standardized announcements for phase transitions:
```
[MASTER RAY™ | PHASE 1 START] - "Validating discovery evidence for Project Brief creation."
[MASTER RAY™ | PHASE 2 START] - "Compiling Project Brief sections with traceable sources."
[MASTER RAY™ | PHASE 3 START] - "Running structural validation and collecting approvals."
[PHASE COMPLETE] - "Project Brief approved and archived for downstream use."
[RAY ERROR] - "Issue encountered during [phase]; see validation-issues.md for details."
```

### Validation Prompts:
**[STRICT]** Use standardized prompts for validation requests:
```
[RAY CONFIRMATION REQUIRED]
> "Project Brief assembled and validated. Evidence available:
> - project-brief-validation-report.json
> - PROJECT-BRIEF.md
> - brief-structure-report.json
> - BRIEF-APPROVAL-RECORD.json
>
> Confirm readiness to trigger Protocol 04: Project Bootstrap & Context Engineering."
```

### Error Handling:
**[STRICT]** Use standardized error messages for gate failures:
```
[RAY GATE FAILED: Structural Integrity]
> "Quality gate 'Structural Integrity' failed.
> Criteria: All sections must be populated with traceable references.
> Actual: Technical Architecture Baseline missing source references.
> Required action: Update traceability-map.json, repopulate section, rerun validator.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 8. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### Validation Scripts:

1. **`[MUST]` Run prerequisite validation:**
   * **Action:** Execute script to validate prerequisites
   * **Evidence:** Validation output in execution log
   * **Validation:** Exit code 0
   
   ```bash
   # Prerequisite validation
   python scripts/validate_prerequisites_01.py
   ```

2. **`[MUST]` Run discovery input validation:**
   * **Action:** Execute script to validate discovery artifacts
   * **Evidence:** `.artifacts/protocol-03/project-brief-validation-report.json`
   * **Validation:** Validation score ≥ 0.95
   
   ```bash
   # Quality gate automation
   python scripts/validate_discovery_inputs.py \
     --input .artifacts/protocol-02/ \
     --output .artifacts/protocol-03/project-brief-validation-report.json
   ```

3. **`[MUST]` Run structural validation:**
   * **Action:** Execute script to validate brief structure
   * **Evidence:** `.artifacts/protocol-03/brief-structure-report.json`
   * **Validation:** Coverage ≥ 100%
   
   ```bash
   python scripts/validate_brief_structure.py \
     --input .artifacts/protocol-03/PROJECT-BRIEF.md \
     --report .artifacts/protocol-03/brief-structure-report.json
   ```

4. **`[MUST]` Run approval verification:**
   * **Action:** Execute script to verify approvals
   * **Evidence:** `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`
   * **Validation:** Both client and internal approvals recorded
   
   ```bash
   python scripts/verify_brief_approvals.py \
     --input .artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json
   ```

5. **`[MUST]` Aggregate evidence:**
   * **Action:** Execute script to collect all evidence
   * **Evidence:** Evidence manifest in `.artifacts/protocol-03/`
   * **Validation:** All artifacts included in manifest
   
   ```bash
   # Evidence aggregation
   python scripts/aggregate_evidence_01.py \
     --output .artifacts/protocol-03/
   ```

### CI/CD Integration:
```yaml
name: Protocol 03 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 03 Gates
        run: python scripts/run_protocol_01_gates.py
```

### Manual Fallbacks:

**When automation is unavailable:**

1. **Manual Discovery Validation:**
   - Perform manual peer review of discovery artifacts
   - Note findings in `manual-validation-checklist.md`
   - Document in `.artifacts/protocol-03/manual-validation-log.md`

2. **Manual Brief Review:**
   - Review PROJECT-BRIEF.md with stakeholders over call
   - Capture approval email or meeting minutes
   - Store evidence in `.artifacts/protocol-03/manual-validation-log.md`

3. **Manual Evidence Collection:**
   - Create manual checklist of all required artifacts
   - Verify each artifact exists and contains expected content
   - Document validation in manual evidence log

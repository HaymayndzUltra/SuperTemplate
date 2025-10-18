---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 01: PROJECT BRIEF CREATION (PROJECT-SCOPING COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `client-discovery-form.md` from Protocol 00B (validated functional requirements)
- [ ] `scope-clarification.md` from Protocol 00B (technical constraints)
- [ ] `communication-plan.md` and `timeline-discussion.md` from Protocol 00B (collaboration expectations)
- [ ] `PROPOSAL.md` and `proposal-summary.json` from Protocol 00A (accepted commitments)

### Required Approvals
- [ ] Client confirmation captured in `discovery-recap.md`
- [ ] Internal solutions architect sign-off that discovery evidence is complete

### System State Requirements
- [ ] Access to project brief templates under `.templates/briefs/`
- [ ] Automation scripts `assemble_project_brief.py` and `validate_brief_structure.py` available

---

## 01. AI ROLE AND MISSION

You are a **Freelance Solutions Architect**. Your mission is to convert validated discovery intelligence into a single source of truth—an implementation-ready Project Brief that downstream teams can trust.

**🚫 [CRITICAL] Do not finalize the brief without recorded client approval and reconciliation against discovery scope.**

---

## 01. PROJECT BRIEF WORKFLOW

### STEP 1: Discovery Validation

1. **`[MUST]` Audit Required Artifacts:**
   * **Action:** Confirm discovery artifacts exist, contain approved content, and align with accepted proposal commitments; log results in `project-brief-validation-report.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Auditing discovery artifacts for completeness and alignment."
   * **Halt condition:** Stop if any artifact is missing, empty, or lacks approval evidence.
   * **Evidence:** `.artifacts/protocol-01/project-brief-validation-report.json`

2. **`[MUST]` Resolve Inconsistencies:**
   * **Action:** Cross-check feature lists, constraints, and expectations; record discrepancies in `validation-issues.md` and resolve with stakeholders before proceeding.
   * **Communication:** 
     > "Highlighting discovery inconsistencies for resolution before brief assembly."
   * **Evidence:** `.artifacts/protocol-01/validation-issues.md`

3. **`[GUIDELINE]` Capture Context Summary:**
   * **Action:** Summarize client goals, audience, and success metrics in `context-summary.md` for quick reference.
   * **Example:**
     ```markdown
     **Client Goals**
     - Reduce onboarding time from 7 days to 2 days
     - Support 10k MAU within first quarter
     ```

### STEP 2: Brief Assembly

1. **`[MUST]` Compile Core Sections:**
   * **Action:** Generate `PROJECT-BRIEF.md` with sections: Executive Summary, Business Objectives, Functional Scope, Technical Architecture Baseline, Delivery Plan, Communication Plan, Risks & Assumptions.
   * **Communication:** 
     > "[PHASE 2] - Assembling Project Brief from validated discovery inputs."
   * **Halt condition:** Pause if any section cannot be populated from validated sources.
   * **Evidence:** `.artifacts/protocol-01/PROJECT-BRIEF.md`

2. **`[MUST]` Embed Traceability Links:**
   * **Action:** Reference source artifacts using inline footnotes and appendices linking back to discovery evidence.
   * **Communication:** 
     > "Embedding traceability to maintain auditability between discovery and brief."
   * **Evidence:** `.artifacts/protocol-01/traceability-map.json`

3. **`[GUIDELINE]` Draft Risk Register:**
   * **Action:** Populate risk appendix with impact, likelihood, and mitigation strategies derived from discovery notes.
   * **Example:**
     ```markdown
     | Risk | Impact | Likelihood | Mitigation |
     |------|--------|------------|------------|
     | Third-party API delay | High | Medium | Add buffer sprint and mock services |
     ```

### STEP 3: Validation and Approval

1. **`[MUST]` Run Structural Validation:**
   * **Action:** Execute `validate_brief_structure.py` to confirm section coverage, glossary presence, and formatting standards.
   * **Communication:** 
     > "[PHASE 3] - Running automated validation on Project Brief structure and content."
   * **Halt condition:** Stop if validation fails; remediate and rerun.
   * **Evidence:** `.artifacts/protocol-01/brief-structure-report.json`

2. **`[MUST]` Capture Approval Evidence:**
   * **Action:** Send approval summary to client and internal lead; log confirmations in `BRIEF-APPROVAL-RECORD.json`.
   * **Communication:** 
     > "Awaiting explicit client approval for Project Brief finalization."
   * **Halt condition:** Do not proceed until approvals recorded.
   * **Evidence:** `.artifacts/protocol-01/BRIEF-APPROVAL-RECORD.json`

3. **`[GUIDELINE]` Prepare Downstream Briefing Deck:**
   * **Action:** Optional slide deck summarizing key sections for kickoff; save as `project-brief-slides.pptx` if requested.
   * **Example:**
     ```markdown
     Slide 1: Objectives & Success Metrics
     Slide 2: MVP Scope Overview
     Slide 3: Timeline & Governance
     ```

---

## 01. INTEGRATION POINTS

### Inputs From:
- **Protocol 00A**: `PROPOSAL.md`, `proposal-summary.json` - Alignment baseline and commitments.
- **Protocol 00B**: `client-discovery-form.md`, `scope-clarification.md`, `communication-plan.md`, `timeline-discussion.md`, `discovery-recap.md` - Validated discovery intelligence.

### Outputs To:
- **Protocol 00**: `PROJECT-BRIEF.md`, `project-brief-validation-report.json` - Context kit enrichment for bootstrap activities.
- **Protocol 06**: `technical-baseline.json` (extracted from brief) - Inputs for technical design.

### Artifact Storage Locations:
- `.artifacts/protocol-01/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 01. QUALITY GATES

### Gate 1: Discovery Evidence Verification
- **Criteria**: All prerequisite artifacts validated, discrepancies resolved, validation report status = PASS.
- **Evidence**: `.artifacts/protocol-01/project-brief-validation-report.json`
- **Pass Threshold**: Validation score ≥ 0.95.
- **Failure Handling**: Re-open discovery with client, update artifacts, rerun validation.
- **Automation**: `python scripts/validate_discovery_inputs.py --input .artifacts/protocol-00B/ --output .artifacts/protocol-01/project-brief-validation-report.json`

### Gate 2: Structural Integrity
- **Criteria**: Every brief section populated, traceability map references source artifacts, glossary present.
- **Evidence**: `.artifacts/protocol-01/PROJECT-BRIEF.md`, `.artifacts/protocol-01/traceability-map.json`
- **Pass Threshold**: Structural validator returns `pass` with coverage ≥ 100%.
- **Failure Handling**: Fill missing sections, update traceability, rerun validator.
- **Automation**: `python scripts/validate_brief_structure.py --input .artifacts/protocol-01/PROJECT-BRIEF.md --report .artifacts/protocol-01/brief-structure-report.json`

### Gate 3: Approval Compliance
- **Criteria**: Client and internal approvals recorded with timestamps and references.
- **Evidence**: `.artifacts/protocol-01/BRIEF-APPROVAL-RECORD.json`
- **Pass Threshold**: Approval record includes `client_status = approved` and `internal_status = approved`.
- **Failure Handling**: Escalate to account lead, reconcile feedback, update record, rerun gate.
- **Automation**: `python scripts/verify_brief_approvals.py --input .artifacts/protocol-01/BRIEF-APPROVAL-RECORD.json`

---

## 01. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Validating discovery evidence for Project Brief creation."
[MASTER RAY™ | PHASE 2 START] - "Compiling Project Brief sections with traceable sources."
[MASTER RAY™ | PHASE 3 START] - "Running structural validation and collecting approvals."
[PHASE COMPLETE] - "Project Brief approved and archived for downstream use."
[RAY ERROR] - "Issue encountered during [phase]; see validation-issues.md for details."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Project Brief assembled and validated. Evidence available:
> - project-brief-validation-report.json
> - PROJECT-BRIEF.md
> - brief-structure-report.json
> - BRIEF-APPROVAL-RECORD.json
>
> Confirm readiness to trigger Protocol 00: Project Bootstrap & Context Engineering."
```

### Error Handling:
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

## 01. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_01.py

# Quality gate automation
python scripts/validate_discovery_inputs.py --input .artifacts/protocol-00B/ --output .artifacts/protocol-01/project-brief-validation-report.json
python scripts/validate_brief_structure.py --input .artifacts/protocol-01/PROJECT-BRIEF.md --report .artifacts/protocol-01/brief-structure-report.json
python scripts/verify_brief_approvals.py --input .artifacts/protocol-01/BRIEF-APPROVAL-RECORD.json

# Evidence aggregation
python scripts/aggregate_evidence_01.py --output .artifacts/protocol-01/
```

### CI/CD Integration:
```yaml
name: Protocol 01 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 01 Gates
        run: python scripts/run_protocol_01_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform manual peer review of discovery artifacts; note findings in `manual-validation-checklist.md`.
2. Review PROJECT-BRIEF.md with stakeholders over call; capture approval email or meeting minutes.
3. Store manual evidence in `.artifacts/protocol-01/manual-validation-log.md`.

---

## 01. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 00:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 00: Project Bootstrap & Context Engineering

**Evidence Package:**
- `PROJECT-BRIEF.md` - Canonical source of truth for planning
- `technical-baseline.json` - Extracted architecture signals for bootstrap and technical design

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md
```

---

## 01. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `project-brief-validation-report.json` | `.artifacts/protocol-01/` | Proof of discovery alignment | Protocol 00 |
| `PROJECT-BRIEF.md` | `.artifacts/protocol-01/` | Authoritative brief | Protocols 00 & 06 |
| `traceability-map.json` | `.artifacts/protocol-01/` | Source linkage for brief content | Protocol 06 |
| `BRIEF-APPROVAL-RECORD.json` | `.artifacts/protocol-01/` | Approval evidence | Protocol 00 |
| `technical-baseline.json` | `.artifacts/protocol-01/` | Technical summary for design | Protocol 06 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

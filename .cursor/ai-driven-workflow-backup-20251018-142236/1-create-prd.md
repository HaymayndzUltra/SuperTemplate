---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 1: IMPLEMENTATION-READY PRD CREATION (PLANNING COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `PROJECT-BRIEF.md` from Protocol 01 (approved project brief)
- [ ] `discovery-brief.md` and `evidence-map.json` from Protocol 00-CD (traceable discovery signals)
- [ ] `architecture-principles.md` from Protocol 0 (governance context)

### Required Approvals
- [ ] Product owner authorization to begin PRD drafting
- [ ] Technical lead confirmation of architectural constraints

### System State Requirements
- [ ] Access to PRD templates in `.templates/prd/`
- [ ] Availability of automation scripts `generate_prd_assets.py` and `validate_prd_gate.py`

---

## 1. AI ROLE AND MISSION

You are a **Product Manager**. Your mission is to convert validated discovery inputs into an implementation-ready Product Requirements Document (PRD) that fully specifies scope, user experience, data, and integration requirements for engineering execution.

**🚫 [CRITICAL] Do not write production code or modify repositories; deliver documentation only.**

---

## 1. PRD CREATION WORKFLOW

### STEP 1: Context Alignment

1. **`[MUST]` Confirm Feature Intent:**
   * **Action:** Determine whether the effort is a net-new feature or modification; capture rationale in `prd-context.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating feature intent and architectural placement."
   * **Halt condition:** Await stakeholder clarification if intent unclear.
   * **Evidence:** `.artifacts/protocol-1/prd-context.json`

2. **`[MUST]` Map to Architectural Layer:**
   * **Action:** Use discovery inputs and architecture principles to identify primary implementation layer (e.g., frontend, backend, data pipeline) and announce detected layer.
   * **Communication:** 
     > "Detected primary implementation layer: [layer]. Constraints: [communication, technology, governance]."
   * **Evidence:** `.artifacts/protocol-1/layer-detection.md`

3. **`[GUIDELINE]` Capture Stakeholder Goals:**
   * **Action:** Summarize business goals, KPIs, and success metrics in `stakeholder-goals.md` for quick reference.

### STEP 2: Requirements Elaboration

1. **`[MUST]` Gather User Narratives:**
   * **Action:** Elicit user stories and personas aligned with detected layer; store in `user-stories.md`.
   * **Communication:** 
     > "[PHASE 2] - Capturing user stories and personas for PRD foundation."
   * **Evidence:** `.artifacts/protocol-1/user-stories.md`

2. **`[MUST]` Define Functional Requirements:**
   * **Action:** Detail feature behavior, workflows, acceptance criteria, and non-functional requirements in `functional-requirements.md`.
   * **Evidence:** `.artifacts/protocol-1/functional-requirements.md`

3. **`[MUST]` Specify Technical Requirements:**
   * **Action:** Document API contracts, data models, integration points, security considerations, and system interactions in `technical-specs.md`.
   * **Communication:** 
     > "Documenting technical interfaces and constraints to guide engineering."
   * **Evidence:** `.artifacts/protocol-1/technical-specs.md`

4. **`[GUIDELINE]` Populate Decision Matrix:**
   * **Action:** Maintain architectural decision matrix linking need types to implementation targets.
   * **Example:**
     ```markdown
     | Need | Target | Constraints | Notes |
     |------|--------|-------------|-------|
     | Analytics KPI export | Backend service | Must align with GDPR retention | Use existing data warehouse pipeline |
     ```

### STEP 3: Risk, Dependency, and Validation Planning

1. **`[MUST]` Consolidate Risks and Assumptions:**
   * **Action:** Aggregate risks, assumptions, and mitigations from discovery into `risk-assumption-log.md`; include new items identified during elaboration.
   * **Communication:** 
     > "[PHASE 3] - Updating risk and assumption log for PRD readiness."
   * **Evidence:** `.artifacts/protocol-1/risk-assumption-log.md`

2. **`[MUST]` Define Acceptance & Validation Criteria:**
   * **Action:** Establish measurable acceptance tests, KPIs, and validation steps in `validation-plan.md`.
   * **Evidence:** `.artifacts/protocol-1/validation-plan.md`

3. **`[GUIDELINE]` Align Timeline & Release Strategy:**
   * **Action:** Outline milestones, release phases, and rollout strategy referencing `timeline-discussion.md`.

### STEP 4: PRD Assembly and Automation

1. **`[MUST]` Assemble PRD Document:**
   * **Action:** Compile context, requirements, risks, and validation sections into `prd-{feature}.md` following standard template.
   * **Communication:** 
     > "[PHASE 4] - Assembling implementation-ready PRD."
   * **Halt condition:** Pause if any mandatory section lacks confirmed content.
   * **Evidence:** `.artifacts/protocol-1/prd-{feature}.md`

2. **`[MUST]` Generate PRD Assets:**
   * **Action:** Run `python scripts/generate_prd_assets.py --prd .artifacts/protocol-1/prd-{feature}.md --output .artifacts/protocol-1/prd-assets/` to create supporting artifacts (user stories, schemas, APIs).
   * **Communication:** 
     > "[RAY AUTOMATION] PRD assets generated and archived."
   * **Evidence:** `.artifacts/protocol-1/prd-assets/`

3. **`[MUST]` Validate PRD Quality:**
   * **Action:** Execute `python scripts/validate_prd_gate.py --prd .artifacts/protocol-1/prd-{feature}.md --output .artifacts/protocol-1/prd-validation.json` ensuring completeness and alignment.
   * **Communication:** 
     > "PRD validation status: {status} - Score: {score}/100."
   * **Evidence:** `.artifacts/protocol-1/prd-validation.json`

4. **`[GUIDELINE]` Record Traceability:**
   * **Action:** Map PRD sections to source discovery artifacts in `prd-traceability.json`.

---

## 1. INTEGRATION POINTS

### Inputs From:
- **Protocol 01**: `PROJECT-BRIEF.md` - Strategic direction and approved scope.
- **Protocol 00-CD**: `discovery-brief.md`, `evidence-map.json`, `risk-register.md` - Discovery intelligence and risks.
- **Protocol 0**: `architecture-principles.md` - Governance constraints.

### Outputs To:
- **Protocol 06**: `technical-specs.md`, `prd-traceability.json`, `prd-assets/technical-baseline.json` - Inputs for technical design.
- **Protocol 02**: `prd-{feature}.md`, `user-stories.md`, `validation-plan.md` - Task generation references.

### Artifact Storage Locations:
- `.artifacts/protocol-1/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts (summary pointers)

---

## 1. QUALITY GATES

### Gate 1: Context Alignment Gate
- **Criteria**: Feature intent confirmed, layer detection approved, stakeholder goals documented.
- **Evidence**: `prd-context.json`, `layer-detection.md`, `stakeholder-goals.md`
- **Pass Threshold**: Stakeholder confirmation recorded; detected layer accuracy acknowledged.
- **Failure Handling**: Re-engage stakeholders, update documents, rerun gate.
- **Automation**: `python scripts/validate_prd_context.py --input .artifacts/protocol-1/prd-context.json`

### Gate 2: Requirements Completeness Gate
- **Criteria**: User stories, functional requirements, technical specs completed with acceptance criteria.
- **Evidence**: `user-stories.md`, `functional-requirements.md`, `technical-specs.md`
- **Pass Threshold**: Requirements coverage ≥ 95% and traceability established.
- **Failure Handling**: Address gaps, update documents, rerun validation.
- **Automation**: `python scripts/validate_prd_requirements.py --dir .artifacts/protocol-1/`

### Gate 3: Validation Readiness Gate
- **Criteria**: Risk log updated, validation plan defined, PRD assets generated and validated.
- **Evidence**: `risk-assumption-log.md`, `validation-plan.md`, `prd-validation.json`
- **Pass Threshold**: PRD validation score ≥ 85/100.
- **Failure Handling**: Remediate findings, rerun automation, capture waivers if necessary.
- **Automation**: `python scripts/validate_prd_gate.py --prd .artifacts/protocol-1/prd-{feature}.md --output .artifacts/protocol-1/prd-validation.json`

---

## 1. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Aligning feature intent and architectural placement for PRD."
[MASTER RAY™ | PHASE 2 START] - "Detailing functional and technical requirements."
[MASTER RAY™ | PHASE 3 START] - "Consolidating risks, assumptions, and validation plan."
[MASTER RAY™ | PHASE 4 START] - "Assembling PRD and running automation gates."
[PHASE COMPLETE] - "PRD approved; assets archived in .artifacts/protocol-1/."
[RAY ERROR] - "Issue during [phase]; refer to validation logs for remediation."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "PRD draft ready with validation evidence:
> - prd-context.json
> - functional-requirements.md
> - technical-specs.md
> - prd-validation.json
>
> Confirm readiness to proceed to Protocol 06: Technical Design & Architecture."
```

### Error Handling:
```
[RAY GATE FAILED: Requirements Completeness Gate]
> "Quality gate 'Requirements Completeness' failed.
> Criteria: Functional and technical requirements must reach 95% coverage.
> Actual: Acceptance criteria missing for checkout workflow.
> Required action: Update functional-requirements.md, rerun validator.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 1. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_1.py

# Quality gate automation
python scripts/validate_prd_context.py --input .artifacts/protocol-1/prd-context.json
python scripts/validate_prd_requirements.py --dir .artifacts/protocol-1/
python scripts/validate_prd_gate.py --prd .artifacts/protocol-1/prd-{feature}.md --output .artifacts/protocol-1/prd-validation.json

# Evidence aggregation
python scripts/aggregate_evidence_1.py --output .artifacts/protocol-1/
```

### CI/CD Integration:
```yaml
name: Protocol 1 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 1 Gates
        run: python scripts/run_protocol_1_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct PRD review workshop; capture minutes in `manual-prd-review.md`.
2. Obtain stakeholder sign-off via email; archive under `.artifacts/protocol-1/approvals/`.
3. Document manual validations in `.artifacts/protocol-1/manual-validation-log.md`.

---

## 1. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 06:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 06: Technical Design & Architecture

**Evidence Package:**
- `prd-{feature}.md` - Comprehensive PRD for design translation
- `technical-specs.md` - Detailed interfaces for architecture planning

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/6-technical-design-architecture.md
```

---

## 1. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `prd-context.json` | `.artifacts/protocol-1/` | Intent and layer alignment | Protocol 06 |
| `user-stories.md` | `.artifacts/protocol-1/` | Persona narratives | Protocol 02 |
| `functional-requirements.md` | `.artifacts/protocol-1/` | Behavioral specification | Protocols 02 & 06 |
| `technical-specs.md` | `.artifacts/protocol-1/` | API/data details | Protocol 06 |
| `prd-{feature}.md` | `.artifacts/protocol-1/` | Implementation-ready PRD | Protocol 02 |
| `prd-validation.json` | `.artifacts/protocol-1/` | Quality validation evidence | Protocol 06 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

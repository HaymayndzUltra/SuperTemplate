---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 00-CD: CLIENT DISCOVERY (DISCOVERY COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `JOB-POST.md` or equivalent intake document captured from client
- [ ] `architecture-principles.md` from Protocol 05 (governance-aligned conventions)
- [ ] `PROJECT-BRIEF.md` if available, to cross-reference tone and commitments

### Required Approvals
- [ ] Authorization from engagement lead to initiate alternate discovery track
- [ ] Confirmation that implementation teams are on standby for validated brief handoff

### System State Requirements
- [ ] Ability to store artifacts under `.artifacts/protocol-00-CD/`
- [ ] Access to semantic search tools within repository (per Tool Usage Protocol)
- [ ] Communication channel established with client for clarifications

---

## 00-CD. AI ROLE AND MISSION

You are a **Client Discovery Specialist**. Your mission is to transform inbound requests into a validated discovery package with clear scope, risks, and assumptions that downstream teams can immediately act upon.

**🚫 [CRITICAL] Do not progress into implementation or task execution; discovery outputs must remain informational.**

---

## 00-CD. DISCOVERY WORKFLOW

### STEP 1: Intake Normalization

1. **`[MUST]` Capture Raw Input:**
   * **Action:** Consolidate the client message (job post, RFP, email) into `raw-intake.md`, including timestamps and source context.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Capturing and normalizing client intake content."
   * **Halt condition:** Stop if intake content incomplete; request full context.
   * **Evidence:** `.artifacts/protocol-00-CD/raw-intake.md`

2. **`[MUST]` Extract Domain Hints:**
   * **Action:** Parse for domain, budget, deadline, or critical requirement tags; record in `intake-metadata.json`.
   * **Communication:** 
     > "Extracted domain hints and metadata for discovery alignment."
   * **Evidence:** `.artifacts/protocol-00-CD/intake-metadata.json`

3. **`[GUIDELINE]` Reference Architectural Source:**
   * **Action:** Review `README.md` or `architecture-principles.md` to tailor questions and avoid conflicts with established norms.
   * **Example:**
     ```markdown
     - Existing convention: RESTful API with JWT auth
     - Ensure questions confirm compatibility with proposed work
     ```

### STEP 2: Signal Extraction

1. **`[MUST]` Identify Core Signals:**
   * **Action:** Parse intake for objectives, target users, deliverables, constraints, and success metrics; quote original text.
   * **Communication:** 
     > "[PHASE 2] - Extracting objectives, deliverables, and constraints with traceable evidence."
   * **Evidence:** `.artifacts/protocol-00-CD/evidence-map.json`

2. **`[MUST]` Classify Domain & Apply Adapters:**
   * **Action:** Determine domain (web, mobile, data/BI, ML/AI, infra, other) and apply relevant extraction heuristics.
   * **Communication:** 
     > "Domain classified as [domain]; applying adapter to refine signal extraction."
   * **Evidence:** `.artifacts/protocol-00-CD/domain-classification.json`

3. **`[GUIDELINE]` Highlight Missing Information:**
   * **Action:** Tag gaps or ambiguities in `information-gaps.md` for follow-up.

### STEP 3: Clarifications and Assumptions

1. **`[MUST]` Draft Targeted Questions:**
   * **Action:** Produce ≤10 clarifying questions prioritized by impact; include context and risk if unanswered.
   * **Communication:** 
     > "[PHASE 3] - Presenting clarification questions and initial assumptions."
   * **Halt condition:** Await client response or stakeholder guidance before assuming answers.
   * **Evidence:** `.artifacts/protocol-00-CD/clarification-questions.md`

2. **`[MUST]` Document Assumptions v1:**
   * **Action:** For unresolved gaps, state assumption, rationale, and potential impact; record in `assumptions-v1.md`.
   * **Evidence:** `.artifacts/protocol-00-CD/assumptions-v1.md`

3. **`[GUIDELINE]` Package Client Outreach:**
   * **Action:** Prepare communication summary with questions and assumptions for client validation.
   * **Example:**
     ```markdown
     **Blocking Questions**
     1. Do you require HIPAA compliance for patient data?
     2. What analytics KPIs must be reported monthly?

     **Assumptions v1**
     - MVP includes admin dashboard with role-based access.
     ```

### STEP 4: Risks, Dependencies, and Prioritization

1. **`[MUST]` Build Risk Register:**
   * **Action:** Catalog risks (scope, technical, compliance, resource) with impact/likelihood and mitigation plan; store in `risk-register.md`.
   * **Communication:** 
     > "[PHASE 4] - Documenting risks and mitigation strategies."
   * **Evidence:** `.artifacts/protocol-00-CD/risk-register.md`

2. **`[MUST]` Map Dependencies:**
   * **Action:** Identify required accesses, data sources, integrations, and approvals; assign owners and due dates in `dependency-map.json`.
   * **Evidence:** `.artifacts/protocol-00-CD/dependency-map.json`

3. **`[GUIDELINE]` Prioritize Deliverables:**
   * **Action:** Create MoSCoW or priority list aligning deliverables with constraints for briefing.
   * **Example:**
     ```markdown
     - Must: Appointment scheduling module
     - Should: Analytics dashboard
     - Could: SMS reminders (phase 2)
     ```

### STEP 5: Discovery Synthesis and Handoff Prep

1. **`[MUST]` Produce Discovery Brief:**
   * **Action:** Assemble `discovery-brief.md` summarizing objectives, scope, assumptions, risks, dependencies, and next steps.
   * **Communication:** 
     > "[PHASE 5] - Generating discovery brief for downstream protocols."
   * **Halt condition:** Await internal review if critical risks unresolved.
   * **Evidence:** `.artifacts/protocol-00-CD/discovery-brief.md`

2. **`[MUST]` Validate Against Intake:**
   * **Action:** Ensure every brief statement traces back to evidence map or confirmed assumption; document traceability in `traceability-index.json`.
   * **Evidence:** `.artifacts/protocol-00-CD/traceability-index.json`

3. **`[GUIDELINE]` Prepare Executive Summary:**
   * **Action:** Create `executive-summary.md` with concise overview for leadership sign-off.

---

## 00-CD. INTEGRATION POINTS

### Inputs From:
- **Protocol 05**: `architecture-principles.md`, `template-inventory.md` - Governance-aligned conventions for framing discovery questions.
- **Protocol 01**: `jobpost-analysis.json`, `PROPOSAL.md` - Prior proposal insights and tone alignment.

### Outputs To:
- **Protocol 03**: `discovery-brief.md`, `evidence-map.json`, `assumptions-v1.md` - Inputs for project brief creation.
- **Protocol 06**: `traceability-index.json`, `risk-register.md` - Baseline evidence for PRD development.

### Artifact Storage Locations:
- `.artifacts/protocol-00-CD/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts (linked summaries)

---

## 00-CD. QUALITY GATES

### Gate 1: Intake Completeness Gate
- **Criteria**: Raw intake captured fully with metadata, evidence map initiated.
- **Evidence**: `raw-intake.md`, `intake-metadata.json`
- **Pass Threshold**: No missing sections; metadata coverage ≥ 90%.
- **Failure Handling**: Request missing input, re-run normalization, log delay.
- **Automation**: `python scripts/validate_intake.py --input .artifacts/protocol-00-CD/raw-intake.md`

### Gate 2: Signal Traceability Gate
- **Criteria**: Evidence map includes objectives, users, deliverables, constraints, success metrics with source quotes.
- **Evidence**: `evidence-map.json`
- **Pass Threshold**: Traceability score ≥ 0.95.
- **Failure Handling**: Re-extract signals, enrich quotes, rerun validation.
- **Automation**: `python scripts/validate_evidence_map.py --input .artifacts/protocol-00-CD/evidence-map.json`

### Gate 3: Clarification Package Gate
- **Criteria**: ≤10 prioritized questions, assumptions documented with rationale.
- **Evidence**: `clarification-questions.md`, `assumptions-v1.md`
- **Pass Threshold**: Blocking questions addressed; assumptions flagged for validation.
- **Failure Handling**: Refine questions for clarity, reassess assumptions, rerun gate.
- **Automation**: `python scripts/validate_clarifications.py --questions .artifacts/protocol-00-CD/clarification-questions.md`

### Gate 4: Discovery Brief Gate
- **Criteria**: Discovery brief aligns with evidence, risk register populated, dependencies assigned owners.
- **Evidence**: `discovery-brief.md`, `risk-register.md`, `dependency-map.json`, `traceability-index.json`
- **Pass Threshold**: Traceability score ≥ 0.95 and no critical risks without mitigation.
- **Failure Handling**: Update brief, escalate unresolved risks, rerun validation.
- **Automation**: `python scripts/validate_discovery_brief.py --input .artifacts/protocol-00-CD/discovery-brief.md`

---

## 00-CD. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Normalizing client intake and capturing metadata."
[MASTER RAY™ | PHASE 2 START] - "Extracting traceable signals and classifying domain."
[MASTER RAY™ | PHASE 3 START] - "Preparing clarification questions and initial assumptions."
[MASTER RAY™ | PHASE 4 START] - "Documenting risks and dependency map."
[MASTER RAY™ | PHASE 5 START] - "Synthesizing discovery brief for downstream teams."
[PHASE COMPLETE] - "Discovery package ready; evidence archived in .artifacts/protocol-00-CD/."
[RAY ERROR] - "Issue encountered during [phase]; see associated artifact for remediation."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Discovery artifacts prepared. Evidence available:
> - raw-intake.md
> - evidence-map.json
> - clarification-questions.md
> - discovery-brief.md
>
> Confirm readiness to proceed to Protocol 03: Project Brief Creation."
```

### Error Handling:
```
[RAY GATE FAILED: Signal Traceability Gate]
> "Quality gate 'Signal Traceability' failed.
> Criteria: All major signals must reference original text.
> Actual: Missing source quotes for success metrics.
> Required action: Update evidence-map.json with citations and rerun validation.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 00-CD. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_00CD.py

# Quality gate automation
python scripts/validate_intake.py --input .artifacts/protocol-00-CD/raw-intake.md
python scripts/validate_evidence_map.py --input .artifacts/protocol-00-CD/evidence-map.json
python scripts/validate_clarifications.py --questions .artifacts/protocol-00-CD/clarification-questions.md
python scripts/validate_discovery_brief.py --input .artifacts/protocol-00-CD/discovery-brief.md

# Evidence aggregation
python scripts/aggregate_evidence_00CD.py --output .artifacts/protocol-00-CD/
```

### CI/CD Integration:
```yaml
name: Protocol 04-CD Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 04-CD Gates
        run: python scripts/run_protocol_00CD_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review raw intake with stakeholder; record confirmation in `manual-intake-review.md`.
2. Conduct collaborative risk workshop; capture outputs in `.artifacts/protocol-00-CD/manual-risk-session.md`.
3. Store manual validation logs in `.artifacts/protocol-00-CD/manual-validation-log.md`.

---

## 00-CD. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 03:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 03: Project Brief Creation

**Evidence Package:**
- `discovery-brief.md` - Consolidated discovery output for brief drafting
- `evidence-map.json` - Traceability index for downstream validation

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/03-project-brief-creation.md
```

---

## 00-CD. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `raw-intake.md` | `.artifacts/protocol-00-CD/` | Source content normalization | Protocol 03 |
| `evidence-map.json` | `.artifacts/protocol-00-CD/` | Traceable signals mapping | Protocol 03 |
| `clarification-questions.md` | `.artifacts/protocol-00-CD/` | Client outreach package | Protocol 03 |
| `assumptions-v1.md` | `.artifacts/protocol-00-CD/` | Pending assumption log | Protocol 03 |
| `risk-register.md` | `.artifacts/protocol-00-CD/` | Risk catalogue | Protocols 01 & 1 |
| `discovery-brief.md` | `.artifacts/protocol-00-CD/` | Primary discovery deliverable | Protocol 03 |


### Traceability Matrix

**Upstream Dependencies:**
- Input artifacts inherit from: [list predecessor protocols]
- Configuration dependencies: [list config files or environment requirements]
- External dependencies: [list third-party systems or APIs]

**Downstream Consumers:**
- Output artifacts consumed by: [list successor protocols]
- Shared artifacts: [list artifacts used by multiple protocols]
- Archive requirements: [list retention policies]

**Verification Chain:**
- Each artifact includes: SHA-256 checksum, timestamp, verified_by field
- Verification procedure: [describe validation process]
- Audit trail: All artifact modifications logged in protocol execution log

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

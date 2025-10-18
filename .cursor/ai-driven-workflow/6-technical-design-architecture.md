---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 6: TECHNICAL DESIGN & ARCHITECTURE (ARCHITECTURE COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `PROJECT-BRIEF.md` and `project-brief-validation-report.json` from Protocol 01
- [ ] `prd-{feature}.md`, `technical-specs.md`, and `prd-validation.json` from Protocol 1
- [ ] `risk-register.md` and `assumptions-v1.md` from Protocol 00-CD

### Required Approvals
- [ ] Product and engineering leadership approval to begin architecture design
- [ ] Security/compliance stakeholder availability for design review

### System State Requirements
- [ ] Access to architecture templates (`.templates/architecture/`)
- [ ] Diagram tooling (draw.io, Mermaid) or ASCII diagram capability
- [ ] Automation scripts `plan_from_brief.py`, `validate_workflow_integration.py` available

---

## 6. AI ROLE AND MISSION

You are a **Solutions Architect**. Your mission is to transform the approved PRD and discovery evidence into a validated technical architecture package with explicit decisions, diagrams, and task-generation inputs.

**🚫 [CRITICAL] Do not introduce components or integrations that lack grounding in the brief or PRD; every element must trace to validated requirements.**

---

## 6. TECHNICAL DESIGN WORKFLOW

### STEP 1: Source Validation & Context Alignment

1. **`[MUST]` Verify Inputs and Versions:**
   * **Action:** Confirm that Project Brief, PRD, and discovery artifacts exist, match approved versions, and reflect latest sign-offs; record results in `source-alignment-report.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating brief and PRD alignment for architecture planning."
   * **Halt condition:** Stop if any artifact missing or outdated.
   * **Evidence:** `.artifacts/protocol-6/source-alignment-report.json`

2. **`[MUST]` Consolidate Design Inputs:**
   * **Action:** Extract functional scope, non-functional requirements, constraints, and risks into `design-input-matrix.md`.
   * **Communication:** 
     > "Consolidating functional and non-functional requirements into design input matrix."
   * **Evidence:** `.artifacts/protocol-6/design-input-matrix.md`

3. **`[GUIDELINE]` Map Key Assumptions:**
   * **Action:** Translate outstanding assumptions into design checkpoints for later validation; store in `design-assumptions.md`.

### STEP 2: Architecture Decomposition

1. **`[MUST]` Identify System Boundaries:**
   * **Action:** Use `plan_from_brief.py` to derive domains, services, and integration surfaces; output to `architecture-boundaries.json`.
   * **Communication:** 
     > "[PHASE 2] - Mapping system boundaries and core components."
   * **Evidence:** `.artifacts/protocol-6/architecture-boundaries.json`

2. **`[MUST]` Capture Architecture Decisions:**
   * **Action:** Create Architecture Decision Records (ADRs) for key choices, including rationale, constraints, and alternatives; compile in `architecture-decisions.md`.
   * **Communication:** 
     > "Documenting architecture decisions with traceable rationale."
   * **Evidence:** `.artifacts/protocol-6/architecture-decisions.md`

3. **`[GUIDELINE]` Produce Interaction Diagrams:**
   * **Action:** Generate sequence/data flow diagram showing critical interactions; save as `interaction-diagram.drawio` or `interaction-diagram.md`.

### STEP 3: Specification Packaging & Validation

1. **`[MUST]` Assemble Technical Design Document:**
   * **Action:** Compile inputs, boundaries, ADRs, data contracts, security notes, and operational considerations into `TECHNICAL-DESIGN.md`.
   * **Communication:** 
     > "[PHASE 3] - Assembling comprehensive technical design specification."
   * **Evidence:** `.artifacts/protocol-6/TECHNICAL-DESIGN.md`

2. **`[MUST]` Validate Compliance and Feasibility:**
   * **Action:** Run `python scripts/validate_workflow_integration.py --design .artifacts/protocol-6/TECHNICAL-DESIGN.md --output .artifacts/protocol-6/design-validation-report.json` covering security, integration, and performance constraints.
   * **Communication:** 
     > "Design validation status: {status}; review report for details."
   * **Evidence:** `.artifacts/protocol-6/design-validation-report.json`

3. **`[GUIDELINE]` Draft Implementation Roadmap:**
   * **Action:** Outline epics/modules, sequencing, and readiness criteria in `implementation-roadmap.md`.

### STEP 4: Approval & Handoff Preparation

1. **`[MUST]` Conduct Stakeholder Review:**
   * **Action:** Present design summary, diagram, and decisions; log approvals in `design-approval-record.json` with timestamps and approvers.
   * **Communication:** 
     > "[PHASE 4] - Requesting stakeholder approval for technical design."
   * **Halt condition:** Do not continue without recorded approval or documented waiver.
   * **Evidence:** `.artifacts/protocol-6/design-approval-record.json`

2. **`[MUST]` Generate Task Inputs:**
   * **Action:** Export component responsibilities, interfaces, and dependencies into `task-generation-input.json` for Protocol 2.
   * **Evidence:** `.artifacts/protocol-6/task-generation-input.json`

3. **`[GUIDELINE]` Archive Artifacts:**
   * **Action:** Produce `design-artifact-manifest.json` listing all diagrams, ADRs, validation reports, and locations.

---

## 6. INTEGRATION POINTS

### Inputs From:
- **Protocol 01**: `PROJECT-BRIEF.md`, `project-brief-validation-report.json`, `BRIEF-APPROVAL-RECORD.json` - Strategic alignment.
- **Protocol 1**: `prd-{feature}.md`, `technical-specs.md`, `prd-validation.json` - Detailed functional/technical requirements.
- **Protocol 00-CD**: `risk-register.md`, `assumptions-v1.md` - Risk and assumption context.

### Outputs To:
- **Protocol 2**: `task-generation-input.json`, `TECHNICAL-DESIGN.md`, `implementation-roadmap.md` - Task planning data.
- **Protocol 7**: `design-validation-report.json`, `architecture-boundaries.json` - Environment setup dependencies.

### Artifact Storage Locations:
- `.artifacts/protocol-6/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 6. QUALITY GATES

### Gate 1: Source Alignment Gate
- **Criteria**: Project Brief and PRD validated, discovery risks acknowledged, design input matrix complete.
- **Evidence**: `source-alignment-report.json`, `design-input-matrix.md`
- **Pass Threshold**: Validation status `pass`, no missing artifacts.
- **Failure Handling**: Obtain updated inputs, refresh reports, rerun validation.
- **Automation**: `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-6/source-alignment-report.json`

### Gate 2: Architecture Integrity Gate
- **Criteria**: Boundaries defined, ADRs documented, interaction diagrams generated.
- **Evidence**: `architecture-boundaries.json`, `architecture-decisions.md`, `interaction-diagram.*`
- **Pass Threshold**: All core components mapped with traceable decisions.
- **Failure Handling**: Reassess decomposition, update ADRs, rerun gate.
- **Automation**: `python scripts/plan_from_brief.py --brief PROJECT-BRIEF.md --output .artifacts/protocol-6/architecture-boundaries.json`

### Gate 3: Design Validation Gate
- **Criteria**: Compliance validation passes with no critical issues, risks mitigated, assumptions addressed.
- **Evidence**: `design-validation-report.json`, `design-assumptions.md`
- **Pass Threshold**: Validation script returns `pass` and all critical risks mitigated.
- **Failure Handling**: Update design, adjust ADRs, rerun validation script.
- **Automation**: `python scripts/validate_workflow_integration.py --design .artifacts/protocol-6/TECHNICAL-DESIGN.md --output .artifacts/protocol-6/design-validation-report.json`

### Gate 4: Approval & Handoff Gate
- **Criteria**: Stakeholder approvals logged, task-generation input produced, artifact manifest created.
- **Evidence**: `design-approval-record.json`, `task-generation-input.json`, `design-artifact-manifest.json`
- **Pass Threshold**: Approval status `approved`, outputs delivered to downstream protocols.
- **Failure Handling**: Follow up for approval, document waivers, ensure outputs regenerated.
- **Automation**: `python scripts/validate_design_handoff.py --input .artifacts/protocol-6/task-generation-input.json`

---

## 6. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Validating PRD and discovery inputs for architecture design."
[MASTER RAY™ | PHASE 2 START] - "Decomposing system boundaries and documenting decisions."
[MASTER RAY™ | PHASE 3 START] - "Compiling technical design and running validation checks."
[MASTER RAY™ | PHASE 4 START] - "Seeking stakeholder approval and packaging task inputs."
[PHASE COMPLETE] - "Technical design approved; artifacts archived in .artifacts/protocol-6/."
[RAY ERROR] - "Issue encountered during [phase]; see corresponding report for details."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Technical design package ready. Evidence includes:
> - source-alignment-report.json
> - architecture-decisions.md
> - design-validation-report.json
> - task-generation-input.json
>
> Confirm readiness to initiate Protocol 2: Generate Tasks."
```

### Error Handling:
```
[RAY GATE FAILED: Design Validation Gate]
> "Quality gate 'Design Validation' failed.
> Criteria: Compliance validation must pass with no critical issues.
> Actual: Security review flagged unauthenticated webhook integration.
> Required action: Update TECHNICAL-DESIGN.md with auth flow, rerun validation.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 6. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_6.py

# Quality gate automation
python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-6/source-alignment-report.json
python scripts/plan_from_brief.py --brief PROJECT-BRIEF.md --output .artifacts/protocol-6/architecture-boundaries.json
python scripts/validate_workflow_integration.py --design .artifacts/protocol-6/TECHNICAL-DESIGN.md --output .artifacts/protocol-6/design-validation-report.json
python scripts/validate_design_handoff.py --input .artifacts/protocol-6/task-generation-input.json

# Evidence aggregation
python scripts/aggregate_evidence_6.py --output .artifacts/protocol-6/
```

### CI/CD Integration:
```yaml
name: Protocol 6 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 6 Gates
        run: python scripts/run_protocol_6_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct architecture review meeting; record minutes in `manual-design-review.md`.
2. Perform manual compliance checklist; store results in `.artifacts/protocol-6/manual-compliance-checklist.md`.
3. Document manual validation evidence in `.artifacts/protocol-6/manual-validation-log.md`.

---

## 6. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 2:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 2: Technical Task Generation

**Evidence Package:**
- `TECHNICAL-DESIGN.md` - Comprehensive architecture guide
- `task-generation-input.json` - Structured input for task generation automation

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/2-generate-tasks.md
```

---

## 6. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `source-alignment-report.json` | `.artifacts/protocol-6/` | Input verification evidence | Protocol 2 |
| `architecture-boundaries.json` | `.artifacts/protocol-6/` | Component & boundary mapping | Protocols 2 & 7 |
| `architecture-decisions.md` | `.artifacts/protocol-6/` | Decision rationale log | Protocol 2 |
| `TECHNICAL-DESIGN.md` | `.artifacts/protocol-6/` | Master technical spec | Protocols 2 & 7 |
| `design-validation-report.json` | `.artifacts/protocol-6/` | Compliance validation proof | Protocol 7 |
| `task-generation-input.json` | `.artifacts/protocol-6/` | Task generation dataset | Protocol 2 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

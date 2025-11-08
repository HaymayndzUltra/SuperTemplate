---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL AR: ARCHITECTURE REVIEW (SOFTWARE DESIGN COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `architecture-decision-log.json` from Protocol 6 – authoritative architecture decisions
- [ ] `system-context-diagram.png` from Protocol 6 – context boundary diagram
- [ ] `service-contracts.yaml` from Protocol 9 – API/interface contracts
- [ ] `quality-audit-architecture-findings.json` from Protocol 4 – audit observations
- [ ] `performance-architecture-profile.md` from Protocol 14 – performance implications
- [ ] `security-risk-log.csv` from Security Check Protocol – security constraints

### Required Approvals
- [ ] Technical Design Authority approval to convene review board
- [ ] Lead Architect confirmation of review scope and criteria
- [ ] Product Owner acknowledgement of architectural risk appetite

### System State Requirements
- [ ] Architecture repository accessible with read permissions
- [ ] Modeling tool licenses active for diagram updates (e.g., Draw.io, PlantUML)
- [ ] Collaboration workspace available for review annotations

---

## AR. AI ROLE AND MISSION

You are an **Architecture Review Chair**. Your mission is to validate that the solution architecture aligns with standards, satisfies quality attributes, and mitigates systemic risks before downstream delivery proceeds.

**🚫 [CRITICAL] DO NOT approve the architecture unless all critical risks have documented mitigations and traceability to backlog actions.**

---

## AR. ARCHITECTURE REVIEW WORKFLOW

### STEP 1: Review Preparation & Context Alignment

1. **`[MUST]` Validate Architectural Inputs:**
   * **Action:** Confirm all prerequisite artifacts are present, current, and traceable to requirements.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Verifying architecture review prerequisites and artifact freshness..."
   * **Halt condition:** Stop if any artifact missing or stale beyond agreed threshold.
   * **Evidence:** `.artifacts/review-architecture/input-validation.json` logging artifact status.

2. **`[MUST]` Establish Review Goals & Quality Attributes:**
   * **Action:** Define prioritized quality attributes (scalability, reliability, security, maintainability) and success criteria.
   * **Communication:** 
     > "[PHASE 1] Documenting prioritized quality attributes and acceptance criteria for architecture review..."
   * **Halt condition:** Pause if stakeholders disagree on prioritized attributes.
   * **Evidence:** `.artifacts/review-architecture/quality-attribute-matrix.csv`.

3. **`[GUIDELINE]` Prepare Architecture Overview Deck:**
   * **Action:** Assemble slides summarizing system context, domain model, deployment topology, and integration flows.
   * **Example:**
     ```bash
     python scripts/generate_arch_review_deck.py --adl architecture-decision-log.json --output .artifacts/review-architecture/overview-deck.pdf
     ```

### STEP 2: Structural Analysis & Risk Identification

1. **`[MUST]` Evaluate Modular Boundaries & Coupling:**
   * **Action:** Assess adherence to bounded context boundaries, interface contracts, and coupling metrics.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Reviewing modular boundaries, interfaces, and coupling metrics..."
   * **Halt condition:** Halt if coupling violations or boundary breaches detected without remediation plan.
   * **Evidence:** `.artifacts/review-architecture/boundary-analysis.md` with findings.

2. **`[MUST]` Assess Quality Attribute Scenarios:**
   * **Action:** Run scenario-based evaluations for prioritized attributes (performance spikes, failover, security events).
   * **Communication:** 
     > "[PHASE 2] Assessing quality attribute scenarios against architecture design..."
   * **Halt condition:** Pause if scenarios fail without mitigation.
   * **Evidence:** `.artifacts/review-architecture/quality-scenarios.json` capturing scenario, result, mitigation.

3. **`[GUIDELINE]` Perform Architecture Fitness Function Checks:**
   * **Action:** Execute automated architecture linting or dependency analysis scripts.
   * **Example:**
     ```bash
     python scripts/run_arch_fitness_functions.py --config config/architecture-rules.yaml --output .artifacts/review-architecture/fitness-report.json
     ```

### STEP 3: Decisioning & Action Tracking

1. **`[MUST]` Document Findings & Risk Ratings:**
   * **Action:** Log issues, severity, impact, recommended actions, and ownership.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Documenting architecture review findings and assigning risk levels..."
   * **Halt condition:** Stop if critical findings lack mitigation path.
   * **Evidence:** `.artifacts/review-architecture/findings-register.csv` with severity, owner, due date.

2. **`[MUST]` Issue Review Decision & Conditions:**
   * **Action:** Determine approval status (approve/approve with conditions/reject) and communicate required follow-ups.
   * **Communication:** 
     > "[PHASE 3] Issuing architecture review decision. Stating conditions and next steps..."
   * **Halt condition:** Pause if decision cannot be reached due to unresolved disputes.
   * **Evidence:** `.artifacts/review-architecture/decision-record.md` documenting outcome and signatures.

3. **`[GUIDELINE]` Publish Architecture Improvement Backlog:**
   * **Action:** Push improvement tasks into engineering backlog or protocol 6 updates.
   * **Example:**
     ```json
     {
       "title": "Refine caching strategy for catalog service",
       "owner": "Platform Team",
       "due_sprint": "2024-W22",
       "linked_protocol": 6
     }
     ```

---

## AR. INTEGRATION POINTS

### Inputs From:
- **Protocol 6**: `architecture-decision-log.json`, `system-context-diagram.png` – core architecture artifacts
- **Protocol 9**: `service-contracts.yaml` – integration contracts for review
- **Protocol 4**: `quality-audit-architecture-findings.json` – prior audit considerations
- **Protocol 14**: `performance-architecture-profile.md` – performance constraints
- **Security Check Protocol**: `security-risk-log.csv` – security considerations

### Outputs To:
- **Protocol 6**: `architecture-review-findings.csv` – updates required for technical design
- **Protocol 2**: `architecture-action-items.json` – backlog updates for task planning
- **Protocol 4**: `architecture-risk-waivers.md` – waivers for quality audit follow-up

### Artifact Storage Locations:
- `.artifacts/review-architecture/` – Primary evidence storage
- `.cursor/context-kit/` – Context and configuration artifacts

---

## AR. QUALITY GATES

### Gate 1: Structural Compliance
- **Criteria**: No critical boundary violations; dependency graph passes fitness checks.
- **Evidence**: `.artifacts/review-architecture/boundary-analysis.md`, `fitness-report.json`.
- **Pass Threshold**: 0 critical findings, ≤3 medium findings.
- **Failure Handling**: Require remediation plan, schedule follow-up review, rerun gate.
- **Automation**: `python scripts/validate_gate_AR_structure.py --analysis .artifacts/review-architecture/boundary-analysis.md`

### Gate 2: Quality Attribute Validation
- **Criteria**: All prioritized scenarios validated with acceptable outcomes or mitigations.
- **Evidence**: `.artifacts/review-architecture/quality-scenarios.json`.
- **Pass Threshold**: 100% scenarios = `Pass` or `Pass with Mitigation`.
- **Failure Handling**: Define mitigation tasks, update decision record, rerun scenario analysis.
- **Automation**: `python scripts/validate_gate_AR_quality.py --scenarios .artifacts/review-architecture/quality-scenarios.json`

### Gate 3: Decision Traceability
- **Criteria**: Findings register items mapped to action owners and backlog references.
- **Evidence**: `.artifacts/review-architecture/findings-register.csv`, `.artifacts/review-architecture/decision-record.md`.
- **Pass Threshold**: 100% findings include owner, due date, action reference.
- **Failure Handling**: Assign missing ownership, update backlog, rerun validation.
- **Automation**: `python scripts/validate_gate_AR_traceability.py --register .artifacts/review-architecture/findings-register.csv`

---

## AR. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Starting architecture review preparation. Validating prerequisite artifacts."
[MASTER RAY™ | PHASE 2 COMPLETE] - "Structural analysis complete. Evidence: boundary-analysis.md, quality-scenarios.json."
[RAY VALIDATION REQUEST] - "Please confirm acceptance of architecture review decision and mitigation plan."
[RAY ERROR] - "Failed at quality attribute validation. Reason: Failover scenario lacks mitigation. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Architecture review decision is ready. Evidence includes:
> - findings-register.csv
> - decision-record.md
>
> Please review and confirm acceptance or provide additional guidance."
```

### Error Handling:
```
[RAY GATE FAILED: Structural Compliance]
> "Quality gate 'Structural Compliance' failed.
> Criteria: No critical boundary violations.
> Actual: Detected unauthorized dependency between billing and auth services.
> Required action: Implement architectural guard, update dependency rules, rerun validation.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## AR. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_AR.py

# Quality gate automation
python scripts/validate_gate_AR_structure.py --analysis .artifacts/review-architecture/boundary-analysis.md
python scripts/validate_gate_AR_quality.py --scenarios .artifacts/review-architecture/quality-scenarios.json
python scripts/validate_gate_AR_traceability.py --register .artifacts/review-architecture/findings-register.csv

# Evidence aggregation
python scripts/aggregate_evidence_AR.py --output .artifacts/review-architecture/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Architecture Review Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Architecture Review Gates
        run: python scripts/run_protocol_AR_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform whiteboard review with architecture council to inspect dependency graph.
2. Manually log scenario outcomes and mitigation commitments in shared workspace.
3. Document results in `.artifacts/review-architecture/manual-validation-log.md`

---

## AR. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 6:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 6: Technical Design & Architecture Specification

**Evidence Package:**
- `architecture-review-findings.csv` - Review findings and actions
- `architecture-risk-waivers.md` - Approved waivers and conditions

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md
```

---

## AR. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `input-validation.json` | `.artifacts/review-architecture/` | Track prerequisite completeness | Internal Audit |
| `findings-register.csv` | `.artifacts/review-architecture/` | Capture review findings & owners | Protocol 6 |
| `decision-record.md` | `.artifacts/review-architecture/` | Communicate review decision | Leadership |
| `architecture-review-findings.csv` | `.artifacts/review-architecture/` | Action import for backlog | Protocol 2 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

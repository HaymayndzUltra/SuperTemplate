---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 00B: CLIENT DISCOVERY INITIATION (PROJECT-SCOPING COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `PROPOSAL.md` from Protocol 00A (accepted proposal content)
- [ ] `proposal-summary.json` from Protocol 00A (proposal highlights)
- [ ] Client response transcript or email saved to `.artifacts/protocol-00B/client-reply.md`

### Required Approvals
- [ ] Business development lead approval to initiate structured discovery

### System State Requirements
- [ ] Scheduled communication channel established with client (email, call, or chat)
- [ ] Access to discovery templates within `.templates/discovery/`

---

## 00B. AI ROLE AND MISSION

You are a **Freelance Solutions Architect**. Your mission is to orchestrate a structured discovery session with the client, validate scope and expectations, and produce authoritative artifacts for the project brief.

**🚫 [CRITICAL] Do not advance to planning deliverables until every discovery question is answered and validated with the client.**

---

## 00B. CLIENT DISCOVERY WORKFLOW

### STEP 1: Context Alignment

1. **`[MUST]` Review Proposal and Client Response:**
   * **Action:** Synthesize proposal highlights and client feedback to identify priorities, tone, and unresolved questions; log results in `client-context-notes.md`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Reviewing accepted proposal and client reply to align objectives."
   * **Halt condition:** Stop if the client response is missing or ambiguous; request clarification.
   * **Evidence:** `.artifacts/protocol-00B/client-context-notes.md`

2. **`[GUIDELINE]` Capture Business Background:**
   * **Action:** Draft a one-paragraph summary of the client's business model, target users, and success metrics using public info or provided material.
   * **Example:**
     ```markdown
     **Business Snapshot**
     - Industry: HealthTech SaaS
     - Primary Users: Clinic administrators
     - Success Metric: Reduce patient intake time by 30%
     ```

### STEP 2: Requirement Deep Dive

1. **`[MUST]` Facilitate Feature Prioritization:**
   * **Action:** Guide the client through identifying mandatory MVP features versus optional backlog items; capture in `client-discovery-form.md`.
   * **Communication:** 
     > "[PHASE 2] - Confirming core features and optional roadmap items."
   * **Halt condition:** Pause if feature classifications are incomplete or conflicting.
   * **Evidence:** `.artifacts/protocol-00B/client-discovery-form.md`

2. **`[MUST]` Validate Technical and Integration Requirements:**
   * **Action:** Document stack preferences, compliance needs, integrations, and constraints in `scope-clarification.md`.
   * **Communication:** 
     > "[PHASE 2] - Documenting technology preferences, integrations, and compliance constraints."
   * **Evidence:** `.artifacts/protocol-00B/scope-clarification.md`

3. **`[GUIDELINE]` Capture Risks and Assumptions:**
   * **Action:** Note known risks, assumptions, and open questions for resolution in `risk-log.md`.
   * **Example:**
     ```markdown
     - Assumption: Client provides existing API documentation
     - Risk: Third-party auth provider contract pending renewal
     ```

### STEP 3: Delivery Framework Alignment

1. **`[MUST]` Confirm Timeline, Budget, and Milestones:**
   * **Action:** Establish milestone dates, success checkpoints, and budget guardrails; summarize in `timeline-discussion.md`.
   * **Communication:** 
     > "[PHASE 3] - Aligning delivery milestones, budget expectations, and decision points."
   * **Halt condition:** Await confirmation if budget or schedule remains unresolved.
   * **Evidence:** `.artifacts/protocol-00B/timeline-discussion.md`

2. **`[MUST]` Establish Collaboration and Communication Plan:**
   * **Action:** Agree on communication cadence, tools, timezone overlap, and escalation paths; record in `communication-plan.md`.
   * **Communication:** 
     > "[PHASE 3] - Finalizing collaboration channels and escalation procedure."
   * **Halt condition:** Pause until both parties confirm the communication plan.
   * **Evidence:** `.artifacts/protocol-00B/communication-plan.md`

3. **`[GUIDELINE]` Define Decision Governance:**
   * **Action:** Map decision owners, approval thresholds, and change-control expectations in `governance-map.md`.
   * **Example:**
     ```markdown
     | Decision Type | Owner | SLA |
     |---------------|-------|-----|
     | Scope Change  | Product Owner | 2 business days |
     ```

### STEP 4: Discovery Confirmation

1. **`[MUST]` Summarize Discovery Outcomes:**
   * **Action:** Compile a client-facing recap (`discovery-recap.md`) and send validation prompt to confirm accuracy.
   * **Communication:** 
     > "[PHASE 4] - Presenting discovery recap for client confirmation."
   * **Halt condition:** Stop until client explicitly approves the recap or requests updates.
   * **Evidence:** `.artifacts/protocol-00B/discovery-recap.md`

2. **`[GUIDELINE]` Archive Communication Evidence:**
   * **Action:** Store transcripts, call notes, and recordings in `.artifacts/protocol-00B/transcripts/` for audit trail.
   * **Example:**
     ```text
     2024-05-10-discovery-call.txt
     ```

---

## 00B. INTEGRATION POINTS

### Inputs From:
- **Protocol 00A**: `PROPOSAL.md`, `proposal-summary.json` - Baseline scope and commitments to validate with client.
- **Protocol 00**: `client-intake-log.md` - Original contact context and opportunity metadata.

### Outputs To:
- **Protocol 01**: `client-discovery-form.md`, `scope-clarification.md`, `discovery-recap.md` - Structured inputs for project brief drafting.
- **Protocol 00**: `communication-plan.md`, `governance-map.md` - Updates to organizational context kit.

### Artifact Storage Locations:
- `.artifacts/protocol-00B/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 00B. QUALITY GATES

### Gate 1: Objective Alignment Gate
- **Criteria**: Business objectives, user goals, and success metrics documented and approved.
- **Evidence**: `.artifacts/protocol-00B/client-context-notes.md`
- **Pass Threshold**: Coverage score ≥ 95% across objectives, users, and KPIs.
- **Failure Handling**: Re-engage client, fill missing objectives, document delays.
- **Automation**: `python scripts/validate_discovery_objectives.py --input .artifacts/protocol-00B/client-context-notes.md`

### Gate 2: Requirement Completeness Gate
- **Criteria**: MVP features, optional backlog, and technical constraints fully captured.
- **Evidence**: `.artifacts/protocol-00B/client-discovery-form.md`, `.artifacts/protocol-00B/scope-clarification.md`
- **Pass Threshold**: Requirement completeness score ≥ 0.9 and no open `critical` risks.
- **Failure Handling**: Pause, request missing data, update risk log, rerun gate.
- **Automation**: `python scripts/validate_discovery_scope.py --form .artifacts/protocol-00B/client-discovery-form.md`

### Gate 3: Expectation Alignment Gate
- **Criteria**: Timeline, budget, collaboration cadence, and governance confirmed by client.
- **Evidence**: `.artifacts/protocol-00B/timeline-discussion.md`, `.artifacts/protocol-00B/communication-plan.md`, `.artifacts/protocol-00B/governance-map.md`
- **Pass Threshold**: Client approval flag recorded in `discovery-recap.md`.
- **Failure Handling**: Escalate to account lead, negotiate adjustments, capture new agreement, rerun gate.
- **Automation**: `python scripts/validate_discovery_expectations.py --recap .artifacts/protocol-00B/discovery-recap.md`

### Gate 4: Discovery Confirmation Gate
- **Criteria**: Client-approved recap with no unresolved blockers and all artifacts archived.
- **Evidence**: `.artifacts/protocol-00B/discovery-recap.md`, `.artifacts/protocol-00B/transcripts/`
- **Pass Threshold**: Confirmation timestamp recorded and transcripts stored.
- **Failure Handling**: Document outstanding items, schedule follow-up, halt downstream protocols.
- **Automation**: `python scripts/check_client_confirmation.py --recap .artifacts/protocol-00B/discovery-recap.md`

---

## 00B. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Analyzing proposal acceptance and clarifying business objectives."
[MASTER RAY™ | PHASE 2 START] - "Gathering detailed functional and technical requirements."
[MASTER RAY™ | PHASE 3 START] - "Aligning delivery timeline, budget, and collaboration plan."
[MASTER RAY™ | PHASE 4 START] - "Sharing discovery recap for client approval."
[PHASE COMPLETE] - "Discovery artifacts finalized and archived."
[RAY ERROR] - "Issue encountered during [phase]. Refer to risk-log.md for context."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Discovery recap prepared with the following evidence:
> - client-context-notes.md
> - client-discovery-form.md
> - scope-clarification.md
> - timeline-discussion.md
> - communication-plan.md
>
> Please confirm client approval to proceed to Protocol 01: Project Brief Creation."
```

### Error Handling:
```
[RAY GATE FAILED: Requirement Completeness Gate]
> "Quality gate 'Requirement Completeness' failed.
> Criteria: MVP and optional feature lists must be complete.
> Actual: Missing integration requirements for payment provider.
> Required action: Schedule follow-up with client to capture missing details.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 00B. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_00B.py

# Quality gate automation
python scripts/validate_discovery_objectives.py --input .artifacts/protocol-00B/client-context-notes.md
python scripts/validate_discovery_scope.py --form .artifacts/protocol-00B/client-discovery-form.md
python scripts/validate_discovery_expectations.py --recap .artifacts/protocol-00B/discovery-recap.md

# Evidence aggregation
python scripts/aggregate_evidence_00B.py --output .artifacts/protocol-00B/
```

### CI/CD Integration:
```yaml
name: Protocol 00B Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 00B Gates
        run: python scripts/run_protocol_00B_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct live review of discovery forms with client and record notes in `manual-discovery-review.md`.
2. Obtain written confirmation via email and store `.eml` or `.pdf` copies under `.artifacts/protocol-00B/transcripts/`.
3. Document manual checks in `.artifacts/protocol-00B/manual-validation-log.md`.

---

## 00B. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 01:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 01: Project Brief Creation

**Evidence Package:**
- `client-discovery-form.md` - Validated functional requirements
- `discovery-recap.md` - Client-approved discovery summary

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/01-project-brief-creation.md
```

---

## 00B. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `client-context-notes.md` | `.artifacts/protocol-00B/` | Business objectives and goals | Protocol 01 |
| `client-discovery-form.md` | `.artifacts/protocol-00B/` | Structured feature list | Protocol 01 |
| `scope-clarification.md` | `.artifacts/protocol-00B/` | Technical preferences and constraints | Protocol 01 |
| `timeline-discussion.md` | `.artifacts/protocol-00B/` | Delivery expectations | Protocol 01 |
| `communication-plan.md` | `.artifacts/protocol-00B/` | Collaboration blueprint | Protocol 00 |
| `discovery-recap.md` | `.artifacts/protocol-00B/` | Client-approved summary | Protocol 01 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

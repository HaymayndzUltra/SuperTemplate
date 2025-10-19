---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 02: CLIENT DISCOVERY INITIATION (PROJECT-SCOPING COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `PROPOSAL.md` from Protocol 01 (accepted proposal content)
- [ ] `proposal-summary.json` from Protocol 01 (proposal highlights)
- [ ] Client response transcript or email saved to `.artifacts/protocol-02/client-reply.md`

### Required Approvals
- [ ] Business development lead approval to initiate structured discovery

### System State Requirements
- [ ] Scheduled communication channel established with client (email, call, or chat)
- [ ] Access to discovery templates within `.templates/discovery/`

---

## 02. AI ROLE AND MISSION

You are a **Freelance Solutions Architect**. Your mission is to orchestrate a structured discovery session with the client, validate scope and expectations, and produce authoritative artifacts for the project brief.

**🚫 [CRITICAL] Do not advance to planning deliverables until every discovery question is answered and validated with the client.**

---

## 02. CLIENT DISCOVERY WORKFLOW

### STEP 1: Context Alignment

1. **`[MUST]` Review Proposal and Client Response:**
   * **Action:** Synthesize proposal highlights and client feedback to identify priorities, tone, and unresolved questions; log results in `client-context-notes.md`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Reviewing accepted proposal and client reply to align objectives."
   * **Halt condition:** Stop if the client response is missing or ambiguous; request clarification.
   * **Evidence:** `.artifacts/protocol-02/client-context-notes.md`

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
   * **Evidence:** `.artifacts/protocol-02/client-discovery-form.md`

2. **`[MUST]` Validate Technical and Integration Requirements:**
   * **Action:** Document stack preferences, compliance needs, integrations, and constraints in `scope-clarification.md`.
   * **Communication:** 
     > "[PHASE 2] - Documenting technology preferences, integrations, and compliance constraints."
   * **Evidence:** `.artifacts/protocol-02/scope-clarification.md`

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
   * **Evidence:** `.artifacts/protocol-02/timeline-discussion.md`

2. **`[MUST]` Establish Collaboration and Communication Plan:**
   * **Action:** Agree on communication cadence, tools, timezone overlap, and escalation paths; record in `communication-plan.md`.
   * **Communication:** 
     > "[PHASE 3] - Finalizing collaboration channels and escalation procedure."
   * **Halt condition:** Pause until both parties confirm the communication plan.
   * **Evidence:** `.artifacts/protocol-02/communication-plan.md`

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
   * **Evidence:** `.artifacts/protocol-02/discovery-recap.md`

2. **`[GUIDELINE]` Archive Communication Evidence:**
   * **Action:** Store transcripts, call notes, and recordings in `.artifacts/protocol-02/transcripts/` for audit trail.
   * **Example:**
     ```text
     2024-05-10-discovery-call.txt
     ```

---

## 02. INTEGRATION POINTS

### Inputs From:
- **Protocol 01**: `PROPOSAL.md`, `proposal-summary.json` - Baseline scope and commitments to validate with client.
- **Protocol 04**: `client-intake-log.md` - Original contact context and opportunity metadata.

### Outputs To:
- **Protocol 03**: `client-discovery-form.md`, `scope-clarification.md`, `discovery-recap.md` - Structured inputs for project brief drafting.
- **Protocol 04**: `communication-plan.md`, `governance-map.md` - Updates to organizational context kit.

### Artifact Storage Locations:
- `.artifacts/protocol-02/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 02. QUALITY GATES

### Gate 1: Objective Alignment Gate
- **Criteria**: Business objectives, user goals, and success metrics documented and approved.
- **Evidence**: `.artifacts/protocol-02/client-context-notes.md`
- **Pass Threshold**: Coverage score ≥ 95% across objectives, users, and KPIs.
- **Failure Handling**: Re-engage client, fill missing objectives, document delays.
- **Automation**: `python scripts/validate_discovery_objectives.py --input .artifacts/protocol-02/client-context-notes.md`

### Gate 2: Requirement Completeness Gate
- **Criteria**: MVP features, optional backlog, and technical constraints fully captured.
- **Evidence**: `.artifacts/protocol-02/client-discovery-form.md`, `.artifacts/protocol-02/scope-clarification.md`
- **Pass Threshold**: Requirement completeness score ≥ 0.9 and no open `critical` risks.
- **Failure Handling**: Pause, request missing data, update risk log, rerun gate.
- **Automation**: `python scripts/validate_discovery_scope.py --form .artifacts/protocol-02/client-discovery-form.md`

### Gate 3: Expectation Alignment Gate
- **Criteria**: Timeline, budget, collaboration cadence, and governance confirmed by client.
- **Evidence**: `.artifacts/protocol-02/timeline-discussion.md`, `.artifacts/protocol-02/communication-plan.md`, `.artifacts/protocol-02/governance-map.md`
- **Pass Threshold**: Client approval flag recorded in `discovery-recap.md`.
- **Failure Handling**: Escalate to account lead, negotiate adjustments, capture new agreement, rerun gate.
- **Automation**: `python scripts/validate_discovery_expectations.py --recap .artifacts/protocol-02/discovery-recap.md`

### Gate 4: Discovery Confirmation Gate
- **Criteria**: Client-approved recap with no unresolved blockers and all artifacts archived.
- **Evidence**: `.artifacts/protocol-02/discovery-recap.md`, `.artifacts/protocol-02/transcripts/`
- **Pass Threshold**: Confirmation timestamp recorded and transcripts stored.
- **Failure Handling**: Document outstanding items, schedule follow-up, halt downstream protocols.
- **Automation**: `python scripts/check_client_confirmation.py --recap .artifacts/protocol-02/discovery-recap.md`

---

## 02. COMMUNICATION PROTOCOLS

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
> Please confirm client approval to proceed to Protocol 03: Project Brief Creation."
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

## 02. AUTOMATION HOOKS

### Gate Runner (Recommended):
```bash
# Run all quality gates with single command
python3 scripts/run_protocol_gates.py 02

# Aggregate evidence into manifest
python3 scripts/aggregate_evidence_02.py

# Output: .artifacts/protocol-02/gate-manifest.json
#         .artifacts/protocol-02/evidence-manifest.json
```

### Individual Validators (Advanced):
```bash
# Run gates individually for debugging
python3 scripts/validate_gate_02_objectives.py      # Gate 1: Objective alignment
python3 scripts/validate_gate_02_requirements.py    # Gate 2: Requirement completeness
python3 scripts/validate_gate_02_expectations.py    # Gate 3: Expectation alignment
python3 scripts/validate_gate_02_confirmation.py    # Gate 4: Discovery confirmation
```

### CI/CD Integration:
```yaml
name: Protocol 02 Gate Validation
on: [push, pull_request]
jobs:
  validate-gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run Protocol 02 Gates
        run: python3 scripts/run_protocol_gates.py 02
      
      - name: Aggregate Evidence
        run: python3 scripts/aggregate_evidence_02.py
      
      - name: Upload Evidence Manifest
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: protocol-02-evidence
          path: .artifacts/protocol-02/evidence-manifest.json
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct live review of discovery forms with client and record notes in `manual-discovery-review.md`.
2. Obtain written confirmation via email and store `.eml` or `.pdf` copies under `.artifacts/protocol-02/transcripts/`.
3. Document manual checks in `.artifacts/protocol-02/manual-validation-log.md`.

### Quick Reference:
- **Gate config**: `config/protocol_gates/02.yaml`
- **Full documentation**: `documentation/gate-automation-quick-reference.md`
- **Test integration**: `bash scripts/test_gate_integration.sh`

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

### Handoff to Protocol 03:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 03: Project Brief Creation

**Evidence Package:**
- `client-discovery-form.md` - Validated functional requirements
- `discovery-recap.md` - Client-approved discovery summary

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/03-project-brief-creation.md
```

---

## 00B. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `client-context-notes.md` | `.artifacts/protocol-02/` | Business objectives and goals | Protocol 03 |
| `client-discovery-form.md` | `.artifacts/protocol-02/` | Structured feature list | Protocol 03 |
| `scope-clarification.md` | `.artifacts/protocol-02/` | Technical preferences and constraints | Protocol 03 |
| `timeline-discussion.md` | `.artifacts/protocol-02/` | Delivery expectations | Protocol 03 |
| `communication-plan.md` | `.artifacts/protocol-02/` | Collaboration blueprint | Protocol 04 |
| `discovery-recap.md` | `.artifacts/protocol-02/` | Client-approved summary | Protocol 03 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

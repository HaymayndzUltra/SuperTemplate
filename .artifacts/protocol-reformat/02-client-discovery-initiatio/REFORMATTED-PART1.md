---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 02: CLIENT DISCOVERY INITIATION (PROJECT-SCOPING COMPLIANT)

**Purpose:** Orchestrate structured client discovery to validate scope, requirements, and expectations, producing authoritative artifacts for project brief creation. This protocol transforms proposal acceptance into actionable project definition through systematic requirements gathering, risk assessment, and stakeholder alignment.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT] All prerequisites must be met before protocol execution.**

### Required Artifacts
**[STRICT]** The following artifacts must exist and be validated:
- `PROPOSAL.md` from Protocol 01 (accepted proposal content)
- `proposal-summary.json` from Protocol 01 (proposal highlights)
- Client response transcript or email saved to `.artifacts/protocol-02/client-reply.md`

### Required Approvals
**[STRICT]** The following approvals must be obtained:
- Business development lead approval to initiate structured discovery

### System State Requirements
**[STRICT]** System must meet the following conditions:
- Scheduled communication channel established with client (email, call, or chat)
- Access to discovery templates within `.templates/discovery/`

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

You are a **Freelance Solutions Architect**. Your mission is to orchestrate a structured discovery session with the client, validate scope and expectations, and produce authoritative artifacts for the project brief.

**[STRICT] Do not advance to planning deliverables until every discovery question is answered and validated with the client.**

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### PHASE 1: Context Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for reviewing and capturing context -->

1. **`[MUST]` Review Proposal and Client Response:**
   * **Action:** Synthesize proposal highlights and client feedback to identify priorities, tone, and unresolved questions; log results in `client-context-notes.md`.
   * **Evidence:** `.artifacts/protocol-02/client-context-notes.md`
   * **Validation:** Client context notes contains business objectives, user goals, and success metrics.
   
   **Communication:** 
   > "[MASTER RAY™ | PHASE 1 START] - Reviewing accepted proposal and client reply to align objectives."
   
   **Halt condition:** Stop if the client response is missing or ambiguous; request clarification.

2. **`[GUIDELINE]` Capture Business Background:**
   * **Action:** Draft a one-paragraph summary of the client's business model, target users, and success metrics using public info or provided material.
   * **Evidence:** Business snapshot section in `client-context-notes.md`
   * **Validation:** Summary includes industry, primary users, and at least one success metric.
   
   **Example (DO):**
   ```markdown
   **Business Snapshot**
   - Industry: HealthTech SaaS
   - Primary Users: Clinic administrators
   - Success Metric: Reduce patient intake time by 30%
   ```

### PHASE 2: Requirement Deep Dive
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Critical prioritization and validation decisions requiring documented reasoning -->

1. **`[MUST]` Facilitate Feature Prioritization:**
   * **Action:** Guide the client through identifying mandatory MVP features versus optional backlog items; capture in `client-discovery-form.md`.
   
   **[REASONING]:**
   - **Premises:** Client has multiple feature requests, limited budget, and timeline constraints
   - **Constraints:** Must deliver working MVP within budget and timeline
   - **Alternatives Considered:**
     * **A)** Include all features in MVP - Rejected: exceeds budget and timeline
     * **B)** Strict MVP with minimal features - Selected: meets constraints
     * **C)** Phased approach with MVP + roadmap - Considered: depends on client flexibility
   - **Decision:** Prioritize features using MoSCoW method to ensure clear MVP scope
   - **Evidence:** Client communication history, budget constraints from proposal
   - **Risks & Mitigations:**
     * **Risk:** Feature creep during discovery → **Mitigation:** Document all requests but categorize strictly
     * **Risk:** Client dissatisfaction with limited MVP → **Mitigation:** Create detailed roadmap for future phases
   - **Acceptance Link:** Aligns with Protocol 01 proposal commitments
   
   * **Evidence:** `.artifacts/protocol-02/client-discovery-form.md`
   * **Validation:** MVP features list complete with acceptance criteria.
   
   **Communication:** 
   > "[PHASE 2] - Confirming core features and optional roadmap items."
   
   **Halt condition:** Pause if feature classifications are incomplete or conflicting.

2. **`[MUST]` Validate Technical and Integration Requirements:**
   * **Action:** Document stack preferences, compliance needs, integrations, and constraints in `scope-clarification.md`.
   
   **[REASONING]:**
   - **Premises:** Technical decisions impact architecture, timeline, and cost
   - **Constraints:** Client may have existing systems, compliance requirements
   - **Alternatives Considered:**
     * **A)** Greenfield approach with latest tech - Consider if no constraints
     * **B)** Integrate with existing systems - Required if legacy systems exist
     * **C)** Hybrid approach - Balance modern and legacy
   - **Decision:** Document all technical requirements and constraints explicitly
   - **Evidence:** Client technical documentation, compliance requirements
   - **Risks & Mitigations:**
     * **Risk:** Unknown integration complexity → **Mitigation:** Request technical deep dive if >5 integrations
   
   * **Evidence:** `.artifacts/protocol-02/scope-clarification.md`
   * **Validation:** Technical requirements include stack, integrations, and compliance needs.
   
   **Communication:** 
   > "[PHASE 2] - Documenting technology preferences, integrations, and compliance constraints."

3. **`[GUIDELINE]` Capture Risks and Assumptions:**
   * **Action:** Note known risks, assumptions, and open questions for resolution in `risk-log.md`.
   * **Evidence:** `.artifacts/protocol-02/risk-log.md`
   * **Validation:** Risk log contains at least identified risks with severity ratings.
   
   **Example (DO):**
   ```markdown
   - Assumption: Client provides existing API documentation
   - Risk: Third-party auth provider contract pending renewal
   ```

### PHASE 3: Delivery Framework Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward alignment and communication planning -->

1. **`[MUST]` Confirm Timeline, Budget, and Milestones:**
   * **Action:** Establish milestone dates, success checkpoints, and budget guardrails; summarize in `timeline-discussion.md`.
   * **Evidence:** `.artifacts/protocol-02/timeline-discussion.md`
   * **Validation:** Timeline includes start date, milestones, and delivery date.
   
   **Communication:** 
   > "[PHASE 3] - Aligning delivery milestones, budget expectations, and decision points."
   
   **Halt condition:** Await confirmation if budget or schedule remains unresolved.

2. **`[MUST]` Establish Collaboration and Communication Plan:**
   * **Action:** Agree on communication cadence, tools, timezone overlap, and escalation paths; record in `communication-plan.md`.
   * **Evidence:** `.artifacts/protocol-02/communication-plan.md`
   * **Validation:** Plan includes cadence, channels, and escalation procedure.
   
   **Communication:** 
   > "[PHASE 3] - Finalizing collaboration channels and escalation procedure."
   
   **Halt condition:** Pause until both parties confirm the communication plan.

3. **`[GUIDELINE]` Define Decision Governance:**
   * **Action:** Map decision owners, approval thresholds, and change-control expectations in `governance-map.md`.
   * **Evidence:** `.artifacts/protocol-02/governance-map.md`
   * **Validation:** Governance map includes decision types and owners.
   
   **Example (DO):**
   ```markdown
   | Decision Type | Owner | SLA |
   |---------------|-------|-----|
   | Scope Change  | Product Owner | 2 business days |
   ```

### PHASE 4: Discovery Confirmation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple confirmation and archival steps -->

1. **`[MUST]` Summarize Discovery Outcomes:**
   * **Action:** Compile a client-facing recap (`discovery-recap.md`) and send validation prompt to confirm accuracy.
   * **Evidence:** `.artifacts/protocol-02/discovery-recap.md`
   * **Validation:** Recap includes all discovery findings and client approval section.
   
   **Communication:** 
   > "[PHASE 4] - Presenting discovery recap for client confirmation."
   
   **Halt condition:** Stop until client explicitly approves the recap or requests updates.

2. **`[GUIDELINE]` Archive Communication Evidence:**
   * **Action:** Store transcripts, call notes, and recordings in `.artifacts/protocol-02/transcripts/` for audit trail.
   * **Evidence:** `.artifacts/protocol-02/transcripts/`
   * **Validation:** Transcripts folder contains at least one communication record.
   
   **Example (DO):**
   ```text
   2024-05-10-discovery-call.txt
   ```
## 4. REASONING & COGNITIVE PROCESS
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level protocol analysis and reasoning patterns documentation -->

### Reasoning Patterns

#### Primary Reasoning Pattern: Hierarchical Task Decomposition
- Break complex discovery into 4 sequential phases (Context → Requirements → Delivery → Confirmation)
- Each phase decomposes into concrete steps with defined inputs/outputs
- Pattern ensures completeness while maintaining focus

#### Secondary Reasoning Pattern: Risk-Based Triage
- Continuously assess risk severity and impact throughout discovery
- Apply decision trees to determine escalation needs
- Pattern enables proactive risk management vs. reactive firefighting

#### Tertiary Reasoning Pattern: Adaptive Template Selection
- Match client context (industry, maturity, preferences) to appropriate discovery approach
- Pattern reduces discovery friction and improves relevance

#### Pattern Improvement Strategy:
- Track pattern effectiveness via gate pass rates and client satisfaction
- Quarterly review identifies pattern weaknesses
- Iterate patterns based on empirical evidence from completed projects

### Decision Logic

#### Decision Point 1: Scope Validation Strategy
**Context:** Determining depth of technical investigation based on proposal complexity and client technical maturity.

**Decision Criteria:**
- Proposal mentions <5 integrations → Standard discovery flow
- Proposal mentions 5-10 integrations → Extended technical deep dive
- Proposal mentions >10 integrations or compliance requirements → Architect-led technical validation session
- Client demonstrates low technical fluency → Include glossary and visual diagrams in all artifacts

**Outcomes:**
- **Standard flow:** Use default `client-discovery-form.md` template
- **Extended flow:** Add `integration-inventory.md` and schedule dedicated technical session
- **Architect-led:** Escalate to Protocol 07 (Technical Design) preview, assign senior architect

**Logging:** Record decision in `client-context-notes.md` under `## Discovery Approach`

#### Decision Point 2: Risk Escalation Threshold
**Context:** Determining whether identified risks require immediate stakeholder notification.

**Decision Criteria:**
- Risk impacts timeline by >20% → Escalate to account lead immediately
- Risk introduces compliance gap → Escalate to legal/compliance team
- Risk blocks MVP delivery → Halt discovery, schedule emergency client call
- Risk is acceptable within contingency → Document in `risk-log.md`, continue

**Outcomes:**
- **Escalate:** Notify stakeholders via `governance-map.md` escalation path, document in `risk-escalation-log.md`
- **Continue:** Add risk to `discovery-recap.md`, include mitigation plan

**Logging:** Timestamp and rationale in `risk-log.md`

#### Decision Point 3: Discovery Completion Criteria
**Context:** Determining if discovery is sufficiently complete to proceed to Protocol 03.

**Decision Criteria:**
- All 4 quality gates passed → Proceed
- 3/4 gates passed + documented waivers → Conditional proceed with monitoring
- <3 gates passed → Halt, schedule additional discovery session
- Client approval pending for >72 hours → Escalate to account lead

**Outcomes:**
- **Proceed:** Execute handoff to Protocol 03
- **Conditional:** Proceed with flagged items tracked in `.artifacts/protocol-02/conditional-proceed-log.md`
- **Halt:** Document blockers, schedule follow-up, notify downstream teams

**Logging:** Final decision recorded in `discovery-recap.md` approval section

### Root Cause Analysis Framework

When discovery blockers or quality gate failures occur:

1. **Identify Symptom:** What immediate issue prevented progress? (e.g., "Gate 2 failed - incomplete integration requirements")
2. **Trace to Root Cause:**
   - Was prerequisite artifact missing/incomplete?
   - Did client lack internal alignment?
   - Were questions ambiguous or missing from template?
   - Did communication channel fail?
3. **Document in `discovery-blockers.md`:**
   ```markdown
   **Blocker:** Gate 2 failure
   **Root Cause:** Payment provider integration details unknown to client contact
   **Resolution:** Requested client connect us with technical lead at payment provider
   **Prevention:** Update discovery template to include "who owns integration details" question
   ```
4. **Implement Fix:** Update template, re-engage stakeholder, adjust timeline
5. **Validate Fix:** Re-run quality gate, confirm resolution

### Learning Mechanisms

#### Feedback Loops

**Feedback Loop 1: Client Experience**
- **Collection:** After each discovery session, client completes satisfaction survey (`.artifacts/protocol-02/client-feedback-YYYY-MM-DD.json`)
- **Analysis:** Monthly review identifies pain points, confusion areas, and value-add moments
- **Action:** Feedback scores <4.0 trigger template review and adjustment
- **Closure:** Updated templates tested on next 2 projects, feedback re-measured

**Feedback Loop 2: Quality Gate Performance**
- **Collection:** Automated gate results stored in `.artifacts/protocol-02/gate-history.json`
- **Analysis:** Quarterly analysis identifies consistently failing gates or criteria
- **Action:** Gate pass rate <80% for 3+ consecutive projects triggers criteria recalibration
- **Closure:** Adjusted gates monitored for 5 projects, validated against project success outcomes

**Feedback Loop 3: Downstream Protocol Issues**
- **Collection:** Protocol 03 logs missing/unclear discovery inputs in `.artifacts/protocol-03/upstream-issues-log.json`
- **Analysis:** Weekly review during active projects
- **Action:** Recurring issues (3+ mentions) trigger immediate discovery template enhancement
- **Closure:** Enhanced templates validated by Protocol 03 team before deployment

#### Improvement Tracking

**Metrics Dashboard:** `.artifacts/protocol-02/improvement-metrics-YYYY-QN.json`
- Discovery duration trend (target: <5 days)
- First-time gate pass rate trend (target: ≥80%)
- Client satisfaction trend (target: ≥4.5/5)
- Downstream rework requests (target: <10%)

**Template Evolution Log:** `.artifacts/protocol-02/template-changelog.md`
```markdown
## 2024-05-15: Added integration complexity triage
**Trigger:** 3 projects missed complex integrations in initial discovery
**Change:** Added Decision Point 1 with integration count thresholds
**Impact:** Next 5 projects correctly identified architecture needs (100% vs. 40%)
```

**Question Effectiveness Matrix:** `.artifacts/protocol-02/question-effectiveness.json`
```json
{
  "question_id": "Q2.3_integration_list",
  "times_asked": 47,
  "actionable_answers": 42,
  "confusion_rate": 0.11,
  "clarity_score": 0.89,
  "recommendation": "keep"
}
```

**Continuous Monitoring:** Automated alerts when:
- Gate pass rate drops >10% from baseline
- Discovery duration exceeds 7 days for 2+ consecutive projects
- Client satisfaction falls below 4.0

#### Knowledge Base Integration

**Knowledge Base Components:**

1. **Industry Templates Library:** `.templates/discovery/industries/`
   - Healthcare: HIPAA checklist, EHR integration questions
   - FinTech: PCI-DSS requirements, payment gateway inventory
   - E-commerce: Logistics integrations, payment flows
   - **Usage:** Auto-selected based on client industry tag from Protocol 01

2. **Client Personas Database:** `.artifacts/protocol-02/client-personas/`
   ```json
   {
     "persona_id": "technical-founder",
     "characteristics": ["high technical fluency", "fast decision-making", "prefers async"],
     "discovery_adjustments": ["skip technical glossary", "use detailed technical questions", "email-first communication"],
     "communication_style": "direct, technical, concise",
     "risk_tolerance": "high"
   }
   ```

3. **Common Blockers Playbook:** `.artifacts/protocol-02/common-blockers-playbook.md`
   ```markdown
   ## Blocker: Third-party integration details unavailable
   **Frequency:** 18% of projects
   **Root Cause:** Client contact lacks access to partner technical documentation
   **Resolution:** Request introduction to partner technical team OR use fallback: capture integration as "TBD" with contingency timeline buffer
   **Prevention:** Ask "Who owns technical details for each integration?" in Step 2.2
   ```

4. **Risk Checklists by Domain:** `.artifacts/protocol-02/risk-playbooks/`
   - Automatically presented based on project domain and compliance requirements

**Knowledge Base Growth Strategy:**
- After every 5 projects: Extract patterns, add to knowledge base
- Quarterly review: Identify gaps, commission new templates
- Annual audit: Remove outdated/unused knowledge base entries

#### Adaptation Mechanisms

**Adaptation 1: Template Customization**
- **Trigger:** Client industry + technical maturity profile identified in Protocol 01
- **Action:** Pre-populate `client-discovery-form.md` with industry-standard features, common integrations
- **Example:** E-commerce client automatically gets payment gateway, shipping, inventory questions
- **Benefit:** Reduces discovery time by 30%, improves question relevance

**Adaptation 2: Escalation Threshold Tuning**
- **Trigger:** Client risk tolerance score from prior engagement or Protocol 01 assessment
- **Action:** Adjust Decision Point 2 thresholds dynamically
- **Example:** Risk-tolerant startup: only escalate risks >50% impact; risk-averse enterprise: escalate >20%
- **Storage:** Client-specific overrides in `.artifacts/protocol-02/client-overrides/[client-id].json`

**Adaptation 3: Communication Channel Selection**
- **Trigger:** Client communication preferences from Protocol 01
- **Action:** Optimize discovery approach (live calls vs. async forms vs. hybrid)
- **Example:** Client prefers async → send detailed discovery form upfront; prefers sync → schedule live workshop
- **Benefit:** Improves client satisfaction by matching their workflow

**Adaptation 4: Gate Sensitivity Adjustment**
- **Trigger:** Project complexity score (simple, standard, complex)
- **Action:** Adjust quality gate pass thresholds
- **Example:** Simple project: 85% pass threshold; complex project: 95% pass threshold
- **Rationale:** Higher stakes projects need more thorough discovery validation
### Meta-Cognition

#### Self-Awareness and Process Awareness

**Awareness Statement Protocol:**
At the start of each workflow step, AI must generate and log awareness statement:

```markdown
## Self-Awareness Check - [Step X.Y] - [Timestamp]

**Current State:**
- Phase: [1-4 of 4]
- Step: [X.Y Step Name]
- Artifacts Completed: [X/Y] (list: artifact1, artifact2...)
- Artifacts Pending: [list]
- Blockers: [None | List with severity]

**Context Awareness:**
- Client Communication: [Active | Awaiting Response | Delayed >48h]
- Risk Level: [Low | Medium | High]
- Confidence in Current Outputs: [0-100%] based on [specific factors]

**Limitations Acknowledged:**
- Cannot proceed without: [specific inputs/approvals]
- Assumptions made: [list with validation plan]
- Information gaps: [list with resolution strategy]

**Next Action:**
- Immediate: [specific action]
- Requires: [resources/approvals needed]
- Expected completion: [timeframe]
```

**Example Self-Awareness Statements:**
- "I am currently in Discovery Phase 2 of 4 (Requirement Deep Dive), with 3 of 6 required artifacts completed."
- "I have identified 2 unresolved high-severity risks and 4 missing critical integration requirements that require client input before proceeding to Step 3."
- "My confidence in requirement completeness is 65% (Medium) based on: (1) 40% of integration questions unanswered, (2) client approval pending for 36 hours, (3) technical constraint section incomplete."
- "I am aware that I cannot validate technical feasibility without architecture review, which is deferred to Protocol 07."
- "I acknowledge I am making an assumption that client will provide API documentation; validation plan: confirm in next client call."

#### Process Monitoring and Progress Tracking

**Monitoring Dashboard:** `.artifacts/protocol-02/discovery-progress.md`

Auto-updated after each workflow step:
```markdown
# Discovery Progress Monitor

## Execution Timeline
- Started: 2024-05-10 09:00
- Current: 2024-05-10 14:30 (Day 1 of target ≤5 days)
- Projected completion: 2024-05-14 (within target)

## Workflow Steps Status
- [✓] Step 1.1: Review Proposal (completed 2024-05-10 10:00, duration: 1h)
- [✓] Step 1.2: Capture Background (completed 2024-05-10 10:30, duration: 0.5h)
- [⏳] Step 2.1: Facilitate Prioritization (in progress, started 2024-05-10 11:00)
- [ ] Step 2.2: Validate Technical Requirements (pending, blocked by: client prioritization incomplete)
- [ ] Step 2.3: Capture Risks (pending)
- [ ] Step 3.1: Confirm Timeline (pending)

## Quality Gates Status
- Gate 1: Not yet run (prerequisites: Step 1.2 complete ✓)
- Gate 2: Not yet run (prerequisites: Steps 2.1, 2.2 complete)
- Gate 3: Not yet run (prerequisites: Step 3.1, 3.2 complete)
- Gate 4: Not yet run (prerequisites: All gates 1-3 pass)

## Risk Indicators
- ⚠️ Client response delay: 36 hours (threshold: 48h)
- ✓ Discovery duration: Day 1 of 5 (on track)
- ✓ Artifact completeness: 50% (expected for day 1)

## Velocity Monitoring
- Current pace: 2 steps/day (target: 2-3 steps/day)
- Projected: 5 days total (within target ≤5 days)
```

**Automated Monitoring Alerts:**
- If discovery extends >5 business days → flag for review, notify account manager
- If gate pass rate <80% → trigger immediate retrospective
- If client non-responsive >72h → escalate to account lead
- If scope grows >150% from initial estimate → flag scope creep, propose renegotiation

#### Self-Correction Protocols and Error Recovery

**Self-Correction Trigger 1: Halt Condition Detection**
```markdown
## Halt Detected - [Step X.Y] - [Timestamp]

**Halt Type:** [Missing Input | Approval Required | Blocker | Error]
**Description:** [specific issue]
**Impact:** [blocks Steps X, Y, Z]
**Resolution Strategy:**
1. Log to `.artifacts/protocol-02/halt-log.md`
2. Notify: [Account Manager | Client | Technical Lead]
3. Required Action: [specific action needed]
4. Await: [approval | input | resolution]
5. Resume Point: [Step X.Y]

**Self-Correction Action Taken:**
- Preserved partial outputs: [list artifacts saved]
- Set resume bookmark: Step X.Y
- Escalated to: [role/person]
- Provided resolution options: [option 1, option 2]
```

**Self-Correction Trigger 2: Quality Gate Failure**
```markdown
## Gate Failure Detected - Gate [N] - [Timestamp]

**Gate:** [Gate Name]
**Score:** [actual] (threshold: [required])
**Failure Reasons:** [list specific criteria failed]

**Automated Corrective Action Plan:**
1. Analyze failure root cause: [diagnosis]

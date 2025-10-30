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
2. Identify missing artifacts/data: [list]
3. Propose fixes:
   - Option A: [description, effort, timeline]
   - Option B: [description, effort, timeline]
4. Request approval: [from role/person]
5. Re-run validation: [command to execute]

**Self-Awareness:** I acknowledge this gate failure blocks Protocol 03 handoff. I am proposing Option A (re-engage client for missing integration details) because [rationale].
```

**Self-Correction Trigger 3: Scope Creep Detection**
```markdown
## Scope Anomaly Detected - [Timestamp]

**Indicator:** Discovery form size: 127 requirements (initial estimate: 45, +182%)
**Threshold:** >150% triggers review
**Impact:** Timeline risk, budget risk

**Self-Correction Actions:**
1. Alert account lead: scope expansion detected
2. Categorize new requirements: [MVP vs. nice-to-have]
3. Propose scope negotiation: [options]
4. Document scope change: `.artifacts/protocol-02/scope-change-log.md`
5. Update timeline projection: [new estimate]

**Awareness:** I am aware this scope expansion may require contract amendment or phased delivery approach.
```

#### Continuous Improvement and Learning Integration

**Improvement Cycle:**
1. **Execution:** Run discovery protocol, collect metrics
2. **Retrospective:** After each project, document lessons (Protocol 22)
3. **Analysis:** Quarterly review of metrics, identify improvement opportunities
4. **Enhancement:** Update templates, thresholds, or workflows
5. **Validation:** Test enhancements on 2-3 projects
6. **Deployment:** Roll out validated improvements to all projects

**Improvement Tracking:**
- **Retrospective Schedule:** Within 24h of Protocol 02 completion
- **Template Review Cadence:** Quarterly (or after 10 projects, whichever comes first)
- **Gate Calibration:** After every 20 projects, analyze pass rates and adjust thresholds
- **Tool Evaluation:** If >3 projects encounter same blocker, evaluate process/template enhancement

**Learning Integration:**
- Capture lessons in `.artifacts/protocol-02/lessons-learned.md`
- Update knowledge base after every 5 projects
- Share improvements in weekly delivery syncs
- Incorporate high-impact lessons into Protocol 22 (Implementation Retrospective)

---

## 5. REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Continuous improvement and learning integration for protocol evolution -->

### Retrospective Guidance

After completing discovery (successful or halted), conduct micro-retrospective:

**Timing:** Within 24 hours of Protocol 02 completion or halt

**Participants:** Account lead, delivery lead, AI orchestrator

**Agenda:**
1. **What went well:**
   - Which discovery questions yielded highest-value insights?
   - Which communication approaches worked effectively?
   - Were quality gates appropriately calibrated?

2. **What went poorly:**
   - Which questions caused confusion or yielded unusable answers?
   - Were there unexpected blockers not covered by risk framework?
   - Did any artifacts require rework after handoff to Protocol 03?

3. **Action items:**
   - Template updates required?
   - Escalation thresholds need adjustment?
   - New risks to add to standard checklist?

**Output:** `.artifacts/protocol-02/discovery-retrospective-YYYY-MM-DD.md`

### Continuous Improvement Opportunities

#### Identified Improvement Opportunities

**Opportunity 1: Automated Risk Detection**
- **Current State:** Manual risk identification in Step 2.3
- **Opportunity:** Use ML model to scan discovery inputs for risk keywords/patterns
- **Potential Impact:** Reduce missed risks by 40%, save 2 hours per discovery
- **Priority:** High
- **Timeline:** Q3 2024

**Opportunity 2: Client Persona Auto-Classification**
- **Current State:** Manual classification based on Protocol 01 notes
- **Opportunity:** Auto-classify based on communication patterns, industry, company size
- **Potential Impact:** Improve template matching accuracy from 70% to 90%
- **Priority:** Medium
- **Timeline:** Q4 2024

**Opportunity 3: Real-Time Discovery Progress Dashboard**
- **Current State:** Static progress.md file, manual updates
- **Opportunity:** Live web dashboard with stakeholder access
- **Potential Impact:** Improve transparency, reduce status update requests by 60%
- **Priority:** Low
- **Timeline:** Q1 2025

#### Process Optimization Tracking
- **Discovery duration:** Target <5 business days from Protocol 01 acceptance to Protocol 02 completion
- **First-time gate pass rate:** Target ≥80% for each quality gate
- **Client satisfaction:** Target ≥4.5/5 on discovery process (captured in `discovery-recap.md`)

#### Tracking Mechanisms and Metrics
- **Quarterly metrics dashboard:** `.artifacts/protocol-02/metrics-YYYY-QN.json`
  ```json
  {
    "quarter": "2024-Q2",
    "projects_completed": 12,
    "average_discovery_days": 4.2,
    "gate_pass_rates": {"gate1": 0.92, "gate2": 0.83, "gate3": 0.88, "gate4": 0.95},
    "common_blockers": ["integration details unavailable", "budget ambiguity"],
    "template_updates": 3
  }
  ```

- **Improvement Tracking Log:** `.artifacts/protocol-02/improvement-tracking-log.md`
  ```markdown
  ## 2024-Q2 Improvements
  - **Implemented:** Decision Point 1 (Scope Validation Strategy)
  - **Metric:** Gate 2 pass rate improved from 0.78 to 0.87 (+12%)
  - **Status:** ✅ Validated, deployed to all projects
  ```

#### Evidence of Improvement and Validation
- **Blocker reduction:** Track repeat blocker frequency; target 20% reduction quarter-over-quarter
- **Template effectiveness:** Measure question-to-actionable-answer ratio; target ≥85%
- **Downstream rework:** Monitor Protocol 03 requests for discovery clarification; target <10% per project
- **Velocity improvement:** Track discovery duration trend; target 10% reduction year-over-year
- **Quality improvement:** Track gate pass rate trend; target 5% increase year-over-year

### System Evolution

#### Version History
- **Current Version:** 2.0 (2024-05-01)
- **Previous Version:** 1.5 (2024-01-15) - Added risk escalation decision tree
- **Previous Version:** 1.0 (2023-10-01) - Initial structured discovery protocol

#### Rationale for Changes
- **v1.5 → v2.0:** Added Decision Point 2 (Risk Escalation Threshold) after 3 projects experienced late-stage risk surprises; improved early risk visibility
- **v1.0 → v1.5:** Introduced `governance-map.md` after client confusion over decision authority caused delays

#### Impact Assessment
- **v2.0 Impact:** Average discovery duration reduced from 6.5 days to 4.2 days (35% improvement)
- **v1.5 Impact:** Risk-related project delays reduced from 40% to 15% of projects

#### Rollback Procedures

**If Protocol 02 changes cause degradation (e.g., gate pass rates drop >15%):**

1. **Immediate:** Revert to previous protocol version from `.cursor/ai-driven-workflow/archive/02-client-discovery-initiation-v[X.Y].md`
2. **Notify:** Alert all active projects to use archived version
3. **Analyze:** Conduct root cause analysis of what caused degradation
4. **Test Fix:** Pilot updated protocol on 1-2 low-risk projects before re-deploying
5. **Document:** Record rollback event and resolution in `.artifacts/protocol-02/protocol-evolution-log.md`
### Knowledge Capture and Organizational Learning

#### Lessons Learned Repository and Documentation

**Purpose:** Systematically capture and disseminate discovery insights to accelerate team learning.

**Lessons Learned Structure:**

Maintain `.artifacts/protocol-02/lessons-learned.md` with standardized format:

```markdown
### Lesson: [Title]
**Project:** [Project Name/ID]
**Date:** YYYY-MM-DD
**Context:** [What happened]
**Insight:** [What we learned]
**Action:** [How we changed process/template]
**Outcome:** [Result of change]
**Applicable To:** [All projects | Specific industry | Specific client type]
```

**Recent Lessons Example:**
```markdown
### Lesson: Early Architecture Review Prevents Scope Creep
**Project:** HealthTech Portal v2
**Date:** 2024-03-15
**Context:** Client requested "simple user dashboard" but had 12 complex integrations
**Insight:** Integration complexity not discoverable without technical deep dive
**Action:** Added Decision Point 1 (Scope Validation Strategy) with integration threshold
**Outcome:** Next 3 similar projects identified architecture needs early, preventing late surprises
**Applicable To:** All projects with >5 integrations

### Lesson: Async Discovery Forms Work Better for Technical Founders
**Project:** SaaS Analytics Platform
**Date:** 2024-04-02
**Context:** Technical founder preferred detailed written questions over synchronous calls
**Insight:** Technical clients value precision and documentation over speed
**Action:** Created "Technical Founder" persona with async-first discovery approach
**Outcome:** Client satisfaction score increased from 4.2 to 4.8 for this persona
**Applicable To:** Technical founder persona
```

#### Knowledge Base Growth and Maintenance

**Knowledge Base Components:**
1. **Industry-specific templates:** After 3+ projects in same industry, create specialized discovery template
2. **Client personas library:** Document communication preferences, decision-making styles for repeat clients
3. **Risk playbooks:** Build industry-specific risk checklists (`.artifacts/protocol-02/risk-playbooks/[industry].md`)
4. **Blocker resolution patterns:** Common issues and proven solutions

**Knowledge Base Update Cadence:**
- **After every 5 projects:** Extract lessons, update knowledge base
- **Quarterly review:** Identify gaps, commission new content
- **Annual audit:** Archive outdated content, consolidate overlapping entries

**Knowledge Base Quality Metrics:**
- **Coverage:** % of projects that benefit from knowledge base (target: ≥70%)
- **Accuracy:** % of knowledge base recommendations that prove effective (target: ≥85%)
- **Freshness:** % of entries updated in last 12 months (target: ≥80%)

#### Knowledge Sharing Mechanisms and Distribution

**Internal Sharing:**
1. **Weekly Delivery Sync:**
   - Share 1-2 recent high-impact lessons
   - Present blocker resolutions and template updates
   - Solicit feedback on proposed improvements

2. **Monthly Knowledge Base Newsletter:**
   - Highlight new templates, personas, risk playbooks
   - Share success metrics (gate pass rates, client satisfaction)
   - Announce upcoming protocol enhancements

3. **Quarterly Learning Sessions:**
   - Deep dive into specific improvement opportunities
   - Workshop new reasoning patterns or decision trees
   - Cross-team knowledge exchange

**External Sharing (Client-Facing):**
- Share anonymized best practices with clients (e.g., "Discovery Best Practices for Healthcare Projects")
- Builds credibility and demonstrates expertise

**Onboarding Integration:**
- Incorporate high-impact lessons into new team member training
- Use real project examples to illustrate reasoning patterns
- Provide knowledge base tour during first week

**Knowledge Storage and Access:**
- **Central Repository:** `.artifacts/protocol-02/knowledge-base/`
- **Search Tool:** `python scripts/search_knowledge_base.py --query "[keywords]"`
- **Access Control:** Team members have read access; leads have write access

### Future Planning

#### Roadmap
- **Q3 2024:** Integrate AI-assisted discovery form generation based on proposal analysis
- **Q4 2024:** Build discovery analytics dashboard for real-time gate pass monitoring
- **Q1 2025:** Pilot automated risk assessment using historical project data

#### Priorities
1. **High:** Reduce average discovery duration to <3 days (currently 4.2)
2. **High:** Increase first-time gate pass rate to ≥90% (currently 85%)
3. **Medium:** Build industry-specific template library (currently 0, target 5)
4. **Low:** Automate discovery recap generation (currently manual)

#### Resource Requirements
- **Q3 2024:** 40 hours engineering time for AI form generation feature
- **Q4 2024:** BI tool license for analytics dashboard ($2k/year)
- **Q1 2025:** Historical data cleanup and ML model training (80 hours data science time)

#### Timeline
- **May 2024:** Complete v2.1 with enhanced risk escalation automation
- **August 2024:** Launch AI form generation pilot
- **November 2024:** Deploy analytics dashboard
- **February 2025:** Risk assessment automation beta

---

## 6. INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### Inputs From:
**[STRICT]** The following inputs must be validated before execution:
- **Protocol 01**: `PROPOSAL.md`, `proposal-summary.json` - Baseline scope and commitments to validate with client.
- **Protocol 04**: `client-intake-log.md` - Original contact context and opportunity metadata.

### Outputs To:
**[STRICT]** The following outputs must be generated for downstream protocols:
- **Protocol 03**: `client-discovery-form.md`, `scope-clarification.md`, `discovery-recap.md` - Structured inputs for project brief drafting.
- **Protocol 04**: `communication-plan.md`, `governance-map.md` - Updates to organizational context kit.

### Artifact Storage Locations:
**[STRICT]** All artifacts must be stored in standardized locations:
- `.artifacts/protocol-02/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 7. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and criteria -->

### Gate 1: Objective Alignment Gate
**[STRICT]** This gate validates business objectives, user goals, and success metrics.
- **Criteria**: Business objectives, user goals, and success metrics documented and approved.
- **Evidence**: `.artifacts/protocol-02/client-context-notes.md`
- **Pass Threshold**: Coverage score ≥ 95% across objectives, users, and KPIs.
- **Failure Handling**: Re-engage client, fill missing objectives, document delays.
- **Automation**: `python scripts/validate_discovery_objectives.py --input .artifacts/protocol-02/client-context-notes.md`

### Gate 2: Requirement Completeness Gate
**[STRICT]** This gate validates MVP features, optional backlog, and technical constraints.
- **Criteria**: MVP features, optional backlog, and technical constraints fully captured.
- **Evidence**: `.artifacts/protocol-02/client-discovery-form.md`, `.artifacts/protocol-02/scope-clarification.md`
- **Pass Threshold**: Requirement completeness score ≥ 0.9 and no open `critical` risks.
- **Failure Handling**: Pause, request missing data, update risk log, rerun gate.
- **Automation**: `python scripts/validate_discovery_scope.py --form .artifacts/protocol-02/client-discovery-form.md`

### Gate 3: Expectation Alignment Gate
**[STRICT]** This gate validates timeline, budget, collaboration, and governance.
- **Criteria**: Timeline, budget, collaboration cadence, and governance confirmed by client.
- **Evidence**: `.artifacts/protocol-02/timeline-discussion.md`, `.artifacts/protocol-02/communication-plan.md`, `.artifacts/protocol-02/governance-map.md`
- **Pass Threshold**: Client approval flag recorded in `discovery-recap.md`.
- **Failure Handling**: Escalate to account lead, negotiate adjustments, capture new agreement, rerun gate.
- **Automation**: `python scripts/validate_discovery_expectations.py --recap .artifacts/protocol-02/discovery-recap.md`

### Gate 4: Discovery Confirmation Gate
**[STRICT]** This gate validates client approval and artifact completeness.
- **Criteria**: Client-approved recap with no unresolved blockers and all artifacts archived.
- **Evidence**: `.artifacts/protocol-02/discovery-recap.md`, `.artifacts/protocol-02/transcripts/`
- **Pass Threshold**: Confirmation timestamp recorded and transcripts stored.
- **Failure Handling**: Document outstanding items, schedule follow-up, halt downstream protocols.
- **Automation**: `python scripts/check_client_confirmation.py --recap .artifacts/protocol-02/discovery-recap.md`

---

## 8. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### Status Announcements:
**[STRICT]** Use standardized announcements for phase transitions:
```
[MASTER RAY™ | PHASE 1 START] - "Analyzing proposal acceptance and clarifying business objectives."
[MASTER RAY™ | PHASE 2 START] - "Gathering detailed functional and technical requirements."
[MASTER RAY™ | PHASE 3 START] - "Aligning delivery timeline, budget, and collaboration plan."
[MASTER RAY™ | PHASE 4 START] - "Sharing discovery recap for client approval."
[PHASE COMPLETE] - "Discovery artifacts finalized and archived."
[RAY ERROR] - "Issue encountered during [phase]. Refer to risk-log.md for context."
```

### Validation Prompts:
**[STRICT]** Use standardized prompts for validation requests:
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
**[STRICT]** Use standardized error messages for gate failures:
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

## 9. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### Validation Scripts:

#### Gate 1: Objective Alignment
1. **`[MUST]` Run objective validation:**
   * **Action:** Execute validation script to check business objectives and success criteria
   * **Evidence:** `.artifacts/protocol-02/gate1-validation.json`
   * **Validation:** Exit code 0 and coverage_score ≥ 0.95
   
   ```bash
   # Validate business objectives and success criteria
   python scripts/validate_discovery_objectives.py \
     --input .artifacts/protocol-02/client-context-notes.md \
     --output .artifacts/protocol-02/gate1-validation.json \
     --threshold 0.95
   
   # Exit codes: 0=pass, 1=fail, 2=warning
   # Logs: .artifacts/protocol-02/gate1-validation.log
   # Output format: JSON with coverage_score, missing_fields, recommendations
   # Owner: discovery team
   # CI Integration: runs on commit to .artifacts/protocol-02/
   ```

#### Gate 2: Requirement Completeness
1. **`[MUST]` Run scope validation:**
   * **Action:** Execute validation script to check feature prioritization and scope clarity
   * **Evidence:** `.artifacts/protocol-02/gate2-validation.json`
   * **Validation:** Exit code 0 and completeness_score ≥ 0.9
   
   ```bash
   # Validate feature prioritization and scope clarity
   python scripts/validate_discovery_scope.py \
     --form .artifacts/protocol-02/client-discovery-form.md \
     --clarification .artifacts/protocol-02/scope-clarification.md \
     --output .artifacts/protocol-02/gate2-validation.json \
     --completeness-threshold 0.9
   
   # Exit codes: 0=pass, 1=fail (missing critical fields), 2=warning (missing optional fields)
   # Logs: .artifacts/protocol-02/gate2-validation.log
   # Output: JSON with completeness_score, missing_requirements, risk_flags
   # Owner: solutions architect team
   # CI Integration: runs on merge to main
   ```
#### Gate 3: Expectation Alignment
1. **`[MUST]` Run expectation validation:**
   * **Action:** Execute validation script to check timeline, budget, and collaboration agreements
   * **Evidence:** `.artifacts/protocol-02/gate3-validation.json`
   * **Validation:** Exit code 0 and client approval confirmed
   
   ```bash
   # Validate timeline, budget, and collaboration agreements
   python scripts/validate_discovery_expectations.py \
     --recap .artifacts/protocol-02/discovery-recap.md \
     --timeline .artifacts/protocol-02/timeline-discussion.md \
     --comms .artifacts/protocol-02/communication-plan.md \
     --output .artifacts/protocol-02/gate3-validation.json
   
   # Exit codes: 0=pass (client approved), 1=fail (missing approval), 3=escalation required
   # Logs: .artifacts/protocol-02/gate3-validation.log
   # Output: JSON with approval_status, pending_items, escalation_recommendations
   # Owner: account management team
   # CI Integration: manual trigger only (requires client input)
   ```

#### Evidence Aggregation
1. **`[MUST]` Aggregate evidence artifacts:**
   * **Action:** Execute script to collect and validate all discovery artifacts
   * **Evidence:** `.artifacts/protocol-02/evidence-manifest.json`
   * **Validation:** Exit code 0 and all required artifacts present
   
   ```bash
   # Aggregate all discovery artifacts into evidence package
   python scripts/aggregate_evidence_02.py \
     --input-dir .artifacts/protocol-02/ \
     --output .artifacts/protocol-02/evidence-manifest.json \
     --include-transcripts \
     --validate-integrity
   
   # Exit codes: 0=success, 1=missing artifacts, 2=integrity check failed
   # Logs: .artifacts/protocol-02/evidence-aggregation.log
   # Output: JSON manifest with artifact_list, checksums, timestamps, completeness_score
   # Owner: protocol orchestration team
   # Registry: scripts/script-registry.json → protocol-gates.evidence-aggregation
   ```

#### Prerequisite Validation
1. **`[MUST]` Validate prerequisites:**
   * **Action:** Execute script to check all prerequisites before starting discovery
   * **Evidence:** `.artifacts/protocol-02/prereq-validation.json`
   * **Validation:** Exit code 0 and all prerequisites met
   
   ```bash
   # Validate all prerequisites before starting discovery
   python scripts/validate_prerequisites_02.py \
     --check-artifacts \
     --check-approvals \
     --check-system-state \
     --output .artifacts/protocol-02/prereq-validation.json
   
   # Exit codes: 0=all met, 1=missing prerequisites, 2=partial (can proceed with warnings)
   # Logs: .artifacts/protocol-02/prereq-validation.log
   # Output: JSON with prerequisites_status, missing_items, blocking_issues
   # Owner: protocol orchestration team
   # Note: Must run BEFORE any workflow steps
   ```

### CI/CD Integration:
```yaml
name: Protocol 02 Validation Pipeline
on:
  push:
    paths:
      - '.artifacts/protocol-02/**'
  pull_request:
    paths:
      - '.cursor/ai-driven-workflow/02-*.md'

jobs:
  validate-gates:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run Protocol 02 Quality Gates
        run: |
          python3 scripts/run_protocol_gates.py \
            --protocol 02 \
            --fail-on-gate-failure \
            --output .artifacts/protocol-02/ci-gate-results.json
        continue-on-error: false
      
      - name: Upload gate results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: protocol-02-gate-results
          path: .artifacts/protocol-02/*-validation.json
      
      - name: Comment on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(fs.readFileSync('.artifacts/protocol-02/ci-gate-results.json'));
            const comment = `## Protocol 02 Validation Results\n\n${results.summary}`;
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

### Script Execution Context

**Environment Requirements:**
- Python 3.9+
- Dependencies: `pyyaml`, `jsonschema`, `pydantic` (see `requirements.txt`)
- Environment variables: `PROJECT_ROOT`, `ARTIFACTS_DIR` (optional, defaults to `.artifacts/`)

**Permissions:**
- Read access: `.artifacts/protocol-01/`, `.artifacts/protocol-02/`
- Write access: `.artifacts/protocol-02/`
- No external API credentials required

**Output Capture:**
All validation scripts write structured JSON to `--output` path and human-readable logs to `.log` file with same basename:
```bash
# Example: Both files created
.artifacts/protocol-02/gate1-validation.json  # Machine-readable
.artifacts/protocol-02/gate1-validation.log   # Human-readable
```

### Manual Fallbacks:

**When automation is unavailable:**

1. **Manual Discovery Review:**
   - Conduct live review session with client
   - Document in `.artifacts/protocol-02/manual-discovery-review.md`
   - Use checklist from `.templates/discovery/manual-review-checklist.md`
   - Record session: `.artifacts/protocol-02/transcripts/YYYY-MM-DD-review-session.txt`

2. **Manual Gate Validation:**
   - For each gate, complete manual checklist:
     ```markdown
     ## Gate 1 Manual Validation
     - [ ] Business objectives documented (min 3)
     - [ ] User personas identified (min 2)
     - [ ] Success metrics defined (min 3 KPIs)
     - [ ] Client approval obtained (email/signature)
     ```
   - Store completed checklists: `.artifacts/protocol-02/manual-gate-[N]-checklist.md`

3. **Evidence Collection:**
   - Obtain written confirmation via email → save as `.artifacts/protocol-02/transcripts/client-approval-YYYY-MM-DD.eml`
   - Scan signed documents → save as `.artifacts/protocol-02/transcripts/signed-discovery-recap-YYYY-MM-DD.pdf`
   - Log all manual validations: `.artifacts/protocol-02/manual-validation-log.md`

4. **Manual Evidence Aggregation:**
   - Create evidence manifest manually: `.artifacts/protocol-02/manual-evidence-manifest.json`
   - Use template from `.templates/discovery/evidence-manifest-template.json`
   - Include checksums (SHA-256) of all artifacts for integrity verification

---

## 10. HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple checklist execution for protocol completion -->

### Pre-Handoff Validation:

1. **`[MUST]` Validate protocol completion:**
   * **Action:** Verify all prerequisites were met and workflow steps completed
   * **Evidence:** Completed checklist in protocol execution log
   * **Validation:** All items checked
   
   **Checklist:**
   - [ ] All prerequisites were met
   - [ ] All workflow steps completed successfully
   - [ ] All quality gates passed (or waivers documented)
   - [ ] All evidence artifacts captured and stored
   - [ ] All integration outputs generated
   - [ ] All automation hooks executed successfully
   - [ ] Communication log complete

### Handoff to Protocol 03:

1. **`[MUST]` Execute protocol handoff:**
   * **Action:** Package evidence and trigger Protocol 03
   * **Evidence:** Handoff confirmation in execution log
   * **Validation:** Protocol 03 acknowledges receipt
   
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

## 11. EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for evidence collection and quality metrics -->

### Learning and Improvement Mechanisms

**[STRICT]** All artifacts must generate feedback for continuous improvement:

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.

### Generated Artifacts:

**[STRICT]** The following artifacts must be generated and validated:

| Artifact | Location | Purpose | Consumer | Verification Owner |
|----------|----------|---------|----------|-------------------|
| `client-context-notes.md` | `.artifacts/protocol-02/` | Business objectives and goals | Protocol 03 | Solutions Architect |
| `client-discovery-form.md` | `.artifacts/protocol-02/` | Structured feature list | Protocol 03 | Product Owner |
| `scope-clarification.md` | `.artifacts/protocol-02/` | Technical preferences and constraints | Protocol 03, 07 | Technical Lead |
| `timeline-discussion.md` | `.artifacts/protocol-02/` | Delivery expectations | Protocol 03, 08 | Account Manager |
| `communication-plan.md` | `.artifacts/protocol-02/` | Collaboration blueprint | Protocol 04 | Delivery Manager |
| `governance-map.md` | `.artifacts/protocol-02/` | Decision authority matrix | Protocol 04, 20 | Account Manager |
| `risk-log.md` | `.artifacts/protocol-02/` | Identified risks and mitigation | Protocol 03, 08, 17 | Risk Manager |
| `discovery-recap.md` | `.artifacts/protocol-02/` | Client-approved summary | Protocol 03 | Account Manager |
| `gate1-validation.json` | `.artifacts/protocol-02/` | Gate 1 validation results | Protocol 04, CI/CD | Automation |
| `gate2-validation.json` | `.artifacts/protocol-02/` | Gate 2 validation results | Protocol 04, CI/CD | Automation |
| `gate3-validation.json` | `.artifacts/protocol-02/` | Gate 3 validation results | Protocol 04, CI/CD | Automation |
| `evidence-manifest.json` | `.artifacts/protocol-02/` | Complete evidence package | Protocol 03, 20, 22 | Protocol Orchestrator |

### Traceability Matrix

**Upstream Dependencies:**
- Input artifacts inherit from: Protocol 01, Protocol 04
- Configuration dependencies: `.templates/discovery/`, `scripts/script-registry.json`
- External dependencies: Client communication channel

**Downstream Consumers:**
- Output artifacts consumed by: Protocol 03, Protocol 04, Protocol 07, Protocol 08, Protocol 17, Protocol 20, Protocol 22
- Shared artifacts: `communication-plan.md`, `governance-map.md`, `risk-log.md`
- Archive requirements: 7-year retention per compliance

**Verification Chain:**
- Each artifact includes: SHA-256 checksum, timestamp, verified_by field
- Verification procedure: Run `scripts/validate_protocol_handoffs.py`
- Audit trail: All artifact modifications logged in protocol execution log

### Archival and Traceability

**Evidence Manifest Schema:**
```json
{
  "protocol_id": "02",
  "execution_timestamp": "2024-05-10T14:30:00Z",
  "artifacts": [
    {
      "name": "client-discovery-form.md",
      "path": ".artifacts/protocol-02/client-discovery-form.md",
      "sha256": "abc123...",
      "created": "2024-05-10T14:15:00Z",
      "verified_by": "product-owner@example.com",
      "verification_timestamp": "2024-05-10T14:20:00Z"
    }
  ],
  "quality_gates": [
    {"gate_id": "gate1", "status": "pass", "score": 0.97, "timestamp": "2024-05-10T14:25:00Z"},
    {"gate_id": "gate2", "status": "pass", "score": 0.92, "timestamp": "2024-05-10T14:28:00Z"}
  ],
  "traceability_links": {
    "upstream_protocols": ["01"],
    "downstream_protocols": ["03", "04"],
    "related_artifacts": [".artifacts/protocol-01/PROPOSAL.md"]
  }
}
```

**Archival Procedure:**
1. Generate evidence manifest: `python scripts/aggregate_evidence_02.py --validate-integrity`
2. Create archive bundle: `.artifacts/protocol-02/archive/protocol-02-YYYY-MM-DD-HHmm.tar.gz`
3. Upload to long-term storage: `s3://project-archives/protocol-02/[project-id]/[timestamp]/`
4. Record archive location in project ledger: `.artifacts/project-ledger.json`

**Retention Policy:**
- Active project artifacts: Retain in `.artifacts/protocol-02/` until project closure
- Archived artifacts: Retain for 7 years per compliance requirements
- PII-containing artifacts: Purge after 30 days post-project completion (per GDPR)

### Quality Metrics:

**[STRICT]** Track and maintain the following quality metrics:

| Metric | Target | Baseline | Current | Status | Trend |
|--------|--------|----------|---------|--------|-------|
| Gate 1 Pass Rate | ≥ 95% | 0.88 | 0.92 | ⚠️ Warning | ↗️ +4% |
| Gate 2 Pass Rate | ≥ 90% | 0.83 | 0.87 | ⚠️ Warning | ↗️ +5% |
| Gate 3 Pass Rate | ≥ 95% | 0.88 | 0.91 | ⚠️ Warning | ↗️ +3% |
| Gate 4 Pass Rate | ≥ 95% | 0.95 | 0.96 | ✅ Pass | ↗️ +1% |
| Evidence Completeness | 100% | 0.94 | 0.98 | ⚠️ Warning | ↗️ +4% |
| Integration Integrity | 100% | 0.97 | 0.99 | ⚠️ Warning | ↗️ +2% |
| Client Satisfaction | ≥ 4.5/5 | 4.2 | 4.6 | ✅ Pass | ↗️ +0.4 |
| Discovery Duration (days) | ≤ 5 | 6.5 | 4.2 | ✅ Pass | ↗️ -2.3 |

**Quality Gate History:** `.artifacts/protocol-02/gate-history.json`

### Downstream Handoff Verification

**Verification Checklist for Protocol 03:**
- [ ] `client-discovery-form.md` contains ≥5 MVP features with acceptance criteria
- [ ] `scope-clarification.md` includes tech stack preferences and constraints
- [ ] `discovery-recap.md` has client approval timestamp and signature
- [ ] All quality gates passed or have documented waivers
- [ ] Evidence manifest generated and archived

**Verification Procedure:**
```bash
# Run downstream handoff verification
python scripts/validate_protocol_handoffs.py \
  --from-protocol 02 \
  --to-protocol 03 \
  --output .artifacts/protocol-02/handoff-verification.json

# Exit code 0 = ready for handoff, 1 = missing artifacts, 2 = quality gate failures
```

**Verification Owner:** Protocol Orchestrator (automated) + Account Manager (final approval)
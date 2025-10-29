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

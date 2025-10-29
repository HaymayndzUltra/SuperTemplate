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

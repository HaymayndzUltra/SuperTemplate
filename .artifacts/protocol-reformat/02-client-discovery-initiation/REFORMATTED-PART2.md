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

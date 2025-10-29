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

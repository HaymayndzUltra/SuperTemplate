# Governance Map - Decision Authority Matrix

**Project:** Surfa - AI-powered Local SEO SaaS Platform  
**Generated:** 2025-10-31  
**Protocol:** 02 - Client Discovery Initiation

---

## Decision Authority Matrix

| Decision Type | Owner | Approval Required | SLA | Escalation Path |
|---------------|-------|-------------------|-----|-----------------|
| **Technical Implementation** | Developer | None (inform only) | N/A | Client (if concern raised) |
| **Library/Package Selection** | Developer | Client (if adds cost/risk) | 1 business day | N/A |
| **Code Architecture** | Developer | None (within approved stack) | N/A | N/A |
| **UX/UI Changes** | Client | Client approval required | 1 business day | Developer proposes, client decides |
| **Feature Scope Addition** | Client | Mutual agreement + change order | 2 business days | Formal scope change process |
| **Feature Scope Removal** | Client | Client decision | Same day | Developer notified immediately |
| **Timeline Adjustment** | Developer (proposes) | Client approval required | 1 business day | Mutual negotiation |
| **Budget Change** | Client | Mutual agreement + written approval | 2 business days | Formal change order |
| **Milestone Acceptance** | Client | Client validates + approves | 2 business days | Developer re-tests if rejected |
| **Payment Approval** | Client | Client authorizes payment | Per Net-15 terms | N/A |
| **Production Deployment** | Developer (executes) | Client approval required | Same day | Pre-deployment checklist |
| **Emergency Hotfix** | Developer | Client notification (post-fix) | <4 hours | Post-fix review |
| **Performance Target Adjustment** | Client | Mutual agreement | 1 business day | Document rationale |
| **Third-Party Service Changes** | Client | Client approval required | 1 business day | Cost/risk assessment |
| **Data Access/Permissions** | Client | Client grants access | Same day | Secure credential sharing |

---

## Roles & Responsibilities

### Developer (Technical Lead)
**Primary Responsibilities:**
- Code implementation (M1, M2, M3 deliverables)
- Technical architecture decisions (within agreed stack)
- Testing (unit, integration, E2E)
- Staging deployment automation
- Daily progress updates
- Blocker escalation
- Performance optimization
- Security best practices (RLS, webhook idempotency)

**Decision Authority:**
- Implementation details (code structure, testing approach)
- Technical debt trade-offs (within timeline/budget)
- Library selection (if no new cost/risk)
- Git workflow and branching strategy

**Approval Required For:**
- Scope changes (adding/removing features)
- Timeline adjustments (if delay >1 day)
- Budget modifications
- Production deployment (go-live decision)
- Performance target changes

**Communication Obligations:**
- Daily EOD updates (Slack)
- Blocker escalation (<4 hours)
- Milestone reviews (end of M1, M2, M3)
- Immediate notification of critical issues

---

### Client (Product Owner / Project Sponsor)
**Primary Responsibilities:**
- Requirement clarification
- Acceptance criteria validation
- Staging testing and feedback
- Milestone approval (quality gates)
- Payment authorization (per milestone)
- Credential provisioning (Stripe, GBP, Supabase)
- Business decision-making (scope, timeline, budget)

**Decision Authority:**
- Feature prioritization (MVP vs. backlog)
- UX/UI approval
- Scope changes (approve/reject)
- Milestone acceptance (pass/fail)
- Production deployment timing
- Budget allocation

**Approval Required For:**
- Major technical architecture changes (if affects maintainability)
- Third-party service additions (if new ongoing cost)

**Communication Obligations:**
- Respond to blocker escalations (<1 hour during 10am-6pm EST)
- Milestone review and approval (<2 business days)
- Staging feedback (within 1 business day)
- Credential sharing (by Monday start date)

---

## Decision-Making Processes

### Process 1: Technical Implementation Decisions
**Owner:** Developer  
**Approval Required:** No (inform client via daily update)

**Examples:**
- "Implementing retry logic using exponential backoff strategy"
- "Using React Query for API state management"
- "Adding Cypress for E2E testing"

**Communication:**
```markdown
💻 **Technical Decision - [Date]**

**Decision:** [Description]
**Rationale:** [Why this approach]
**Impact:** [Timeline/budget/risk: none expected]
**Alternatives Considered:** [Brief mention if relevant]

[No approval needed - informing for transparency]
```

---

### Process 2: Feature Scope Change
**Owner:** Client (approves/rejects)  
**Initiator:** Either party can propose  
**SLA:** 2 business days for decision

**Trigger Scenarios:**
- Client requests feature not in original proposal
- Developer identifies missing requirement during discovery
- Performance target adjustment needed

**Process:**
1. **Proposal:** Initiator documents change request (see template below)
2. **Impact Analysis:** Developer estimates effort, timeline, budget impact
3. **Options:** Present options (approve, defer, reject)
4. **Client Decision:** Client chooses within 2 business days
5. **Documentation:** Update `client-discovery-form.md` if scope changes
6. **Timeline Adjustment:** Update `timeline-discussion.md` if applicable

**Template:**
```markdown
📋 **Scope Change Request - [Date]**

**Requested By:** [Client/Developer]

**Description:** [What's being added/changed/removed]

**Rationale:** [Why this change is needed]

**Impact Analysis:**
- Effort: [hours]
- Cost: [$amount]
- Timeline: [+/- X days to milestone]
- Risk: [Low/Medium/High - description]

**Options:**
1. **Approve + Adjust:** Add to current milestone (delay M[X] by Y days, increase budget by $Z)
2. **Defer:** Move to post-launch backlog (no immediate impact)
3. **Reject:** Do not implement (no change)

**Developer Recommendation:** [Option X] because [rationale]

**Client Decision:** [To be confirmed]
```

---

### Process 3: Milestone Acceptance
**Owner:** Client (validates and approves)  
**SLA:** 2 business days from milestone completion notification

**Process:**
1. **Developer:** Completes milestone deliverables, deploys to staging
2. **Developer:** Sends milestone review notification (Slack)
3. **Client:** Tests on staging environment (within 2 business days)
4. **Client:** Validates acceptance criteria (checklist in `client-discovery-form.md`)
5. **Client:** Decision:
   - **PASS:** Approve milestone, authorize payment
   - **FAIL:** Document issues, developer fixes, re-submit for validation

**Acceptance Criteria Template:**
```markdown
✅ **Milestone [N] Acceptance - [Date]**

**Deliverables:**
- [Feature 1]: ✅ Pass / ❌ Fail - [Comments]
- [Feature 2]: ✅ Pass / ❌ Fail - [Comments]

**Acceptance Criteria:**
- [Criterion 1]: ✅ Met / ❌ Not Met
- [Criterion 2]: ✅ Met / ❌ Not Met

**Known Issues:**
- [None] OR [List with severity: P0-critical, P1-high, P2-medium, P3-low]

**Decision:**
- ✅ **APPROVED** - Invoice approved, proceed to M[N+1]
- ❌ **REJECTED** - Issues to resolve: [list]

**Client Signature:** [Name, Date]
```

**Rejection Handling:**
- Developer fixes issues within 1-2 business days
- Re-deploy to staging
- Client re-validates (1 business day)
- Payment released upon approval

---

### Process 4: Production Deployment (Go/No-Go)
**Owner:** Client (final approval), Developer (executes deployment)  
**SLA:** Same day decision

**Pre-Deployment Checklist:**
- [ ] All M1 + M2 + M3 milestones approved
- [ ] Staging validation complete (all tests pass)
- [ ] No P0/P1 bugs outstanding
- [ ] Vercel Pro upgrade confirmed
- [ ] Stripe live mode credentials configured
- [ ] RLS policies validated (zero data leakage)
- [ ] Performance targets met (<500ms dashboard load)
- [ ] Monitoring + error logging active
- [ ] Rollback plan documented

**Decision Matrix:**
| Criteria | Status | Go/No-Go |
|----------|--------|----------|
| All milestones approved | ✅ Yes | Go |
| P0 bugs outstanding | ❌ Yes | **NO-GO** (must fix) |
| P1 bugs outstanding | ⚠️ Yes | Client decision (risk tolerance) |
| Performance <500ms | ✅ Yes | Go |
| Performance <750ms | ⚠️ Yes | Client decision (accept vs. delay) |
| Performance >750ms | ❌ | **NO-GO** (must optimize) |
| RLS validated | ✅ Yes | Go |
| RLS not validated | ❌ | **NO-GO** (critical security) |

**Go Decision:**
- Client approves deployment (Slack confirmation)
- Developer executes production deployment
- Developer performs smoke test post-deployment
- Client validates production environment
- M3 milestone approved + final payment authorized

**No-Go Decision:**
- Document blocking issues
- Developer fixes blocking issues
- Re-run validation
- Reschedule deployment (typically +1-3 days)

---

### Process 5: Emergency Escalation
**Owner:** Developer (identifies), Client (approves action)  
**SLA:** <1 hour response (during client's 10am-6pm EST availability)

**Trigger Scenarios:**
- Critical bug discovered (P0 - breaks core functionality)
- Security vulnerability identified
- Third-party API outage blocking progress
- Data integrity issue

**Process:**
1. **Developer:** Immediate Slack notification (see template below)
2. **Client:** Respond within 1 hour (during availability)
3. **Decision:** Approve recommended action OR propose alternative
4. **Execution:** Developer implements fix/mitigation
5. **Post-Mortem:** Document incident + resolution (within 24 hours)

**Template:**
```markdown
🚨 **EMERGENCY ESCALATION - [Severity: P0/P1]**

**Issue:** [Brief description]

**Impact:**
- Affected: [Feature/users/data]
- Severity: [P0-Critical / P1-High]
- Timeline: [Blocking milestone? Yes/No]

**Recommended Action:**
[Specific proposed fix/mitigation]

**Alternatives:**
1. [Option A]
2. [Option B]

**Risk of Recommended Action:**
[Low/Medium/High - explain]

**Need Approval:** YES / NO (if no, this is FYI notification)

**Urgency:** [Can wait X hours] OR [Need decision NOW]
```

**Post-Incident:**
- Document root cause
- Implement preventive measures
- Update testing/monitoring to catch similar issues

---

## Change Control & Governance

### Scope Baseline
**Source of Truth:** `.artifacts/protocol-02/client-discovery-form.md` (MVP features)

**Change Tracking:**
- All approved scope changes logged in `governance-map.md` (this document)
- Rejected changes logged with rationale
- Timeline/budget impacts tracked in `timeline-discussion.md`

### Version Control
**Governance Artifacts:**
- `client-discovery-form.md` → Version controlled (Git)
- `timeline-discussion.md` → Version controlled (Git)
- `communication-plan.md` → Version controlled (Git)
- `governance-map.md` → Version controlled (Git)

**Change Log:**
```markdown
## Scope Change Log

### [Date] - [Change ID]
- **Type:** [Addition/Removal/Modification]
- **Description:** [What changed]
- **Approved By:** [Client name]
- **Impact:** Timeline +X days, Budget +$Y
- **Rationale:** [Why change was needed]
```

---

## Conflict Resolution

### Disagreement on Scope
**Scenario:** Developer believes feature is out of scope, client believes it's included

**Resolution:**
1. Reference `client-discovery-form.md` MVP section
2. Review original proposal (`PROPOSAL.md`)
3. If ambiguous: Developer provides effort estimate → Client decides (approve vs. defer)
4. Document decision in scope change log

---

### Disagreement on Quality
**Scenario:** Client rejects milestone, developer believes acceptance criteria met

**Resolution:**
1. Review acceptance criteria in `client-discovery-form.md`
2. Test on staging together (async or live call)
3. Identify specific failing criteria (must be objective, measurable)
4. Developer fixes objective failures
5. If criteria are subjective/unclear: Clarify criteria, re-test

---

### Timeline Dispute
**Scenario:** Developer needs more time, client has hard deadline

**Resolution:**
1. Developer documents blocker/reason for delay
2. Propose options:
   - **Option A:** Reduce scope (defer features to backlog)
   - **Option B:** Extend timeline (move deadline)
   - **Option C:** Add resources (increase budget)
3. Client chooses option
4. Update timeline and communicate to all stakeholders

---

## Audit Trail & Documentation

### Decision Log
**Location:** `.artifacts/protocol-02/decision-log.md` (created as needed)

**Format:**
```markdown
## Decision Log

### [Date] - Decision ID-001
- **Decision:** [What was decided]
- **Type:** [Technical/Scope/Timeline/Budget]
- **Owner:** [Who made decision]
- **Rationale:** [Why]
- **Impact:** [Timeline/budget/risk]
- **Alternatives Rejected:** [List]
```

### Communication Archive
**Location:** `.artifacts/protocol-02/transcripts/`

**Contents:**
- Milestone review recordings/notes
- Important Slack threads (exported)
- Scope change approvals
- Client feedback emails

---

**Evidence:** `.artifacts/protocol-02/governance-map.md`  
**Status:** ✅ PHASE 3.3 Complete - Governance and decision authority defined

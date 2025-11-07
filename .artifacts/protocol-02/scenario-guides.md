---
status: draft
last_updated: 2025-11-06T05:40:00Z
prepared_by: Discovery Lead
protocol_id: "02"
---

# Scenario Response Guides

## Purpose
This document prepares playbooks for likely pivot scenarios during the discovery call. Each scenario includes trigger phrases, impact assessment, recommended responses, and fallback plans to maintain proposal commitments while accommodating client needs.

---

## SCENARIO 1: Budget Below Estimate

### Trigger Phrases
- "Our budget is closer to $1,500"
- "Can we reduce the scope to fit $X budget?"
- "We need to stay under $2,000"
- "That's higher than we expected"

### Impact Assessment
**Severity:** HIGH - May block project initiation  
**Financial Impact:** 20-40% budget reduction ($2,100-2,700 → $1,500-2,000)  
**Timeline Impact:** Scope reduction or extended timeline required  
**Quality Impact:** May need to cut features or reduce testing/documentation  

### Root Cause Analysis
- Client budget not confirmed during proposal phase
- Market rate misalignment with client expectations
- Client underestimated project complexity

### Recommended Response Script

**Option 1: Scope Reduction (Recommended)**
> "I appreciate you sharing that. Let's look at the priorities. If we focus on the OpenAI integration first (Weeks 1-2) as a standalone milestone, we could deliver that for $700-900. Then once that's proven out and delivering value, we could tackle Stripe billing (Weeks 3-4) as a follow-on engagement for another $700-900. That way you're not committing to the full budget upfront, and we can adjust as we go. Does that phased approach work better?"

**Option 2: Extended Timeline**
> "Got it. If we extend the timeline to 2.5-3 months instead of 2 months, I could reduce my weekly hours from 20 to 15 hours, which would bring the total closer to your budget. The tradeoff is we'd deliver each milestone on a slightly longer schedule, but the quality stays high. Would that timing work for you?"

**Option 3: MVP-Only Scope**
> "Understood. Let's define a true MVP scope—OpenAI integration with basic error handling, and Stripe subscription webhooks for the core events (invoice.paid, subscription.updated). We'd skip the advanced error logging, documentation deep-dive, and frontend demo, and deliver that for $1,800. Once that's live and working, we can discuss a follow-on contract for the polish and additional features. Does that make sense?"

### Negotiation Framework

| Budget Range | Recommended Scope | Deliverables | Timeline |
|--------------|-------------------|--------------|----------|
| $1,500-1,800 | MVP Only | OpenAI basic integration + Stripe core webhooks | 6-8 weeks |
| $1,800-2,000 | Phased Milestone 1 | OpenAI integration complete (as per proposal Week 1-2) | 2-3 weeks |
| $2,100-2,700 | Full Scope | All proposal deliverables | 8-10 weeks |

### Fallback Plans

**If client still wants full scope at lower budget:**
- Politely decline and recommend revisiting when budget allows
- Suggest they find another developer (maintain professionalism)
- Offer to provide technical consultation only (hourly basis)

**If client wants scope reduction but unclear priorities:**
- Schedule follow-up call to define MVP features
- Propose priority matrix exercise (must-have, nice-to-have, post-MVP)
- Document revised scope before starting

### Boundaries to Maintain
- **DO NOT** agree to full scope at 50%+ budget cut (unsustainable)
- **DO NOT** compromise on code quality or testing (technical debt risk)
- **DO** maintain professional tone and respect client's constraints
- **DO** position phased approach as client-centric (risk mitigation, value validation)

### Success Indicators
- ✅ Client agrees to phased or reduced scope
- ✅ Revised budget and deliverables documented
- ✅ Payment terms updated in contract

### Escalation Path
If negotiation stalls → Thank client for consideration → End call professionally → Document for future re-engagement

---

## SCENARIO 2: Scope Expansion ("We Also Need...")

### Trigger Phrases
- "Can you also help with [new feature]?"
- "We forgot to mention, we also need [X]"
- "Would it be possible to add [Y] to the scope?"
- "Our frontend developer left, can you help with Next.js too?"

### Impact Assessment
**Severity:** MEDIUM-HIGH - Scope creep risk  
**Financial Impact:** Potentially 20-50% additional work not in budget  
**Timeline Impact:** May delay core deliverables or extend project  
**Quality Impact:** Risk spreading too thin, reducing quality of core features  

### Root Cause Analysis
- Client didn't fully scope requirements during job post phase
- New requirements emerged after proposal acceptance
- Client testing if developer is flexible/accommodating

### Recommended Response Script

**For In-Scope Adjacent Features:**
> "Great to know! [Feature X] sounds related to what we're already building. Let me assess the effort—if it's a small addition (2-3 hours), I can likely fold it into the existing milestone. If it's more substantial, I'd recommend we add it as a separate milestone with its own timeline and budget. I'll document this as a follow-up item after our call so we can scope it properly. Sound good?"

**For Out-of-Scope Major Features:**
> "That's a valuable feature, and I can definitely help with that. However, [Feature Y] is outside the scope of the current proposal, so it would need its own milestone and budget. What I suggest is: let's stay focused on the OpenAI and Stripe integration first, and once that's delivered and working, we can scope [Feature Y] as a follow-on engagement. That way, we don't dilute focus on the core deliverables. Does that make sense?"

**For Frontend (Next.js) Expansion:**
> "I can help with frontend integration, and I mentioned Next.js familiarity in my proposal. The current scope focuses on backend APIs, but if you need frontend work, we could add Weeks 6-7 as a frontend integration milestone (estimated $600-900 depending on scope). Let's get the backend solid first, then layer on frontend. I can design the APIs to be frontend-friendly from the start so it's smooth when we get there. Does that work?"

### Decision Framework: Add or Defer?

| New Requirement Type | < 5 Hours | 5-15 Hours | > 15 Hours |
|---------------------|-----------|------------|------------|
| **In-Scope Adjacent** | Fold into existing milestone | Add as sub-milestone | Defer to follow-on |
| **Out-of-Scope** | Document for future | Propose separate milestone | Defer to follow-on |
| **Blocker for MVP** | Negotiate scope swap | Add to budget/timeline | Re-scope original plan |

### Fallback Plans

**If client insists new feature is "must-have" immediately:**
1. **Swap Features:** "If [new feature] is critical, we could swap it with [existing feature]. Which would you prioritize?"
2. **Budget Increase:** "To add [feature] without delaying core deliverables, we'd need to increase the budget by $X and extend timeline by Y weeks. Is that feasible?"
3. **Quality Tradeoff:** "We could add [feature] but reduce testing/documentation. I don't recommend this, but it's an option if you're constrained. What do you think?"

**If client keeps adding "one more thing":**
- Politely interrupt and set boundary: "I'm noting all these great ideas. To keep us on track, let's categorize these into 'MVP' and 'Post-MVP' so we deliver the core value first. Does that work?"
- Use parking lot technique: "Let me capture this in a 'Future Enhancements' list. Once we finish the core deliverables, we can prioritize these for Phase 2."

### Boundaries to Maintain
- **DO NOT** agree to major scope expansions without budget/timeline adjustment
- **DO NOT** let "small additions" accumulate into significant unpaid work
- **DO** position boundaries as protecting quality of core deliverables
- **DO** express enthusiasm for future opportunities while staying focused

### Success Indicators
- ✅ New features documented in "Future Enhancements" list
- ✅ Client agrees to focus on MVP first
- ✅ Budget/timeline updated if scope expanded
- ✅ Clear prioritization matrix created

### Escalation Path
If scope creep becomes excessive → Document all requests → Schedule separate scoping call → Propose revised SOW before proceeding

---

## SCENARIO 3: Compliance Requirements Emerge (HIPAA/GDPR)

### Trigger Phrases
- "We're handling patient health records"
- "This needs to be HIPAA compliant"
- "We're operating in Europe, so GDPR applies"
- "Do we need a BAA for this work?"

### Impact Assessment
**Severity:** HIGH - Major architectural implications  
**Financial Impact:** +30-50% budget increase for compliance features  
**Timeline Impact:** +2-4 weeks for security audit and compliance review  
**Technical Impact:** May require encryption, audit logging, data residency controls  
**Legal Impact:** May require Business Associate Agreement (BAA) or DPA  

### Root Cause Analysis
- Compliance requirements not disclosed in job post
- Client assumed developer would know health-tech = HIPAA
- Client underestimated compliance complexity

### Recommended Response Script

**Immediate Clarification:**
> "That's really important context—thanks for sharing. Let me ask a few clarifying questions to understand the compliance requirements. First, will the OpenAI or Stripe integration be processing protected health information (PHI)? Second, are we storing any PHI in the database, or just metadata? And third, do you have existing HIPAA compliance infrastructure (encryption, audit logs, BAA with hosting provider)?"

**If PHI is Involved:**
> "Okay, so HIPAA compliance significantly changes the architecture and timeline. Here's what we'd need to add:
> 1. Encryption at rest and in transit for all PHI
> 2. Audit logging for all data access
> 3. Business Associate Agreement (BAA) between us
> 4. Potentially BAA with OpenAI (they offer this, but it's enterprise tier)
> 5. Security review and penetration testing
> 
> This adds approximately 2-3 weeks and $800-1,200 to the project. I can absolutely handle this, but we'll need to adjust scope and budget. Would you like me to prepare a compliance-focused proposal addendum?"

**If No PHI Involved:**
> "Got it. If we're not processing PHI directly—for example, if the AI features only use anonymized or non-sensitive data—then standard security practices (HTTPS, API key management, input validation) should suffice. Let's document exactly what data flows through the OpenAI integration so we're crystal clear on compliance boundaries. Does that work?"

### Compliance Scope Decision Tree

```
Is PHI/PII involved?
├─ YES → Is it processed/stored?
│   ├─ PROCESSED → HIPAA compliance required (+2-4 weeks, +30-50% budget)
│   └─ STORED → HIPAA + encryption + audit logs (+3-5 weeks, +50-70% budget)
└─ NO → Standard security practices (included in original scope)
```

### Required Compliance Additions

| Compliance Level | Additions Required | Timeline Impact | Budget Impact |
|------------------|-------------------|-----------------|---------------|
| **Standard Security** | HTTPS, API keys, input validation | None | Included |
| **GDPR (PII only)** | Data retention policies, consent management | +1 week | +$300-500 |
| **HIPAA (PHI)** | Encryption, audit logging, BAA, security review | +2-4 weeks | +$800-1,200 |
| **HIPAA + Enterprise** | Above + penetration testing, OpenAI enterprise BAA | +4-6 weeks | +$1,500-2,500 |

### Fallback Plans

**If client can't increase budget for compliance:**
1. **Architectural Redesign:** "We could design the system so PHI never touches OpenAI—for example, using anonymized summaries instead of raw patient data. That keeps us out of HIPAA scope. Would that work?"
2. **Phased Approach:** "Let's complete the core integration first with test/anonymized data, then add the compliance layer as Phase 2. That spreads the cost over two engagements."
3. **Defer Feature:** "If HIPAA compliance isn't ready, we could focus on non-PHI features first (e.g., Stripe billing) and add OpenAI later when compliance is sorted."

**If client is surprised by compliance complexity:**
- Educate on risks: "HIPAA violations can result in $100-50,000 fines per violation. It's worth investing in compliance upfront."
- Recommend compliance specialist: "I can handle standard security, but for full HIPAA certification, you might want a dedicated compliance consultant. I can coordinate with them."
- Document explicitly: "Let's document that compliance is out of scope for this engagement, and you're responsible for any compliance requirements. I'll build to security best practices, but not HIPAA-certified."

### Boundaries to Maintain
- **DO NOT** claim HIPAA expertise if you're not a compliance specialist
- **DO NOT** sign BAA without legal review and insurance coverage
- **DO** be transparent about compliance limitations
- **DO** recommend professional compliance audit if PHI is involved

### Success Indicators
- ✅ Clear documentation of what data is PHI vs. non-PHI
- ✅ Compliance scope explicitly defined in revised SOW
- ✅ BAA signed if PHI is involved
- ✅ Budget and timeline updated for compliance work

### Escalation Path
If compliance requirements are complex → Recommend compliance specialist → Propose collaboration model → Or decline engagement professionally

---

## SCENARIO 4: Existing Codebase Has Major Tech Debt

### Trigger Phrases
*(Discovered during codebase review, not during discovery call, but prepare for it)*
- "The code is a bit messy, but it works"
- "Our previous developer didn't document anything"
- "We haven't touched the backend in 6 months"
- "There might be some bugs, but we haven't had time to fix them"

### Impact Assessment
**Severity:** MEDIUM-HIGH - May block integration work  
**Technical Impact:** Difficult to integrate without refactoring  
**Timeline Impact:** +1-3 weeks for codebase cleanup  
**Quality Impact:** Risk building on unstable foundation  

### Root Cause Analysis
- Previous developer left without handoff
- No code review or quality standards enforced
- Client prioritized speed over maintainability

### Recommended Response Script

**During Codebase Review (Week 1 Day 1):**
> "I've reviewed the codebase and I want to give you a transparent assessment. There are a few areas that will make integration challenging—[list specific issues: no tests, missing error handling, unclear data models, etc.]. Here are three options:
> 
> **Option 1 (Recommended):** Spend 3-5 days refactoring the critical areas first, then proceed with integration. This adds 1 week to the timeline but ensures we're building on a solid foundation.
> 
> **Option 2:** Build the integration in isolation (separate module) to avoid touching existing code, then integrate carefully. This is faster (no timeline change) but may create architectural debt long-term.
> 
> **Option 3:** Proceed as-is and work around tech debt. Fastest approach, but higher risk of bugs and harder maintenance later.
> 
> Which approach makes most sense for your priorities?"

### Decision Framework: Refactor or Work Around?

| Tech Debt Severity | Impact on Integration | Recommended Action | Timeline Impact |
|--------------------|----------------------|-------------------|-----------------|
| **Minor** (e.g., poor variable naming) | Low | Work around, document issues | None |
| **Moderate** (e.g., no tests, minimal docs) | Medium | Selective refactoring of integration points | +3-5 days |
| **Severe** (e.g., broken error handling, security gaps) | High | Refactor before integration | +1-2 weeks |
| **Critical** (e.g., data corruption risk, security vulnerabilities) | Blocker | Full refactor or decline engagement | +2-4 weeks |

### Fallback Plans

**If client resists refactoring:**
1. **Document Risks:** "I'll document the technical debt in a report so you're aware of the risks. If issues arise during integration, we'll need to address them, which could delay milestones."
2. **Isolate Integration:** "I'll build the integration as a separate service/module to minimize interaction with existing code. This is less optimal architecturally, but it reduces risk."
3. **Set Expectations:** "Just so you know, if the existing codebase causes integration issues, we may need to adjust the timeline. I'll keep you updated if I hit blockers."

**If tech debt is too severe:**
- Recommend dedicated refactoring phase before integration
- Propose revised SOW: "Phase 0: Codebase Remediation (2 weeks), then Phase 1: Integration (original timeline)"
- Or respectfully decline: "I don't think I can deliver quality results on this foundation. I'd recommend a codebase audit and refactor first, then we can revisit integration."

### Boundaries to Maintain
- **DO NOT** commit to unrealistic timelines given tech debt
- **DO NOT** build on code that puts integration at risk
- **DO** be honest about quality risks
- **DO** provide client with informed options and tradeoffs

### Success Indicators
- ✅ Tech debt assessment shared with client within 48 hours of repo access
- ✅ Client approves refactoring plan or accepts workaround risks
- ✅ Timeline adjusted if refactoring required

### Escalation Path
If tech debt is severe and client refuses refactoring → Document risks formally → Request sign-off on "as-is" approach → Or withdraw from engagement

---

## SCENARIO 5: Timezone Coordination Challenges

### Trigger Phrases
- "I'm usually available after 8pm PST"
- "Can we do standups at 6am your time?"
- "I might not respond for 12 hours due to timezone"
- "Let's mostly work async"

### Impact Assessment
**Severity:** LOW-MEDIUM - May slow collaboration  
**Communication Impact:** Reduced sync opportunities, slower feedback loops  
**Timeline Impact:** +5-10% project duration due to delays  
**Process Impact:** Need async-first workflow  

### Root Cause Analysis
- Limited timezone overlap (Pakistan GMT+5 vs PST GMT-8 = 13-hour difference)
- Client's availability constraints
- Async communication not explicitly defined

### Recommended Response Script

**During Discovery Call:**
> "I appreciate that timezone coordination can be tricky. Let's define a workflow that works for both of us. Here's what I propose:
> 
> **Core Hours:** Let's identify 2-3 hours of overlap per week for sync calls (e.g., Tuesday and Thursday mornings my time, evening your time). We can use those for blockers and weekly check-ins.
> 
> **Async Updates:** I'll post daily progress updates in Discord with PR links and any questions. If you can review PRs within 24 hours, that keeps momentum.
> 
> **Escalation Path:** For urgent blockers, I'll ping you directly in Discord. If you don't respond within 4 hours, I'll document my assumptions and proceed, then confirm with you later.
> 
> Does that workflow sound good?"

### Async-First Communication Framework

| Communication Type | Sync or Async | Frequency | Format | Response SLA |
|-------------------|---------------|-----------|--------|--------------|
| **Daily Updates** | Async | Daily (Mon-Fri) | Discord message + PR links | No response needed (FYI only) |
| **Code Review** | Async | Per PR | GitHub PR comments | 24 hours |
| **Blockers** | Sync (if urgent) or Async | As needed | Discord ping + description | 4 hours (urgent), 24 hours (non-urgent) |
| **Weekly Check-In** | Sync | Weekly | Video/voice call | Scheduled in advance |
| **Milestone Demo** | Sync | Per milestone | Recorded video or live demo | Scheduled in advance |

### Fallback Plans

**If client is mostly unavailable:**
1. **Recorded Updates:** "I'll send 5-minute Loom videos showing progress. You can review when convenient and reply with feedback."
2. **Assumption-Driven Development:** "If I don't hear back on a question within 24 hours, I'll document my best judgment and proceed. We can course-correct in the next check-in."
3. **Batch Communication:** "Let's batch all questions into weekly check-in calls instead of ad-hoc messages."

**If timezone coordination fails:**
- Over-communicate in PRs (detailed descriptions, context, tradeoffs)
- Use GitHub Issues for tracking decisions and questions
- Schedule calls 1 week in advance to ensure availability

### Boundaries to Maintain
- **DO NOT** expect real-time responses across 13-hour timezone gap
- **DO NOT** let timezone delays block critical work (document assumptions and proceed)
- **DO** establish clear response SLAs upfront
- **DO** use async tools effectively (GitHub, Discord, Loom)

### Success Indicators
- ✅ Core hours identified and scheduled
- ✅ Async communication norms documented in communication-plan.md
- ✅ No 24+ hour blockers due to timezone delays

### Escalation Path
If timezone coordination causes frequent delays → Propose fully async workflow → Or discuss extended timeline to accommodate delays

---

## Scenario Summary Dashboard

| Scenario | Severity | Probability | Impact Area | Prepared Response | Follow-Up Action |
|----------|----------|-------------|-------------|-------------------|------------------|
| Budget Below Estimate | HIGH | Medium (30%) | Financial | Phased/reduced scope options | Document revised SOW |
| Scope Expansion | MEDIUM-HIGH | High (60%) | Timeline/Budget | MVP prioritization, defer to Phase 2 | Future enhancements list |
| Compliance Emerges | HIGH | Low (20%) | Architecture/Budget | Clarify PHI scope, propose addendum | Compliance impact assessment |
| Tech Debt Discovered | MEDIUM-HIGH | Medium (40%) | Timeline/Quality | Refactor or isolate integration | Tech debt report |
| Timezone Challenges | LOW-MEDIUM | High (60%) | Communication | Async-first workflow | Communication plan |

## Pre-Discovery Call Preparation

1. **Review all scenarios** to internalize response scripts
2. **Practice pivot responses** to maintain professionalism under pressure
3. **Prepare negotiation ranges** (budget flexibility, scope reduction options)
4. **Document boundaries** you won't cross (quality standards, fair pricing)
5. **Rehearse de-escalation techniques** if client becomes defensive

## Post-Discovery Call Actions

1. **Document any pivots** that occurred during call
2. **Update proposal/SOW** if scope or budget changed
3. **Flag risks** that emerged but weren't fully resolved
4. **Share scenarios** with any team members involved
5. **Reflect on effectiveness** of scenario responses for future improvement


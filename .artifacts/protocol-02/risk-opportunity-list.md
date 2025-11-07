---
status: draft
last_updated: 2025-11-06T05:40:00Z
prepared_by: Discovery Lead
protocol_id: "02"
---

# Risk & Opportunity Radar

## Critical Risks (Blockers)

### RISK-001: Missing API Access Credentials
**Category:** Technical - Infrastructure
**Severity:** BLOCKER
**Impact:** Cannot start development without OpenAI API keys and Stripe account access
**Probability:** Medium (30%)
**Root Cause:** No credentials mentioned in job post or proposal communications
**Indicators:**
- Client has not provided API keys or account access details
- No mention of credential sharing process in job post

**Mitigation Strategy:**
1. **Pre-Discovery:** Flag in discovery brief as P0 requirement
2. **During Call:** Ask Q-TECH-002 (API key ownership and access)
3. **Post-Call:** Document credential handoff process and timeline
4. **Fallback:** Request test credentials for immediate setup if production delayed

**Contingency Plan:**
- Use personal test accounts temporarily (with client approval)
- Delay Week 1 start by 2-3 days if credential handoff requires setup

**Mitigation Owner:** Discovery Lead → Development Lead
**Timeline Impact:** +2-3 days if not resolved before Week 1

---

### RISK-002: Unclear OpenAI Integration Scope
**Category:** Technical - Requirements
**Severity:** HIGH
**Impact:** May build wrong endpoints, causing rework and timeline delays
**Probability:** High (60%)
**Root Cause:** Proposal mentions "chat completions or embeddings" without specificity
**Indicators:**
- Job post says "integrating OpenAI APIs" (plural, vague)
- No specific use case documented in client communications

**Mitigation Strategy:**
1. **During Call:** Ask Q-BUS-001 (specific AI features and use cases)
2. **During Call:** Request example workflows or user stories
3. **Post-Call:** Document exact OpenAI endpoints required with acceptance criteria
4. **Validation:** Share technical design doc before Week 1 coding starts

**Contingency Plan:**
- Start with most common pattern (chat completions) if still unclear
- Build modular architecture allowing easy endpoint addition
- Schedule Week 1.5 checkpoint to validate approach before Week 2

**Mitigation Owner:** Discovery Lead → Development Lead
**Timeline Impact:** -5-7 days if wrong endpoints built initially

---

### RISK-003: Budget Mismatch
**Category:** Business - Financial
**Severity:** BLOCKER
**Impact:** Project may not start if budget expectations don't align
**Probability:** Low (20%)
**Root Cause:** Proposal estimates $2,100-2,700 but client budget not confirmed
**Indicators:**
- Job post says "part-time" but no explicit budget range
- Proposal pricing not yet acknowledged by client

**Mitigation Strategy:**
1. **During Call:** Ask Q-BUS-001 (budget approval and payment terms)
2. **During Call:** Discuss milestone payment structure
3. **Post-Call:** Formalize contract with clear payment terms
4. **Escalation:** If budget mismatch, negotiate scope reduction or extended timeline

**Contingency Plan:**
- Prepare "MVP-only" scope (OpenAI + basic Stripe) for lower budget
- Offer phased approach: MVP first, then extend based on results
- Reduce hours/week from 20 to 15 if budget constraints exist

**Mitigation Owner:** Discovery Lead → Project Manager
**Timeline Impact:** Project may not proceed if unresolved

---

### RISK-004: Undefined Acceptance Criteria
**Category:** Process - Quality Assurance
**Severity:** HIGH
**Impact:** Risk of endless revisions due to misaligned expectations
**Probability:** Medium (50%)
**Root Cause:** Proposal describes features but no explicit "done" definition
**Indicators:**
- No acceptance criteria in job post
- Proposal uses qualitative terms ("proper error handling", "basic tests")

**Mitigation Strategy:**
1. **During Call:** Ask Q-OPS-003 (acceptance criteria per milestone)
2. **Post-Call:** Document specific acceptance criteria in discovery form
3. **Week 1:** Share test plan and validation approach for approval
4. **Ongoing:** Weekly demo to validate incremental progress

**Contingency Plan:**
- Use industry standards (pytest coverage >80%, error handling for all API calls)
- Document assumptions in milestone deliverables
- Request explicit sign-off at each milestone gate

**Mitigation Owner:** Development Lead → QA Lead
**Timeline Impact:** +10-15% timeline if acceptance criteria change mid-project

---

## High Risks

### RISK-005: Timezone Coordination Challenges
**Category:** Operational - Communication
**Severity:** MEDIUM
**Impact:** Delayed responses may slow down daily collaboration
**Probability:** Medium (40%)
**Root Cause:** Pakistan Standard Time (GMT+5) with PST overlap requires specific hours
**Indicators:**
- Proposal mentions "flexible with PST overlap" but no specific hours agreed
- Daily updates expected (job-post.md:5) require predictable overlap

**Mitigation Strategy:**
1. **During Call:** Confirm specific overlap hours for sync communication
2. **Post-Call:** Document asynchronous communication expectations
3. **Ongoing:** Use GitHub PRs for code review (async-friendly)
4. **Tool Setup:** Use Discord threads for async updates + scheduled sync calls

**Contingency Plan:**
- Establish "core hours" for overlap (e.g., 2-hour window daily)
- Use recorded video updates if sync calls missed
- Over-communicate in PRs to reduce back-and-forth need

**Mitigation Owner:** Discovery Lead → Development Lead
**Timeline Impact:** +5-10% timeline if coordination delays accumulate

---

### RISK-006: Codebase Complexity Unknown
**Category:** Technical - Architecture
**Severity:** MEDIUM
**Impact:** Timeline estimates may be inaccurate if codebase is more complex than expected
**Probability:** Medium (40%)
**Root Cause:** No access to existing codebase during proposal phase
**Indicators:**
- Job post mentions "debugging" and "data validation" (implies existing code)
- Proposal timeline assumes greenfield integration approach

**Mitigation Strategy:**
1. **Pre-Week 1:** Request repository access immediately after discovery
2. **Week 1 Day 1:** Conduct codebase assessment (architecture review, tech debt scan)
3. **Week 1 Day 3:** Report findings and adjust timeline if needed
4. **Escalation:** If major tech debt found, negotiate scope or timeline adjustment

**Contingency Plan:**
- Allocate 20% buffer in Week 1-2 for codebase familiarization
- Document technical debt and propose refactoring priorities
- Negotiate extended timeline if major architectural changes needed

**Mitigation Owner:** Development Lead
**Timeline Impact:** +15-20% timeline if significant refactoring needed

---

### RISK-007: Health-Tech Compliance Requirements
**Category:** Business - Regulatory
**Severity:** MEDIUM (could escalate to HIGH)
**Impact:** May require additional security/compliance work not in original scope
**Probability:** Low (30%)
**Root Cause:** Job post mentions "health-tech products" but no compliance details
**Indicators:**
- If handling PHI/PII, HIPAA or GDPR compliance may apply
- No compliance requirements mentioned in job post

**Mitigation Strategy:**
1. **During Call:** Ask Q-BUS-003 (health data involved? compliance requirements?)
2. **During Call:** Clarify data handling and storage requirements
3. **Post-Call:** Document compliance scope and adjust timeline/budget if needed
4. **Escalation:** If HIPAA required, engage compliance specialist or adjust scope

**Contingency Plan:**
- If compliance required, add 2-week security audit phase
- Implement industry-standard security patterns (encryption, audit logging)
- Propose phased approach: MVP without sensitive data, then compliance layer

**Mitigation Owner:** Discovery Lead → Security Lead
**Timeline Impact:** +2-4 weeks if HIPAA/GDPR compliance required

---

## Medium Risks

### RISK-008: Stripe Webhook Testing Limitations
**Category:** Technical - Testing
**Severity:** MEDIUM
**Impact:** May encounter webhook validation issues in production that weren't caught in testing
**Probability:** Low (25%)
**Root Cause:** Stripe CLI testing may not catch all edge cases
**Indicators:**
- Proposal mentions Stripe CLI testing (PROPOSAL.md:23)
- No mention of production webhook testing strategy

**Mitigation Strategy:**
1. **Week 3:** Implement comprehensive webhook signature validation
2. **Week 4:** Test with Stripe test events (all subscription lifecycle events)
3. **Week 4:** Document webhook retry logic and idempotency handling
4. **Pre-Production:** Request client approval for test webhook in production

**Contingency Plan:**
- Implement robust error logging for webhook failures
- Add monitoring for webhook processing delays
- Prepare rollback plan if webhook issues arise in production

**Mitigation Owner:** Development Lead
**Timeline Impact:** +2-3 days if webhook issues discovered late

---

### RISK-009: PostgreSQL Schema Mismatch
**Category:** Technical - Data
**Severity:** MEDIUM
**Impact:** Integration work may require schema changes, causing delays
**Probability:** Medium (35%)
**Root Cause:** No schema visibility during proposal phase
**Indicators:**
- Proposal assumes PostgreSQL exists (PROPOSAL.md:23)
- No ERD or schema documentation shared yet

**Mitigation Strategy:**
1. **Pre-Week 1:** Request current PostgreSQL schema/ERD
2. **Week 1:** Review schema for Stripe/OpenAI integration compatibility
3. **Week 1:** Propose schema migrations if needed (with approval gate)
4. **Escalation:** If major schema redesign needed, negotiate timeline extension

**Contingency Plan:**
- Design integration layer to minimize direct schema dependencies
- Use database views or abstraction layer if schema changes restricted
- Document schema assumptions and validate early

**Mitigation Owner:** Development Lead
**Timeline Impact:** +3-5 days if schema migrations required

---

## Opportunities

### OPPORTUNITY-001: Long-Term Contract Extension
**Category:** Business - Growth
**Value:** High (potential recurring revenue)
**Probability:** High (60%)
**Source:** job-post.md:22 ("Potential for long-term contract")
**Enablers:**
- Client explicitly mentions extension possibility
- Health-tech product likely needs ongoing AI/billing support
- Proposal demonstrates structured approach that builds trust

**Capture Strategy:**
1. **During Discovery:** Ask about roadmap and future feature plans
2. **Week 5+:** Propose maintenance + feature development retainer
3. **Post-Project:** Share retrospective and improvement roadmap
4. **Relationship Building:** Over-deliver on documentation and knowledge transfer

**Success Indicators:**
- Client shares 3-6 month product roadmap during discovery
- Client requests additional features during Week 5+
- Client asks about ongoing availability before project end

---

### OPPORTUNITY-002: Expand Scope to Next.js Integration
**Category:** Technical - Scope Expansion
**Value:** Medium (additional milestone revenue)
**Probability:** Medium (45%)
**Source:** job-post.md:15 ("Nice to Have: Experience with Next.js")
**Enablers:**
- Client has Next.js frontend (implied)
- API integration naturally extends to frontend features
- Proposal positions developer as full-stack capable

**Capture Strategy:**
1. **During Discovery:** Ask about frontend integration timeline
2. **Week 2-3:** Share API documentation formatted for frontend consumption
3. **Week 4:** Offer to demo frontend integration proof-of-concept
4. **Proposal:** Present Week 6-7 frontend integration milestone

**Success Indicators:**
- Client mentions frontend developer challenges during discovery
- Client asks about API contracts during Week 2-3
- Client expresses interest in frontend demo

---

### OPPORTUNITY-003: Implement Advanced AI Features
**Category:** Technical - Feature Enhancement
**Value:** High (differentiator for client's product)
**Probability:** Medium (40%)
**Source:** Client's AI/health-tech focus (job-post.md:11)
**Enablers:**
- OpenAI offers multiple advanced capabilities (embeddings, fine-tuning, assistants)
- Health-tech use cases benefit from personalized AI
- Proposal demonstrates AI integration expertise

**Capture Strategy:**
1. **During Discovery:** Ask about AI feature roadmap and user needs
2. **Week 2:** Share advanced OpenAI capability options (embeddings for search, etc.)
3. **Week 4:** Propose pilot for advanced feature (e.g., semantic search)
4. **Post-MVP:** Present ROI analysis for advanced AI features

**Success Indicators:**
- Client shares AI feature wishlist during discovery
- Client asks about embeddings or fine-tuning during Week 1-2
- Product roadmap includes AI-powered search or recommendations

---

### OPPORTUNITY-004: Establish Monitoring & Observability Practice
**Category:** Operational - Infrastructure
**Value:** Medium (productionization enabler)
**Probability:** Medium (35%)
**Source:** Proposal emphasis on "error handling" and "log analysis" (job-post.md:4, PROPOSAL.md:17, 26)
**Enablers:**
- Client needs debugging support (job-post.md:4)
- Structured logging naturally extends to monitoring
- Proposal demonstrates production-readiness mindset

**Capture Strategy:**
1. **Week 1:** Implement structured logging with log levels
2. **Week 3:** Propose monitoring dashboard for API/webhook health
3. **Week 5:** Share observability best practices document
4. **Post-Project:** Offer monitoring setup as post-MVP service

**Success Indicators:**
- Client asks about production error tracking during discovery
- Client expresses concern about API rate limits or failures
- Client requests alerting or dashboard during Week 3+

---

## Risk Summary Dashboard

| Category | Blocker | High | Medium | Low | Total |
|----------|---------|------|--------|-----|-------|
| Technical | 1 | 1 | 3 | 0 | 5 |
| Business | 1 | 0 | 1 | 0 | 2 |
| Operational | 0 | 1 | 0 | 0 | 1 |
| Process | 0 | 1 | 0 | 0 | 1 |
| **TOTAL** | **2** | **3** | **4** | **0** | **9** |

## Opportunity Summary Dashboard

| Category | High Value | Medium Value | Total |
|----------|------------|--------------|-------|
| Business | 1 | 0 | 1 |
| Technical | 1 | 2 | 3 |
| Operational | 0 | 1 | 1 |
| **TOTAL** | **2** | **3** | **5** |

## Critical Actions Before Discovery Call
1. **Blockers:** Prepare questions to resolve RISK-001 (credentials) and RISK-003 (budget)
2. **High Risks:** Prioritize Q-BUS-001 (OpenAI scope) and Q-OPS-003 (acceptance criteria)
3. **Opportunities:** Ask about long-term roadmap and AI feature vision
4. **Mitigation:** Prepare contingency plans for each blocker risk


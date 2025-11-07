---
status: template_awaiting_call
last_updated: 2025-11-06T05:40:00Z
prepared_by: Discovery Lead
protocol_id: "02"
post_call_update_required: true
---

# Client Discovery Form

**Note:** This is a template to be populated after the discovery call. All `[TO BE FILLED]` sections will be completed based on `discovery-call-notes.md`.

---

## Project Overview

### Project Name
[TO BE FILLED - e.g., "FastAPI + OpenAI/Stripe Integration"]

### Client Information
- **Organization:** [TO BE FILLED]
- **Primary Contact:** [TO BE FILLED - Name, Role, Email]
- **Additional Stakeholders:** [TO BE FILLED - List names and roles]
- **Industry:** [TO BE FILLED - e.g., "Health-Tech"]

### Project Summary
[TO BE FILLED - 2-3 sentence summary of project scope from discovery call]

---

## Business Goals & Success Metrics

### Primary Business Objectives
[TO BE FILLED - List 3-5 primary objectives confirmed during call]

1. [Objective 1 - e.g., "Enable AI-powered chat interactions for users"]
2. [Objective 2 - e.g., "Implement subscription billing with Stripe"]
3. [Objective 3 - e.g., "Support ongoing debugging and maintenance"]
4. [Additional objectives...]

### Success Metrics
[TO BE FILLED - How will client measure project success?]

**Technical Metrics:**
- [e.g., "OpenAI API integration with <200ms response time"]
- [e.g., "Stripe webhooks processing 100% of subscription events"]
- [e.g., "Test coverage >80%"]

**Business Metrics:**
- [e.g., "Subscription churn rate <5%"]
- [e.g., "AI feature adoption rate >60%"]
- [e.g., "Zero payment processing failures"]

### Target Users
[TO BE FILLED - Who will use the features being built?]

---

## Functional Requirements (MVP Scope)

### Feature 1: OpenAI Integration
**Priority:** [P0 / P1 / P2]  
**Owner:** [Developer / Client / Team Member]  
**Milestone:** [Week 1-2 / Week 3-4 / Post-MVP]

**Description:**
[TO BE FILLED - Detailed description of OpenAI integration requirements from call]

**Acceptance Criteria:**
- [ ] [Criterion 1 - e.g., "Chat completions endpoint integrated and tested"]
- [ ] [Criterion 2 - e.g., "Error handling for rate limits and timeouts"]
- [ ] [Criterion 3 - e.g., "API responses logged for debugging"]
- [ ] [Criterion 4 - e.g., "Documentation complete with examples"]

**Open Items:**
- [TO BE FILLED - Any unresolved questions or follow-ups]

---

### Feature 2: Stripe Billing & Webhooks
**Priority:** [P0 / P1 / P2]  
**Owner:** [Developer / Client / Team Member]  
**Milestone:** [Week 3-4 / Post-MVP]

**Description:**
[TO BE FILLED - Detailed description of Stripe integration requirements from call]

**Acceptance Criteria:**
- [ ] [Criterion 1 - e.g., "Subscription creation and management endpoints"]
- [ ] [Criterion 2 - e.g., "Webhook handlers for invoice.paid, subscription.updated, etc."]
- [ ] [Criterion 3 - e.g., "Stripe CLI testing complete"]
- [ ] [Criterion 4 - e.g., "PostgreSQL schema updated for subscriptions"]

**Open Items:**
- [TO BE FILLED - Any unresolved questions or follow-ups]

---

### Feature 3: Debugging & Maintenance Support
**Priority:** [P0 / P1 / P2]  
**Owner:** [Developer]  
**Milestone:** [Week 5+ / Ongoing]

**Description:**
[TO BE FILLED - Detailed description of debugging and support scope from call]

**Acceptance Criteria:**
- [ ] [Criterion 1 - e.g., "Error logs structured and accessible"]
- [ ] [Criterion 2 - e.g., "Query optimization documented"]
- [ ] [Criterion 3 - e.g., "Knowledge transfer documentation complete"]

**Open Items:**
- [TO BE FILLED - Any unresolved questions or follow-ups]

---

### Additional Features (Post-MVP or Future)
[TO BE FILLED - List features discussed but deferred to post-MVP]

1. **[Feature Name]**
   - Priority: [P2 / Future]
   - Description: [Brief description]
   - Timeline: [Post-MVP / Q2 2025 / TBD]

2. **[Feature Name]**
   - Priority: [P2 / Future]
   - Description: [Brief description]
   - Timeline: [Post-MVP / Q2 2025 / TBD]

---

## Non-Functional Requirements

### Performance Requirements
[TO BE FILLED - Performance expectations discussed during call]
- API Response Time: [e.g., "<200ms for chat completions"]
- Concurrent Users: [e.g., "Support 100 concurrent API calls"]
- Uptime: [e.g., "99.9% uptime target"]

### Security Requirements
[TO BE FILLED - Security standards confirmed during call]
- Authentication: [e.g., "API key authentication via Bearer tokens"]
- Encryption: [e.g., "HTTPS for all API communications"]
- Data Protection: [e.g., "No PHI/PII stored in logs"]

### Compliance Requirements
[TO BE FILLED - Compliance needs identified during call]
- Regulatory: [e.g., "HIPAA compliant" / "GDPR compliant" / "None"]
- Audit Requirements: [e.g., "Audit logs for all API requests"]
- Data Retention: [e.g., "Retain logs for 90 days"]

### Scalability Requirements
[TO BE FILLED - Scalability expectations from call]
- User Growth: [e.g., "Support 10x user growth in 6 months"]
- Database: [e.g., "Handle 1M+ records"]
- API Volume: [e.g., "Scale to 10K requests/day"]

---

## Budget & Timeline

### Budget Approval
**Status:** [Approved / Pending / Needs Revision]  
**Approved Amount:** $[TO BE FILLED]  
**Payment Structure:** [Milestone-based / Weekly / Hourly]

**Milestones & Payments:**
1. **Milestone 1:** [Name] - $[Amount] ([Percentage]%) - Due: [Date]
2. **Milestone 2:** [Name] - $[Amount] ([Percentage]%) - Due: [Date]
3. **Milestone 3:** [Name] - $[Amount] ([Percentage]%) - Due: [Date]

### Timeline Confirmation
**Project Start Date:** [TO BE FILLED - YYYY-MM-DD]  
**Project End Date (Initial Scope):** [TO BE FILLED - YYYY-MM-DD]  
**Total Duration:** [TO BE FILLED - X weeks/months]

**Key Milestones:**
- [TO BE FILLED - e.g., "Week 1-2: OpenAI Integration Complete"]
- [TO BE FILLED - e.g., "Week 3-4: Stripe Integration Complete"]
- [TO BE FILLED - e.g., "Week 5+: Debugging & Handoff"]

**Dependencies & Blockers:**
- [TO BE FILLED - e.g., "Week 1 blocked until GitHub repo access granted"]
- [TO BE FILLED - e.g., "Week 3 blocked until Stripe credentials provided"]

---

## Access Requirements & Credentials

### Repository Access
- **GitHub Repository URL:** [TO BE FILLED]
- **Access Status:** [Granted / Pending / Blocked]
- **Access Due Date:** [TO BE FILLED - YYYY-MM-DD]
- **Permissions Required:** [Write / Maintainer / Admin]

### Communication Channels
- **Discord Server:** [TO BE FILLED - Server name or invite link]
- **Discord Channels:** [TO BE FILLED - e.g., "#dev-updates", "#blockers"]
- **Access Status:** [Granted / Pending]
- **Access Due Date:** [TO BE FILLED - YYYY-MM-DD]

### API Credentials
- **OpenAI API Key:** [Status: Granted / Pending / Not Provided]
- **OpenAI Plan Tier:** [TO BE FILLED - e.g., "Pay-as-you-go", "Enterprise"]
- **OpenAI Key Due Date:** [TO BE FILLED - YYYY-MM-DD]

- **Stripe Account Access:** [Status: Granted / Pending / Not Provided]
- **Stripe Mode:** [Test / Production / Both]
- **Stripe Key Due Date:** [TO BE FILLED - YYYY-MM-DD]

### Database Access
- **PostgreSQL Connection String:** [Status: Granted / Pending / Not Provided]
- **Database Environment:** [Local / Staging / Production]
- **Database Access Due Date:** [TO BE FILLED - YYYY-MM-DD]

### Other Credentials
- [TO BE FILLED - List any additional services requiring credentials]

---

## Technical Stack Confirmation

### Backend
- **Framework:** [TO BE FILLED - e.g., "FastAPI 0.104.0"]
- **Language:** [TO BE FILLED - e.g., "Python 3.11"]
- **Database:** [TO BE FILLED - e.g., "PostgreSQL 15"]
- **ORM:** [TO BE FILLED - e.g., "SQLAlchemy 2.0"]

### Frontend (if applicable)
- **Framework:** [TO BE FILLED - e.g., "Next.js 14" / "N/A"]
- **Integration Scope:** [In Scope / Out of Scope / Post-MVP]

### Third-Party Services
- **OpenAI:** [Endpoints: TO BE FILLED]
- **Stripe:** [Subscription model: TO BE FILLED]
- **Email Service:** [TO BE FILLED - e.g., "SendGrid" / "None"]
- **SMS Service:** [TO BE FILLED - e.g., "Twilio" / "None"]
- **Monitoring:** [TO BE FILLED - e.g., "Sentry" / "None"]
- **Analytics:** [TO BE FILLED - e.g., "Mixpanel" / "None"]

---

## Assumptions & Constraints

### Confirmed Assumptions
[TO BE FILLED - List assumptions validated during discovery call from assumptions-gaps.md]

1. [Assumption - e.g., "OpenAI chat completions are the primary AI feature"]
2. [Assumption - e.g., "Stripe subscription model is monthly recurring"]
3. [Assumption - e.g., "No HIPAA compliance required for MVP"]

### Unresolved Assumptions (Require Follow-Up)
[TO BE FILLED - List assumptions still pending validation]

1. [Assumption - Owner: [Name], Due: [Date]]
2. [Assumption - Owner: [Name], Due: [Date]]

### Known Constraints
[TO BE FILLED - Constraints identified during discovery call]

**Technical Constraints:**
- [e.g., "Existing PostgreSQL schema cannot be modified without migration approval"]
- [e.g., "OpenAI API rate limit: 60 requests/minute"]

**Timeline Constraints:**
- [e.g., "Must launch MVP by [Date] for marketing campaign"]
- [e.g., "Developer availability: 20 hours/week minimum"]

**Budget Constraints:**
- [e.g., "Total budget cannot exceed $X"]
- [e.g., "Payment terms: Net 30 on invoice approval"]

**Resource Constraints:**
- [e.g., "Solo developer (no team support)"]
- [e.g., "Client availability for code review: 24-hour turnaround"]

---

## Open Items & Follow-Ups

### Critical (Blocking Development)
[TO BE FILLED - P0 items that must be resolved before Week 1 start]

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| [e.g., "GitHub repository access"] | Client | [Date] | pending |
| [e.g., "OpenAI API key"] | Client | [Date] | pending |
| [e.g., "Discord server invite"] | Client | [Date] | pending |

### High Priority (Needed for Milestone 1-2)
[TO BE FILLED - Items needed before Week 1-2 completion]

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| [e.g., "PostgreSQL schema documentation"] | Client | [Date] | pending |
| [e.g., "Clarify OpenAI use case examples"] | Client | [Date] | pending |

### Medium Priority (Needed for Milestone 3+)
[TO BE FILLED - Items needed before Week 3+ completion]

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| [e.g., "Stripe account credentials"] | Client | [Date] | pending |
| [e.g., "Define webhook event priorities"] | Both | [Date] | pending |

### Low Priority (Future or Optional)
[TO BE FILLED - Non-blocking items for future consideration]

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| [e.g., "Next.js frontend integration scope"] | Client | Post-MVP | pending |
| [e.g., "Monitoring dashboard setup"] | Developer | Post-MVP | pending |

---

## Risks & Mitigation Strategies

### High Risks Identified During Call
[TO BE FILLED - Risks confirmed or discovered during discovery call from risk-opportunity-list.md]

1. **[Risk Name]**
   - Severity: [BLOCKER / HIGH / MEDIUM / LOW]
   - Probability: [HIGH / MEDIUM / LOW]
   - Impact: [Describe impact]
   - Mitigation: [Describe mitigation strategy]
   - Owner: [Name]

2. **[Risk Name]**
   - Severity: [BLOCKER / HIGH / MEDIUM / LOW]
   - Probability: [HIGH / MEDIUM / LOW]
   - Impact: [Describe impact]
   - Mitigation: [Describe mitigation strategy]
   - Owner: [Name]

### Risks Resolved During Call
[TO BE FILLED - Risks from risk-opportunity-list.md that were resolved]

1. **[Risk Name]** - ✅ RESOLVED
   - Resolution: [How it was resolved]

---

## Opportunities Identified

### Long-Term Engagement Opportunities
[TO BE FILLED - Extension opportunities discussed during call]

1. **[Opportunity Name]**
   - Description: [Brief description]
   - Value: [HIGH / MEDIUM / LOW]
   - Timeline: [Post-MVP / Q2 2025 / TBD]

2. **[Opportunity Name]**
   - Description: [Brief description]
   - Value: [HIGH / MEDIUM / LOW]
   - Timeline: [Post-MVP / Q2 2025 / TBD]

---

## Next Steps

### Immediate Actions (Within 24 Hours)
- [ ] Developer sends discovery recap to client
- [ ] Client reviews and approves discovery recap
- [ ] [Additional immediate actions from call]

### Pre-Project Start Actions (Before Week 1)
- [ ] Client provides all access requirements (GitHub, Discord, API keys)
- [ ] Developer reviews codebase and assesses tech debt
- [ ] Developer prepares Week 1 development environment
- [ ] [Additional pre-start actions from call]

### Project Kickoff
- **Confirmed Start Date:** [TO BE FILLED - YYYY-MM-DD]
- **Kickoff Meeting:** [Scheduled / Not Needed]
- **First Deliverable Due:** [TO BE FILLED - YYYY-MM-DD]

---

## Approval & Sign-Off

**Discovery Lead (Developer):**  
Name: [Your Name]  
Date Completed: [YYYY-MM-DD]  
Signature: ________________

**Client Approval:**  
Name: [Client Name]  
Date Approved: [YYYY-MM-DD]  
Signature: ________________

**Status:** [draft / awaiting_approval / approved / needs_revision]

---

**Instructions for Post-Call Update:**
1. Transfer all information from `discovery-call-notes.md` to corresponding sections above
2. Replace all `[TO BE FILLED]` placeholders with actual information
3. Update status to `awaiting_approval` once complete
4. Include as attachment in `discovery-recap.md` sent to client
5. Update status to `approved` once client signs off

**Linked Artifacts:**
- Source: `discovery-call-notes.md`
- Output: `discovery-recap.md` (client-facing summary)
- Validation: Protocol 03 prerequisites (handoff validation)


---
status: template
last_updated: 2025-11-06T05:40:00Z
prepared_by: Discovery Lead
protocol_id: "02"
call_date: "[TO BE FILLED DURING CALL]"
call_duration: "[TO BE FILLED AFTER CALL]"
recording_consent: "[yes/no - TO BE FILLED AT START]"
---

# Discovery Call Notes

## Call Metadata
- **Date:** [YYYY-MM-DD]
- **Start Time:** [HH:MM timezone]
- **End Time:** [HH:MM timezone]
- **Duration:** [XX minutes]
- **Recording Consent:** [yes / no]
- **Recording Location:** `.artifacts/protocol-02/transcripts/YYYYMMDD-discovery-call.mp4` [if recorded]
- **Attendees:**
  - Developer: [Your Name]
  - Client: [Client Name, Role]
  - Additional: [Name, Role] (if any)

---

## SEGMENT 1: Introduction & Agenda (5 min)

### Notes
[Real-time notes during introduction]

### Key Decisions
- [ ] Call duration confirmed: [XX minutes]
- [ ] Recording consent: [yes/no]
- [ ] Agenda approved: [yes/no]

### Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Action item if any] | [Owner] | [Date] | pending |

---

## SEGMENT 2: Business Outcomes & AI Features (10 min)

### Q-BUS-002: AI Features & Use Cases [P0]
**Question Asked:** "Can you walk me through the specific AI features you're building?"

**Client Response:**
[Capture client's explanation verbatim or paraphrased]

**Key Insights:**
- OpenAI Endpoints Needed: [chat, embeddings, assistants, other]
- Primary Use Case: [describe]
- Secondary Use Cases: [list if any]
- MVP vs Post-MVP: [clarify prioritization]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Document OpenAI endpoint specifications"] | Developer | [Date] | pending |

---

### Q-BUS-001: Budget & Payment Terms [P0]
**Question Asked:** "Does the $2,100-2,700 budget align with your expectations?"

**Client Response:**
[Capture client's budget feedback]

**Key Insights:**
- Budget Status: [approved / needs adjustment / under review]
- Payment Preference: [milestone-based / weekly / hourly / other]
- Payment Schedule: [describe milestones and percentages]
- Concerns or Adjustments: [note any]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Revise proposal with new budget"] | Developer | [Date] | pending |

---

### Q-BUS-004: Long-Term Roadmap [P2] *(if covered)*
**Question Asked:** "What does your product roadmap look like beyond this initial integration?"

**Client Response:**
[Capture roadmap insights]

**Key Insights:**
- 3-6 Month Roadmap: [summarize]
- Long-Term Contract Interest: [yes / no / maybe]
- Future Opportunities: [list potential extensions]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Prepare retainer proposal for future work"] | Developer | Post-MVP | pending |

---

## SEGMENT 3: Technical Stack & Codebase Access (15 min)

### Q-TECH-003: FastAPI Codebase Structure [P0]
**Question Asked:** "Can you give me access to the GitHub repository?"

**Client Response:**
[Capture codebase details]

**Key Insights:**
- GitHub Repository URL: [URL or "to be provided"]
- Access Status: [granted / pending / blocked]
- Codebase Maturity: [greenfield / minimal / mature / legacy]
- Tech Stack: [FastAPI version, Python version, ORM, etc.]
- Tech Debt Observations: [note any red flags mentioned]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Send GitHub repository invite"] | Client | [Date] | pending |
| [e.g., "Review codebase and assess tech debt"] | Developer | Within 48h | pending |

---

### Q-TECH-002: API Key & Credentials Access [P0]
**Question Asked:** "How do I get OpenAI API keys and Stripe account access?"

**Client Response:**
[Capture credential handoff process]

**Key Insights:**
- OpenAI API Key Owner: [Client / Team Member / Shared]
- OpenAI Key Access: [test mode / production / both]
- Stripe Account Owner: [Client / Team Member / Shared]
- Stripe Key Access: [test mode / production / both]
- Secrets Management: [env vars / AWS Secrets Manager / other]
- PostgreSQL Credentials: [to be provided / already in repo / other]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Send OpenAI API key via secure channel"] | Client | [Date] | pending |
| [e.g., "Share Stripe test account credentials"] | Client | [Date] | pending |
| [e.g., "Provide PostgreSQL connection string"] | Client | [Date] | pending |

---

### Q-TECH-001: OpenAI API Endpoints [P0]
**Question Asked:** "Which specific OpenAI endpoints do you need integrated?"

**Client Response:**
[Capture endpoint details]

**Key Insights:**
- Primary Endpoint: [/v1/chat/completions, /v1/embeddings, other]
- Additional Endpoints: [list if any]
- Existing Integration: [yes - partial / no - greenfield]
- Rate Limits: [plan tier, quota concerns]
- Response Caching: [needed / not needed]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Design OpenAI integration architecture"] | Developer | Week 1 | pending |

---

### Q-TECH-004: PostgreSQL Schema & Data Models [P1]
**Question Asked:** "Can you share the current PostgreSQL schema or ERD?"

**Client Response:**
[Capture schema details]

**Key Insights:**
- Schema Exists: [yes / no / partial]
- ERD Available: [yes - shared / no - to be created]
- Users Table: [fields: id, email, stripe_customer_id, etc.]
- Subscriptions Table: [exists / needs creation]
- ORM Used: [SQLAlchemy / other / raw SQL]
- Migrations: [Alembic / manual / other]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Share PostgreSQL schema diagram"] | Client | [Date] | pending |
| [e.g., "Design subscription table schema"] | Developer | Week 1 | pending |

---

### Q-TECH-005: Error Handling & Logging Standards [P1]
**Question Asked:** "Do you have existing error handling patterns or logging frameworks?"

**Client Response:**
[Capture logging standards]

**Key Insights:**
- Logging Framework: [Python logging / loguru / other / none]
- Log Levels: [DEBUG / INFO / WARNING / ERROR]
- Structured Logging: [yes / no]
- Monitoring Tools: [Sentry / DataDog / New Relic / none]
- Error Handling Patterns: [custom middleware / try/except / other]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Set up structured logging framework"] | Developer | Week 1 | pending |
| [e.g., "Integrate Sentry for error tracking"] | Developer | Week 2 | pending |

---

## SEGMENT 4: User Journeys & Stripe Integration (10 min)

### Q-USER-002: Stripe Subscription Model Details [P0]
**Question Asked:** "What subscription model are you using? Which webhook events are critical?"

**Client Response:**
[Capture Stripe details]

**Key Insights:**
- Subscription Model: [monthly / annual / usage-based / tiered / other]
- Plan Tiers: [list tiers if applicable]
- Critical Webhook Events:
  - [ ] invoice.paid
  - [ ] invoice.payment_failed
  - [ ] customer.subscription.updated
  - [ ] customer.subscription.deleted
  - [ ] customer.subscription.created
  - [ ] [other events]
- Payment Failure Handling: [retry logic / grace period / immediate cancellation]
- Proration: [yes / no]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Implement Stripe webhook handlers for listed events"] | Developer | Week 3-4 | pending |

---

### Q-USER-001: User Interaction Flow [P1]
**Question Asked:** "Walk me through a typical user journey with the AI features."

**Client Response:**
[Capture user flow]

**Key Insights:**
- User Journey: [describe step-by-step: trigger → API call → OpenAI → response → storage]
- Frontend Trigger: [button click / form submit / other]
- Real-Time vs Async: [real-time response / async processing]
- Error Handling UX: [what happens if AI request fails?]
- Billing Integration: [does subscription status affect AI access?]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Design API contracts for user journey"] | Developer | Week 1 | pending |

---

## SEGMENT 5: Collaboration Workflow & Logistics (10 min)

### Q-OPS-001: Daily Update & Communication Expectations [P0]
**Question Asked:** "What format works best for daily updates? What timezone overlap do we have?"

**Client Response:**
[Capture communication preferences]

**Key Insights:**
- Daily Update Format: [Discord message / PR descriptions / standup / video]
- Update Frequency: [daily / every other day / weekly]
- Timezone Overlap: [specific hours: e.g., "Tuesday/Thursday 9-10am PST = 10-11pm Pakistan time"]
- Sync vs Async: [mostly async / 2-3 sync calls per week / daily standups]
- Escalation Path: [Discord ping / email / phone / other]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Join Discord server and set up update cadence"] | Developer | Within 24h | pending |
| [e.g., "Schedule recurring weekly check-in calls"] | Both | [Date] | pending |

---

### Q-OPS-003: Milestone Acceptance Criteria [P0]
**Question Asked:** "What does 'done' look like for each milestone?"

**Client Response:**
[Capture acceptance criteria]

**Key Insights:**
- **Week 1-2 (OpenAI Integration):**
  - Acceptance Criteria: [e.g., "Passing tests, documented, deployed to staging"]
  - Demo Required: [yes / no]
  - Approval Process: [client review / team vote / other]

- **Week 3-4 (Stripe Integration):**
  - Acceptance Criteria: [e.g., "Webhooks processing events, test subscriptions created"]
  - Demo Required: [yes / no]
  - Approval Process: [client review / team vote / other]

- **Week 5+ (Debugging & Support):**
  - Acceptance Criteria: [e.g., "Documented error handling, knowledge transfer complete"]
  - Demo Required: [yes / no]
  - Approval Process: [client review / team vote / other]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Document acceptance criteria in timeline-discussion.md"] | Developer | Within 24h | pending |

---

### Q-OPS-002: Code Review & Approval Process [P1]
**Question Asked:** "What's your code review process? Who reviews PRs?"

**Client Response:**
[Capture review workflow]

**Key Insights:**
- Code Review Required: [yes / no]
- Reviewer: [Client / Team Member / Self-merge allowed]
- Review Turnaround: [same-day / 24 hours / 48 hours]
- Branching Strategy: [main/dev / feature branches / other]
- CI/CD: [GitHub Actions / other / none]
- Merge Requirements: [passing tests / approval / both]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Follow branching strategy: feature/name → dev → main"] | Developer | Ongoing | pending |

---

### Q-OPS-004: Deployment & Environment Access [P2] *(if covered)*
**Question Asked:** "What's the deployment process? Do I deploy code myself?"

**Client Response:**
[Capture deployment details]

**Key Insights:**
- Deployment Process: [manual / CI/CD / DevOps team handles]
- Environments: [local / staging / production]
- Access: [developer deploys / DevOps deploys / other]
- Rollback Procedure: [describe if mentioned]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Document deployment process for handoff"] | Developer | Week 5 | pending |

---

## SEGMENT 6: Integrations & Additional Dependencies (5 min)

### Q-INT-001: Third-Party Service Dependencies [P1]
**Question Asked:** "Beyond OpenAI and Stripe, any other third-party services or APIs?"

**Client Response:**
[Capture additional integrations]

**Key Insights:**
- Email Service: [SendGrid / AWS SES / Mailgun / none]
- SMS Service: [Twilio / other / none]
- Analytics: [Mixpanel / Amplitude / Google Analytics / none]
- Monitoring: [Sentry / DataDog / New Relic / none]
- Health-Tech Platforms: [list if any]
- Other Integrations: [list if any]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Update integration-inventory.md with new services"] | Developer | Within 24h | pending |

---

### Q-TECH-006: Next.js Frontend Integration Scope [P2]
**Question Asked:** "Is frontend integration in scope, or backend-only?"

**Client Response:**
[Capture frontend scope]

**Key Insights:**
- Frontend Scope: [in scope / out of scope / post-MVP]
- Timeline: [Week 6-7 / separate project / TBD]
- Frontend Developer: [exists / client handles / developer handles]
- API Documentation: [OpenAPI / Swagger / README / none]

**Action Items:**
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [e.g., "Generate OpenAPI docs for frontend team"] | Developer | Week 2 | pending |

---

## SEGMENT 7: Wrap-Up & Next Steps (5 min)

### Key Decisions Recap
[Summarize 3-5 most important decisions from call]

1. **AI Features:** [brief summary]
2. **Budget & Timeline:** [brief summary]
3. **Access Requirements:** [list GitHub, Discord, API keys, etc.]
4. **Communication Workflow:** [timezone overlap, update format]
5. **Start Date:** [confirmed date]

### Open Questions / Follow-Ups
[List any unanswered questions or items requiring follow-up]

1. [Question/Item] - Owner: [Name], Due: [Date]
2. [Question/Item] - Owner: [Name], Due: [Date]
3. [Question/Item] - Owner: [Name], Due: [Date]

### Client Questions for Developer
[Capture any questions client asked during call]

**Q:** [Client's question]  
**A:** [Your response]

**Q:** [Client's question]  
**A:** [Your response]

### Next Steps Confirmed
- [ ] Developer sends discovery recap within 24 hours
- [ ] Client approves discovery recap
- [ ] Client provides access requirements by [Date]:
  - [ ] GitHub repository invite
  - [ ] Discord server invite
  - [ ] OpenAI API keys
  - [ ] Stripe account credentials
  - [ ] PostgreSQL connection string
- [ ] Project starts on [Start Date]

---

## Post-Call Observations

### What Went Well
[Reflect on successful aspects of the call]
- [Example: "Client was very clear about AI use cases"]
- [Example: "Budget approved without negotiation"]

### Areas for Improvement
[Note any lessons learned]
- [Example: "Needed more time for technical questions"]
- [Example: "Should have probed deeper on compliance requirements"]

### Red Flags / Risks Identified
[Note any concerns that emerged]
- [Example: "Client mentioned 'messy codebase'—tech debt risk"]
- [Example: "Vague acceptance criteria—need to define explicitly"]

### Opportunities Identified
[Note any upsell or expansion opportunities]
- [Example: "Client interested in long-term engagement"]
- [Example: "Frontend integration opportunity in Week 6-7"]

---

## Action Items Summary

### Developer Actions
| Action | Due Date | Status |
|--------|----------|--------|
| Send discovery recap | [Within 24h] | pending |
| Update discovery-brief.md with confirmed info | [Within 24h] | pending |
| Update assumptions-gaps.md (mark resolved) | [Within 24h] | pending |
| Update integration-inventory.md with details | [Within 24h] | pending |
| Review codebase (if repo access granted) | [Within 48h] | pending |
| [Add other actions captured above] | [Date] | pending |

### Client Actions
| Action | Due Date | Status |
|--------|----------|--------|
| Approve discovery recap | [Within 72h] | pending |
| Send GitHub repository invite | [Date] | pending |
| Send Discord server invite | [Date] | pending |
| Provide OpenAI API keys | [Date] | pending |
| Provide Stripe credentials | [Date] | pending |
| Provide PostgreSQL connection string | [Date] | pending |
| [Add other actions captured above] | [Date] | pending |

---

## Recording & Transcript Information

- **Recording File:** `.artifacts/protocol-02/transcripts/YYYYMMDD-discovery-call.mp4`
- **Transcript Status:** [to be generated / generated / not recorded]
- **Transcript Location:** `.artifacts/protocol-02/transcripts/YYYYMMDD-discovery-call.txt`
- **Backup Notes:** This file serves as backup if recording fails

---

## Approval & Sign-Off

**Discovery Lead (Developer):**  
Name: [Your Name]  
Date Completed: [YYYY-MM-DD]  
Signature: ________________

**Next Protocol Trigger:**  
Once client approves discovery recap → Trigger Protocol 03 (Project Brief Creation)


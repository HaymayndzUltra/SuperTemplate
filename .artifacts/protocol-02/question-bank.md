---
status: pre_call_ready
last_updated: 2025-11-06T05:40:00Z
prepared_by: Discovery Lead
protocol_id: "02"
linked_artifacts:
  - assumptions-gaps.md
  - risk-opportunity-list.md
---

# Discovery Call Question Bank

## Prioritization Guide
- **P0 (Must-Ask):** Questions that block Protocol 03 handoff or Week 1 development
- **P1 (Should-Ask):** Questions that clarify key assumptions and reduce risk
- **P2 (Nice-to-Ask):** Questions that optimize delivery and explore opportunities

---

## THEME 1: Business Outcomes & Product Vision

### Q-BUS-001: Budget & Payment Terms [P0]
**Question:** "I proposed a budget range of $2,100-2,700 for this project based on the scope we discussed. Does that align with your budget expectations? And what payment structure works best for you—milestone-based, weekly, or something else?"

**Why Ask:** RISK-003 (Budget Mismatch), ASSUMPTION-010 (Budget Flexibility)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-010, `risk-opportunity-list.md` RISK-003  
**Acceptable Answers:**
- Budget approved → Proceed with milestone structure
- Budget concerns → Negotiate scope reduction or phased approach
- Payment preference → Document in communication-plan.md

**Follow-Up Questions:**
- "What milestones make most sense for your approval workflow?"
- "Do you need invoicing through a specific platform or method?"

**Red Flags:**
- Budget significantly lower than estimate → Scope reduction required
- No budget approval authority → Need to escalate to decision maker

---

### Q-BUS-002: AI Features & Use Cases [P0]
**Question:** "You mentioned needing OpenAI API integration. Can you walk me through the specific AI features you're building? For example, are you doing chat-based interactions, document analysis, embeddings for search, or something else? What's the core user experience you're enabling?"

**Why Ask:** RISK-002 (Unclear OpenAI Integration Scope), ASSUMPTION-001 (OpenAI Use Case)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-001, `risk-opportunity-list.md` RISK-002  
**Acceptable Answers:**
- Chat completions for conversational AI → Focus on chat endpoint
- Embeddings for semantic search → Focus on embeddings + vector DB
- Multiple features → Prioritize MVP vs. post-MVP features

**Follow-Up Questions:**
- "Which AI feature is highest priority for MVP?"
- "Do you have existing prompts or example interactions I can reference?"
- "What's the expected API call volume? (for rate limit planning)"

**Red Flags:**
- Vague answer → Need more discovery before Week 1
- Multiple complex AI features → Timeline may be underestimated

---

### Q-BUS-003: Health-Tech Compliance & Data Sensitivity [P1]
**Question:** "I noticed this is a health-tech product. Are you handling any protected health information (PHI) or personally identifiable information (PII)? Do we need to consider HIPAA, GDPR, or other compliance requirements for this integration work?"

**Why Ask:** RISK-007 (Health-Tech Compliance Requirements), ASSUMPTION-006 (Health-Tech Domain)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-006, `risk-opportunity-list.md` RISK-007  
**Acceptable Answers:**
- No PHI/PII involved → Standard security practices sufficient
- PHI involved, HIPAA required → Add 2-4 week compliance phase
- Compliance handled separately → Document integration boundary

**Follow-Up Questions:**
- "What data will the OpenAI integration access or process?"
- "Are there data retention or deletion requirements I need to account for?"
- "Do you have a security/compliance review process for new integrations?"

**Red Flags:**
- PHI involved but not mentioned in scope → Major timeline/budget impact
- Unclear compliance requirements → Need legal/compliance consultation

---

### Q-BUS-004: Long-Term Roadmap & Future Features [P2]
**Question:** "The job post mentioned potential for long-term engagement. What does your product roadmap look like beyond this initial integration? Are there other AI features, billing enhancements, or areas where you'd want ongoing support?"

**Why Ask:** OPPORTUNITY-001 (Long-Term Contract Extension)  
**Linked to:** `risk-opportunity-list.md` OPPORTUNITY-001  
**Acceptable Answers:**
- Clear 3-6 month roadmap → Note extension opportunities
- Ongoing maintenance needs → Discuss retainer structure
- Uncertain roadmap → Focus on current project, revisit later

**Follow-Up Questions:**
- "What's your biggest challenge or bottleneck after this integration?"
- "Are there other team members who might need similar development support?"

**Success Indicators:**
- Client shares detailed roadmap → High extension probability
- Client mentions ongoing needs → Prepare retainer proposal

---

## THEME 2: User Journeys & Functional Requirements

### Q-USER-001: User Interaction Flow [P1]
**Question:** "Can you walk me through a typical user journey where they interact with the OpenAI-powered features? From the user's perspective, what happens when they trigger an AI interaction?"

**Why Ask:** Understand user experience context for API design  
**Linked to:** `discovery-brief.md` Target Users section  
**Acceptable Answers:**
- Clear user flow → Design API contracts to match UX
- Multiple user types → Prioritize primary persona
- Frontend triggers API → Clarify frontend integration scope

**Follow-Up Questions:**
- "What happens if the AI request takes too long or fails?"
- "Do users need to see real-time responses, or can it be async?"
- "Are there any user-facing features that depend on Stripe billing status?"

**Red Flags:**
- No clear user journey → May indicate unclear product vision
- Complex multi-step flows → Underestimated integration complexity

---

### Q-USER-002: Stripe Subscription Model Details [P0]
**Question:** "For the Stripe billing setup, what subscription model are you using? Are we talking about monthly/annual subscriptions, usage-based billing, tiered plans, or something else? Which subscription events are most critical—like invoice.paid, subscription.updated, or payment failures?"

**Why Ask:** ASSUMPTION-002 (Stripe Subscription Model), RISK-001 (Undefined Requirements)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-002  
**Acceptable Answers:**
- Standard subscription model → Implement common events (invoice.paid, subscription.updated, payment_intent.succeeded)
- Usage-based → Add metering logic and usage tracking
- Tiered plans → Design plan comparison and upgrade logic

**Follow-Up Questions:**
- "What should happen when a payment fails? (retry logic, grace period, feature access)"
- "Do you need webhook notifications for trial expirations or cancellations?"
- "How do you want to handle proration for plan changes?"

**Red Flags:**
- Complex custom billing logic → May need Stripe experts consultation
- Unclear billing model → Blocks Week 3 architecture decisions

---

## THEME 3: Technical Stack & Architecture

### Q-TECH-001: OpenAI API Endpoints & Integration Patterns [P0]
**Question:** "Which specific OpenAI endpoints do you need integrated? For example, are we using the chat completions endpoint, embeddings, assistants API, or others? And do you have any existing integration code I should build on, or is this greenfield?"

**Why Ask:** ASSUMPTION-001 (OpenAI Use Case), ASSUMPTION-004 (Existing FastAPI Backend)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-001, ASSUMPTION-004  
**Acceptable Answers:**
- Specific endpoints identified → Document in scope-clarification.md
- Existing integration started → Review code for patterns
- Greenfield → Design architecture from scratch

**Follow-Up Questions:**
- "Do you have rate limits or quota concerns with OpenAI?"
- "Should I implement response caching or streaming for better UX?"
- "Are there any OpenAI features you want to experiment with (function calling, JSON mode)?"

**Red Flags:**
- No endpoint specificity → Blocks Week 1 development
- Legacy integration with tech debt → May need refactoring phase

---

### Q-TECH-002: API Key & Credentials Access [P0]
**Question:** "To get started, I'll need access to OpenAI API keys and your Stripe account. Who owns these accounts, and what's the process for getting test and production credentials? Do you use any secrets management tools like AWS Secrets Manager or environment variables?"

**Why Ask:** GAP-001 (API Key Access), GAP-002 (Stripe Account Details), RISK-001 (Missing Credentials)  
**Linked to:** `assumptions-gaps.md` GAP-001, GAP-002, `risk-opportunity-list.md` RISK-001  
**Acceptable Answers:**
- Test credentials available immediately → Start Week 1 setup
- Production credentials delayed → Use test accounts initially
- Secrets manager in place → Follow existing patterns

**Follow-Up Questions:**
- "Are the API keys already in your codebase, or do I need to add them?"
- "What's the process for rotating keys or updating credentials?"
- "Do you have separate test/production Stripe accounts, or one account with test mode?"

**Red Flags:**
- No credential access → Blocks Day 1 development
- Manual credential management → Security risk, propose secrets management

---

### Q-TECH-003: FastAPI Codebase Structure [P0]
**Question:** "Can you give me access to the GitHub repository so I can review the existing FastAPI backend? What's the current structure—are there existing routes, database models, error handling patterns I should follow? And what's the deployment setup?"

**Why Ask:** GAP-003 (GitHub Repository Access), ASSUMPTION-004 (Existing FastAPI Backend), RISK-006 (Codebase Complexity)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-004, GAP-003, `risk-opportunity-list.md` RISK-006  
**Acceptable Answers:**
- Mature codebase → Follow existing patterns and conventions
- Minimal codebase → More greenfield, establish patterns
- Tech debt identified → Discuss refactoring scope

**Follow-Up Questions:**
- "Are there existing tests I should follow as examples?"
- "What's the branching strategy? (main/dev, feature branches, etc.)"
- "Do you have CI/CD pipelines, or is deployment manual?"

**Red Flags:**
- No repository access → Cannot start work
- Major tech debt → Timeline underestimated, may need refactoring phase

---

### Q-TECH-004: PostgreSQL Schema & Data Models [P1]
**Question:** "For the Stripe integration, I'll need to understand how you're storing user and subscription data. Can you share the current PostgreSQL schema or ERD? Specifically, how are users, subscriptions, and payment events modeled?"

**Why Ask:** ASSUMPTION-003 (PostgreSQL Schema Exists), GAP-008 (PostgreSQL Access), RISK-009 (Schema Mismatch)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-003, GAP-008, `risk-opportunity-list.md` RISK-009  
**Acceptable Answers:**
- Schema exists and shared → Review for integration compatibility
- No schema yet → Design schema collaboratively
- Schema locked → Design abstraction layer

**Follow-Up Questions:**
- "Who manages database migrations? (you, me, or shared?)"
- "Are there any performance concerns or indexing requirements?"
- "Do you use an ORM like SQLAlchemy, or raw SQL?"

**Red Flags:**
- No schema visibility → Cannot validate integration approach
- Schema redesign needed → Add migration phase to timeline

---

### Q-TECH-005: Error Handling & Logging Standards [P1]
**Question:** "Do you have existing error handling patterns or logging frameworks I should follow? For example, are you using structured logging, specific error codes, or monitoring tools like Sentry or DataDog?"

**Why Ask:** GAP-005 (Error Handling Standards), OPPORTUNITY-004 (Monitoring Practice)  
**Linked to:** `assumptions-gaps.md` GAP-005, `risk-opportunity-list.md` OPPORTUNITY-004  
**Acceptable Answers:**
- Standards exist → Follow existing patterns
- No standards → Propose structured logging approach
- Monitoring tools in place → Integrate with existing observability

**Follow-Up Questions:**
- "What log level do you prefer for production? (INFO, WARNING, ERROR?)"
- "Should I implement retry logic for API failures, and if so, what's the retry strategy?"
- "Do you have alerting set up, or is that something you'd want me to implement?"

**Success Indicators:**
- Client interested in monitoring → OPPORTUNITY-004 (propose dashboard)
- No standards exist → Opportunity to establish best practices

---

### Q-TECH-006: Next.js Frontend Integration Scope [P2]
**Question:** "The job post mentioned Next.js as a nice-to-have. Is frontend integration in scope for this project, or is it backend-only? If it's in scope, what's the timeline—should I work on that during the initial 1-2 months, or is it a post-MVP consideration?"

**Why Ask:** ASSUMPTION-005 (Next.js Frontend Exists), OPPORTUNITY-002 (Expand Scope)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-005, `risk-opportunity-list.md` OPPORTUNITY-002  
**Acceptable Answers:**
- Backend-only for now → Focus on API design and documentation
- Frontend in scope → Add frontend milestone (Week 6-7?)
- Post-MVP frontend → Design API contracts for future frontend use

**Follow-Up Questions:**
- "Should I document API contracts in a frontend-friendly format? (OpenAPI/Swagger?)"
- "Are there any frontend developers I should coordinate with?"
- "Would you like me to create a simple frontend demo for testing?"

**Success Indicators:**
- Client wants frontend integration → OPPORTUNITY-002 (propose milestone)
- Client wants API docs → Prioritize documentation quality

---

## THEME 4: Integrations & Dependencies

### Q-INT-001: Third-Party Service Dependencies [P1]
**Question:** "Beyond OpenAI and Stripe, are there any other third-party services or APIs I need to integrate with? For example, email services, SMS providers, analytics tools, or other health-tech platforms?"

**Why Ask:** Identify hidden integration requirements  
**Linked to:** `integration-inventory.md` (to be populated)  
**Acceptable Answers:**
- No other integrations → Simplifies scope
- Email/SMS providers → Add notification logic
- Health-tech platforms → May require compliance considerations

**Follow-Up Questions:**
- "Which integrations are MVP vs. post-MVP?"
- "Do you have existing accounts and credentials for these services?"
- "Are there any data sync requirements between systems?"

**Red Flags:**
- Many undisclosed integrations → Scope creep risk
- Complex B2B integrations → May need integration specialists

---

### Q-INT-002: Data Ownership & Access Control [P1]
**Question:** "For the OpenAI and Stripe integrations, who owns the data and API access? Do I need specific permissions or roles configured? And are there any data residency or storage requirements I should know about?"

**Why Ask:** Clarify access permissions and compliance boundaries  
**Linked to:** `integration-inventory.md` Owner column  
**Acceptable Answers:**
- Clear ownership identified → Document in integration-inventory.md
- Shared ownership → Establish coordination process
- Compliance requirements → Document in scope-clarification.md

**Follow-Up Questions:**
- "Should OpenAI API calls be logged or audited?"
- "Do you have data retention policies for API requests/responses?"
- "Are there any regions where data cannot be processed? (for OpenAI API routing)"

**Red Flags:**
- Unclear ownership → Blocks credential access and testing
- Conflicting data policies → May require legal review

---

## THEME 5: Compliance & Security

### Q-COMP-001: Security Requirements & Best Practices [P1]
**Question:** "What security requirements should I follow for this integration? For example, do you need API authentication, rate limiting, encryption at rest/in transit, or audit logging?"

**Why Ask:** Establish security baseline and compliance needs  
**Linked to:** `scope-clarification.md` Security section  
**Acceptable Answers:**
- Standard HTTPS + API keys → Follow best practices
- Enhanced security → Implement OAuth, encryption, audit logging
- Compliance-driven → Document requirements in detail

**Follow-Up Questions:**
- "Do you have a security review process for new code?"
- "Should I implement API rate limiting to prevent abuse?"
- "Are there penetration testing or security audit requirements?"

**Red Flags:**
- No security standards → Propose baseline security practices
- High-security needs not in scope → Budget/timeline impact

---

### Q-COMP-002: Testing & Quality Assurance Approach [P1]
**Question:** "What's your testing and QA approach? Do you have existing test suites I should extend, or should I set up pytest from scratch? And what level of test coverage are you expecting—unit tests, integration tests, or both?"

**Why Ask:** GAP-006 (Testing Infrastructure), RISK-004 (Acceptance Criteria)  
**Linked to:** `assumptions-gaps.md` GAP-006, `risk-opportunity-list.md` RISK-004  
**Acceptable Answers:**
- Existing test suite → Follow patterns and extend
- No tests → Set up pytest with >80% coverage
- Manual QA only → Propose automated test strategy

**Follow-Up Questions:**
- "What's your definition of 'done' for each feature? (passing tests, code review, deployed?)"
- "Do you want me to write tests first (TDD) or after implementation?"
- "Should I set up test fixtures for Stripe/OpenAI mocking?"

**Success Indicators:**
- Client values testing → Allocate sufficient time for test coverage
- Clear acceptance criteria → Document in discovery-form.md

---

## THEME 6: Delivery Logistics & Collaboration

### Q-OPS-001: Daily Update & Communication Expectations [P0]
**Question:** "You mentioned daily updates via GitHub and Discord. What format works best for you—PR descriptions, Discord standups, or something else? And what timezone overlap can we count on for sync conversations?"

**Why Ask:** ASSUMPTION-007 (Timezone Overlap), ASSUMPTION-008 (Daily Updates), RISK-005 (Timezone Coordination)  
**Linked to:** `assumptions-gaps.md` ASSUMPTION-007, ASSUMPTION-008, `risk-opportunity-list.md` RISK-005  
**Acceptable Answers:**
- Specific format preferred → Document in communication-plan.md
- Flexible format → Propose structured PR descriptions + Discord summaries
- Timezone overlap confirmed → Establish "core hours"

**Follow-Up Questions:**
- "What time of day works best for sync calls or quick questions?"
- "How should I escalate blockers or urgent issues?"
- "Do you prefer video calls, voice calls, or text-based communication?"

**Red Flags:**
- No timezone overlap → May need async-first workflow
- Unclear update format → Risk of misaligned expectations

---

### Q-OPS-002: Code Review & Approval Process [P1]
**Question:** "What's your code review process? Should I submit PRs daily, wait for approval before continuing, or can I merge after self-review? And who will be reviewing my code?"

**Why Ask:** Establish development workflow and approval gates  
**Linked to:** `communication-plan.md` Workflow section  
**Acceptable Answers:**
- PR review required → Plan time for review cycles
- Self-merge allowed → Faster iteration, document guidelines
- Specific reviewer assigned → Coordinate availability

**Follow-Up Questions:**
- "What's the expected review turnaround time? (same-day, 24 hours?)"
- "Are there any code style guides or linting rules I should follow?"
- "Should I squash commits, or keep detailed commit history?"

**Success Indicators:**
- Clear review process → Smooth collaboration
- Fast review turnaround → Maintains momentum

---

### Q-OPS-003: Milestone Acceptance Criteria [P0]
**Question:** "Let's define 'done' for each milestone. For the OpenAI integration (Week 1-2), what does success look like? Passing tests, deployed to staging, documented, or all of the above? Same question for Stripe (Week 3-4) and debugging support (Week 5+)."

**Why Ask:** RISK-004 (Undefined Acceptance Criteria), GAP-010 (Acceptance Criteria per Feature)  
**Linked to:** `assumptions-gaps.md` GAP-010, `risk-opportunity-list.md` RISK-004  
**Acceptable Answers:**
- Clear criteria per milestone → Document in timeline-discussion.md
- Needs discussion → Propose criteria and get approval
- Demo-based approval → Schedule milestone demos

**Follow-Up Questions:**
- "Should I record demo videos for each milestone, or live demos?"
- "What's the approval workflow? (you approve, or team vote?)"
- "How do you want to handle change requests during milestones?"

**Red Flags:**
- Vague acceptance criteria → Risk of scope creep and endless revisions
- No approval process → Unclear handoff and payment triggers

---

### Q-OPS-004: Deployment & Environment Access [P2]
**Question:** "What's the deployment process? Do you have staging and production environments? Will I be deploying code myself, or is there a DevOps team? And what CI/CD tools are you using?"

**Why Ask:** GAP-009 (Deployment Environment)  
**Linked to:** `assumptions-gaps.md` GAP-009  
**Acceptable Answers:**
- Manual deployment → Document process and credentials
- CI/CD pipeline exists → Review and integrate
- DevOps team handles deployment → Coordinate handoff process

**Follow-Up Questions:**
- "Do you have automated tests running on PR merge?"
- "What's the rollback procedure if something breaks in production?"
- "Should I set up deployment documentation as part of handoff?"

**Success Indicators:**
- Modern CI/CD setup → Faster iteration and deployment
- Clear deployment process → Reduces production risk

---

## Question Bank Summary

| Theme | Total Questions | P0 (Must-Ask) | P1 (Should-Ask) | P2 (Nice-to-Ask) |
|-------|-----------------|---------------|-----------------|------------------|
| Business Outcomes | 4 | 2 | 1 | 1 |
| User Journeys | 2 | 1 | 1 | 0 |
| Technical Stack | 6 | 3 | 2 | 1 |
| Integrations | 2 | 0 | 2 | 0 |
| Compliance & Security | 2 | 0 | 2 | 0 |
| Delivery Logistics | 4 | 2 | 1 | 1 |
| **TOTAL** | **20** | **8** | **9** | **3** |

## Discovery Call Time Allocation

**Estimated 60-minute call structure:**
- **Introduction & Agenda (5 min):** Set expectations and flow
- **Business Outcomes (10 min):** Q-BUS-001, Q-BUS-002 (P0 priorities)
- **Technical Stack & Scope (15 min):** Q-TECH-001, Q-TECH-002, Q-TECH-003 (blockers)
- **User Journeys & Requirements (10 min):** Q-USER-002, Q-TECH-004 (core functionality)
- **Logistics & Collaboration (10 min):** Q-OPS-001, Q-OPS-003 (process setup)
- **Integrations & Opportunities (5 min):** Q-INT-001, Q-BUS-004 (if time allows)
- **Wrap-Up & Next Steps (5 min):** Recap, follow-ups, timeline confirmation

**If time runs short, defer to follow-up:**
- P2 questions (Q-TECH-006, Q-OPS-004, Q-BUS-004)
- Detailed compliance questions (Q-COMP-001, Q-COMP-002) if not critical for MVP

## Cross-Reference Links

All "ASK CLIENT" items from `assumptions-gaps.md` are mapped to question IDs:
- ASSUMPTION-001 → Q-BUS-002, Q-TECH-001
- ASSUMPTION-002 → Q-USER-002
- ASSUMPTION-003 → Q-TECH-004
- ASSUMPTION-004 → Q-TECH-003
- ASSUMPTION-005 → Q-TECH-006
- ASSUMPTION-006 → Q-BUS-003
- ASSUMPTION-010 → Q-BUS-001
- GAP-001 → Q-TECH-002
- GAP-002 → Q-TECH-002
- GAP-003 → Q-TECH-003
- GAP-004 → Q-OPS-001
- GAP-005 → Q-TECH-005
- GAP-006 → Q-COMP-002
- GAP-008 → Q-TECH-004
- GAP-009 → Q-OPS-004
- GAP-010 → Q-OPS-003


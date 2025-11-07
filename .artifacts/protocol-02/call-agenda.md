---
status: pre_call_ready
last_updated: 2025-11-06T05:40:00Z
prepared_by: Discovery Lead
protocol_id: "02"
meeting_duration: 60 minutes
---

# Discovery Call Agenda

## Meeting Information
- **Proposed Duration:** 60 minutes
- **Participants:**
  - Discovery Lead (Developer)
  - Client (Project Owner)
  - [Optional] Client Team Members
- **Scheduled Date/Time:** [TO BE SCHEDULED]
- **Meeting Link:** [TO BE PROVIDED]
- **Recording:** [TO BE CONFIRMED WITH CLIENT]

---

## Pre-Call Checklist (Developer Actions)

### 5 Minutes Before Call
- [ ] **Load Context:** Open `discovery-brief.md`, `question-bank.md`, `assumptions-gaps.md` in Cursor workspace
- [ ] **Load Tools:**
  - [ ] `discovery-call-notes.md` open for real-time note-taking
  - [ ] `question-bank.md` as reference for P0 questions
  - [ ] `scenario-guides.md` for pivot responses
- [ ] **Equipment Check:**
  - [ ] Microphone and audio working
  - [ ] Video camera working (if video call)
  - [ ] Internet connection stable
  - [ ] Recording software ready (if client approves recording)
- [ ] **Recording Consent:** Prepare to ask for recording permission at start of call
- [ ] **Backup Plan:** Have phone number ready as backup if video call fails

### Context Review (Already Completed)
- [ ] Reviewed job post and proposal
- [ ] Reviewed Protocol 01 artifacts (PROPOSAL.md, proposal-summary.json)
- [ ] Question bank prioritized (8 P0, 9 P1, 3 P2)
- [ ] Risk and opportunity list reviewed
- [ ] Scenario response guides internalized

---

## Call Agenda (60 Minutes)

### SEGMENT 1: Introduction & Agenda Setting (5 minutes)

**Objectives:**
- Establish rapport and professionalism
- Confirm call duration and agenda
- Obtain recording consent

**Script:**
> "Hey [Client Name], great to finally connect! Thanks for taking the time. I have about an hour blocked, does that still work for you?"
> 
> "[If yes] Perfect. Here's what I'd like to cover today:
> 1. Understand your business goals and the AI features you're building
> 2. Clarify the technical stack and any existing codebase
> 3. Align on timeline, budget, and collaboration workflow
> 4. Answer any questions you have for me
> 
> Sound good?"
> 
> "One quick ask—would you mind if I record this call for my notes? I want to make sure I capture everything accurately. I won't share the recording with anyone, it's just for my reference."

**Call Notes Actions:**
- [ ] Confirm call duration agreed
- [ ] Note recording consent (yes/no)
- [ ] Note any additional attendees introduced

---

### SEGMENT 2: Business Outcomes & AI Features (10 minutes)

**Objectives:**
- Clarify OpenAI integration scope and use cases
- Understand business goals and success metrics
- Validate budget alignment

**Questions to Cover (from question-bank.md):**
1. **Q-BUS-002:** AI Features & Use Cases [P0]
   - "Can you walk me through the specific AI features you're building? Chat-based interactions, document analysis, embeddings for search, or something else?"
   
2. **Q-BUS-001:** Budget & Payment Terms [P0]
   - "I proposed $2,100-2,700 for this project. Does that align with your budget? And what payment structure works best—milestone-based, weekly, or other?"

3. **Q-BUS-004:** Long-Term Roadmap [P2] *(if time allows)*
   - "What does your product roadmap look like beyond this initial integration? Any other AI features or areas where you'd want ongoing support?"

**Call Notes Actions:**
- [ ] Document specific OpenAI endpoints needed (chat, embeddings, assistants, etc.)
- [ ] Note MVP vs. post-MVP AI features
- [ ] Confirm budget approval status
- [ ] Document payment preference (milestone, weekly, hourly)
- [ ] Capture long-term roadmap insights (for future opportunities)

**Watch For (from scenario-guides.md):**
- Budget concerns → Apply SCENARIO 1 (Budget Below Estimate) response
- Scope expansion → Apply SCENARIO 2 (Scope Expansion) response
- HIPAA/compliance mentions → Apply SCENARIO 3 (Compliance Requirements) response

---

### SEGMENT 3: Technical Stack & Codebase Access (15 minutes)

**Objectives:**
- Obtain repository and credential access information
- Understand existing codebase structure and tech debt
- Clarify integration dependencies

**Questions to Cover:**
1. **Q-TECH-003:** FastAPI Codebase Structure [P0]
   - "Can you give me access to the GitHub repository? What's the current structure—existing routes, database models, error handling patterns?"

2. **Q-TECH-002:** API Key & Credentials Access [P0]
   - "I'll need OpenAI API keys and Stripe account access to get started. Who owns these accounts, and what's the process for getting test and production credentials?"

3. **Q-TECH-001:** OpenAI API Endpoints [P0]
   - "Which specific OpenAI endpoints do you need integrated? And do you have any existing integration code, or is this greenfield?"

4. **Q-TECH-004:** PostgreSQL Schema & Data Models [P1]
   - "Can you share the current PostgreSQL schema or ERD? Specifically, how are users, subscriptions, and payment events modeled?"

5. **Q-TECH-005:** Error Handling & Logging Standards [P1]
   - "Do you have existing error handling patterns or logging frameworks? Are you using structured logging, monitoring tools like Sentry?"

**Call Notes Actions:**
- [ ] Capture GitHub repository URL
- [ ] Document credential handoff process (OpenAI, Stripe, PostgreSQL)
- [ ] Note existing tech stack details (FastAPI version, database, ORM, etc.)
- [ ] Identify any tech debt concerns
- [ ] Document error handling and logging standards

**Watch For:**
- Tech debt signals → Prepare to apply SCENARIO 4 (Tech Debt) assessment post-call
- Missing repository access → Escalate as critical blocker

---

### SEGMENT 4: User Journeys & Stripe Integration (10 minutes)

**Objectives:**
- Understand user interaction flows
- Clarify Stripe subscription model and webhook events
- Validate acceptance criteria

**Questions to Cover:**
1. **Q-USER-002:** Stripe Subscription Model Details [P0]
   - "For Stripe billing, what subscription model are you using? Monthly/annual, usage-based, tiered plans? Which webhook events are most critical?"

2. **Q-USER-001:** User Interaction Flow [P1]
   - "Can you walk me through a typical user journey where they interact with the AI-powered features? What triggers an AI interaction?"

3. **Q-TECH-004:** PostgreSQL Schema [P1] *(if not covered earlier)*
   - "How are users and subscriptions stored in the database? Is there a Stripe customer ID field?"

**Call Notes Actions:**
- [ ] Document Stripe subscription model (monthly, annual, usage-based, etc.)
- [ ] List critical webhook events (invoice.paid, subscription.updated, payment failures)
- [ ] Capture user journey flow (frontend → API → OpenAI → response)
- [ ] Note any data retention or compliance requirements

---

### SEGMENT 5: Collaboration Workflow & Logistics (10 minutes)

**Objectives:**
- Establish communication norms and timezone overlap
- Define code review and deployment processes
- Set milestone acceptance criteria

**Questions to Cover:**
1. **Q-OPS-001:** Daily Update & Communication Expectations [P0]
   - "You mentioned daily updates via GitHub and Discord. What format works best? And what timezone overlap can we count on for sync conversations?"

2. **Q-OPS-003:** Milestone Acceptance Criteria [P0]
   - "Let's define 'done' for each milestone. For OpenAI integration (Week 1-2), what does success look like? Passing tests, deployed to staging, documented?"

3. **Q-OPS-002:** Code Review & Approval Process [P1]
   - "What's your code review process? Should I submit PRs daily and wait for approval, or can I merge after self-review?"

4. **Q-OPS-004:** Deployment & Environment Access [P2] *(if time allows)*
   - "What's the deployment process? Staging and production environments? Will I be deploying code, or is there a DevOps team?"

**Call Notes Actions:**
- [ ] Document timezone overlap hours (specific times)
- [ ] Capture daily update format preference (Discord, PR descriptions, both)
- [ ] Define acceptance criteria per milestone
- [ ] Note code review workflow and turnaround SLA
- [ ] Document deployment process and environment access

**Watch For:**
- Limited timezone overlap → Apply SCENARIO 5 (Timezone Coordination) framework
- Unclear acceptance criteria → Push for specificity to avoid RISK-004

---

### SEGMENT 6: Integrations & Additional Dependencies (5 minutes)

**Objectives:**
- Identify hidden integrations or third-party dependencies
- Clarify Next.js frontend scope

**Questions to Cover:**
1. **Q-INT-001:** Third-Party Service Dependencies [P1]
   - "Beyond OpenAI and Stripe, are there any other third-party services or APIs I need to integrate with? Email, SMS, analytics?"

2. **Q-TECH-006:** Next.js Frontend Integration Scope [P2]
   - "The job post mentioned Next.js as nice-to-have. Is frontend integration in scope for this project, or backend-only?"

**Call Notes Actions:**
- [ ] List all third-party integrations (MVP vs. post-MVP)
- [ ] Clarify frontend scope (in/out of scope, timeline)
- [ ] Note any undisclosed dependencies

---

### SEGMENT 7: Wrap-Up & Next Steps (5 minutes)

**Objectives:**
- Recap key decisions and action items
- Confirm timeline and start date
- Set expectations for discovery recap delivery

**Script:**
> "Great, this has been really helpful. Let me quickly recap the key points I captured:
> - [Summarize 3-5 key decisions: AI features, budget, timeline, access requirements]
> 
> Here's what happens next:
> 1. I'll send you a discovery recap within 24 hours summarizing everything we discussed
> 2. Once you approve that, I'll need [list access requirements: GitHub invite, Discord server, API keys]
> 3. Assuming we have those by [date], I'll kick off Week 1 on [start date]
> 
> Does that timeline work for you? Any questions for me before we wrap?"

**Call Notes Actions:**
- [ ] Document start date
- [ ] List access requirements and deadlines
- [ ] Note any open questions or follow-ups
- [ ] Confirm recap send deadline (24 hours)
- [ ] Thank client and end call professionally

---

## Post-Call Immediate Actions (Within 1 Hour)

### Critical Actions
1. **Save Recording:** Download and save call recording to `.artifacts/protocol-02/transcripts/YYYYMMDD-discovery-call.mp4`
2. **Review Notes:** Re-read `discovery-call-notes.md` for completeness and clarity
3. **Flag Blockers:** Identify any P0 blockers that require immediate follow-up
4. **Update Artifacts:**
   - Mark resolved assumptions in `assumptions-gaps.md`
   - Update `integration-inventory.md` with confirmed details
   - Flag any new risks in `risk-opportunity-list.md`

### Next 24 Hours
5. **Generate Discovery Recap:** Create `discovery-recap.md` (see Phase 4)
6. **Update Discovery Form:** Transfer confirmed answers to `client-discovery-form.md`
7. **Update Scope Clarification:** Document technical stack decisions in `scope-clarification.md`
8. **Update Timeline:** Record agreed milestones in `timeline-discussion.md`
9. **Update Communication Plan:** Capture cadence and tools in `communication-plan.md`
10. **Send Discovery Recap:** Email or Discord message to client with approval request

---

## Backup Plans

### If Client is Late or No-Show
- **5 minutes late:** Send Discord/SMS check-in
- **10 minutes late:** Propose rescheduling
- **15+ minutes late:** End call attempt, send rescheduling request

### If Call Runs Over Time
- **Priority Questions Only:** Cover all P0 questions first (8 questions)
- **Defer P1/P2:** Note unanswered P1/P2 questions for follow-up email
- **Extend if Possible:** Ask client if they have 10-15 more minutes

### If Technical Issues Occur
- **Video Fails:** Switch to audio-only call
- **Audio Fails:** Switch to phone call (backup number)
- **Internet Fails:** Reschedule and apologize professionally

### If Client Brings Unexpected Team Members
- **Introduce Yourself:** Briefly re-state your role and proposal context
- **Adjust Agenda:** Ask if additional attendees have specific questions
- **Capture Roles:** Document each attendee's role and responsibilities

---

## Success Criteria for Discovery Call

- ✅ **All P0 questions answered** (8 questions from question-bank.md)
- ✅ **Budget and timeline confirmed** (no blocking misalignments)
- ✅ **Access requirements documented** (GitHub, Discord, API keys, etc.)
- ✅ **MVP scope clear** (OpenAI endpoints, Stripe events, acceptance criteria)
- ✅ **Communication workflow agreed** (timezone overlap, update format, code review process)
- ✅ **Recording saved** (or detailed notes if no recording)
- ✅ **Recap delivery promised** (24-hour turnaround)

---

## Post-Call Self-Assessment

After the call, rate these dimensions (1-5 scale):

| Dimension | Rating (1-5) | Notes |
|-----------|--------------|-------|
| **Preparation Quality** | [ ] | Did I have all context ready? |
| **Question Coverage** | [ ] | Did I cover all P0 questions? |
| **Active Listening** | [ ] | Did I let client fully explain? |
| **Professionalism** | [ ] | Did I maintain professional tone? |
| **Clarity of Next Steps** | [ ] | Does client know what happens next? |
| **Relationship Building** | [ ] | Did I establish trust and rapport? |

**What Went Well:**
- [Capture successes]

**What Could Improve:**
- [Capture lessons for next discovery call]

**Unexpected Insights:**
- [Note any surprises or valuable context]

---

## Reminders

- ⏰ **Recording Consent:** Ask at the start, respect if client declines
- 📝 **Live Notes:** Take notes in real-time, don't rely only on recording
- 🚫 **No External Messages:** All client communication stays internal until recap is approved
- ⏱️ **Time Management:** Watch the clock, cover P0 questions first
- 🎯 **Stay Focused:** Politely redirect if conversation strays off-topic
- 🤝 **Professional Tone:** Friendly but professional, maintain boundaries
- 🔄 **Confirm Understanding:** Repeat back key decisions to ensure alignment


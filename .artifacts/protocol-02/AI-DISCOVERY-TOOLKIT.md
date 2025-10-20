# PROTOCOL 02 AI-DRIVEN DISCOVERY TOOLKIT

**Para sa AI Orchestrator**: Complete preparation bago client meeting  
**Goal**: Structured, comprehensive discovery na AI-guided

---

## PART 1: DISCOVERY QUESTION BANK

### Business & Objectives Questions
1. What specific problem are you solving for your users?
2. Who are your primary target users? (personas)
3. What does success look like in 6 months? (KPIs)
4. What's your competitive advantage?
5. What's your budget range?
6. What's your target launch date?

### Functional Requirements Questions
7. What are the MUST-HAVE features for MVP?
8. What features can be Phase 2?
9. What user roles/permissions do you need?
10. What are the critical user workflows?
11. What reporting/analytics do you need?
12. What notifications/alerts are required?

### Technical Requirements Questions
13. Do you have existing systems to integrate with?
14. What's your preferred tech stack? (or open to recommendations)
15. Do you have compliance requirements? (GDPR, HIPAA, SOC2)
16. What's your expected user load? (concurrent users)
17. What are your performance requirements?
18. Do you have existing data to migrate?

### Integration & Dependencies Questions
19. What third-party services must integrate? (payment, email, etc.)
20. Do you have API documentation for existing systems?
21. What authentication method? (OAuth, SSO, custom)
22. What payment gateways? (Stripe, PayPal, etc.)

### Timeline & Delivery Questions
23. What are your key milestone dates?
24. Are there any hard deadlines? (events, launches)
25. What's your preferred payment schedule?
26. How often do you want progress updates?

### Communication & Governance Questions
27. Who are the key decision makers?
28. What's your preferred communication tool? (Slack, email, etc.)
29. What's your availability for meetings? (timezone, schedule)
30. How do you want to handle scope changes?

---

## PART 2: DISCOVERY CHECKLIST

### Pre-Meeting Preparation
- [ ] Review accepted proposal (PROPOSAL.md)
- [ ] Review client reply/acceptance
- [ ] Prepare question bank (30 questions ready)
- [ ] Prepare note-taking template
- [ ] Setup recording/transcript tool (if applicable)
- [ ] Review similar projects for reference

### During Discovery Session
- [ ] Record client answers to all 30 questions
- [ ] Capture exact quotes for critical requirements
- [ ] Note any concerns or red flags
- [ ] Identify missing information
- [ ] Document assumptions made
- [ ] Get clarity on priorities (MoSCoW)

### Post-Meeting Actions
- [ ] Transcribe notes to structured artifacts
- [ ] Fill out client-discovery-form.md
- [ ] Complete scope-clarification.md
- [ ] Document timeline-discussion.md
- [ ] Create communication-plan.md
- [ ] Build risk-log.md
- [ ] Draft discovery-recap.md
- [ ] Send recap to client for approval

---

## PART 3: ARTIFACT TEMPLATES

### Template: client-discovery-form.md
```markdown
# Client Discovery Form

## MVP Features (MUST HAVE)
Based on client priority:
1. [Feature 1] - [Why critical]
2. [Feature 2] - [Why critical]
3. [Feature 3] - [Why critical]

## Phase 2 Features (SHOULD HAVE)
1. [Feature] - [Value but not blocking]
2. [Feature] - [Value but not blocking]

## Phase 3 Features (COULD HAVE)
1. [Feature] - [Nice to have]

## User Roles
1. [Role] - [Permissions]
2. [Role] - [Permissions]

## Critical Workflows
1. [Workflow name] - [Steps]
2. [Workflow name] - [Steps]
```

### Template: scope-clarification.md
```markdown
# Scope Clarification

## Tech Stack (Confirmed)
- Backend: [Technology]
- Frontend: [Technology]
- Database: [Technology]
- Hosting: [Platform]
- CI/CD: [Tool]

## Integrations Required
1. [Service] - [Purpose] - [API available: Y/N]
2. [Service] - [Purpose] - [API available: Y/N]

## Compliance Requirements
- [ ] GDPR (EU data)
- [ ] HIPAA (Health data)
- [ ] SOC2 (Enterprise)
- [ ] PCI-DSS (Payments)
- [ ] Other: [Specify]

## Performance Requirements
- Expected users: [Number]
- Concurrent users: [Number]
- Response time: < [X] seconds
- Uptime: [X]%

## Security Requirements
- Authentication: [Method]
- Authorization: [RBAC/ABAC]
- Data encryption: [At rest/In transit]
- Audit logging: [Y/N]
```

### Template: timeline-discussion.md
```markdown
# Timeline Discussion

## Project Phases
### Phase 1: Foundation (Week 1-2)
- Deliverables: [List]
- Milestone: [Name]
- Budget: $[Amount]

### Phase 2: Core Development (Week 3-6)
- Deliverables: [List]
- Milestone: [Name]
- Budget: $[Amount]

### Phase 3: Testing & Launch (Week 7-8)
- Deliverables: [List]
- Milestone: [Name]
- Budget: $[Amount]

## Key Dates
- Project Start: [Date]
- MVP Delivery: [Date]
- Production Launch: [Date]
- Final Handoff: [Date]

## Payment Schedule
- Upfront: [%] - $[Amount]
- Milestone 1: [%] - $[Amount]
- Milestone 2: [%] - $[Amount]
- Final: [%] - $[Amount]
```

### Template: communication-plan.md
```markdown
# Communication Plan

## Regular Meetings
- Daily Standups: [Time] via [Tool] (async/sync)
- Weekly Progress: [Day/Time] via [Tool]
- Sprint Planning: [Frequency] via [Tool]

## Communication Channels
- Urgent: [Tool/Channel] - Response: < 2 hours
- Technical: [Tool/Channel] - Response: < 4 hours
- General: [Tool/Channel] - Response: < 24 hours

## Stakeholders
1. [Name] - [Role] - [Email] - [Decision authority]
2. [Name] - [Role] - [Email] - [Decision authority]

## Escalation Path
- Level 1: [Person] - [Type of issues]
- Level 2: [Person] - [Type of issues]
- Level 3: [Person] - [Type of issues]

## Timezone
- Client: [Timezone]
- Team: [Timezone]
- Overlap hours: [Hours]
```

### Template: risk-log.md
```markdown
# Risk Log

## High Priority Risks
### Risk 1: [Name]
- Impact: [High/Medium/Low]
- Probability: [%]
- Mitigation: [Strategy]
- Owner: [Person]

## Medium Priority Risks
### Risk 2: [Name]
- Impact: [High/Medium/Low]
- Probability: [%]
- Mitigation: [Strategy]
- Owner: [Person]

## Assumptions
1. [Assumption] - Risk if false: [Impact]
2. [Assumption] - Risk if false: [Impact]

## Dependencies
1. [Dependency] - Owner: [Person] - Due: [Date]
2. [Dependency] - Owner: [Person] - Due: [Date]

## Open Questions
1. [Question] - Priority: [High/Medium/Low] - Blocking: [Y/N]
2. [Question] - Priority: [High/Medium/Low] - Blocking: [Y/N]
```

---

## PART 4: AI ORCHESTRATION WORKFLOW

### Step 1: Pre-Client Preparation (AI-Driven)
```bash
# Generate question bank from proposal
python scripts/generate_discovery_questions.py \
  --proposal .artifacts/protocol-01/PROPOSAL.md \
  --output .artifacts/protocol-02/question-bank.md

# Analyze job post for domain-specific questions
python scripts/analyze_domain.py \
  --jobpost JOB-POST.md \
  --output .artifacts/protocol-02/domain-questions.md

# Prepare meeting agenda
python scripts/generate_meeting_agenda.py \
  --questions .artifacts/protocol-02/question-bank.md \
  --output .artifacts/protocol-02/meeting-agenda.md
```

### Step 2: During Client Meeting
```markdown
## AI Assistant Role
- Present questions systematically
- Capture responses in real-time
- Flag missing information
- Suggest follow-up questions
- Note client priorities
- Identify risks/concerns
```

### Step 3: Post-Meeting Processing (AI-Driven)
```bash
# Transcribe meeting notes to structured artifacts
python scripts/process_discovery_notes.py \
  --notes .artifacts/protocol-02/meeting-notes.md \
  --output-dir .artifacts/protocol-02/

# Validate completeness
python scripts/validate_discovery_completeness.py \
  --artifacts .artifacts/protocol-02/ \
  --report .artifacts/protocol-02/completeness-report.json

# Generate discovery recap
python scripts/generate_discovery_recap.py \
  --artifacts .artifacts/protocol-02/ \
  --output .artifacts/protocol-02/discovery-recap.md
```

### Step 4: Client Approval
```bash
# Send recap to client
# Wait for approval
# Update completion manifest
python scripts/mark_protocol_complete.py --protocol 02
```

---

## PART 5: VALIDATION CHECKLIST

### Before Client Meeting
- [ ] 30 discovery questions prepared
- [ ] Meeting agenda created
- [ ] Note-taking template ready
- [ ] Recording tool setup (if needed)
- [ ] Proposal reviewed
- [ ] Similar projects reviewed

### After Client Meeting
- [ ] All 30 questions answered (or marked as pending)
- [ ] client-discovery-form.md completed
- [ ] scope-clarification.md completed
- [ ] timeline-discussion.md completed
- [ ] communication-plan.md completed
- [ ] risk-log.md completed
- [ ] discovery-recap.md drafted
- [ ] Client approval received

### Quality Gates
- [ ] Gate 1: Objective Alignment (95% coverage)
- [ ] Gate 2: Requirement Completeness (90% score)
- [ ] Gate 3: Expectation Alignment (client approved)
- [ ] Gate 4: Discovery Confirmation (recap approved)

---

## PART 6: SCRIPTS TO CREATE

### Priority 1: Essential Scripts
1. `generate_discovery_questions.py` - Auto-generate questions from proposal
2. `process_discovery_notes.py` - Convert notes to structured artifacts
3. `validate_discovery_completeness.py` - Check if all info captured
4. `generate_discovery_recap.py` - Auto-generate client-facing summary

### Priority 2: Enhancement Scripts
5. `analyze_domain.py` - Domain-specific question suggestions
6. `generate_meeting_agenda.py` - Structured meeting flow
7. `identify_risks.py` - Auto-detect risks from requirements
8. `estimate_timeline.py` - Suggest timeline based on scope

### Priority 3: Validation Scripts
9. `validate_discovery_objectives.py` - Gate 1 validation
10. `validate_discovery_scope.py` - Gate 2 validation
11. `validate_discovery_expectations.py` - Gate 3 validation
12. `check_client_confirmation.py` - Gate 4 validation

---

## PART 7: EXAMPLE WORKFLOW

### Scenario: Upwork Appointment Booking Project

#### 1. Pre-Meeting (AI Preparation)
```bash
# Review proposal
cat .artifacts/protocol-01/PROPOSAL.md

# Generate questions
python scripts/generate_discovery_questions.py

# Output: 30 questions ready
✅ Business questions (6)
✅ Functional questions (6)
✅ Technical questions (6)
✅ Integration questions (4)
✅ Timeline questions (5)
✅ Governance questions (3)
```

#### 2. Client Meeting
```markdown
AI: "Let's go through discovery questions systematically"

Q1: What specific problem are you solving?
Client: "Patients miss appointments, we lose revenue"

Q7: What are MUST-HAVE features for MVP?
Client: "Booking, payment, email reminders"

Q13: Existing systems to integrate?
Client: "Our clinic management system has an API"

[Continue through all 30 questions]
```

#### 3. Post-Meeting (AI Processing)
```bash
# Process notes
python scripts/process_discovery_notes.py
✅ Created client-discovery-form.md
✅ Created scope-clarification.md
✅ Created timeline-discussion.md
✅ Created communication-plan.md
✅ Created risk-log.md

# Validate completeness
python scripts/validate_discovery_completeness.py
✅ 28/30 questions answered (93%)
⚠️ 2 questions pending client follow-up

# Generate recap
python scripts/generate_discovery_recap.py
✅ Created discovery-recap.md
```

#### 4. Client Approval
```markdown
Email to client:
"Here's our discovery summary. Please review and approve."

Client response:
"Looks good\! Approved. Let's proceed."

✅ Protocol 02 COMPLETE
✅ Ready for Protocol 03
```

---

## NEXT ACTIONS FOR YOU

### Immediate (Today)
1. Create discovery question bank (30 questions)
2. Create artifact templates (5 templates)
3. Prepare meeting agenda template

### Short-term (This Week)
4. Create `generate_discovery_questions.py`
5. Create `process_discovery_notes.py`
6. Create `validate_discovery_completeness.py`
7. Create `generate_discovery_recap.py`

### Medium-term (Next Week)
8. Create remaining validation scripts
9. Test full discovery workflow
10. Document AI orchestration process

---

## SUCCESS CRITERIA

✅ **Pre-Meeting**: 30 questions ready, templates prepared  
✅ **During Meeting**: All questions asked, responses captured  
✅ **Post-Meeting**: All artifacts completed, validated  
✅ **Client Approval**: Recap approved, ready for Protocol 03  

**Result**: Complete, structured discovery na AI-orchestrated\! 🚀

# Teleprompter Mode - Planning Notes

**Date:** 2025-11-09
**Purpose:** Discovery Call Assistant - Cascade provides questions and answers during live client discovery calls

---

## ✅ CORE ASSUMPTION

**ALL INPUT = CLIENT SPEAKING**
- No explanation needed on how/why
- Just assume: Whatever appears in chat = Client said it
- Cascade responds accordingly

---

## ✅ RESPONSE REQUIREMENTS

- ✅ SHORT, ready-to-read responses (2-4 sentences max)
- ✅ NATURAL conversational English
- ✅ NO meta-commentary ("let me check artifacts...")
- ✅ NO file references (".artifacts/protocol-06/...")
- ✅ DIRECT responses only - ready to read verbatim

---

## ✅ ARTIFACT REQUIREMENTS

**[STRICT]** ALL artifacts must be loaded BEFORE mode starts.

**Protocol 01 Artifacts** (Client Proposal Generation):
```
.artifacts/protocol-01/
├── notes.md                    # Working notes with timestamps
├── job-post.md                 # Copy of original job post
├── jobpost-analysis.json       # Extracted job post details
│   ├── exact_quotes[]
│   ├── tech_stack[]
│   ├── pain_points[]
│   ├── tone_type
│   ├── urgency_signals[]
│   └── vague_requirements[]
├── tone-map.json               # Tone analysis (formal/casual/technical)
├── humanization-log.json       # Proposal writing strategy
├── pricing-analysis.json       # Pricing strategy and assumptions
├── PROPOSAL.md                 # Final proposal sent to client
└── proposal-summary.json       # Differentiators, pricing, next steps
```

**Protocol 02 Artifacts** (Client Discovery Initiation):
```
.artifacts/protocol-02/
├── client-reply.md             # Client's response to proposal (optional)
├── discovery-brief.md          # Business goals, users, metrics, constraints
├── assumptions-gaps.md         # Assumptions tracker with validation status
├── risk-opportunity-list.md    # Risks, blockers, opportunities
├── question-bank.md            # Prioritized discovery questions (P0/P1/P2)
├── integration-inventory.md    # Systems, owners, data, risks
├── scenario-guides.md          # Pivot scenarios and responses
├── call-agenda.md              # Meeting structure and timing
├── discovery-call-notes.md     # Live notes template
├── ready-for-call-summary.md   # Pre-call readiness checklist
├── client-discovery-form.md    # Post-call feature requirements
├── scope-clarification.md      # Technical scope updates
├── timeline-discussion.md      # Milestones, dependencies, budget
└── collaboration-plan.md       # Communication and workflow agreements
```

**Cascade must understand:**
- Business Context: Client goals, pain points, success metrics
- Technical Stack: Proposed technologies, integrations, constraints
- Pricing Strategy: Rates, milestones, budget assumptions
- Risks & Assumptions: Known blockers, validation status
- Discovery Insights: Client preferences, priorities, timeline

---

## 🎯 CASCADE'S ROLE DURING DISCOVERY CALL

### **MODE 1: DISCOVERY DRIVER** (Proactive)
Generate QUESTIONS for user to ask client

**Question Sources:**
- `question-bank.md` (P0/P1/P2 prioritized)
- `assumptions-gaps.md` (ASK CLIENT items)
- `integration-inventory.md` (@ASK_CLIENT tags)

**Capabilities:**
- Decide question priority and flow
- Generate dynamic follow-ups based on client responses
- Track what's been answered
- Skip redundant questions

### **MODE 2: ANSWER PROVIDER** (Reactive)
Generate ANSWERS when client asks questions

**Answer Sources:**
- Protocol 01 artifacts (PROPOSAL.md, pricing-analysis.json)
- Protocol 02 artifacts (discovery-brief.md, scope-clarification.md)

**Output:**
- Short, natural, conversational responses
- Ready to read verbatim

### **WHAT CASCADE DOES NOT DO:**
❌ No silent logging during call
❌ No file editing during call
❌ No background artifact updates during call

**Why?**
- Everything recorded in conversation history
- Extract after call → Update artifacts

---

## 📋 QUESTION GENERATION STRATEGY

### **Question Sources (Priority Order):**

1. **P0 Questions (Must-Ask - Blocking)**
   - From `question-bank.md` marked P0
   - Critical for Protocol 03 handoff
   - Example: "What features are critical for MVP?"

2. **@ASK_CLIENT Tags (Critical Dependencies)**
   - From `integration-inventory.md`
   - System owners, API access, data requirements
   - Example: "Who owns the HR API and can provide access?"

3. **Assumption Validation (Confirmation)**
   - From `assumptions-gaps.md` marked "ASK CLIENT"
   - Things assumed in proposal needing confirmation
   - Example: "I assumed mobile support needed - correct?"

4. **P1/P2 Questions (Optimization)**
   - From `question-bank.md` marked P1/P2
   - Clarifying and optimization questions
   - Example: "What's your preferred testing approach?"

### **Dynamic Question Generation:**

**Follow-up Logic:**
- If client mentions new requirement → Ask clarifying question
- If client's answer conflicts with proposal → Ask to resolve
- If client's answer creates dependency → Ask about it
- If client gives incomplete answer → Ask for specifics

**Example Flow:**
```
CLIENT: "We need Stripe integration"
CASCADE: "Got it. Do you already have a Stripe account, 
          or should I include setup in the timeline?"

CLIENT: "We have an account already"
CASCADE: "Perfect. Can you provide the API keys, or should 
          I coordinate with someone on your team?"
```

### **Conversation Flow Control:**

**Intelligent Sequencing:**
- Start with business/scope questions (P0)
- Move to technical/integration questions
- End with logistics/communication questions
- Allow natural conversation flow (not rigid order)

**Context Awareness:**
- Track what's been answered
- Skip redundant questions
- Adjust priority based on client's responses
- Recognize when client volunteers information

---

## 🎯 COMPLETE EXAMPLE FLOW

### **Call Start:**

```
CASCADE (opening):
"Good day! Thanks for joining. Based on our proposal discussion, 
I'd like to clarify key points to ensure we're aligned.

First, regarding your MVP scope - can you confirm which features 
are absolutely critical for your initial launch?"

[Source: question-bank.md P0 #1]
```

### **Client Responds:**

```
INPUT: "We need recording, playback, and PDF reports. AI can come later."

CASCADE (acknowledges + next question):
"Perfect! So MVP focuses on recording, playback, and PDF reports, 
with AI features in phase 2. That helps me scope the timeline.

What's your target launch date for this MVP?"

[Source: question-bank.md P0 #2]
```

### **Client Asks Question:**

```
INPUT: "What's your experience with real-time audio?"

CASCADE (answers from artifacts):
"I have 5+ years with real-time audio systems. I've implemented 
Deepgram integration before and achieved sub-500ms latency in 
production. I'm confident I can meet your requirements."

[Source: PROPOSAL.md experience section]

[Then resumes discovery]:
"Now, regarding the HR system integration you mentioned - who 
should I coordinate with for API access?"

[Source: integration-inventory.md @ASK_CLIENT tag]
```

### **Call Continues:**

```
- All P0 questions asked and answered
- All @ASK_CLIENT tags addressed
- All assumptions validated
- Client questions answered
- Everything captured in conversation history
```

### **Call End:**

```
CASCADE (wrap-up):
"Thank you! Let me summarize what we confirmed:
- MVP: Recording, playback, PDF reports
- Timeline: Q1 2025 end
- Integrations: HR system (Sarah), Stripe (existing account)
- Budget: $15k confirmed

I'll send a detailed recap within 24 hours. Sound good?"
```

---

## 🎯 POST-CALL PROCESS

**After call ends:**

1. Review conversation history (all client inputs and responses recorded)
2. Extract all confirmed details
3. Update Protocol 02 Phase 4 artifacts:
   - `client-discovery-form.md` - Add confirmed features
   - `scope-clarification.md` - Finalize tech stack
   - `integration-inventory.md` - Resolve @ASK_CLIENT tags
   - `timeline-discussion.md` - Add agreed milestones
   - `communication-plan.md` - Document collaboration workflow
   - `discovery-recap.md` - Create client-facing summary
4. Validate completeness (all questions answered, gaps filled)
5. Ready for Protocol 03 (Project Brief Creation)

---

## 📊 REAL-WORLD DISCOVERY CALL PRACTICES

### **Industry Standard (Upwork/Freelance):**

**Call Duration:** 10-20 minutes (not 1 hour)

**Structure (5 Parts):**
1. **Goal** (2-3 min) - "What would make this project a win?"
2. **Current State & Constraints** (3-5 min) - "Any non-negotiables?"
3. **Risks & Unknowns** (2-3 min) - "Top two risks to avoid?"
4. **First Slice Proposal** (3-5 min) - "Done = {criteria}"
5. **Options & Close** (2-3 min) - "I'll send milestone today"

**Key Pattern:**
- Developer DRIVES conversation with structured questions
- Focus on OUTCOMES ("Done = {criteria}")
- Immediate post-call summary (same hour)
- Clear next steps (milestone proposal)

**Example Questions:**
- "What would make this project a win in plain language?"
- "If we only shipped one thing next week, what should it be?"
- "Where is this today? {repo/CMS/stack/data}"
- "Any non-negotiables (stack, design system, compliance)?"
- "Top two risks you want avoided?"
- "Any third-party blockers or approvals?"

**Call-Ending Line:**
"I'll summarize in Upwork messages with Milestone 1: Done = {criteria}, price, and date. Anything I missed?"

**Post-Call (Same Hour):**
```
Great call—here's the summary:
• Goal: {client words}
• Risks to avoid: {list}
• Milestone 1 ({days} days): {deliverables} — Done = {criteria} (${amount})
• Start: {date} | Update day: {weekday}
I'll send the proposal now for approval.
```

---

## 🗣️ HUMAN CONVERSATION RULES

### **CRITICAL: Sound Like a HUMAN DEVELOPER, Not AI**

**NEVER say technical workflow terms:**
❌ "I use 28 protocols"
❌ "Protocol 01, Protocol 02"
❌ "Quality gates and validation scripts"
❌ "Evidence artifacts and manifests"
❌ "question-bank.md and assumptions-gaps.md"

**ALWAYS explain the LOGIC and BENEFITS:**
✅ "I follow a structured approach"
✅ "I make sure I understand your needs first"
✅ "I test everything before delivery"
✅ "You'll get regular updates"
✅ "No surprises - everything documented"

---

### **Translation Guide: Technical → Human**

| Technical Term | Human Explanation |
|----------------|-------------------|
| "Protocol 01" | "proposal phase" or "initial planning" |
| "Protocol 02" | "discovery call" or "requirements gathering" |
| "Protocol 03" | "project planning" or "creating the roadmap" |
| "Quality gates" | "testing checkpoints" or "quality checks" |
| "Evidence artifacts" | "documentation and deliverables" |
| "28 protocols" | "structured process from start to finish" |
| "Validation scripts" | "automated testing" |
| "question-bank.md" | "list of important questions" |
| "assumptions-gaps.md" | "things we need to clarify" |
| "integration-inventory.md" | "systems we need to connect" |

---

### **Example Responses (Human Style)**

**Q: "What's your development process?"**

✅ "I follow a structured approach. First, I make sure I really understand what you need through a discovery call. Then I create a clear project plan with milestones so you know exactly what to expect. During development, I keep you updated regularly and make sure everything is tested before delivery. At the end, you get complete documentation and support."

---

**Q: "How do you ensure quality?"**

✅ "I test everything thoroughly before showing it to you. I also do code reviews and make sure the app works on different devices. You'll see working demos at each milestone, so if something's not right, we catch it early. No surprises at the end."

---

**Q: "How do you handle requirements?"**

✅ "I start by asking detailed questions about your goals and constraints. I document everything we discuss and send you a summary to make sure we're aligned. If anything's unclear, I ask before starting work - this way there are no misunderstandings later."

---

**Q: "What makes you different from other developers?"**

✅ "I'm very organized and systematic. You'll always know what's happening with your project - clear milestones, regular updates, and everything documented. I also make sure to understand your business goals, not just the technical requirements. This means the solution actually solves your problem, not just checks boxes."

---

**Q: "How do you manage timelines?"**

✅ "I break the project into smaller milestones with clear deliverables. You'll see progress every week, not just at the end. If something takes longer than expected, I let you know immediately with options to adjust. No last-minute surprises."

---

**Q: "What happens after you deliver?"**

✅ "You get complete documentation, source code, and a handover session where I walk you through everything. I also provide support for any questions or issues. Everything is organized so another developer can easily understand the code if needed."

---

**Q: "How do you handle changes during development?"**

✅ "Changes happen - I get it. When you need something different, I'll explain how it affects timeline and budget, then we decide together. Everything stays documented so we're always on the same page."

---

**Q: "Do you work with a team?"**

✅ "I'm a solo developer, which means you work directly with me - no middlemen. I handle everything from planning to deployment. This keeps communication clear and costs lower."

---

### **Key Principles:**

1. **Focus on BENEFITS, not PROCESS**
   - "You'll know exactly what to expect" (not "I use Protocol 06")
   - "No surprises" (not "I have quality gates")
   - "Regular updates" (not "I execute validation scripts")

2. **Use SIMPLE LANGUAGE**
   - "testing" not "validation"
   - "planning" not "protocol execution"
   - "documentation" not "evidence artifacts"

3. **Be CONVERSATIONAL**
   - "I make sure..." not "The protocol requires..."
   - "You'll get..." not "Artifacts include..."
   - "We'll discuss..." not "Discovery phase initiates..."

4. **Show EMPATHY**
   - "I understand changes happen"
   - "I know timelines are important"
   - "I want to make sure you're happy"

---

**Status:** ✅ Complete Understanding - Ready for Implementation

# Teleprompter Mode - Reasoning Framework

**Date:** 2025-11-09
**Purpose:** How Cascade understands client questions and generates reasoning-based responses

---

## 🧠 CORE REASONING PRINCIPLE

**NO KEYWORD MATCHING - USE REASONING INSTEAD**

### **WRONG Approach:**
```
IF question contains "development process" THEN
  return canned_response_1
IF question contains "quality" THEN
  return canned_response_2
```

### **CORRECT Approach:**
```
1. ANALYZE: What is client really asking?
2. UNDERSTAND: Why are they asking this?
3. CONTEXT: What do they care about?
4. REASON: What knowledge do I have that addresses this?
5. GENERATE: Create response based on logic
```

---

## 📊 REASONING PROCESS (5 STEPS)

### **STEP 1: ANALYZE THE QUESTION**

**Ask yourself:**
- What is the literal question?
- What is the REAL question behind it?
- What concern does this reveal?

**Example:**
```
CLIENT: "What's your development process?"

ANALYSIS:
- Literal: They want to know my workflow
- Real question: "Are you organized and reliable?"
- Concern: They're worried about chaos/delays
```

---

### **STEP 2: UNDERSTAND THE INTENT**

**Common intents behind questions:**

| Question Type | Real Intent | What They Care About |
|--------------|-------------|---------------------|
| "What's your process?" | "Are you organized?" | Predictability, no chaos |
| "How do you ensure quality?" | "Will this work properly?" | Reliability, no bugs |
| "How do you handle changes?" | "Are you flexible?" | Adaptability, no rigidity |
| "What's your timeline?" | "Can you deliver on time?" | Deadlines, no delays |
| "How do you communicate?" | "Will I know what's happening?" | Transparency, updates |
| "What makes you different?" | "Why should I hire you?" | Unique value, trust |
| "Do you work with a team?" | "Who am I dealing with?" | Accountability, clarity |
| "What happens after delivery?" | "Will you abandon me?" | Support, handoff |

---

### **STEP 3: CHECK CONTEXT**

**What context is relevant?**

**From Artifacts:**
- What did I propose? (PROPOSAL.md)
- What's the project about? (job-post.md)
- What are the constraints? (assumptions-gaps.md)
- What systems involved? (integration-inventory.md)
- What's the timeline? (timeline-discussion.md)

**From Conversation:**
- What have we discussed already?
- What concerns have they expressed?
- What's their tone? (worried, excited, skeptical)

**From Industry Standards:**
- What do Upwork clients typically care about?
- What are common pain points?
- What differentiates good vs bad freelancers?

---

### **STEP 4: REASON ABOUT THE ANSWER**

**Connect the dots:**

```
QUESTION INTENT + MY KNOWLEDGE + THEIR CONTEXT = ANSWER
```

**Example:**
```
INTENT: "Are you organized?"
MY KNOWLEDGE: I have 28-protocol workflow with clear phases
THEIR CONTEXT: They need realtime-interview app in 12 weeks
REASONING: They need to know I won't waste time or miss deadlines

ANSWER SHOULD:
- Show I'm organized (without saying "28 protocols")
- Give them confidence (clear milestones)
- Address their timeline (12 weeks is doable)
- Focus on THEIR benefit (predictability)
```

---

### **STEP 5: GENERATE RESPONSE**

**Response Formula:**

```
ACKNOWLEDGE + EXPLAIN BENEFIT + PROVIDE EVIDENCE + NEXT STEP
```

**Example:**
```
ACKNOWLEDGE: "I follow a structured approach"
EXPLAIN BENEFIT: "so you know exactly what to expect and when"
PROVIDE EVIDENCE: "We'll have clear milestones - you'll see progress every week"
NEXT STEP: "For your 12-week timeline, I'd break it into 2-week sprints"
```

---

## 💡 REASONING EXAMPLES

### **Example 1: Process Question**

**CLIENT:** "What's your development process?"

**STEP 1 - ANALYZE:**
- Real question: "Are you organized and reliable?"
- Concern: Previous developers were chaotic

**STEP 2 - UNDERSTAND INTENT:**
- They want: Predictability, clear communication, no surprises
- They fear: Missed deadlines, scope creep, poor quality

**STEP 3 - CHECK CONTEXT:**
- From PROPOSAL.md: I proposed structured delivery
- From job-post.md: They need realtime-interview app
- From timeline: 12 weeks deadline
- Industry standard: Upwork clients value transparency

**STEP 4 - REASON:**
- I have: Protocol 01-28 (structured workflow)
- They need: Confidence I won't waste time
- Translation: "28 protocols" → "structured approach with milestones"
- Focus: What THEY get (visibility, predictability)

**STEP 5 - GENERATE:**
"I follow a structured approach. First, I make sure I really understand what you need through a detailed discussion. Then I create a clear plan with milestones so you know exactly what to expect. For your 12-week timeline, I'd break it into 2-week sprints - you'll see working demos regularly, not just at the end. This way, if something needs adjustment, we catch it early."

---

### **Example 2: Quality Question**

**CLIENT:** "How do you ensure quality?"

**STEP 1 - ANALYZE:**
- Real question: "Will this actually work?"
- Concern: They've had buggy software before

**STEP 2 - UNDERSTAND INTENT:**
- They want: Confidence it will work properly
- They fear: Bugs, crashes, poor user experience

**STEP 3 - CHECK CONTEXT:**
- From job-post.md: Realtime audio processing (critical functionality)
- From PROPOSAL.md: I mentioned Deepgram integration
- Industry standard: Audio apps need thorough testing

**STEP 4 - REASON:**
- I have: Quality gates at Protocol 10, 11, 12
- They need: Assurance of reliability
- Translation: "Quality gates" → "thorough testing before delivery"
- Focus: What THEY get (working product, no surprises)

**STEP 5 - GENERATE:**
"I test everything thoroughly before showing it to you. For the audio processing, I'll test on different devices and network conditions to make sure it's reliable. You'll see working demos at each milestone - if something's not right, we catch it early and fix it. No surprises at the end."

---

### **Example 3: Change Management Question**

**CLIENT:** "What if we need to change requirements?"

**STEP 1 - ANALYZE:**
- Real question: "Are you flexible or rigid?"
- Concern: They might need to adjust scope

**STEP 2 - UNDERSTAND INTENT:**
- They want: Flexibility + transparency about impact
- They fear: Being locked in, hidden costs

**STEP 3 - CHECK CONTEXT:**
- From PROPOSAL.md: Fixed price with milestones
- Industry standard: Changes affect timeline/budget
- My knowledge: Protocol 08b (Change Management)

**STEP 4 - REASON:**
- I have: Formal change process (Protocol 08b)
- They need: Flexibility without chaos
- Translation: "Change protocol" → "transparent impact analysis"
- Focus: What THEY get (control, no surprises)

**STEP 5 - GENERATE:**
"Changes are normal - I understand requirements evolve. When you need something different, I'll explain how it affects the timeline and budget, then we decide together what makes sense. Everything stays documented so we're always aligned. The key is communication - no hidden costs or surprises."

---

## 🎯 ADAPTATION BASED ON CONTEXT

### **Same Question, Different Contexts:**

**Question:** "How long will this take?"

**CONTEXT A: Client is relaxed, exploratory**
```
REASONING: They're just curious, not stressed
ANSWER: "Based on the features we discussed, I estimate 10-16 days for the core functionality. We can break it into phases if you want to launch sooner with fewer features."
```

**CONTEXT B: Client mentioned urgent deadline**
```
REASONING: They're under time pressure
ANSWER: "I can start immediately. For your Q1 deadline, I'd recommend focusing on the must-have features first - recording, playback, and basic reports. We can add the AI integration in phase 2. This way you launch on time."
```

**CONTEXT C: Client seems budget-conscious**
```
REASONING: They're worried about cost
ANSWER: "I estimate 10-16 days for the MVP. To keep costs predictable, I'd propose fixed-price milestones - you approve each phase before we continue. No surprises on the bill."
```

---

## 🔄 DYNAMIC FOLLOW-UP REASONING

### **When Client Gives Partial Information:**

**CLIENT:** "We need Stripe integration"

**REASONING:**
- They mentioned Stripe (specific requirement)
- But didn't say: Do they have account? Who has access? Timeline impact?
- I should: Ask clarifying question to avoid assumptions

**RESPONSE:**
"Got it. Do you already have a Stripe account set up, or should I include that in the timeline? Also, who on your team can provide the API keys when we're ready to integrate?"

---

### **When Client Reveals New Concern:**

**CLIENT:** "We had a bad experience with a developer before..."

**REASONING:**
- They're expressing past pain
- This reveals: Trust issues, fear of repeat
- I should: Acknowledge, show how I'm different

**RESPONSE:**
"I understand - that's frustrating. Can you tell me what went wrong? This helps me make sure we avoid those issues. In my experience, most problems come from poor communication or unclear expectations. That's why I document everything and keep you updated regularly - no guessing games."

---

## 📋 KNOWLEDGE SOURCES FOR REASONING

### **What I Know (From Artifacts):**

**From Protocol 01:**
- My proposal content (PROPOSAL.md)
- My pricing strategy (pricing-analysis.json)
- Client's original job post (job-post.md)
- My differentiators (proposal-summary.json)

**From Protocol 02:**
- Business goals (discovery-brief.md)
- Assumptions to validate (assumptions-gaps.md)
- Questions to ask (question-bank.md)
- Systems to integrate (integration-inventory.md)
- Risks identified (risk-opportunity-list.md)

**From Industry Knowledge:**
- Upwork discovery call best practices
- Common client concerns
- Standard freelancer pain points
- Professional communication patterns

**From Conversation History:**
- What we've discussed
- Client's tone and concerns
- Questions they've asked
- Information they've volunteered

---

## ⚠️ ANTI-PATTERNS TO AVOID

### **DON'T:**

❌ **Match keywords and return canned responses**
```
BAD: IF "process" in question THEN return template_1
```

❌ **Ignore context**
```
BAD: Same answer regardless of client's situation
```

❌ **Use technical jargon**
```
BAD: "I execute Protocol 06 with quality gates"
```

❌ **Be vague**
```
BAD: "I follow best practices"
```

❌ **Over-promise**
```
BAD: "I guarantee zero bugs"
```

### **DO:**

✅ **Reason about intent**
```
GOOD: Understand WHY they're asking
```

✅ **Adapt to context**
```
GOOD: Different answers for different situations
```

✅ **Use human language**
```
GOOD: "I test everything thoroughly"
```

✅ **Be specific**
```
GOOD: "You'll see working demos every 2 weeks"
```

✅ **Be honest**
```
GOOD: "I'll catch most bugs, but we'll fix any that slip through"
```

---

## 🎯 SUMMARY: HOW TO RESPOND

**Every response should:**

1. **Understand the REAL question** (not just literal words)
2. **Check relevant CONTEXT** (artifacts, conversation, industry)
3. **Reason about ANSWER** (connect knowledge to their need)
4. **Generate HUMAN response** (benefits, not process)
5. **Adapt to SITUATION** (different clients, different answers)

**NOT:**
- Keyword matching
- Canned responses
- Ignoring context
- Technical jargon
- One-size-fits-all

---

**This is KNOWLEDGE, not implementation. The actual rule will use this reasoning framework.**

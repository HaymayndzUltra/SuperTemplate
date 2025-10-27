# Client Proposal Generation System

## Context
You are writing a technical proposal in response to a client's job post. Your goal is to demonstrate understanding of their requirements and present a clear approach.

---

## Required Inputs
Provide exactly these items:
1. **Client's job post**: [Paste exact text]
2. **Your capabilities**: [List specific technologies/services you offer]
3. **Target length**: [Specify word count, e.g., 300-500 words]
4. **Client domain**: [e.g., e-commerce, fintech, healthcare, or "unknown"]

---

## Writing Rules

### Rule 1: Problem-First Opening
- **First sentence must reference the client's stated problem or goal**
- Do NOT start with your credentials or experience
- Example: "Your requirement for real-time inventory sync suggests you're experiencing oversell issues during peak traffic."

### Rule 2: Translate Vague Requirements
For each vague client statement, provide ONE specific technical interpretation:
- Client: "needs to scale" → You: "I interpret this as handling 10x current traffic via horizontal pod autoscaling"
- Client: "modern UI" → You: "I interpret this as WCAG 2.1 AA compliance with mobile-first responsive design"
- **Always prefix with "I interpret this as..." to show it's your understanding, not fact**

### Rule 3: Collaborative Language
- Use "we" when describing joint activities: "We'll establish...", "We can architect..."
- Use "I" only for your specific deliverables: "I will deliver...", "I have experience with..."
- Aim for collaborative tone without forcing artificial percentages

### Rule 4: Show One Detailed Example
- Provide ONE specific approach with technical details
- Example: "For the authentication system, I'd implement JWT tokens with refresh rotation, Redis session storage, and rate-limiting at 100 req/min per IP."
- Optionally mention alternatives exist: "This is one of several approaches we'd evaluate based on your traffic patterns."

### Rule 5: Structured Paragraphs
Each paragraph should follow this pattern:
1. **Opening claim** (1 sentence): State your point
2. **Supporting detail** (1-2 sentences): Provide technical specificity or evidence
3. **Implication** (1 sentence): Connect to client benefit or next step

### Rule 6: Verifiable Statements Only
- ❌ Avoid: "best quality", "fast delivery", "highly scalable"
- ✅ Use: "test coverage >80%", "2-week delivery", "handles 10K concurrent users"
- If you cannot quantify, don't claim it

---

## Output Structure

**[OPENING]** (1-2 sentences addressing client's stated problem)

**[REQUIREMENT INTERPRETATION]** (2-3 paragraphs translating client's vague needs into specific technical decisions. Use "I interpret X as Y" format to show these are interpretations.)

**[PROPOSED APPROACH]** (1 detailed technical example showing your methodology. Optionally reference that alternatives exist.)

**[NEXT STEPS]** (2-3 sentences describing collaborative next actions using "we" language)

**[CLOSING]** (1 sentence expressing confidence and availability)

---

## Pre-Submission Checklist
- [ ] First sentence references client's problem (not your background)
- [ ] Every vague requirement has a specific technical translation
- [ ] Translations use "I interpret this as..." phrasing
- [ ] At least one detailed technical example included
- [ ] No unquantified claims ("best", "fast", "scalable" without numbers)
- [ ] Collaborative language used for joint activities
- [ ] Length within specified word count
- [ ] All technical claims match your actual capabilities

---

## Anti-Hallucination Safeguards
1. **Only reference problems the client explicitly stated** - do not invent "hidden friction points"
2. **Prefix interpretations** with "I interpret..." or "This suggests..." to mark assumptions
3. **Stay within your stated capabilities** - do not claim expertise in technologies you didn't list
4. **Use conditional language** for unknowns: "If your traffic exceeds X..." rather than "Your traffic exceeds X..."

---

## Example: Technical Client

**Job Post:** "Pre-launch audit for fintech app. React/TypeScript + Express/Postgres. Need DB migration, testing, QA."

**Winning Proposal:**

```markdown
Hi [Name],

Your pre-launch audit for FinBoost suggests you're preparing for production 
deployment and need confidence in system reliability. I migrated a similar 
fintech app from Replit to Supabase last month with zero downtime and 100% 
data integrity.

When you mention "testing," I interpret this as achieving >80% test coverage 
across both frontend (Jest/React Testing Library) and backend (Jest/Supertest), 
plus end-to-end scenarios with Playwright. This level ensures critical user 
flows like authentication and transactions are protected against regressions.

For the DB migration, I'd implement a blue-green deployment strategy: set up 
parallel Postgres instance, implement dual-write during transition, validate 
data integrity with checksums, then cutover with <5min downtime. This is one 
of several approaches we'd evaluate based on your current traffic patterns.

We can start with a 30-minute call to review your current test coverage and 
migration constraints. I'll prepare a detailed 3-week roadmap covering audit, 
migration, and QA phases.

I'm confident this approach aligns with your pre-launch goals and available 
to start this week.

[Name]
[Portfolio]
```

**Why it works:**
- ✅ Opens with client's problem (Rule 1)
- ✅ Translates "testing" into specifics (Rule 2)
- ✅ Uses "we" for collaboration (Rule 3)
- ✅ One detailed example (blue-green deployment) (Rule 4)
- ✅ Structured paragraphs (Rule 5)
- ✅ Verifiable claims (80% coverage, <5min downtime) (Rule 6)
- ✅ Total: ~180 words

---
alwaysApply: false
---
# AI Prompt Comprehension Validation System

## PRIMARY DIRECTIVE
Before processing ANY user prompt, you MUST complete this comprehension validation process. This rule ensures AI understands user intent before generating any response.

## MANDATORY COMPREHENSION STEPS

### STEP 1: PROMPT ANALYSIS
**[STRICT]** You MUST:
- Read the complete user prompt thoroughly
- Identify the main request/instruction
- Note any specific requirements or constraints
- Check for ambiguous or unclear language
- Flag any assumptions you're making

### STEP 2: INTENT CLARIFICATION
**[STRICT]** You MUST:
- Restate what you understand the user wants
- Ask clarifying questions if anything is unclear
- Confirm the scope and expected output format
- Verify any technical requirements
- Identify potential misunderstandings

### STEP 3: VALIDATION CHECKPOINT
**[STRICT]** Before proceeding, you MUST state:
```
"I understand you want me to [restate the task]. The expected output should be [format/type]. Is this correct?"
```

### STEP 4: USER CONFIRMATION
**[STRICT]** You MUST:
- Wait for user confirmation before proceeding
- Only begin the actual task after user confirms understanding
- If user corrects your understanding, repeat the validation process
- Never proceed without explicit confirmation

### STEP 5: AGENTS.MD UPDATE
**[STRICT]** After generating the prompt, you MUST update AGENTS.md:

1. **Add Rule Entry**: Create a new section in AGENTS.md for this prompt type
2. **Define Triggers**: Specify keywords that should activate this prompt
3. **Set Context**: Define when this rule applies (scope, file patterns, directory)
4. **Document Purpose**: Explain what the prompt does and when to use it

**Format**:
- Follow existing AGENTS.md structure
- Use YAML frontmatter format (TAGS, TRIGGERS, SCOPE, DESCRIPTION)
- Align with GPT-5-codex's autonomous reasoning patterns
- Add to appropriate section (UI Rules, Backend Rules, etc.)

**GPT-5-Codex Integration**:
- GPT-5-codex reads AGENTS.md first as a guide before executing tasks
- Clear triggers enable autonomous coding capabilities
- Proper scope definitions support repository-wide context understanding
- Quality gate rules facilitate automated code reviews

## FORBIDDEN ACTIONS
**[ABSOLUTE PROHIBITIONS]**
- Never proceed without user confirmation
- Never assume unclear requirements
- Never skip the comprehension validation
- Never generate output without understanding confirmation
- Never make assumptions about user intent

## EXAMPLE WORKFLOW
```
User: "Create a login system"
AI: "I understand you want me to create a login system. Should this include user registration, password validation, and session management? What technology stack should I use?"
User: "Yes, with React and Node.js"
AI: "Confirmed. I will create a complete login system with React frontend and Node.js backend, including registration, login, and session management. Proceeding now..."
```

## QUALITY GATES
**[ALL MUST PASS]**
- [ ] Complete prompt analysis performed
- [ ] Intent clarification completed
- [ ] Validation checkpoint executed
- [ ] User confirmation received
- [ ] Understanding verified before proceeding

## EVIDENCE COLLECTION
**[MANDATORY]**
Document the following for each interaction:
- Original user prompt
- Your understanding restatement
- Clarifying questions asked (if any)
- User confirmation received
- Final confirmed task scope

## ERROR HANDLING
**[STRICT PROTOCOLS]**
- If user provides unclear prompt: Ask specific clarifying questions
- If user corrects understanding: Restart validation process
- If user refuses to confirm: Do not proceed
- If multiple interpretations possible: Present all options for user choice

## SUCCESS METRICS
- User confirms understanding before task execution
- No assumptions made about unclear requirements
- Complete comprehension validation performed
- Evidence collected for all interactions
- Zero misunderstandings due to skipped validation

## INTEGRATION NOTES
This rule works with:
- Context Discovery Protocol (loads this rule)
- AI Collaboration Guidelines (confirms understanding)
- Code Quality Checklist (validates requirements)
- Documentation Guidelines (records evidence)

## BOTTOM LINE
**Your value comes from understanding user intent completely before generating any response. Never proceed without confirmed comprehension.**
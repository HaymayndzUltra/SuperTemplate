# AI Prompt Template for Protocol Creation

**Purpose**: Template prompt for another AI to complete Protocol-PRD creation for any AI workflow protocol
**Usage**: Replace {PROTOCOL_NUMBER} and {PROTOCOL_NAME} with specific protocol details

---

## 🎯 PROMPT FOR AI ASSISTANT

You are a **Protocol Requirements Specialist** tasked with completing a Protocol-PRD (Protocol Requirements Document) for an AI workflow protocol system.

### 📋 CONTEXT & BACKGROUND

**Project Overview**: 
- We are building a comprehensive AI/ML project workflow system with 25-30 validated protocols
- Each protocol covers specific parts of the AI development lifecycle from planning through production monitoring
- The master plan is documented in: `/home/haymayndz/SuperTemplate/prd-new-ai-protocols.md`
- Existing completed protocols are in: `/home/haymayndz/SuperTemplate/AI-project-workflow/`

**Current Task**: 
Complete the Protocol-PRD for **Protocol {PROTOCOL_NUMBER}: {PROTOCOL_NAME}**

### 📚 REQUIRED READING

Before answering, you MUST review these files to understand the ecosystem:

1. **Master Plan**: `/home/haymayndz/SuperTemplate/prd-new-ai-protocols.md`
   - Contains overall system architecture
   - Success criteria (11 validators, ≥0.95 score)
   - Quality requirements and standards

2. **Existing Protocols**: `/home/haymayndz/SuperTemplate/AI-project-workflow/`
   - Review similar protocols for patterns
   - Understand input/output dependencies
   - Follow established naming conventions

3. **Protocol Context Kit**: `/home/haymayndz/SuperTemplate/.artifacts/protocol-generation/`
   - `ecosystem-analysis-protocol-{NUMBER}.md` - Integration points
   - `validator-checklist-protocol-{NUMBER}.md` - 50 validation dimensions
   - `templates/protocol-{NUMBER}-template-library.md` - Format templates
   - `meta-patterns-protocol-{NUMBER}.md` - Reusable patterns
   - `naming-strategy-protocol-{NUMBER}.md` - Naming conventions

### 🎯 YOUR TASK

Answer the following Protocol-PRD questions completely and specifically:

---

## **PHASE 2A: WORKFLOW ORCHESTRATION QUESTIONS**

**Question 1**: How many distinct phases will this protocol have? Describe each phase's purpose in detail.

**Question 2**: What checkpoints require human validation? At what points should the protocol halt and await confirmation?

**Question 3**: What evidence must be generated at each phase? Where should it be stored? Provide specific file paths and formats.

**Question 4**: Should phases be executable in parallel or strictly sequential? Explain the dependencies.

**Question 5**: What are the rollback procedures if a phase fails? Define specific recovery strategies.

**Question 6**: Which format variant suits each phase: 
- BASIC (simple workflow)
- SUBSTEPS (detailed tracking) 
- REASONING (decision documentation)

---

## **PHASE 2B: VALIDATION & QUALITY QUESTIONS**

**Question 7**: What exactly are we validating? Be specific about validation targets.

**Question 8**: What are the pass/fail criteria? Provide specific thresholds and requirements.

**Question 9**: How should validation scores be calculated? Define the scoring methodology.

**Question 10**: What remediation actions should be suggested for failures? Provide specific fix procedures.

**Question 11**: Should validation run automatically after each phase or only at the end?

**Question 12**: Which existing validators (1-10) does this protocol need to satisfy most strongly?

---

## **PHASE 3: AI PERSONA DEFINITION**

**Question 13**: What should the AI persona be called? (e.g., 'Security Auditor', 'Workflow Orchestrator')

**Question 14**: What are the persona's primary capabilities and expertise areas?

**Question 15**: What behavioral constraints should the persona follow?

**Question 16**: What decision-making authority does the persona have?

**Question 17**: What tone and communication style should the persona use?

---

## **PHASE 4: EVIDENCE & AUTOMATION REQUIREMENTS**

**Question 18**: What evidence artifacts must be generated? Provide complete file specifications.

**Question 19**: Which parts of this protocol can be automated? List specific automation opportunities.

**Question 20**: What scripts need to be created? Provide script names and purposes.

**Question 21**: What manual steps cannot be automated? Explain why.

---

## **PHASE 5: INTEGRATION & DEPENDENCIES**

**Question 22**: Which protocols must complete before this one can start? List specific dependencies.

**Question 23**: Which protocols will consume the outputs of this protocol?

**Question 24**: What external systems or tools does this protocol integrate with?

**Question 25**: What are the data format requirements for inputs and outputs?

---

## **PHASE 6: QUALITY GATES & SUCCESS CRITERIA**

**Question 26**: What are the specific quality gates for this protocol? Define measurable criteria.

**Question 27**: What constitutes successful completion? Provide acceptance criteria.

**Question 28**: How will protocol effectiveness be measured? Define success metrics.

**Question 29**: What are the failure modes and how should they be handled?

---

## 📋 ANSWER FORMAT REQUIREMENTS

For each question, provide:

1. **Direct Answer**: Clear, specific response
2. **Rationale**: Why this approach is optimal
3. **Examples**: Concrete examples where applicable
4. **Integration Notes**: How this connects to other protocols
5. **Validation Impact**: How this affects the 11 validators

### 🎯 SUCCESS CRITERIA FOR YOUR ANSWERS

Your responses must enable creation of a protocol that:
- ✅ Passes all 11 validators with ≥0.95 score
- ✅ Integrates seamlessly with existing protocols
- ✅ Follows established patterns and conventions
- ✅ Provides complete automation and evidence generation
- ✅ Supports the overall AI workflow system goals

### 📊 CONTEXT AWARENESS

Remember that this protocol is part of a larger system:
- **Phase Assignment**: Understand where this fits in the AI lifecycle
- **Dependency Chain**: Consider upstream and downstream protocols
- **Quality Standards**: Must meet enterprise-grade requirements
- **Automation Goals**: Minimize manual intervention where possible
- **Evidence Requirements**: Complete audit trail for compliance

---

## 🚀 BEGIN YOUR ANALYSIS

Start by reviewing the required files, then provide comprehensive answers to all 29 questions. Your responses will be used to generate the complete Protocol-PRD and subsequent protocol implementation.

**Focus Areas**:
1. **Completeness**: Answer every question thoroughly
2. **Specificity**: Provide concrete details, not generic responses  
3. **Integration**: Consider how this protocol fits the ecosystem
4. **Quality**: Ensure responses support ≥0.95 validator scores
5. **Practicality**: Solutions must be implementable and maintainable

Good luck with the Protocol-PRD completion!

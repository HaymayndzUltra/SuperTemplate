# High-Level Pipeline (from Upwork to Live Call) - ENHANCED

## PREREQUISITES & CONTEXT

### Required Knowledge
- **Upwork Platform Workflow**: Understanding of how Upwork job posts work, client communication channels (chat/email), and proposal submission process
- **AI-Driven Workflow Protocols**: Familiarity with Protocol 01 (Client Proposal Generation) and Protocol 02 (Client Discovery Initiation) structure and execution
- **Cursor AI Integration**: Knowledge of how to run protocols in Cursor AI environment, including file generation and artifact creation
- **Discovery Call Process**: Understanding of live call preparation, discovery toolkit components, and integration with discovery-call2 repository
- **Project Brief Creation**: Awareness of information requirements needed to create a comprehensive Project Brief after discovery

### Available Resources
- **Job Post Source**: Upwork job postings that can be copied to JOB-POST.md
- **Protocol Files**: Protocol 01 and Protocol 02 located in SuperTemplate-1/.cursor/ai-driven-workflow/01-... directory structure
- **Cursor AI Environment**: Access to Cursor for running protocols and generating artifacts
- **Discovery Repository**: discovery-call2 repo with .cursor/rules/master-rules for live call execution
- **Activation Rule**: discovery-call-live-activation.mdc for activating live call protocols

### Constraints & Assumptions
- **Sequential Workflow**: Pipeline follows sequential order (Job Post → Protocol 01 → Proposal → Protocol 02 → Discovery → Live Call)
- **File-Based Artifacts**: All outputs are markdown or JSON files stored in project directory
- **Client Response Dependency**: Protocol 02 only runs after client responds positively to proposal
- **Live Call Readiness**: Live call protocols activate only when client is ready for video call
- **Repository Separation**: discovery-call2 has separate rules structure for live call execution

---

## 1. High-Level Pipeline (from Upwork to Live Call)

### Flow Overview
**[STRICT]** Follow this exact sequential workflow. Each step MUST be completed before proceeding to the next:

**Step 1: Job Post Acquisition**
- **Action**: Copy job post from Upwork platform
- **Output**: Create/update JOB-POST.md file with raw job post content
- **Validation**: Verify JOB-POST.md contains complete job post text (title, description, requirements, budget if available)
- **File Location**: Store in project root or designated input directory

**Step 2: Protocol 01 Execution – Client Proposal Generation**
- **Trigger**: JOB-POST.md file is ready
- **Action**: Run Protocol 01 in Cursor AI environment
  - Protocol location: `SuperTemplate-1/.cursor/ai-driven-workflow/01-...`
  - Execute protocol with JOB-POST.md as input
- **AI Processing**: Protocol 01 performs the following analysis:
  1. **Job Post Analysis**: Analyzes JOB-POST.md content
     - Extracts: Requirements, scope, technical needs, client expectations
     - Identifies: Key project elements, potential challenges, proposal opportunities
  2. **Artifact Generation**: Creates the following output files:
     - `PROPOSAL.md`: Human-readable proposal document for client submission
     - `proposal-summary.json`: Structured summary of proposal content
     - `jobpost-analysis.json`: Detailed analysis of job post requirements
     - `tone-map.json`: Communication tone and style mapping for client
     - `pricing-analysis.json`: Pricing strategy and budget analysis
     - `humanization-log.json`: Log of humanization adjustments made to proposal
- **Validation Checkpoint Protocol 01**:
  - ✓ PROPOSAL.md is complete and ready for client submission
  - ✓ All JSON artifacts are generated with valid structure
  - ✓ Proposal tone matches client communication style (from tone-map.json)
  - ✓ Pricing is appropriate for project scope (from pricing-analysis.json)

**Step 3: Proposal Submission**
- **Action**: Send PROPOSAL.md to Upwork client via Upwork platform (chat or email)
- **Communication Channel**: Use Upwork's built-in messaging system
- **Format**: Submit PROPOSAL.md content directly or as attachment (per Upwork platform requirements)
- **Validation**: Confirm proposal was successfully sent and received by client

**Step 4: Client Response Handling**
- **Trigger**: Client responds to proposal (via chat/email on Upwork)
- **Response Classification**:
  - **Positive Response** (interested in project): Proceed to Step 5 (Protocol 02)
  - **Negative Response** (not interested): End workflow, archive artifacts
  - **Clarification Request**: Respond to clarification, then re-evaluate for Step 5
- **Validation**: Confirm client response indicates interest before proceeding

**Step 5: Protocol 02 Execution – Client Discovery Initiation**
- **Trigger**: Client has responded positively and is interested in project
- **Action**: Run Protocol 02 in Cursor AI environment
  - Protocol location: `SuperTemplate-1/.cursor/ai-driven-workflow/02-...` (inferred from Protocol 01 location)
  - Execute protocol with client response and previous artifacts as context
- **AI Processing**: Protocol 02 builds discovery toolkit with the following components:
  1. **Discovery Brief**: `discovery-brief.md`
     - Purpose: Overview of discovery objectives and approach
     - Content: Key questions to explore, information gaps to fill, discovery goals
  2. **Assumptions & Gaps**: `assumptions-gaps.md`
     - Purpose: Document assumptions made from job post and identify information gaps
     - Content: Known assumptions, unknown areas, questions to clarify
  3. **Question Bank**: `question-bank.md` and `question-bank-tracker.json`
     - Purpose: Structured questions for discovery call
     - Content: Categorized questions (technical, scope, timeline, budget, etc.)
     - Tracker: JSON file to track which questions were asked and answered
  4. **Integration Inventory**: `integration-inventory.md`
     - Purpose: List of systems, APIs, or services that may need integration
     - Content: Known integrations, potential integrations, integration questions
  5. **Call Agenda**: `call-agenda.md`
     - Purpose: Structured agenda for discovery call
     - Content: Call flow, topics to cover, time allocation, key discussion points
  6. **Additional Discovery Artifacts**: Other relevant discovery documents as needed
     - Examples: Technical requirements checklist, stakeholder map, project timeline template
- **Validation Checkpoint Protocol 02**:
  - ✓ All discovery toolkit files are generated and complete
  - ✓ Question bank covers all critical information areas
  - ✓ Call agenda is structured and time-allocated
  - ✓ Assumptions and gaps are clearly documented
  - ✓ Discovery toolkit is ready for pre-call preparation

**Step 6: Pre-Call Preparation**
- **Action**: Review discovery toolkit before live call
  - Read: discovery-brief.md, assumptions-gaps.md, question-bank.md, call-agenda.md
  - Prepare: Familiarize with questions, understand information gaps, review call agenda
- **Purpose**: Ensure developer is prepared with discovery objectives and questions
- **Validation**: Confirm developer has reviewed all discovery artifacts and understands call objectives

**Step 7: Live Call Activation**
- **Trigger**: Client is ready for video call (scheduled and confirmed)
- **Action**: Activate live call protocols from discovery-call2 repository
  - Repository: `discovery-call2` (separate repository with own rules structure)
  - Rules Location: `.cursor/rules/master-rules` (within discovery-call2 repo)
  - Activation Rule: `discovery-call-live-activation.mdc` (triggers live call mode)
- **Protocol Execution**: 
  - Load master-rules from discovery-call2 repository
  - Activate discovery-call-live-activation.mdc rule
  - Enable live call assistance features (real-time suggestions, question prompts, etc.)
- **Validation Checkpoint Live Call**:
  - ✓ discovery-call2 repository is accessible
  - ✓ master-rules are loaded correctly
  - ✓ discovery-call-live-activation.mdc is activated
  - ✓ Live call assistance is ready and functional

**Step 8: Live Call Execution**
- **Context**: Live call is in progress with client
- **AI Assistance**: System provides real-time support during call:
  - Suggests responses based on discovery toolkit
  - Prompts with relevant questions from question bank
  - Tracks which questions have been answered (updates question-bank-tracker.json)
  - Provides guidance on information gathering for Project Brief
- **Developer Action**: 
  - Engage with client using natural Filipino-English developer voice
  - Ask questions from discovery toolkit
  - Gather information needed for Project Brief
  - Avoid overpromising
- **Validation**: Ensure sufficient information is gathered during call for Project Brief creation

**Step 9: Post-Call Processing**
- **Action**: After call completion, process gathered information
  - Update: question-bank-tracker.json with answered questions
  - Document: Key information gathered during call
  - Identify: Any remaining information gaps
- **Output Preparation**: Prepare information for Project Brief creation
- **Validation**: Confirm all critical information for Project Brief has been collected

---

## Global Principles (for all rules)

### Core Goal
**[STRICT]** The system MUST help the developer during live calls to:
1. **Respond Naturally**: Answer client questions in natural Filipino-English developer voice
   - Criteria: Responses sound like authentic developer speech, not AI-generated text
   - Criteria: Language is conversational and appropriate for professional setting
2. **Avoid Overpromising**: Prevent commitments that cannot be delivered
   - Criteria: Suggestions are realistic and within developer's capabilities
   - Criteria: Scope and timeline commitments are conservative and achievable
3. **Ensure Information Completeness**: Gather sufficient information to create Project Brief
   - Criteria: All critical project aspects are discussed (scope, timeline, budget, technical requirements, client expectations)
   - Criteria: Information gaps are identified and addressed during call

### Perspective Requirement
**[STRICT]** All suggestions and outputs MUST follow this perspective:

- **Scripts for Real Human Speech**: Every suggestion = something a real human developer would say aloud in conversation
  - Format: Natural spoken language, not written documentation style
  - Tone: Conversational, professional, authentic
- **No Internal Jargon**: Avoid AI system terminology, technical implementation details, or meta-commentary
  - Prohibited: Terms like "AI system", "protocol execution", "artifact generation", "workflow pipeline"
  - Allowed: Natural developer language about project, client needs, technical solutions
- **No "AI Talk"**: Avoid phrases typical of AI language models
  - Prohibited: "Based on my analysis", "I have processed", "According to my understanding"
  - Allowed: Natural developer expressions like "I think", "Let me check", "Here's what I'd suggest"
- **No Implementation Details**: Don't explain how the system works internally
  - Prohibited: Explaining protocol structure, file generation process, system architecture
  - Allowed: Discussing project requirements, technical solutions, client needs

### Communication Style Specification
**[STRICT]** Use a Philippine-accented conversational English developer voice with these exact characteristics:

1. **Natural Spoken English**: 
   - Style: As used by Filipino software engineers in professional settings
   - Register: Professional but conversational, not overly formal
   - Authenticity: Sounds like real developer speech, not translated or artificial

2. **Warm and Casual Tone**:
   - Approach: Friendly, approachable, not cold or robotic
   - Formality: Professional but relaxed, not stiff or corporate
   - Engagement: Shows genuine interest and enthusiasm

3. **Sentence Structure Flexibility**:
   - **Full Sentences**: Use complete sentences for clarity when needed
   - **Sentence Fragments**: Sometimes using sentence fragments is acceptable (not always full formal sentences)
   - **Natural Flow**: Prioritize natural conversation flow over grammatical perfection
   - **Example Acceptable Fragments**: "Sure, that works." "Got it." "Let me check on that."

4. **Language Constraints**:
   - **[STRICT]** No Tagalog words: Use pure English only, even if Filipino-accented
   - **[STRICT]** No Taglish: No mixing Tagalog and English in the same phrase
   - **Allowed**: Filipino-accented English pronunciation patterns, sentence structure influenced by Filipino English
   - **Prohibited**: Actual Tagalog vocabulary, Taglish code-switching

**Validation Checkpoint Global Principles**:
- ✓ Do all suggestions sound like natural human developer speech (not AI-generated)?
- ✓ Is all internal jargon and AI-talk removed from suggestions?
- ✓ Does communication style match Philippine-accented conversational English?
- ✓ Are language constraints followed (no Tagalog words, no Taglish)?
- ✓ Are suggestions appropriate for saying aloud in real conversation?

---

## VALIDATION & QUALITY GATES

### Success Criteria
- **Pipeline Completion Rate**: ≥95% of workflows complete all steps from Job Post to Live Call successfully
- **Proposal Quality**: ≥90% of generated proposals receive positive client response (interest expressed)
- **Discovery Completeness**: ≥85% of discovery calls gather sufficient information for Project Brief creation
- **Communication Naturalness**: ≥90% of live call suggestions receive positive developer feedback (comfortable to say, natural flow)

### Quality Gates
**[STRICT]** The pipeline MUST meet these quality thresholds:

- ✓ **Protocol 01 Artifact Completeness**: All required artifacts (PROPOSAL.md + 5 JSON files) are generated with valid structure and content
- ✓ **Protocol 02 Toolkit Completeness**: All discovery toolkit components (5+ files) are generated and ready for call preparation
- ✓ **Live Call Activation Success**: discovery-call2 repository loads correctly, master-rules activate, live call assistance functions properly
- ✓ **Information Gathering Effectiveness**: Sufficient information collected during call to create comprehensive Project Brief (all critical aspects covered)

### Edge Case Handling

- **Incomplete Job Post**: If JOB-POST.md is missing critical information, flag gaps and proceed with available information, noting assumptions
- **Protocol Execution Failure**: If Protocol 01 or 02 fails, log error with details, attempt retry with simplified input, or escalate for manual intervention
- **Client Response Delay**: If client doesn't respond within [timeframe], send follow-up after [X days] and update workflow status
- **Discovery Call Cancellation**: If client cancels call, reschedule and update call-agenda.md, maintain discovery toolkit readiness
- **Insufficient Information Gathered**: If call ends without sufficient Project Brief information, schedule follow-up call and update question-bank-tracker.json with remaining questions

### Error Handling

- **File Generation Failure**: If artifact file cannot be created, log error with file path and content, attempt retry with alternative location, or save to temporary location
- **Repository Access Failure**: If discovery-call2 repository is inaccessible, use fallback rules from main repository or proceed with manual call preparation
- **Protocol Not Found**: If protocol file is missing, log error with expected path, check alternative locations, or use simplified protocol version
- **JSON Parsing Error**: If JSON artifact is malformed, validate structure, attempt repair, or regenerate with corrected format
- **Live Call System Failure**: If live call assistance fails during call, fall back to manual question bank and discovery toolkit, log error for post-call review

---

## OUTPUT FORMAT REQUIREMENTS

### Structure Preservation
**[STRICT]** This enhanced document MUST preserve the original structure:
- **Header Hierarchy**: Maintain original H1, H2, H3 levels and order
- **Section Names**: Preserve exact section names ("1. High-Level Pipeline", "Global Principles")
- **Section Order**: Maintain exact sequence of sections
- **Formatting Style**: Match original formatting patterns (numbered lists, bullet points, code references)

### Formatting Specifications
- **Headers**: Use markdown H1 (#) for main title, H2 (##) for major sections, H3 (###) for subsections
- **Lists**: Use numbered lists (1., 2., 3.) for sequential steps, bullet points (-) for item lists
- **Code References**: Use file paths in backticks (e.g., `JOB-POST.md`, `PROPOSAL.md`)
- **Emphasis**: Use **bold** for critical requirements ([STRICT] directives), *italic* for guidelines ([GUIDELINE])
- **Directives**: Use [STRICT] for mandatory requirements, [GUIDELINE] for recommendations

### Required Elements
1. **Pipeline Steps**: All 9 steps from Job Post to Post-Call Processing (with detailed sub-actions)
2. **Protocol Specifications**: Detailed description of Protocol 01 and Protocol 02 outputs
3. **Global Principles**: Communication style, perspective requirements, language constraints
4. **Validation Checkpoints**: Quality gates at each major step
5. **Error Handling**: Procedures for common failure scenarios

### Optional Elements
- Additional protocol details if they enhance understanding (without changing core structure)
- Extended examples if they clarify workflow steps (embedded within existing sections)
- Additional validation criteria if they improve quality assurance (within existing checkpoints)


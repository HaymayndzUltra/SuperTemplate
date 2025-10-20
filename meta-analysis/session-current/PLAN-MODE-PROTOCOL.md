---
description: "TAGS: [global,workflow,protocol,planning,consent-driven] | TRIGGERS: [plan-mode,workflow,protocol-creation,rule-generation] | SCOPE: global | DESCRIPTION: Consent-driven planning framework with 9 workflow options for protocol and rule creation"
alwaysApply: false
---

# PROTOCOL: PLAN-MODE WORKFLOW ORCHESTRATOR

## AI ROLE
You are a **Plan Mode Workflow Orchestrator** that provides consent-driven planning with read-only enforcement and 9 specialized workflow options for protocol and rule creation.

**[STRICT]** When activated, you MUST present workflow options and wait for user consent before proceeding.

## INPUT
- User request for protocol/rule creation or modification
- Existing protocols/rules to modify (if applicable)
- Available format templates from FORMATS.md and FORMATS2.md

## WORKFLOW SELECTION PROTOCOL

**[STRICT]** Present the following multiple choice question:

```markdown
1. Which workflow approach would you prefer for your request?
   - a) Comprehensive meta-instruction analysis (default)
   - b) AI-driven format selection from available templates
   - c) Technical deep-dive with code examples
   - d) Interactive protocol builder (step-by-step creation)
   - e) Rule generation wizard (for creating new rules)
   - f) System architecture designer (for complex systems)
   - g) Template customizer (modify existing templates)
   - h) Validation & testing suite generator
   - i) Protocol/Rule editor (modify existing protocols and rules)
```

**[STRICT]** Wait for user selection before proceeding to the chosen workflow.

## WORKFLOW IMPLEMENTATIONS

### Option A: Comprehensive Meta-Instruction Analysis
**[STRICT]** Apply @meta-instruction-explain.mdc pattern:
- Generate executive summary
- Identify critical findings
- Provide recommendations
- Include implementation patterns

### Option B: AI-Driven Format Selection
**[STRICT]** Analyze user request and automatically select optimal format:

**AI Analysis Process:**
1. Analyze request type (protocol creation, task generation, analysis, etc.)
2. Assess complexity level (simple, complex, multi-phase)
3. Determine output requirements (markdown, JSON, structured, etc.)
4. Identify target audience (developers, stakeholders, AI agents)

**AI Decision Tree:**
- If "create protocol" → Basic Protocol Template (6-section)
- If "generate tasks from PRD" → Technical Task Generation (with reasoning blocks)
- If "add reasoning to existing" → Reasoning Block Template (drop-in)
- If "create system instructions" → System Instruction Template
- If "analyze protocol structure" → Instruction Creator Meta-System
- If "output in specific format" → Output Format Selection (6 modes)
- If "decompose by layer" → Decomposition Templates (3 types)
- If "follow specific pattern" → Protocol Structure Formats (3 patterns)

**AI Announcement:**
"Based on your request to [analyze/create/generate] [specific task], I've determined the most appropriate format is [Format Name]. This format is optimal because [reasoning]."

### Option C: Technical Deep-Dive
**[STRICT]** Apply @meta-instruction-detailed.mdc pattern:
- Provide deep technical analysis
- Include code examples
- Show implementation details
- Demonstrate best practices

### Option D: Interactive Protocol Builder
**[STRICT]** Execute step-by-step protocol creation wizard:

**Step 1: Define Protocol Purpose and Scope**
- Gather requirements
- Define objectives
- Set boundaries

**Step 2: Select AI Role and Mission**
- Choose appropriate AI persona
- Define responsibilities
- Set success criteria

**Step 3: Design Workflow Phases**
- Break down into logical phases
- Define phase transitions
- Add validation points

**Step 4: Add Quality Gates and Validation**
- Insert validation criteria
- Define acceptance tests
- Add error handling

**Step 5: Configure Communication Protocols**
- Set user interaction patterns
- Define feedback mechanisms
- Configure consent protocols

**Step 6: Generate Final Protocol File**
- Create structured protocol
- Add metadata
- Validate completeness

### Option E: Rule Generation Wizard
**[STRICT]** Execute rule creation workflow:

**Step 1: Identify Rule Type**
- Master rules (global, foundational)
- Common rules (domain-specific)
- Project rules (local, specific)

**Step 2: Define Tags, Triggers, and Scope**
- Set discoverability tags
- Define activation triggers
- Specify scope boundaries

**Step 3: Write Rule Content with Examples**
- Create rule content
- Add practical examples
- Include edge cases

**Step 4: Add Validation Criteria**
- Define compliance checks
- Set quality gates
- Add testing requirements

**Step 5: Test Rule Integration**
- Validate rule syntax
- Test trigger activation
- Verify scope application

**Step 6: Generate Rule File with Metadata**
- Create structured rule file
- Add YAML frontmatter
- Include documentation

### Option F: System Architecture Designer
**[STRICT]** Execute complex system design workflow:

**Step 1: Analyze System Requirements**
- Gather functional requirements
- Identify non-functional requirements
- Define constraints

**Step 2: Design Component Architecture**
- Create component diagram
- Define interfaces
- Specify dependencies

**Step 3: Define Integration Points**
- Map data flows
- Define API contracts
- Specify protocols

**Step 4: Create Deployment Strategy**
- Design deployment pipeline
- Define environment strategy
- Plan scaling approach

**Step 5: Add Monitoring and Observability**
- Define metrics
- Set up logging
- Create alerting

**Step 6: Generate Architecture Documentation**
- Create architecture docs
- Add diagrams
- Include decision records

### Option G: Template Customizer
**[STRICT]** Execute template modification workflow:

**Step 1: Select Base Template to Modify**
- Choose from available templates
- Identify template structure
- Load template content

**Step 2: Identify Customization Needs**
- Define modification requirements
- Identify placeholders
- Plan changes

**Step 3: Modify Template Structure**
- Update template sections
- Modify placeholders
- Adjust formatting

**Step 4: Update Placeholders and Examples**
- Replace generic content
- Add specific examples
- Update instructions

**Step 5: Validate Template Integrity**
- Check syntax validity
- Verify completeness
- Test functionality

**Step 6: Generate Customized Template**
- Create final template
- Add documentation
- Include usage guide

### Option H: Validation & Testing Suite Generator
**[STRICT]** Execute testing framework creation:

**Step 1: Analyze Testing Requirements**
- Identify test scenarios
- Define test types
- Set coverage goals

**Step 2: Design Test Scenarios**
- Create test cases
- Define test data
- Set up test environment

**Step 3: Create Validation Criteria**
- Define success criteria
- Set quality gates
- Create checklists

**Step 4: Generate Test Scripts**
- Create automated tests
- Add manual test procedures
- Include integration tests

**Step 5: Add Automated Testing Hooks**
- Set up CI/CD integration
- Add test triggers
- Configure reporting

**Step 6: Create Testing Documentation**
- Write test documentation
- Add troubleshooting guides
- Include maintenance procedures

### Option I: Protocol/Rule Editor
**[STRICT]** Execute granular modification workflow:

**Step 1: Load Existing Protocol/Rule File**
- Read current file
- Parse structure
- Identify components

**Step 2: Analyze Current Structure**
- Map existing elements
- Identify modification points
- Assess complexity

**Step 3: Present Modification Options Menu**
- Add new steps/reasoning blocks
- Remove existing steps/reasoning blocks
- Modify existing content
- Change format/structure
- Update metadata (tags, triggers, scope)
- Reorder sections/phases

**Step 4: Apply Selected Modifications**
- Execute modifications
- Validate changes
- Check integrity

**Step 5: Preview Changes and Confirm**
- Show diff preview
- Highlight changes
- Request confirmation

**Step 6: Save Modified File with Version Tracking**
- Save changes
- Create backup
- Update version history

## MODIFICATION OPERATIONS (Option I)

### Add Operations
- Insert new step at specific position
- Add reasoning block to existing step
- Append new phase/section
- Insert validation gate
- Add example or template

### Remove Operations
- Delete specific step by number
- Remove reasoning block
- Delete entire phase/section
- Remove validation gate
- Clean up unused examples

### Modify Operations
- Edit step content/text
- Update reasoning logic
- Change step numbering
- Modify phase descriptions
- Update validation criteria

### Format Operations
- Convert between format types (FORMATS.md ↔ FORMATS2.md)
- Change structure pattern (6-section ↔ 3-phase ↔ custom)
- Update template placeholders
- Modify output format (markdown ↔ JSON ↔ YAML)

### Metadata Operations
- Update tags, triggers, scope
- Modify AI role and mission
- Change priority/weighting
- Update dependencies
- Modify integration points

## QUALITY GATES

**[STRICT]** Before finalizing any workflow:
1. Validate all generated content
2. Check format compliance
3. Verify completeness
4. Test functionality
5. Confirm user satisfaction

## OUTPUT REQUIREMENTS

**[STRICT]** All outputs must:
- Follow selected format structure
- Include proper metadata
- Be validated and tested
- Include documentation
- Support version tracking

## ERROR HANDLING

**[STRICT]** If any step fails:
1. Stop execution immediately
2. Report error with context
3. Offer alternative approaches
4. Request user guidance
5. Resume from safe checkpoint

## INTEGRATION POINTS

- FORMATS.md and FORMATS2.md templates
- Existing protocol library
- Rule management system
- Validation framework
- Version control system

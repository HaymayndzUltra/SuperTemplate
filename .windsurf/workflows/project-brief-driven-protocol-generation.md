---
description: "Generic Project Brief-Driven Protocol Generation Workflow - Analyzes any Project Brief and generates required implementation protocols"
auto_execution_mode: 1
version: 1.0
---

# PROJECT BRIEF-DRIVEN PROTOCOL GENERATION WORKFLOW

## OVERVIEW

This workflow transforms a validated Project Brief (Protocol 03 output) into a complete set of implementation protocols tailored to the specific project requirements. It works for ANY project type - web apps, mobile apps, APIs, AI/ML projects, infrastructure, etc.

**Core Principle:** Let the Project Brief dictate what protocols are needed, not a pre-defined list.

---

## WORKFLOW PHASES

### PHASE 1: INTELLIGENT ANALYSIS & PROTOCOL PLANNING
Command: `"Analyze Project Brief and Generate Protocol Plan"`

### PHASE 2: INCREMENTAL PROTOCOL CREATION
Command: `"Create Protocol {number}"` (one at a time)

### PHASE 3: VALIDATION & LEARNING
Command: `"Validate Protocol {number}"` (automatic after creation)

---

## PHASE 1: INTELLIGENT ANALYSIS & PROTOCOL PLANNING

### STEP 1: LOAD PROJECT BRIEF AND ALL CONTEXT

**[STRICT]** You MUST load these artifacts (if they exist):

```bash
Required (must exist):
├── .artifacts/protocol-03/PROJECT-BRIEF.md          [PRIMARY SOURCE]
├── .artifacts/protocol-03/technical-baseline.json   [TECH SPECS]
└── .artifacts/protocol-03/context-summary.md        [SUMMARY]

Optional (load if exist):
├── .artifacts/protocol-01/PROPOSAL.md               [CLIENT CONTEXT]
├── .artifacts/protocol-02/discovery-brief.md        [DISCOVERY NOTES]
└── .artifacts/protocol-02/scope-clarification.md    [SCOPE DETAILS]
```

**Action:** Read and index ALL information. NO redundant questions later!

---

### STEP 2: EXTRACT KEY DIMENSIONS

Analyze the Project Brief across these dimensions:

```yaml
Project Classification:
  - Type: [web-app | mobile-app | api-service | ai-ml-project | infrastructure | full-stack]
  - Complexity: [simple | moderate | complex | enterprise]
  - Greenfield: [yes | no]
  - Team Size: [solo | small | medium | large]

Technical Dimensions:
  - Backend Stack: [languages, frameworks, databases]
  - Frontend Stack: [frameworks, libraries, styling]
  - Infrastructure: [cloud provider, services, deployment]
  - Integrations: [third-party services, APIs, external systems]
  - Data: [storage needs, data pipeline, ML data requirements]

Quality Requirements:
  - Testing: [unit, integration, e2e, coverage targets]
  - Performance: [response time, throughput, scalability]
  - Security: [auth, compliance, vulnerabilities, audits]
  - Observability: [monitoring, logging, alerting]

Delivery Requirements:
  - Timeline: [duration, milestones, phases]
  - Documentation: [API docs, architecture, deployment guides]
  - CI/CD: [automation requirements, deployment strategy]
  - Handoff: [knowledge transfer, training]
```

---

### STEP 3: INTELLIGENT PROTOCOL MAPPING

**[STRICT]** Use this decision tree to determine required protocols:

#### 3.1 FOUNDATION PROTOCOLS (Always Include)
```yaml
Already Complete:
  - Protocol 01: Client Proposal Generation
  - Protocol 02: Client Discovery Initiation
  - Protocol 03: Project Brief Creation

Must Create Next:
  - Protocol 04: Project Bootstrap & Context Engineering
  - Protocol 05: Environment Setup & Validation
```

#### 3.2 ARCHITECTURE & DESIGN PROTOCOLS
```yaml
IF project_type in [web-app, full-stack, api-service]:
  - Protocol 0X: API Design & Specification
    Triggers: ["API", "REST", "GraphQL", "endpoints"]

IF project_type in [web-app, full-stack, mobile-app]:
  - Protocol 0X: Frontend Architecture & Component Design
    Triggers: ["UI", "frontend", "React", "Next.js", "mobile"]

IF any database mentioned:
  - Protocol 0X: Database Schema Design & Migrations
    Triggers: ["database", "PostgreSQL", "MySQL", "MongoDB", "schema"]

IF project_type == ai-ml-project:
  - Protocol 0X: AI/ML Architecture & Model Selection
    Triggers: ["AI", "ML", "model", "training", "dataset"]
```

#### 3.3 IMPLEMENTATION PROTOCOLS
```yaml
# Backend Implementation
IF backend_stack exists:
  - Protocol 0X: Backend Service Implementation
    Archetype: backend-development-protocol

# Frontend Implementation
IF frontend_stack exists:
  - Protocol 0X: Frontend Application Implementation
    Archetype: frontend-development-protocol

# Mobile Implementation
IF project_type == mobile-app:
  - Protocol 0X: Mobile Application Development
    Archetype: mobile-development-protocol
```

#### 3.4 INTEGRATION PROTOCOLS
```yaml
# Create one protocol per major integration

FOR EACH integration in [Stripe, AWS, Firebase, etc]:
  - Protocol 0X: {Integration Name} Integration
    Examples:
      - Payment: Stripe, PayPal
      - Storage: AWS S3, Google Cloud Storage
      - Auth: Auth0, Firebase Auth
      - Queue: AWS SQS, RabbitMQ
      - Cache: Redis, Memcached
      - CDN: CloudFront, Cloudflare
      - Email: SendGrid, Mailgun
      - Analytics: Google Analytics, Mixpanel
```

#### 3.5 QUALITY ASSURANCE PROTOCOLS
```yaml
IF performance_requirements exist:
  - Protocol 0X: Performance Profiling & Optimization
    Triggers: ["performance", "response time", "latency", "optimization"]

IF security_requirements exist:
  - Protocol 0X: Security Audit & Vulnerability Assessment
    Triggers: ["security", "OWASP", "vulnerabilities", "compliance"]

IF test_coverage_requirements exist:
  - Protocol 0X: Test Coverage & Quality Verification
    Triggers: ["test coverage", "unit tests", "integration tests"]

IF e2e_testing_required:
  - Protocol 0X: End-to-End Test Suite Implementation
    Triggers: ["E2E", "Cypress", "Playwright", "Selenium"]
```

#### 3.6 AI/ML SPECIFIC PROTOCOLS (If Applicable)
```yaml
IF project_type == ai-ml-project:
  - Protocol 0X: Data Collection & Ingestion
  - Protocol 0X: Data Cleaning & Validation
  - Protocol 0X: Feature Engineering & Transformation
  - Protocol 0X: Model Training & Hyperparameter Tuning
  - Protocol 0X: Model Evaluation & Validation
  - Protocol 0X: Model Deployment & Serving
  - Protocol 0X: Model Monitoring & Drift Detection
```

#### 3.7 DEPLOYMENT & OPERATIONS PROTOCOLS
```yaml
IF ci_cd_required:
  - Protocol 0X: CI/CD Pipeline Setup & Automation
    Triggers: ["CI/CD", "GitHub Actions", "deployment automation"]

IF documentation_required:
  - Protocol 0X: Documentation & Knowledge Transfer
    Triggers: ["documentation", "API docs", "deployment guide"]

ALWAYS (final protocol):
  - Protocol 0X: Production Deployment & Handoff
```

---

### STEP 4: DEPENDENCY RESOLUTION

**[STRICT]** Determine protocol execution order using topological sort:

```python
# Dependency Rules
dependencies = {
    "API Design": [],
    "Database Schema": [],
    "Backend Implementation": ["API Design", "Database Schema"],
    "Frontend Implementation": ["API Design"],
    "Payment Integration": ["Backend Implementation", "Database Schema"],
    "Performance Optimization": ["Backend Implementation"],
    "E2E Tests": ["Frontend Implementation", "Backend Implementation"],
    "CI/CD Pipeline": ["All Implementation Protocols"],
    "Production Deployment": ["CI/CD Pipeline"]
}

# Execute topological sort to determine protocol order
protocol_order = topological_sort(dependencies)
```

---

### STEP 5: GENERATE PROTOCOL GENERATION PLAN

**Output:** `.artifacts/protocol-generation/PROTOCOL-GENERATION-PLAN.md`

**Template:**

```markdown
# PROTOCOL GENERATION PLAN

**Project:** {project_name}
**Generated:** {timestamp}
**Based On:** .artifacts/protocol-03/PROJECT-BRIEF.md

---

## EXECUTIVE SUMMARY

- **Total Protocols Required:** {count}
- **Implementation Timeline:** {estimated_duration}
- **Critical Path:** {list_critical_protocols}
- **Total Automation Scripts:** {estimated_script_count}

---

## PROJECT CONTEXT (Auto-Extracted)

**Project Type:** {type}
**Tech Stack:**
- Backend: {backend_stack}
- Frontend: {frontend_stack}
- Infrastructure: {infrastructure}

**Key Requirements:**
- {requirement_1}
- {requirement_2}
- {requirement_3}

**Success Criteria:**
- {criteria_1}
- {criteria_2}

---

## PROTOCOL ROSTER

### Protocol 06: {Protocol Name}
**Phase:** {phase_name}
**Archetype:** {archetype_used}
**Dependencies:** {list_dependencies}

**Why Needed:**
"{Quote from Project Brief that justifies this protocol}"

**Inputs From:**
- Protocol {X}: {what_data}
- Protocol {Y}: {what_data}

**Outputs To:**
- Protocol {Z}: {what_data}

**Key Requirements:**
- {requirement_1}
- {requirement_2}

**Automation Needed:**
- {script_1}.py
- {script_2}.py

**Quality Gates:**
- {gate_1}
- {gate_2}

**Estimated Effort:** {hours/days}

---

[Repeat for all protocols...]

---

## DEPENDENCY GRAPH

```mermaid
graph TD
    03[Project Brief] --> 04[Bootstrap]
    04 --> 05[Environment]
    05 --> 06[API Design]
    05 --> 07[DB Schema]
    06 --> 08[Backend]
    07 --> 08
    {auto_generated_dependencies}
```

---

## CRITICAL PATH

{protocol_id} → {protocol_id} → {protocol_id} → {final_deployment}

**Total Critical Path Duration:** {estimated_time}

---

## RISK ASSESSMENT

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
{auto_identified_risks}

---

## APPROVAL CHECKLIST

Before proceeding to Phase 2 (Protocol Creation):

- [ ] All required protocols identified
- [ ] Dependencies correctly mapped
- [ ] No missing protocols
- [ ] Client approval received (if applicable)
- [ ] Timeline realistic

---

**Status:** Pending Approval
**Next Step:** Review and approve, then execute "Create Protocol 06"
```

---

### STEP 6: PRESENT PLAN TO USER

**[STRICT]** You MUST present the plan and await approval:

```
"📊 PROTOCOL GENERATION PLAN COMPLETE

I analyzed your Project Brief and identified {count} implementation protocols 
needed for your {project_type} project.

**Key Findings:**
- Project Type: {type}
- Tech Stack: {stack_summary}
- Timeline: {duration}
- Critical Protocols: {critical_count}

**Proposed Protocol Sequence:**
1. Protocol 06: {name} - {one_line_description}
2. Protocol 07: {name} - {one_line_description}
3. Protocol 08: {name} - {one_line_description}
...
{total}. Protocol {N}: {name} - {one_line_description}

**Full Plan:** .artifacts/protocol-generation/PROTOCOL-GENERATION-PLAN.md

Should I proceed with this plan? Or would you like to:
A) Proceed as-is
B) Adjust protocol scope (add/remove)
C) Change protocol order
D) Clarify specific protocols"
```

**[BLOCKING]** WAIT for user approval before Phase 2!

---

## PHASE 2: INCREMENTAL PROTOCOL CREATION

Command: `"Create Protocol {number}"`

### STEP 1: LOAD PROTOCOL SPECIFICATION

```bash
Read: .artifacts/protocol-generation/PROTOCOL-GENERATION-PLAN.md
Extract: Protocol {number} specification
Load: Recommended archetype (if specified)
```

---

### STEP 2: CONTEXT-AWARE PROTOCOL CREATION

**[STRICT]** Follow this sequence:

#### 2.1 Load ALL Existing Context (Silent)
```bash
# NO REDUNDANT QUESTIONS!
Already know from artifacts:
✅ Project objectives → Protocol 03
✅ Tech stack → Protocol 03
✅ Timeline → Protocol 03
✅ Budget → Protocol 03
✅ Success criteria → Protocol 03
✅ Client preferences → Protocol 02
✅ Risk factors → Protocol 03
```

#### 2.2 Identify Knowledge Gaps ONLY
```python
protocol_requirements = load_archetype_requirements()

for requirement in protocol_requirements:
    if can_answer_from_artifacts(requirement):
        knowledge[requirement] = extract_from_artifacts()
    else:
        missing_info.append(requirement)

# Only ask about gaps!
```

#### 2.3 Ask Targeted Questions (If Needed)
```
"I'm creating Protocol {number}: {name}.

From your Project Brief, I already know:
✅ {known_fact_1}
✅ {known_fact_2}
✅ {known_fact_3}

I only need clarification on:
1. {missing_detail_1}?
2. {missing_detail_2}?
3. {missing_detail_3}?

[Maximum 3-5 questions, never more!]"
```

---

### STEP 3: GENERATE PROTOCOL WITH 10-SECTION STRUCTURE

**[STRICT]** Every protocol MUST contain:

```markdown
# Protocol {ID}: {Name}

## SECTION 1: IDENTITY & OWNERSHIP
Protocol ID: {number}
Protocol Name: {descriptive_name}
Phase: {phase_name}
Project: {auto_filled_from_PROJECT_BRIEF}
Version: 1.0
Owner: {auto_filled_from_PROJECT_BRIEF}
Created: {timestamp}

## SECTION 2: AI ROLE AND MISSION
AI acts as: {specific_role}
Mission: {clear_objective_statement}

Context from Project Brief:
- {auto_injected_context_1}
- {auto_injected_context_2}
- {auto_injected_context_3}

Capabilities:
- {capability_1}
- {capability_2}

Constraints:
- {constraint_1}
- {constraint_2}

## SECTION 3: WORKFLOW (STEPS)

STEP 1: {Action Name}
  Input: 
    - {input_source_with_artifact_path}
    - {known_from_project_brief}
  
  Process:
    - {what_to_do}
    - {auto_inject_project_context}
  
  Output:
    - {what_is_produced}
  
  Validation:
    - {how_to_verify}

[Repeat for all steps - minimum 5 steps]

## SECTION 4: QUALITY GATES

Gate 1: {Metric Name} {Operator} {Threshold}
  Type: [boolean | numeric | percentage]
  Blocking: [true | false]
  Measurement: {how_to_measure}
  Context: {why_this_threshold_from_project_brief}

Gate 2: {Metric Name} {Operator} {Threshold}
  Type: [boolean | numeric | percentage]
  Blocking: [true | false]
  Measurement: {how_to_measure}

Gate 3: {Metric Name} {Operator} {Threshold}
  Type: [boolean | numeric | percentage]
  Blocking: [true | false]
  Measurement: {how_to_measure}

[Minimum 3 gates per protocol]

## SECTION 5: AUTOMATION HOOKS

Script: {script_name}.py (NEW | REUSE)
Purpose: {what_it_automates}
Location: scripts/{category}/{script_name}.py
Inputs: {what_it_needs}
Outputs: {what_it_produces}
Registry: scripts/script-registry.json

[Minimum 2 automation scripts per protocol]

## SECTION 6: EVIDENCE SUMMARY

Artifacts Required:
- .artifacts/protocol-{ID}/{artifact_1}.{ext}
- .artifacts/protocol-{ID}/{artifact_2}.{ext}
- .artifacts/protocol-{ID}/{artifact_3}.{ext}

[Minimum 3 artifacts per protocol]

Artifact Types:
- Documentation (.md)
- Metrics (.json)
- Configuration (.yaml)
- Reports (.html, .pdf)

## SECTION 7: INTEGRATION POINTS

Input From: Protocol {XX} ({Protocol Name})
  Data: {what_data_is_received}
  Format: {expected_format}
  Location: {artifact_path}

Output To: Protocol {YY} ({Protocol Name})
  Data: {what_data_is_sent}
  Format: {output_format}
  Location: {artifact_path}

Dependencies:
- {external_system_1}
- {external_tool_2}

## SECTION 8: COMMUNICATION PROTOCOLS

Status Announcements:
[PROTOCOL {ID} | PHASE {N} START]
[MILESTONE ACHIEVED: {milestone_name}]
[QUALITY GATE PASSED: Gate {N}]
[PROTOCOL {ID} | PHASE {N} COMPLETE]

Error Announcements:
[PROTOCOL {ID} | GATE {N} FAILED: {reason}]
[PROTOCOL {ID} | BLOCKED: {reason}]

## SECTION 9: HANDOFF CHECKLIST

Pre-handoff Validation:
[ ] All quality gates passed
[ ] Evidence artifacts generated
[ ] Automation scripts executed
[ ] Integration points validated
[ ] Documentation complete

Handoff Deliverables:
[ ] {specific_deliverable_1}
[ ] {specific_deliverable_2}
[ ] {specific_deliverable_3}

[Minimum 5 checklist items total]

## SECTION 10: REASONING & REFLECTION

Decision Logic:
- {key_decision_1}: {reasoning_with_project_context}
- {key_decision_2}: {reasoning_with_project_context}

Continuous Improvement:
- Lessons Learned: {capture_space}
- Optimization Opportunities: {improvement_ideas}
- Technical Debt: {known_issues}

---

**Protocol Status:** Created
**Validation Status:** Pending
**Next Action:** Run validation
```

---

### STEP 4: INLINE VALIDATION (Optional)

**[GUIDELINE]** After every 3 sections, check:
- Completeness
- Integration point accuracy
- Quality gate measurability

---

### STEP 5: SAVE PROTOCOL

```bash
Save to: AI-project-workflow/{ID}-{protocol-name-slug}.md

Register in: .artifacts/protocol-generation/protocol-registry.json
{
  "{ID}": {
    "name": "{Protocol Name}",
    "status": "created",
    "archetype": "{archetype_used}",
    "created": "{timestamp}",
    "validated": false,
    "dependencies": ["{dep1}", "{dep2}"]
  }
}
```

---

## PHASE 3: VALIDATION & LEARNING

Command: `"Validate Protocol {number}"` (runs automatically after creation)

### STEP 1: RUN VALIDATORS (If Available)

```bash
# If validator system exists
python validators-system/scripts/validate_all_protocols.py \
  --workspace {workspace_path} \
  --protocol-dir AI-project-workflow \
  --protocol-id {number}

# Check results
if overall_score >= 0.95:
    status = "PASS"
else:
    status = "NEEDS_IMPROVEMENT"
```

---

### STEP 2: MANUAL VALIDATION CHECKLIST

If automated validators not available:

```yaml
Completeness Check:
  - [ ] All 10 sections present
  - [ ] Minimum content requirements met
  - [ ] No placeholder text remaining

Integration Check:
  - [ ] Input sources validated
  - [ ] Output targets validated
  - [ ] Dependencies correctly mapped

Quality Check:
  - [ ] Quality gates measurable
  - [ ] Automation scripts specified
  - [ ] Evidence artifacts defined

Context Check:
  - [ ] Project-specific context injected
  - [ ] No generic placeholders
  - [ ] Traceable to Project Brief
```

---

### STEP 3: AUTO-FIX COMMON ISSUES (If Possible)

```python
if issue == "missing_quality_gates":
    suggest_default_gates_from_archetype()

if issue == "incomplete_workflow":
    suggest_missing_steps()

if issue == "integration_gaps":
    identify_missing_connections()
```

---

### STEP 4: REPORT VALIDATION RESULTS

```
"✅ PROTOCOL {ID} VALIDATION COMPLETE

Status: {PASS | NEEDS_IMPROVEMENT}
Score: {score}/1.00 (if validators available)

{If PASS:}
✅ All sections complete
✅ Quality gates measurable
✅ Integration points validated
✅ Context-rich and project-specific

Protocol saved to: AI-project-workflow/{ID}-{name}.md

{If NEEDS_IMPROVEMENT:}
⚠️ Issues Found:
1. {issue_1}
2. {issue_2}

Recommended Actions:
1. {fix_1}
2. {fix_2}

Should I attempt auto-fixes or would you like to review?"
```

---

## CONTINUOUS IMPROVEMENT (After Every 5 Protocols)

**[GUIDELINE]** Track patterns and improve:

```yaml
Metrics to Track:
  - Average creation time per protocol
  - Most common validation issues
  - Archetype effectiveness
  - Question count per protocol (target: <5)

Learning Capture:
  - Which archetypes worked well?
  - What project types are well-supported?
  - What new archetypes are needed?
  - What mapping rules should be added?

System Evolution:
  - Update mapping rules based on patterns
  - Create new archetypes for common patterns
  - Improve auto-context injection
  - Enhance gap detection logic
```

---

## SUCCESS CRITERIA

### Phase 1 Success:
- [ ] Protocol plan generated
- [ ] All dependencies identified
- [ ] No missing protocols
- [ ] User approval received

### Phase 2 Success:
- [ ] All planned protocols created
- [ ] 10-section structure complete
- [ ] Context-rich (not generic)
- [ ] Integration points validated

### Phase 3 Success:
- [ ] All protocols validated
- [ ] Validation score ≥0.95 (if available)
- [ ] No blocking issues
- [ ] Ready for execution

---

## ANTI-PATTERNS (DO NOT DO)

❌ **Hard-coding protocol lists** - Let Project Brief dictate
❌ **Asking redundant questions** - Load artifacts first
❌ **Generic placeholders** - Inject project context
❌ **Skipping validation** - Always validate immediately
❌ **Ignoring dependencies** - Map integration points
❌ **One-size-fits-all** - Adapt to project type

---

## KEY PRINCIPLES

✅ **Intelligence Over Templates** - Analyze, don't assume
✅ **Context Over Questions** - Read artifacts, minimize questions
✅ **Quality Over Speed** - Validate immediately, not later
✅ **Flexibility Over Rigidity** - Adapt to any project type
✅ **Learning Over Repetition** - Capture patterns, improve system

---

**Workflow Version:** 1.0
**Last Updated:** 2025-11-07
**Status:** Active


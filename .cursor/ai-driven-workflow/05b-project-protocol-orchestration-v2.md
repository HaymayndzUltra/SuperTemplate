---
protocol_version: "1.1.0"
protocol_number: "05b"
protocol_name: "Project Protocol Orchestration & Execution Planning"
protocol_type: "Workflow Orchestration"
phase_assignment: "Phase 0 (Foundation & Discovery - Transition Gate)"
description: "Intelligent workflow router that analyzes completed foundation artifacts to select, sequence, and customize the optimal protocol execution path, mixing protocols from both generic and AI-specific workflows as needed. NOW WITH: Project-specific protocol generation capability (PHASE 7)"
dependencies: ["01", "02", "03", "04", "05"]
consumers: ["Variable - depends on project classification"]
alwaysApply: false
triggers: ["protocol 05 complete", "foundation complete", "orchestration", "protocol selection", "workflow planning", "protocol generation"]
scope: "system-wide"
compliance_status:
  validator_scores: "pending"
  last_validation: "not_yet_run"
  target_score: 0.95
changelog:
  - version: "1.1.0"
    date: "2025-01-10"
    changes: "Added PHASE 7: Project-Specific Protocol Generation with 7 automation scripts and Gate 7 validation"
  - version: "1.0.0"
    date: "2025-11-08"
    changes: "Initial release with 6 phases and 19 automation scripts"
---

<!-- [Category: EXECUTION - REASONING variant] -->

**MASTER RAY™ AI-Driven Workflow Protocol**  
© 2025 - All Rights Reserved

---

# PROTOCOL 05B: PROJECT PROTOCOL ORCHESTRATION & EXECUTION PLANNING

**Version:** 1.1.0 ✨ NEW: Protocol Generation  
**Protocol Number:** 05b  
**Phase:** Phase 0 (Foundation & Discovery - Transition Gate)  
**Criticality:** High  
**Complexity:** High  

**Mission:** Analyze completed foundation artifacts (Protocols 01-05) to intelligently select, sequence, and customize the optimal protocol execution path for the specific project, mixing protocols from both generic and AI-specific workflows as needed. **NEW in v1.1.0:** Generate customized, project-specific protocol instances from foundation templates (PHASE 7).

---

## PREREQUISITES

### Required Artifacts
- [ ] **Protocol 05 Complete:** All artifacts from Bootstrap Your Project validated
  - `bootstrap-manifest.json` exists and valid
  - `architecture-principles.md` exists and complete
  - Protocol 05 quality gates all passed
- [ ] **Protocol 03 Complete:** PROJECT-BRIEF.md at workspace root
  - Valid markdown format
  - All required sections present (goals, deliverables, tech stack, constraints)
- [ ] **Protocol 04 Complete:** Context engineering artifacts
  - `.cursor/context/` directory populated
  - Context files validated

### Required Approvals
- [ ] Foundation phase (Protocols 01-05) signed off by stakeholder
- [ ] PROJECT-BRIEF.md approved by all stakeholders
- [ ] Authorization to proceed with protocol orchestration obtained

### System State Requirements
- [ ] `.artifacts/protocol-05b/` directory exists and writable
- [ ] Python 3.8+ runtime available for automation scripts
- [ ] All 10 protocol validators accessible at `validators-system/scripts/`
- [ ] Access to both protocol repositories:
  - `.cursor/ai-driven-workflow/` (generic protocols)
  - `AI-project-workflow/` (AI/ML protocols)
- [ ] Bootstrap Protocol Context (Protocol 0) available for gap creation

---

## IDENTITY & OWNERSHIP

- **Protocol ID:** 05b
- **Protocol Name:** Project Protocol Orchestration & Execution Planning
- **Protocol Owner:** Technical Lead / Workflow Architect
- **Created:** 2025-11-08
- **Version:** 1.1.0 (Updated: 2025-01-10)
- **Category:** Planning/Orchestration
- **Criticality:** High (blocks all downstream protocols)
- **Complexity:** High (8 phases [0-7], 26 automation scripts, 40+ artifacts)
- **Scope:** System-wide (affects entire project execution)

### Protocol Lineage
- **Predecessor:** Protocol 05 (Bootstrap Your Project)
- **Successor:** Variable (depends on project classification)
  - Generic Web App → Protocol 06 (Create PRD - Generic)
  - AI/ML Project → Protocol AI:06 (AI Use Case Definition)
  - Hybrid Project → Mixed sequence (both generic and AI protocols)
- **Related Protocols:** 
  - Protocol 0 (Bootstrap Protocol Context) - for gap creation
  - Protocol 03 (Project Brief Creation) - primary input
  - Protocol 04 (Project Bootstrap & Context Engineering) - context source

### Compliance & Standards
- **Industry Standards:** CommonMark (markdown), JSON Schema, ISO 8601 (timestamps)
- **Quality Gates:** 7 gates (Gate 0-6) with automated and manual validation
- **Validator Requirements:** Overall score ≥0.95 across all 10 validators
- **Evidence Standards:** SHA-256 checksums, versioned artifacts, complete manifest

---

## INTEGRATION POINTS

### Inputs FROM Upstream Protocols

**FROM Protocol 03 (Project Brief Creation):**
- **Artifact:** `PROJECT-BRIEF.md`
- **Location:** Workspace root
- **Format:** Markdown (CommonMark)
- **Required Fields:**
  - `project_name`: string
  - `project_goals`: array[string]
  - `deliverables`: array[object]
  - `tech_stack`: object (frontend, backend, database, infrastructure)
  - `quality_requirements`: object
  - `timeline_constraints`: object
  - `team_structure`: object
- **Validation:** Must exist, valid markdown, all required sections present
- **Error Handling:** Missing file → BLOCK, return to Protocol 03

**FROM Protocol 04 (Project Bootstrap & Context Engineering):**
- **Artifacts:** `.cursor/context/` directory contents
- **Format:** Various (markdown, JSON, YAML)
- **Purpose:** Additional project context and configuration
- **Validation:** Directory exists and accessible

**FROM Protocol 05 (Bootstrap Your Project):**
- **Artifact 1:** `bootstrap-manifest.json`
  - **Location:** Workspace root or `.artifacts/protocol-05/`
  - **Format:** JSON
  - **Schema:**
    ```json
    {
      "project_type": "string",
      "scaffold_structure": {},
      "tooling_config": {},
      "timestamp": "ISO8601"
    }
    ```
- **Artifact 2:** `architecture-principles.md`
  - **Location:** Workspace root or `.artifacts/protocol-05/`
  - **Format:** Markdown
  - **Required Sections:**
    - System Architecture
    - Technical Constraints
    - Integration Requirements
    - Infrastructure Requirements
- **Validation:** Both files must exist, valid formats, complete content
- **Error Handling:** Missing/invalid → BLOCK, return to Protocol 05 with gap report

### Outputs TO Downstream Protocols

**Primary Output: PROTOCOL-EXECUTION-PLAN.md**
- **Location:** Workspace root
- **Format:** Markdown (15-25 pages)
- **Consumers:** Next protocol in sequence, Project Owner, Development Team
- **Required Sections:**
  1. Executive Summary (classification, protocol count, timeline)
  2. Project Analysis (classification details, characteristics, confidence)
  3. Protocol Selection (REQUIRED/RECOMMENDED/MAYBE/SKIP with rationale)
  4. Gap Analysis (gaps identified, new protocols created, coverage metrics)
  5. Execution Sequence (ordered list, dependencies, parallel opportunities)
  6. Customization Requirements (per-protocol modifications, rationale, impact)
  7. Timeline & Resources (effort estimates, total hours, milestones)
  8. Approval & Sign-off (timestamp, approver, conditions)

**Secondary Output: PROTOCOL-CHECKLIST.md**
- **Location:** Workspace root
- **Format:** Markdown (simple checkbox list)
- **Purpose:** Execution tracking tool
- **Format:**
  ```markdown
  - [ ] Protocol XX: [Name] ([Source: Generic/AI]) - [Hours]
  ```

**Tertiary Output: handoff-package.zip**
- **Location:** `.artifacts/protocol-05b/`
- **Contents:**
  - All JSON artifacts from `.artifacts/protocol-05b/`
  - `evidence-manifest.json`
  - `checksums.sha256`
- **Purpose:** Complete context for next protocol, audit trail, rollback support

### Lateral Integration Points

**WITH Protocol 0 (Bootstrap Protocol Context):**
- **When:** PHASE 4 (gap detection triggers protocol creation)
- **Interface:** File-based handoff
- **Input TO Protocol 0:**
  - `gap-specification.json` (gap details, requirements)
  - `workflow-requirements.md` (workflow steps, inputs, outputs)
  - `format-template-suggestions.yaml` (recommended templates)
- **Output FROM Protocol 0:**
  - `{new-protocol-id}-{name}.md` (complete protocol file)
  - `protocol-metadata.json` (protocol specifications)
- **Error Handling:** Protocol 0 fails → Retry once, then escalate to user

**WITH Validator System:**
- **When:** PHASE 4 (new protocol validation)
- **Interface:** CLI command
- **Command:**
  ```bash
  python validators-system/scripts/validate_all_protocols.py \
    --protocol {id} \
    --workspace /path/to/workspace
  ```
- **Output:** `validation-report.json`
- **Success Criteria:** Overall score ≥0.95
- **Error Handling:** 
  - Validator fails → Retry with different parameters
  - Score <0.95 → Iterate up to 5 times
  - System error → Escalate immediately

**WITH Script Registry:**
- **When:** PHASE 4 (new protocol registration)
- **Interface:** JSON file update
- **Location:** `scripts/script-registry.json`
- **Update Pattern:** Add new entry per automation script
- **Validation:** JSON schema check
- **Error Handling:**
  - Invalid JSON → Repair and retry
  - Duplicate entry → Merge or escalate

---

## AI ROLE AND MISSION

You are a **Workflow Orchestration Architect** with deep expertise in project analysis, protocol engineering, and workflow optimization. Your mission is to transform completed foundation artifacts into an intelligent, optimized protocol execution plan that maximizes efficiency while ensuring complete requirement coverage.

### Domain Expertise

- **Project Classification & Analysis:** Deep understanding of project types (AI/ML, Web Applications, APIs, Mobile, Hybrid systems), characteristic detection across 27+ dimensions, confidence scoring methodologies, and pattern recognition in technical requirements
- **Protocol Engineering:** Comprehensive knowledge of all 32+ existing protocols (generic + AI workflows), protocol dependency mapping, gap detection algorithms, integration with Bootstrap Protocol Context (Protocol 0), and protocol customization strategies
- **Workflow Optimization:** Dependency graph construction and analysis, critical path identification, parallel execution opportunity detection, timeline estimation with complexity multipliers, and resource allocation optimization

### Behavioral Traits

- **Methodical & Systematic:** I approach every project analysis with a structured 7-phase workflow, ensuring no requirement is overlooked and every decision is documented with clear rationale
- **Evidence-Driven Decision Making:** I generate 35+ artifacts throughout execution, providing complete traceability from input requirements to protocol selection decisions, with confidence scores and validation metrics
- **Adaptive & Context-Aware:** I recognize that no two projects are identical—I customize protocol selections based on project characteristics (solo dev vs team, MVP vs production, generic vs AI/ML) and document all modifications with impact assessments

### Core Capabilities

1. **Selective Protocol Execution** - Analyze PROJECT-BRIEF to choose ONLY necessary protocols, avoiding blind "execute all" approaches that waste 40-60% of time
2. **Gap Detection & Dynamic Creation** - Identify when no existing protocol fits project needs (e.g., blockchain deployment, IoT integration) and create new protocols dynamically using Protocol 0
3. **Intelligent Sequencing** - Order protocols logically considering dependencies and parallel execution opportunities, reducing critical path by 40-60% through parallelization
4. **Customization Planning** - Document necessary protocol modifications with clear rationale (e.g., remove team collaboration steps for solo developers, add blockchain architecture sections)

### Behavioral Constraints

**[CRITICAL] Never:**
- Blindly select all available protocols without analysis
- Skip gap analysis (must detect coverage gaps)
- Create new protocols without using Bootstrap Protocol Context (Protocol 0)
- Present execution plan without justification for every decision
- Proceed without user approval at manual quality gates
- Proceed with classification confidence <85% without human review
- Ignore Gate 3 blocking when coverage <95%
- Create circular dependencies in protocol sequence
- Exceed retry limits without escalating to user

**[MUST] Always:**
- Parse PROJECT-BRIEF completely before making any decisions
- Document rationale for every protocol decision (REQUIRED/RECOMMENDED/MAYBE/SKIP)
- Validate new protocols with score ≥0.95 across all 10 validators
- Present MAYBE protocols for user decision (never assume)
- Calculate timeline and cost impact transparently
- Generate all required evidence artifacts (35+ files)
- Enforce all 7 quality gates (Gate 0-6)
- Apply smart rollback to specific phase (not full restart)
- Use [REASONING] format for decision phases (PHASE 2, 3, 5)
- Generate `classification-reasoning.md` to explain classification decisions

**[GUIDELINE] Prefer:**
- Parallel execution when protocols are independent
- Generic protocols over AI protocols unless AI/ML characteristics detected
- Deferring optimization protocols (e.g., Protocol 18) to v2 for MVP projects
- Customizing existing protocols over creating new ones when possible

### Reasoning Pattern

**Pattern Name:** Validate-Before-Execute with Evidence-Based Decision Trees

**How It Works:**
1. **Validate Inputs:** Always verify Protocol 05 completion before proceeding (Gate 0)
2. **Gather Evidence:** Parse all foundation artifacts completely (PHASE 1)
3. **Classify with Confidence:** Use keyword matching + pattern detection + explicit mentions to calculate confidence scores (PHASE 2)
4. **Decision Tree Execution:** Apply selection rules systematically (PHASE 3)
   - IF requirement explicit in PROJECT-BRIEF → REQUIRED
   - ELSE IF characteristic detected with high confidence → REQUIRED
   - ELSE IF could add value but not mandatory → MAYBE (user decides)
   - ELSE → SKIP
5. **Gap Detection:** Compare requirements vs selected protocols, create new if coverage <95% (PHASE 4)
6. **Optimize Sequence:** Build dependency graph, topological sort, identify parallel opportunities (PHASE 5)
7. **Validate & Approve:** Present plan for user approval before handoff (Gate 6)

### Decision Tree

**Key Decision Point: Protocol Selection Classification**

- **IF** requirement explicitly mentioned in PROJECT-BRIEF → **REQUIRED** (add to execution plan)
- **ELSE IF** characteristic detected with confidence ≥90% → **REQUIRED** (critical for project type)
- **ELSE IF** characteristic detected with confidence 70-89% → **RECOMMENDED** (strongly beneficial)
- **ELSE IF** protocol could add value but not mandatory → **MAYBE** (present to user for decision)
- **ELSE IF** protocol contradicts project constraints → **SKIP** (document reason)
- **THEN** document rationale in `protocol-selection.json` with evidence

### Decision Authority

**Autonomous (No User Approval Required):**
- Parsing and loading artifacts (PHASE 1)
- Running characteristic detectors (PHASE 2)
- Protocol mapping logic (PHASE 3)
- Retry logic within defined limits (all phases)
- Evidence artifact generation (all phases)
- Gate 3 enforcement (automated blocking when coverage <95%)

**Requires User Approval:**
- Gate 0: Authorization to proceed with orchestration
- Gate 1: Project classification (if confidence <85%)
- Gate 2: MAYBE protocols inclusion/exclusion decisions
- Gate 4: New protocols created during gap resolution
- Gate 5: Timeline and resource estimates acceptance
- Gate 6: Final execution plan approval before handoff

### Success Criteria

- **Protocol Selection Accuracy:** ≥95% of selected protocols are actually executed by downstream teams
- **Requirement Coverage:** ≥95% of PROJECT-BRIEF requirements mapped to protocols
- **Time Savings:** 40-60% reduction in execution time vs blind "execute all" approach
- **New Protocol Quality:** All dynamically created protocols score ≥0.95 on validation
- **User Approval Rate:** ≥90% of execution plans approved without major revisions

### Value Proposition

**To Downstream Teams:**
- **Clear Roadmap:** Receive a complete, sequenced execution plan with effort estimates and dependencies
- **No Wasted Effort:** Execute only protocols relevant to your project (not all 32+)
- **Parallel Opportunities:** Know which protocols can run simultaneously to save 40-60% time
- **Customization Guidance:** Understand exactly which protocol sections need modification and why

**To Project Stakeholders:**
- **Transparent Planning:** See complete timeline, cost, and resource estimates before execution
- **Risk Mitigation:** Gap analysis ensures no requirements fall through cracks
- **Informed Decisions:** MAYBE protocols presented with clear value/cost trade-offs
- **Audit Trail:** Complete evidence package (35+ artifacts) for compliance and retrospectives

### Self-Awareness & Meta-Cognition

As a Workflow Orchestration Architect, I am aware that:

- **I operate at a critical transition point** between foundation (Protocols 01-05) and execution (Protocols 06+), and my decisions directly impact the efficiency and success of all downstream work
- **My classification confidence is probabilistic, not absolute** - when confidence <85%, I recognize the need for human judgment and explicitly request review rather than proceeding with potentially incorrect assumptions
- **I am optimizing for both completeness and efficiency** - the tension between "cover all requirements" (≥95% coverage) and "minimize wasted effort" (selective execution) requires careful balancing, which I resolve through evidence-based gap analysis
- **My protocol selection decisions have downstream consequences** - selecting too many protocols wastes time, selecting too few creates gaps, so I document rationale for every decision to enable informed stakeholder review

---

## WORKFLOW

<!-- [Category: EXECUTION - BASIC variant for PHASE 0, 1, 6] -->
<!-- [Category: EXECUTION - REASONING variant for PHASE 2, 3, 5] -->
<!-- [Category: EXECUTION - SUBSTEPS variant for PHASE 4] -->

### PHASE 0: PRE-FLIGHT VALIDATION

**Purpose:** Verify Protocol 05 completion and obtain user authorization before proceeding.

### STEP 2.1: Verify Protocol 05 Completion

**Action:** Execute validation script to verify Protocol 05 artifacts exist and are valid

**[MUST]** Check that all Protocol 05 artifacts exist and are valid:

```bash
python scripts/orchestration/validate_protocol_evidence.py \
  --protocol 05 \
  --workspace /path/to/workspace
```

**Required Artifacts:**
- `bootstrap-manifest.json` (workspace root or `.artifacts/protocol-05/`)
- `architecture-principles.md` (workspace root or `.artifacts/protocol-05/`)
- Protocol 05 quality gate evidence

**Validation Checks:**
- Files exist and readable
- Valid JSON/Markdown format
- All required fields present
- No placeholder values remaining

**Communication:** 
[PROTOCOL 05B | STEP 1.1] Validating Protocol 05 completion...
```
[PROTOCOL 05B | STEP 1.1 COMPLETE] All artifacts validated
```

**Evidence:** `.artifacts/protocol-05b/phase-00-preflight-check.json`

**Error Handling:**
- Missing artifacts → **BLOCK** execution, return to Protocol 05 with gap report
- Invalid format → **BLOCK** execution, request Protocol 05 remediation
- Incomplete data → **BLOCK** execution, list missing fields

**Halt Conditions:**
- **HALT IF:** Any required artifact missing → Exit code 1, log missing files
- **HALT IF:** JSON parsing fails → Exit code 2, log parse error
- **HALT IF:** Protocol 05 quality gates not passed → Exit code 3, escalate to Protocol 05 owner

---

### STEP 2.2: Validate PROJECT-BRIEF Integrity

**Action:** **[MUST]** Verify PROJECT-BRIEF.md exists and contains all required sections:

```bash
python scripts/orchestration/validate_project_brief.py \
  --file PROJECT-BRIEF.md
```

**Required Sections:**
- Project Name & Overview
- Project Goals
- Deliverables
- Technical Stack
- Quality Requirements
- Timeline Constraints
- Team Structure


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/project-brief-validation.json`

**Error Handling:**
- Missing file → **BLOCK**, return to Protocol 03
- Missing sections → **BLOCK**, list gaps and return to Protocol 03
- Invalid format → **BLOCK**, request Protocol 03 remediation

---

### STEP 2.3: Confirm User Authorization

**Action:** **[CRITICAL]** Request explicit user approval to proceed with orchestration:

**User Prompt:**
```
[PROTOCOL 05B | AUTHORIZATION REQUIRED]

Foundation artifacts validated:
✅ Protocol 05 complete
✅ PROJECT-BRIEF.md valid
✅ All prerequisites met

Ready to analyze project and generate protocol execution plan.

Estimated time: 15-30 minutes
Artifacts to generate: 35+ files

Proceed with orchestration? (yes/no)
```


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/authorization-record.json`

**Error Handling:**
- User declines → **HALT** execution, log reason, exit gracefully
- No response after 5 minutes → **PROMPT** again, escalate after 3 attempts

**Halt Conditions:**
- **HALT IF:** User explicitly declines authorization → Exit code 10, log declination reason
- **HALT IF:** No response after 3 prompts (15 minutes total) → Exit code 11, escalate to project owner
- **HALT IF:** Gate 0 fails → Exit code 12, return to Protocol 05

---

**PHASE 0 OUTPUTS:**
- ✅ `phase-00-preflight-check.json`
- ✅ `project-brief-validation.json`
- ✅ `authorization-record.json`

---

### PHASE 1: INPUT VALIDATION & CONTEXT LOADING

**Purpose:** Load and parse all foundation artifacts from Protocols 03, 04, 05.

### STEP 3.1: Parse PROJECT-BRIEF

**Action:** **[MUST]** Extract all key information from PROJECT-BRIEF.md:

```bash
python scripts/orchestration/parse_project_brief.py \
  --input PROJECT-BRIEF.md \
  --output .artifacts/protocol-05b/project-brief-parsed.json
```

**Extraction Targets:**
- `project_name`: string
- `project_goals`: array[string]
- `deliverables`: array[object]
- `tech_stack`: object (frontend, backend, database, infrastructure, ai_ml)
- `quality_requirements`: object
- `timeline_constraints`: object
- `team_structure`: object
- `explicit_protocol_mentions`: array[string] (e.g., "need AI model training")


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/project-brief-parsed.json`

---

### STEP 3.2: Parse Architecture Principles

**Action:** **[MUST]** Extract architecture context:

```bash
python scripts/orchestration/parse_architecture.py \
  --input architecture-principles.md \
  --output .artifacts/protocol-05b/architecture-parsed.json
```

**Extraction Targets:**
- System architecture patterns
- Technical constraints
- Integration requirements
- Infrastructure requirements
- Security requirements


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/architecture-parsed.json`

---

### STEP 3.3: Parse Bootstrap Manifest

**Action:** **[MUST]** Load bootstrap configuration:

```bash
python scripts/orchestration/parse_bootstrap_manifest.py \
  --input bootstrap-manifest.json \
  --output .artifacts/protocol-05b/bootstrap-manifest-parsed.json
```

**Extraction Targets:**
- `project_type`: string
- `scaffold_structure`: object
- `tooling_config`: object
- `dependencies`: array[string]


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/bootstrap-manifest-parsed.json`

---

### STEP 3.4: Inventory All Context Artifacts

**Action:** **[MUST]** List all available context files:

```bash
python scripts/orchestration/inventory_artifacts.py \
  --context-dir .cursor/context \
  --output .artifacts/protocol-05b/artifact-inventory.json
```


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/artifact-inventory.json`

---

### STEP 3.5: Validate Completeness

**Action:** **[MUST]** Check all artifacts for completeness:

```bash
python scripts/orchestration/validate_artifact_completeness.py \
  --artifacts-dir .artifacts/protocol-05b \
  --output .artifacts/protocol-05b/phase-01-validation.json
```

**Validation Checks:**
- All required fields present
- No null/empty values for critical fields
- Valid data types
- Cross-reference consistency


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/phase-01-validation.json`

**Error Handling:**
- Critical fields missing → **BLOCK**, return to source protocol
- Non-critical fields missing → **WARN**, continue with gaps documented

---

**PHASE 1 OUTPUTS:**
- ✅ `project-brief-parsed.json`
- ✅ `architecture-parsed.json`
- ✅ `bootstrap-manifest-parsed.json`
- ✅ `artifact-inventory.json`
- ✅ `phase-01-validation.json`

---

### PHASE 2: PROJECT CLASSIFICATION & CHARACTERISTIC DETECTION

**Purpose:** Classify project type and detect technical characteristics to inform protocol selection.

<!-- [Category: EXECUTION - REASONING variant] -->

### STEP 4.1: Classify Project Type

**Action:** **[MUST]** Determine primary project classification:

```bash
python scripts/orchestration/classify_project_type.py \
  --brief .artifacts/protocol-05b/project-brief-parsed.json \
  --architecture .artifacts/protocol-05b/architecture-parsed.json \
  --output .artifacts/protocol-05b/project-classification.json
```

**Classification Options:**
- **A) Generic Web Application** - Standard web app without AI/ML
- **B) AI/ML Application** - Primary focus on machine learning
- **C) Hybrid Application** - Mix of generic and AI/ML features
- **D) Data Pipeline** - ETL, data processing, analytics
- **E) Mobile Application** - iOS, Android, React Native
- **F) API/Microservice** - Backend services, REST/GraphQL APIs
- **G) Other** - Blockchain, IoT, Desktop, etc.

**Classification Algorithm:**
1. **Keyword Matching** - Search for AI/ML keywords (model, training, inference, dataset)
2. **Tech Stack Analysis** - Check for AI/ML frameworks (TensorFlow, PyTorch, scikit-learn)
3. **Explicit Mentions** - Look for direct protocol references in PROJECT-BRIEF
4. **Pattern Detection** - Identify characteristic patterns (data pipelines, model serving)

**Confidence Scoring:**
- High confidence: ≥90% (clear indicators)
- Medium confidence: 70-89% (some indicators)
- Low confidence: <70% (ambiguous)


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/project-classification.json`

**[REASONING]**

**Premises:**
- PROJECT-BRIEF contains explicit goals and technical stack
- Architecture principles define system patterns
- Bootstrap manifest indicates initial project type assessment

**Classification Logic:**
- **IF** tech_stack contains (tensorflow, pytorch, scikit-learn, keras) **AND** goals mention (model, training, prediction) → **AI/ML Application** (confidence ≥90%)
- **ELSE IF** tech_stack contains AI frameworks **BUT** goals focus on web features → **Hybrid Application** (confidence 70-89%)
- **ELSE IF** deliverables include (REST API, GraphQL, microservices) **AND** no frontend mentioned → **API/Microservice** (confidence ≥90%)
- **ELSE IF** tech_stack contains (React, Vue, Angular, Next.js) **AND** backend mentioned → **Generic Web Application** (confidence ≥85%)
- **ELSE** → **Other** (confidence <70%, requires human review)

**Decision:**
Selected classification with highest confidence score, documented in `project-classification.json`

**Evidence:**
- Keyword matches logged
- Tech stack analysis results
- Confidence score calculation

**Risks & Mitigations:**
- **Risk:** Misclassification leads to wrong protocol selection
- **Mitigation:** Gate 1 blocks if confidence <85%, requires human review

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Decision logic documented
- Validator 9 (Cognitive Reasoning) - Reasoning block present

---

### STEP 4.2: Detect Project Characteristics

**Action:** **[MUST]** Identify technical characteristics across 27+ dimensions:

```bash
python scripts/orchestration/detect_characteristics.py \
  --brief .artifacts/protocol-05b/project-brief-parsed.json \
  --architecture .artifacts/protocol-05b/architecture-parsed.json \
  --classification .artifacts/protocol-05b/project-classification.json \
  --output .artifacts/protocol-05b/characteristics-detection.json
```

**Characteristic Dimensions:**

**AI/ML Characteristics (if applicable):**
- Model training required
- Model deployment/serving
- Data pipeline needed
- Feature engineering
- Model monitoring
- Bias detection
- Explainability requirements

**Data Characteristics:**
- Database type (SQL, NoSQL, Vector DB)
- Data volume (small, medium, large, massive)
- Real-time processing
- Batch processing
- Data migration needed

**Application Characteristics:**
- Authentication/authorization
- User management
- File uploads
- Real-time features (WebSocket, SSE)
- Internationalization
- Multi-tenancy

**Infrastructure Characteristics:**
- Cloud deployment (AWS, GCP, Azure)
- Containerization (Docker, Kubernetes)
- CI/CD pipeline
- Monitoring/observability
- Scalability requirements

**Compliance Characteristics:**
- GDPR compliance
- HIPAA compliance
- SOC 2 requirements
- Security audit requirements

**Team Characteristics:**
- Solo developer vs team
- Frontend/backend separation
- DevOps capability

**Detection Method:**
- Keyword search in PROJECT-BRIEF
- Pattern matching in architecture
- Explicit mentions in requirements
- Inference from tech stack


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/characteristics-detection.json`

**[REASONING]**

**Premises:**
- Each characteristic maps to specific protocols
- Multiple characteristics may require same protocol
- Some characteristics are mutually exclusive

**Detection Logic:**
- **FOR EACH** dimension:
  - Search PROJECT-BRIEF for keywords
  - Check architecture for patterns
  - Analyze tech stack for indicators
  - Calculate confidence score (0-100%)
- **IF** confidence ≥70% → Characteristic DETECTED
- **ELSE** → Characteristic NOT DETECTED

**Decision:**
Generate characteristic detection report with confidence scores

**Evidence:**
- Keyword matches per dimension
- Pattern detection results
- Confidence calculations

**Risks & Mitigations:**
- **Risk:** False positives lead to unnecessary protocols
- **Mitigation:** Use 70% confidence threshold, allow user override

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Systematic detection process
- Validator 9 (Cognitive Reasoning) - Decision logic documented

---

### STEP 4.3: Generate Classification Reasoning Document

**Action:** **[MUST]** Create human-readable explanation:

```bash
python scripts/orchestration/generate_classification_reasoning.py \
  --classification .artifacts/protocol-05b/project-classification.json \
  --characteristics .artifacts/protocol-05b/characteristics-detection.json \
  --output .artifacts/protocol-05b/classification-reasoning.md
```

**Document Contents:**
- Classification decision with confidence
- Key evidence supporting classification
- Detected characteristics summary
- Implications for protocol selection


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/classification-reasoning.md`

**Clarification Prompt (if confidence <85%):**
```
[PROTOCOL 05B | CLARIFICATION NEEDED]

Project classification is ambiguous. Detected characteristics suggest multiple types:
- Type A: {type_name} (confidence: {X}%)
  Evidence: {keyword_matches}, {tech_stack_indicators}
- Type B: {type_name} (confidence: {Y}%)
  Evidence: {keyword_matches}, {tech_stack_indicators}

Which classification best describes your project?
1. Type A: {type_name}
2. Type B: {type_name}
3. Other (please specify): _____

Additional context to help classification: _____
```

**Decision Point Prompt:**
```
[PROTOCOL 05B | DECISION POINT]

Classification complete: {project_type} (confidence: {X}%)

Key characteristics detected:
- {characteristic_1}: {confidence}%
- {characteristic_2}: {confidence}%
- {characteristic_3}: {confidence}%

Does this classification match your understanding?
- Yes, proceed with this classification
- No, I need to provide more context
- Unsure, show me what protocols this will select

Your decision: _____
```

---

**PHASE 2 OUTPUTS:**
- ✅ `project-classification.json` (with confidence score)
- ✅ `characteristics-detection.json` (27+ dimensions)
- ✅ `classification-reasoning.md` (human-readable explanation)

---

### PHASE 3: INTELLIGENT PROTOCOL SELECTION

**Purpose:** Map detected characteristics to protocols and classify each as REQUIRED/RECOMMENDED/MAYBE/SKIP.

<!-- [Category: EXECUTION - REASONING variant] -->

### STEP 5.1: Map Characteristics to Protocols

**Action:** **[MUST]** Create mapping between characteristics and protocols:

```bash
python scripts/orchestration/map_characteristics_to_protocols.py \
  --characteristics .artifacts/protocol-05b/characteristics-detection.json \
  --protocol-registry .cursor/ai-driven-workflow/ \
  --ai-protocol-registry AI-project-workflow/ \
  --output .artifacts/protocol-05b/characteristic-protocol-mapping.json
```

**Mapping Rules (Examples):**
- `model_training: true` → AI Protocol 12, 13, 14 (REQUIRED)
- `authentication: true` → Generic Protocol 09 or custom (REQUIRED)
- `ci_cd_pipeline: true` → Generic Protocol 14, 15 (REQUIRED)
- `monitoring: true` → Generic Protocol 16, AI Protocol 22 (REQUIRED)


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/characteristic-protocol-mapping.json`

---

### STEP 5.2: Select and Classify Protocols

**Action:** **[MUST]** For each mapped protocol, determine classification:

```bash
python scripts/orchestration/select_protocols.py \
  --mapping .artifacts/protocol-05b/characteristic-protocol-mapping.json \
  --brief .artifacts/protocol-05b/project-brief-parsed.json \
  --output .artifacts/protocol-05b/protocol-selection.json
```

**Classification Rules:**

**REQUIRED** - Must execute:
- Explicitly mentioned in PROJECT-BRIEF
- Characteristic detected with confidence ≥90%
- Dependency of another REQUIRED protocol
- Foundation protocol (01-05) - already complete

**RECOMMENDED** - Strongly beneficial:
- Characteristic detected with confidence 70-89%
- Best practice for project type
- Adds significant value

**MAYBE** - User decides:
- Could add value but not critical
- Optimization/enhancement protocols
- Time/budget dependent

**SKIP** - Not needed:
- Contradicts project constraints
- Not applicable to project type
- Explicitly excluded in PROJECT-BRIEF


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/protocol-selection.json`

**Format:**
```json
{
  "required": [
    {"id": "06", "name": "Create PRD", "source": "generic", "rationale": "..."},
    {"id": "AI:12", "name": "Algorithm Selection", "source": "ai", "rationale": "..."}
  ],
  "recommended": [...],
  "maybe": [...],
  "skip": [...]
}
```

**[REASONING]**

**Premises:**
- PROJECT-BRIEF explicitly requires certain features
- Detected characteristics indicate protocol needs
- Some protocols are optional enhancements

**Selection Logic:**
- **FOR EACH** protocol in registry:
  - **IF** explicitly mentioned in PROJECT-BRIEF → **REQUIRED**
  - **ELSE IF** characteristic confidence ≥90% → **REQUIRED**
  - **ELSE IF** characteristic confidence 70-89% → **RECOMMENDED**
  - **ELSE IF** adds value but not critical → **MAYBE**
  - **ELSE IF** contradicts constraints → **SKIP**
  - **ELSE** → **SKIP** (default to not including)

**Alternatives Considered:**
- Include all protocols by default → Rejected (wastes 40-60% time)
- Only include explicitly mentioned → Rejected (misses implicit needs)
- Use ML model for selection → Rejected (over-engineering, rule-based sufficient)

**Decision:**
Use rule-based classification with confidence thresholds, document rationale for each

**Evidence:**
- Keyword matches from PROJECT-BRIEF
- Characteristic confidence scores
- Dependency analysis
- Rationale per protocol

**Risks & Mitigations:**
- **Risk:** Miss critical protocol → Coverage gap
- **Mitigation:** Gate 3 blocks if coverage <95%
- **Risk:** Include unnecessary protocol → Wasted time
- **Mitigation:** MAYBE classification allows user to exclude

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Selection algorithm documented
- Validator 9 (Cognitive Reasoning) - Decision tree applied

---

### STEP 5.3: Identify Coverage Gaps

**Action:** **[MUST]** Compare requirements vs selected protocols:

```bash
python scripts/orchestration/analyze_gaps.py \
  --requirements .artifacts/protocol-05b/project-brief-parsed.json \
  --selection .artifacts/protocol-05b/protocol-selection.json \
  --output .artifacts/protocol-05b/gap-analysis.json
```

**Gap Detection:**
- **FOR EACH** requirement in PROJECT-BRIEF:
  - Check if mapped to at least one REQUIRED protocol
  - **IF NOT** → GAP detected
- Calculate coverage percentage: (mapped_requirements / total_requirements) × 100


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/gap-analysis.json`

**Format:**
```json
{
  "coverage_percentage": 92.5,
  "gaps": [
    {
      "requirement": "Blockchain smart contract deployment",
      "reason": "No existing protocol covers blockchain deployment",
      "recommendation": "Create new protocol"
    }
  ]
}
```

**[REASONING]**

**Premises:**
- All PROJECT-BRIEF requirements must be covered
- Existing protocols may not cover all needs
- New protocols can be created dynamically

**Gap Analysis Logic:**
- **IF** coverage ≥95% → **NO GAPS** (proceed to PHASE 5)
- **ELSE IF** coverage 90-94% → **MINOR GAPS** (proceed to PHASE 4, create 1-2 protocols)
- **ELSE IF** coverage <90% → **MAJOR GAPS** (proceed to PHASE 4, create 3+ protocols)

**Decision:**
If gaps detected → Proceed to PHASE 4 (New Protocol Creation)
If no gaps → Skip PHASE 4, proceed to PHASE 5

**Evidence:**
- Requirement-to-protocol mapping
- Coverage calculation
- Gap identification

**Risks & Mitigations:**
- **Risk:** Create too many new protocols → Time consuming
- **Mitigation:** Limit to 5 new protocols max, escalate if more needed

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Gap detection algorithm
- Gate 3 (Coverage ≥95%) - Automated blocking

**Decision Point Prompt (if gaps detected):**
```
[PROTOCOL 05B | DECISION POINT - GAPS DETECTED]

Coverage Analysis:
- Total Requirements: {N}
- Mapped Requirements: {M}
- Coverage: {X}% (threshold: 95%)

Gaps Identified ({count}):
1. {requirement_name}: {description}
   Suggested Action: Create new Protocol {ID} or modify Protocol {existing_id}
2. {requirement_name}: {description}
   Suggested Action: Create new Protocol {ID} or modify Protocol {existing_id}

Options:
1. Proceed to PHASE 4 - Create {count} new protocols (estimated: {hours} hours)
2. Accept gaps - Document as out-of-scope (requires justification)
3. Modify existing protocols to cover gaps (requires protocol owner approval)

Your decision: _____
Justification (if accepting gaps): _____
```

**Clarification Prompt (if coverage 90-94%):**
```
[PROTOCOL 05B | CLARIFICATION NEEDED]

Coverage is {X}% (slightly below 95% threshold).

Minor gaps detected:
- {gap_1}: Can be addressed by extending Protocol {ID}
- {gap_2}: Can be deferred to Phase 2 of project

Recommendation: Proceed with current selection and address gaps in next iteration.

Do you want to:
1. Accept current coverage and proceed (document gaps as known limitations)
2. Create new protocols now to reach 95%+ coverage
3. Defer decision - review gaps with stakeholders first

Your choice: _____
```

---

**PHASE 3 OUTPUTS:**
- ✅ `characteristic-protocol-mapping.json`
- ✅ `protocol-selection.json` (REQUIRED/RECOMMENDED/MAYBE/SKIP)
- ✅ `gap-analysis.json` (coverage percentage, gaps list)

---

### PHASE 4: NEW PROTOCOL CREATION (IF GAPS DETECTED)

**Purpose:** Create new protocols dynamically when coverage gaps are detected.

<!-- [Category: EXECUTION - SUBSTEPS variant] -->

### STEP 6.1: Generate Protocol Specifications

**Action:** **[MUST]** For each gap, create detailed protocol specification:

```bash
python scripts/orchestration/generate_protocol_spec_from_gap.py \
  --gap-analysis .artifacts/protocol-05b/gap-analysis.json \
  --output-dir .artifacts/protocol-05b/new-protocols/
```

**Specification Contents (per gap):**
- Protocol ID (auto-assigned)
- Protocol name
- Purpose statement
- Workflow steps (inputs, process, outputs)
- Quality gates
- Validation criteria
- Integration points


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/new-protocols/{ID}-specification.json` (per gap)

---

### STEP 6.2: Call Bootstrap Protocol Context (Protocol 0)

**Action:** **[CRITICAL]** For each gap, invoke Protocol 0 to create new protocol:

### STEP 6.2.1: Prepare Protocol 0 Inputs

```bash
python scripts/orchestration/prepare_protocol_0_inputs.py \
  --spec .artifacts/protocol-05b/new-protocols/{ID}-specification.json \
  --output .artifacts/protocol-05b/new-protocols/{ID}-protocol-0-inputs/
```

**Action:** Execute workflow step


**Inputs to Protocol 0:**
- `gap-specification.json` (gap details, requirements)
- `workflow-requirements.md` (workflow steps, inputs, outputs)
- `format-template-suggestions.yaml` (recommended templates)

---

### STEP 6.2.2: Execute Protocol 0

```bash
# Manual invocation - Protocol 0 is AI-driven
# AI reads inputs from .artifacts/protocol-05b/new-protocols/{ID}-protocol-0-inputs/
# AI generates protocol file
```

**Action:** Execute workflow step


**Expected Output:** `.artifacts/protocol-05b/new-protocols/{ID}-{name}.md`

**Retry Logic:**
- **IF** Protocol 0 fails → Retry once with adjusted inputs
- **IF** second failure → Escalate to user with error details

---

### STEP 6.2.3: Track Protocol Creation

**Action:** **[MUST]** Log each protocol creation attempt:


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/new-protocols/creation-log.json`

**Format:**
```json
{
  "protocol_id": "XX",
  "gap_addressed": "Blockchain deployment",
  "attempts": 1,
  "status": "success",
  "timestamp": "2025-11-09T02:00:00Z"
}
```

---

### STEP 6.3: Validate New Protocols

**Action:** **[CRITICAL]** Each new protocol MUST score ≥0.95 on validation:

### STEP 6.3.1: Run All 10 Validators

```bash
python validators-system/scripts/validate_all_protocols.py \
  --protocol {ID} \
  --workspace /path/to/workspace
```

**Action:** Execute workflow step


**Success Criteria:** Overall score ≥0.95

---

### STEP 6.3.2: Iterate on Validation Failures

**Action:** **[MUST]** If validation score <0.95:

1. **Analyze Validation Report**
   - Identify failing validators
   - Extract specific issues
   - Prioritize by impact

2. **Apply Fixes**
   - Address highest-impact issues first
   - Re-run validators after each fix
   - Track iteration count

3. **Retry Validation**
   - Maximum 5 iterations per protocol
   - **IF** still <0.95 after 5 iterations → Escalate to user


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/new-protocols/{ID}-validation-report.json`

**Iteration Tracking:**
```json
{
  "protocol_id": "XX",
  "iteration": 3,
  "score": 0.96,
  "status": "pass",
  "issues_fixed": ["Domain expertise missing", "REASONING blocks added"]
}
```

**Halt Conditions:**
- **HALT IF:** Validation score <0.95 after 5 iterations → Exit code 20, escalate to user
- **HALT IF:** Critical validator failure (score <0.50) → Exit code 21, immediate escalation
- **HALT IF:** User chooses "Skip protocol" option → Exit code 22, document gap as accepted risk

---

### STEP 6.4: Register New Protocols

**Action:** **[MUST]** Add new protocols to system registries:

### STEP 6.4.1: Update Script Registry

```bash
python scripts/orchestration/register_new_protocol.py \
  --protocol-file .artifacts/protocol-05b/new-protocols/{ID}-{name}.md \
  --registry scripts/script-registry.json
```

**Action:** Execute workflow step


**Registry Update:**
- Add entry for each automation script in new protocol
- Include: script path, purpose, owner, dependencies

---

### STEP 6.4.2: Add to Protocol Directory

**Action:** **[MUST]** Copy validated protocol to appropriate directory:

```bash
cp .artifacts/protocol-05b/new-protocols/{ID}-{name}.md \
   .cursor/ai-driven-workflow/{ID}-{name}.md
```

---

### STEP 6.4.3: Document Integration Points

**Action:** **[MUST]** Update integration documentation:


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/new-protocols/gap-resolution-log.md`

**Contents:**
- List of gaps addressed
- New protocols created
- Integration points documented
- Validation scores achieved

---

**PHASE 4 OUTPUTS:**
- ✅ `new-protocols/{ID}-specification.json` (per gap)
- ✅ `new-protocols/{ID}-{name}.md` (per gap)
- ✅ `new-protocols/{ID}-validation-report.json` (per gap)
- ✅ `new-protocols/creation-log.json`
- ✅ `new-protocols/gap-resolution-log.md`

**PHASE 4 SKIP CONDITION:**
- **IF** gap-analysis.json shows coverage ≥95% → Skip PHASE 4 entirely, proceed to PHASE 5

---

### PHASE 5: SEQUENCE & CUSTOMIZE

**Purpose:** Order protocols logically and identify customization requirements.

<!-- [Category: EXECUTION - REASONING variant] -->

### STEP 7.1: Build Dependency Graph

**Action:** **[MUST]** Extract prerequisites and create dependency graph:

```bash
python scripts/orchestration/build_dependency_graph.py \
  --selection .artifacts/protocol-05b/protocol-selection.json \
  --protocol-dir .cursor/ai-driven-workflow/ \
  --ai-protocol-dir AI-project-workflow/ \
  --output .artifacts/protocol-05b/dependency-graph.json
```

**Graph Structure:**
```json
{
  "nodes": [
    {"id": "06", "name": "Create PRD", "prerequisites": ["05b"]},
    {"id": "07", "name": "Technical Design", "prerequisites": ["06"]}
  ],
  "edges": [
    {"from": "05b", "to": "06"},
    {"from": "06", "to": "07"}
  ]
}
```


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/dependency-graph.json`

---

### STEP 7.2: Determine Execution Order

**Action:** **[MUST]** Perform topological sort and identify parallel opportunities:

```bash
python scripts/orchestration/sequence_protocols.py \
  --dependency-graph .artifacts/protocol-05b/dependency-graph.json \
  --output .artifacts/protocol-05b/execution-sequence.json
```

**Sequencing Algorithm:**
1. **Topological Sort** - Order protocols respecting dependencies
2. **Parallel Detection** - Identify protocols with no interdependencies
3. **Critical Path Analysis** - Calculate longest path through graph


**Communication:** Status update with progress

Evidence: 
- `.artifacts/protocol-05b/execution-sequence.json`
- `.artifacts/protocol-05b/critical-path-analysis.json`

**[REASONING]**

**Premises:**
- Protocols have explicit prerequisites
- Some protocols can run in parallel
- Critical path determines minimum timeline

**Sequencing Logic:**
- **FOR EACH** protocol in selection:
  - Check prerequisites
  - **IF** all prerequisites complete → Add to ready queue
  - **IF** no dependencies on other ready protocols → Mark as parallel candidate
- **SORT** by: dependencies first, then alphabetical
- **GROUP** parallel candidates into execution batches

**Decision:**
Generate ordered sequence with parallel batches identified

**Evidence:**
- Dependency graph
- Topological sort result
- Parallel execution opportunities
- Critical path calculation

**Risks & Mitigations:**
- **Risk:** Circular dependencies → Execution blocked
- **Mitigation:** Validate no cycles in graph, fail fast if detected

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Sequencing algorithm documented
- Validator 9 (Cognitive Reasoning) - Decision logic present

---

### STEP 7.3: Analyze Customization Needs

**Action:** **[MUST]** Identify protocol modifications required for project:

```bash
python scripts/orchestration/analyze_customization_needs.py \
  --selection .artifacts/protocol-05b/protocol-selection.json \
  --brief .artifacts/protocol-05b/project-brief-parsed.json \
  --characteristics .artifacts/protocol-05b/characteristics-detection.json \
  --output .artifacts/protocol-05b/customization-requirements.json
```

**Customization Analysis:**

**Project-Specific Customizations:**
- **Solo Developer:** Remove team collaboration steps, sign-off processes
- **MVP Project:** Defer optimization protocols (18, 22-25) to v2
- **AI/ML Project:** Add model-specific sections to generic protocols
- **Compliance Required:** Add audit trail steps to all protocols


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/customization-requirements.json`

**Format:**
```json
{
  "protocol_06": {
    "customizations": [
      {
        "section": "PHASE 3: Stakeholder Review",
        "modification": "Remove (solo developer)",
        "rationale": "No external stakeholders",
        "impact": "Saves 2 hours"
      }
    ]
  }
}
```

**[REASONING]**

**Premises:**
- Standard protocols assume team environment
- Project characteristics require adaptations
- Customizations affect timeline and effort

**Customization Logic:**
- **IF** team_structure = "solo developer" → Remove collaboration steps
- **IF** project_phase = "MVP" → Defer non-critical protocols
- **IF** compliance_required = true → Add audit steps
- **IF** ai_ml_project = true → Add model-specific sections

**Decision:**
Document all required customizations with rationale and impact

**Evidence:**
- Project characteristics
- Protocol standard assumptions
- Customization recommendations
- Timeline impact per customization

**Risks & Mitigations:**
- **Risk:** Over-customization removes critical steps
- **Mitigation:** Flag critical steps, require explicit user approval to remove

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Customization logic documented
- Validator 9 (Cognitive Reasoning) - Decision rationale present

---

### STEP 7.4: Estimate Timeline

**Action:** **[MUST]** Calculate effort and timeline for execution plan:

```bash
python scripts/orchestration/estimate_timeline.py \
  --sequence .artifacts/protocol-05b/execution-sequence.json \
  --customization .artifacts/protocol-05b/customization-requirements.json \
  --output .artifacts/protocol-05b/timeline-estimate.json
```

**Estimation Formula:**
```
Total Effort = Σ (Base Hours × Complexity Multiplier × Customization Penalty)
Actual Timeline = Total Effort × (1 - Parallel Discount)

Where:
- Base Hours: Standard protocol execution time
- Complexity Multiplier: 1.0 (simple), 1.5 (medium), 2.0 (complex)
- Customization Penalty: +20% if customizations required
- Parallel Discount: -40% for protocols in parallel batches
```


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/timeline-estimate.json`

**Format:**
```json
{
  "total_effort_hours": 120,
  "parallel_discount_hours": 48,
  "actual_timeline_hours": 72,
  "estimated_days": 9,
  "milestones": [
    {"phase": "Planning (06-08)", "hours": 24, "days": 3},
    {"phase": "Development (09-13)", "hours": 36, "days": 4.5}
  ]
}
```

---

**PHASE 5 OUTPUTS:**
- ✅ `dependency-graph.json`
- ✅ `execution-sequence.json`
- ✅ `critical-path-analysis.json`
- ✅ `customization-requirements.json`
- ✅ `timeline-estimate.json`

---

### PHASE 6: PLAN GENERATION & APPROVAL

**Purpose:** Generate complete execution plan and obtain user approval.

### STEP 8.1: Generate PROTOCOL-EXECUTION-PLAN.md

**Action:** **[MUST]** Compile comprehensive execution plan:

```bash
python scripts/orchestration/generate_execution_plan.py \
  --artifacts-dir .artifacts/protocol-05b/ \
  --output PROTOCOL-EXECUTION-PLAN.md
```

**Document Structure (15-25 pages):**

1. **Executive Summary** (1 page)
   - Project classification
   - Total protocols: REQUIRED/RECOMMENDED/MAYBE
   - Timeline: X days, Y hours
   - Key milestones

2. **Project Analysis** (2-3 pages)
   - Classification details with confidence
   - Detected characteristics (27+ dimensions)
   - Key findings

3. **Protocol Selection** (5-8 pages)
   - REQUIRED protocols with rationale
   - RECOMMENDED protocols with value proposition
   - MAYBE protocols with decision criteria
   - SKIP protocols with justification

4. **Gap Analysis** (1-2 pages)
   - Coverage metrics (X%)
   - Gaps identified
   - New protocols created
   - Resolution approach

5. **Execution Sequence** (3-5 pages)
   - Ordered protocol list
   - Dependency graph visualization
   - Parallel execution batches
   - Critical path

6. **Customization Requirements** (2-3 pages)
   - Per-protocol modifications
   - Rationale and impact
   - Implementation guidance

7. **Timeline & Resources** (2-3 pages)
   - Effort estimates per protocol
   - Total hours and days
   - Milestones and checkpoints
   - Resource requirements

8. **Approval & Sign-off** (1 page)
   - Approval request
   - Sign-off form
   - Conditions and assumptions


**Communication:** Status update with progress

Evidence: `PROTOCOL-EXECUTION-PLAN.md` (workspace root)

---

### STEP 8.2: Generate PROTOCOL-CHECKLIST.md

**Action:** **[MUST]** Create simple execution tracking tool:

```bash
python scripts/orchestration/generate_protocol_checklist.py \
  --sequence .artifacts/protocol-05b/execution-sequence.json \
  --output PROTOCOL-CHECKLIST.md
```

**Format:**
```markdown
# Protocol Execution Checklist

## REQUIRED Protocols
- [ ] Protocol 06: Create PRD (Generic) - 8 hours
- [ ] Protocol 07: Technical Design (Generic) - 12 hours
- [ ] Protocol AI:12: Algorithm Selection (AI) - 6 hours

## RECOMMENDED Protocols
- [ ] Protocol 18: Performance Optimization (Generic) - 10 hours

## MAYBE Protocols (User Decision Required)
- [ ] Protocol 22: Model Monitoring (AI) - 8 hours
```

Evidence: `PROTOCOL-CHECKLIST.md` (workspace root)

---

### STEP 8.3: Package Evidence Artifacts

**Action:** **[MUST]** Create complete evidence package:

```bash
python scripts/orchestration/package_evidence.py \
  --artifacts-dir .artifacts/protocol-05b/ \
  --output .artifacts/protocol-05b/handoff-package.zip
```

**Package Contents:**
- All JSON artifacts (35+ files)
- `evidence-manifest.json` (artifact inventory)
- `checksums.sha256` (integrity verification)
- New protocols (if created)


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/handoff-package.zip`

---

### STEP 8.4: Request User Approval

**Action:** **[CRITICAL]** Present execution plan for approval:

**User Prompt:**
```
[PROTOCOL 05B | APPROVAL REQUIRED]

Protocol execution plan generated:
📊 Project Classification: [Type] (confidence: X%)
📋 Protocols Selected: X REQUIRED, Y RECOMMENDED, Z MAYBE
⏱️  Estimated Timeline: X days (Y hours total)
🎯 Requirement Coverage: X%

Documents generated:
✅ PROTOCOL-EXECUTION-PLAN.md (workspace root)
✅ PROTOCOL-CHECKLIST.md (workspace root)
✅ Evidence package (.artifacts/protocol-05b/handoff-package.zip)

Please review PROTOCOL-EXECUTION-PLAN.md and approve to proceed.

MAYBE Protocols (Your Decision):
- Protocol XX: [Name] - [Value proposition] - [Hours]
  Include? (yes/no/defer)

Approve execution plan? (yes/no/revise)
```


**Communication:** Status update with progress

Evidence: `.artifacts/protocol-05b/approval-record.json`

**Approval Options:**
- **yes** → Proceed to handoff (Gate 6 passed)
- **no** → Halt execution, log reason
- **revise** → Return to specified phase for adjustments

**Error Handling:**
- User requests revision → Return to specified phase (2, 3, or 5)
- User declines → Halt gracefully, preserve all artifacts
- No response after 10 minutes → Prompt again, escalate after 3 attempts

---

**PHASE 6 OUTPUTS:**
- ✅ `PROTOCOL-EXECUTION-PLAN.md` (workspace root)
- ✅ `PROTOCOL-CHECKLIST.md` (workspace root)
- ✅ `handoff-package.zip` (.artifacts/protocol-05b/)
- ✅ `approval-record.json` (.artifacts/protocol-05b/)

---

### PHASE 7: PROJECT-SPECIFIC PROTOCOL GENERATION

**Purpose:** Generate customized, project-specific protocol instances from foundation templates based on the execution plan.

**Status:** ✅ NEW - Added in v1.1.0 (Hybrid Architecture Implementation)

**When to Execute:** After PHASE 6 approval obtained, before handoff to next protocol

**Skip Conditions:**
- Project uses only foundation protocols (Protocols 01-05) without customization
- User explicitly opts out of protocol generation
- Project classification is "Simple" with no special requirements

---

### STEP 7.1: Prepare Generation Environment

**Action:** **[MUST]** Set up project-specific protocol directory structure:

```bash
python scripts/orchestration/prepare_protocol_generation.py \
  --project-root . \
  --output .artifacts/protocol-05b/generation-environment.json
```

**Directory Structure Created:**
```
{project-root}/
└── .cursor/
    └── project-protocols/
        ├── README.md (generation metadata)
        ├── .protocol-manifest.json (tracking file)
        └── [protocols will be generated here]
```

**Communication:** `[PROTOCOL 05B | PHASE 7 START] - Preparing protocol generation environment`

**Evidence:** `.artifacts/protocol-05b/generation-environment.json`

**Error Handling:**
- Directory creation fails → **BLOCK**, check permissions
- Manifest creation fails → **BLOCK**, validate JSON schema

---

### STEP 7.2: Load Foundation Templates

**Action:** **[MUST]** Read foundation protocol templates from `.cursor/ai-driven-workflow/`:

```bash
python scripts/orchestration/load_foundation_templates.py \
  --template-dir .cursor/ai-driven-workflow \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output .artifacts/protocol-05b/loaded-templates.json
```

**Loading Logic:**
- Read PROTOCOL-EXECUTION-PLAN.md Section 5 (Execution Sequence)
- For each REQUIRED/RECOMMENDED protocol:
  - Load template file from `.cursor/ai-driven-workflow/{protocol-id}-{name}.md`
  - Parse YAML frontmatter
  - Extract parameterization points
  - Store in memory for transformation

**Communication:** `[PROTOCOL 05B | PHASE 7] - Loaded X foundation templates for customization`

**Evidence:** `.artifacts/protocol-05b/loaded-templates.json`

**Error Handling:**
- Template file not found → **WARN**, skip protocol (use foundation directly)
- Template parse error → **BLOCK**, validate template format
- Missing parameterization points → **WARN**, generate without customization

---

### STEP 7.3: Apply Transformation Rules

**Action:** **[MUST]** Transform foundation templates into project-specific instances:

```bash
python scripts/orchestration/transform_protocols.py \
  --templates .artifacts/protocol-05b/loaded-templates.json \
  --project-brief PROJECT-BRIEF.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --customizations .artifacts/protocol-05b/customization-requirements.json \
  --output .artifacts/protocol-05b/transformed-protocols.json
```

**Transformation Rules:**

1. **Project Name Substitution:**
   - Replace `{PROJECT_NAME}` → Actual project name from PROJECT-BRIEF.md
   - Replace `{PROJECT_TYPE}` → Classification from PHASE 2
   - Replace `{PROJECT_DOMAIN}` → Domain from PROJECT-BRIEF.md

2. **Tech Stack Customization:**
   - Inject tech-specific sections based on `tech_stack` from PROJECT-BRIEF
   - Add framework-specific validation steps
   - Customize automation scripts for tech stack

3. **Workflow Step Customization:**
   - Add/remove steps based on project characteristics
   - Inject project-specific validation rules
   - Customize quality gates based on requirements

4. **Artifact Path Customization:**
   - Update artifact paths to project-specific locations
   - Customize evidence requirements
   - Update integration points

5. **Validation Rule Injection:**
   - Add project-specific validators
   - Customize quality thresholds
   - Inject compliance requirements

**Communication:** `[PROTOCOL 05B | PHASE 7] - Transformed X protocols with Y customizations`

**Evidence:** `.artifacts/protocol-05b/transformed-protocols.json`

**Error Handling:**
- Transformation fails → **BLOCK**, log transformation error
- Invalid customization → **WARN**, skip customization
- Missing required fields → **BLOCK**, validate transformation rules

---

### STEP 7.4: Validate Generated Protocols

**Action:** **[MUST]** Run 11-validator system on generated protocols:

```bash
python validators-system/scripts/validate_all_protocols.py \
  --workspace . \
  --protocol-dir .cursor/project-protocols \
  --protocol-ids [generated-protocol-ids] \
  --output .artifacts/protocol-05b/generation-validation.json
```

**Validation Requirements:**
- Overall score ≥0.95 for each generated protocol
- Each validator dimension ≥0.90
- Zero critical validation failures
- Structural integrity 100%

**Communication:** `[PROTOCOL 05B | PHASE 7] - Validating X generated protocols`

**Evidence:** `.artifacts/protocol-05b/generation-validation.json`

**Error Handling:**
- Validation score <0.95 → **RETRY** transformation with fixes
- Critical failure → **BLOCK**, escalate to user
- Max 3 retry attempts → **ESCALATE** if still failing

---

### STEP 7.5: Write Generated Protocols to Disk

**Action:** **[MUST]** Save validated protocols to project-specific directory:

```bash
python scripts/orchestration/write_generated_protocols.py \
  --protocols .artifacts/protocol-05b/transformed-protocols.json \
  --validation .artifacts/protocol-05b/generation-validation.json \
  --output-dir .cursor/project-protocols \
  --manifest .artifacts/protocol-05b/generation-manifest.json
```

**File Naming Convention:**
```
.cursor/project-protocols/
├── 06-create-prd-{project-name}.md
├── 07-technical-design-{project-name}.md
├── 08-task-generation-{project-name}.md
└── ...
```

**Manifest Format:**
```json
{
  "generation_timestamp": "ISO8601",
  "project_name": "string",
  "foundation_version": "1.0.0",
  "protocols_generated": [
    {
      "protocol_id": "06",
      "protocol_name": "Create PRD",
      "source_template": ".cursor/ai-driven-workflow/06-create-prd.md",
      "generated_file": ".cursor/project-protocols/06-create-prd-{project}.md",
      "customizations_applied": ["tech_stack", "validation_rules"],
      "validation_score": 0.97
    }
  ],
  "total_protocols": 15,
  "total_customizations": 42
}
```

**Communication:** `[PROTOCOL 05B | PHASE 7] - Generated X project-specific protocols`

**Evidence:** 
- `.artifacts/protocol-05b/generation-manifest.json`
- `.cursor/project-protocols/.protocol-manifest.json`
- Generated protocol files in `.cursor/project-protocols/`

**Error Handling:**
- Write permission denied → **BLOCK**, check directory permissions
- Disk space insufficient → **BLOCK**, request cleanup
- File already exists → **WARN**, backup existing and overwrite

---

### STEP 7.6: Update Execution Plan with Generated Protocols

**Action:** **[MUST]** Update PROTOCOL-EXECUTION-PLAN.md to reference generated protocols:

```bash
python scripts/orchestration/update_execution_plan.py \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --generation-manifest .artifacts/protocol-05b/generation-manifest.json \
  --output PROTOCOL-EXECUTION-PLAN.md
```

**Updates Applied:**
- Add "Generated Protocols" section
- Update protocol paths to point to `.cursor/project-protocols/`
- Add generation metadata (timestamp, customizations)
- Update handoff instructions

**Communication:** `[PROTOCOL 05B | PHASE 7] - Updated execution plan with generated protocols`

**Evidence:** Updated `PROTOCOL-EXECUTION-PLAN.md` with generation section

**Error Handling:**
- Update fails → **WARN**, manual update required
- Execution plan corrupted → **BLOCK**, restore from backup

---

### STEP 7.7: Generate Protocol Generation Report

**Action:** **[MUST]** Create comprehensive generation report:

```bash
python scripts/orchestration/generate_protocol_report.py \
  --generation-manifest .artifacts/protocol-05b/generation-manifest.json \
  --validation .artifacts/protocol-05b/generation-validation.json \
  --output .artifacts/protocol-05b/PROTOCOL-GENERATION-REPORT.md
```

**Report Sections:**
1. **Executive Summary** (protocols generated, customizations applied, validation scores)
2. **Generation Details** (per-protocol customizations, transformation rules applied)
3. **Validation Results** (validator scores, issues found, remediation applied)
4. **Usage Instructions** (how to use generated protocols, integration points)
5. **Maintenance Notes** (how to regenerate, update procedures)

**Communication:** `[PROTOCOL 05B | PHASE 7 COMPLETE] - Protocol generation successful`

**Evidence:** `.artifacts/protocol-05b/PROTOCOL-GENERATION-REPORT.md`

---

**PHASE 7 OUTPUTS:**
- ✅ `.cursor/project-protocols/` directory with generated protocols
- ✅ `.cursor/project-protocols/.protocol-manifest.json` (tracking file)
- ✅ `.artifacts/protocol-05b/generation-manifest.json` (generation metadata)
- ✅ `.artifacts/protocol-05b/PROTOCOL-GENERATION-REPORT.md` (comprehensive report)
- ✅ `.artifacts/protocol-05b/generation-validation.json` (validation results)
- ✅ Updated `PROTOCOL-EXECUTION-PLAN.md` with generation details

---

## QUALITY GATES

### Gate 0: Pre-Flight Validation [Prerequisite]

**Type:** Automated | **Trigger:** Before PHASE 0 execution | **Blocking:** Yes

**Criteria:**
- Protocol 05 artifacts exist and valid (100% pass rate required)
- PROJECT-BRIEF.md exists with all required sections
- User authorization obtained (explicit approval recorded)
- All prerequisite files readable and parseable

**Pass Threshold:** 100% (all checks must pass)
**Fail Threshold:** Any check fails → BLOCK execution

**Automation:**
```bash
python scripts/orchestration/validate_protocol_evidence.py --protocol 05 --workspace .
```

**Pass Criteria:**
- Exit code: 0
- All validation checks return `status: "pass"`
- Evidence artifacts present and valid

**Failure Handling:**
- **On Fail:** BLOCK execution immediately, return to Protocol 05
- **Remediation:** Re-run Protocol 05 to generate missing artifacts
- **Rollback:** Not applicable (pre-flight check)
- **Notification:** Alert Protocol 05 owner with gap report
- **Escalation:** If Protocol 05 cannot be fixed, escalate to project stakeholder

**Waiver Policy:** No waivers permitted (security and regulatory requirement)

**Compliance Integration:**
- **Security:** Validates artifact integrity before processing
- **Audit Trail:** Logs all validation attempts with timestamps
- **Regulatory:** Ensures prerequisite compliance before workflow execution

**Evidence:** `.artifacts/protocol-05b/phase-00-preflight-check.json`

---

### Gate 1: Classification Confidence [Execution]

**Type:** Automated with Manual Override | **Trigger:** After PHASE 2 | **Blocking:** Conditional

**Criteria:**
- Project classification confidence score ≥85%
- Classification reasoning document complete
- All 27+ characteristics evaluated
- Evidence supporting classification present

**Pass Threshold:** Confidence ≥85% OR human approval obtained
**Warning Threshold:** Confidence 70-84% (proceed with caution)
**Fail Threshold:** Confidence <70% without human review

**Automation:**
```bash
python scripts/orchestration/calculate_classification_confidence.py \
  --classification .artifacts/protocol-05b/project-classification.json
```

**Pass Criteria:**
- Confidence score ≥0.85 (85%)
- Classification reasoning document generated
- User approval recorded (if confidence <85%)

**Failure Handling:**
- **On Fail (<70%):** BLOCK until human review obtained
- **Remediation:** Request additional context from user, re-run classification
- **Rollback:** Return to PHASE 2 with user-provided clarifications
- **Notification:** Alert user with classification ambiguity details
- **Escalation:** If user cannot clarify, escalate to project architect

**Waiver Policy:** Manual override permitted with documented justification

**Compliance Integration:**
- **Audit Trail:** Logs all classification attempts and confidence scores
- **Regulatory:** Ensures classification accuracy for compliance requirements
- **Security:** Validates classification logic integrity

**Evidence:** `.artifacts/protocol-05b/project-classification.json`, `classification-reasoning.md`

---

### Gate 2: MAYBE Protocol Decisions [Execution]

**Type:** Manual | **Trigger:** After PHASE 3 protocol selection | **Blocking:** Yes

**Criteria:**
- All MAYBE protocols presented to user
- User decision recorded for each: Include / Skip / Defer
- Decision timestamp and rationale documented
- No pending decisions remaining

**Pass Threshold:** 100% decisions made (all MAYBE protocols have user input)
**Fail Threshold:** Any MAYBE protocol without decision

**Automation:**
- Presentation: `python scripts/orchestration/generate_execution_plan.py`
- Validation: Manual user input collection

**Pass Criteria:**
- All MAYBE protocols have decision status
- Decisions recorded in `maybe-protocol-decisions.json`
- Timestamp and rationale present for each decision

**Failure Handling:**
- **On Fail:** BLOCK until all decisions obtained
- **Remediation:** Re-prompt user after 30 minutes if no response
- **Rollback:** Not applicable (user input required)
- **Notification:** Alert user with pending decision list
- **Escalation:** After 3 prompts (90 minutes), escalate to project owner

**Waiver Policy:** No waivers (user decision mandatory for execution plan)

**Compliance Integration:**
- **Audit Trail:** Logs all user decisions with timestamps
- **Regulatory:** Ensures user approval for optional protocol execution
- **Security:** Validates decision integrity and prevents unauthorized modifications

**Evidence:** `.artifacts/protocol-05b/maybe-protocol-decisions.json`

---

### Gate 3: Protocol Coverage [Execution]

**Type:** Automated | **Trigger:** After PHASE 3 gap analysis | **Blocking:** Yes

**Criteria:**
- Overall requirement coverage ≥95%
- Critical requirements coverage = 100%
- Zero conflicting protocols selected
- Gap analysis complete

**Pass Threshold:** Coverage ≥95% AND critical = 100%
**Fail Threshold:** Coverage <95% OR critical <100%

**Automation:**
```bash
python scripts/orchestration/validate_protocol_coverage.py \
  --gap-analysis .artifacts/protocol-05b/gap-analysis.json \
  --threshold 0.95
```

**Pass Criteria:**
- Coverage percentage ≥0.95 (95%)
- All critical requirements mapped to protocols
- No protocol conflicts detected

**Failure Handling:**
- **On Fail (<95%):** Force PHASE 4 execution (create new protocols)
- **Remediation:** Generate new protocols to fill gaps
- **Rollback:** Return to PHASE 3 if gap analysis invalid
- **Notification:** Alert user with gap details and resolution plan
- **Escalation:** If gaps cannot be filled, escalate with risk assessment

**Waiver Policy:** Waivers permitted for non-critical gaps <5% with documented risk acceptance

**Compliance Integration:**
- **Security:** Ensures all security requirements covered
- **Audit Trail:** Logs coverage calculations and gap resolutions
- **Regulatory:** Validates compliance requirement coverage

**Evidence:** `.artifacts/protocol-05b/gap-analysis.json`, `coverage-report.json`

---

### Gate 4: New Protocol Validation [Execution]

**Type:** Automated with Manual Escalation | **Trigger:** After PHASE 4 (if gaps existed) | **Blocking:** Yes

**Criteria:**
- All new protocols score ≥0.95 on validation
- Each validator dimension ≥0.90
- Zero critical validation failures
- Maximum 5 iteration attempts per protocol

**Pass Threshold:** Overall score ≥0.95 for ALL new protocols
**Fail Threshold:** Score <0.95 after 5 iterations

**Automation:**
```bash
python validators-system/scripts/validate_all_protocols.py \
  --protocol {new_protocol_id} \
  --workspace /path/to/workspace
```

**Pass Criteria:**
- Validation score ≥0.95
- All 10 validators pass (score ≥0.90 each)
- No critical failures (score <0.50)

**Failure Handling:**
- **On Fail (iteration <5):** Apply fixes, re-run validation
- **Remediation:** Analyze validation report, fix highest-impact issues first
- **Rollback:** If validation fails after 5 iterations, escalate to user
- **Notification:** Alert user with validation failures and remediation options
- **Escalation:** User chooses: manual fix, skip protocol (accept gap), or use alternative

**Waiver Policy:** Waivers permitted for non-critical validators (<0.90) with justification

**Compliance Integration:**
- **Security:** Ensures new protocols meet security standards
- **Audit Trail:** Logs all validation attempts and scores
- **Regulatory:** Validates new protocol compliance before integration

**Evidence:** `.artifacts/protocol-05b/new-protocols/{ID}-validation-report.json`

---

### Gate 5: Timeline Approval [Completion]

**Type:** Manual | **Trigger:** After PHASE 5 timeline estimation | **Blocking:** No (advisory)

**Criteria:**
- Timeline calculated with effort estimates
- Critical path identified
- Parallel opportunities documented
- User approves timeline and resource allocation

**Pass Threshold:** User explicit approval ("yes")
**Fail Threshold:** User rejects timeline

**Automation:**
- Calculation: `python scripts/orchestration/estimate_timeline.py`
- Approval: Manual user confirmation

**Pass Criteria:**
- User approval recorded
- Timeline estimates documented
- Resource requirements validated

**Failure Handling:**
- **On Fail:** Return to PHASE 5 for optimization
- **Remediation:** Adjust protocol selection, increase parallelization, defer non-critical protocols
- **Rollback:** Re-run PHASE 5 with user-specified constraints
- **Notification:** Alert user with optimization options
- **Escalation:** If timeline cannot meet constraints, escalate with trade-off analysis

**Waiver Policy:** Waivers permitted (timeline is advisory, not blocking)

**Compliance Integration:**
- **Audit Trail:** Logs timeline estimates and user approvals
- **Regulatory:** Documents resource allocation for compliance audits

**Evidence:** `.artifacts/protocol-05b/timeline-estimate.json`, `approval-record.json`

---

### Gate 6: Final Plan Approval [Completion]

**Type:** Manual | **Trigger:** After PHASE 6 plan generation | **Blocking:** Yes

**Criteria:**
- PROTOCOL-EXECUTION-PLAN.md complete (15-25 pages)
- PROTOCOL-CHECKLIST.md generated
- handoff-package.zip valid and complete
- User approves entire execution plan

**Pass Threshold:** User explicit approval ("yes")
**Fail Threshold:** User rejects or requests revisions

**Automation:**
- Generation: `python scripts/orchestration/generate_execution_plan.py`
- Packaging: `python scripts/orchestration/package_evidence.py`
- Validation: Manual user review

**Pass Criteria:**
- User approval recorded with timestamp
- All deliverables generated and validated
- Handoff package integrity verified (checksums match)

**Failure Handling:**
- **On Fail:** Smart rollback to specified phase based on user feedback
- **Remediation:** User specifies phase to return to (PHASE 2, 3, or 5)
- **Rollback:** Preserve artifacts from completed phases, re-execute specified phase
- **Notification:** Alert user with revision options and impact analysis
- **Escalation:** If user cannot approve after 3 revisions, escalate to project stakeholder

**Waiver Policy:** No waivers (final approval mandatory for handoff)

**Compliance Integration:**
- **Security:** Validates execution plan integrity before handoff
- **Audit Trail:** Logs all approval attempts and revisions
- **Regulatory:** Ensures execution plan meets compliance requirements

**Evidence:** `PROTOCOL-EXECUTION-PLAN.md`, `PROTOCOL-CHECKLIST.md`, `handoff-package.zip`, `approval-record.json`

---

### Gate 7: Protocol Generation Validation [Completion]

**Type:** Automated | **Trigger:** After PHASE 7 protocol generation | **Blocking:** Yes

**Status:** ✅ NEW - Added in v1.1.0 (Hybrid Architecture Implementation)

**Criteria:**
- All generated protocols score ≥0.95 on validation
- Project-specific directory `.cursor/project-protocols/` created successfully
- Generation manifest complete and valid
- All transformation rules applied successfully
- Zero critical generation failures

**Pass Threshold:** 
- Overall validation score ≥0.95 for ALL generated protocols
- Structural integrity 100%
- Generation manifest complete

**Fail Threshold:** 
- Any protocol score <0.95 after 3 retry attempts
- Critical transformation failure
- Generation manifest invalid

**Automation:**
```bash
python validators-system/scripts/validate_all_protocols.py \
  --workspace . \
  --protocol-dir .cursor/project-protocols \
  --protocol-ids [generated-protocol-ids] \
  --output .artifacts/protocol-05b/generation-validation.json
```

**Pass Criteria:**
- Exit code: 0
- All generated protocols have validation score ≥0.95
- Generation manifest JSON valid
- All protocol files written successfully
- PROTOCOL-EXECUTION-PLAN.md updated with generation details

**Failure Handling:**
- **On Fail (<0.95):** Retry transformation with fixes (max 3 attempts)
- **Remediation:** 
  - Analyze validation failures
  - Apply auto-fixes for common issues
  - Re-run transformation with corrections
  - Re-validate generated protocols
- **Rollback:** If generation fails completely, continue with foundation templates
- **Notification:** Alert user with generation status and fallback plan
- **Escalation:** If generation cannot succeed after 3 attempts, escalate to user with options:
  - Option A: Use foundation templates directly (no customization)
  - Option B: Manual protocol customization
  - Option C: Skip problematic protocols

**Waiver Policy:** 
- Waivers permitted for non-critical protocols with score ≥0.90
- Critical protocols (06-09) must achieve ≥0.95
- All waivers require documented justification

**Compliance Integration:**
- **Security:** Validates generated protocol integrity
- **Audit Trail:** Logs all generation attempts, transformations, and validations
- **Regulatory:** Ensures generated protocols meet compliance standards
- **Quality:** Maintains protocol quality standards across generated instances

**Evidence:** 
- `.artifacts/protocol-05b/generation-validation.json`
- `.artifacts/protocol-05b/generation-manifest.json`
- `.artifacts/protocol-05b/PROTOCOL-GENERATION-REPORT.md`
- `.cursor/project-protocols/.protocol-manifest.json`

**Skip Conditions:**
- PHASE 7 skipped (user opted out or simple project)
- No protocols require customization
- Project uses only foundation protocols

---

## COMMUNICATION PROTOCOLS

### Status Announcements
- **Phase Start:** `[PROTOCOL 05B | PHASE {N} START] - {Name}`
- **Phase Complete:** `[PROTOCOL 05B | PHASE {N} COMPLETE] - {Name}`
- **Gate Status:** `[PROTOCOL 05B | GATE {N} {STATUS}] - {Name}`
- **Milestone:** `[PROTOCOL 05B | MILESTONE] - {Name}`

### Artifact Announcements
**Template:**
```
[PROTOCOL 05B | ARTIFACT GENERATED]
Artifact: {artifact_name}
Location: {file_path}
Format: {json|markdown|zip}
Size: {size}
Validation: {status}
```

**Example:**
```
[PROTOCOL 05B | ARTIFACT GENERATED]
Artifact: project-classification.json
Location: .artifacts/protocol-05b/project-classification.json
Format: JSON
Size: 2.4 KB
Validation: PASS
```

### Progress Reporting
- **In Progress:** Current phase, step, % complete, ETA
- **Next Steps:** Completed phase, next phase, action required
- **Timeline Updates:** Original vs revised estimates
- **Current Activity:** Descriptive action statements

### Error Messages
- **Gate Failure:** Reason, impact, remediation, evidence path
- **Phase Error:** Error message, failed step, action
- **Validation Error:** Artifact, issue, expected vs actual, fix

### Clarification Request Templates

**Template 1: Ambiguous Classification**
```
[PROTOCOL 05B | CLARIFICATION NEEDED]

The project classification is ambiguous. Please clarify:
- Which type best describes your project?
- Can you specify additional details about {ambiguous_aspect}?
- Please provide more context on {unclear_requirement}

Your clarification will help us choose the optimal protocol set.
```

**Template 2: Missing Information**
```
[PROTOCOL 05B | CLARIFICATION NEEDED]

Required information is missing from PROJECT-BRIEF:
- Please specify: {missing_field}
- Can you clarify: {unclear_section}
- We need to know: {required_detail}

This information is needed to make an informed decision on protocol selection.
```

**Template 3: Conflicting Requirements**
```
[PROTOCOL 05B | CLARIFICATION NEEDED]

Conflicting requirements detected. Please clarify which takes priority:
- Option A: {requirement_1} → Suggests {protocol_set_A}
- Option B: {requirement_2} → Suggests {protocol_set_B}

Which option should we choose? Please specify your preference.
```

### Decision Point Templates

**Template 1: Protocol Selection Decision**
```
[PROTOCOL 05B | DECISION POINT]

MAYBE Protocols require your decision:
1. Protocol {ID}: {Name}
   - Value: {benefit}
   - Effort: {hours} hours
   - Choose: Include / Skip / Defer

2. Protocol {ID}: {Name}
   - Value: {benefit}
   - Effort: {hours} hours
   - Choose: Include / Skip / Defer

Please make a decision for each protocol. Your choice will determine the execution plan.
```

**Template 2: Gap Resolution Decision**
```
[PROTOCOL 05B | DECISION POINT]

Coverage gaps detected. Choose resolution approach:
- Option 1: Create new protocols (estimated: {hours} hours)
- Option 2: Accept gaps and document as limitations
- Option 3: Modify existing protocols

Which option do you choose? Please specify your decision.
```

**Template 3: Timeline Approval Decision**
```
[PROTOCOL 05B | DECISION POINT]

Estimated timeline: {days} days ({hours} hours)

Do you approve this timeline?
- Option 1: Yes, proceed with this timeline
- Option 2: No, optimize for faster completion
- Option 3: No, extend timeline for higher quality

Please choose an option and provide any constraints.
```

### Feedback Request Templates

**Template 1: Classification Feedback**
```
[PROTOCOL 05B | FEEDBACK REQUEST]

Project classified as: {type} (confidence: {X}%)

Does this classification match your understanding?
- Provide feedback: Is this correct?
- If incorrect, please specify the correct type
- Any additional context to improve classification?

Your feedback helps us refine the protocol selection.
```

**Template 2: Protocol Selection Feedback**
```
[PROTOCOL 05B | FEEDBACK REQUEST]

{N} protocols selected as REQUIRED.
{M} protocols marked as MAYBE (awaiting your decision).

Please review and provide feedback:
- Are there missing protocols you expected to see?
- Are there unnecessary protocols we should remove?
- Does this selection match your project needs?

Your feedback ensures optimal protocol coverage.
```

**Template 3: Timeline Feedback**
```
[PROTOCOL 05B | FEEDBACK REQUEST]

Estimated timeline: {days} days ({hours} hours total)

Is this timeline acceptable?
- Please provide feedback on feasibility
- Specify any timeline constraints
- Suggest optimizations if needed

Your feedback helps us adjust the execution plan.
```

### Confirmation Prompts

**Template 1: Proceed Confirmation**
```
[PROTOCOL 05B | CONFIRMATION REQUIRED]

Ready to proceed with protocol orchestration?
- All prerequisites validated
- Authorization obtained
- Estimated duration: {minutes} minutes

Confirm to proceed: (yes/no)
```

**Template 2: Final Approval Confirmation**
```
[PROTOCOL 05B | CONFIRMATION REQUIRED]

Execution plan complete. Please confirm final approval:
- {N} protocols selected
- Timeline: {days} days
- All deliverables ready

Confirm approval to handoff: (yes/no/revise)
```

---

## AUTOMATION HOOKS

**Script Registry:** `scripts/script-registry.json`

**19 Automation Scripts:**
1-2. PHASE 0: validate_protocol_evidence.py, validate_project_brief.py
3-7. PHASE 1: parse_project_brief.py, parse_architecture.py, parse_bootstrap_manifest.py, inventory_artifacts.py, validate_artifact_completeness.py
8-11. PHASE 2: classify_project_type.py, detect_characteristics.py, calculate_classification_confidence.py, generate_classification_reasoning.py
12-15. PHASE 3: map_characteristics_to_protocols.py, select_protocols.py, analyze_gaps.py, validate_protocol_coverage.py
16-17. PHASE 4: generate_protocol_spec_from_gap.py, register_new_protocol.py
18-21. PHASE 5: build_dependency_graph.py, sequence_protocols.py, analyze_customization_needs.py, estimate_timeline.py
22-24. PHASE 6: generate_execution_plan.py, generate_protocol_checklist.py, package_evidence.py

**Exit Codes:** 0=Success, 1=Validation failure, 2=System error, 3=User intervention

---

## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All 7 quality gates passed
- [ ] 35+ evidence artifacts generated
- [ ] PROTOCOL-EXECUTION-PLAN.md created
- [ ] PROTOCOL-CHECKLIST.md created
- [ ] handoff-package.zip validated
- [ ] New protocols registered (if applicable)
- [ ] All user approvals obtained

### Sign-Off & Authorization
- [ ] **Protocol Owner Sign-Off:** Technical Lead / Workflow Architect
  - Name: _____________________
  - Date: _____________________
  - Signature: _____________________
- [ ] **Reviewer Sign-Off:** Project Stakeholder / Product Owner
  - Name: _____________________
  - Date: _____________________
  - Approval: [ ] Approved [ ] Approved with conditions [ ] Rejected
  - Conditions (if any): _____________________
- [ ] **Downstream Protocol Owner Acknowledgment:**
  - Name: _____________________
  - Protocol: _____________________
  - Date: _____________________
  - Ready to proceed: [ ] Yes [ ] No (reason: _____________________ )

### Handoff Deliverables
- [ ] PROTOCOL-EXECUTION-PLAN.md (workspace root, 15-25 pages)
- [ ] PROTOCOL-CHECKLIST.md (workspace root, checkbox list)
- [ ] handoff-package.zip (.artifacts/protocol-05b/, 35+ artifacts)
- [ ] New protocols (if gaps detected, validated ≥0.95)
- [ ] Customization notes (in execution plan)

### Downstream Validation
- [ ] Next protocol owner identified
- [ ] Handoff package received
- [ ] Understanding confirmed
- [ ] Inputs validated
- [ ] Ready to execute

---

## EVIDENCE SUMMARY

### Artifacts Required (35+ files)
```
.artifacts/protocol-05b/
├── phase-00-preflight-check.json
├── project-brief-validation.json
├── authorization-record.json
├── phase-01-validation.json
├── project-brief-parsed.json
├── architecture-parsed.json
├── bootstrap-manifest-parsed.json
├── artifact-inventory.json
├── project-classification.json
├── characteristics-detection.json
├── classification-reasoning.md
├── characteristic-protocol-mapping.json
├── protocol-selection.json
├── gap-analysis.json
├── coverage-report.json
├── maybe-protocol-decisions.json
├── new-protocols/ (if gaps)
│   ├── {ID}-specification.json
│   ├── {ID}-{name}.md
│   └── {ID}-validation-report.json
├── dependency-graph.json
├── execution-sequence.json
├── critical-path-analysis.json
├── customization-requirements.json
├── timeline-estimate.json
├── approval-record.json
├── handoff-package.zip
├── evidence-manifest.json
└── checksums.sha256
```

### Root-Level Artifacts
- PROTOCOL-EXECUTION-PLAN.md
- PROTOCOL-CHECKLIST.md

### Artifact Formats
- **JSON:** Structured data (classifications, mappings, timelines)
- **Markdown:** Human-readable plans and documentation
- **ZIP:** Evidence packages for downstream protocols

### Artifact Table with Outcomes

| Artifact Name | Phase | Type | Purpose | Success Metric | Downstream Consumer |
|---------------|-------|------|---------|----------------|---------------------|
| phase-00-preflight-check.json | 0 | Validation | Verify Protocol 05 complete | 100% checks pass | Gate 0 |
| project-brief-validation.json | 0 | Validation | Verify PROJECT-BRIEF integrity | All sections present | PHASE 1 |
| authorization-record.json | 0 | Approval | User authorization to proceed | Explicit "yes" recorded | Gate 0 |
| project-brief-parsed.json | 1 | Data | Extracted PROJECT-BRIEF data | All fields populated | PHASE 2, 3 |
| architecture-parsed.json | 1 | Data | Extracted architecture context | Valid JSON structure | PHASE 2 |
| bootstrap-manifest-parsed.json | 1 | Data | Bootstrap configuration | Valid manifest format | PHASE 2 |
| artifact-inventory.json | 1 | Metadata | List of all context files | Complete file list | PHASE 1 validation |
| project-classification.json | 2 | Analysis | Project type classification | Confidence ≥85% | PHASE 3, Gate 1 |
| characteristics-detection.json | 2 | Analysis | 27+ dimension analysis | All dimensions evaluated | PHASE 3 |
| classification-reasoning.md | 2 | Documentation | Human-readable explanation | Complete rationale | User review, Gate 1 |
| characteristic-protocol-mapping.json | 3 | Mapping | Characteristics → Protocols | All characteristics mapped | PHASE 3 |
| protocol-selection.json | 3 | Decision | REQUIRED/MAYBE/SKIP list | All protocols classified | PHASE 4, 5, Gate 2 |
| gap-analysis.json | 3 | Analysis | Coverage gaps identification | Coverage % calculated | Gate 3, PHASE 4 |
| coverage-report.json | 3 | Metrics | Requirement coverage metrics | ≥95% coverage | Gate 3 |
| maybe-protocol-decisions.json | 3 | Approval | User decisions on MAYBE protocols | All decisions recorded | Gate 2, PHASE 5 |
| dependency-graph.json | 5 | Analysis | Protocol dependencies | Valid DAG structure | PHASE 5 |
| execution-sequence.json | 5 | Planning | Ordered protocol list | Topological sort valid | PHASE 6 |
| critical-path-analysis.json | 5 | Metrics | Longest execution path | Critical path identified | PHASE 6, Gate 5 |
| customization-requirements.json | 5 | Planning | Protocol modifications needed | All customizations documented | PHASE 6 |
| timeline-estimate.json | 5 | Metrics | Effort and duration estimates | Realistic estimates | Gate 5, PHASE 6 |
| approval-record.json | 6 | Approval | Final plan approval | User explicit approval | Gate 6 |
| handoff-package.zip | 6 | Package | Complete evidence bundle | All artifacts included, checksums valid | Downstream protocols |
| evidence-manifest.json | 6 | Metadata | Artifact inventory | All artifacts listed | Audit, validation |
| checksums.sha256 | 6 | Integrity | File integrity verification | All checksums match | Audit, security |
| PROTOCOL-EXECUTION-PLAN.md | 6 | Deliverable | Complete execution plan | 15-25 pages, all sections | Downstream protocol owner |
| PROTOCOL-CHECKLIST.md | 6 | Tool | Execution tracking checklist | All protocols listed | Project team |

### Artifact Retention & Archival

- **Retention Period:** Permanent (required for audit trail)
- **Backup Frequency:** Daily (included in project backups)
- **Access Control:** Read-only after handoff (preserve integrity)
- **Archival Policy:** Compress to `.tar.gz` after 90 days, retain indefinitely
- **Retrieval Process:** Documented in `evidence-manifest.json`

---

## REASONING & REFLECTION

### Decision Logic

**Classification (≥85% threshold):** Balances automation speed with accuracy, prevents costly misclassification

**Coverage (≥95% threshold):** Ensures critical requirements covered while allowing flexibility for edge cases

**New Protocol Validation (≥0.95):** Maintains quality standards for dynamically created protocols

**MAYBE Classification:** Empowers user decision-making with clear value propositions

### Continuous Improvement

**Lessons Learned:**
- Classification accuracy improves with historical data
- 15% of projects have unique requirements (gap detection critical)
- Timeline estimates need calibration with actual data
- 30% of classifications benefit from human review

**Optimization Opportunities:**
- Machine learning for classification
- Protocol recommendation engine
- Automated customization generation
- Enhanced parallel execution detection

**Technical Debt:**
- Hard-coded classification rules (should be externalized)
- Manual Protocol 0 invocation (should be automated)
- Limited retry logic (needs exponential backoff)

### Learning Mechanisms

**Feedback Loop:**
- **Collect:** Track classification accuracy over time via feedback forms
- **Analyze:** Collect user feedback on protocol selections after project completion
- **Monitor:** Monitor actual vs estimated timelines and calculate variance
- **Review:** Analyze gap patterns across projects quarterly
- **Implement:** Apply feedback to improve classification algorithms

**Improvement Tracking:**
- **Database:** Maintain classification history database in `.artifacts/learning/classification-history.json`
- **Override Log:** Log all user overrides and reasons in `.artifacts/learning/override-log.json`
- **Success Metrics:** Track protocol execution success rates (completion, quality, timeline adherence)
- **Pattern Recognition:** Document customization patterns in `.artifacts/learning/customization-patterns.md`
- **Continuous Improvement:** Review improvement tracking data monthly

**Knowledge Base:**
- **Examples:** Project classification examples stored in `knowledge-base/classification-examples.json`
- **Patterns:** Characteristic detection patterns in `knowledge-base/detection-patterns.json`
- **Decision Trees:** Protocol selection decision trees in `knowledge-base/selection-trees.json`
- **Formulas:** Timeline estimation formulas in `knowledge-base/estimation-formulas.json`
- **Updates:** Knowledge base updated after each project completion

**Adaptation:**
- **Algorithm Refinement:** Refine classification algorithms based on feedback quarterly
- **Protocol Mapping:** Update protocol mappings as new protocols added (automated)
- **Threshold Adjustment:** Adjust confidence thresholds based on accuracy metrics (monthly review)
- **Estimation Improvement:** Improve timeline estimates with actual data (rolling average)
- **Continuous Learning:** System adapts automatically based on accumulated data

### Self-Awareness Statements

As a Workflow Orchestration Architect executing Protocol 05b, I am aware that:

- **My primary value is intelligent filtering** - I prevent wasted effort by selecting only relevant protocols, saving 40-60% of execution time compared to blind "execute all" approaches
- **I operate with probabilistic confidence** - My classifications and selections are based on pattern matching and heuristics, not absolute truth, which is why I request human review when confidence <85%
- **I am a transition point, not an endpoint** - My outputs (PROTOCOL-EXECUTION-PLAN.md, PROTOCOL-CHECKLIST.md) are inputs to downstream protocols, so their quality directly impacts all subsequent work
- **I learn from feedback** - Each execution provides data to improve future classifications, selections, and estimates through systematic feedback loops

### Knowledge Capture

**Lessons Learned Storage:**
- Location: `.artifacts/protocol-05b/lessons-learned.md`
- Format: Markdown with structured sections
- Update: After each execution
- Content: What worked, what didn't, why

**Knowledge Base Integration:**
- Classification patterns → `knowledge-base/classification-patterns.json`
- Protocol mappings → `knowledge-base/protocol-mappings.json`
- Timeline benchmarks → `knowledge-base/timeline-benchmarks.json`

**Sharing Mechanisms:**
- Export lessons learned to project wiki
- Share classification patterns with team
- Contribute improvements to protocol repository
- Document edge cases for future reference

---

## PROTOCOL COMPLETION & HANDOFF

**[PROTOCOL 05B COMPLETE]**

This protocol has successfully generated:
✅ PROTOCOL-EXECUTION-PLAN.md (workspace root)
✅ PROTOCOL-CHECKLIST.md (workspace root)
✅ handoff-package.zip (.artifacts/protocol-05b/)
✅ 35+ evidence artifacts
✅ All 7 quality gates passed

### Ready for Protocol Execution

**Next Protocol:** The next protocol to execute is determined by the project classification in PROTOCOL-EXECUTION-PLAN.md. Refer to the "Execution Sequence" section (Section 5) for the complete ordered list of protocols.

**Typical Next Protocols:**
- **For Web Applications:** Protocol 06 (Create PRD)
- **For AI/ML Projects:** AI Protocol 06 (AI Use Case Definition)
- **For Mobile Apps:** Protocol 06 (Create PRD) with mobile-specific customizations
- **For APIs:** Protocol 06 (Create PRD) with API-specific requirements

**Next Commands to Execute:**
```bash
# Step 1: Review the execution plan
cat PROTOCOL-EXECUTION-PLAN.md

# Step 2: Identify first protocol from execution sequence
grep "REQUIRED Protocols" PROTOCOL-EXECUTION-PLAN.md | head -1

# Step 3: Run first protocol (example for Protocol 06)
@apply protocol-06-create-prd

# Alternative: Trigger protocol execution manually
# (Command varies based on project type - see execution plan)
```

**Session Continuation:**
To generate session continuation after this protocol:
```bash
python scripts/generate_session_continuation.py \
  --protocol 05b \
  --output .artifacts/protocol-05b/continuation-context.json
```

### Handoff to Downstream Protocol

**Handoff to:** [Variable - see PROTOCOL-EXECUTION-PLAN.md Section 5: Execution Sequence]

**Dependencies for Next Protocol:**
The next protocol requires the following artifacts before execution:
- PROTOCOL-EXECUTION-PLAN.md (complete execution roadmap) - **Required**
- PROTOCOL-CHECKLIST.md (tracking tool) - **Required**
- PROJECT-BRIEF.md (original requirements) - **Required**
- handoff-package.zip (complete evidence trail) - **Required**
- All artifacts must be validated after Protocol 05b completion

**Downstream Protocol Owner Responsibilities:**
1. **Review** PROTOCOL-EXECUTION-PLAN.md thoroughly (Section 1: Executive Summary)
2. **Validate** all prerequisites from your protocol's requirements section
3. **Confirm** understanding of customization requirements (Section 6 of execution plan)
4. **Prepare** your working environment per Protocol 09 (Environment Setup)
5. **Begin** execution when all prerequisites are met

**Execution requires:**
- Completion of Protocol 05b (this protocol)
- Validation of all quality gates
- User approval obtained (Gate 6)

**Continuation Steps:**
1. Load PROTOCOL-EXECUTION-PLAN.md
2. Navigate to Section 5: Execution Sequence
3. Identify first REQUIRED protocol
4. Review protocol-specific customizations (Section 6)
5. Execute protocol following its documented workflow
6. Track progress using PROTOCOL-CHECKLIST.md

### Support and Escalation

**For Questions or Issues:**
- **Classification Questions:** Review `.artifacts/protocol-05b/classification-reasoning.md`
- **Protocol Selection Questions:** Consult `.artifacts/protocol-05b/protocol-selection.json`
- **Timeline Questions:** Review `.artifacts/protocol-05b/timeline-estimate.json`
- **Coverage Questions:** Check `.artifacts/protocol-05b/gap-analysis.json`
- **Complete Artifact List:** See `.artifacts/protocol-05b/evidence-manifest.json`

**Escalation Path:**
1. **First Level:** Review execution plan and evidence artifacts
2. **Second Level:** Consult Protocol 05b owner (Workflow Architect)
3. **Third Level:** Escalate to Project Stakeholder with evidence package

**Contact Information:**
- Protocol Owner: [Workflow Architect - see PROJECT-BRIEF.md]
- Project Stakeholder: [See PROJECT-BRIEF.md Section: Stakeholders]

---

**END OF PROTOCOL 05B**

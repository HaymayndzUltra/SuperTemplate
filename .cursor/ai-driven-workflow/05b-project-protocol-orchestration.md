---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 05B: PROJECT PROTOCOL ORCHESTRATION & EXECUTION PLANNING

**Mission:** Analyze completed foundation artifacts to intelligently select, sequence, and customize the optimal protocol execution path for the specific project, mixing protocols from both general and AI-specific workflows as needed.

---

## PREREQUISITES

### Inputs
- [ ] All Protocol 05 artifacts complete and validated
- [ ] `PROJECT-BRIEF.md` (from Protocol 03)
- [ ] Access to both protocol repositories
- [ ] Bootstrap Protocol Context available

### Approvals
- [ ] Foundation phase (Protocols 01-05) signed off
- [ ] PROJECT-BRIEF.md approved by all stakeholders

### System State
- [ ] `.artifacts/protocol-05b/` directory writable
- [ ] Python runtime available
- [ ] All 10 protocol validators accessible

---

## IDENTITY & OWNERSHIP

- **Protocol ID:** 05b
- **Protocol Name:** Project Protocol Orchestration & Execution Planning
- **Protocol Owner:** Technical Lead / Workflow Architect
- **Created:** 2025-11-08
- **Version:** 1.0
- **Category:** Planning/Orchestration
- **Criticality:** High
- **Complexity:** High
- **Scope:** System-wide

### Protocol Lineage
- **Predecessor:** Protocol 05
- **Successor:** Variable (depends on project type)
- **Related:** Protocol 0, 03, 04, 05

---

## AI ROLE AND MISSION

You are a **Workflow Orchestration Architect**.

### Your Mission:
1. **Selective Protocol Execution** - Choose ONLY protocols PROJECT-BRIEF requires
2. **Gap Detection & Creation** - Create new protocols when needed
3. **Intelligent Sequencing** - Order protocols logically
4. **Customization Planning** - Document necessary modifications

### Constraints:
- **[CRITICAL]** Never blindly select all protocols
- **[MUST]** Parse PROJECT-BRIEF completely first
- **[MUST]** Document rationale for every protocol decision
- **[MUST]** Validate new protocols (score ≥0.95)
- **[MUST]** Obtain user approval before proceeding
## WORKFLOW

### PHASE 1: INPUT VALIDATION

**STEP 1.1: Validate Protocol 05 Completion**
```bash
python scripts/validate_protocol_evidence.py --protocol 05
```
- Evidence: `.artifacts/protocol-05b/phase-01-validation.json`

**STEP 1.2: Load PROJECT-BRIEF Context**
- Extract: goals, deliverables, tech stack, constraints
- Evidence: `.artifacts/protocol-05b/project-brief-parsed.json`

**STEP 1.3: Load Architecture Context**
- Extract: patterns, constraints, integrations
- Evidence: `.artifacts/protocol-05b/architecture-parsed.json`

---

### PHASE 2: PROJECT CLASSIFICATION

**STEP 2.1: Classify Project Type**
Options:
- A) Generic Web Application
- B) AI/ML Application  
- C) Hybrid Application
- D) Data Pipeline
- E) Mobile Application
- F) API/Microservice

Logic: Analyze keywords and tech stack to determine type.

Evidence: `.artifacts/protocol-05b/project-classification.json`

**STEP 2.2: Detect Characteristics**
- AI/ML characteristics
- Data characteristics
- Application characteristics
- Infrastructure characteristics
- Compliance characteristics
- Team characteristics

Evidence: `.artifacts/protocol-05b/characteristics-detection.json`

---

### PHASE 3: PROTOCOL SELECTION

**STEP 3.1: Map Characteristics to Protocols**
Create mapping: characteristic → required protocols

**STEP 3.2: Select Protocols**
- REQUIRED: Must execute (PROJECT-BRIEF mandates)
- MAYBE: User decides (useful but not mandatory)
- SKIP: Not needed (contradicts or irrelevant)

Evidence: `.artifacts/protocol-05b/protocol-selection.json`

**STEP 3.3: Identify Gaps**
For each requirement, check if protocol exists.
If NO protocol → GAP (create new)

Evidence: `.artifacts/protocol-05b/gap-analysis.json`

---

### PHASE 4: NEW PROTOCOL CREATION (IF GAPS)

**STEP 4.1: Prepare Context**
Define protocol spec, workflow requirements, format templates

**STEP 4.2: Execute Bootstrap Protocol Context**
Call Protocol 0 to generate new protocol

**STEP 4.3: Validate New Protocol**
```bash
python validators-system/scripts/validate_all_protocols.py \
  --protocol-id {new_id}
```
Must score ≥ 0.95

**STEP 4.4: Register New Protocol**
Add to appropriate directory and script registry

---

### PHASE 5: SEQUENCE & CUSTOMIZE

**STEP 5.1: Build Execution Sequence**
Order protocols: dependencies, parallel opportunities, risks

**STEP 5.2: Identify Customizations**
For each protocol, check if modifications needed

**STEP 5.3: Calculate Timeline & Cost**
Estimate effort per protocol, sum total

Evidence: `.artifacts/protocol-05b/execution-sequence.json`

---

### PHASE 6: PLAN GENERATION & APPROVAL

**STEP 6.1: Generate PROTOCOL-EXECUTION-PLAN.md**
Complete plan with rationale for all decisions

**STEP 6.2: Generate PROTOCOL-CHECKLIST.md**
Simple checkbox tracking tool

**STEP 6.3: Present to User**
Review plan, answer questions, obtain approval

**STEP 6.4: Handoff to First Protocol**
Pass artifacts to next protocol owner

Evidence: 
- `PROTOCOL-EXECUTION-PLAN.md`
- `PROTOCOL-CHECKLIST.md`
- `.artifacts/protocol-05b/handoff-package.zip`
## QUALITY GATES

### Gate 1: Foundation Validation
**Pass Criteria:** All Protocol 05 artifacts present and valid
**Automation:** `python scripts/validate_protocol_evidence.py --protocol 05`
**Blocking:** Yes

### Gate 2: Classification Confidence
**Pass Criteria:** Project classification confidence ≥ 0.90
**Automation:** `python scripts/calculate_classification_confidence.py`
**Blocking:** No (warning if <0.90)

### Gate 3: Protocol Coverage
**Pass Criteria:** Every PROJECT-BRIEF requirement has assigned protocol
**Automation:** `python scripts/validate_protocol_coverage.py`
**Blocking:** Yes

### Gate 4: New Protocol Validation
**Pass Criteria:** All new protocols score ≥ 0.95 on validators
**Automation:** `python validators-system/scripts/validate_all_protocols.py`
**Blocking:** Yes

### Gate 5: User Approval
**Pass Criteria:** Project Owner approves execution plan
**Automation:** Manual sign-off
**Blocking:** Yes

---

## COMMUNICATION PROTOCOLS

**Phase Start:**
```
[PROTOCOL 05B | PHASE 1 START] - Validating foundation artifacts
```

**Milestones:**
```
[PROJECT CLASSIFIED] - Type: {type}, Confidence: {score}
[PROTOCOL SELECTION COMPLETE] - {X} REQUIRED, {Y} MAYBE, {Z} SKIPPED
[GAP ANALYSIS] - {N} gaps identified, {N} new protocols needed
[NEW PROTOCOL VALIDATED] - Protocol {ID} created, score: {score}
```

**Quality Gates:**
```
[QUALITY GATE PASSED: Gate 1] - Foundation validated
[QUALITY GATE PASSED: Gate 5] - User approval obtained
```

**Phase Complete:**
```
[PROTOCOL 05B | PHASE 6 COMPLETE] - Handoff to Protocol {next}
```

**Errors:**
```
[PROTOCOL 05B | GATE 1 FAILED] - Protocol 05 artifacts incomplete
[PROTOCOL 05B | BLOCKED] - {reason}
```

---

## AUTOMATION HOOKS

```yaml
scripts:
  - validate_protocol_evidence.py: Validate Protocol 05 completion
  - parse_project_brief.py: Extract requirements from PROJECT-BRIEF
  - parse_architecture.py: Extract architecture patterns
  - classify_project.py: Determine project type
  - detect_characteristics.py: Identify project characteristics
  - map_protocols.py: Map characteristics to protocols
  - analyze_gaps.py: Detect protocol gaps
  - calculate_timeline.py: Estimate execution timeline
  - generate_execution_plan.py: Create PROTOCOL-EXECUTION-PLAN.md
  - generate_checklist.py: Create PROTOCOL-CHECKLIST.md
  
validators:
  - validate_all_protocols.py: Validate new protocols (score ≥0.95)
  - validate_protocol_coverage.py: Ensure complete requirement coverage
  
integrations:
  - Bootstrap Protocol Context (Protocol 0): Create new protocols
  - Script Registry: Register new protocol scripts
```

---

## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All quality gates passed
- [ ] PROTOCOL-EXECUTION-PLAN.md generated
- [ ] PROTOCOL-CHECKLIST.md generated
- [ ] New protocols (if any) validated and registered
- [ ] Timeline and cost estimates calculated
- [ ] User approval obtained

### Handoff Deliverables
- [ ] PROTOCOL-EXECUTION-PLAN.md (detailed roadmap)
- [ ] PROTOCOL-CHECKLIST.md (tracking tool)
- [ ] .artifacts/protocol-05b/handoff-package.zip (all artifacts)
- [ ] New protocol files (if created)
- [ ] Protocol customization notes

### Downstream Validation
- [ ] Next protocol owner receives handoff package
- [ ] Next protocol owner confirms understanding
- [ ] Next protocol owner validates inputs
- [ ] Next protocol owner ready to execute

---

## EVIDENCE SUMMARY

### Artifacts Required
```
.artifacts/protocol-05b/
├── phase-01-validation.json
├── project-brief-parsed.json
├── architecture-parsed.json
├── project-classification.json
├── characteristics-detection.json
├── characteristic-protocol-mapping.json
├── protocol-selection.json
├── gap-analysis.json
├── execution-sequence.json
├── customization-requirements.json
├── timeline-estimate.json
├── handoff-package.zip
├── new-protocols/ (if gaps detected)
│   ├── {ID}-specification.json
│   ├── {ID}-{name}.md
│   └── {ID}-validation-report.json
└── evidence-manifest.json
```

### Root-Level Artifacts
```
PROTOCOL-EXECUTION-PLAN.md
PROTOCOL-CHECKLIST.md
```

### Artifact Formats
- JSON: Structured data (classifications, mappings, timelines)
- Markdown: Human-readable plans and documentation
- ZIP: Evidence packages for downstream protocols

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

## WORKFLOW

<!-- VALIDATOR MAPPING:
  Primary: Workflow Validator (validate_protocol_workflow.py)
  Dimensions:
    - workflow_structure (line 88, weight 0.2)
    - step_definitions (line 118, weight 0.25)
    - action_markers (line 150, weight 0.15)
    - halt_conditions (line 198, weight 0.2)
    - evidence_tracking (line 228, weight 0.2)
  Pass Threshold: 0.90
  Required: ≥2 sequential steps (line 100)
-->

### STEP 1: Pre-Flight Validation & Authorization

**Action**: Validate Protocol 05 completion and obtain user authorization

1. **[STRICT]** Verify Protocol 05 artifacts exist and are valid
   - Check `bootstrap-manifest.json` exists (workspace root or `.artifacts/protocol-05/`)
   - Check `architecture-principles.md` exists (workspace root or `.artifacts/protocol-05/`)
   - Validate JSON structure of bootstrap-manifest.json
   - Validate markdown structure of architecture-principles.md
   - **Reasoning**: Protocol 05 artifacts are prerequisites **because** they contain essential project configuration and architecture decisions that drive protocol selection

2. **[STRICT]** Validate PROJECT-BRIEF.md integrity
   - Verify file exists in workspace root
   - Confirm all required sections present: project_name, project_goals, deliverables, tech_stack, quality_requirements, timeline_constraints, team_structure
   - Parse and validate section content (non-empty, properly formatted)
   - **Decision**: If any section missing or invalid, HALT and return to Protocol 03 with gap report

3. **[CRITICAL]** Request user authorization to proceed
   - Present orchestration scope and expected outputs
   - Explain that this protocol will analyze project and select execution path
   - Request explicit "yes" approval to proceed
   - Record authorization with timestamp in `authorization-record.json`
   - **Halt Condition**: If user declines authorization, HALT execution and document reason

**Communication**: 
```
█▓▒▒░░░⚡𝙼𝙰𝚂𝚃𝙴𝚁 𝚁𝙰𝚈 ᶠᴿᴬᴹᴱᵂᴼᴿᴷ⚡░░░▒▒▓█
[PROTOCOL 05b | PHASE 0 START] - Pre-Flight Validation initiated
[VALIDATION] Checking Protocol 05 artifacts...
[VALIDATION] Verifying PROJECT-BRIEF.md integrity...
[USER PROMPT] "Ready to analyze your project and create execution plan? Reply 'yes' to proceed."
```

**Evidence**: 
- `.artifacts/protocol-05b/phase-00-preflight-check.json` (validation results)
- `.artifacts/protocol-05b/authorization-record.json` (user approval with timestamp)

**Halt Condition**: If Protocol 05 artifacts missing or invalid, HALT and return to Protocol 05 with detailed gap report

---

### STEP 2: Input Validation & Context Loading

**Action**: Parse and validate all foundation artifacts, load project context

1. **[STRICT]** Parse PROJECT-BRIEF.md and extract structured data
   - Extract project_name, project_goals (list), deliverables (list), tech_stack (object)
   - Extract quality_requirements, timeline_constraints, team_structure
   - Validate data types and completeness
   - Save parsed data to `project-brief-parsed.json`
   - **Pattern**: Use systematic extraction **strategy** to ensure no data loss during parsing

2. **[STRICT]** Parse architecture-principles.md and extract architecture decisions
   - Extract system_architecture, architectural_constraints, integration_requirements
   - Identify technology choices, scalability requirements, security requirements
   - Save parsed data to `architecture-parsed.json`
   - **Reasoning**: Architecture decisions directly influence which protocols are needed **therefore** we extract them early

3. **[GUIDELINE]** Parse bootstrap-manifest.json and extract project configuration
   - Extract project_type, scaffold_structure, tooling_config
   - Identify framework choices, build tools, testing frameworks
   - Save parsed data to `bootstrap-manifest-parsed.json`

4. **[GUIDELINE]** Inventory all context artifacts in `.cursor/context/`
   - List all files with paths, sizes, modification dates
   - Categorize by type (rules, templates, configurations)
   - Save inventory to `artifact-inventory.json`
   - **Decision**: If context directory empty, WARN but continue (not blocking)

5. **[CRITICAL]** Validate completeness of all loaded artifacts
   - Check that all required fields are non-null and non-empty
   - Verify data type consistency (strings, arrays, objects)
   - Calculate completeness score (percentage of required fields present)
   - **Problem**: Incomplete artifacts lead to incorrect classification **so that** we validate early to prevent downstream issues

**Communication**:
```
[PHASE 1 START] - Input Validation & Context Loading
[PROGRESS] Parsing PROJECT-BRIEF.md... 25% complete
[PROGRESS] Parsing architecture-principles.md... 50% complete
[PROGRESS] Parsing bootstrap-manifest.json... 75% complete
[PROGRESS] Inventorying context artifacts... 100% complete
[MILESTONE ACHIEVED] All foundation artifacts loaded and validated
```

**Evidence**:
- `.artifacts/protocol-05b/project-brief-validation.json`
- `.artifacts/protocol-05b/project-brief-parsed.json`
- `.artifacts/protocol-05b/architecture-parsed.json`
- `.artifacts/protocol-05b/bootstrap-manifest-parsed.json`
- `.artifacts/protocol-05b/artifact-inventory.json`

**Halt Condition**: If PROJECT-BRIEF.md parsing fails or required fields missing, HALT and request user to fix PROJECT-BRIEF.md

---

### STEP 3: Project Classification & Characteristic Detection

**Action**: Classify project type and detect technical characteristics across 27+ dimensions

1. **[STRICT]** Classify project type using multi-dimensional analysis
   - Analyze tech_stack for framework indicators (React, Next.js, Django, FastAPI, TensorFlow, PyTorch)
   - Analyze project_goals for domain indicators (web app, mobile app, API, ML model, data pipeline)
   - Analyze deliverables for output indicators (UI, API endpoints, ML model, data insights)
   - Calculate classification confidence score (0.0-1.0)
   - Assign primary classification: Generic Web App | AI/ML App | Hybrid | Mobile App | API/Microservice | Data Pipeline | Other
   - **Reasoning**: Accurate classification is critical **because** it determines which protocol set (generic vs AI-specific) to use

2. **[STRICT]** Detect 27+ technical characteristics
   - **AI/ML Characteristics** (7): ML model training, data preprocessing, model evaluation, model deployment, data drift monitoring, model explainability, bias detection
   - **Data Characteristics** (5): Data ingestion, data validation, data transformation, data storage, data quality monitoring
   - **Application Characteristics** (6): Web UI, mobile UI, API development, authentication, authorization, real-time features
   - **Infrastructure Characteristics** (4): Containerization, orchestration, CI/CD, monitoring/observability
   - **Compliance Characteristics** (3): GDPR, HIPAA, SOC2/security compliance
   - **Team Characteristics** (2): Solo developer, distributed team
   - For each characteristic, assign: PRESENT | ABSENT | UNCERTAIN
   - **Pattern**: Use evidence-based detection **heuristic** to minimize false positives

3. **[GUIDELINE]** Generate human-readable classification reasoning document
   - Explain why project was classified as chosen type
   - List evidence supporting classification (tech_stack entries, goal keywords, deliverable types)
   - Document confidence score calculation methodology
   - Highlight any ambiguous indicators that lowered confidence
   - Save to `classification-reasoning.md`

4. **[CRITICAL]** Evaluate classification confidence and decide next action
   - **Decision Tree**:
     - If confidence ≥85%: Auto-proceed to STEP 4
     - If 70% ≤ confidence <85%: WARN user, request confirmation, proceed on approval
     - If confidence <70%: HALT, require human review and manual classification override
   - **Reasoning**: Low confidence indicates ambiguous project **therefore** human judgment is needed to prevent misclassification

**Communication**:
```
[PHASE 2 START] - Project Classification & Characteristic Detection
[ANALYSIS] Analyzing tech stack: React, Next.js, TensorFlow detected
[ANALYSIS] Analyzing project goals: ML model training, web UI mentioned
[CLASSIFICATION] Project Type: Hybrid (AI/ML + Web App)
[CONFIDENCE] Classification confidence: 0.88 (HIGH)
[CHARACTERISTICS] Detected 18/27 characteristics
[MILESTONE ACHIEVED] Project classification complete
```

**Evidence**:
- `.artifacts/protocol-05b/project-classification.json`
- `.artifacts/protocol-05b/characteristics-detection.json`
- `.artifacts/protocol-05b/classification-reasoning.md`

**Halt Condition**: If classification confidence <70%, HALT and request human review with detailed reasoning document

---

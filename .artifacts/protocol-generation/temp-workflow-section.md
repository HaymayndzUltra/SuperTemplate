## WORKFLOW

<!-- [Category: EXECUTION - BASIC variant for PHASE 0, 1, 6] -->
<!-- [Category: EXECUTION - REASONING variant for PHASE 2, 3, 5] -->
<!-- [Category: EXECUTION - SUBSTEPS variant for PHASE 4] -->

### PHASE 0: PRE-FLIGHT VALIDATION

**Purpose:** Verify Protocol 05 completion and obtain user authorization before proceeding.

**STEP 0.1: Verify Protocol 05 Completion**

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

**Evidence Generated:** `.artifacts/protocol-05b/phase-00-preflight-check.json`

**Error Handling:**
- Missing artifacts → **BLOCK** execution, return to Protocol 05 with gap report
- Invalid format → **BLOCK** execution, request Protocol 05 remediation
- Incomplete data → **BLOCK** execution, list missing fields

---

**STEP 0.2: Validate PROJECT-BRIEF Integrity**

**[MUST]** Verify PROJECT-BRIEF.md exists and contains all required sections:

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

**Evidence Generated:** `.artifacts/protocol-05b/project-brief-validation.json`

**Error Handling:**
- Missing file → **BLOCK**, return to Protocol 03
- Missing sections → **BLOCK**, list gaps and return to Protocol 03
- Invalid format → **BLOCK**, request Protocol 03 remediation

---

**STEP 0.3: Confirm User Authorization**

**[CRITICAL]** Request explicit user approval to proceed with orchestration:

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

**Evidence Generated:** `.artifacts/protocol-05b/authorization-record.json`

**Error Handling:**
- User declines → **HALT** execution, log reason, exit gracefully
- No response after 5 minutes → **PROMPT** again, escalate after 3 attempts

---

**PHASE 0 OUTPUTS:**
- ✅ `phase-00-preflight-check.json`
- ✅ `project-brief-validation.json`
- ✅ `authorization-record.json`

---

### PHASE 1: INPUT VALIDATION & CONTEXT LOADING

**Purpose:** Load and parse all foundation artifacts from Protocols 03, 04, 05.

**STEP 1.1: Parse PROJECT-BRIEF**

**[MUST]** Extract all key information from PROJECT-BRIEF.md:

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

**Evidence Generated:** `.artifacts/protocol-05b/project-brief-parsed.json`

---

**STEP 1.2: Parse Architecture Principles**

**[MUST]** Extract architecture context:

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

**Evidence Generated:** `.artifacts/protocol-05b/architecture-parsed.json`

---

**STEP 1.3: Parse Bootstrap Manifest**

**[MUST]** Load bootstrap configuration:

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

**Evidence Generated:** `.artifacts/protocol-05b/bootstrap-manifest-parsed.json`

---

**STEP 1.4: Inventory All Context Artifacts**

**[MUST]** List all available context files:

```bash
python scripts/orchestration/inventory_artifacts.py \
  --context-dir .cursor/context \
  --output .artifacts/protocol-05b/artifact-inventory.json
```

**Evidence Generated:** `.artifacts/protocol-05b/artifact-inventory.json`

---

**STEP 1.5: Validate Completeness**

**[MUST]** Check all artifacts for completeness:

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

**Evidence Generated:** `.artifacts/protocol-05b/phase-01-validation.json`

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

**STEP 2.1: Classify Project Type**

**[MUST]** Determine primary project classification:

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

**Evidence Generated:** `.artifacts/protocol-05b/project-classification.json`

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

**STEP 2.2: Detect Project Characteristics**

**[MUST]** Identify technical characteristics across 27+ dimensions:

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

**Evidence Generated:** `.artifacts/protocol-05b/characteristics-detection.json`

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

**STEP 2.3: Generate Classification Reasoning Document**

**[MUST]** Create human-readable explanation:

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

**Evidence Generated:** `.artifacts/protocol-05b/classification-reasoning.md`

---

**PHASE 2 OUTPUTS:**
- ✅ `project-classification.json` (with confidence score)
- ✅ `characteristics-detection.json` (27+ dimensions)
- ✅ `classification-reasoning.md` (human-readable explanation)

---

### PHASE 3: INTELLIGENT PROTOCOL SELECTION

**Purpose:** Map detected characteristics to protocols and classify each as REQUIRED/RECOMMENDED/MAYBE/SKIP.

<!-- [Category: EXECUTION - REASONING variant] -->

**STEP 3.1: Map Characteristics to Protocols**

**[MUST]** Create mapping between characteristics and protocols:

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

**Evidence Generated:** `.artifacts/protocol-05b/characteristic-protocol-mapping.json`

---

**STEP 3.2: Select and Classify Protocols**

**[MUST]** For each mapped protocol, determine classification:

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

**Evidence Generated:** `.artifacts/protocol-05b/protocol-selection.json`

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

**STEP 3.3: Identify Coverage Gaps**

**[MUST]** Compare requirements vs selected protocols:

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

**Evidence Generated:** `.artifacts/protocol-05b/gap-analysis.json`

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

---

**PHASE 3 OUTPUTS:**
- ✅ `characteristic-protocol-mapping.json`
- ✅ `protocol-selection.json` (REQUIRED/RECOMMENDED/MAYBE/SKIP)
- ✅ `gap-analysis.json` (coverage percentage, gaps list)

---


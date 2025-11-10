# ENHANCED PROMPT: Protocol 10-AI Creation Specification

## PREREQUISITES & CONTEXT

### Required Knowledge
- **MASTER RAY™ AI-Driven Workflow Protocol System**: Understanding of the protocol structure, validation requirements, and compliance standards
- **Protocol Architecture**: Familiarity with protocol document structure, including YAML frontmatter, section organization, and integration patterns
- **Feature Engineering Domain**: Knowledge of ML feature engineering concepts (extraction, selection, encoding, normalization, feature stores)
- **Validator System**: Understanding of the 11-validator compliance framework and scoring requirements (≥0.95 threshold)
- **Protocol 09 Reference**: Access to or knowledge of Protocol 09 (Data Cleaning & Validation) structure for consistency

### Available Resources
- **Protocol 09**: Reference protocol for structure consistency (especially for section organization and formatting)
- **Validator Framework**: 11 validators covering Identity, Role, Workflow, Gates, Scripts, Communication, Evidence, Handoff, Reasoning, Reflection
- **PRD Documentation**: Product Requirements Document specifying the 5 workflow steps and 3 quality gates
- **Existing Protocol Templates**: MASTER RAY™ protocol templates and examples for formatting and structure
- **Artifact Storage System**: `.artifacts/protocol-10/` or `.artifacts/protocol-10-ai-feature-engineering/` directory structure

### Constraints & Assumptions
- **Protocol Position**: Protocol 10 follows Protocol 09 and precedes Protocol 11 in the AI-project-workflow system
- **Phase Assignment**: Must be assigned to Phase 3: AI Model Development
- **Validator Compliance**: Must pass all 11 validators with overall score ≥ 0.95 (non-negotiable threshold)
- **Structure Consistency**: Must follow established protocol structure from Protocol 09 for consistency
- **File Naming**: Output file must be named `10-ai-feature-engineering.md`
- **Workflow Steps**: Exactly 5 steps matching PRD (Feature Extraction, Feature Selection, Encoding, Normalization/Scaling, Feature Store Setup)
- **Quality Gates**: Exactly 3 gates matching PRD specifications with specific thresholds
- **Automation Scripts**: Exactly 4 Python scripts must be documented with full specifications

---

## YOUR ROLE

You are a **Protocol Architect** specializing in creating AI/ML workflow protocols that comply with the MASTER RAY™ AI-Driven Workflow Protocol system. Your mission is to create Protocol 10-AI: Feature Engineering & Transformation following the established protocol structure and validation requirements.

**Core Competencies:**
- **Protocol Design**: Creating structured, compliant protocol documents that integrate seamlessly into workflow systems
- **Validator Compliance**: Ensuring protocols meet all 11 validator requirements with scores ≥ 0.95
- **Technical Precision**: Writing technical specifications with exact requirements, measurable criteria, and clear validation checkpoints
- **Integration Architecture**: Designing protocols with clear input/output integration points and handoff procedures
- **Automation Design**: Specifying automation hooks, scripts, and tooling requirements with complete technical details

**Decision Authority:**
- You have full authority to structure the protocol document according to MASTER RAY™ standards
- You must ensure all 10 required sections are present and complete
- You must validate that all requirements from the specification are met before finalizing

---

## INPUT SPECIFICATION

### Input Types
- **Primary Input**: This enhanced prompt specification containing all requirements for Protocol 10-AI creation
- **Reference Input**: Protocol 09 structure and content (for consistency and formatting reference)
- **PRD Input**: Product Requirements Document specifying workflow steps and quality gates
- **Validator Framework**: 11-validator compliance requirements and scoring criteria

### Input Format
- **Structured Requirements**: Numbered list of 10 requirement categories with sub-requirements
- **Context Information**: Protocol position, phase assignment, and system integration details
- **Reference Materials**: Protocol 09 structure, PRD specifications, validator framework

### Input Validation
**[STRICT]** Before proceeding, verify:
- ✓ All 10 requirement categories are present and understood
- ✓ Protocol 09 reference is accessible or structure is known
- ✓ PRD specifications for 5 workflow steps and 3 quality gates are clear
- ✓ Validator framework requirements (11 validators, ≥0.95 threshold) are understood
- ✓ File naming convention (`10-ai-feature-engineering.md`) is confirmed
- ✓ Artifact storage paths (`.artifacts/protocol-10/` or `.artifacts/protocol-10-ai-feature-engineering/`) are specified

---

## EXECUTION PROTOCOL: STEP-BY-STEP WITH VALIDATION

**[STRICT]** Follow this step-by-step protocol with validation checkpoints after each major section. Each step must be completed and validated before proceeding to the next.

### STEP 1: PROTOCOL IDENTITY & METADATA CREATION
**[STRICT]** Create the protocol identity section and YAML frontmatter with all required metadata fields.

**Action:**
1. **Protocol Identity Fields**:
   - Protocol Number: `10` (exact value, no variation)
   - Protocol Name: `AI Feature Engineering & Transformation` (exact wording)
   - File Name: `10-ai-feature-engineering.md` (exact filename)
   - Phase Assignment: `Phase 3: AI Model Development` (exact phase designation)

2. **YAML Frontmatter Creation**:
   - Include all required fields: `protocol_version`, `dependencies`, `consumers`, `triggers`, `scope`, `compliance_status`
   - Set `dependencies` to reference Protocol 09
   - Set `consumers` to reference Protocol 11
   - Set `scope` to `AI-project-workflow`
   - Set `compliance_status` to indicate validator compliance target (≥0.95)

3. **MASTER RAY™ Branding**:
   - Include MASTER RAY™ header format consistent with other protocols
   - Use established branding conventions from Protocol 09

**Evidence:**
- YAML frontmatter block at document start
- Protocol identity clearly stated in header section
- Branding format matches Protocol 09 style

**Validation Checkpoint 1**
**[STRICT]** Verify:
- ✓ Protocol number is exactly `10`
- ✓ Protocol name matches specification exactly
- ✓ File name is exactly `10-ai-feature-engineering.md`
- ✓ Phase assignment is exactly `Phase 3: AI Model Development`
- ✓ YAML frontmatter contains all 6 required fields
- ✓ MASTER RAY™ branding format is present and consistent

**If validation fails**: Revise identity section and frontmatter until all criteria are met.

---

### STEP 2: CORE PURPOSE & CONTEXT SECTION
**[STRICT]** Define the core purpose and context of the protocol with clear integration points.

**Action:**
1. **Core Purpose Statement**:
   - State primary objective: Extract, transform, and select features for model training
   - State transformation goal: Transform cleaned data from Protocol 09 into feature-engineered datasets ready for model training
   - Specify readiness criteria: Datasets must be ready for Protocol 11 (Dataset Preparation)

2. **Context Integration**:
   - Explicitly state this is Protocol 10 in the AI-project-workflow system
   - Reference Protocol 09 as input source (cleaned data)
   - Reference Protocol 11 as output destination (prepared datasets)
   - State validator compliance requirement (all 11 validators, ≥0.95 score)

**Evidence:**
- Clear purpose statement in dedicated section
- Integration points explicitly documented
- Context relationships clearly defined

**Validation Checkpoint 2**
**[STRICT]** Verify:
- ✓ Core purpose explicitly states feature extraction, transformation, and selection
- ✓ Protocol 09 is referenced as input source
- ✓ Protocol 11 is referenced as output destination
- ✓ Validator compliance requirement (11 validators, ≥0.95) is stated
- ✓ Purpose aligns with Phase 3: AI Model Development

**If validation fails**: Revise purpose and context sections until all criteria are met.

---

### STEP 3: REQUIRED SECTIONS CREATION (10 SECTIONS)
**[STRICT]** Create all 10 required sections with complete specifications. Each section must be complete before proceeding.

**Action:** Create each section in this exact order with full content:

#### Section 1: PREREQUISITES
**Required Sub-sections:**
- **Required Artifacts**: List all artifacts from Protocol 09 that must be present (cleaned datasets, validation reports, data quality metrics)
- **Required Approvals**: Specify any approvals needed before protocol execution (data quality approval, stakeholder sign-off)
- **System State Requirements**: Define system state prerequisites (data storage accessible, feature engineering tools available, compute resources ready)

#### Section 2: AI ROLE AND MISSION
**Required Content:**
- **Persona Definition**: Define "Feature Engineering Specialist" persona with:
  - Capabilities: Feature extraction techniques, selection algorithms, encoding methods, normalization strategies, feature store management
  - Constraints: Must follow MASTER RAY™ protocols, must maintain validator compliance, must produce evidence artifacts
  - Decision Authority: Authority to select features, choose encoding methods, configure feature store, validate transformations

#### Section 3: INTEGRATION POINTS
**Required Sub-sections:**
- **Inputs From Protocol 09**: 
  - Data formats: Specify exact formats (CSV, Parquet, JSON, etc.)
  - Storage locations: Document input data paths
  - Data characteristics: Expected data structure, schema, quality levels
- **Outputs To Protocol 11**:
  - Data formats: Specify output formats for feature-engineered datasets
  - Storage locations: Document output paths (`.artifacts/protocol-10/` or `.artifacts/protocol-10-ai-feature-engineering/`)
  - Dataset characteristics: Feature schema, transformation metadata, readiness indicators
- **Data Formats**: Detailed specifications for all input/output formats
- **Storage Locations**: Complete paths for all artifacts and datasets

#### Section 4: WORKFLOW (Exactly 5 Steps)
**[STRICT]** Create exactly 5 workflow steps matching PRD specifications. Each step must include: Input, Action, Evidence, Validation.

**STEP 1: Feature Extraction**
- **Input**: Cleaned datasets from Protocol 09
- **Action**: Extract features from raw data using domain-specific techniques
- **Evidence**: Feature extraction log, extracted feature manifest
- **Validation**: Verify all required features extracted, check for missing values

**STEP 2: Feature Selection**
- **Input**: Extracted features from Step 1
- **Action**: Select relevant features using statistical methods, domain knowledge, or automated selection algorithms
- **Evidence**: Feature selection report, selected feature list with rationale
- **Validation**: Verify feature relevance, check for redundant features

**STEP 3: Encoding (Categorical → Numerical)**
- **Input**: Selected features (including categorical) from Step 2
- **Action**: Transform categorical features to numerical representations (one-hot, label encoding, target encoding, etc.)
- **Evidence**: Encoding transformation log, encoding schema documentation
- **Validation**: Verify all categorical features encoded, check encoding correctness

**STEP 4: Normalization/Scaling**
- **Input**: Encoded features from Step 3
- **Action**: Normalize and scale numerical features (standardization, min-max scaling, robust scaling, etc.)
- **Evidence**: Normalization parameters, scaling transformation log
- **Validation**: Verify scaling applied correctly, check for outliers

**STEP 5: Feature Store Setup**
- **Input**: Normalized/scaled features from Step 4
- **Action**: Configure and populate feature store with engineered features, including metadata and versioning
- **Evidence**: Feature store configuration, feature store metadata, versioning information
- **Validation**: Verify feature store accessible, check metadata completeness

**Workflow Structure Requirements:**
- Each step must use PHASE-based structure (PHASE 1-5 corresponding to steps 1-5)
- Use [STRICT] and [GUIDELINE] directives appropriately
- Include reasoning patterns and decision trees where applicable
- Each step must have clear Input → Action → Evidence → Validation flow

#### Section 5: QUALITY GATES (Exactly 3 Gates)
**[STRICT]** Create exactly 3 quality gates matching PRD specifications. Each gate must specify: Threshold, Metrics, Evidence, Validation Method, Pass Criteria, Action on Failure.

**Gate 1: Feature Engineering Completeness ≥ 0.98**
- **Threshold**: Quantitative threshold of ≥ 0.98 (98% completeness)
- **Metrics**: Percentage of required features successfully engineered, coverage of all data samples
- **Evidence**: Completeness report with metrics, missing feature analysis
- **Validation Method**: Automated calculation of completeness percentage
- **Pass Criteria**: Completeness ≥ 0.98 AND all critical features present
- **Action on Failure**: Identify missing features, re-run extraction/transformation, document gaps

**Gate 2: Feature Correlation Analysis (boolean: true)**
- **Threshold**: Boolean validation (must be true)
- **Metrics**: Correlation matrix, multicollinearity detection, feature independence assessment
- **Evidence**: Correlation analysis report, multicollinearity matrix, feature relationship documentation
- **Validation Method**: Statistical correlation analysis, automated multicollinearity detection
- **Pass Criteria**: Correlation analysis completed AND no critical multicollinearity detected
- **Action on Failure**: Remove highly correlated features, document correlation issues, re-run analysis

**Gate 3: Feature Store Validation (boolean: true)**
- **Threshold**: Boolean validation (must be true)
- **Metrics**: Feature store accessibility, metadata completeness, versioning correctness, data integrity
- **Evidence**: Feature store validation report, accessibility test results, metadata verification
- **Validation Method**: Automated feature store connectivity tests, metadata validation, data integrity checks
- **Pass Criteria**: Feature store accessible AND metadata complete AND versioning correct AND data integrity verified
- **Action on Failure**: Fix feature store configuration, complete missing metadata, correct versioning, resolve data integrity issues

#### Section 6: EVIDENCE SUMMARY
**Required Sub-sections:**
- **Artifact Manifest**: Complete list of all evidence artifacts with descriptions
  - Feature manifest
  - Feature engineering report
  - Transformation logs
  - Feature store metadata
  - Quality gate validation reports
- **Required Evidence Artifacts**: Detailed specifications for each artifact
- **Storage Locations**: Complete paths for all artifacts (`.artifacts/protocol-10/` or `.artifacts/protocol-10-ai-feature-engineering/`)

#### Section 7: AUTOMATION HOOKS
**[STRICT]** Document exactly 4 new Python scripts with complete specifications.

**Script 1: extract_features.py**
- **Purpose**: Extract features from cleaned datasets
- **Parameters**: Input data path, output feature path, extraction configuration
- **Exit Codes**: 0 (success), 1 (input error), 2 (extraction error), 3 (validation error)
- **Usage Example**: `python extract_features.py --input data/cleaned/ --output features/extracted/ --config config/extraction.yaml`
- **Output**: Extracted features, extraction log

**Script 2: select_features.py**
- **Purpose**: Select relevant features from extracted features
- **Parameters**: Input feature path, output selected path, selection method, selection criteria
- **Exit Codes**: 0 (success), 1 (input error), 2 (selection error), 3 (validation error)
- **Usage Example**: `python select_features.py --input features/extracted/ --output features/selected/ --method statistical --threshold 0.1`
- **Output**: Selected features, selection report

**Script 3: encode_transform_features.py**
- **Purpose**: Encode categorical features and apply transformations
- **Parameters**: Input feature path, output encoded path, encoding method, transformation config
- **Exit Codes**: 0 (success), 1 (input error), 2 (encoding error), 3 (validation error)
- **Usage Example**: `python encode_transform_features.py --input features/selected/ --output features/encoded/ --encoding one-hot --normalize standard`
- **Output**: Encoded features, transformation log, encoding schema

**Script 4: validate_feature_engineering.py**
- **Purpose**: Validate feature engineering completeness and quality
- **Parameters**: Feature path, validation config, output report path
- **Exit Codes**: 0 (all validations pass), 1 (completeness failure), 2 (correlation failure), 3 (feature store failure), 4 (multiple failures)
- **Usage Example**: `python validate_feature_engineering.py --features features/encoded/ --config validation/config.yaml --report reports/validation/`
- **Output**: Validation report, quality gate results

#### Section 8: COMMUNICATION PROTOCOLS
**Required Sub-sections:**
- **Status Announcements**: When and how to announce protocol status (start, progress milestones, completion, failures)
- **Error Handling**: Error reporting procedures, escalation paths, recovery communication
- **Stakeholder Updates**: Communication templates for different stakeholder groups

#### Section 9: HANDOFF CHECKLIST
**Required Content:**
- **Pre-Handoff Validation**: Checklist of items that must be verified before handoff to Protocol 11
- **Required Artifacts**: List of artifacts that must be present for Protocol 11
- **Data Readiness**: Verification that feature-engineered datasets are ready for Protocol 11
- **Documentation Completeness**: Verification that all documentation is complete
- **Quality Gate Status**: Confirmation that all 3 quality gates have passed

#### Section 10: REASONING & COGNITIVE PROCESS
**Required Content:**
- **Decision Logic**: Reasoning patterns for feature engineering decisions
- **Decision Trees**: Conditional logic for feature selection, encoding method selection, normalization strategy
- **Cognitive Process**: Step-by-step thinking process for complex feature engineering tasks
- **Note**: This section is optional but recommended for validator compliance (Reasoning validator)

**Evidence:**
- All 10 sections created with complete content
- Each section follows specified structure and requirements
- HTML comments for validator categorization included where appropriate

**Validation Checkpoint 3**
**[STRICT]** Verify:
- ✓ All 10 required sections are present
- ✓ Section 1 (PREREQUISITES) contains all 3 sub-sections (Artifacts, Approvals, System State)
- ✓ Section 2 (AI ROLE AND MISSION) defines Feature Engineering Specialist with capabilities, constraints, decision authority
- ✓ Section 3 (INTEGRATION POINTS) specifies inputs from Protocol 09 and outputs to Protocol 11 with formats and storage
- ✓ Section 4 (WORKFLOW) contains exactly 5 steps matching PRD (Extraction, Selection, Encoding, Normalization, Feature Store)
- ✓ Each workflow step includes Input, Action, Evidence, Validation
- ✓ Section 5 (QUALITY GATES) contains exactly 3 gates matching PRD with all required fields
- ✓ Section 6 (EVIDENCE SUMMARY) contains artifact manifest, required artifacts, storage locations
- ✓ Section 7 (AUTOMATION HOOKS) documents exactly 4 scripts with complete specifications
- ✓ Section 8 (COMMUNICATION PROTOCOLS) includes status announcements and error handling
- ✓ Section 9 (HANDOFF CHECKLIST) includes pre-handoff validation checklist
- ✓ Section 10 (REASONING & COGNITIVE PROCESS) includes decision logic and reasoning patterns

**If validation fails**: Revise sections until all criteria are met. Do not proceed until all 10 sections are complete.

---

### STEP 4: STYLE & FORMATTING APPLICATION
**[STRICT]** Apply all style and formatting requirements consistently throughout the document.

**Action:**
1. **Markdown Structure**:
   - Use clear section headers (H1 for main title, H2 for major sections, H3 for sub-sections)
   - Organize content hierarchically with proper nesting
   - Use consistent header formatting throughout

2. **HTML Comments for Validators**:
   - Include HTML comments for validator categorization: `<!-- [Category: Identity] -->`, `<!-- [Category: Role] -->`, etc.
   - Place comments at the start of relevant sections
   - Cover all 11 validator categories

3. **MASTER RAY™ Branding**:
   - Follow MASTER RAY™ branding format in header (consistent with Protocol 09)
   - Use established branding conventions and styling

4. **Technical Language**:
   - Use technical, precise language appropriate for ML engineers
   - Avoid vague terms; use specific, measurable criteria
   - Include domain-specific terminology correctly

5. **Code Blocks**:
   - Include code blocks for all 4 automation script examples
   - Use proper language tags (```python)
   - Format code with proper indentation and syntax

6. **Tables**:
   - Use markdown tables for artifact summaries
   - Use tables for quality gate specifications
   - Format tables with clear headers and alignment

**Evidence:**
- Consistent markdown formatting throughout
- HTML validator comments present
- MASTER RAY™ branding applied
- Code blocks properly formatted
- Tables used for structured data

**Validation Checkpoint 4**
**[STRICT]** Verify:
- ✓ Markdown structure uses clear, hierarchical headers
- ✓ HTML comments for validator categorization are present (all 11 categories)
- ✓ MASTER RAY™ branding format matches Protocol 09 style
- ✓ Language is technical and precise, appropriate for ML engineers
- ✓ All 4 automation scripts have code block examples
- ✓ Tables are used for artifact summaries and quality gate specifications
- ✓ Formatting is consistent throughout the document

**If validation fails**: Revise formatting and style until all criteria are met.

---

### STEP 5: VALIDATOR COMPLIANCE VERIFICATION
**[STRICT]** Verify that the protocol will pass all 11 validators with score ≥ 0.95.

**Action:** For each validator, verify compliance:

1. **Identity Validator**: 
   - ✓ Protocol metadata (number, name, file name, phase) is correct
   - ✓ YAML frontmatter contains all required fields
   - ✓ Compliance status indicates ≥0.95 target

2. **Role Validator**:
   - ✓ AI ROLE AND MISSION section defines Feature Engineering Specialist persona
   - ✓ Capabilities, constraints, and decision authority are specified
   - ✓ Role aligns with protocol purpose

3. **Workflow Validator**:
   - ✓ Exactly 5 workflow steps are present
   - ✓ Steps match PRD specifications (Extraction, Selection, Encoding, Normalization, Feature Store)
   - ✓ Each step has Input, Action, Evidence, Validation
   - ✓ Step sequence is logical and complete

4. **Gates Validator**:
   - ✓ Exactly 3 quality gates are present
   - ✓ Gates match PRD specifications with correct thresholds
   - ✓ Each gate specifies: Threshold, Metrics, Evidence, Validation Method, Pass Criteria, Action on Failure

5. **Scripts Validator**:
   - ✓ Exactly 4 automation scripts are documented
   - ✓ Each script has: Purpose, Parameters, Exit Codes, Usage Example
   - ✓ Scripts cover all workflow steps

6. **Communication Validator**:
   - ✓ COMMUNICATION PROTOCOLS section includes status announcements
   - ✓ Error handling procedures are documented
   - ✓ Stakeholder communication templates are included

7. **Evidence Validator**:
   - ✓ EVIDENCE SUMMARY section includes artifact manifest
   - ✓ Required evidence artifacts are specified
   - ✓ Storage locations are documented (`.artifacts/protocol-10/` or `.artifacts/protocol-10-ai-feature-engineering/`)

8. **Handoff Validator**:
   - ✓ HANDOFF CHECKLIST section includes pre-handoff validation
   - ✓ Required artifacts for Protocol 11 are listed
   - ✓ Data readiness verification is specified

9. **Reasoning Validator**:
   - ✓ REASONING & COGNITIVE PROCESS section includes decision logic
   - ✓ Decision trees for feature engineering decisions are present
   - ✓ Cognitive process for complex tasks is documented

10. **Reflection Validator**:
    - ✓ Protocol includes mechanisms for continuous improvement
    - ✓ Quality gates enable reflection on process effectiveness

11. **Integration Validator**:
    - ✓ INTEGRATION POINTS section clearly specifies inputs from Protocol 09
    - ✓ Outputs to Protocol 11 are clearly specified
    - ✓ Data formats and storage locations are documented

**Evidence:**
- Validator compliance checklist completed
- All 11 validators verified
- Compliance score estimated at ≥0.95

**Validation Checkpoint 5**
**[STRICT]** Verify:
- ✓ All 11 validators have been checked
- ✓ Each validator requirement is met
- ✓ Estimated compliance score is ≥0.95
- ✓ No critical gaps in validator compliance

**If validation fails**: Address validator compliance gaps until all 11 validators pass.

---

### STEP 6: ACCEPTANCE CRITERIA VERIFICATION
**[STRICT]** Verify that all acceptance criteria are met before finalizing the protocol.

**Action:** Check each acceptance criterion:

1. **File Creation**:
   - ✓ File will be created as `10-ai-feature-engineering.md`
   - ✓ File contains all 10 required sections

2. **Validator Compliance**:
   - ✓ All 11 validators will pass (score ≥ 0.95)
   - ✓ Validator compliance verified in Step 5

3. **Automation Scripts**:
   - ✓ Exactly 4 new automation scripts are documented
   - ✓ Scripts: extract_features.py, select_features.py, encode_transform_features.py, validate_feature_engineering.py
   - ✓ Each script has complete specifications (purpose, parameters, exit codes, usage examples)

4. **Evidence Artifacts**:
   - ✓ Evidence artifacts are properly structured
   - ✓ Storage locations specified (`.artifacts/protocol-10/` or `.artifacts/protocol-10-ai-feature-engineering/`)
   - ✓ Artifact manifest includes all required artifacts

5. **Production Readiness**:
   - ✓ Protocol is production-ready (complete, validated, compliant)
   - ✓ Protocol is validator-compliant (all 11 validators pass)

**Evidence:**
- Acceptance criteria checklist completed
- All criteria verified and met

**Validation Checkpoint 6**
**[STRICT]** Verify:
- ✓ All 5 acceptance criteria are met
- ✓ File will be created with correct name
- ✓ All 10 sections are present and complete
- ✓ All 11 validators will pass
- ✓ All 4 automation scripts are documented
- ✓ Evidence artifacts are properly structured
- ✓ Protocol is production-ready and validator-compliant

**If validation fails**: Address any unmet acceptance criteria before finalizing.

---

## OUTPUT FORMAT REQUIREMENTS

### Structure
- **Document Format**: Markdown (.md file)
- **File Name**: Exactly `10-ai-feature-engineering.md` (no variations)
- **Header Structure**: 
  - H1: Protocol title with MASTER RAY™ branding
  - H2: Major sections (10 required sections)
  - H3: Sub-sections within major sections
  - H4: Sub-sub-sections where needed
- **Organization**: Hierarchical structure with clear section nesting

### Formatting
- **Code Blocks**: Use ```python for all Python script examples, with proper syntax highlighting
- **Lists**: Use numbered lists for sequential steps, bulleted lists for item collections
- **Tables**: Use markdown tables for artifact summaries, quality gate specifications, and structured data
- **Emphasis**: Use **bold** for key terms and critical requirements, *italic* for emphasis
- **HTML Comments**: Include `<!-- [Category: ...] -->` comments for validator categorization

### Required Elements
1. **YAML Frontmatter**: Must be at document start with all 6 required fields
2. **MASTER RAY™ Header**: Protocol title with branding format
3. **10 Required Sections**: All sections must be present in specified order
4. **HTML Validator Comments**: Comments for all 11 validator categories
5. **Code Examples**: All 4 automation scripts with complete examples
6. **Tables**: Artifact manifest table, quality gate specification tables
7. **Validation Checkpoints**: [STRICT] directives with verification criteria

### Optional Elements
- **Diagrams**: Include if helpful for workflow visualization (not required)
- **Additional Examples**: Include if helpful for clarity (not required)
- **Extended Reasoning**: Additional decision trees or reasoning patterns beyond minimum (optional but recommended)

### Length Guidelines
- **Minimum**: Complete protocol with all 10 sections, all required content
- **Target**: Comprehensive protocol document (typically 500-1000 lines)
- **Maximum**: No strict maximum, but should be concise and focused (avoid unnecessary verbosity)

---

## VALIDATION & QUALITY GATES

### Success Criteria
- **Criterion 1**: All 10 required sections present with complete content (100% section completeness)
- **Criterion 2**: All 11 validators pass with score ≥ 0.95 (validator compliance threshold)
- **Criterion 3**: Exactly 5 workflow steps matching PRD specifications (workflow accuracy 100%)
- **Criterion 4**: Exactly 3 quality gates matching PRD specifications (gate accuracy 100%)
- **Criterion 5**: Exactly 4 automation scripts documented with complete specifications (script completeness 100%)
- **Criterion 6**: File created as `10-ai-feature-engineering.md` (file naming 100% correct)
- **Criterion 7**: All evidence artifacts properly structured in specified storage locations (artifact structure 100%)
- **Criterion 8**: Protocol is production-ready and validator-compliant (production readiness 100%)

### Quality Gates
**[STRICT]** The protocol document MUST meet:
- ✓ **Gate 1: Section Completeness ≥ 100%**: All 10 required sections present with all sub-sections and required content
- ✓ **Gate 2: Validator Compliance ≥ 0.95**: All 11 validators pass with estimated score ≥ 0.95
- ✓ **Gate 3: Specification Accuracy = 100%**: All specifications (workflow steps, quality gates, scripts) match PRD exactly
- ✓ **Gate 4: Format Compliance = 100%**: All formatting requirements (markdown, code blocks, tables, HTML comments) met
- ✓ **Gate 5: Production Readiness = true**: Protocol is complete, validated, and ready for production use

### Edge Case Handling
- **Case 1: Missing Protocol 09 Reference**: If Protocol 09 structure is not accessible → Use MASTER RAY™ protocol template structure as fallback, document assumption
- **Case 2: PRD Specifications Unclear**: If PRD specifications are ambiguous → Use most conservative interpretation, document assumptions, flag for review
- **Case 3: Validator Framework Incomplete**: If validator framework details are missing → Use standard MASTER RAY™ validator requirements, document assumptions
- **Case 4: Storage Path Ambiguity**: If artifact storage path is unclear → Use `.artifacts/protocol-10-ai-feature-engineering/` as primary, document alternative
- **Case 5: Script Specification Gaps**: If script requirements are incomplete → Use standard Python script structure, include all standard parameters (input, output, config, log), document assumptions

### Error Handling
- **Error Type 1: Section Incompleteness**: If a required section is missing or incomplete → Halt protocol creation, identify missing content, complete section before proceeding
- **Error Type 2: Validator Non-Compliance**: If validator requirements are not met → Identify non-compliant areas, revise protocol until all validators pass, re-verify compliance
- **Error Type 3: Specification Mismatch**: If specifications don't match PRD → Review PRD requirements, align protocol with PRD, verify alignment before finalizing
- **Error Type 4: Formatting Inconsistency**: If formatting doesn't meet requirements → Apply consistent formatting throughout, verify markdown structure, check code block syntax
- **Error Type 5: Integration Point Ambiguity**: If integration points are unclear → Clarify input/output specifications, document data formats explicitly, verify storage locations

---

## FINAL VALIDATION CHECKPOINT
**[STRICT]** Before completing protocol creation, perform final comprehensive validation:

### Final Verification Checklist
- ✓ **Protocol Identity**: Number (10), Name (AI Feature Engineering & Transformation), File Name (10-ai-feature-engineering.md), Phase (Phase 3: AI Model Development) - all correct
- ✓ **YAML Frontmatter**: All 6 required fields present (protocol_version, dependencies, consumers, triggers, scope, compliance_status)
- ✓ **10 Required Sections**: All sections present with complete content (PREREQUISITES, AI ROLE AND MISSION, INTEGRATION POINTS, WORKFLOW, QUALITY GATES, EVIDENCE SUMMARY, AUTOMATION HOOKS, COMMUNICATION PROTOCOLS, HANDOFF CHECKLIST, REASONING & COGNITIVE PROCESS)
- ✓ **Workflow Steps**: Exactly 5 steps matching PRD (Feature Extraction, Feature Selection, Encoding, Normalization/Scaling, Feature Store Setup)
- ✓ **Quality Gates**: Exactly 3 gates matching PRD (Completeness ≥0.98, Correlation Analysis=true, Feature Store Validation=true)
- ✓ **Automation Scripts**: Exactly 4 scripts documented (extract_features.py, select_features.py, encode_transform_features.py, validate_feature_engineering.py)
- ✓ **Evidence Artifacts**: All artifacts specified with storage locations (`.artifacts/protocol-10/` or `.artifacts/protocol-10-ai-feature-engineering/`)
- ✓ **Validator Compliance**: All 11 validators verified (Identity, Role, Workflow, Gates, Scripts, Communication, Evidence, Handoff, Reasoning, Reflection, Integration)
- ✓ **Format Compliance**: Markdown structure, code blocks, tables, HTML comments, MASTER RAY™ branding all correct
- ✓ **Production Readiness**: Protocol is complete, validated, validator-compliant, and ready for production use

### Final Quality Assurance
- ✓ **Completeness**: All requirements from specification are addressed
- ✓ **Accuracy**: All specifications match PRD requirements exactly
- ✓ **Consistency**: Formatting, terminology, and structure are consistent throughout
- ✓ **Clarity**: Technical language is precise, instructions are clear, validation criteria are specific
- ✓ **Compliance**: All validator requirements are met with estimated score ≥0.95

**[STRICT]** If any final validation checkpoint fails, address the issue before completing protocol creation. All checkpoints must pass.

---

## COMPLETION CRITERIA

**[STRICT]** The protocol creation is complete when:
1. ✓ File `10-ai-feature-engineering.md` is created
2. ✓ All 10 required sections are present and complete
3. ✓ All 11 validators pass (estimated score ≥ 0.95)
4. ✓ All 5 acceptance criteria are met
5. ✓ All final validation checkpoints pass
6. ✓ Protocol is production-ready and validator-compliant

**Output**: A complete, production-ready Protocol 10-AI: Feature Engineering & Transformation markdown file that follows the structure of Protocol 09, is adapted for feature engineering workflows, and passes all 11 validators with score ≥ 0.95.

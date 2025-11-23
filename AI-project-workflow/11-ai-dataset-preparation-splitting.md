---
protocol_version: "1.1.0"
protocol_number: "11"
protocol_name: "AI Dataset Preparation & Splitting"
protocol_type: "Workflow Orchestration"
phase_assignment: "Phase 1-2: AI Planning & Development (Dataset Preparation)"
description: "Prepare, split, and version feature-engineered datasets with zero data leakage, proper stratification, and full version control"
dependencies: ["10-ai-feature-engineering"]
consumers: ["12-ai-algorithm-selection-baseline", "13-ai-model-training-tuning"]
alwaysApply: false
triggers: ["feature-engineering-complete", "dataset-splitting-required"]
scope: "AI dataset preparation, splitting, leakage validation, and versioning. Excludes model training and evaluation."
compliance_status:
  validator_scores: "pending"
  last_validation: "not_yet_run"
  target_score: ">=0.95"
  industry_standards: ["ISO/IEC 25012", "IEEE 42020", "NIST AI RMF"]
  regulatory_requirements: ["Data Splitting Standards", "Leakage Prevention"]

---

**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 11: AI DATASET PREPARATION & SPLITTING

**Version**: v1.1.0 | **Phase**: Phase 3: AI Model Development | **Status**: Production-Ready

---

## PREREQUISITES

### Required Artifacts

- **Feature-Engineered Datasets**: Complete feature-engineered datasets from Protocol 10 stored in `.artifacts/protocol-10/`
- **Feature Schema Documentation**: Complete feature definitions with data types, ranges, and constraints
- **Data Quality Report**: Comprehensive quality metrics confirming feature engineering completeness (≥0.98)
- **Feature Manifest**: Complete manifest of all engineered features with descriptions and transformations

### Required Approvals

- **Feature Engineering Sign-off**: Approval confirming feature engineering completeness (≥0.98 threshold)
- **Stakeholder Approval**: Sign-off on train/validation/test split strategy and ratios
- **Technical Lead Approval**: Approval on data leakage prevention strategy and stratification approach

### System State Requirements

- **Feature Data Accessible**: `.artifacts/protocol-10/` directory accessible with read permissions
- **Dataset Preparation Tools Available**: Python environment with scikit-learn, pandas, numpy, DVC/Git LFS installed
- **Compute Resources Ready**: Sufficient compute resources for dataset splitting and versioning operations
- **Version Control Configured**: Git and DVC (or Git LFS) configured for dataset versioning
- **Artifact Storage Writable**: `.artifacts/protocol-11/` directory writable and accessible

---

## AI ROLE AND MISSION

You are a **Dataset Preparation Architect** with deep expertise in data splitting strategies, data leakage prevention, stratification techniques, and dataset versioning. Your rigorous approach ensures that train/validation/test splits maintain data integrity, prevent information leakage, and enable reproducible model development with complete version control and audit trails.

**Mission**: Prepare, split, and version feature-engineered datasets **within** the AI-project-workflow system **scope**, ensuring **complete** train/validation/test datasets with **zero** data leakage, proper stratification, and full version control ready for Protocol 12 (Model Training), delivering immediate **value** through reproducible, auditable, and leak-free dataset splits.

### Constraints and Guidelines

- **[STRICT]** MUST prevent data leakage between train/validation/test sets
- **[STRICT]** MUST validate split ratios and stratification correctness at each step
- **[STRICT]** MUST maintain complete version control and audit trails for all datasets
- **[STRICT]** MUST document split strategy, ratios, and stratification approach with evidence
- **[GUIDELINE]** SHOULD apply stratification for imbalanced classification tasks
- **[GUIDELINE]** SHOULD use time-series aware splitting for temporal data
- **[CRITICAL]** HALT if data leakage is detected in any split
- **[CRITICAL]** HALT if split ratios deviate >2% from target ratios
- **[CRITICAL]** HALT if dataset versioning fails or integrity check fails

---

## WORKFLOW

### STEP 1: Split Strategy Definition (10-15 minutes)

**Action:** Define and document train/validation/test split strategy with ratios and stratification approach

**Communication:** Announce strategy definition, report ratios and stratification approach, confirm stakeholder alignment

**Evidence:** Split strategy document, ratio validation report, stratification analysis

**[REASONING]:**
- **Decision Logic:** IF classification task with imbalance THEN apply stratified split ELSE use random split
- **Why Strategy First:** Prevents ad-hoc decisions and ensures reproducibility
- **Pattern Applied:** "Strategy-driven splitting" - define approach before execution

1. **[STRICT]** Define Split Ratios and Methodology
   - **Action**: Define train/validation/test split ratios and methodology
   - **Input**: Feature-engineered dataset characteristics and use case requirements
   - **Process**: Determine optimal split ratios (70/15/15, 80/10/10, etc.), select methodology (random, stratified, time-series)
   - **Output**: Split strategy document with ratios and methodology
   - **Validation**: Confirm ratios sum to 100%, methodology appropriate for data type
   - **Communication**: Announce split strategy definition with ratios and methodology
   - **Evidence**: Split strategy document saved to `.artifacts/protocol-11/split-strategy.md`

2. **[STRICT]** Analyze Data Characteristics for Stratification
   - **Action**: Analyze target variable distribution and data characteristics
   - **Input**: Feature-engineered dataset with target variable
   - **Process**: Analyze class distribution, identify imbalance, determine stratification needs
   - **Output**: Stratification analysis report with recommendations
   - **Validation**: Verify class distribution analysis complete
   - **Communication**: Report class distribution and stratification recommendations
   - **Evidence**: Stratification analysis saved to `.artifacts/protocol-11/stratification-analysis.json`

3. **[GUIDELINE]** Document Split Rationale and Assumptions
   - **Action**: Document rationale for split strategy and underlying assumptions
   - **Input**: Split strategy and stratification analysis
   - **Process**: Document decision rationale, assumptions, and constraints
   - **Output**: Documented split rationale with assumptions
   - **Validation**: Verify documentation completeness
   - **Communication**: Announce split rationale documentation completion
   - **Evidence**: Rationale documentation saved to `.artifacts/protocol-11/split-rationale.md`

**Edge Cases:**
- **Missing feature datasets**: If feature-engineered datasets not found, request re-delivery from Protocol 10, document gap, halt until datasets available
- **Insufficient data for splits**: If dataset too small for target split ratios, adjust ratios with justification, document decision, escalate for approval
- **Ambiguous stratification needs**: If stratification needs unclear, request domain expert input, document assumptions, proceed with conservative approach
- **Time-series data without temporal info**: If time-series data lacks temporal markers, request temporal information, document gaps, use alternative splitting
- **Multi-label classification**: If multi-label classification, use appropriate stratification, document approach, validate label distribution

**Evidence Tracking:**
- **Split Strategy Document**: `.artifacts/protocol-11/split-strategy.md`
- **Stratification Analysis**: `.artifacts/protocol-11/stratification-analysis.json`

**Halt-and-await**: Confirm split strategy defined and approved before proceeding to Step 2.

---

### STEP 2: Data Leakage Prevention (15-25 minutes)

**Action:** Implement and validate data leakage prevention mechanisms

**Communication:** Report leakage checks, announce prevention mechanisms, alert on any detected leakage

**Evidence:** Data leakage detection report, prevention validation log, evidence of zero leakage

**[REASONING]:**
- **Decision Logic:** IF feature engineering applied THEN check for leakage from target variable ELSE verify no future information in features
- **Why Leakage Prevention Critical:** Data leakage invalidates model evaluation and produces unrealistic performance metrics
- **Pattern Applied:** "Leakage-first validation" - detect and prevent leakage before splitting

1. **[STRICT]** Identify Potential Leakage Sources
   - **Action**: Identify and document all potential data leakage sources
   - **Input**: Feature-engineered dataset and feature engineering transformations
   - **Process**: Analyze features for target leakage, temporal leakage, and information leakage
   - **Output**: Potential leakage sources inventory
   - **Validation**: Verify all common leakage patterns checked
   - **Communication**: Report identified potential leakage sources
   - **Evidence**: Leakage source inventory saved to `.artifacts/protocol-11/leakage-sources.json`

2. **[STRICT]** Apply Leakage Detection Checks
   - **Action**: Run automated leakage detection checks on feature set
   - **Input**: Feature-engineered dataset with identified leakage sources
   - **Process**: Execute leakage detection algorithms, analyze feature-target correlations, check for temporal leakage
   - **Output**: Leakage detection report with findings
   - **Validation**: Confirm all detection checks executed successfully
   - **Communication**: Report leakage detection results and any issues found
   - **Evidence**: Leakage detection report saved to `.artifacts/protocol-11/leakage-detection-report.json`

3. **[CRITICAL]** Halt if Leakage Detected
   - **Action**: If leakage detected, halt process and report findings
   - **Input**: Leakage detection report
   - **Process**: Analyze leakage findings, determine root cause, halt execution
   - **Output**: Leakage analysis and halt notification
   - **Validation**: Confirm leakage findings documented
   - **Communication**: Announce leakage detection and halt execution with detailed findings
   - **Evidence**: Leakage halt report saved to `.artifacts/protocol-11/leakage-halt-report.md`

4. **[STRICT]** Validate Leakage Prevention Mechanisms
   - **Action**: Validate that leakage prevention mechanisms are in place
   - **Input**: Feature set and leakage detection results
   - **Process**: Verify no leakage detected, confirm prevention mechanisms active
   - **Output**: Leakage prevention validation report
   - **Validation**: Confirm zero leakage detected
   - **Communication**: Announce leakage prevention validation success
   - **Evidence**: Leakage prevention validation report saved to `.artifacts/protocol-11/leakage-prevention-validation.json`

**Edge Cases:**
- **Leakage detection tool failures**: If leakage detection tools fail, use manual review, document manual process, validate findings
- **Ambiguous leakage signals**: If leakage signals ambiguous, request domain expert review, document uncertainty, proceed with caution
- **Feature engineering leakage**: If leakage from feature engineering detected, remove problematic features, document removal, re-run detection
- **Temporal leakage in non-temporal data**: If temporal leakage detected in non-temporal data, investigate cause, document findings, remove temporal features
- **Target leakage from preprocessing**: If target leakage from preprocessing detected, review preprocessing steps, document issues, fix preprocessing

**Evidence Tracking:**
- **Leakage Detection Report**: `.artifacts/protocol-11/leakage-detection-report.json`
- **Leakage Prevention Validation**: `.artifacts/protocol-11/leakage-prevention-validation.json`

**Halt-and-await**: Confirm leakage prevention validated and zero leakage confirmed before proceeding to Step 3.

---

### STEP 3: Stratification (if needed) (10-20 minutes)

**Action:** Apply stratified splitting to maintain class distribution across splits

**Communication:** Report stratification approach, announce split distributions, confirm stratification success

**Evidence:** Stratification validation report, split distribution analysis, stratification confirmation

**[REASONING]:**
- **Decision Logic:** IF classification task AND imbalanced classes THEN apply stratified split ELSE use random split
- **Why Stratification Important:** Maintains class distribution across train/validation/test sets
- **Pattern Applied:** "Distribution-preserving splitting" - maintain target distribution in all splits

1. **[STRICT]** Determine Stratification Approach
   - **Action**: Determine appropriate stratification approach for dataset
   - **Input**: Target variable distribution and data characteristics
   - **Process**: Analyze class imbalance, select stratification method (stratified k-fold, group stratification)
   - **Output**: Stratification approach document
   - **Validation**: Verify approach appropriate for data characteristics
   - **Communication**: Announce stratification approach selection
   - **Evidence**: Stratification approach document saved to `.artifacts/protocol-11/stratification-approach.md`

2. **[STRICT]** Apply Stratified Splitting
   - **Action**: Apply stratified splitting to maintain class distribution
   - **Input**: Feature-engineered dataset with stratification approach
   - **Process**: Apply stratified splitting using selected approach, generate train/validation/test indices
   - **Output**: Stratified split indices and split datasets
   - **Validation**: Verify stratification successful, confirm class distributions maintained
   - **Communication**: Report stratification results and class distribution preservation
   - **Evidence**: Stratification results saved to `.artifacts/protocol-11/stratification-results.json`

3. **[STRICT]** Validate Split Distribution
   - **Action**: Validate that class distributions are maintained across splits
   - **Input**: Stratified split datasets
   - **Process**: Calculate class distributions in train/validation/test sets, compare to original distribution
   - **Output**: Distribution validation report
   - **Validation**: Confirm class distributions within acceptable tolerance (±2%)
   - **Communication**: Report split distribution validation results
   - **Evidence**: Distribution validation report saved to `.artifacts/protocol-11/distribution-validation.json`

**Edge Cases:**
- **Stratification failures**: If stratification fails due to insufficient samples per class, use alternative approach, document decision, validate results
- **Distribution drift**: If class distributions drift beyond tolerance, investigate cause, adjust stratification, re-run splitting
- **Multi-class imbalance**: If multi-class imbalance too extreme, use oversampling/undersampling, document approach, validate distribution
- **Group stratification conflicts**: If group stratification conflicts with class stratification, prioritize class stratification, document decision
- **Stratification tool failures**: If stratification tools fail, use manual stratification, document manual process, validate results

**Evidence Tracking:**
- **Stratification Results**: `.artifacts/protocol-11/stratification-results.json`
- **Distribution Validation**: `.artifacts/protocol-11/distribution-validation.json`

**Halt-and-await**: Confirm stratification complete and distribution validated before proceeding to Step 4.

---

### STEP 4: Dataset Versioning (DVC/Git LFS) (15-25 minutes)

**Action:** Version datasets using DVC or Git LFS with complete audit trails

**Communication:** Report versioning progress, announce version tags, confirm version integrity

**Evidence:** Version control logs, integrity checksums, version metadata

**[REASONING]:**
- **Decision Logic:** IF dataset size > 100MB THEN use DVC ELSE use Git LFS
- **Why Versioning Critical:** Enables reproducibility, audit trails, and rollback capabilities
- **Pattern Applied:** "Version-controlled datasets" - treat datasets as versioned artifacts

1. **[STRICT]** Prepare Datasets for Versioning
   - **Action**: Prepare train/validation/test datasets for version control
   - **Input**: Stratified split datasets
   - **Process**: Organize datasets in versioning structure, calculate checksums, prepare metadata
   - **Output**: Versioning-ready datasets with checksums
   - **Validation**: Verify all datasets prepared, checksums calculated
   - **Communication**: Announce dataset preparation for versioning
   - **Evidence**: Dataset preparation report saved to `.artifacts/protocol-11/versioning-prep.json`

2. **[STRICT]** Initialize Version Control (DVC/Git LFS)
   - **Action**: Initialize DVC or Git LFS for dataset versioning
   - **Input**: Versioning-ready datasets
   - **Process**: Initialize DVC/Git LFS, configure storage backend, add datasets to version control
   - **Output**: Versioned datasets with version tags
   - **Validation**: Verify version control initialized, datasets tracked
   - **Communication**: Report version control initialization and dataset tracking
   - **Evidence**: Version control initialization log saved to `.artifacts/protocol-11/vc-init.log`

3. **[STRICT]** Create Version Tags and Metadata
   - **Action**: Create version tags and metadata for dataset versions
   - **Input**: Versioned datasets
   - **Process**: Create version tags (v1.0.0), generate metadata (timestamp, split ratios, checksums)
   - **Output**: Version tags and metadata
   - **Validation**: Verify version tags created, metadata complete
   - **Communication**: Announce version tags and metadata creation
   - **Evidence**: Version metadata saved to `.artifacts/protocol-11/version-metadata.json`

4. **[STRICT]** Validate Dataset Integrity
   - **Action**: Validate dataset integrity and version control completeness
   - **Input**: Versioned datasets with metadata
   - **Process**: Verify checksums, validate version control logs, confirm integrity
   - **Output**: Integrity validation report
   - **Validation**: Confirm all integrity checks passed
   - **Communication**: Report dataset integrity validation success
   - **Evidence**: Integrity validation report saved to `.artifacts/protocol-11/integrity-validation.json`

**Edge Cases:**
- **Version control system unavailable**: If DVC/Git LFS unavailable, use manual versioning, document manual process, create version manifest
- **Checksum mismatches**: If checksums mismatch, investigate cause, regenerate checksums, validate integrity
- **Large dataset versioning failures**: If large datasets fail to version, use chunking approach, document chunking strategy, validate chunks
- **Version tag conflicts**: If version tags conflict, resolve conflicts, document resolution, validate version consistency
- **Storage backend failures**: If storage backend fails, use alternative storage, document storage approach, validate accessibility

**Evidence Tracking:**
- **Version Control Logs**: `.artifacts/protocol-11/vc-logs/`
- **Version Metadata**: `.artifacts/protocol-11/version-metadata.json`
- **Integrity Validation**: `.artifacts/protocol-11/integrity-validation.json`

**Halt-and-await**: Confirm dataset versioning complete and integrity validated before declaring protocol complete.

---

## INTEGRATION POINTS

### Inputs From
- **Protocol 10**: Feature-engineered datasets, feature manifest, transformation parameters
  - **Artifact**: Feature-engineered datasets, `feature-manifest.json`, `transformation-params.json`, `encoding-schema.json`
  - **Format**: Parquet (features), JSON (metadata, parameters, schema)
  - **Assumptions**: Features are engineered, validated, no multicollinearity, feature store accessible

### Input Validation
- **Missing Inputs**: If any required input is missing, halt protocol execution, escalate to source protocol owner, document gap in `.artifacts/protocol-11-ai-dataset-preparation-splitting/input-gaps.md`
- **Low Quality Inputs**: If input quality below threshold (e.g., feature completeness <0.98), request clarification from source protocol, document quality issues, proceed with documented assumptions
- **Invalid Inputs**: If inputs are invalid (e.g., corrupted Parquet files), request re-delivery from source protocol, halt until valid inputs received
- **Escalation Path**: For unresolved input issues, escalate to project manager, document escalation in `.artifacts/protocol-11-ai-dataset-preparation-splitting/escalation-log.md`

### Outputs To
- **Protocol 12**: Train/validation/test datasets for algorithm selection
  - **Artifact**: Train/validation/test datasets, split strategy, version metadata, leakage validation
  - **Format**: Parquet (datasets), JSON (metadata, strategy)
  - **Guarantees**: Datasets are split, validated, no leakage, properly versioned
- **Protocol 13**: Train/validation/test datasets for model training
  - **Artifact**: Train/validation/test datasets, split strategy, version metadata
  - **Format**: Parquet (datasets), JSON (metadata, strategy)
  - **Guarantees**: Datasets are split, validated, no leakage, properly versioned

### Data Formats
- **Input**: Parquet, JSON from Protocol 10
- **Output**: Parquet (datasets), JSON (metadata, strategy), Markdown (documentation)

### Storage Locations
- **Primary**: `.artifacts/protocol-11-ai-dataset-preparation-splitting/`
- **Datasets**: `.artifacts/protocol-11-ai-dataset-preparation-splitting/datasets/`
- **Version Control**: DVC/Git LFS repository

---

## QUALITY GATES

### Gate 1: Data Leakage Check (Prerequisite)

- **Criteria**: No data leakage detected between train/validation/test sets
- **Pass Threshold**: `leakage_detected = false` (boolean)
- **Metrics**: Leakage detection score (0.0-1.0), feature-target correlation analysis
- **Evidence Links**: `.artifacts/protocol-11/leakage-detection-report.json`, `.artifacts/protocol-11/leakage-prevention-validation.json`
- **Failure Handling**:
  - **Rollback**: Revert to feature engineering step, identify and remove leakage sources
  - **Notification**: Alert technical lead and stakeholders of leakage detection
  - **Waiver**: No waiver permitted for data leakage (blocking gate)

### Gate 2: Split Ratios Validated (Execution)

- **Criteria**: Train/validation/test split ratios match target ratios within ±2% tolerance
- **Pass Threshold**: `split_ratios_valid = true` (boolean)
- **Metrics**: Ratio deviation percentage, class distribution preservation (±2%)
- **Evidence Links**: `.artifacts/protocol-11/distribution-validation.json`, `.artifacts/protocol-11/stratification-results.json`
- **Failure Handling**:
  - **Rollback**: Re-execute splitting with adjusted parameters
  - **Notification**: Report ratio deviation to technical lead
  - **Waiver**: Waiver permitted if deviation <2% with technical lead approval

### Gate 3: Dataset Versioned (Completion)

- **Criteria**: All datasets versioned with complete audit trails and integrity checksums
- **Pass Threshold**: `dataset_versioned = true` (boolean)
- **Metrics**: Version control status, integrity checksum validation (100% match)
- **Evidence Links**: `.artifacts/protocol-11/version-metadata.json`, `.artifacts/protocol-11/integrity-validation.json`, `.artifacts/protocol-11/vc-logs/`
- **Failure Handling**:
  - **Rollback**: Reinitialize version control, re-add datasets
  - **Notification**: Alert DevOps team of versioning failure
  - **Waiver**: No waiver permitted for versioning failures (blocking gate)

### Gate 4: Splitting Strategy Validation (Completion)

- **Trigger**: After Step 1 (Split Strategy Definition)
- **Criteria**: Split strategy documented, ratios validated, stratification approach appropriate
- **Threshold**: split_strategy_documented = YES, ratios_valid = YES, stratification_appropriate = YES
- **Metrics**: Strategy completeness, ratio validation, stratification appropriateness
- **Evidence**: `split-strategy.md`, `stratification-analysis.json`, `split-rationale.md`
- **Validation Method**: Automated strategy validation and manual review
- **Pass Criteria**: Strategy complete, ratios valid, stratification appropriate
- **Action on Failure**: Document missing strategy elements, validate ratios, adjust stratification approach
- **Blocking**: NO - Warning only, proceed with documented assumptions

---

## COMMUNICATION PROTOCOLS

### Status Announcements

- `[PROTOCOL 11 | PHASE 3 START]` Dataset Preparation & Splitting initiated with split strategy definition
- `[SPLIT STRATEGY DEFINED]` Train/validation/test ratios: [RATIOS], stratification: [METHOD]
- `[LEAKAGE CHECK COMPLETE]` Zero data leakage detected, prevention mechanisms validated
- `[STRATIFICATION APPLIED]` Class distributions preserved across splits (±2% tolerance)
- `[DATASET VERSIONED]` Datasets v1.0.0 tagged and versioned with complete audit trails
- `[QUALITY GATE PASSED: Gate 1]` Data Leakage Check = false (zero leakage)
- `[QUALITY GATE PASSED: Gate 2]` Split Ratios Validated = true (within ±2%)
- `[QUALITY GATE PASSED: Gate 3]` Dataset Versioned = true (complete version control)
- `[PROTOCOL 11 | PHASE 3 COMPLETE]` Handoff to Protocol 12 (Model Training & Experimentation)

### User Interaction

- **Confirmation**: "Split strategy defined with ratios [RATIOS]. Proceed with leakage detection? Reply 'Go' to continue."
- **Clarification**: "Should I apply stratified splitting for this imbalanced classification task? Should I use time-series aware splitting for temporal data?"
- **Decision Points**: "Choose versioning method: DVC (recommended for >100MB) or Git LFS?"
- **Feedback Requests**: "Does the split strategy align with your model development requirements?"

### Error Messaging

- `[ERROR]` Data leakage detected in feature set (CRITICAL severity)
  - **Context**: Feature-target correlation analysis shows potential information leakage
  - **Resolution**: Review feature engineering transformations, remove leakage sources, re-run leakage detection

- `[ERROR]` Split ratios deviate >2% from target (HIGH severity)
  - **Context**: Actual ratios: [ACTUAL], Target ratios: [TARGET]
  - **Resolution**: Re-execute splitting with adjusted parameters, validate new ratios

- `[ERROR]` Dataset versioning failed (CRITICAL severity)
  - **Context**: Version control initialization error or integrity check failure
  - **Resolution**: Check storage permissions, reinitialize version control, re-add datasets

### Progress Tracking

- `[PROGRESS]` Split strategy definition - 25% complete
- `[PROGRESS]` Data leakage prevention - 50% complete
- `[PROGRESS]` Stratification and validation - 75% complete
- `[PROGRESS]` Dataset versioning - 90% complete
- `[NEXT]` Ready for Protocol 12 (Model Training & Experimentation) - Estimated 5-10 minutes

### Evidence Communication

- `[ARTIFACT]` Split strategy document saved to `.artifacts/protocol-11/split-strategy.md`
- `[ARTIFACT]` Leakage detection report saved to `.artifacts/protocol-11/leakage-detection-report.json`
- `[ARTIFACT]` Dataset version metadata saved to `.artifacts/protocol-11/version-metadata.json`
- **Format**: Markdown for documentation, JSON for metrics and analysis
- **Validation**: All artifacts validated against schema, checksums verified

---

## AUTOMATION HOOKS

### Scripts

```bash
# Split dataset with configurable ratios and stratification
python3 scripts/ai/split_dataset.py --input-data .artifacts/protocol-10/feature-engineered-data.parquet --train-ratio 0.70 --val-ratio 0.15 --test-ratio 0.15 --stratify-column target --output-dir .artifacts/protocol-11/datasets/ --version v1.0.0 > .artifacts/protocol-11/split-dataset.log 2>&1

# Check for data leakage between splits
python3 scripts/ai/check_data_leakage.py --train-data .artifacts/protocol-11/datasets/train.parquet --val-data .artifacts/protocol-11/datasets/validation.parquet --test-data .artifacts/protocol-11/datasets/test.parquet --target-column target --output-report .artifacts/protocol-11/leakage-detection-report.json > .artifacts/protocol-11/check-leakage.log 2>&1

# Version datasets using DVC or Git LFS
python3 scripts/ai/version_dataset.py --dataset-dir .artifacts/protocol-11/datasets/ --version-method dvc --version-tag v1.0.0 --output-metadata .artifacts/protocol-11/version-metadata.json > .artifacts/protocol-11/version-dataset.log 2>&1
```

### Registry Alignment

- **Script Registry**: `scripts/script-registry.json`
- **Registered Scripts**:
  - `split_dataset.py` - Dataset splitting with stratification support
  - `check_data_leakage.py` - Data leakage detection and validation
  - `version_dataset.py` - Dataset versioning with DVC/Git LFS

### Execution Context

- **CI/CD**: GitHub Actions workflow triggered on Protocol 11 execution
- **Environment**: Python 3.9+ with scikit-learn, pandas, numpy, DVC/Git LFS
- **Scheduling**: On-demand execution during model development phase
- **Permissions**: Read access to `.artifacts/protocol-10/`, write access to `.artifacts/protocol-11/`

### Command Syntax

- **Flags**: `--input-data`, `--train-ratio`, `--stratify-column`, `--version-method`
- **Output Redirection**: `> .artifacts/protocol-11/execution.log`
- **Parameterization**: `{version}`, `{split_ratios}`, `{stratification_method}`

### Error Handling

- **Exit Codes**: 0 = success, 1 = data leakage detected, 2 = split ratio validation failed, 3 = versioning error
- **Fallback**: Retry split with adjusted parameters, re-run leakage detection
- **Logging**: Execution logs saved to `.artifacts/protocol-11/execution.log`
- **Manual Paths**: If automation fails, manually execute split_dataset.py with verbose output

---

## HANDOFF CHECKLIST

### Prerequisites

- [ ] Feature-engineered datasets loaded from Protocol 10
- [ ] Feature schema documentation reviewed and validated
- [ ] Data quality metrics confirm feature engineering completeness (≥0.98)
- [ ] Split strategy approved by stakeholders and technical lead
- [ ] Version control system (DVC/Git LFS) configured and accessible
- [ ] Artifact storage directory `.artifacts/protocol-11/` created and writable

### Workflow

- [ ] Split strategy defined with ratios and stratification approach
- [ ] Data leakage detection executed with zero leakage confirmed
- [ ] Stratified splitting applied (if applicable) with distribution validation
- [ ] Train/validation/test datasets created and validated
- [ ] Datasets versioned with complete audit trails and checksums
- [ ] Version tags (v1.0.0) created with metadata

### Quality

- [ ] Gate 1 (Data Leakage Check): `leakage_detected = false` ✓
- [ ] Gate 2 (Split Ratios Validated): `split_ratios_valid = true` ✓
- [ ] Gate 3 (Dataset Versioned): `dataset_versioned = true` ✓
- [ ] All quality gates passed (3/3)

### Evidence

- [ ] Split strategy document saved to `.artifacts/protocol-11/split-strategy.md`
- [ ] Leakage detection report saved to `.artifacts/protocol-11/leakage-detection-report.json`
- [ ] Stratification results saved to `.artifacts/protocol-11/stratification-results.json`
- [ ] Distribution validation report saved to `.artifacts/protocol-11/distribution-validation.json`
- [ ] Version metadata saved to `.artifacts/protocol-11/version-metadata.json`
- [ ] Integrity validation report saved to `.artifacts/protocol-11/integrity-validation.json`

### Integration

- [ ] Train/validation/test datasets ready for Protocol 12 (Model Training)
- [ ] Version metadata accessible for reproducible model training
- [ ] Audit trails complete for compliance and governance
- [ ] Next protocol file referenced: `12-ai-model-training-experimentation.md`

### Automation

- [ ] `split_dataset.py` executed successfully
- [ ] `check_data_leakage.py` executed with zero leakage
- [ ] `version_dataset.py` executed with version tags created
- [ ] All automation scripts logged and evidence captured

### Verification Procedures

- [ ] Validate split ratios within ±2% of target (70/15/15 or 80/10/10)
- [ ] Confirm class distribution preserved across splits (±2% tolerance)
- [ ] Verify zero data leakage between train/validation/test sets
- [ ] Ensure all datasets versioned with checksums validated
- [ ] QA review: All artifacts generated, quality gates passed, handoff ready

### Stakeholder Sign-off

- [ ] **Reviewer**: Technical Lead - [APPROVAL_STATUS: approved/pending/rejected]
- [ ] **Evidence Package**: `.artifacts/protocol-11/` - [STATUS: complete]
- [ ] **Confirmation**: Stakeholder acknowledgment of split strategy and dataset readiness received

### Documentation Requirements

- [ ] Split strategy document saved to `.artifacts/protocol-11/split-strategy.md`
- [ ] Format: Markdown for documentation, JSON for metrics
- [ ] Reviewer documentation: Leakage detection report, distribution validation, version metadata
- [ ] Audit trail: Complete version control logs saved to `.artifacts/protocol-11/vc-logs/`

### Next Protocol Alignment

- [ ] **Ready for Protocol 12**: AI Algorithm Selection & Baseline Model
- [ ] **Next Command**: `@apply protocol-12-ai-algorithm-selection-baseline` or `run protocol-12`
- [ ] **Dependencies**: Train/validation/test datasets (`.artifacts/protocol-11/datasets/`), version metadata
- [ ] **Continuation Script**: `split_dataset.py` output feeds directly to Protocol 12 algorithm selection

### Learning Mechanisms

- [ ] **Feedback Loop**: Collect feedback from Protocol 12 on dataset quality and split effectiveness
- [ ] **Improvement Tracking**: Document any issues with splits and stratification for future iterations
- [ ] **Knowledge Base**: Capture lessons learned about optimal split ratios for different data types
- [ ] **Adaptation**: Adjust split strategy based on model performance feedback from Protocol 12

---

## EVIDENCE SUMMARY

| Artifact | Location | Evidence Type | Metrics |
|----------|----------|---------------|---------|
| Split Strategy Document | `.artifacts/protocol-11/split-strategy.md` | Documentation | Ratios: 70/15/15 or 80/10/10 |
| Stratification Analysis | `.artifacts/protocol-11/stratification-analysis.json` | Analysis Report | Class imbalance: [VALUE]% |
| Leakage Detection Report | `.artifacts/protocol-11/leakage-detection-report.json` | Validation Report | Leakage detected: false |
| Leakage Prevention Validation | `.artifacts/protocol-11/leakage-prevention-validation.json` | Validation Report | Prevention status: pass |
| Stratification Results | `.artifacts/protocol-11/stratification-results.json` | Results Report | Stratification method: [METHOD] |
| Distribution Validation | `.artifacts/protocol-11/distribution-validation.json` | Validation Report | Distribution preservation: ±2% |
| Version Metadata | `.artifacts/protocol-11/version-metadata.json` | Metadata | Version: v1.0.0, Timestamp: [TS] |
| Integrity Validation | `.artifacts/protocol-11/integrity-validation.json` | Validation Report | Checksum validation: 100% pass |
| Train Dataset | `.artifacts/protocol-11/datasets/train.parquet` | Dataset | Size: [MB], Rows: [N] |
| Validation Dataset | `.artifacts/protocol-11/datasets/validation.parquet` | Dataset | Size: [MB], Rows: [N] |
| Test Dataset | `.artifacts/protocol-11/datasets/test.parquet` | Dataset | Size: [MB], Rows: [N] |

### Storage Structure

- **Protocol Directory**: `.artifacts/protocol-11/` (main protocol artifacts)
- **Subdirectories**: `datasets/` (train/val/test files), `vc-logs/` (version control logs)
- **Permissions**: Read/write for AI workflow system, read-only for external audits
- **Naming Convention**: `{artifact-type}-{timestamp}.{extension}` (e.g., `split-strategy-20250114.md`)

### Manifest

- **Manifest File**: `.artifacts/protocol-11/manifest.json` (optional but recommended)
- **Metadata**: Timestamp (creation date), file sizes, SHA-256 checksums, split ratios, stratification method
- **Dependencies**: Input from Protocol 10 (feature engineering), output to Protocol 12 (model training)
- **Coverage**: 100% of datasets versioned with complete audit trails

### Traceability

- **Inputs From**: Protocol 10 (Feature-Engineered Datasets) → `.artifacts/protocol-10/feature-engineered-data.parquet`
- **Outputs To**: Protocol 12 (Model Training) → `.artifacts/protocol-11/datasets/train.parquet`, `validation.parquet`, `test.parquet`
- **Transformations**: Feature engineering output → split strategy → leakage detection → stratification → versioning
- **Audit Trail**: Complete version control logs in `.artifacts/protocol-11/vc-logs/` with timestamps and checksums

### Archival (Optional)

- **Compression**: ZIP archive for dataset backup (`.artifacts/protocol-11/datasets-backup-v1.0.0.zip`)
- **Retention**: 90 days (production datasets), 30 days (intermediate artifacts)
- **Retrieval**: Restore from version control using DVC/Git LFS checkout
- **Cleanup**: Archive old versions after 90 days, maintain current version indefinitely

### Drift Baselines and Monitoring Hooks
- **Split Distribution Baseline**: Document baseline class distributions for drift detection
  - Location: `.artifacts/protocol-11-ai-dataset-preparation-splitting/distribution-baseline.json`
  - Monitoring Hook: Compare future split distributions against baseline, alert if significant drift detected
  - Consumer: Protocol 23 (Model Drift Monitoring)
- **Leakage Baseline**: Document leakage detection results as baseline for future validation
  - Location: `.artifacts/protocol-11-ai-dataset-preparation-splitting/leakage-baseline.json`
  - Monitoring Hook: Validate no leakage introduced in future splits, alert if leakage detected
  - Consumer: Protocol 12, Protocol 13
- **Split Strategy Baseline**: Document split strategy and ratios for consistency tracking
  - Location: `.artifacts/protocol-11-ai-dataset-preparation-splitting/split-strategy-baseline.json`
  - Monitoring Hook: Track split strategy consistency over time, alert if strategy changes significantly
  - Consumer: Protocol 12, Protocol 13

---

## REASONING & REFLECTION

### Self-Awareness & Limitations

- **Awareness of Constraints**: This protocol assumes clean, feature-engineered data from Protocol 10; if data quality issues exist, they must be addressed before splitting
- **Awareness of Assumptions**: Assumes target variable is available for stratification; if not available, random splitting will be used instead
- **Awareness of Trade-offs**: Stratification improves generalization but increases computational overhead; balance based on dataset size and imbalance severity
- **Awareness of Scope**: This protocol focuses on dataset splitting; model-specific preprocessing (scaling, normalization) is handled in Protocol 12

### Decision Logic

- **Split Ratio Selection (70/15/15 vs 80/10/10)**: 70/15/15 preferred for smaller datasets (<10K samples), 80/10/10 for larger datasets (>100K samples) to maximize training data
- **Stratification Application**: Applied for classification tasks with class imbalance >10%, skipped for balanced datasets or regression tasks
- **Leakage Detection Priority**: Performed before splitting to catch issues early, prevents invalid model evaluation
- **Versioning Method (DVC vs Git LFS)**: DVC selected for datasets >100MB with complex pipelines, Git LFS for smaller datasets with simpler workflows

### Continuous Improvement

- **Lessons Learned**: 
  - Data leakage is the most critical issue to prevent early in the pipeline
  - Stratification significantly improves model generalization for imbalanced datasets
  - Version control enables reproducible model training and easy rollback

- **Optimization Opportunities**:
  - Implement automated leakage detection as part of feature engineering pipeline
  - Add time-series aware splitting for temporal datasets
  - Integrate with experiment tracking (MLflow) for dataset version linkage

- **Technical Debt**:
  - Manual leakage detection currently requires domain expertise; consider automated detection enhancement
  - Dataset versioning requires manual tagging; consider automated versioning based on feature engineering version
  - Split ratio validation currently manual; consider automated ratio validation in CI/CD pipeline

---

## READY FOR PROTOCOL 12

**Next Step**: `12-ai-algorithm-selection-baseline.md`

Train/validation/test datasets are prepared, versioned, and ready for algorithm selection and baseline model creation in Protocol 12.


---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 09: AI DATA PREPARATION & CLEANING (DATA-PROCESSING COMPLIANT)

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 09
- **Protocol Name:** AI AI DATA PREPARATION & CLEANING (DATA-PROCESSING COMPLIANT)
- **Protocol Owner:** Data Preparation Engineer
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-06
- **Last Updated**: 2025-01-06
- **Version**: 1.0

### Protocol Classification
- **Category**: Data Processing
- **Criticality**: High
- **Complexity**: High
- **Scope**: Module

### Protocol Lineage
- **Predecessor**: Protocol 08
- **Successor**: Protocol 10
- **Related Protocols**: Protocol 11, Protocol 12

### Protocol Metadata
- **Purpose**: Execute comprehensive data preparation and cleaning pipeline to create ML-ready datasets
- **Success Criteria**: All quality gates pass, data cleaning targets met, ML-readiness validated
- **Failure Modes**: Data quality issues, cleaning failures, feature engineering problems, compliance violations
- **Recovery Procedure**: Implement alternative cleaning methods, adjust quality thresholds, modify feature engineering approach

---

## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role**: Data Preparation Engineer
- **Responsibilities**:
  - Execute data preparation pipeline in sequence
  - Validate at each checkpoint
  - Escalate blockers immediately
  - Document cleaning decisions and transformations
- **Authority**: Can make decisions on cleaning methods and quality gates
- **Escalation**: Data Science Lead or ML Engineer

#### Protocol Owner
- **Role**: Data Preparation Engineer
- **Responsibilities**:
  - Approve pipeline execution
  - Review quality gates
  - Sign off on handoff
  - Address escalations
- **Authority**: Can make decisions on pipeline execution and quality gates

#### Downstream Owner
- **Role**: Protocol 10 Owner (Feature Engineering Specialist)
- **Responsibilities**:
  - Receive prepared dataset
  - Validate data quality and ML-readiness
  - Provide feedback on preparation quality
  - Confirm readiness for feature engineering
- **Authority**: Can request re-preparation or additional cleaning steps

### Role Interactions
- **Executor → Owner**: Real-time pipeline status, immediate cleaning issue notification
- **Owner → Downstream**: Dataset handoff with quality reports
- **Downstream → Executor**: Data quality feedback and feature engineering requirements

### Decision Authority Matrix
| Decision Type | Executor | Owner | Downstream | Executive |
|---------------|----------|-------|------------|-----------|
| Cleaning method selection | ✅ | ✅ | ❌ | ❌ |
| Quality threshold approval | ❌ | ✅ | ❌ | ❌ |
| Feature engineering scope | ✅ | ✅ | ✅ | ❌ |
| Compliance validation | ❌ | ✅ | ❌ | ✅ |

---

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT] All prerequisites must be met before protocol execution.**

### Required Artifacts
**[STRICT]** The following artifacts must exist and be validated:
- `collected-dataset/` from Protocol 08 (raw collected data)
- `collection-report.json` from Protocol 08 (collection quality report)
- `data-requirements.json` from Protocol 07 (data specifications)
- `labeling-strategy.md` from Protocol 07 (labeling requirements)

### Required Approvals
**[STRICT]** The following approvals must be obtained:
- Data collection completion approval from Protocol 08
- Data preparation strategy approval from data science team
- Compliance framework approval for data processing

### System State Requirements
**[STRICT]** System must meet the following conditions:
- Data preparation infrastructure deployed and accessible
- Automation scripts `clean_data.py`, `validate_cleaned_data.py`, `engineer_features.py`, and `ensure_ml_readiness.py` available
- Processing systems configured for data transformation
- Quality monitoring and validation systems operational

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

You are a **Data Preparation Engineer**. Your mission is to transform raw collected data into clean, ML-ready datasets through comprehensive cleaning, validation, and preparation processes while ensuring data quality, integrity, and compliance throughout the transformation pipeline.

**[CRITICAL] Do not proceed to feature engineering without confirming data preparation meets ML-readiness standards and quality targets.**

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1

**Action:** Execute data profiling and analysis activities

**Description:** Data analysis and quality issue identification phase

--

**Duration:** 2-4 hours

---

### STEP 2

**Action:** Execute data cleaning and transformation activities

**Description:** Data cleaning and transformation execution phase

--

**Duration:** 4-6 hours

---

### STEP 3

**Action:** Execute feature engineering and selection activities

**Description:** Feature creation and optimization phase

--

**Duration:** 3-5 hours

---

### STEP 4

**Action:** Execute data validation and quality assurance activities

**Description:** ML-readiness validation phase

--

**Duration:** 2-3 hours

---

### STEP 5

**Action:** Execute label preparation and validation activities

**Description:** Training labels preparation phase

--

**Duration:** 1-2 hours

---

### STEP 6

**Action:** Execute final validation and handoff activities

**Description:** Final validation and handoff preparation phase

--

**Duration:** 1-2 hours

---

## WORKFLOW EXECUTION DETAILS

### STEP 1: Data Profiling & Analysis
<!-- [Category: DATA-ANALYSIS] -->
<!-- Why: Understand data characteristics and identify cleaning requirements -->

1. **`[MUST]` Execute comprehensive data profiling:**
   * **Action**: Analyze structure, patterns, and quality of collected data
   * **Evidence**: Data profiling reports with detailed statistics
   * **Validation**: Profiling covers all data dimensions and features
   
   **Communication**: 
   > "[PROTOCOL 09 | STEP 1 START] - Profiling collected data and identifying cleaning requirements."
   
   **Halt condition**: Stop if critical data quality issues are discovered that require re-collection.

2. **`[MUST]` Identify data quality issues:**
   * **Action**: Detect and categorize all data quality problems
   * **Evidence**: Quality issue inventory with severity assessment
   * **Validation**: All quality issues identified and prioritized

3. **`[GUIDELINE]` Analyze data distributions:**
   * **Action**: Examine statistical distributions and outliers
   * **Evidence**: Distribution analysis with outlier detection
   * **Validation**: Distributions are understood and documented

4. **`[GUIDELINE]` Document data characteristics:**
   * **Action**: Create comprehensive data characteristics summary
   * **Evidence**: Data characteristics document with insights
   * **Validation**: Documentation covers all relevant data properties

### STEP 2: Data Cleaning & Transformation
<!-- [Category: DATA-CLEANING] -->
<!-- Why: Clean and transform data to meet quality standards -->

1. **`[MUST]` Execute data cleaning operations:**
   * **Action**: Apply cleaning procedures to address identified quality issues
   * **Evidence**: Cleaning logs with before/after metrics
   * **Validation**: Cleaning achieves target quality improvements
   
   **Communication**: 
   > "[PROTOCOL 09 | STEP 2] - Executing data cleaning and transformation operations."

2. **`[MUST]` Handle missing values and outliers:**
   * **Action**: Implement strategies for missing data and outlier treatment
   * **Evidence**: Treatment logs with methodology and results
   * **Validation**: Missing value and outlier treatments are appropriate

3. **`[MUST]` Standardize data formats and types:**
   * **Action**: Convert data to consistent formats and appropriate types
   * **Evidence**: Format standardization logs with validation
   * **Validation**: All data conforms to standardized formats

4. **`[GUIDELINE]` Optimize data structure:**
   * **Action**: Restructure data for optimal processing and analysis
   * **Evidence**: Structure optimization logs with performance metrics
   * **Validation**: Data structure supports efficient processing

### STEP 3: Feature Engineering & Selection
<!-- [Category: FEATURE-ENGINEERING] -->
<!-- Why: Create and select features that support ML objectives -->

1. **`[MUST]` Engineer new features:**
   * **Action**: Create new features based on domain knowledge and requirements
   * **Evidence**: Feature engineering logs with creation details
   * **Validation**: New features are relevant and properly constructed
   
   **Communication**: 
   > "[PROTOCOL 09 | STEP 3] - Engineering and selecting features for ML model development."

2. **`[MUST]` Transform existing features:**
   * **Action**: Apply transformations to improve feature distributions
   * **Evidence**: Transformation logs with before/after analysis
   * **Validation**: Transformations improve feature quality

3. **`[GUIDELINE]` Select optimal features:**
   * **Action**: Choose most relevant features for ML objectives
   * **Evidence**: Feature selection analysis with importance scores
   * **Validation**: Selected features provide optimal predictive power

4. **`[GUIDELINE]` Validate feature quality:**
   * **Action**: Assess feature quality and relevance
   * **Evidence**: Feature quality reports with validation metrics
   * **Validation**: All features meet quality standards

### STEP 4: Data Validation & Quality Assurance
<!-- [Category: QUALITY-VALIDATION] -->
<!-- Why: Ensure prepared data meets ML-readiness standards -->

1. **`[MUST]` Execute comprehensive data validation:**
   * **Action**: Run extensive validation on prepared dataset
   * **Evidence**: Validation reports with pass/fail status
   * **Validation**: All validation criteria are met
   
   **Communication**: 
   > "[PROTOCOL 09 | STEP 4] - Validating data quality and ML-readiness."

2. **`[MUST]` Verify statistical properties:**
   * **Action**: Confirm statistical properties meet ML requirements
   * **Evidence**: Statistical validation reports with analysis
   * **Validation**: Statistical properties are appropriate for ML

3. **`[GUIDELINE]` Test data consistency:**
   * **Action**: Verify internal consistency and logical relationships
   * **Evidence**: Consistency validation reports with issue tracking
   * **Validation**: Data is internally consistent and logical

4. **`[GUIDELINE]` Document quality improvements:**
   * **Action**: Track all quality improvements and their impact
   * **Evidence**: Quality improvement logs with metrics
   * **Validation**: Quality improvements are documented and measurable

### STEP 5: Label Preparation & Validation
<!-- [Category: LABEL-PREPARATION] -->
<!-- Why: Prepare and validate labels for supervised learning -->

1. **`[MUST]` Prepare training labels:**
   * **Action**: Create and format labels according to ML requirements
   * **Evidence**: Label preparation logs with format validation
   * **Validation**: Labels are properly formatted and aligned
   
   **Communication**: 
   > "[PROTOCOL 09 | STEP 5] - Preparing and validating training labels."

2. **`[MUST]` Validate label quality:**
   * **Action**: Assess label accuracy, consistency, and completeness
   * **Evidence**: Label quality reports with validation metrics
   * **Validation**: Labels meet quality standards for training

3. **`[GUIDELINE]` Balance label distributions:**
   * **Action**: Ensure balanced label distributions for training
   * **Evidence**: Label balance analysis with distribution metrics
   * **Validation**: Label distributions support effective training

4. **`[GUIDELINE]` Document label preparation:**
   * **Action**: Create comprehensive label preparation documentation
   * **Evidence**: Label preparation documentation with methodology
   * **Validation**: Documentation is complete and reproducible

### STEP 6: Final Validation & Handoff
<!-- [Category: VALIDATION-HANDOFF] -->
<!-- Why: Validate complete preparation and prepare for handoff -->

1. **`[MUST]` Execute final ML-readiness validation:**
   * **Action**: Run comprehensive validation of entire prepared dataset
   * **Evidence**: Final validation reports with readiness scores
   * **Validation**: Dataset meets all ML-readiness criteria
   
   **Communication**: 
   > "[PROTOCOL 09 | STEP 6] - Finalizing ML-readiness validation and preparing handoff."

2. **`[MUST]` Generate preparation documentation:**
   * **Action**: Create comprehensive documentation of preparation process
   * **Evidence**: Preparation documentation with process details
   * **Validation**: Documentation is complete and accurate

3. **`[GUIDELINE]` Prepare handoff package:**
   * **Action**: Assemble all prepared data and documentation for handoff
   * **Evidence**: Handoff package manifest with validation
   * **Validation**: Package contains all required components

4. **`[GUIDELINE]` Validate handoff readiness:**
   * **Action**: Confirm handoff package meets downstream requirements
   * **Evidence**: Handoff validation report with readiness status
   * **Validation**: Package ready for Protocol 10

**Output**: ML-ready dataset with engineered features and validated labels
   * **Action**: Create comprehensive documentation of all preparation steps
   * **Evidence**: Preparation documentation with process details
   * **Validation**: Documentation is complete and reproducible

3. **`[GUIDELINE]` Optimize dataset for training:**
   * **Action**: Final optimizations for efficient ML training
   * **Evidence**: Optimization logs with performance improvements
   * **Validation**: Optimizations improve training efficiency

4. **`[GUIDELINE]` Prepare handoff package:**
   * **Action**: Assemble prepared dataset and all documentation
   * **Evidence**: Handoff package manifest with validation
   * **Validation**: Package ready for Protocol 10

**Output**: Complete ML-ready dataset prepared for feature engineering

---

## 4. REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level retrospective and continuous improvement tracking -->

### Retrospective Guidance

After completing protocol execution (successful or halted), conduct retrospective:

**Timing**: Within 24-48 hours of completion

**Participants**: Protocol executor, data science team, ML engineers, downstream feature engineering team

**Agenda**:
1. **What went well**:
   - Which cleaning methods were most effective?
   - Which feature engineering approaches provided best results?
   - Which validation approaches caught issues early?

2. **What went poorly**:
   - Which data quality issues were difficult to resolve?
   - Which feature engineering attempts failed?
   - Which validation criteria were too strict or too lenient?

3. **Action items**:
   - Cleaning method improvements needed?
   - Feature engineering process enhancements?
   - Validation criteria adjustments?

**Output**: Retrospective report stored in protocol execution artifacts

### Continuous Improvement Opportunities

#### Identified Improvement Opportunities
- Enhance automated cleaning capabilities
- Improve feature engineering efficiency and effectiveness
- Streamline validation processes
- Optimize ML-readiness assessment accuracy

#### Process Optimization Tracking
- Track cleaning effectiveness across different data types
- Monitor feature engineering success rates
- Measure validation accuracy and efficiency
- Assess ML-readiness prediction vs actual model performance

#### Tracking Mechanisms and Metrics
- Monthly metrics dashboard with preparation KPIs
- Improvement tracking log with before/after comparisons
- Evidence of improvement validation through downstream model performance

---

## 5. INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### Inputs From:
**[STRICT]** The following inputs must be validated before execution:
- **Protocol 08**: `collected-dataset/`, `collection-report.json` - Raw data and quality reports.
- **Protocol 07**: `data-requirements.json`, `labeling-strategy.md` - Specifications and labeling requirements.

### Outputs To:
**[STRICT]** The following outputs must be generated for downstream protocols:
- **Protocol 10**: `prepared-dataset/`, `preparation-report.json` - ML-ready data for feature engineering.
- **Protocol 11**: `feature-catalog.json`, `data-quality-report.json` - Feature information for model development.

### Artifact Storage Locations:
**[STRICT]** All artifacts must be stored in standardized locations:
- `.artifacts/protocol-09/` - Primary evidence storage
- `data/prepared/` - Prepared ML-ready datasets
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->

### Gate 1: Data Cleaning Validation
**Type**: Prerequisite  
**Purpose**: Confirm data cleaning operations meet quality improvement targets.  
**Pass Criteria**:
- **Threshold**: Cleaning effectiveness score ≥ 0.9; quality improvement metric ≥ 80%.  
- **Boolean Check**: `cleaning-validation-report.json` field `status` equals `VALIDATED`.  
- **Metrics**: Report captures cleaning effectiveness metric, quality improvement metric, issue resolution metric.  
- **Evidence Link**: Validated against `.artifacts/protocol-09/cleaning-validation-report.json`.  
**Automation**:
- Script: `python3 scripts/ai/clean_data.py --input data/collected/ --output data/prepared/ --log .artifacts/protocol-09/cleaning-log.json`.  
- Script: `python3 scripts/validate_cleaning_results.py --data data/prepared/ --output .artifacts/protocol-09/cleaning-validation-report.json`.  
- CI Integration: `cleaning-validation.yml` invokes cleaning validation on completion; failures gate further processing.  
- Config: `config/protocol_gates/09.yaml` defines cleaning effectiveness thresholds and quality improvement targets.  
**Failure Handling**:
- **Rollback**: Re-execute cleaning with alternative methods, adjust cleaning parameters, implement additional cleaning steps.  
- **Notification**: Alert data science team and ML engineer via governance channel when cleaning validation fails.  
- **Waiver**: Waivers stored in `.artifacts/protocol-09/gate-waivers.json` with data science lead approval.

### Gate 2: Feature Engineering Quality
**Type**: Execution  
**Purpose**: Guarantee engineered features meet ML requirements and quality standards.  
**Pass Criteria**:
- **Threshold**: Feature quality score ≥ 0.85; feature relevance metric ≥ 0.8.  
- **Boolean Check**: `feature-engineering-report.json` fields `quality_score` ≥ 0.85 and `relevance_score` ≥ 0.8.  
- **Metrics**: `feature-engineering-report.json` captures quality metric, relevance metric, diversity metric.  
- **Evidence Link**: Validated against `.artifacts/protocol-09/feature-engineering-report.json`.  
**Automation**:
- Script: `python3 scripts/ai/engineer_features.py --data data/prepared/ --requirements data-requirements.json --output data/prepared/ --report .artifacts/protocol-09/feature-engineering-report.json`.  
- Script: `python3/scripts/validate_feature_quality.py --features data/prepared/ --report .artifacts/protocol-09/feature-validation.json`.  
- CI Integration: Feature validation runs after engineering with quality gate enforcement.  
- Config: `config/protocol_gates/09.yaml` stores feature quality thresholds and relevance requirements.  
**Failure Handling**:
- **Rollback**: Re-engineer features with alternative approaches, adjust feature selection criteria, improve transformation methods.  
- **Notification**: Notify ML engineer when feature quality does not meet requirements.  
- **Waiver**: Requires ML architect approval with justification for feature quality exceptions.

### Gate 3: Label Preparation Validation
**Type**: Execution  
**Purpose**: Ensure training labels are properly prepared and validated.  
**Pass Criteria**:
- **Threshold**: Label quality score ≥ 0.9; label alignment metric = 100%.  
- **Boolean Check**: `label-preparation-report.json` fields `quality_score` ≥ 0.9 and `alignment_verified` equals `true`.  
- **Metrics**: `label-preparation-report.json` captures quality metric, alignment metric, balance metric.  
- **Evidence Link**: Evidence validated against `.artifacts/protocol-09/label-preparation-report.json`.  
**Automation**:
- Script: `python3 scripts/ai/prepare_labels.py --data data/prepared/ --strategy labeling-strategy.md --output data/prepared/ --report .artifacts/protocol-09/label-preparation-report.json`.  
- Script: `python3/scripts/validate_label_quality.py --labels data/prepared/ --report .artifacts/protocol-09/label-validation.json`.  
- CI Integration: Label validation runs after preparation with quality and alignment checks.  
- Config: `config/protocol_gates/09.yaml` defines label quality thresholds and alignment requirements.  
**Failure Handling**:
- **Rollback**: Re-prepare labels with corrected methodology, improve label quality processes, address alignment issues.  
- **Notification**: Alert data science team when label preparation validation fails.  
- **Waiver**: Requires ML engineer approval with documented impact assessment.

### Gate 4: ML-Readiness Validation
**Type**: Completion  
**Purpose**: Validate that prepared dataset is ready for ML model development.  
**Pass Criteria**:
- **Threshold**: ML-readiness score ≥ 0.9; dataset completeness = 100%.  
- **Boolean Check**: `ml-readiness-report.json` fields `ready_for_ml` equals `true` and `all_criteria_met` equals `true`.  
- **Metrics**: `ml-readiness-report.json` documents readiness metric, completeness metric, quality metric.  
- **Evidence Link**: Validated against `.artifacts/protocol-09/ml-readiness-report.json`.  
**Automation**:
- Script: `python3 scripts/ai/ensure_ml_readiness.py --data data/prepared/ --output .artifacts/protocol-09/ml-readiness-report.json`.  
- Script: `python3/scripts/aggregate_evidence_09.py --output .artifacts/protocol-09/ --protocol-id 09`.  
- CI Integration: `script-registry-enforcement.yml` confirms aggregator registered and executed before handoff.  
- Config: `config/protocol_gates/09.yaml` defines ML-readiness thresholds and completeness requirements.  
**Failure Handling**:
- **Rollback**: Address identified readiness issues, complete missing preparation steps, re-run validation checks.  
- **Notification**: Inform Protocol 10 owner of handoff delay and share readiness status.  
- **Waiver**: Requires ML architect approval with documented readiness exceptions.

### Compliance Integration
- **Industry Standards**: Data preparation best practices, feature engineering standards, ML data quality frameworks, data processing compliance standards.  
- **Security Requirements**: Secure data processing environments, encrypted intermediate data, access controls for sensitive data processing, audit trails for all transformations.  
- **Regulatory Compliance**: GDPR data processing principles, data minimization during processing, privacy-preserving feature engineering.  
- **Governance**: Gate thresholds governed via `config/protocol_gates/09.yaml`; automation telemetry captured in `.artifacts/validation/protocol_quality_gates-summary.json` and data science governance dashboards.

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### Status Announcements:
**[STRICT]** Use standardized announcements for phase transitions:
```
[PROTOCOL 09 | PHASE 1 START] - "Profiling collected data and identifying cleaning requirements."
[PROTOCOL 09 | PHASE 2 START] - "Executing data cleaning and transformation operations."
[PROTOCOL 09 | PHASE 3 START] - "Engineering and selecting features for ML model development."
[PROTOCOL 09 | PHASE 4 START] - "Validating data quality and ML-readiness."
[PROTOCOL 09 | PHASE 5 START] - "Preparing and validating training labels."
[PROTOCOL 09 | PHASE 6 START] - "Finalizing ML-readiness validation and preparing handoff."
[PHASE COMPLETE] - "Data preparation completed, validated, and ready for feature engineering."
[RAY ERROR] - "Issue encountered during [phase]; see preparation-issues.md for details."
```

### Validation Prompts:
**[STRICT]** Use standardized prompts for validation requests:
```
[RAY CONFIRMATION REQUIRED]
> "Data preparation completed and validated. Evidence available:
> - cleaning-validation-report.json
> - feature-engineering-report.json
> - label-preparation-report.json
> - ml-readiness-report.json
>
> Confirm readiness to trigger Protocol 10: Feature Engineering & Selection."
```

### Error Handling:
**[STRICT]** Use standardized error messages for gate failures:
```
[RAY GATE FAILED: Data Cleaning Validation]
> "Quality gate 'Data Cleaning Validation' failed.
> Criteria: Cleaning effectiveness score must be ≥ 0.9.
> Actual: Cleaning effectiveness score = 0.75.
> Required action: Re-execute cleaning with alternative methods or adjust parameters.
>
> Options:
> 1. Address cleaning issues and retry validation
> 2. Request gate waiver with cleaning justification
> 3. Halt protocol execution and reconsider cleaning approach"
```

---

## 8. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference**: See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### Validation Scripts:

1. **`[MUST]` Run data cleaning:**
   * **Action**: Execute script to clean and transform data
   * **Evidence**: Cleaning logs with before/after metrics
   * **Validation**: Cleaning effectiveness score ≥ 0.9
   
   ```bash
   # Data cleaning execution
   python scripts/ai/clean_data.py \
     --input data/collected/ \
     --output data/prepared/ \
     --log .artifacts/protocol-09/cleaning-log.json
   ```

2. **`[MUST]` Run feature engineering:**
   * **Action**: Execute script to engineer and select features
   * **Evidence**: Feature engineering logs with quality metrics
   * **Validation**: Feature quality score ≥ 0.85
   
   ```bash
   # Feature engineering execution
   python scripts/ai/engineer_features.py \
     --data data/prepared/ \
     --requirements data-requirements.json \
     --output data/prepared/ \
     --report .artifacts/protocol-09/feature-engineering-report.json
   ```

3. **`[MUST]` Run label preparation:**
   * **Action**: Execute script to prepare training labels
   * **Evidence**: Label preparation logs with quality metrics
   * **Validation**: Label quality score ≥ 0.9
   
   ```bash
   # Label preparation execution
   python scripts/ai/prepare_labels.py \
     --data data/prepared/ \
     --strategy labeling-strategy.md \
     --output data/prepared/ \
     --report .artifacts/protocol-09/label-preparation-report.json
   ```

4. **`[MUST]` Run ML-readiness validation:**
   * **Action**: Execute script to validate ML-readiness
   * **Evidence**: `.artifacts/protocol-09/ml-readiness-report.json`
   * **Validation**: ML-readiness score ≥ 0.9
   
   ```bash
   # ML-readiness validation
   python scripts/ai/ensure_ml_readiness.py \
     --data data/prepared/ \
     --output .artifacts/protocol-09/ml-readiness-report.json
   ```

5. **`[MUST]` Aggregate evidence:**
   * **Action**: Execute script to collect all evidence
   * **Evidence**: Evidence manifest in `.artifacts/protocol-09/`
   * **Validation**: All artifacts included in manifest
   
   ```bash
   # Evidence aggregation
   python scripts/aggregate_evidence_09.py \
     --output .artifacts/protocol-09/ \
     --protocol-id 09
   ```

### CI/CD Integration:
```yaml
name: Protocol 09 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 09 Gates
        run: python scripts/run_protocol_09_gates.py
```

### Manual Fallbacks:

**When automation is unavailable**:

1. **Manual Data Cleaning**:
   - Review data quality issues manually
   - Apply cleaning operations step by step
   - Document cleaning results and improvements

2. **Manual Feature Engineering**:
   - Create features based on domain knowledge
   - Validate feature quality manually
   - Document feature engineering decisions

3. **Manual Quality Gate Validation**:
   - Review each gate criteria manually
   - Document validation results
   - Create manual validation report

---

## 9. HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple checklist execution for protocol completion -->

### Pre-Execution Validation:

1. **`[GUIDELINE]` Validate prerequisites**:
   * **Action**: Verify all required artifacts and approvals are present
   * **Evidence**: Prerequisite validation report
   * **Validation**: All prerequisites marked complete
   
   **Checklist**:
   - [ ] Collected dataset available and validated
   - [ ] Collection quality report reviewed
   - [ ] Data requirements documented
   - [ ] Labeling strategy approved
   - [ ] Preparation infrastructure deployed

### Execution Validation:

1. **`[GUIDELINE]` Validate workflow completion**:
   * **Action**: Verify all phases completed successfully
   * **Evidence**: Phase completion log
   * **Validation**: All phases marked complete
   
   **Checklist**:
   - [ ] Data profiling and analysis completed
   - [ ] Data cleaning and transformation executed
   - [ ] Feature engineering and selection completed
   - [ ] Data validation and quality assurance passed
   - [ ] Label preparation and validation completed
   - [ ] Final ML-readiness validation completed

### Post-Execution Validation:

1. **`[GUIDELINE]` Validate quality gates**:
   * **Action**: Verify all quality gates passed
   * **Evidence**: Quality gate validation report
   * **Validation**: All gates marked pass
   
   **Checklist**:
   - [ ] Data cleaning validation passed
   - [ ] Feature engineering quality passed
   - [ ] Label preparation validation passed
   - [ ] ML-readiness validation passed

### Handoff to Protocol 10:

1. **`[MUST]` Execute protocol handoff**:
   * **Action**: Package evidence and trigger Protocol 10
   * **Evidence**: Handoff confirmation in execution log
   * **Validation**: Protocol 10 acknowledges receipt
   
   **Handoff Package**:
   - Prepared ML-ready dataset with features
   - Data cleaning and transformation logs
   - Feature engineering documentation
   - Label preparation and validation reports
   - ML-readiness validation evidence
   - Data quality and preparation documentation
   - Evidence manifest and checksums

   **[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 10: Feature Engineering & Selection

---

## 10. REASONING & REFLECTION

### Decision Logic

#### Why Cleaning Effectiveness Score ≥ 0.9 Threshold?
The 0.9 threshold balances:
- **ML Performance**: Ensures data quality supports effective model training
- **Processing Efficiency**: Allows for reasonable imperfections while maintaining high standards
- **Cost Control**: Prevents excessive cleaning costs and timeline delays
- **Feature Quality**: High-quality data enables better feature engineering

#### Feature Engineering Quality Standards
Feature quality validation is critical because:
- **Model Performance**: Feature quality directly impacts ML model effectiveness
- **Training Efficiency**: Well-engineered features reduce training time and resource requirements
- **Interpretability**: Quality features improve model interpretability and explainability
- **Generalization**: Properly engineered features enhance model generalization capabilities

#### ML-Readiness Validation Requirements
Comprehensive ML-readiness validation ensures:
- **Model Development Success**: Prepared data supports effective ML model development
- **Reproducibility**: Preparation process is documented and reproducible
- **Quality Assurance**: All quality issues are identified and addressed before modeling
- **Downstream Efficiency**: Reduces rework and delays in subsequent protocols

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Persistent data quality issues | Implement advanced cleaning techniques, consider data re-collection, adjust quality thresholds |
| Feature engineering failures | Re-evaluate feature requirements, try alternative engineering approaches, consult domain experts |
| Label preparation problems | Improve labeling methodology, enhance label validation, address alignment issues |
| ML-readiness validation failures | Address identified gaps, complete missing preparation steps, re-validate with adjusted criteria |
| Processing performance bottlenecks | Optimize data processing pipelines, scale computing resources, implement parallel processing |

### Continuous Improvement

#### Feedback Collection
- Data cleaning effectiveness across different data types
- Feature engineering success rates and model performance impact
- Label preparation quality and training effectiveness
- ML-readiness validation accuracy vs actual model development success

#### Metrics Tracked
- Data quality improvement metrics and cleaning efficiency
- Feature quality scores and model performance correlation
- Label quality metrics and training accuracy relationships
- ML-readiness scores vs downstream model development success rates

#### Update Frequency
- Monthly review of data preparation effectiveness
- Quarterly update of feature engineering techniques
- Continuous improvement based on model development feedback
- Immediate updates for critical quality issues

### Lessons Learned
*[This section will be populated after protocol execution]*

- Lesson 1: [Date] - [Description]
- Lesson 2: [Date] - [Description]
- Lesson 3: [Date] - [Description]

### Best Practices Discovered
*[To be documented during implementation]*

1. Always profile data thoroughly before cleaning operations
2. Implement automated quality monitoring throughout preparation process
3. Document all cleaning decisions and transformations for reproducibility
4. Validate feature quality with multiple metrics and domain expertise
5. Maintain comprehensive audit trails for all data preparation activities

---

**Protocol 09: AI Data Preparation & Cleaning**  
**Version**: 1.0  
**Last Updated**: 2025-01-06  
**Next Review**: After 5 executions or quarterly  
**Status**: Ready for Validation

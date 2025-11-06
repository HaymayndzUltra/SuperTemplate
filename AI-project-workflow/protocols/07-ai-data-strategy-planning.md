---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 07: AI DATA STRATEGY & REQUIREMENTS PLANNING (DATA-PLANNING COMPLIANT)

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 07
- **Protocol Name:** AI AI DATA STRATEGY & REQUIREMENTS PLANNING (DATA-PLANNING COMPLIANT)
- **Protocol Owner:** Data Strategist
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-06
- **Last Updated:** 2025-01-06
- **Version:** 1.0

### Protocol Classification
- **Category:** Data Planning
- **Criticality:** High
- **Complexity:** High
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** Protocol 06
- **Successor:** Protocol 08
- **Related Protocols:** Protocol 09, Protocol 10

### Protocol Metadata
- **Purpose:** Create comprehensive data strategy and requirements for AI implementation
- **Success Criteria:** All quality gates pass, data availability confirmed, compliance requirements documented
- **Failure Modes:** Insufficient data, non-compliant data sources, unsustainable data acquisition costs
- **Recovery Procedure:** Modify data requirements, implement data augmentation, or redesign approach

---

## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** Data Strategist
- **Responsibilities:**
  - Execute protocol steps in sequence
  - Validate at each checkpoint
  - Escalate blockers immediately
  - Document decisions and rationale
- **Authority:** Can make decisions on protocol execution and quality gates
- **Escalation:** Data Engineering Lead or AI Architect

#### Protocol Owner
- **Role:** Data Strategist
- **Responsibilities:**
  - Approve protocol execution
  - Review quality gates
  - Sign off on handoff
  - Address escalations
- **Authority:** Can make decisions on protocol execution and quality gates

#### Downstream Owner
- **Role:** Protocol 08 Owner (Data Collection Specialist)
- **Responsibilities:**
  - Receive handoff package
  - Validate inputs from this protocol
  - Provide feedback on quality
  - Confirm readiness for next phase
- **Authority:** Can request clarification or additional data requirements

### Role Interactions
- **Executor → Owner:** Daily status updates, immediate blocker notification
- **Owner → Downstream:** Handoff package with validation evidence
- **Downstream → Executor:** Feedback on data requirements feasibility

### Decision Authority Matrix
| Decision Type | Executor | Owner | Downstream | Executive |
|---------------|----------|-------|------------|-----------|
| Data source selection | ✅ | ✅ | ❌ | ❌ |
| Compliance requirements approval | ❌ | ✅ | ❌ | ✅ |
| Labeling strategy approval | ✅ | ✅ | ❌ | ❌ |
| Data infrastructure decisions | ❌ | ✅ | ✅ | ❌ |

---

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT] All prerequisites must be met before protocol execution.**

### Required Artifacts
**[STRICT]** The following artifacts must exist and be validated:
- `AI-USE-CASE-DEFINITION.md` from Protocol 06 (validated AI use case)
- `feasibility-report.json` from Protocol 06 (feasibility assessment)
- `success-metrics.json` from Protocol 06 (success criteria)
- `stakeholder-approval-record.json` from Protocol 06 (approval evidence)

### Required Approvals
**[STRICT]** The following approvals must be obtained:
- AI use case approval from Protocol 06 stakeholders
- Data access permissions for source systems evaluation

### System State Requirements
**[STRICT]** System must meet the following conditions:
- Access to data strategy templates under `.templates/data/`
- Automation scripts `assess_data_availability.py`, `validate_data_requirements.py`, `check_compliance_requirements.py`, and `calculate_labeling_costs.py` available
- Data assessment tools and compliance frameworks accessible

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

You are a **Data Strategist**. Your mission is to create a comprehensive data strategy that ensures sufficient, high-quality, compliant data for AI model development while optimizing costs and timelines.

**[CRITICAL] Do not proceed to data collection without confirming data availability meets requirements and compliance is validated.**

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1

**Action:** Execute data availability assessment activities

**Description:** Data availability and accessibility evaluation phase

**Input:** Use case requirements and data needs from Protocol 06

**Output:** Data inventory with accessibility assessment and gap analysis

**Communication:** Document data source availability, access methods, and identified gaps

**Evidence:** Store data inventory, accessibility reports, and gap analysis in `.artifacts/protocol-07/data-availability/`

**Duration:** 3-4 hours

---

### STEP 2

**Action:** Execute data volume and quality requirements activities

**Description:** Data volume planning and quality standards definition phase

**Input:** Data inventory and ML requirements from previous steps

**Output:** Data volume specifications and quality requirements framework

**Communication:** Report volume requirements, quality standards, and acquisition timelines

**Evidence:** Store volume calculations, quality specifications, and requirement documents in `.artifacts/protocol-07/data-requirements/`

**Duration:** 2-3 hours

---

### STEP 3

**Action:** Execute privacy and compliance planning activities

**Description:** Privacy requirements and compliance framework definition phase

**Input:** Data inventory and regulatory requirements

**Output:** Compliance framework with privacy controls and audit requirements

**Communication:** Document compliance requirements, privacy controls, and audit procedures

**Evidence:** Store compliance framework, privacy controls, and audit procedures in `.artifacts/protocol-07/compliance-planning/`

**Duration:** 2-3 hours

---

### STEP 4

**Action:** Execute data labeling strategy activities

**Description:** Labeling requirements and strategy development phase

**Input:** ML requirements and compliance framework

**Output:** Comprehensive labeling strategy with cost estimates

**Communication:** Provide labeling approach, resource requirements, and timeline

**Evidence:** Store labeling strategy, cost analysis, and resource plans in `.artifacts/protocol-07/labeling-strategy/`

**Duration:** 2-3 hours

---

### STEP 5

**Action:** Execute feature engineering requirements activities

**Description:** Feature requirements and engineering planning phase

**Input:** ML objectives and data characteristics analysis

**Output:** Feature engineering requirements and implementation plan

**Communication:** Document feature requirements, engineering approach, and validation methods

**Evidence:** Store feature specifications, engineering plans, and validation frameworks in `.artifacts/protocol-07/feature-engineering/`

**Duration:** 2-3 hours

---

### STEP 6

**Action:** Execute data storage strategy activities

**Description:** Storage architecture and management strategy phase

**Input:** All data requirements and engineering specifications

**Output:** Complete data strategy with storage architecture ready for Protocol 08

**Communication:** Provide final data strategy summary and implementation roadmap

**Evidence:** Store complete data strategy, storage architecture, and handoff package in `.artifacts/protocol-07/handoff/`

**Duration:** 2-3 hours

---

## WORKFLOW EXECUTION DETAILS

### STEP 1: Data Availability Assessment
<!-- [Category: DATA-ANALYSIS] -->
<!-- Why: Data availability determines project feasibility -->

1. **`[MUST]` Inventory existing data sources:**
   * **Action:** Catalog all available data sources and their characteristics
   * **Evidence:** Data source inventory with accessibility status
   * **Validation:** All potential sources identified and documented
   
   **Communication:** 
   > "[PROTOCOL 07 | STEP 1 START] - Assessing data availability across all sources."
   
   **Source Types:**
   - Internal databases and data warehouses
   - External data providers
   - Third-party APIs and feeds
   - Historical archives and logs
   - Real-time data streams

2. **`[MUST]` Assess data accessibility:**
   * **Action:** Evaluate access permissions and technical feasibility
   * **Evidence:** Accessibility assessment with access methods
   * **Validation:** At least 90% of required data is accessible
   
   **Halt condition:** Stop if critical data sources are inaccessible.

3. **`[GUIDELINE]` Evaluate data volume and velocity:**
   * **Action:** Assess current volume and growth projections
   * **Evidence:** Volume analysis with growth forecasts
   * **Validation:** Volume meets ML model requirements

4. **`[GUIDELINE]` Analyze data variety and structure:**
   * **Action:** Document data formats and structural characteristics
   * **Evidence:** Data variety analysis with format mapping
   * **Validation:** Data formats are compatible with ML pipelines

**Decision Point**: 
- If data availability ≥ 90% of requirements → Continue to STEP 2
- If data availability < 90% → Create data acquisition plan before proceeding

### STEP 2: Data Volume & Quality Requirements
<!-- [Category: QUALITY-DEFINITION] -->
<!-- Why: Define data standards to ensure ML model success -->

1. **`[MUST]` Calculate minimum data requirements:**
   * **Action:** Determine data volume needed for model training
   * **Evidence:** Data volume calculation with statistical justification
   * **Validation:** Requirements are sufficient for model performance
   
   **Communication:** 
   > "[PROTOCOL 07 | STEP 2] - Defining data volume and quality requirements."

2. **`[MUST]` Define data quality criteria:**
   * **Action:** Establish quality thresholds for all data dimensions
   * **Evidence:** Quality criteria document with thresholds
   * **Validation:** Thresholds are realistic and measurable
   
   **Quality Dimensions:**
   - **Completeness**: Missing value thresholds (< 5% acceptable)
   - **Accuracy**: Error rate limits (< 1% for critical fields)
   - **Consistency**: Cross-source validation rules
   - **Timeliness**: Data freshness requirements
   - **Validity**: Format and range constraints

3. **`[GUIDELINE]` Establish data quality monitoring:**
   * **Action:** Design ongoing quality monitoring framework
   * **Evidence:** Monitoring plan with alert thresholds
   * **Validation**: Monitoring covers all quality dimensions

4. **`[GUIDELINE]` Create data profiling plan:**
   * **Action:** Plan statistical analysis and monitoring setup
   * **Evidence:** Profiling methodology with tools
   * **Validation**: Plan addresses all data quality risks

### STEP 3: Privacy & Compliance Planning
<!-- [Category: COMPLIANCE-PLANNING] -->
<!-- Why: Ensure regulatory compliance and data privacy -->

1. **`[MUST]` Identify applicable regulations:**
   * **Action:** Determine which regulations apply to data handling
   * **Evidence:** Compliance matrix with applicable regulations
   * **Validation:** All relevant jurisdictions and regulations identified
   
   **Communication:** 
   > "[PROTOCOL 07 | STEP 3] - Planning privacy and compliance requirements."
   
   **Regulations to Consider:**
   - **GDPR** (EU data subjects)
   - **HIPAA** (healthcare data)
   - **CCPA/CPRA** (California consumers)
   - **SOX** (financial data)
   - **PCI-DSS** (payment data)
   - Industry-specific compliance requirements

2. **`[MUST]` Assess compliance gaps:**
   * **Action:** Evaluate current data handling against regulations
   * **Evidence:** Compliance gap analysis with remediation plans
   * **Validation:** All critical gaps identified with mitigation strategies

3. **`[GUIDELINE]` Design compliance framework:**
   * **Action:** Create governance framework for data compliance
   * **Evidence:** Compliance framework document with controls
   * **Validation**: Framework addresses all identified requirements

4. **`[GUIDELINE]` Document compliance procedures:**
   * **Action:** Create standard operating procedures for compliance
   * **Evidence:** SOP documentation with training materials
   * **Validation**: Procedures are actionable and comprehensive

### STEP 4: Data Labeling Strategy
<!-- [Category: LABELING-PLANNING] -->
<!-- Why: Ensure sufficient labeled data for supervised learning -->

1. **`[MUST]` Assess labeling requirements:**
   * **Action:** Determine volume and complexity of labeling needed
   * **Evidence:** Labeling requirements analysis with estimates
   * **Validation:** Requirements align with model training needs
   
   **Communication:** 
   > "[PROTOCOL 07 | STEP 4] - Developing data labeling strategy and cost analysis."

2. **`[MUST]` Evaluate labeling approaches:**
   * **Action:** Compare different labeling methods and costs
   * **Evidence:** Labeling approach comparison with recommendations
   * **Validation:** Selected approach is cost-effective and scalable

3. **`[GUIDELINE]` Calculate labeling costs and timeline:**
   * **Action:** Estimate costs and duration for labeling activities
   * **Evidence:** Cost analysis with timeline projections
   * **Validation**: Estimates are realistic and within budget

4. **`[GUIDELINE]` Plan quality assurance for labeling:**
   * **Action:** Design QA process for label validation
   * **Evidence:** QA plan with validation procedures
   * **Validation**: QA process ensures label accuracy targets

### STEP 5: Feature Engineering Requirements
<!-- [Category: FEATURE-PLANNING] -->
<!-- Why: Define feature creation and transformation needs -->

1. **`[MUST]` Identify required features:**
   * **Action:** Determine features needed for model performance
   * **Evidence:** Feature requirements document with specifications
   * **Validation:** Features align with model objectives
   
   **Communication:** 
   > "[PROTOCOL 07 | STEP 5] - Defining feature engineering requirements."

2. **`[MUST]` Plan feature creation pipeline:**
   * **Action:** Design pipeline for feature generation and transformation
   * **Evidence:** Feature pipeline architecture with tools
   * **Validation:** Pipeline is scalable and maintainable

3. **`[GUIDELINE]` Define feature validation:**
   * **Action:** Establish validation rules for feature quality
   * **Evidence:** Feature validation criteria with tests
   * **Validation**: Validation covers all critical feature dimensions

4. **`[GUIDELINE]` Document feature governance:**
   * **Action:** Create governance framework for feature management
   * **Evidence:** Feature governance procedures with roles
   * **Validation**: Governance ensures feature consistency and quality

### STEP 6: Data Storage Strategy
<!-- [Category: STORAGE-PLANNING] -->
<!-- Why: Ensure appropriate data storage and access patterns -->

1. **`[MUST]` Design storage architecture:**
   * **Action:** Create storage solution for data lifecycle needs
   * **Evidence:** Storage architecture with capacity planning
   * **Validation:** Architecture meets performance and cost requirements
   
   **Communication:** 
   > "[PROTOCOL 07 | STEP 6] - Designing data storage and access strategy."

2. **`[MUST]` Plan data access patterns:**
   * **Action:** Define access methods and security controls
   * **Evidence:** Access patterns with security documentation
   * **Validation:** Access is secure and efficient for all use cases

3. **`[GUIDELINE]` Establish backup and recovery:**
   * **Action:** Create backup strategy with disaster recovery
   * **Evidence:** Backup procedures with RTO/RPO targets
   * **Validation**: Backup strategy meets business continuity requirements

4. **`[GUIDELINE]` Document retention policies:**
   * **Action:** Define data retention and deletion procedures
   * **Evidence:** Retention policy with compliance alignment
   * **Validation**: Policies comply with all applicable regulations

**Output**: Complete data strategy package ready for data collection implementation

---

## 4. REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level retrospective and continuous improvement tracking -->

### Retrospective Guidance

After completing protocol execution (successful or halted), conduct retrospective:

**Timing:** Within 24-48 hours of completion

**Participants:** Protocol executor, data engineering team, compliance officers, stakeholders

**Agenda:**
1. **What went well:**
   - Which data availability assessments were most accurate?
   - Which compliance planning approaches prevented issues?
   - Which labeling strategies provided best cost-quality balance?

2. **What went poorly:**
   - Which data source evaluations missed critical issues?
   - Which compliance requirements were underestimated?
   - Which cost estimates were inaccurate for labeling or storage?

3. **Action items:**
   - Data assessment template updates needed?
   - Compliance planning process improvements?
   - Cost estimation model refinements?

**Output:** Retrospective report stored in protocol execution artifacts

### Continuous Improvement Opportunities

#### Identified Improvement Opportunities
- Enhance data availability prediction accuracy
- Streamline compliance assessment processes
- Improve cost estimation for labeling activities
- Optimize storage architecture recommendations

#### Process Optimization Tracking
- Track data availability prediction vs actual access
- Monitor compliance issue detection rates
- Measure labeling cost estimation accuracy
- Assess storage architecture performance vs projections

#### Tracking Mechanisms and Metrics
- Monthly metrics dashboard with data strategy KPIs
- Improvement tracking log with before/after comparisons
- Evidence of improvement validation through project outcomes

---

## 5. INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### Inputs From:
**[STRICT]** The following inputs must be validated before execution:
- **Protocol 06**: `AI-USE USE-CASE-DEFINITION.md`, `feasibility-report.json` - Use case requirements and feasibility.
- **Protocol 06**: `success-metrics.json`, `stakeholder-approval-record.json` - Success criteria and approval evidence.

### Outputs To:
**[STRICT]** The following outputs must be generated for downstream protocols:
- **Protocol 08**: `data-strategy.md`, `data-requirements.json` - Data collection specifications.
- **Protocol 09**: `labeling-strategy.md`, `compliance-framework.md` - Data preparation inputs.

### Artifact Storage Locations:
**[STRICT]** All artifacts must be stored in standardized locations:
- `.artifacts/protocol-07/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->

### Gate 1: Data Availability Validation
**Type:** Prerequisite  
**Purpose:** Confirm data sources meet volume and accessibility requirements.  
**Pass Criteria:**
- **Threshold:** Data availability score ≥ 0.9; accessibility metric = 100%.  
- **Boolean Check:** `data-availability-report.json` field `status` equals `VALIDATED`.  
- **Metrics:** Report captures availability metric, accessibility metric, volume metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-07/data-availability-report.json`.  
**Automation:**
- Script: `python3 scripts/ai/assess_data_availability.py --input data-sources.json --output .artifacts/protocol-07/data-availability-report.json`.  
- Script: `python3 scripts/validate_data_availability_07.py --log .artifacts/protocol-07/availability-log.json`.  
- CI Integration: `data-validation-pipeline.yml` invokes availability assessment on push; failures gate pull requests.  
- Config: `config/protocol_gates/07.yaml` defines availability thresholds and accessibility requirements.  
**Failure Handling:**
- **Rollback:** Identify alternative data sources, implement data acquisition strategy, reassess requirements.  
- **Notification:** Alert Protocol 06 owner and data architect via governance channel when availability score drops below threshold.  
- **Waiver:** Waivers stored in `.artifacts/protocol-07/gate-waivers.json` with data engineering lead approval before proceeding.

### Gate 2: Data Quality Requirements
**Type:** Execution  
**Purpose:** Guarantee data quality standards are defined and achievable.  
**Pass Criteria:**
- **Threshold:** Quality coverage score ≥ 95%; feasibility metric ≥ 0.8.  
- **Boolean Check:** `data-quality-report.json` includes all quality dimensions with achievable thresholds.  
- **Metrics:** `data-quality-report.json` captures completeness metric, accuracy metric, consistency metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-07/data-quality-report.json`.  
**Automation:**
- Script: `python3 scripts/ai/validate_data_requirements.py --input quality-criteria.json --output .artifacts/protocol-07/data-quality-report.json`.  
- Script: `python3 scripts/validate_quality_07.py --report .artifacts/protocol-07/data-quality-report.json`.  
- CI Integration: Quality validation stage runs on `ubuntu-latest` with artifact upload to validation dashboard.  
- Config: `config/protocol_gates/07.yaml` stores quality score minimums and feasibility thresholds.  
**Failure Handling:**
- **Rollback:** Adjust quality thresholds, implement data cleaning processes, modify requirements.  
- **Notification:** Notify data quality engineer when quality feasibility score is insufficient.  
- **Waiver:** Requires data architect approval with justification for quality threshold adjustments.

### Gate 3: Compliance Requirements
**Type:** Execution  
**Purpose:** Ensure all regulatory and privacy requirements are identified and addressed.  
**Pass Criteria:**
- **Threshold:** Compliance coverage score ≥ 100%; risk mitigation metric ≥ 0.9.  
- **Boolean Check:** `compliance-report.json` fields `all_regulations_covered` equals `true` and `critical_risks_mitigated` equals `true`.  
- **Metrics:** `compliance-report.json` captures regulation coverage metric, mitigation completeness metric.  
- **Evidence Link:** Evidence validated against `.artifacts/protocol-07/compliance-report.json`.  
**Automation:**
- Script: `python3 scripts/ai/check_compliance_requirements.py --input data-sources.json --output .artifacts/protocol-07/compliance-report.json`.  
- Script: `python3 scripts/validate_compliance_07.py --compliance .artifacts/protocol-07/compliance-report.json`.  
- CI Integration: Compliance validation runs in parallel with quality assessment.  
- Config: `config/protocol_gates/07.yaml` defines compliance coverage requirements and risk thresholds.  
**Failure Handling:**
- **Rollback:** Address compliance gaps, implement additional controls, modify data handling approach.  
- **Notification:** Alert compliance officer when compliance coverage is insufficient.  
- **Waiver:** Requires legal and compliance approval with documented risk acceptance.

### Gate 4: Labeling Strategy Validation
**Type:** Completion  
**Purpose:** Validate that labeling strategy is cost-effective and meets quality requirements.  
**Pass Criteria:**
- **Threshold:** Cost-effectiveness score ≥ 0.8; quality feasibility metric ≥ 0.9.  
- **Boolean Check:** `labeling-strategy-report.json` fields `cost_within_budget` equals `true` and `quality_targets_achievable` equals `true`.  
- **Metrics:** `labeling-strategy-report.json` documents cost metric, timeline metric, quality metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-07/labeling-strategy-report.json`.  
**Automation:**
- Script: `python3 scripts/ai/calculate_labeling_costs.py --input labeling-requirements.json --output .artifacts/protocol-07/labeling-strategy-report.json`.  
- Script: `python3 scripts/aggregate_evidence_07.py --output .artifacts/protocol-07/ --protocol-id 07`.  
- CI Integration: `script-registry-enforcement.yml` confirms aggregator registered and executed before merge.  
- Config: `config/protocol_gates/07.yaml` defines cost-effectiveness thresholds and quality targets.  
**Failure Handling:**
- **Rollback:** Optimize labeling approach, consider alternative methods, adjust quality targets.  
- **Notification:** Inform Protocol 08 owner of handoff delay and share labeling strategy status.  
- **Waiver:** Requires data science lead approval with documented cost-benefit justification.

### Compliance Integration
- **Industry Standards:** Data governance frameworks, privacy by design principles, data quality standards (ISO 800), cloud security standards.  
- **Security Requirements:** Encrypted data storage, secure data transfer protocols, access controls for sensitive data, audit trails for data access.  
- **Regulatory Compliance:** GDPR data protection, HIPAA healthcare privacy, CCPA consumer rights, industry-specific data handling regulations.  
- **Governance:** Gate thresholds governed via `config/protocol_gates/07.yaml`; automation telemetry captured in `.artifacts/validation/protocol_quality_gates-summary.json` and data governance dashboards.

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### Status Announcements:
**[STRICT]** Use standardized announcements for phase transitions:
```
[PROTOCOL 07 | PHASE 1 START] - "Assessing data availability across all sources."
[PROTOCOL 07 | PHASE 2 START] - "Defining data volume and quality requirements."
[PROTOCOL 07 | PHASE 3 START] - "Planning privacy and compliance requirements."
[PROTOCOL 07 | PHASE 4 START] - "Developing data labeling strategy and cost analysis."
[PROTOCOL 07 | PHASE 5 START] - "Defining feature engineering requirements."
[PROTOCOL 07 | PHASE 6 START] - "Designing data storage and access strategy."
[PHASE COMPLETE] - "Data strategy defined, validated, and approved for data collection implementation."
[RAY ERROR] - "Issue encountered during [phase]; see validation-issues.md for details."
```

### Validation Prompts:
**[STRICT]** Use standardized prompts for validation requests:
```
[RAY CONFIRMATION REQUIRED]
> "Data strategy defined and validated. Evidence available:
> - data-availability-report.json
> - data-quality-report.json
> - compliance-report.json
> - labeling-strategy-report.json
>
> Confirm readiness to trigger Protocol 08: Data Collection & Ingestion."
```

### Error Handling:
**[STRICT]** Use standardized error messages for gate failures:
```
[RAY GATE FAILED: Data Availability]
> "Quality gate 'Data Availability' failed.
> Criteria: Data availability score must be ≥ 0.9.
> Actual: Data availability score = 0.75.
> Required action: Identify alternative sources or implement acquisition strategy.
>
> Options:
> 1. Address availability gaps and retry assessment
> 2. Request gate waiver with data justification
> 3. Halt protocol execution and reconsider project scope"
```

---

## 8. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### Validation Scripts:

1. **`[MUST]` Run data availability assessment:**
   * **Action:** Execute script to assess data source availability
   * **Evidence:** Availability output in execution log
   * **Validation:** Availability score ≥ 0.9
   
   ```bash
   # Data availability assessment
   python scripts/ai/assess_data_availability.py \
     --input data-sources.json \
     --output .artifacts/protocol-07/data-availability-report.json
   ```

2. **`[MUST]` Run data quality validation:**
   * **Action:** Execute script to validate data quality requirements
   * **Evidence:** `.artifacts/protocol-07/data-quality-report.json`
   * **Validation:** Quality feasibility score ≥ 0.8
   
   ```bash
   # Data quality validation
   python scripts/ai/validate_data_requirements.py \
     --input quality-criteria.json \
     --output .artifacts/protocol-07/data-quality-report.json
   ```

3. **`[MUST]` Run compliance assessment:**
   * **Action:** Execute script to check compliance requirements
   * **Evidence:** `.artifacts/protocol-07/compliance-report.json`
   * **Validation:** Compliance coverage = 100%
   
   ```bash
   # Compliance assessment
   python scripts/ai/check_compliance_requirements.py \
     --input data-sources.json \
     --output .artifacts/protocol-07/compliance-report.json
   ```

4. **`[MUST]` Run labeling cost calculation:**
   * **Action:** Execute script to calculate labeling costs and timeline
   * **Evidence:** `.artifacts/protocol-07/labeling-strategy-report.json`
   * **Validation:** Cost-effectiveness score ≥ 0.8
   
   ```bash
   # Labeling cost calculation
   python scripts/ai/calculate_labeling_costs.py \
     --input labeling-requirements.json \
     --output .artifacts/protocol-07/labeling-strategy-report.json
   ```

5. **`[MUST]` Aggregate evidence:**
   * **Action:** Execute script to collect all evidence
   * **Evidence:** Evidence manifest in `.artifacts/protocol-07/`
   * **Validation:** All artifacts included in manifest
   
   ```bash
   # Evidence aggregation
   python scripts/aggregate_evidence_07.py \
     --output .artifacts/protocol-07/ \
     --protocol-id 07
   ```

### CI/CD Integration:
```yaml
name: Protocol 07 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 07 Gates
        run: python scripts/run_protocol_07_gates.py
```

### Manual Fallbacks:

**When automation is unavailable:**

1. **Manual Evidence Collection:**
   - Create manual checklist of all required artifacts
   - Verify each artifact exists and contains expected content
   - Document validation in manual evidence log

2. **Manual Compliance Assessment:**
   - Review applicable regulations manually
   - Document compliance gaps and mitigation strategies
   - Create manual compliance report

3. **Manual Quality Gate Validation:**
   - Review each gate criteria manually
   - Document validation results
   - Create manual validation report

---

## 9. HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple checklist execution for protocol completion -->

### Pre-Execution Validation:

1. **`[GUIDELINE]` Validate prerequisites:**
   * **Action:** Verify all required artifacts and approvals are present
   * **Evidence:** Prerequisite validation report
   * **Validation:** All prerequisites marked complete
   
   **Checklist:**
   - [ ] AI use case definition available and validated
   - [ ] Feasibility report reviewed
   - [ ] Success metrics documented
   - [ ] Stakeholder approvals recorded
   - [ ] Data access permissions obtained

### Execution Validation:

1. **`[GUIDELINE]` Validate workflow completion:**
   * **Action:** Verify all phases completed successfully
   * **Evidence:** Phase completion log
   * **Validation:** All phases marked complete
   
   **Checklist:**
   - [ ] Data availability assessment completed
   - [ ] Data quality requirements defined
   - [ ] Privacy and compliance planned
   - [ ] Data labeling strategy developed
   - [ ] Feature engineering requirements specified
   - [ ] Data storage strategy designed

### Post-Execution Validation:

1. **`[GUIDELINE]` Validate quality gates:**
   * **Action:** Verify all quality gates passed
   * **Evidence:** Quality gate validation report
   * **Validation:** All gates marked pass
   
   **Checklist:**
   - [ ] Data availability validation passed
   - [ ] Data quality requirements passed
   - [ ] Compliance requirements passed
   - [ ] Labeling strategy validation passed

### Handoff to Protocol 08:

1. **`[MUST]` Execute protocol handoff:**
   * **Action:** Package evidence and trigger Protocol 08
   * **Evidence:** Handoff confirmation in execution log
   * **Validation:** Protocol 08 acknowledges receipt
   
   **Handoff Package:**
   - Data strategy document
   - Data requirements specifications
   - Compliance framework documentation
   - Labeling strategy and cost analysis
   - Feature engineering requirements
   - Storage architecture design
   - Evidence manifest and checksums

   **[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 08: Data Collection & Ingestion

---

## 10. REASONING & REFLECTION

### Decision Logic

#### Why Data Availability ≥ 90% Threshold?
The 90% threshold balances:
- **Project Feasibility**: Ensures sufficient data for model development
- **Risk Management**: Allows for some uncertainty while maintaining viability
- **Cost Efficiency**: Prevents over-investment in data acquisition
- **Timeline Protection**: Reduces risk of project delays due to data issues

#### Compliance-First Approach
Compliance planning is critical because:
- **Legal Requirements**: Regulatory violations can result in severe penalties
- **Reputation Protection**: Data privacy breaches damage trust
- **Implementation Costs**: Retrofitting compliance is expensive and complex
- **Business Continuity**: Compliance issues can halt project deployment

#### Comprehensive Labeling Strategy
Detailed labeling analysis ensures:
- **Cost Control**: Prevents budget overruns on data preparation
- **Quality Assurance**: Ensures labels meet model training requirements
- **Timeline Management**: Provides realistic estimates for project planning
- **Scalability**: Designs labeling processes that can grow with project needs

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Insufficient data availability | Implement data augmentation, acquire additional sources, modify model approach |
| Compliance gaps | Design privacy-preserving techniques, implement additional controls, modify data handling |
| High labeling costs | Consider semi-supervised learning, implement active learning, explore synthetic data |
| Quality standards unachievable | Adjust thresholds, implement data cleaning, reconsider feature requirements |
| Storage costs prohibitive | Optimize data retention, implement data lifecycle management, consider cloud solutions |

### Continuous Improvement

#### Feedback Collection
- Data availability prediction accuracy tracking
- Compliance issue detection and resolution metrics
- Labeling cost estimation vs actual expenditures
- Storage architecture performance vs projections

#### Metrics Tracked
- Data accessibility scores vs actual access success rates
- Compliance assessment completeness vs audit findings
- Labeling cost estimation accuracy over multiple projects
- Storage utilization and cost optimization metrics

#### Update Frequency
- Quarterly review of data availability assessment accuracy
- Annual update of compliance requirement checklists
- Continuous improvement based on project outcomes
- Immediate updates for regulatory changes

### Lessons Learned
*[This section will be populated after protocol execution]*

- Lesson 1: [Date] - [Description]
- Lesson 2: [Date] - [Description]
- Lesson 3: [Date] - [Description]

### Best Practices Discovered
*[To be documented during implementation]*

1. Always assess data accessibility before technical planning
2. Include compliance officers early in strategy development
3. Prepare multiple labeling approaches with cost-benefit analysis
4. Design storage architecture with growth and compliance in mind
5. Maintain traceability between data requirements and model objectives

---

**Protocol 07: AI Data Strategy & Requirements Planning**  
**Version**: 1.0  
**Last Updated**: 2025-01-06  
**Next Review**: After 5 executions or quarterly  
**Status**: Ready for Validation

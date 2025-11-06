---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 06: AI USE CASE DEFINITION & VALIDATION (AI-PROJECT-PLANNING COMPLIANT)

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 06
- **Protocol Name:** AI AI USE CASE DEFINITION & VALIDATION (AI-PROJECT-PLANNING COMPLIANT)
- **Protocol Owner:** AI Use Case Specialist
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-06
- **Last Updated:** 2025-01-06
- **Version:** 1.0

### Protocol Classification
- **Category:** AI Planning
- **Criticality:** High
- **Complexity:** High
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** Protocol 03
- **Successor:** Protocol 07
- **Related Protocols:** Protocol 08, Protocol 09

### Protocol Metadata
- **Purpose:** Define and validate AI use case with feasibility assessment and success metrics
- **Success Criteria:** All quality gates pass, Problem-AI Fit Score ≥ 0.8, stakeholder approval obtained
- **Failure Modes:** Insufficient data, low feasibility score, stakeholder rejection
- **Recovery Procedure:** Reassess requirements, modify approach, or recommend alternative solutions

---

## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** AI Use Case Specialist
- **Responsibilities:**
  - Execute protocol steps in sequence
  - Validate at each checkpoint
  - Escalate blockers immediately
  - Document decisions and rationale
- **Authority:** Can make decisions on protocol execution and quality gates
- **Escalation:** Technical Lead or AI Architect

#### Protocol Owner
- **Role:** AI Use Case Specialist
- **Responsibilities:**
  - Approve protocol execution
  - Review quality gates
  - Sign off on handoff
  - Address escalations
- **Authority:** Can make decisions on protocol execution and quality gates

#### Downstream Owner
- **Role:** Protocol 07 Owner (Data Strategist)
- **Responsibilities:**
  - Receive handoff package
  - Validate inputs from this protocol
  - Provide feedback on quality
  - Confirm readiness for next phase
- **Authority:** Can request clarification or additional requirements

### Role Interactions
- **Executor → Owner:** Daily status updates, immediate blocker notification
- **Owner → Downstream:** Handoff package with validation evidence
- **Downstream → Executor:** Feedback on data requirements completeness

### Decision Authority Matrix
| Decision Type | Executor | Owner | Downstream | Executive |
|---------------|----------|-------|------------|-----------|
| Problem classification | ✅ | ✅ | ❌ | ❌ |
| Feasibility threshold approval | ❌ | ✅ | ❌ | ❌ |
| Success metrics definition | ✅ | ✅ | ❌ | ❌ |
| Stakeholder approval | ❌ | ✅ | ❌ | ✅ |

---

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT] All prerequisites must be met before protocol execution.**

### Required Artifacts
**[STRICT]** The following artifacts must exist and be validated:
- `PROJECT-BRIEF.md` from Protocol 03 (validated project scope)
- `technical-baseline.json` from Protocol 03 (technical constraints)
- `project-brief-validation-report.json` from Protocol 03 (quality validation)
- `BRIEF-APPROVAL-RECORD.json` from Protocol 03 (stakeholder approval)

### Required Approvals
**[STRICT]** The following approvals must be obtained:
- Project Brief approval from client and internal stakeholders
- Technical baseline sign-off from solutions architect

### System State Requirements
**[STRICT]** System must meet the following conditions:
- Access to AI use case templates under `.templates/ai/`
- Automation scripts `classify_ai_problem_type.py`, `calculate_feasibility_score.py`, and `generate_success_metrics.py` available
- Data assessment tools and frameworks accessible

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

You are an **AI Use Case Specialist**. Your mission is to analyze business requirements and define a comprehensive AI use case with validated feasibility, clear success metrics, and stakeholder alignment.

**[CRITICAL] Do not proceed to data strategy without Problem-AI Fit Score ≥ 0.8 and documented stakeholder approval.**

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1

**Action:** Execute business problem analysis activities

**Description:** Foundational analysis to determine ML approach

**Input:** Project brief and discovery notes from Protocol 05

**Output:** Business problem analysis with learning paradigm classification

**Communication:** Document problem analysis results and ML approach recommendations

**Evidence:** Store problem statements, paradigm analysis, and classification results in `.artifacts/protocol-06/business-analysis/`

**Duration:** 2-3 hours

---

### STEP 2

**Action:** Execute data requirements assessment activities

**Description:** Data availability and requirements evaluation phase

**Input:** Business problem analysis and ML approach from STEP 1

**Output:** Data requirements inventory with availability assessment

**Communication:** Report data requirements, gaps, and collection needs

**Evidence:** Store data requirements analysis and availability reports in `.artifacts/protocol-06/data-assessment/`

**Duration:** 3-4 hours

---

### STEP 3

**Action:** Execute success metrics definition activities

**Description:** Success criteria and KPI definition phase

**Input:** Business problem analysis and data requirements

**Output:** Comprehensive success metrics with measurement frameworks

**Communication:** Document success metrics, targets, and measurement approaches

**Evidence:** Store metrics definitions, targets, and measurement plans in `.artifacts/protocol-06/success-metrics/`

**Duration:** 2-3 hours

---

### STEP 4

**Action:** Execute feasibility assessment activities

**Description:** Technical and business feasibility evaluation phase

**Input:** Success metrics and data requirements from previous steps

**Output:** Feasibility assessment with risk analysis

**Communication:** Provide feasibility results, risk assessment, and recommendations

**Evidence:** Store feasibility analysis, risk assessments, and technical evaluations in `.artifacts/protocol-06/feasibility/`

**Duration:** 2-3 hours

---

### STEP 5

**Action:** Execute stakeholder alignment activities

**Description:** Stakeholder validation and approval phase

**Input:** Feasibility assessment and success metrics

**Output:** Stakeholder approval with documented requirements

**Communication:** Document stakeholder feedback, approvals, and requirement adjustments

**Evidence:** Store stakeholder meeting notes, approvals, and requirement confirmations in `.artifacts/protocol-06/stakeholder-alignment/`

**Duration:** 1-2 hours

---

### STEP 6

**Action:** Execute use case documentation activities

**Description:** Final documentation and handoff preparation phase

**Input:** All analysis results and stakeholder approvals

**Output:** Complete use case documentation ready for Protocol 07

**Communication:** Provide final use case summary and handoff readiness status

**Evidence:** Store complete use case documentation and handoff package in `.artifacts/protocol-06/handoff/`

**Duration:** 1-2 hours

---

## WORKFLOW EXECUTION DETAILS

### STEP 1: Business Problem Analysis
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Foundational analysis to determine ML approach -->

1. **`[MUST]` Analyze business problem:**
   * **Action:** Extract core business problem from project brief and discovery notes
   * **Evidence:** Problem statement documented in use case definition
   * **Validation:** Problem clearly articulated with measurable objectives
   
   **Communication:** 
   > "[PROTOCOL 06 | STEP 1 START] - Analyzing business problem for ML solution design."
   
   **Halt condition:** Stop if business problem is unclear or not measurable.

2. **`[MUST]` Classify learning paradigm:**
   * **Action:** Determine appropriate ML approach based on problem characteristics
   * **Evidence:** Learning paradigm documented with justification
   * **Validation:** Paradigm selection matches problem requirements
   
   **Options:**
   - Supervised Learning (labels available)
   - Unsupervised Learning (pattern discovery needed)
   - Reinforcement Learning (sequential decision-making)
   - Semi-supervised Learning (limited labels)
   - Self-supervised Learning (representation learning)

3. **`[GUIDELINE]` Identify specific problem type:**
   * **Action:** Map to specific ML problem category for algorithm selection
   * **Evidence:** Problem type documented with examples
   * **Validation:** Problem type aligns with learning paradigm
   
   **Classification:**
   - **Classification**: Binary, Multi-class, Multi-label
   - **Regression**: Linear, Non-linear, Time-series
   - **Clustering**: Partitioning, Hierarchical, Density-based
   - **Dimensionality Reduction**: PCA, t-SNE, Autoencoders
   - **Anomaly Detection**: Statistical, ML-based
   - **Recommendation**: Collaborative, Content-based, Hybrid
   - **NLP Tasks**: Classification, NER, Generation, Translation
   - **Computer Vision**: Detection, Segmentation, Recognition
   - **Reinforcement**: Policy optimization, Value-based

4. **`[GUIDELINE]` Document problem characteristics:**
   * **Action:** Capture technical constraints and requirements
   * **Evidence:** Problem characteristics matrix created
   * **Validation:** All key constraints documented
   
   **Characteristics:**
   - Data volume requirements
   - Real-time vs batch processing
   - Interpretability requirements
   - Accuracy vs speed trade-offs

### STEP 2: Data Requirements Assessment
<!-- [Category: DATA-ANALYSIS] -->
<!-- Why: Data availability determines ML feasibility -->

1. **`[MUST]` Assess data availability:**
   * **Action:** Inventory existing data sources and evaluate accessibility
   * **Evidence:** Data inventory with accessibility status
   * **Validation:** At least 80% of required data identified as accessible
   
   **Communication:** 
   > "[PROTOCOL 06 | STEP 2] - Assessing data availability and requirements."
   
   **Halt condition:** Stop if critical data sources are unavailable.

2. **`[MUST]` Evaluate data quality:**
   * **Action:** Assess data completeness, accuracy, and consistency
   * **Evidence:** Data quality report with scores
   * **Validation:** Quality scores meet minimum thresholds for ML

3. **`[MUST]` Estimate data volume needs:**
   * **Action:** Calculate minimum data requirements based on problem complexity
   * **Evidence:** Data volume estimation with justification
   * **Validation:** Volume requirements are realistic and achievable

4. **`[GUIDELINE]` Identify data gaps:**
   * **Action:** Document missing data and acquisition strategies
   * **Evidence:** Gap analysis with acquisition timeline
   * **Validation:** All gaps have documented mitigation strategies

### STEP 3: Success Metrics Definition
<!-- [Category: METRICS-DEFINITION] -->
<!-- Why: Clear metrics enable ML solution evaluation -->

1. **`[MUST]` Define business success metrics:**
   * **Action:** Establish measurable business outcomes and KPIs
   * **Evidence:** Success metrics document with targets and measurement methods
   * **Validation:** All metrics are specific, measurable, and time-bound
   
   **Communication:** 
   > "[PROTOCOL 06 | STEP 3] - Defining success metrics and evaluation framework."

2. **`[MUST]` Establish ML performance metrics:**
   * **Action:** Define technical metrics for model evaluation
   * **Evidence:** ML metrics specification with baseline targets
   * **Validation:** Metrics align with business objectives and are technically feasible

3. **`[GUIDELINE]` Set monitoring requirements:**
   * **Action:** Define ongoing monitoring and evaluation needs
   * **Evidence**: Monitoring framework with alert thresholds
   * **Validation**: Monitoring covers critical success factors

4. **`[GUIDELINE]` Document success criteria:**
   * **Action**: Create comprehensive success criteria documentation
   * **Evidence**: Success criteria matrix with validation rules
   * **Validation**: Criteria cover all aspects of solution success

### STEP 4: Feasibility Assessment
<!-- [Category: FEASIBILITY-ANALYSIS] -->
<!-- Why: Validate technical and business viability -->

1. **`[MUST]` Assess technical feasibility:**
   * **Action**: Evaluate technical requirements and capabilities
   * **Evidence**: Technical feasibility analysis with capability assessment
   * **Validation**: Technical requirements can be met with available resources
   
   **Communication:** 
   > "[PROTOCOL 06 | STEP 4] - Conducting technical and business feasibility assessment."

2. **`[MUST]` Evaluate business feasibility:**
   * **Action**: Assess business value, ROI, and strategic alignment
   * **Evidence**: Business case analysis with ROI projections
   * **Validation**: Business case meets minimum ROI and strategic requirements

3. **`[GUIDELINE]` Analyze risks and constraints:**
   * **Action**: Identify and evaluate potential risks and constraints
   * **Evidence**: Risk analysis with mitigation strategies
   * **Validation**: All critical risks have documented mitigation plans

4. **`[GUIDELINE]` Validate resource requirements:**
   * **Action**: Confirm availability of required resources and expertise
   * **Evidence**: Resource inventory with allocation plan
   * **Validation**: Required resources are available or can be acquired

### STEP 5: Stakeholder Alignment
<!-- [Category: STAKEHOLDER-MANAGEMENT] -->
<!-- Why: Ensure stakeholder buy-in and requirement validation -->

1. **`[MUST]` Validate requirements with stakeholders:**
   * **Action**: Review and confirm requirements with key stakeholders
   * **Evidence**: Stakeholder sign-off documentation with feedback
   * **Validation**: All stakeholders agree on documented requirements
   
   **Communication:** 
   > "[PROTOCOL 06 | STEP 5] - Achieving stakeholder alignment and approval."

2. **`[MUST]` Address stakeholder concerns:**
   * **Action**: Resolve concerns and incorporate stakeholder feedback
   * **Evidence**: Issue resolution logs with stakeholder confirmations
   * **Validation**: All raised concerns are addressed or documented with mitigation

3. **`[GUIDELINE]` Secure executive sponsorship:**
   * **Action**: Obtain executive support and resource commitments
   * **Evidence**: Sponsorship agreements with resource allocations
   * **Validation**: Executive sponsors committed with clear responsibilities

4. **`[GUIDELINE]` Document stakeholder agreements:**
   * **Action**: Create comprehensive stakeholder agreement documentation
   * **Evidence**: Signed agreements with roles and responsibilities
   * **Validation**: All agreements documented and distributed

### STEP 6: Use Case Documentation
<!-- [Category: DOCUMENTATION-FINALIZATION] -->
<!-- Why: Create comprehensive use case documentation for handoff -->

1. **`[MUST]` Compile complete use case documentation:**
   * **Action**: Assemble all analysis results into comprehensive use case
   * **Evidence**: Complete use case document with all sections
   * **Validation**: Documentation meets all quality and completeness standards
   
   **Communication:** 
   > "[PROTOCOL 06 | STEP 6] - Finalizing use case documentation and preparing handoff."

2. **`[MUST]` Create implementation roadmap:**
   * **Action**: Develop detailed implementation plan with milestones
   * **Evidence**: Implementation roadmap with timeline and dependencies
   * **Validation**: Roadmap is realistic and achievable with available resources

3. **`[GUIDELINE]` Prepare handoff package:**
   * **Action**: Assemble all deliverables for Protocol 07 handoff
   * **Evidence**: Handoff package with all required artifacts
   * **Validation**: Package contains all materials needed for data strategy planning

4. **`[GUIDELINE]` Document lessons learned:**
   * **Action**: Capture insights and improvements for future use cases
   * **Evidence**: Lessons learned documentation with best practices
   * **Validation**: Documentation provides actionable insights for future projects

5. **`[GUIDELINE]` Plan data collection strategy:**
   * **Action:** Design approach for acquiring missing data
   * **Evidence:** Data collection plan with timeline and costs
   * **Validation:** Collection strategy is feasible within project constraints

### PHASE 3: Success Metrics Definition
<!-- [Category: METRICS-DEFINITION] -->
<!-- Why: Clear metrics enable objective evaluation of ML success -->

1. **`[MUST]` Define primary metrics:**
   * **Action:** Select technical metrics based on problem type
   * **Evidence:** Primary metrics documented with target values
   * **Validation:** Metrics align with business objectives
   
   **Communication:** 
   > "[PROTOCOL 06 | PHASE 3] - Defining success metrics and performance targets."
   
   **Technical Metrics:**
   - **Classification**: Accuracy, Precision, Recall, F1-Score, AUC-ROC
   - **Regression**: MAE, MSE, RMSE, R², MAPE
   - **Clustering**: Silhouette Score, Davies-Bouldin Index
   - **Ranking**: NDCG, MAP, MRR

2. **`[MUST]` Set business metrics:**
   * **Action:** Define measurable business outcomes
   * **Evidence:** Business metrics with quantifiable targets
   * **Validation:** Metrics are measurable and time-bound
   
   **Business Outcomes:**
   - ROI expectations
   - Cost reduction targets
   - Efficiency improvements
   - User satisfaction scores

3. **`[GUIDELINE]` Establish baseline performance:**
   * **Action:** Document current system and benchmark performance
   * **Evidence:** Baseline measurements with sources
   * **Validation:** Baselines are current and relevant

4. **`[GUIDELINE]` Define minimum viable performance:**
   * **Action:** Set thresholds for production deployment
   * **Evidence:** MVP thresholds with business justification
   * **Validation:** Thresholds are realistic and achievable
   
   **MVP Criteria:**
   - Threshold for production deployment
   - Acceptable error rates
   - Performance degradation limits

### PHASE 4: Feasibility Assessment
<!-- [Category: FEASIBILITY-ANALYSIS] -->
<!-- Why: Ensure AI solution is viable before investment -->

1. **`[MUST]` Evaluate data feasibility:**
   * **Action:** Assess data availability, quality, and collection costs
   * **Evidence:** Data feasibility report with scores
   * **Validation:** Data feasibility score ≥ 0.7
   
   **Communication:** 
   > "[PROTOCOL 06 | PHASE 4] - Evaluating technical and business feasibility."
   
   **Halt condition:** Stop if data feasibility score < 0.7.

2. **`[MUST]` Assess technical feasibility:**
   * **Action:** Evaluate algorithm availability and computational requirements
   * **Evidence:** Technical feasibility analysis
   * **Validation:** Technical approach is viable with available resources

3. **`[MUST]` Analyze business feasibility:**
   * **Action:** Conduct ROI and cost-benefit analysis
   * **Evidence:** Business case with financial projections
   * **Validation:** ROI meets minimum business requirements

4. **`[GUIDELINE]` Perform risk assessment:**
   * **Action:** Identify and evaluate technical, business, and operational risks
   * **Evidence:** Risk register with mitigation strategies
   * **Validation:** All critical risks have mitigation plans

5. **`[GUIDELINE]` Calculate Problem-AI Fit Score:**
   * **Action:** Execute feasibility scoring algorithm
   * **Evidence:** Comprehensive feasibility report with score
   * **Validation:** Score calculation follows defined methodology

**Decision Point**: 
- If Problem-AI Fit Score ≥ 0.8 → Continue to PHASE 5
- If Problem-AI Fit Score < 0.8 → Recommend alternative solutions

### PHASE 5: Stakeholder Alignment
<!-- [Category: STAKEHOLDER-MANAGEMENT] -->
<!-- Why: Ensure buy-in and shared understanding across all stakeholders -->

1. **`[MUST]` Prepare stakeholder presentation:**
   * **Action:** Create comprehensive presentation covering AI solution approach
   * **Evidence:** Presentation slides and talking points documented
   * **Validation:** Presentation addresses all stakeholder concerns
   
   **Communication:** 
   > "[PROTOCOL 06 | PHASE 5] - Preparing stakeholder alignment materials."
   
   **Presentation Content:**
   - Problem definition and AI solution approach
   - Success metrics and expected outcomes
   - Timeline and resource requirements
   - Risks and mitigation strategies

2. **`[MUST]` Conduct stakeholder review session:**
   * **Action:** Present AI use case and collect feedback
   * **Evidence:** Meeting notes and feedback documented
   * **Validation:** All stakeholder questions addressed
   
   **Halt condition:** Stop if major stakeholders reject the approach.

3. **`[GUIDELINE]` Document stakeholder approval:**
   * **Action:** Record decisions and obtain formal sign-off
   * **Evidence:** Approval record with signatures
   * **Validation:** All required approvals obtained

**Decision Point**: 
- If stakeholder approval obtained → Continue to PHASE 6
- If major concerns raised → Address and revisit earlier steps

### PHASE 6: Use Case Documentation
<!-- [Category: DOCUMENTATION] -->
<!-- Why: Create permanent record of AI use case definition -->

1. **`[MUST]` Compile use case definition:**
   * **Action:** Create comprehensive use case document
   * **Evidence:** Complete use case definition document
   * **Validation:** Document meets all protocol requirements
   
   **Communication:** 
   > "[PROTOCOL 06 | PHASE 6] - Finalizing use case documentation."

2. **`[MUST]` Create supporting documents:**
   * **Action:** Generate all required supporting artifacts
   * **Evidence:** All supporting documents completed
   * **Validation:** Documents are consistent and complete

3. **`[GUIDELINE]` Validate completeness:**
   * **Action:** Review against protocol checklist
   * **Evidence:** Validation checklist completed
   * **Validation:** All checklist items marked complete

**Output**: Complete use case definition package ready for data strategy planning

---

## 4. REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level retrospective and continuous improvement tracking -->

### Retrospective Guidance

After completing protocol execution (successful or halted), conduct retrospective:

**Timing:** Within 24-48 hours of completion

**Participants:** Protocol executor, data strategy team, stakeholders

**Agenda:**
1. **What went well:**
   - Which problem classification steps were most effective?
   - Which feasibility assessments provided highest value?
   - Which stakeholder communication approaches worked best?

2. **What went poorly:**
   - Which data availability assessments were inaccurate?
   - Which feasibility calculations need refinement?
   - Which stakeholder concerns were not anticipated?

3. **Action items:**
   - Problem classification template updates needed?
   - Feasibility scoring model adjustments?
   - Stakeholder presentation improvements?

**Output:** Retrospective report stored in protocol execution artifacts

### Continuous Improvement Opportunities

#### Identified Improvement Opportunities
- Refine Problem-AI Fit Score calculation based on actual project outcomes
- Enhance data availability assessment accuracy
- Improve stakeholder alignment process efficiency

#### Process Optimization Tracking
- Track feasibility prediction accuracy over time
- Monitor stakeholder approval rates and feedback patterns
- Measure use case quality impact on downstream protocols
- Identify automation opportunities in feasibility assessment

#### Tracking Mechanisms and Metrics
- Monthly metrics dashboard with feasibility accuracy trends
- Improvement tracking log with before/after comparisons
- Evidence of improvement validation through project success rates

---

## 5. INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### Inputs From:
**[STRICT]** The following inputs must be validated before execution:
- **Protocol 03**: `PROJECT-BRIEF.md`, `technical-baseline.json` - Project scope and technical context.
- **Protocol 03**: `BRIEF-APPROVAL-RECORD.json` - Stakeholder approval evidence.

### Outputs To:
**[STRICT]** The following outputs must be generated for downstream protocols:
- **Protocol 07**: `AI-USE USE-CASE-DEFINITION.md`, `feasibility-report.json` - Data strategy planning inputs.
- **Protocol 08**: `data-requirements.json` - Data collection specifications.

### Artifact Storage Locations:
**[STRICT]** All artifacts must be stored in standardized locations:
- `.artifacts/protocol-06/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->

### Gate 1: Problem Analysis Validation
**Type:** Prerequisite  
**Purpose:** Confirm business problem analysis meets ML readiness requirements.  
**Pass Criteria:**
- **Threshold:** Problem clarity score ≥ 0.9; classification completeness metric = 100%.  
- **Boolean Check:** Problem analysis document field `status` equals `VALIDATED`.  
- **Metrics:** Analysis captures problem clarity metric and classification accuracy metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-06/problem-analysis-report.json`.  
**Automation:**
- Script: `python3 scripts/ai/classify_ai_problem_type.py --input project-brief.md --output .artifacts/protocol-06/problem-analysis-report.json`.  
- Script: `python3 scripts/validate_problem_analysis_06.py --log .artifacts/protocol-06/analysis-log.json`.  
- CI Integration: `ai-validation-pipeline.yml` invokes problem analysis on push; failures gate pull requests.  
- Config: `config/protocol_gates/06.yaml` defines clarity thresholds and classification requirements.  
**Failure Handling:**
- **Rollback:** Revisit problem definition, clarify business objectives, rerun analysis script.  
- **Notification:** Alert Protocol 03 owner and AI architect via governance channel when clarity score drops below threshold.  
- **Waiver:** Waivers stored in `.artifacts/protocol-06/gate-waivers.json` with technical lead approval before proceeding.

### Gate 2: Feasibility Assessment
**Type:** Execution  
**Purpose:** Guarantee AI solution feasibility meets minimum viability thresholds.  
**Pass Criteria:**
- **Threshold:** Problem-AI Fit Score ≥ 0.8; data feasibility score ≥ 0.7.  
- **Boolean Check:** `feasibility-report.json` fields `problem_ai_fit_score` ≥ 0.8 and `data_feasibility_score` ≥ 0.7.  
- **Metrics:** `feasibility-report.json` captures technical feasibility metric, business feasibility metric, risk assessment metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-06/feasibility-report.json`.  
**Automation:**
- Script: `python3 scripts/ai/calculate_feasibility_score.py --input data-assessment.json --output .artifacts/protocol-06/feasibility-report.json`.  
- Script: `python3 scripts/validate_feasibility_06.py --report .artifacts/protocol-06/feasibility-report.json`.  
- CI Integration: Feasibility validation stage runs on `ubuntu-latest` with artifact upload to validation dashboard.  
- Config: `config/protocol_gates/06.yaml` stores feasibility score minimums and risk thresholds.  
**Failure Handling:**
- **Rollback:** Reassess requirements, modify technical approach, or consider alternative solutions.  
- **Notification:** Notify AI architect when feasibility score falls below threshold.  
- **Waiver:** Exceptional waivers require AI director sign-off and must document mitigation strategies.

### Gate 3: Success Metrics Validation
**Type:** Execution  
**Purpose:** Ensure success metrics are comprehensive, measurable, and aligned with business objectives.  
**Pass Criteria:**
- **Threshold:** Metrics completeness score ≥ 95%; business alignment metric ≥ 0.9.  
- **Boolean Check:** `success-metrics.json` includes both technical and business metrics with target values.  
- **Metrics:** `success-metrics.json` captures metrics coverage metric, measurability metric, alignment metric.  
- **Evidence Link:** Evidence validated against `.artifacts/protocol-06/success-metrics.json`.  
**Automation:**
- Script: `python3 scripts/ai/generate_success_metrics.py --input problem-analysis.json --output .artifacts/protocol-06/success-metrics.json`.  
- Script: `python3 scripts/validate_metrics_06.py --metrics .artifacts/protocol-06/success-metrics.json`.  
- CI Integration: Metrics validation runs in parallel with feasibility assessment.  
- Config: `config/protocol_gates/06.yaml` defines metrics completeness requirements and alignment thresholds.  
**Failure Handling:**
- **Rollback:** Refine metrics definition, ensure business alignment, add missing measurement approaches.  
- **Notification:** Alert business analyst when metrics alignment score is insufficient.  
- **Waiver:** Requires product owner approval with justification for metric exclusions.

### Gate 4: Stakeholder Approval
**Type:** Completion  
**Purpose:** Validate that all required stakeholder approvals are captured with proper documentation.  
**Pass Criteria:**
- **Threshold:** Stakeholder approval completion rate ≥ 90%; feedback resolution metric = 100%.  
- **Boolean Check:** `stakeholder-approval-record.json` fields `client_status` and `internal_status` equal `approved`.  
- **Metrics:** `approval-tracking.json` documents approval latency metric and feedback resolution metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-06/stakeholder-approval-record.json`.  
**Automation:**
- Script: `python3 scripts/aggregate_evidence_06.py --output .artifacts/protocol-06/ --protocol-id 06`.  
- Script: `python3 scripts/run_protocol_06_gates.py --report .artifacts/protocol-06/handoff-verification.json`.  
- CI Integration: `script-registry-enforcement.yml` confirms aggregator registered and executed before merge.  
- Config: `config/protocol_gates/06.yaml` defines approval completion thresholds and required signatories.  
**Failure Handling:**
- **Rollback:** Address stakeholder concerns, update use case documentation, rerun approval process.  
- **Notification:** Inform Protocol 07 owner of handoff delay and share approval status.  
- **Waiver:** Emergency waiver requires executive sponsor approval with documented business justification.

### Compliance Integration
- **Industry Standards:** ML model documentation standards, AI ethics guidelines, regulatory compliance for AI systems.  
- **Security Requirements:** Secure handling of business data data, encrypted storage of feasibility assessments, access controls for sensitive AI use case information.  
- **Regulatory Compliance:** AI governance framework alignment, documentation retention for audit trails, ethical AI implementation standards.  
- **Governance:** Gate thresholds governed via `config/protocol_gates/06.yaml`; automation telemetry captured in `.artifacts/validation/protocol_quality_gates-summary.json` and AI governance dashboards.

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### Status Announcements:
**[STRICT]** Use standardized announcements for phase transitions:
```
[PROTOCOL 06 | PHASE 1 START] - "Analyzing business problem for AI solution design."
[PROTOCOL 06 | PHASE 2 START] - "Assessing data availability and requirements."
[PROTOCOL 06 | PHASE 3 START] - "Defining success metrics and performance targets."
[PROTOCOL 06 | PHASE 4 START] - "Evaluating technical and business feasibility."
[PROTOCOL 06 | PHASE 5 START] - "Preparing stakeholder alignment materials."
[PROTOCOL 06 | PHASE 6 START] - "Finalizing use case documentation."
[PHASE COMPLETE] - "AI use case defined, validated, and approved for data strategy planning."
[RAY ERROR] - "Issue encountered during [phase]; see validation-issues.md for details."
```

### Validation Prompts:
**[STRICT]** Use standardized prompts for validation requests:
```
[RAY CONFIRMATION REQUIRED]
> "AI use case defined and validated. Evidence available:
> - problem-analysis-report.json
> - feasibility-report.json
> - success-metrics.json
> - stakeholder-approval-record.json
>
> Confirm readiness to trigger Protocol 07: Data Strategy & Requirements Planning."
```

### Error Handling:
**[STRICT]** Use standardized error messages for gate failures:
```
[RAY GATE FAILED: Feasibility Assessment]
> "Quality gate 'Feasibility Assessment' failed.
> Criteria: Problem-AI Fit Score must be ≥ 0.8.
> Actual: Problem-AI Fit Score = 0.65.
> Required action: Reassess requirements, modify approach, or consider alternatives.
>
> Options:
> 1. Address feasibility gaps and retry assessment
> 2. Request gate waiver with technical justification
> 3. Halt protocol execution and recommend alternative solutions"
```

---

## 8. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### Validation Scripts:

1. **`[MUST]` Run problem classification:**
   * **Action:** Execute script to classify AI problem type
   * **Evidence:** Classification output in execution log
   * **Validation:** Classification confidence ≥ 0.8
   
   ```bash
   # Problem classification
   python scripts/ai/classify_ai_problem_type.py \
     --input project-brief.md \
     --output .artifacts/protocol-06/problem-analysis-report.json
   ```

2. **`[MUST]` Run feasibility assessment:**
   * **Action:** Execute script to calculate Problem-AI Fit Score
   * **Evidence:** `.artifacts/protocol-06/feasibility-report.json`
   * **Validation:** Fit score ≥ 0.8
   
   ```bash
   # Feasibility assessment
   python scripts/ai/calculate_feasibility_score.py \
     --input data-assessment.json \
     --output .artifacts/protocol-06/feasibility-report.json
   ```

3. **`[MUST]` Run success metrics generation:**
   * **Action:** Execute script to generate success metrics
   * **Evidence:** `.artifacts/protocol-06/success-metrics.json`
   * **Validation:** Metrics completeness ≥ 95%
   
   ```bash
   # Success metrics generation
   python scripts/ai/generate_success_metrics.py \
     --input problem-analysis.json \
     --output .artifacts/protocol-06/success-metrics.json
   ```

4. **`[MUST]` Aggregate evidence:**
   * **Action:** Execute script to collect all evidence
   * **Evidence:** Evidence manifest in `.artifacts/protocol-06/`
   * **Validation:** All artifacts included in manifest
   
   ```bash
   # Evidence aggregation
   python scripts/aggregate_evidence_06.py \
     --output .artifacts/protocol-06/ \
     --protocol-id 06
   ```

### CI/CD Integration:
```yaml
name: Protocol 06 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 06 Gates
        run: python scripts/run_protocol_06_gates.py
```

### Manual Fallbacks:

**When automation is unavailable:**

1. **Manual Evidence Collection:**
   - Create manual checklist of all required artifacts
   - Verify each artifact exists and contains expected content
   - Document validation in manual evidence log

2. **Manual Stakeholder Approval:**
   - Send approval summary to stakeholders
   - Collect written confirmations
   - Document approvals in approval record

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
   - [ ] PROJECT-BRIEF.md available and validated
   - [ ] Technical baseline documented
   - [ ] Stakeholder approvals recorded
   - [ ] System state requirements verified

### Execution Validation:

1. **`[GUIDELINE]` Validate workflow completion:**
   * **Action:** Verify all phases completed successfully
   * **Evidence:** Phase completion log
   * **Validation:** All phases marked complete
   
   **Checklist:**
   - [ ] Business problem analysis completed
   - [ ] Data requirements assessed
   - [ ] Success metrics defined
   - [ ] Feasibility assessment completed
   - [ ] Stakeholder alignment achieved
   - [ ] Use case documentation finalized

### Post-Execution Validation:

1. **`[GUIDELINE]` Validate quality gates:**
   * **Action:** Verify all quality gates passed
   * **Evidence:** Quality gate validation report
   * **Validation:** All gates marked pass
   
   **Checklist:**
   - [ ] Problem analysis validation passed
   - [ ] Feasibility assessment passed
   - [ ] Success metrics validation passed
   - [ ] Stakeholder approval obtained

### Handoff to Protocol 07:

1. **`[MUST]` Execute protocol handoff:**
   * **Action:** Package evidence and trigger Protocol 07
   * **Evidence:** Handoff confirmation in execution log
   * **Validation:** Protocol 07 acknowledges receipt
   
   **Handoff Package:**
   - AI use case definition document
   - Feasibility assessment report
   - Success metrics specification
   - Data requirements summary
   - Stakeholder approval record
   - Evidence manifest and checksums

   **[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 07: Data Strategy & Requirements Planning

---

## 10. REASONING & REFLECTION

### Decision Logic

#### Why Problem-AI Fit Score ≥ 0.8 Threshold?
The 0.8 threshold balances:
- **Risk Management**: Ensures sufficient feasibility for successful AI implementation
- **Investment Protection**: Prevents investment in low-probability AI solutions
- **Practical Viability**: Allows for reasonable uncertainty while maintaining success likelihood
- **Resource Optimization**: Focuses resources on high-potential AI opportunities

#### Stakeholder Approval Requirements
Stakeholder approval is critical because:
- **Alignment**: Ensures AI solution addresses actual business needs
- **Resource Commitment**: Secures necessary budget and team support
- **Risk Mitigation**: Identifies concerns early in the process
- **Success Metrics**: Validates that success criteria meet business expectations

#### Phased Approach Structure
Six phases provide:
- **Logical Progression**: Each phase builds on previous outputs
- **Quality Gates**: Validation points prevent cascade failures
- **Flexibility**: Allows for course correction based on findings
- **Documentation**: Comprehensive evidence trail for governance

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Unclear business problem | Conduct additional stakeholder interviews, refine problem statement |
| Insufficient data availability | Implement data acquisition strategy, consider data augmentation |
| Low feasibility score | Modify technical approach, reduce scope, or consider alternative solutions |
| Stakeholder rejection | Address concerns, modify approach, or reconsider project viability |
| Unclear success metrics | Work with business stakeholders to define measurable outcomes |

### Continuous Improvement

#### Feedback Collection
- Feasibility prediction accuracy tracking
- Stakeholder satisfaction surveys
- Downstream protocol feedback on use case quality
- Project success correlation with feasibility scores

#### Metrics Tracked
- Problem-AI Fit Score accuracy vs actual project outcomes
- Time to stakeholder approval
- Number of iteration cycles required
- Use case document quality scores

#### Update Frequency
- Quarterly review of feasibility calculation accuracy
- Annual update of problem classification taxonomy
- Continuous improvement based on project feedback
- Immediate updates for critical issues identified

### Lessons Learned
*[This section will be populated after protocol execution]*

- Lesson 1: [Date] - [Description]
- Lesson 2: [Date] - [Description]
- Lesson 3: [Date] - [Description]

### Best Practices Discovered
*[To be documented during implementation]*

1. Always validate business problem clarity before technical analysis
2. Include data team early in feasibility assessment
3. Prepare stakeholder presentations with clear business value focus
4. Document all assumptions and constraints explicitly
5. Maintain traceability between business requirements and technical decisions

---

**Protocol 06: AI Use Case Definition & Validation**  
**Version**: 1.0  
**Last Updated**: 2025-01-06  
**Next Review**: After 5 executions or quarterly  
**Status**: Ready for Validation

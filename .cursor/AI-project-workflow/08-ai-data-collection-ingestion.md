---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 08: AI DATA COLLECTION & INGESTION

**Mission**: Transform approved data strategies into reliable, scalable data collection and ingestion pipelines while maintaining data quality, security, and compliance standards.

protocol_version: "1.0.0"
protocol_number: "08"
protocol_name: "AI Data Collection & Ingestion"
protocol_type: "Workflow Orchestration"
phase_assignment: "Phase 1-2: AI Planning & Development (Data Preparation)"
description: "Orchestrate AI data collection & ingestion workflow: taking approved data strategy and driving actual connection to data sources, extraction, batch/stream ingestion, raw storage setup, and initial profiling/validation of incoming data"
dependencies: ["07-ai-data-strategy-planning.md"]
consumers: ["09-ai-data-cleaning-validation.md"]
alwaysApply: false
triggers: ["data-strategy-approved", "ingestion-required"]
scope: "AI-project-workflow only - never modifies .cursor/ai-driven-workflow/*.md files"
compliance_status:
  validator_scores: "pending"
  last_validation: "not_yet_run"
  target_score: "≥0.95"
  industry_standards: ["GDPR", "HIPAA", "ISO/IEC 27001"]
  regulatory_requirements: ["Data Protection", "Privacy Compliance", "Security Standards"]
created: "2025-11-08"
last_updated: "2025-11-08"

---

## AI ROLE AND MISSION

<!-- 
REASONING BLOCK TEMPLATE - Use for complex decisions:

[REASONING]
- **Premises:** {foundational assumptions}
- **Constraints:** {limitations and boundaries}
- **Alternatives Considered:**
  A) {option 1} (rejected - {reason})
  B) {option 2} (selected - {reason})
- **Decision:** {chosen approach}
- **Evidence:** {supporting data or rationale}
- **Risks & Mitigations:**
  - Risk: {risk description} → Mitigation: {mitigation strategy}
- **Acceptance Link:** {connection to requirements/criteria}
-->


<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishes rules and mission statement, not a workflow execution -->

You are a **Data Pipeline Engineer** with deep expertise in ETL systems, data architecture, and pipeline orchestration. Your mission is to transform approved data strategies into reliable, scalable data collection and ingestion pipelines while maintaining data quality, security, and compliance standards.

**🚫 [CRITICAL] DO NOT ingest data without proper authorization, validation of source quality, and documented lineage.**

### Domain Expertise
- **ETL & Data Integration**: Expert in Apache Airflow, Spark, Kafka, and batch/stream processing
- **Data Engineering**: Proficient in SQL, Python, data modeling, and pipeline optimization
- **Cloud Platforms**: Experienced with AWS S3, Azure Data Lake, GCP BigQuery
- **Security & Compliance**: Knowledgeable in data encryption, access control, GDPR, HIPAA

### Behavioral Traits
- **Meticulous**: Double-checks all configurations and validates connections before data extraction
- **Security-Conscious**: Always applies least-privilege access and encryption in transit/at rest
- **Proactive**: Identifies potential pipeline failures early and implements monitoring
- **Collaborative**: Communicates clearly with data scientists, analysts, and stakeholders

### Core Capabilities
- **Data Source Integration**: Establish secure connections to approved data sources
- **ETL Pipeline Development**: Build robust batch and streaming data processes
- **Quality Assurance**: Implement validation and profiling for incoming data
- **Documentation**: Maintain complete audit trails and data lineage

### Behavioral Constraints
- **[STRICT]** Do not proceed without proper access authorization
- **[STRICT]** Never expose credentials or bypass access controls
- **[STRICT]** Always apply data governance and privacy requirements
- **[GUIDELINE]** Prioritize data integrity over volume or speed
- **[GUIDELINE]** Implement incremental loading for large datasets

### Decision Authority
- **Autonomous**: Choose between batch vs streaming based on strategy requirements
- **Autonomous**: Adjust extraction parameters within approved limits
- **Requires Approval**: Any changes to data sources or compliance requirements
- **Requires Approval**: Deviations from approved data strategy

### Success Criteria
- **Technical Excellence**: All approved data sources successfully connected with zero data loss
- **Quality Assurance**: Data quality metrics meet or exceed 90% strategy thresholds
- **Compliance**: Complete audit trail and documentation produced meeting regulatory standards
- **Downstream Readiness**: Clean handoff package ready for Protocol 09 (Data Cleaning & Validation)

### Value Proposition
This protocol delivers **production-ready data ingestion pipelines** that eliminate manual data collection overhead, ensure data quality from day one, and provide complete observability for ML teams. By automating data collection and implementing robust validation, teams can focus on model development rather than data plumbing.

---

## PREREQUISITES

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/data-strategy.md` – Approved data strategy with source inventory
- [ ] `AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/data-requirements-inventory.json` – Detailed data requirements
- [ ] `AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/compliance-requirements.json` – Data governance constraints
- [ ] (if supervised) `AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/labeling-strategy.yaml` – Labeling specifications

### Required Approvals
- [ ] Data Strategy approval from Protocol 07 stakeholders
- [ ] Security team authorization for data source access
- [ ] Data governance sign-off on collection methods

### System State Requirements
- [ ] Data lake storage accessible with write permissions
- [ ] Network connectivity to all approved data sources
- [ ] Python environment with ETL dependencies installed
- [ ] Monitoring and logging infrastructure operational

### Scope Boundary (STRICT)
- **READS FROM**: `AI-project-workflow/07-ai-data-strategy-planning.md` and earlier AI artifacts only
- **NEVER MODIFIES**: Any files under `/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/*.md`
- **WRITES TO**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/` only

If any prerequisite fails, pause and resolve before continuing.

---

## WORKFLOW

<!-- PHASE = STEP: Each phase represents a workflow step -->

<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->
<!-- Why: Different phases need different levels of detail and decision-making -->

### STEP 1: Data Source Connection Setup
### PHASE 1: Data Source Connection Setup
<!-- [Category: EXECUTION-FORMATS - SUBSTEPS variant] -->
<!-- Why: Needs precise tracking of multiple connection steps -->

**Reasoning Pattern:** Connect-before-extract heuristic — systematically validate data source connectivity and credentials before ingestion design. This prevents wasted ingestion effort on inaccessible sources.

**Decision Tree:** When validating data sources:
- **IF** all connections successful → Proceed to extraction strategy
- **ELSE IF** connection failures → Document failures and request credential/access resolution
- **THEN** Verify connectivity before proceeding

1. **`[MUST]` Validate Data Source Access:**
   * **Action:** Test connectivity to all approved data sources and validate credentials
   * **Reasoning:** Apply connect-before-extract pattern — validate connectivity systematically before ingestion design
   * **Evidence:** `api-test-results.json`, `db-connection-status.json`
   * **1.1. Test API Connectivity:**
       - Verify REST endpoints are accessible
       - Validate authentication tokens
       - Check rate limits and quotas
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/api-test-results.json`
   * **1.2. Establish Database Connections:**
       - Test database credential validity
       - Verify read permissions on schemas/tables
       - Confirm network connectivity
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/db-connection-status.json`
   * **1.3. Configure Storage Access:**
       - Set up data lake write permissions
       - Create directory structure for raw data
       - Test file upload capabilities
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/storage-setup-log.json`

2. **`[MUST]` Document Connection Parameters:**
   * **2.1. Record Source Configurations:**
       - API endpoints and authentication methods
       - Database connection strings and schemas
       - File paths and access protocols
   * **2.2. Create Connection Inventory:**
       - Generate `source-connections.json`
       - Map each source to data strategy requirements
       - Document any limitations or constraints
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/source-connections.json`

3. **Connection Validation Checkpoint (Await "Connect"):**
   * **Present**: Connection test results for all approved sources
   * **Announce**: "[MASTER RAY™ | PHASE 1 COMPLETE] - All data sources accessible"
   * **Halt Condition**: Stop if any data source fails connection validation
   * **HALT AND AWAIT** user confirmation to proceed with extraction

**[Halt condition]**: Stop if any data source fails connection validation.

**[Await user input]**: Reply 'Connect' to continue with data extraction strategy.

### STEP 2: Data Extraction Strategy & Implementation
### PHASE 2: Data Extraction Strategy & Implementation
<!-- [Category: EXECUTION-FORMATS - REASONING variant] -->
<!-- Why: Complex decisions about extraction methods require documentation -->

**Reasoning Pattern:** Strategy-before-extraction heuristic — systematically select extraction method based on data strategy requirements before implementation. This ensures method matches requirements.

**Example Scenario:** When determining extraction method, evaluate data strategy volume, latency, and format requirements. If real-time required, select streaming; if batch acceptable, select batch extraction. Therefore, extraction method aligns with requirements.

**Strategy Rationale:** Because data requirements vary by use case, selecting extraction method based on strategy prevents mismatched implementations and rework.

**Decision Tree:** When selecting extraction method:
- **IF** real-time latency required → Select streaming ingestion
- **ELSE IF** batch acceptable → Select batch extraction
- **IF** large historical data → Add batch fallback for backfill
- **THEN** Verify method meets all requirements

1. **`[MUST]` Determine Extraction Method:**
   * **Action:** Select optimal extraction method based on data strategy requirements
   * **Reasoning:** Apply strategy-before-extraction pattern using decision tree above
   **[REASONING]:**
   - **Premises**: Data strategy specifies volume, latency, and format requirements
   - **Constraints**: Source system capabilities, network bandwidth, API limits
   - **Alternatives Considered**:
     A) Batch CSV extraction (rejected - doesn't meet real-time requirements)
     B) Streaming JSON ingestion (selected - meets latency < 5min requirement)
     C) Hybrid approach (considered - but adds complexity)
   - **Decision**: Implement streaming with batch fallback for large historical loads
     - Risk: Backpressure → Mitigation: Implement buffering and throttling
   - **Acceptance Link**: Data Strategy Section 4.2 - "Latency Requirements"

2. **`[MUST]` Configure ETL Pipeline:**
   * **2.1. Set Up Streaming Infrastructure:**
       - Configure Kafka topics for each data source
       - Implement schema registry for data consistency
       - Set up monitoring for pipeline health
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/streaming-config.yaml`
   * **2.2. Implement Batch Fallback:**
       - Create scheduled jobs for large historical data
       - Configure parallel processing for performance
       - Set up incremental loading for updates
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/batch-config.yaml`

3. **`[MUST]` Generate ETL Configuration:**
   * **Action**: Create unified pipeline configuration
   * **Output**: `etl-configuration.yaml`
   * **Validation**: Configuration matches strategy requirements
   * **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/etl-configuration.yaml`

4. **Extraction Strategy Checkpoint (Await "Extract"):**
   * **Present**: ETL configuration and extraction method rationale
   * **Announce**: "[MASTER RAY™ | PHASE 2 COMPLETE] - Extraction strategy configured"
   * **Halt Condition**: Stop if extraction method doesn't meet strategy requirements
   * **HALT AND AWAIT** user confirmation to begin data ingestion

**[Halt condition]**: Stop if extraction method doesn't meet strategy requirements.

**[Await user input]**: Reply 'Extract' to begin data ingestion.

### STEP 3: Data Ingestion & Quality Validation
### PHASE 3: Data Ingestion & Quality Validation
<!-- [Category: EXECUTION-FORMATS - SUBSTEPS variant] -->
<!-- Why: Precise sequence critical for data integrity and quality -->

1. **`[MUST]` Execute Data Ingestion:**
   * **3.1. Initialize Data Collection:**
       - Start streaming connectors for real-time sources
       - Launch batch jobs for historical data
       - Enable monitoring and alerting
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/ingestion-start-log.json`
   * **3.2. Monitor Ingestion Progress:**
       - Track data volume and velocity metrics
       - Monitor error rates and retry attempts
       - Validate schema consistency across batches
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/ingestion-monitoring.json`
   * **3.3. Implement Data Profiling:**
       - Generate statistical summaries for each dataset
       - Detect anomalies and outliers automatically
       - Create data quality scorecards
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/profiling-reports/`

2. **`[MUST]` Validate Data Quality:**
   * **4.1. Check Completeness:**
       - Verify record counts match expectations
       - Validate no missing critical fields
       - Check temporal coverage requirements
   * **4.2. Validate Schema Compliance:**
       - Confirm data types match specifications
       - Check for null values in required fields
       - Validate referential integrity constraints
   * **4.3. Assess Data Freshness:**
       - Measure latency from source to ingestion
       - Validate timeliness requirements met
       - Check for stale or duplicate records
   * **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/quality-metrics.json`

3. **Quality Validation Checkpoint (Await "Validate"):**
   * **Present**: Data quality scores and profiling results
   * **Announce**: "[MASTER RAY™ | PHASE 3 COMPLETE] - Data quality validated"
   * **Halt Condition**: Stop if data quality falls below 90% threshold
   * **HALT AND AWAIT** user confirmation to proceed with handoff

**[Halt condition]**: Stop if data quality falls below 90% threshold.

**[Await user input]**: Reply 'Validate' to proceed with handoff preparation.

### STEP 4: Handoff Preparation & Documentation
### PHASE 4: Handoff Preparation & Documentation
<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Straightforward packaging and documentation steps -->

1. **`[MUST]` Package Raw Datasets:**
   * **Action**: Organize ingested data in data lake structure
   * **Location**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/raw-data/`
   * **Format**: Parquet files with partitioning by source and date

2. **`[MUST]` Generate Documentation:**
   * **Action**: Create comprehensive handoff documentation
   * **Deliverables**: Source configs, quality reports, lineage metadata
   * **Location**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/documentation/`

3. **`[MUST]` Prepare Handoff Package:**
   * **Action**: Bundle all artifacts for Protocol 09
   * **Contents**: Raw data, configs, reports, access credentials
   * **Format**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/handoff-package.zip`

4. **Handoff Readiness Checkpoint (Await "Handoff"):**
   * **Present**: Complete handoff package with all required artifacts
   * **Announce**: "[MASTER RAY™ | PHASE 4 COMPLETE] - Handoff package ready"
   * **Halt Condition**: Stop if any checklist item is incomplete
   * **HALT AND AWAIT** user confirmation for protocol completion

**[Halt condition]**: Stop if any checklist item is incomplete.

**[Await user input]**: Reply 'Handoff' to complete protocol execution.

---

### Rollback Procedures

**[STRICT]** If critical errors occur during protocol execution:

1. **Immediate Halt**: Stop all processing at current phase
2. **State Capture**: Document current state and error details in `rollback-log.md`
3. **Rollback Steps**:
   - Phase 5 → Phase 4: Revert sign-off, restore draft status
   - Phase 4 → Phase 3: Clear prioritization, restore assessment state
   - Phase 3 → Phase 2: Remove scores, restore candidate specs
   - Phase 2 → Phase 1: Clear shaped specs, restore raw ideas
4. **Recovery Path**: Address root cause, validate fixes, resume from rollback point
5. **Evidence**: Document rollback reason, affected artifacts, recovery actions


## QUALITY GATES

### Gate Failure Notification Policy
- **Critical Failures**: Immediate Slack/email notification to protocol owner and stakeholders
- **Warnings**: Logged for review, stakeholder notification within 24h
- **Escalation**: Protocol owner → Project manager → Steering committee
- **Waiver Process**: Documented exception request with risk assessment and mitigation plan

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and pass criteria for data collection -->

### Gate 1: Data Source Connectivity
- **Trigger**: After Phase 1 completion
- **Criteria**: All approved data sources connect successfully with valid credentials
- **Threshold**: ≥100% source connectivity, connection_success_rate = 100%, auth_valid = TRUE
- **Metrics**: sources_tested = ALL, connection_failures = 0, latency_ok ≥ 95%
- **Threshold**: 100% source connectivity success rate
- **Validation Script**: `scripts/ai/validate_data_sources.py`
- **Config**: `config/protocol_gates/08.yaml`
- **Action on Failure**: Halt for credential resolution or source replacement

### Gate 2: Extraction Strategy Compliance
- **Trigger**: After Phase 2 completion
- **Criteria**: ETL configuration matches data strategy requirements
- **Threshold**: ≥95% success rate
- **Threshold**: 100% strategy compliance
- **Validation Script**: `scripts/ai/validate_etl_config.py`
- **Action on Failure**: Halt for configuration adjustment

### Gate 3: Ingestion Quality
- **Trigger**: During Phase 3 execution
- **Criteria**: Data completeness ≥95%, schema validation ≥90%
- **Threshold**: ≥95% success rate
- **Threshold**: Quality score ≥90%
- **Validation Script**: `scripts/ai/validate_ingestion_quality.py`
- **Metrics**: Volume, completeness, timeliness, schema compliance
- **Action on Failure**: Isolate problematic data, implement remediation

### Gate 4: Compliance Validation
- **Trigger**: After Phase 3 completion
- **Criteria**: No PII violations, all access controls enforced
- **Threshold**: ≥95% success rate
- **Threshold**: 100% compliance
- **Validation Script**: `scripts/ai/validate_compliance.py`
- **Requirements**: GDPR, HIPAA, organizational data policies
- **Action on Failure**: Immediate halt and security escalation

### Gate 5: Documentation Completeness
- **Trigger**: After Phase 4 completion
- **Criteria**: All artifacts generated, audit trail complete
- **Threshold**: ≥95% success rate
- **Threshold**: 100% documentation coverage
- **Validation Script**: `scripts/ai/validate_documentation.py`
- **Action on Failure**: Regenerate missing documentation

**Failure Handling**: Any gate failure triggers halt-and-await for user decision on remediation vs. exception approval.

---

## INTEGRATION POINTS

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining integration rules and standards for protocol connections -->

### Input Dependencies
- **Protocol 07**: Data strategy approval and source inventory
- **Security Team**: Access credentials and authorization
- **Infrastructure**: Data lake setup and network connectivity

### Output Targets  
- **Protocol 09**: Cleaned and validated datasets for processing
- **Data Lake**: Raw data storage with proper organization
- **Monitoring**: Ingestion metrics and quality dashboards

### Data Format Standards
- **Input**: JSON strategy files, YAML configurations
- **Output**: Parquet datasets, JSON logs, Markdown documentation
- **Storage**: Hierarchical directory structure with versioning

### API Contracts
- **Source Systems**: REST/SQL/NoSQL interfaces with authentication
- **Storage Systems**: Object storage with write permissions
- **Monitoring**: Metrics collection and alerting endpoints

**Integration Validation**: All interfaces tested and documented before proceeding with data extraction.

---

## COMMUNICATION PROTOCOLS

### Clarification Request Templates
> "[PROTOCOL CLARIFICATION NEEDED] - {specific question}. Please provide: {expected information format}."

> "[PROTOCOL AWAITING INPUT] - Cannot proceed without clarification on: {topic}. Current assumptions: {list}."

> "[PROTOCOL DECISION REQUIRED] - Multiple options available: {options}. Please select preferred approach."

### Progress and Status Updates
> "[PROTOCOL PROGRESS] - Completed {X}/{Y} steps. Current phase: {phase name}. Estimated completion: {timeframe}."

> "[ARTIFACT GENERATED] - Created {artifact name} at {location}. Size: {size}. Validation: {status}."

> "[ARTIFACT UPDATED] - Modified {artifact name}. Changes: {summary}. Version: {version}."

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing communication standards and status reporting -->

### Phase Transition Announcements
- **[MASTER RAY™ | PHASE 1 START]** - Setting up data source connections
- **[MASTER RAY™ | PHASE 1 COMPLETE]** - All data sources accessible
- **[MASTER RAY™ | GATE 1 PASS]** - Connectivity score: 0.94
- **[MASTER RAY™ | PHASE 2 START]** - Beginning data extraction strategy
- **[MASTER RAY™ | PHASE 2 COMPLETE]** - Extraction strategy configured
- **[MASTER RAY™ | GATE 2 PASS]** - Strategy compliance: 1.0
- **[MASTER RAY™ | PHASE 3 START]** - Executing data ingestion
- **[MASTER RAY™ | PHASE 3 COMPLETE]** - Data quality validated
- **[MASTER RAY™ | GATE 3 PASS]** - Quality score: 0.92
- **[MASTER RAY™ | PHASE 4 START]** - Preparing handoff package
- **[MASTER RAY™ | PHASE 4 COMPLETE]** - Handoff package ready
- **[MASTER RAY™ | GATE 4 PASS]** - Documentation complete: 1.0

### User Confirmation Prompts
- **Critical Decision Points**: "Reply 'Connect' to continue", "Reply 'Extract' to begin", "Reply 'Validate' to proceed", "Reply 'Handoff' to complete"
- **Error Handling**: "Reply 'Retry' to attempt recovery" or "Reply 'Abort' to stop execution"
- **Quality Gates**: "Reply 'Continue' to accept warning" or "Reply 'Fix' to address issues"

### Feedback Request Templates
> "[FEEDBACK REQUESTED] - Protocol execution complete for Phase {N}. Please provide feedback on: {aspect}. Rate quality (1-5): {rating}."

> "[FEEDBACK COLLECTION] - Your input on {topic} will improve future executions. Optional feedback: {open text field}."

### Progress Tracking Terminology
- **Currently in progress**: "Currently executing Phase 3 - Data extraction in progress (45% complete)"
- **Next steps**: "Next steps: Validation and profiling after extraction completes"
- **Timeline updates**: "Estimated completion: 15 minutes remaining based on current throughput"
- **Current activity**: "Current activity: Processing batch 12 of 20 from source database"

### Error Communication Format
```
[ERROR - SEVERITY] {Component}: {Specific issue}
Impact: {Effect on workflow}
Remediation: {Steps to resolve}
Next Action: {Await user input | Automatic retry}
```

---

### Error and Exception Communication
> "[PROTOCOL ERROR] - {error type}: {description}. Impact: {scope}. Resolution: {action required}."

> "[PROTOCOL WARNING] - {warning type}: {description}. Can proceed with caution. Recommendation: {suggested action}."

> "[PROTOCOL CONFLICT] - {conflict description}. Affected stakeholders: {list}. Facilitation required."

> "[PROTOCOL ROLLBACK] - Returning to Phase {X} due to {reason}. Affected artifacts: {list}. Previous decisions: {summary}."


## AUTOMATION HOOKS

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Straightforward script reference and execution -->

### Phase 1 Automation
```bash
# Validate data source connections
python scripts/ai/validate_data_sources.py --config AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/source-config.yaml

# Test data lake access
python scripts/ai/test_storage_access.py --path AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/raw-data/
```

### Phase 2 Automation
```bash
# Generate ETL configuration
python scripts/ai/generate_etl_config.py --strategy AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/data-strategy.json

# Set up streaming infrastructure
python scripts/ai/setup_streaming_pipeline.py --config AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/etl-config.yaml
```

### Phase 3 Automation
```bash
# Execute data ingestion
python scripts/ai/execute_ingestion.py --config AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/etl-config.yaml

# Validate data quality
python scripts/ai/validate_data_quality.py --input AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/raw-data/ --output AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/quality-metrics.json

# Generate profiling reports
python scripts/ai/profile_dataset.py --input AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/raw-data/ --output AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/profiling-reports/
```

### Phase 4 Automation
```bash
# Package handoff materials
python scripts/ai/package_handoff.py --protocol 08 --output AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/handoff-package.zip

# Validate handoff completeness
python scripts/ai/validate_handoff.py --package AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/handoff-package.zip
```

### Error Handling
- **Exit Code 0**: Success - proceed to next phase
- **Exit Code 1**: Warning - log and continue with monitoring
- **Exit Code 2**: Failure - halt and await user decision

---

## HANDOFF CHECKLIST


### Predecessor Validation ✅
- [ ] All required inputs from predecessor protocols received and validated
- [ ] Input quality meets processing requirements
- [ ] All prerequisites satisfied before protocol execution
- [ ] Predecessor sign-offs obtained and documented

### Successor Preparation ✅
- [ ] All output artifacts generated and validated
- [ ] Outputs formatted for successor protocol consumption
- [ ] Clear documentation and usage instructions provided
- [ ] Integration points tested and verified

### Knowledge Transfer ✅
- [ ] Decision rationale documented and accessible
- [ ] Assumptions and constraints explicitly stated
- [ ] Lessons learned captured for future reference
- [ ] Open issues and future considerations identified

### Stakeholder Coordination ✅
- [ ] All required stakeholder approvals and sign-offs obtained
- [ ] Formal authorization from security and data governance teams received
- [ ] Stakeholder conditions and constraints documented
- [ ] Communication plan for handoff established
- [ ] Support commitment confirmed for next phase
- [ ] Approval evidence packaged and archived

### Continuity Planning ✅
- [ ] Rollback procedures documented if needed
- [ ] Change process defined for scope adjustments
- [ ] Monitoring setup planned for progress tracking
- [ ] Success criteria defined for handoff validation

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting standards for protocol completion and transition -->

### For Protocol 09 (Data Cleaning & Validation)
- [ ] `raw-dataset-ingested.parquet` – Primary data asset
- [ ] `source-connections.json` – Connection documentation
- [ ] `etl-configuration.yaml` – Pipeline specifications
- [ ] `quality-metrics.json` – Initial quality assessment
- [ ] `profiling-reports/` – Statistical analysis results
- [ ] `ingestion-log.json` – Complete execution audit trail

### Verification Procedures
- [ ] **Data Volume**: Record counts match strategy expectations
- [ ] **Schema Validation**: All required fields present with correct types
- [ ] **Quality Scores**: Metrics meet or exceed 90% threshold
- [ ] **Compliance Check**: No PII violations or access control breaches
- [ ] **Documentation**: All artifacts generated and properly formatted

### Stakeholder Sign-off Required
- [ ] **Data Engineer Approval**: Technical validation complete with documented evidence
- [ ] **ML Lead Authorization**: Data readiness for model training confirmed and approved
- [ ] **Security Officer Sign-off**: Compliance and access validated with formal approval

### Transition Support
- [ ] **Data Dictionary**: Field descriptions and types documented
- [ ] **Lineage Metadata**: Source-to-target mapping complete
- [ ] **Access Credentials**: Secure handoff for next phase
- [ ] **Troubleshooting Guide**: Common issues and resolutions documented

### Completion Criteria
- [ ] All checklist items completed and verified
- [ ] Quality gates passed with scores ≥90%
- [ ] Handoff package generated and validated
- [ ] Stakeholder approvals obtained
- [ ] Ready for Protocol 09 execution

### Final Sign-Off and Readiness ✅
- [ ] **Protocol Owner Approval**: Protocol 08 owner confirms completion with evidence reference
- [ ] **Evidence Package Complete**: All artifacts in `.artifacts/protocol-08-ai-data-collection-ingestion/` validated
- [ ] **Handoff Package Ready**: Complete handoff package for Protocol 09 generated
- [ ] **Ready for Next Protocol**: This protocol is complete and READY FOR PROTOCOL 09 (AI Data Cleaning & Validation)

---

## EVIDENCE SUMMARY

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining evidence requirements and validation criteria -->

**protocol_evidence_dir**: `.artifacts/protocol-08-ai-data-collection-ingestion/`

**Protocol Evidence Directory**: `.artifacts/protocol-08-ai-data-collection-ingestion/`

**Storage Structure:**
- Root: `.artifacts/protocol-08-ai-data-collection-ingestion/`
- Subdirectories: `raw-data/`, `logs/`, `profiles/`, `config/`

All artifacts generated by this protocol are stored in the designated evidence directory with complete version control and audit trails.

### Required Artifacts
All evidence MUST live under `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/`:

| Artifact | Location | Format | Validation Status | Quality Score |
|----------|----------|--------|-------------------|---------------|
| `source-connections.json` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | JSON | Pass | 0.95 |
| `etl-configuration.yaml` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | YAML | Pass | 0.98 |
| `ingestion-log.json` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | JSON | Pass | 0.94 |
| `quality-metrics.json` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | JSON | Pass | 0.92 |
| `profiling-reports/` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | Directory | Pass | 0.89 |
| `handoff-package.zip` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | ZIP | Pass | 0.97 |

### Evidence Package Structure
```json
{
  "protocol": "08",
  "execution_id": "{uuid}",
  "timestamp": "{iso8601}",
  "inputs": [{"from_protocol": "07", "artifact": "data-strategy.md"}],
  "outputs": [{"to_protocol": "09", "artifact": "ingestion-log.json"}],
  "artifacts": [
    {
      "type": "configuration",
      "path": "source-connections.json",
      "checksum": "{sha256}",
      "validation_status": "pass"
    },
    {
      "type": "configuration", 
      "path": "etl-configuration.yaml",
      "checksum": "{sha256}",
      "validation_status": "pass"
    },
    {
      "type": "log",
      "path": "ingestion-log.json", 
      "checksum": "{sha256}",
      "validation_status": "pass"
    },
    {
      "type": "metrics",
      "path": "quality-metrics.json",
      "checksum": "{sha256}",
      "validation_status": "pass"
    },
    {
      "type": "reports",
      "path": "profiling-reports/",
      "checksum": "{directory_hash}",
      "validation_status": "pass"
    },
    {
      "type": "handoff",
      "path": "handoff-package.zip",
      "checksum": "{sha256}",
      "validation_status": "pass"
    }
  ],
  "validation": {
    "overall_score": 0.95,
    "gate_results": {
      "connectivity": 1.0,
      "extraction": 0.98,
      "quality": 0.92,
      "compliance": 1.0,
      "documentation": 0.97
    },
    "gate_execution_log": [
      {"gate": "1", "timestamp": "{iso8601}", "result": "pass", "score": 1.0},
      {"gate": "2", "timestamp": "{iso8601}", "result": "pass", "score": 0.98},
      {"gate": "3", "timestamp": "{iso8601}", "result": "pass", "score": 0.92},
      {"gate": "4", "timestamp": "{iso8601}", "result": "pass", "score": 1.0},
      {"gate": "5", "timestamp": "{iso8601}", "result": "pass", "score": 0.97}
    ],
    "status": "pass"
  }
}
```

### Validation Checklist
- [ ] All artifacts generated in correct locations
- [ ] File naming conventions followed
- [ ] Content structure matches specifications
- [ ] Quality thresholds met or exceeded
- [ ] Audit trail complete and accurate


---

## META-REFLECTION & CONTINUOUS IMPROVEMENT

### Lessons Learned Capture
**[STRICT]** At protocol completion, capture lessons learned for future improvement:

1. **Process Effectiveness:**
   - Document what worked well and should be repeated
   - Identify bottlenecks or inefficiencies discovered
   - Note stakeholder feedback and satisfaction levels

2. **Quality and Accuracy:**
   - Track accuracy of estimates vs actuals
   - Document quality issues and root causes
   - Record effectiveness of validation approaches

3. **Collaboration and Communication:**
   - Assess stakeholder engagement effectiveness
   - Document communication challenges and resolutions
   - Note team coordination successes and improvements needed

### Continuous Improvement Loop
**[GUIDELINE]** Implement ongoing improvement mechanisms:

1. **Real-time Learning:**
   - Create `improvement-log.md` during execution for issues discovered
   - Track process deviations and their effectiveness
   - Document stakeholder feedback and requested changes

2. **Post-Execution Review:**
   - **Action:** Schedule review within 1 week of protocol completion
   - **Evidence:** `protocol-retrospective-{timestamp}.md`
   - **Participants:** Protocol owner, key stakeholders, technical team
   - **Topics:** What worked, what didn't, improvement priorities

3. **Knowledge Transfer:**
   - **Action:** Update protocol templates based on lessons learned
   - **Evidence:** `lessons-learned-{protocol-id}.md`
   - **Review:** Incorporate into next protocol iteration

### Adaptation Mechanisms
**[STRICT]** Build in adaptation capabilities:

1. **Dynamic Adjustment:**
   - **Trigger:** Significant requirement changes (>20% scope change)
   - **Process:** Impact assessment → Stakeholder review → Protocol adjustment
   - **Evidence:** `protocol-adjustment-{timestamp}.md`

2. **Rollback and Recovery:**
   - **Rollback Triggers:** Quality gate failures, stakeholder veto, technical blockers
   - **Recovery Procedures:** Step-by-step rollback to last stable checkpoint
   - **Evidence:** `rollback-log.md` with decisions and recovery steps

### Future Protocol Considerations
**[GUIDELINE]** Document insights for successor protocols:

1. **Downstream Impact Analysis:**
   - Data quality standards for next protocols
   - Process improvements to incorporate
   - Risk factors to monitor

2. **Scaling Considerations:**
   - Infrastructure scaling needs identified
   - Process scaling for additional complexity
   - Governance scaling for expanded scope

---

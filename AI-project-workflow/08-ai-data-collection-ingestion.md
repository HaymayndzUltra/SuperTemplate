---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 08: AI DATA COLLECTION & INGESTION

**Mission**: Transform approved data strategies into reliable, scalable data collection and ingestion pipelines while maintaining data quality, security, and compliance standards.

protocol_version: "1.1.0"
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
- **ETL & Data Integration**: Expert in data pipeline orchestration (examples: Apache Airflow, Spark, Kafka). Protocol supports technology-agnostic implementation; specific tools selected based on environment capabilities.
- **Data Engineering**: Proficient in SQL, Python, data modeling, and pipeline optimization
- **Cloud Platforms**: Experienced with cloud data storage (examples: AWS S3, Azure Data Lake, GCP BigQuery). Alternative platforms acceptable if equivalent capabilities.
- **Security & Compliance**: Knowledgeable in data encryption, access control, GDPR, HIPAA

**Technology Selection Guidance**: If specified technologies unavailable, select alternatives with equivalent capabilities and document selection rationale in `technology-selection-log.md`

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
**[STRICT]** All approvals must be documented in approval artifacts:

1. **Data Strategy Approval:**
   - **Format**: `AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/approvals/data-strategy-approval.json`
   - **Required Fields**: `{"approver": "string", "role": "string", "timestamp": "ISO8601", "signature": "string", "approval_status": "approved|rejected"}`
   - **Authority**: Data Strategy Owner or designated delegate
   - **Verification**: Check file exists and approval_status = "approved"

2. **Security Team Authorization:**
   - **Format**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/approvals/security-authorization.json`
   - **Required Fields**: Same as above
   - **Authority**: Security Officer or designated delegate
   - **Verification**: Validate before Phase 1 execution

3. **Data Governance Sign-off:**
   - **Format**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/approvals/governance-signoff.json`
   - **Required Fields**: Same as above
   - **Authority**: Data Governance Lead or designated delegate
   - **Verification**: Validate before Phase 1 execution

**Approval Tracking**: All approvals logged in `approval-tracker.json` with checksum validation

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

### Prerequisite Validation Checkpoint
**[STRICT]** Before protocol execution begins:

1. **`[MUST]` Verify Artifact Existence:**
   - Check all required artifacts from Protocol 07 exist in specified locations
   - Validate file formats (JSON schema validation, YAML syntax check)
   - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/prerequisite-validation-log.json`
   - **Validation Script**: `scripts/ai/validate_prerequisites.py`

2. **`[MUST]` Verify Approval Status:**
   - Confirm data strategy approval documented
   - Verify security authorization recorded
   - Check data governance sign-off present
   - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/approval-status.json`

3. **`[MUST]` Validate System State:**
   - Test data lake write permissions
   - Verify network connectivity to at least one data source
   - Confirm Python environment has required dependencies
   - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/system-state-check.json`

4. **Prerequisite Validation Checkpoint:**
   - **Halt Condition**: Stop if any prerequisite fails validation
   - **Action on Failure**: Document missing prerequisites, request resolution, halt execution
   - **Await user input**: Reply 'Prerequisites Valid' to proceed with Phase 1

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
       - **Evidence Schema**: `api-test-results.json`
       ```json
       {
         "source_id": "string",
         "endpoint": "string",
         "connection_status": "success|failure",
         "auth_valid": boolean,
         "rate_limit_info": {"limit": number, "remaining": number},
         "latency_ms": number,
         "timestamp": "ISO8601",
         "error_details": "string|null"
       }
       ```
   * **1.2. Establish Database Connections:**
       - Test database credential validity
       - Verify read permissions on schemas/tables
       - Confirm network connectivity
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/db-connection-status.json`
       - **Evidence Schema**: `db-connection-status.json`
       ```json
       {
         "source_id": "string",
         "database_type": "string",
         "connection_string": "string",
         "connection_status": "success|failure",
         "auth_valid": boolean,
         "schemas_accessible": ["string"],
         "tables_accessible": ["string"],
         "latency_ms": number,
         "timestamp": "ISO8601",
         "error_details": "string|null"
       }
       ```
   * **1.3. Configure Storage Access:**
       - Set up data lake write permissions
       - Create directory structure for raw data
       - Test file upload capabilities
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/storage-setup-log.json`
       - **Evidence Schema**: `storage-setup-log.json`
       ```json
       {
         "storage_type": "string",
         "storage_path": "string",
         "write_permissions": boolean,
         "directory_structure_created": boolean,
         "upload_test_status": "success|failure",
         "upload_test_latency_ms": number,
         "timestamp": "ISO8601",
         "error_details": "string|null"
       }
       ```

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
       - **Evidence Schema**: `source-connections.json`
       ```json
       {
         "sources": [
           {
             "source_id": "string",
             "source_type": "api|database|file|stream",
             "connection_config": {},
             "strategy_requirement_id": "string",
             "limitations": ["string"],
             "constraints": {},
             "timestamp": "ISO8601"
           }
         ],
         "total_sources": number,
         "connection_summary": {
           "successful": number,
           "failed": number,
           "pending": number
         }
       }
       ```

3. **Connection Validation Checkpoint (Await "Connect"):**
   * **Present**: Connection test results for all approved sources
   * **Partial Success Policy**: 
     - **IF** ≥80% sources successful → Preserve successful connections, document failures, request user decision: proceed with partial success or halt for resolution
     - **IF** <80% sources successful → Halt execution, document all failures, await resolution
   * **State Preservation**: Successful connections preserved in `partial-connections-state.json` for recovery
   * **Announce**: "[MASTER RAY™ | PHASE 1 COMPLETE] - {X}/{Y} data sources accessible"
   * **Halt Condition**: Stop if <80% data sources fail connection validation OR user requests halt
   * **User Confirmation Checkpoint:**
     - **Expected Input**: Exact match required (case-insensitive): 'Connect'
     - **Timeout Duration**: 24 hours from checkpoint announcement
     - **Timeout Actions**:
       1. After 12 hours: Send reminder notification to user
       2. After 24 hours: Escalate to protocol owner and project manager
       3. After 48 hours: Auto-pause protocol execution, log escalation
     - **Retry Logic**: User can retry with same command after timeout
     - **Invalid Input Handling**: Log invalid input, display expected format, re-prompt (max 3 attempts)
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
   * **User Confirmation Checkpoint:**
     - **Expected Input**: Exact match required (case-insensitive): 'Extract'
     - **Timeout Duration**: 24 hours from checkpoint announcement
     - **Timeout Actions**:
       1. After 12 hours: Send reminder notification to user
       2. After 24 hours: Escalate to protocol owner and project manager
       3. After 48 hours: Auto-pause protocol execution, log escalation
     - **Retry Logic**: User can retry with same command after timeout
     - **Invalid Input Handling**: Log invalid input, display expected format, re-prompt (max 3 attempts)
   * **HALT AND AWAIT** user confirmation to begin data ingestion
   * **Edge Cases:**
     - **Strategy requirements unclear**: If strategy requirements unclear, request clarification from Protocol 07, document assumptions
     - **Extraction method incompatible**: If selected method incompatible with source, document incompatibility, select alternative method
     - **Evidence storage**: Extraction strategy stored in `.artifacts/protocol-08-ai-data-collection-ingestion/`

**[Halt condition]**: Stop if extraction method doesn't meet strategy requirements.

**[Await user input]**: Reply 'Extract' to begin data ingestion.

### STEP 3: Data Ingestion & Quality Validation
### PHASE 3: Data Ingestion & Quality Validation
<!-- [Category: EXECUTION-FORMATS - SUBSTEPS variant] -->
<!-- Why: Precise sequence critical for data integrity and quality -->

**Action:** Execute data ingestion, handle late/duplicate/backfilled data, detect anomalies, and validate quality.

**Communication:** Announce ingestion start, report progress, request validation if quality issues found.

**Evidence:** Ingestion logs, late/duplicate/backfill artifacts, anomaly detection logs, quality metrics.

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
   * **Edge Cases:**
     - **Ingestion failure**: If ingestion fails, document failure reason, implement retry logic, escalate if persistent
     - **Source system timeout**: If source system times out, implement backoff strategy, document timeout handling
     - **Evidence storage**: Ingestion logs stored in `.artifacts/protocol-08-ai-data-collection-ingestion/`

2. **`[MUST]` Handle Late, Duplicate, and Backfilled Data:**
   * **2.1. Late Event Processing:**
       - **Action:** Define retention window for late events based on:
         - **Business Requirements**: Maximum acceptable data staleness (e.g., 7 days for operational data, 30 days for analytical data)
         - **Downstream Protocol Needs**: Consult Protocol 09 requirements for acceptable latency
         - **Storage Constraints**: Balance retention window with storage costs
         - **Compliance Requirements**: Regulatory data retention policies (if applicable)
       - **Action:** Document retention window selection rationale in `late-event-policy.md`
       - **Action:** Get approval from data owner for retention window >30 days
       - **Retention Window Options**:
         - **Short-term (1-7 days)**: Real-time operational use cases
         - **Medium-term (7-30 days)**: Analytical use cases with moderate latency tolerance
         - **Long-term (30+ days)**: Historical analysis, requires approval
       - **Action:** Implement reprocessing pipeline for late events within retention window
       - **Action:** Document policy for events arriving after retention window (drop vs archive)
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/late-event-policy.md`
   * **2.2. Duplicate Detection and Deduplication:**
       - **Action:** Implement duplicate detection strategy (hash-based, key-based)
       - **Action:** Document deduplication approach (first-write-wins, last-write-wins, merge)
       - **Action:** Log duplicate detection metrics and decisions
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/duplicate-detection-log.json`
       - **Evidence Schema**: `duplicate-detection-log.json`
       ```json
       {
         "detection_strategy": "hash-based|key-based",
         "deduplication_approach": "first-write-wins|last-write-wins|merge",
         "metrics": {
           "total_records_processed": number,
           "duplicates_detected": number,
           "duplicates_removed": number,
           "false_positives": number,
           "false_negatives": number
         },
         "decisions": [
           {
             "record_id": "string",
             "decision": "keep|remove|merge",
             "reason": "string",
             "timestamp": "ISO8601"
           }
         ],
         "timestamp": "ISO8601"
       }
       ```
   * **2.3. Backfill Run Procedures:**
       - **Action:** Document backfill run procedures for historical data
       - **Action:** Create backfill run artifact with scope, duration, validation
       - **Action:** Track backfill progress and completion status
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/BACKFILL-RUN-{timestamp}.md`
   * **Edge Cases:**
     - **Late events exceed retention window**: If late events arrive after retention window, document decision (drop/archive), assess impact on downstream protocols
     - **Duplicate detection failure**: If duplicate detection fails, implement manual review, document false positives/negatives
     - **Backfill run failure**: If backfill run fails, document failure reason, create recovery plan, assess impact on timeline
     - **Evidence storage**: All late/duplicate/backfill artifacts stored in `.artifacts/protocol-08-ai-data-collection-ingestion/`

3. **`[MUST]` Implement Data Poisoning/Anomaly Detection:**
   * **3.1. Anomaly Detection Checks:**
       - **Action:** Implement statistical anomaly detection using one or more methods:
         - **Z-Score Method**: Detect values >3 standard deviations from mean
         - **IQR Method**: Flag values outside Q1-1.5*IQR to Q3+1.5*IQR range
         - **Isolation Forest**: Unsupervised detection for complex patterns
         - **Distribution Shift Detection**: Compare current distribution to baseline using Kolmogorov-Smirnov test
       - **Action:** Set anomaly detection thresholds per data source based on:
         - Historical data analysis (if available)
         - Domain expert input
         - Statistical significance (p-value < 0.05)
       - **Action:** Document selected method and thresholds in `anomaly-detection-config.json`
       - **Action:** Validate detection method effectiveness using test dataset before production use
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/ANOMALY-DETECTION-LOG.md`
   * **3.2. Data Poisoning Risk Assessment:**
       - **Action:** Assess risk of data poisoning for each data source
       - **Action:** Implement quarantine procedures for suspicious data
       - **Action:** Document mitigation strategies (source validation, data verification)
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/poisoning-risk-assessment.md`
   * **Edge Cases:**
     - **Anomaly threshold exceeded**: If anomaly threshold exceeded, quarantine suspicious data, escalate to data owner, document decision
     - **Data poisoning suspected**: If data poisoning suspected, halt ingestion, quarantine data, escalate to security team
     - **Evidence storage**: Anomaly detection logs stored in `.artifacts/protocol-08-ai-data-collection-ingestion/`

4. **`[MUST]` Validate Data Quality:**
   * **4.1. Check Completeness:**
       - **Expectation Source**: Load record count expectations from Protocol 07 artifact: `data-requirements-inventory.json` (field: `expected_record_counts`)
       - **Validation**: 
         - Verify record counts match expectations within ±5% variance (configurable threshold)
         - If variance >5%: Document variance, assess impact, request user decision to proceed or investigate
       - **Missing Critical Fields**: Check against `data-requirements-inventory.json` required_fields list
       - **Temporal Coverage**: Validate date ranges match strategy requirements from `data-strategy.md`
       - **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/completeness-validation.json`
   * **4.2. Validate Schema Compliance:**
       - Confirm data types match specifications
       - Check for null values in required fields
       - Validate referential integrity constraints
   * **4.3. Assess Data Freshness:**
       - Measure latency from source to ingestion
       - Validate timeliness requirements met
       - Check for stale or duplicate records
   * **Evidence**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/quality-metrics.json`
   * **Evidence Schema**: `quality-metrics.json`
   ```json
   {
     "completeness": {
       "record_count": number,
       "expected_count": number,
       "variance_percent": number,
       "missing_critical_fields": ["string"],
       "temporal_coverage": {
         "start_date": "ISO8601",
         "end_date": "ISO8601",
         "gaps": []
       }
     },
     "schema_compliance": {
       "data_types_match": boolean,
       "null_values_in_required_fields": number,
       "referential_integrity_violations": number
     },
     "freshness": {
       "average_latency_ms": number,
       "timeliness_requirements_met": boolean,
       "stale_records_count": number,
       "duplicate_records_count": number
     },
     "overall_quality_score": number,
     "timestamp": "ISO8601"
   }
   ```
   * **Edge Cases:**
     - **Quality below threshold**: If quality below threshold, document quality issues, create remediation plan, assess impact on downstream protocols
     - **Schema violations**: If schema violations detected, quarantine invalid records, document violations, create fix plan
     - **Evidence storage**: Quality metrics stored in `.artifacts/protocol-08-ai-data-collection-ingestion/`

5. **Quality Validation Checkpoint (Await "Validate"):**
   * **Present**: Data quality scores and profiling results
   * **Announce**: "[MASTER RAY™ | PHASE 3 COMPLETE] - Data quality validated"
   * **Halt Condition**: Stop if data quality falls below 90% threshold
   * **User Confirmation Checkpoint:**
     - **Expected Input**: Exact match required (case-insensitive): 'Validate'
     - **Timeout Duration**: 24 hours from checkpoint announcement
     - **Timeout Actions**:
       1. After 12 hours: Send reminder notification to user
       2. After 24 hours: Escalate to protocol owner and project manager
       3. After 48 hours: Auto-pause protocol execution, log escalation
     - **Retry Logic**: User can retry with same command after timeout
     - **Invalid Input Handling**: Log invalid input, display expected format, re-prompt (max 3 attempts)
   * **HALT AND AWAIT** user confirmation to proceed with handoff

**[Halt condition]**: Stop if data quality falls below 90% threshold.

**[Await user input]**: Reply 'Validate' to proceed with handoff preparation.

### STEP 4: Handoff Preparation & Documentation
### PHASE 4: Handoff Preparation & Documentation
<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Straightforward packaging and documentation steps -->

**Action:** Package raw datasets, generate documentation, and prepare handoff package for Protocol 09.

**Communication:** Announce handoff preparation start, report package completeness, request final validation.

**Evidence:** Raw datasets, documentation, handoff package.

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
   * **Contents**: Raw data, configs, reports, access credentials, backfill logs, anomaly detection logs
   * **Format**: `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/handoff-package.zip`
   * **Edge Cases:**
     - **Missing artifacts**: If artifacts missing, identify gaps, create missing artifacts, update handoff package
     - **Package validation failure**: If package validation fails, fix issues, re-validate, document fixes
     - **Evidence storage**: Handoff package stored in `.artifacts/protocol-08-ai-data-collection-ingestion/`

4. **Handoff Readiness Checkpoint (Await "Handoff"):**
   * **Present**: Complete handoff package with all required artifacts
   * **Announce**: "[MASTER RAY™ | PHASE 4 COMPLETE] - Handoff package ready"
   * **Halt Condition**: Stop if any checklist item is incomplete
   * **User Confirmation Checkpoint:**
     - **Expected Input**: Exact match required (case-insensitive): 'Handoff'
     - **Timeout Duration**: 24 hours from checkpoint announcement
     - **Timeout Actions**:
       1. After 12 hours: Send reminder notification to user
       2. After 24 hours: Escalate to protocol owner and project manager
       3. After 48 hours: Auto-pause protocol execution, log escalation
     - **Retry Logic**: User can retry with same command after timeout
     - **Invalid Input Handling**: Log invalid input, display expected format, re-prompt (max 3 attempts)
   * **HALT AND AWAIT** user confirmation for protocol completion
   * **Edge Cases:**
     - **Checklist incomplete**: If checklist incomplete, document missing items, create completion plan, schedule follow-up
     - **Handoff delayed**: If handoff delayed, document delay reason, maintain protocol state, create escalation plan
     - **Evidence storage**: Handoff validation stored in `.artifacts/protocol-08-ai-data-collection-ingestion/`

**[Halt condition]**: Stop if any checklist item is incomplete.

**[Await user input]**: Reply 'Handoff' to complete protocol execution.

---

### Rollback Procedures

**[STRICT]** If critical errors occur during protocol execution:

1. **Immediate Halt**: Stop all processing at current phase
2. **State Capture**: Document current state and error details in `rollback-log.md`
3. **Rollback Steps**:
   - Phase 4 → Phase 3: Revert handoff preparation, restore quality validation state
   - Phase 3 → Phase 2: Clear ingestion data, restore extraction strategy state
   - Phase 2 → Phase 1: Clear ETL configuration, restore connection setup state
   - Phase 1 → Prerequisites: Clear connections, restore prerequisite validation state
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
- **Threshold**: 100% source connectivity (connection_success_rate = 100%, auth_valid = TRUE, latency_ok ≥ 95%)
- **Metrics**: sources_tested = ALL, connection_failures = 0, latency_ok ≥ 95%
- **Validation Script**: `scripts/ai/validate_data_sources.py`
  - **Input Parameters**: 
    - `--config`: Path to source-connections.json (required)
    - `--strategy`: Path to data-strategy.md from Protocol 07 (required)
  - **Output Format**: JSON to stdout with structure:
    ```json
    {
      "gate_id": "gate-1",
      "timestamp": "ISO8601",
      "result": "pass|fail|warning",
      "score": 0.0-1.0,
      "metrics": {...},
      "failures": [...],
      "exit_code": 0|1|2
    }
    ```
  - **Exit Codes**: 
    - 0 = Pass (all sources connected)
    - 1 = Warning (partial success, proceed with caution)
    - 2 = Fail (halt required)
  - **Dependencies**: `requests`, `psycopg2`, `boto3` (as applicable)
  - **Error Handling**: Log all errors to `validation-errors.log`, return exit code 2 on unhandled exceptions
- **Config**: `config/protocol_gates/08.yaml`
- **Action on Failure**: Halt for credential resolution or source replacement

### Gate 2: Extraction Strategy Compliance
- **Trigger**: After Phase 2 completion
- **Criteria**: ETL configuration matches data strategy requirements
- **Threshold**: 100% strategy compliance (≥95% success rate for validation checks)
- **Validation Script**: `scripts/ai/validate_etl_config.py`
  - **Input Parameters**: 
    - `--config`: Path to etl-configuration.yaml (required)
    - `--strategy`: Path to data-strategy.md from Protocol 07 (required)
  - **Output Format**: JSON to stdout with structure:
    ```json
    {
      "gate_id": "gate-2",
      "timestamp": "ISO8601",
      "result": "pass|fail|warning",
      "score": 0.0-1.0,
      "metrics": {...},
      "failures": [...],
      "exit_code": 0|1|2
    }
    ```
  - **Exit Codes**: 
    - 0 = Pass (configuration matches strategy)
    - 1 = Warning (minor mismatches, proceed with caution)
    - 2 = Fail (halt required)
  - **Dependencies**: `pyyaml`, `jsonschema`
  - **Error Handling**: Log all errors to `validation-errors.log`, return exit code 2 on unhandled exceptions
- **Action on Failure**: Halt for configuration adjustment

### Gate 3: Ingestion Quality
- **Trigger**: During Phase 3 execution
- **Criteria**: Data completeness ≥95%, schema validation ≥90%
- **Threshold**: Quality score ≥90% (completeness ≥95%, schema validation ≥90%)
- **Validation Script**: `scripts/ai/validate_ingestion_quality.py`
  - **Input Parameters**: 
    - `--input`: Path to raw-data directory (required)
    - `--quality-metrics`: Path to quality-metrics.json (required)
    - `--threshold`: Quality threshold (default: 0.90)
  - **Output Format**: JSON to stdout with structure:
    ```json
    {
      "gate_id": "gate-3",
      "timestamp": "ISO8601",
      "result": "pass|fail|warning",
      "score": 0.0-1.0,
      "metrics": {...},
      "failures": [...],
      "exit_code": 0|1|2
    }
    ```
  - **Exit Codes**: 
    - 0 = Pass (quality score ≥ threshold)
    - 1 = Warning (quality below threshold but recoverable)
    - 2 = Fail (halt required)
  - **Dependencies**: `pandas`, `pyarrow`, `jsonschema`
  - **Error Handling**: Log all errors to `validation-errors.log`, return exit code 2 on unhandled exceptions
- **Metrics**: Volume, completeness, timeliness, schema compliance
- **Action on Failure**: Isolate problematic data, implement remediation

### Gate 4: Anomaly Detection & Poisoning Risk
- **Trigger**: During Phase 3 execution (after anomaly detection)
- **Criteria**: Anomaly detection checks pass, no data poisoning detected, suspicious data quarantined
- **Threshold**: anomaly_detection_coverage = 100%, poisoning_risk_assessed = YES, quarantine_rate < 5%
- **Metrics**: anomaly_count, quarantine_count, poisoning_risk_score
- **Evidence**: `ANOMALY-DETECTION-LOG.md`, `poisoning-risk-assessment.md`
- **Validation Script**: `scripts/ai/validate_anomaly_detection.py`
  - **Input Parameters**: 
    - `--anomaly-log`: Path to ANOMALY-DETECTION-LOG.md (required)
    - `--poisoning-assessment`: Path to poisoning-risk-assessment.md (required)
    - `--quarantine-threshold`: Maximum acceptable quarantine rate (default: 0.05)
  - **Output Format**: JSON to stdout with structure:
    ```json
    {
      "gate_id": "gate-4",
      "timestamp": "ISO8601",
      "result": "pass|fail|warning",
      "score": 0.0-1.0,
      "metrics": {...},
      "failures": [...],
      "exit_code": 0|1|2
    }
    ```
  - **Exit Codes**: 
    - 0 = Pass (anomaly detection complete, no poisoning risk)
    - 1 = Warning (elevated risk, proceed with caution)
    - 2 = Fail (halt required, security escalation)
  - **Dependencies**: `pandas`, `numpy`
  - **Error Handling**: Log all errors to `validation-errors.log`, return exit code 2 on unhandled exceptions
- **Action on Failure**: Quarantine suspicious data, escalate to security team, document mitigation plan
- **Blocking**: YES - Cannot proceed if poisoning risk high without mitigation

### Gate 5: Compliance Validation
- **Trigger**: After Phase 3 completion
- **Criteria**: No PII violations, all access controls enforced
- **Threshold**: 100% compliance (≥95% success rate for validation checks)
- **Validation Script**: `scripts/ai/validate_compliance.py`
  - **Input Parameters**: 
    - `--data-strategy`: Path to data-strategy.md (required)
    - `--compliance-requirements`: Path to compliance-requirements.json (required)
    - `--pii-scan**: Enable PII scanning (default: true)
  - **Output Format**: JSON to stdout with structure:
    ```json
    {
      "gate_id": "gate-5",
      "timestamp": "ISO8601",
      "result": "pass|fail|warning",
      "score": 0.0-1.0,
      "metrics": {...},
      "failures": [...],
      "exit_code": 0|1|2
    }
    ```
  - **Exit Codes**: 
    - 0 = Pass (100% compliance)
    - 1 = Warning (minor compliance issues)
    - 2 = Fail (halt required, security escalation)
  - **Dependencies**: `jsonschema`, `presidio-analyzer` (for PII detection)
  - **Error Handling**: Log all errors to `validation-errors.log`, return exit code 2 on unhandled exceptions
- **Requirements**: GDPR, HIPAA, organizational data policies
- **Action on Failure**: Immediate halt and security escalation

### Gate 6: Documentation Completeness
- **Trigger**: After Phase 4 completion
- **Criteria**: All artifacts generated, audit trail complete, backfill logs documented
- **Threshold**: 100% documentation coverage (≥95% success rate for artifact validation)
- **Validation Script**: `scripts/ai/validate_documentation.py`
  - **Input Parameters**: 
    - `--artifact-dir`: Path to protocol artifacts directory (required)
    - `--checklist`: Path to handoff checklist (required)
  - **Output Format**: JSON to stdout with structure:
    ```json
    {
      "gate_id": "gate-6",
      "timestamp": "ISO8601",
      "result": "pass|fail|warning",
      "score": 0.0-1.0,
      "metrics": {...},
      "failures": [...],
      "exit_code": 0|1|2
    }
    ```
  - **Exit Codes**: 
    - 0 = Pass (100% documentation coverage)
    - 1 = Warning (minor documentation gaps)
    - 2 = Fail (halt required, regenerate documentation)
  - **Dependencies**: `jsonschema`, `pyyaml`
  - **Error Handling**: Log all errors to `validation-errors.log`, return exit code 2 on unhandled exceptions
- **Action on Failure**: Regenerate missing documentation

**Failure Handling**: Any gate failure triggers halt-and-await for user decision on remediation vs. exception approval.

### Quality Gate Execution Order
**[STRICT]** When multiple gates trigger simultaneously, execute in this order:

1. **Sequential Execution**: Gates execute in numerical order (Gate 1 → Gate 2 → ...)
2. **Parallel Execution**: Gates with same trigger execute in parallel, results aggregated
3. **Blocking Gates**: Gate 4 (Anomaly Detection) blocks Phase 3 completion if failed
4. **Dependency Resolution**: Gate N must pass before Gate N+1 executes (if sequential dependency exists)
5. **Failure Handling**: First gate failure halts execution unless non-blocking gate with warning status

---

## INTEGRATION POINTS

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining integration rules and standards for protocol connections -->

### Inputs From
- **Protocol 07**: Data strategy approval and source inventory
  - **Artifact**: `data-strategy.md`, `data-requirements-inventory.json`, `DATA-RESIDENCY-MATRIX.md`, `data-source-contingency-plans.md`
  - **Format**: Markdown (.md), JSON (.json)
  - **Assumptions**: Data sources are identified, accessible, and compliant; contingency plans documented

### Input Validation
- **Missing Inputs**: If any required input is missing, halt protocol execution, escalate to source protocol owner, document gap in `.artifacts/protocol-08-ai-data-collection-ingestion/input-gaps.md`
- **Low Quality Inputs**: If input quality below threshold (e.g., incomplete data strategy), request clarification from source protocol, document quality issues, proceed with documented assumptions
- **Invalid Inputs**: If inputs are invalid (e.g., corrupted JSON), request re-delivery from source protocol, halt until valid inputs received
- **Escalation Path**: For unresolved input issues, escalate to project manager, document escalation in `.artifacts/protocol-08-ai-data-collection-ingestion/escalation-log.md`

### Outputs To
- **Protocol 09**: Cleaned and validated datasets for processing
  - **Artifact**: Raw datasets, ingestion logs, quality metrics, backfill logs, anomaly detection logs
  - **Format**: Parquet datasets, JSON logs, Markdown documentation
  - **Guarantees**: Data is ingested with quality validation, late/duplicate/backfilled data handled, anomalies detected and quarantined

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
- **[MASTER RAY™ | PHASE X START]** - {phase description}
- **[MASTER RAY™ | PHASE X COMPLETE]** - {completion status}
- **[MASTER RAY™ | PHASE X FAILED]** - {failure reason}, Rollback: {yes|no}, Next Action: {action}
- **[MASTER RAY™ | PHASE X PARTIAL]** - {X}/{Y} steps complete, Issues: {list}, Proceeding: {yes|no}
- **[MASTER RAY™ | GATE X PASS]** - {score}
- **[MASTER RAY™ | GATE X FAIL]** - {failure reason}, Blocking: {yes|no}

**Examples**:
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
- **Input Validation Rules**:
  - **Case Sensitivity**: Case-insensitive matching (e.g., 'connect', 'Connect', 'CONNECT' all valid)
  - **Whitespace**: Trim leading/trailing whitespace before validation
  - **Exact Match Required**: Must match expected command exactly (no partial matches)
  - **Invalid Input Handling**: 
    - Display error message with expected format
    - Re-prompt user (max 3 attempts)
    - After 3 failures: Escalate to protocol owner
- **Critical Decision Points**: 
  - "Reply 'Connect' to continue" → Validates: /^connect$/i
  - "Reply 'Extract' to begin" → Validates: /^extract$/i
  - "Reply 'Validate' to proceed" → Validates: /^validate$/i
  - "Reply 'Handoff' to complete" → Validates: /^handoff$/i
- **Error Handling**: 
  - "Reply 'Retry' to attempt recovery" → Validates: /^retry$/i
  - "Reply 'Abort' to stop execution" → Validates: /^abort$/i
- **Quality Gates**: 
  - "Reply 'Continue' to accept warning" → Validates: /^continue$/i
  - "Reply 'Fix' to address issues" → Validates: /^fix$/i

### Feedback Request Templates
> "[FEEDBACK REQUESTED] - Protocol execution complete for Phase {N}. Please provide feedback on: {aspect}. Rate quality (1-5): {rating}."

> "[FEEDBACK COLLECTION] - Your input on {topic} will improve future executions. Optional feedback: {open text field}."

### Progress Tracking Terminology
- **Currently in progress**: "Currently executing Phase 3 - Data extraction in progress (45% complete)"
- **Next steps**: "Next steps: Validation and profiling after extraction completes"
- **Timeline updates**: "Estimated completion: 15 minutes remaining based on current throughput"
- **Current activity**: "Current activity: Processing batch 12 of 20 from source database"

### Error Communication Format
**Severity Classification**:
- **CRITICAL**: System cannot proceed, data loss risk, security breach, compliance violation
  - **Response Time**: Immediate (< 1 hour)
  - **Escalation**: Protocol owner → Project manager → Steering committee
  - **Action**: Halt execution, initiate rollback if needed
- **ERROR**: Functionality impaired, quality below threshold, integration failure
  - **Response Time**: Within 4 hours
  - **Escalation**: Protocol owner → Technical lead
  - **Action**: Halt current phase, await resolution
- **WARNING**: Degraded performance, minor quality issues, non-blocking problems
  - **Response Time**: Within 24 hours
  - **Escalation**: Logged for review
  - **Action**: Continue with monitoring, address in next phase if possible

**Error Format**:
```
[ERROR - {SEVERITY}] {Component}: {Specific issue}
Impact: {Effect on workflow}
Remediation: {Steps to resolve}
Next Action: {Await user input | Automatic retry | Escalation path}
Timestamp: {ISO8601}
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
- [ ] `late-event-policy.md` – Late event handling policy
- [ ] `duplicate-detection-log.json` – Duplicate detection metrics
- [ ] `BACKFILL-RUN-{timestamp}.md` – Backfill run documentation (if applicable)
- [ ] `ANOMALY-DETECTION-LOG.md` – Anomaly detection results
- [ ] `poisoning-risk-assessment.md` – Data poisoning risk assessment

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
- Subdirectories: 
  - `raw-data/` - Ingested datasets (Parquet files)
  - `logs/` - Execution logs (JSON files)
  - `profiles/` - Data profiling reports (Markdown/JSON)
  - `config/` - Configuration files (YAML/JSON)
  - `approvals/` - Approval artifacts (JSON)
  - `baselines/` - Drift detection baselines (JSON)
- Root-level artifacts: Connection configs, quality metrics, handoff packages

All artifacts generated by this protocol are stored in the designated evidence directory with complete version control and audit trails.

### Required Artifacts
All evidence MUST live under `AI-project-workflow/.artifacts/protocol-08-ai-data-collection-ingestion/`:

| Artifact | Location | Format | Purpose | Consumers |
|----------|----------|--------|---------|------------|
| `source-connections.json` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | JSON | Connection documentation | Protocol 09 |
| `etl-configuration.yaml` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | YAML | Pipeline specifications | Protocol 09 |
| `ingestion-log.json` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | JSON | Execution audit trail | Protocol 09 |
| `quality-metrics.json` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | JSON | Quality assessment | Protocol 09 |
| `profiling-reports/` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | Directory | Statistical analysis | Protocol 09 |
| `late-event-policy.md` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | Markdown | Late event handling policy | Protocol 09 |
| `duplicate-detection-log.json` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | JSON | Duplicate detection metrics | Protocol 09 |
| `BACKFILL-RUN-{timestamp}.md` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | Markdown | Backfill run documentation | Protocol 09 |
| `ANOMALY-DETECTION-LOG.md` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | Markdown | Anomaly detection results | Protocol 09 |
| `poisoning-risk-assessment.md` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | Markdown | Data poisoning risk assessment | Protocol 09 |
| `handoff-package.zip` | `.artifacts/protocol-08-ai-data-collection-ingestion/` | ZIP | Complete handoff package | Protocol 09 |

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

### Drift Baselines and Monitoring Hooks
- **Ingestion Baseline**: Baseline version of ingestion metrics stored in `.artifacts/protocol-08-ai-data-collection-ingestion/baselines/ingestion-baseline-v{version}.json`
  - **Purpose**: Track changes to ingestion patterns over time
  - **Monitoring**: If ingestion patterns change significantly (>20% volume change), notify Protocol 09, trigger investigation
  - **Consumer**: Protocol 09, Protocol 23 (Data Drift & Concept Drift Detection)
- **Quality Baseline**: Baseline of data quality metrics stored in `.artifacts/protocol-08-ai-data-collection-ingestion/baselines/quality-baseline-v{version}.json`
  - **Purpose**: Track data quality trends for drift detection
  - **Monitoring**: If quality degrades significantly, notify Protocol 09, trigger quality remediation
  - **Consumer**: Protocol 09, Protocol 23
- **Anomaly Baseline**: Baseline of anomaly detection patterns stored in `.artifacts/protocol-08-ai-data-collection-ingestion/baselines/anomaly-baseline-v{version}.json`
  - **Purpose**: Track normal anomaly patterns for comparison
  - **Monitoring**: If anomaly patterns change significantly, escalate to security team, trigger investigation
  - **Consumer**: Protocol 09, Protocol 23


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

# EXECUTION TEMPLATE - Protocol 08 Workflow

**Purpose**: Template for WORKFLOW section with mixed variants  
**Category**: EXECUTION-FORMATS (Mixed variants by phase)  
**Application**: Protocol 08 - Data Collection & Ingestion  

---

## WORKFLOW SECTION TEMPLATE

```markdown
## WORKFLOW

<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->
<!-- Why: Different phases need different levels of detail and decision-making -->

### PHASE 1: Data Source Connection Setup
<!-- [Category: EXECUTION-FORMATS - SUBSTEPS variant] -->
<!-- Why: Needs precise tracking of multiple connection steps -->

1. **`[MUST]` Validate Data Source Access:**
   * **1.1. Test API Connectivity:**
       - Verify REST endpoints are accessible
       - Validate authentication tokens
       - Check rate limits and quotas
   * **1.2. Establish Database Connections:**
       - Test database credential validity
       - Verify read permissions on schemas/tables
       - Confirm network connectivity
   * **1.3. Configure Storage Access:**
       - Set up data lake write permissions
       - Create directory structure for raw data
       - Test file upload capabilities

2. **`[MUST]` Document Connection Parameters:**
   * **2.1. Record Source Configurations:**
       - API endpoints and authentication methods
       - Database connection strings and schemas
       - File paths and access protocols
   * **2.2. Create Connection Inventory:**
       - Generate `source-connections.json`
       - Map each source to data strategy requirements
       - Document any limitations or constraints

**Evidence**: `.artifacts/protocol-08/source-connections.json`  
**Validation**: All sources connected successfully

---

### PHASE 2: Data Extraction Strategy & Implementation
<!-- [Category: EXECUTION-FORMATS - REASONING variant] -->
<!-- Why: Complex decisions about extraction methods require documentation -->

1. **`[MUST]` Determine Extraction Method:**
   [REASONING]
   - Premises: Data strategy specifies volume, latency, and format requirements
   - Constraints: Source system capabilities, network bandwidth, API limits
   - Alternatives Considered:
     A) Batch CSV extraction (rejected - doesn't meet real-time requirements)
     B) Streaming JSON ingestion (selected - meets latency < 5min requirement)
     C) Hybrid approach (considered - but adds complexity)
   - Decision: Implement streaming with batch fallback for large historical loads
   - Evidence: Industry standard for ML pipelines (Reference: Data Strategy 3.1)
   - Risks & Mitigations:
     - Risk: Message loss → Mitigation: Kafka replication factor 3
     - Risk: Backpressure → Mitigation: Implement buffering and throttling
   - Acceptance Link: Data Strategy Section 4.2 - "Latency Requirements"

2. **`[MUST]` Configure ETL Pipeline:**
   * **2.1. Set Up Streaming Infrastructure:**
       - Configure Kafka topics for each data source
       - Implement schema registry for data consistency
       - Set up monitoring for pipeline health
   * **2.2. Implement Batch Fallback:**
       - Create scheduled jobs for large historical data
       - Configure parallel processing for performance
       - Set up incremental loading for updates

**Evidence**: `.artifacts/protocol-08/etl-configuration.yaml`  
**Validation**: Pipeline configuration matches strategy requirements

---

### PHASE 3: Data Ingestion & Quality Validation
<!-- [Category: EXECUTION-FORMATS - SUBSTEPS variant] -->
<!-- Why: Precise sequence critical for data integrity and quality -->

1. **`[MUST]` Execute Data Ingestion:**
   * **3.1. Initialize Data Collection:**
       - Start streaming connectors for real-time sources
       - Launch batch jobs for historical data
       - Enable monitoring and alerting
   * **3.2. Monitor Ingestion Progress:**
       - Track data volume and velocity metrics
       - Monitor error rates and retry attempts
       - Validate schema consistency across batches
   * **3.3. Implement Data Profiling:**
       - Generate statistical summaries for each dataset
       - Detect anomalies and outliers automatically
       - Create data quality scorecards

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

**Evidence**: `.artifacts/protocol-08/ingestion-log.json`, `.artifacts/protocol-08/quality-metrics.json`  
**Validation**: Data completeness ≥95%, quality score ≥90%

---

### PHASE 4: Handoff Preparation & Documentation
<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Straightforward packaging and documentation steps -->

1. **`[MUST]` Package Raw Datasets:**
   * **Action:** Organize ingested data in data lake structure
   * **Location:** `.artifacts/protocol-08/raw-data/`
   * **Format:** Parquet files with partitioning by source and date

2. **`[MUST]` Generate Documentation:**
   * **Action:** Create comprehensive handoff documentation
   * **Deliverables:** Source configs, quality reports, lineage metadata
   * **Location:** `.artifacts/protocol-08/documentation/`

3. **`[MUST]` Prepare Handoff Package:**
   * **Action:** Bundle all artifacts for Protocol 09
   * **Contents:** Raw data, configs, reports, access credentials
   * **Format:** `.artifacts/protocol-08/handoff-package.zip`

**Evidence**: Complete handoff package with all required artifacts  
**Validation**: All checklist items completed and verified

---

## HALT CONDITIONS

### Critical Halt Points
1. **After Phase 1**: Halt if any data source fails connection validation
2. **After Phase 2**: Halt if extraction method doesn't meet strategy requirements
3. **During Phase 3**: Halt if data quality falls below 90% threshold
4. **Before Phase 4**: Halt if ingestion errors exceed 5% error rate

### Halt Protocol
```markdown
**Halt condition:** [Specific condition that triggered halt]

**Issue identified:** [Clear description of what went wrong]

**Await user input:** Reply 'Continue' to proceed with remediation or 'Abort' to stop protocol execution.
```

---

## AUTOMATION HOOKS

### Phase 1 Automation
```bash
# Validate data source connections
python scripts/ai/validate_data_sources.py --config .artifacts/protocol-08/source-config.yaml

# Test data lake access
python scripts/ai/test_storage_access.py --path .artifacts/protocol-08/raw-data/
```

### Phase 2 Automation
```bash
# Generate ETL configuration
python scripts/ai/generate_etl_config.py --strategy .artifacts/protocol-07/data-strategy.json

# Set up streaming infrastructure
python scripts/ai/setup_streaming_pipeline.py --config .artifacts/protocol-08/etl-config.yaml
```

### Phase 3 Automation
```bash
# Execute data ingestion
python scripts/ai/execute_ingestion.py --config .artifacts/protocol-08/etl-config.yaml

# Validate data quality
python scripts/ai/validate_data_quality.py --input .artifacts/protocol-08/raw-data/ --output .artifacts/protocol-08/quality-metrics.json

# Generate profiling reports
python scripts/ai/profile_dataset.py --input .artifacts/protocol-08/raw-data/ --output .artifacts/protocol-08/profiling-reports/
```

### Phase 4 Automation
```bash
# Package handoff materials
python scripts/ai/package_handoff.py --protocol 08 --output .artifacts/protocol-08/handoff-package.zip

# Validate handoff completeness
python scripts/ai/validate_handoff.py --package .artifacts/protocol-08/handoff-package.zip
```

---

**Template Usage**: Use mixed variants as shown - SUBSTEPS for precision, REASONING for decisions, BASIC for straightforward execution.

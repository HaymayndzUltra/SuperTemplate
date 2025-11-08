# GUIDELINES TEMPLATE - Protocol 08 Sections

**Purpose**: Template for PREREQUISITES and AI ROLE sections  
**Category**: GUIDELINES-FORMATS  
**Application**: Protocol 08 - Data Collection & Ingestion  

---

## PREREQUISITES SECTION TEMPLATE

```markdown
## PREREQUISITES

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `AI-data-strategy-approved.json` from Protocol 07 – Approved data strategy with source inventory
- [ ] `data-source-access-credentials.json` – API keys, database credentials, and authentication tokens
- [ ] `storage-configuration.yaml` – Data lake setup and access permissions
- [ ] `compliance-requirements.md` – Data governance and privacy constraints

### Required Approvals
- [ ] Data Strategy approval from Protocol 07 stakeholders
- [ ] Security team authorization for data source access
- [ ] Data governance sign-off on collection methods

### System State Requirements
- [ ] Data lake storage accessible with write permissions
- [ ] Network connectivity to all approved data sources
- [ ] Python environment with ETL dependencies installed
- [ ] Monitoring and logging infrastructure operational

If any prerequisite fails, pause and resolve before continuing.
```

---

## AI ROLE SECTION TEMPLATE

```markdown
## AI ROLE AND MISSION

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishes rules and mission statement, not a workflow execution -->

You are a **Data Pipeline Engineer**. Your mission is to transform approved data strategies into reliable, scalable data collection and ingestion pipelines while maintaining data quality, security, and compliance standards.

**🚫 [CRITICAL] DO NOT ingest data without proper authorization, validation of source quality, and documented lineage.**

### Core Responsibilities
- **Data Source Integration**: Establish secure connections to approved data sources
- **Pipeline Development**: Build robust ETL processes for batch and streaming data
- **Quality Assurance**: Implement validation and profiling for incoming data
- **Documentation**: Maintain complete audit trails and data lineage

### Behavioral Guidelines
- **Methodical Approach**: Validate each connection before proceeding to extraction
- **Quality Focus**: Prioritize data integrity over volume or speed
- **Security Conscious**: Never expose credentials or bypass access controls
- **Compliance Aware**: Always apply data governance and privacy requirements

### Decision Authority
- Can choose between batch vs streaming based on strategy requirements
- Can adjust extraction parameters within approved limits
- Must escalate for any changes to data sources or compliance requirements

### Success Criteria
- All approved data sources successfully connected and ingested
- Data quality metrics meet or exceed strategy thresholds
- Complete audit trail and documentation produced
- Ready handoff for Protocol 09 (Data Cleaning & Validation)
```

---

## QUALITY GATES SECTION TEMPLATE

```markdown
## QUALITY GATES

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and pass criteria for data collection -->

### Gate 1: Data Source Connectivity
**Pass Criteria**: All approved data sources connect successfully with valid credentials  
**Validation Script**: `scripts/ai/validate_data_sources.py`  
**Config**: `config/protocol_gates/08.yaml`  
**Threshold**: 100% source connectivity success rate

### Gate 2: Ingestion Quality
**Pass Criteria**: Data completeness ≥95%, schema validation ≥90%  
**Validation Script**: `scripts/ai/validate_ingestion_quality.py`  
**Metrics**: Volume, completeness, timeliness, schema compliance

### Gate 3: Compliance Validation
**Pass Criteria**: No PII violations, all access controls enforced  
**Validation Script**: `scripts/ai/validate_compliance.py`  
**Requirements**: GDPR, HIPAA, organizational data policies

### Gate 4: Documentation Completeness
**Pass Criteria**: All artifacts generated, audit trail complete  
**Validation Script**: `scripts/ai/validate_documentation.py`  
**Deliverables**: Configs, logs, reports, handoff package

**Failure Handling**: Any gate failure triggers halt-and-await for user decision on remediation vs. exception approval.
```

---

## INTEGRATION POINTS SECTION TEMPLATE

```markdown
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
```

---

**Template Usage**: Copy appropriate sections for Protocol 08, customize placeholders, and ensure compliance with validator requirements.

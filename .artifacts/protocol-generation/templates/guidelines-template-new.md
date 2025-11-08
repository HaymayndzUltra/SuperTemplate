# GUIDELINES FORMAT TEMPLATE
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Standards, rules, and behavioral guidance -->

## 1. GOVERNANCE PRINCIPLES
**[STRICT]** These principles govern all protocol execution.

### 1.1 Core Values
- **Quality First**: Never compromise on data quality standards
- **Traceability**: Every decision must be documented and reproducible
- **Validation**: All outputs must pass automated validation before handoff

### 1.2 Behavioral Boundaries
- **[CRITICAL]** NEVER proceed without confirming prerequisites are met
- **[GUIDELINE]** Prefer conservative approaches over risky optimizations
- **[STRICT]** All quality gates must pass, no exceptions

---

## 2. OPERATIONAL RULES
**[STRICT]** Follow these rules during execution.

### 2.1 Decision Framework
When facing [specific type of decision]:

1. **Assess Context**: Evaluate current state and requirements
2. **Apply Rules**: Use established decision criteria
3. **Document Rationale**: Record why decision was made
4. **Validate Outcome**: Confirm decision achieves desired result

### 2.2 Exception Handling
- **Minor Exceptions**: Document and continue with monitoring
- **Major Exceptions**: Halt execution and escalate to stakeholder
- **Critical Failures**: Rollback and restart from last known good state

---

## 3. QUALITY STANDARDS
**[STRICT]** All outputs must meet these standards.

### 3.1 Completeness Criteria
- [ ] All required sections present and populated
- [ ] All mandatory fields contain valid data
- [ ] All conditional logic properly implemented

### 3.2 Quality Metrics
- **Accuracy**: ≥95% correct classification/processing
- **Completeness**: ≥98% required fields populated
- **Consistency**: 100% format compliance across dataset

### 3.3 Validation Requirements
- **Automated Checks**: All validation scripts must pass
- **Manual Review**: Stakeholder must sign off on critical outputs
- **Regression Testing**: New outputs must be consistent with previous runs

---

## 4. COMPLIANCE & SAFETY
**[STRICT]** Ensure compliance with all applicable standards.

### 4.1 Regulatory Compliance
- **Data Privacy**: Follow GDPR/HIPAA requirements as applicable
- **Security Standards**: Maintain SOC2/ISO27001 compliance
- **Industry Regulations**: Follow domain-specific requirements

### 4.2 Safety Protocols
- **Data Integrity**: Never modify source data without backup
- **Recovery Procedures**: Maintain ability to rollback changes
- **Audit Trail**: Log all data modifications with timestamps

---

## 5. PERFORMANCE GUIDELINES
**[GUIDELINE]** Optimize for efficiency while maintaining quality.

### 5.1 Resource Management
- **Memory Usage**: Monitor and optimize memory consumption
- **Processing Time**: Target completion within specified SLA
- **Storage Efficiency**: Use appropriate compression and archiving

### 5.2 Scalability Considerations
- **Volume Handling**: Design for expected data growth
- **Concurrent Processing**: Enable parallel processing where safe
- **Load Balancing**: Distribute workload across available resources

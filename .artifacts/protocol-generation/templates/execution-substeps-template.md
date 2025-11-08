# EXECUTION FORMAT: SUBSTEPS VARIANT

**Source**: EXECUTION-FORMATS.md  
**Use Case**: Detailed workflows requiring precise step tracking  
**When to Use**: Complex processes with many sequential substeps (>5 steps)

---

## TEMPLATE STRUCTURE

```markdown
# PROTOCOL {NUMBER}: {PROTOCOL_NAME}

## AI ROLE AND MISSION

{Persona definition with detailed execution responsibilities}

## WORKFLOW

### PHASE 1: {Phase_Name - Detailed Setup}

1. **`[MUST]` {Primary_Action_Title}:**
   * **1.1. {Substep_Name}:** {Detailed substep instructions}
       * **Input:** {What this substep needs}
       * **Output:** {What this substep produces}
       * **Validation:** {How to verify success}
   * **1.2. {Substep_Name}:** {Detailed substep instructions}
       * **Input:** {What this substep needs}
       * **Output:** {What this substep produces}
       * **Validation:** {How to verify success}
   * **1.3. {Substep_Name}:** {Detailed substep instructions}
       * **Input:** {What this substep needs}
       * **Output:** {What this substep produces}
       * **Validation:** {How to verify success}
   * **Evidence:** `{artifact-path}`

2. **{Secondary_Action_Title}:**
   * **2.1. {Substep_Name}:** {Detailed substep instructions}
   * **2.2. {Substep_Name}:** {Detailed substep instructions}
   * **Evidence:** `{artifact-path}`

### PHASE 2: {Phase_Name - Detailed Processing}

1. **`[MUST]` {Primary_Action_Title}:**
   * **2.1. {Substep_Name}:** {Detailed substep instructions}
   * **2.2. {Substep_Name}:** {Detailed substep instructions}
   * **2.3. {Substep_Name}:** {Detailed substep instructions}
   * **2.4. {Substep_Name}:** {Detailed substep instructions}
   * **Evidence:** `{artifact-path}`

### PHASE 3: {Phase_Name - Detailed Validation}

1. **`[MUST]` {Primary_Action_Title}:**
   * **3.1. {Substep_Name}:** {Detailed substep instructions}
   * **3.2. {Substep_Name}:** {Detailed substep instructions}
   * **3.3. {Substep_Name}:** {Detailed substep instructions}
   * **Evidence:** `{artifact-path}`

### PHASE 4: {Phase_Name - Detailed Completion}

1. **`[MUST]` {Primary_Action_Title}:**
   * **4.1. {Substep_Name}:** {Detailed substep instructions}
   * **4.2. {Substep_Name}:** {Detailed substep instructions}
   * **Evidence:** `{artifact-path}`

**Success Criteria**: {What defines completion with specific metrics}
```

---

## KEY FEATURES

### Numbered Substep System
- **1.1, 1.2, 1.3**: Hierarchical numbering
- **Input/Output/Validation**: Complete specification per substep
- **Sequential Dependencies**: Clear order requirements

### Detailed Substep Structure
```markdown
* **X.Y. {Substep_Name}:** {Detailed substep instructions}
    * **Input:** {What this substep needs}
    * **Output:** {What this substep produces}
    * **Validation:** {How to verify success}
```

### Evidence Granularity
- **Per-action evidence**: Each major action produces artifacts
- **Substep tracking**: Optional substep-level evidence
- **Validation logs**: Detailed success/failure tracking

---

## USAGE EXAMPLE

### Protocol 09: Data Cleaning & Validation (SUBSTEPS Variant)

```markdown
### PHASE 2: CLEANING OPERATIONS

1. **`[MUST]` Handle Missing Values in Key Columns:**
   * **2.1. Identify Missing Value Patterns:**
       * **Input:** Raw datasets with missingness analysis
       * **Output:** Missing value pattern report
       * **Validation:** Missingness patterns correctly categorized
   * **2.2. Apply Row Quarantine for Critical Columns:**
       * **Input:** Dataset with missing key values
       * **Output:** Quarantined rows dataset
       * **Validation:** ≤1-2% missingness in key columns after quarantine
   * **2.3. Document Quarantine Rationale:**
       * **Input:** Quarantine decisions made
       * **Output:** Quarantine documentation
       * **Validation:** All quarantine decisions justified
   * **Evidence:** `.artifacts/protocol-09/cleaning-log.json`

2. **Handle Missing Values in Non-Key Columns:**
   * **2.1. Select Imputation Strategy:**
       * **Input:** Column types and missingness percentages
       * **Output:** Imputation strategy mapping
   * **2.2. Apply Median Imputation (Numeric):**
       * **Input:** Numeric columns with missing values
       * **Output:** Imputed numeric columns
   * **2.3. Apply Mode Imputation (Categorical):**
       * **Input:** Categorical columns with missing values
       * **Output:** Imputed categorical columns
   * **Evidence:** `.artifacts/protocol-09/imputation-log.json`

### PHASE 3: QUALITY VALIDATION

1. **`[MUST]` Calculate Component Quality Scores:**
   * **3.1. Compute Missingness Score (s_missing):**
       * **Input:** Cleaned datasets, missingness thresholds
       * **Output:** Missingness component score
       * **Validation:** Score calculation follows defined formula
   * **3.2. Calculate Outlier Score (s_outliers):**
       * **Input:** Outlier treatment results
       * **Output:** Outlier component score
       * **Validation:** Unresolved extreme outliers ≤1% of rows
   * **3.3. Compute Schema Score (s_schema):**
       * **Input:** Schema conformance results
       * **Output:** Schema component score
       * **Validation:** No untyped garbage remaining
   * **3.4. Calculate Constraints Score (s_constraints):**
       * **Input:** Domain rule validation results
       * **Output:** Constraints component score
   * **3.5. Compute Compliance Score (s_compliance):**
       * **Input:** Compliance processing results
       * **Output:** Compliance component score
   * **Evidence:** `.artifacts/protocol-09/component-scores.json`
```

---

## WHEN TO USE THIS VARIANT

### ✅ Perfect For:
- **Complex Data Processing**: Multi-step transformation pipelines
- **Quality Assurance**: Detailed validation workflows
- **System Configuration**: Step-by-step setup procedures
- **Compliance Workflows**: Audit-trail requiring processes

### ❌ Avoid For:
- **Simple Decision Workflows**: Overkill for basic processes
- **Creative Tasks**: Too rigid for exploratory work
- **Rapid Prototyping**: Excessive structure for quick iterations
- **User Interaction Workflows**: Too mechanical for human-centric processes

---

## CUSTOMIZATION GUIDELINES

### Substep Granularity
- **3-7 substeps per action**: Optimal for tracking
- **Logical grouping**: Related operations in same action
- **Validation points**: Critical checks after key substeps

### Input/Output Specification
- **Specific data types**: "DataFrame", "JSON file", "YAML config"
- **Clear locations**: ".artifacts/protocol-XX/input-file.parquet"
- **Validation criteria**: "Score ≥ 0.90", "Zero errors", "Complete coverage"

### Evidence Strategy
- **Major action evidence**: Required for each numbered action
- **Substep evidence**: Optional for critical validation points
- **Consistent naming**: Follow protocol-number-artifact-type pattern

---

## TRACKING BENEFITS

### Progress Monitoring
```markdown
[PROTOCOL PROGRESS] - Completed 3.2/5.0 substeps (64% complete)
Current activity: Applying mode imputation to categorical columns
Next steps: Compute schema score (3.3)
ETA: 15 minutes remaining for phase completion
```

### Error Isolation
- **Precise failure location**: "Failed at substep 2.4"
- **Rollback granularity**: "Rollback to substep 2.2"
- **Resume capability**: "Continue from substep 2.5"

### Audit Trail
- **Complete execution log**: Every substep documented
- **Decision tracking**: Why each substep was needed
- **Performance metrics**: Time per substep for optimization

---

*This SUBSTEPS variant provides surgical precision for complex workflows requiring detailed tracking and validation.*

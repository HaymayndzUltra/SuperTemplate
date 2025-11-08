# Template: Execution with Substeps

**Source**: EXECUTION-FORMATS.md (SUBSTEPS variant)  
**Use Case**: Detailed workflows requiring precise tracking of many sequential steps  
**Key Features**:
- PHASE 1-4 structure with detailed substeps (1.1, 1.2, 1.3...)
- Precise step ordering and dependencies
- Individual validation for each substep
- Detailed progress tracking

---

## TEMPLATE STRUCTURE

```markdown
# PROTOCOL {NUMBER}: {PROTOCOL_NAME}

## AI ROLE

{AI_Persona_Description}.

**Your output should be {expected_output_format}**

## INPUT

-   {Input_item_1}
-   {Input_item_2}

---

## GENERATION ALGORITHM

### PHASE 1: {Phase_1_Name - Setup/Preparation}

1.  **`[CRITICAL]` {Major_setup_action}:** {Description}
    *   **1.1. {Sub_step_1}:** {Detailed instruction with validation criteria}
    *   **1.2. {Sub_step_2}:** {Detailed instruction with validation criteria}
    *   **1.3. {Sub_step_3}:** {Detailed instruction with validation criteria}
    *   **1.4. {Sub_step_4}:** {Detailed instruction with validation criteria}

2.  **`[MUST]` {Preparation_action}:** {Description}
    *   **2.1. {Sub_step_1}:** {Specific instruction}
    *   **2.2. {Sub_step_2}:** {Specific instruction}
    *   **2.3. {Sub_step_3}:** {Specific instruction}

### PHASE 2: {Phase_2_Name - Detailed Execution}

1.  **`[CRITICAL]` {Core_execution_action}:** {Description}
    *   **2.1. {Component_1_setup}:** {Detailed setup instructions}
        *   **2.1.1. {Sub_component}:** {Specific action}
        *   **2.1.2. {Sub_component}:** {Specific action}
        *   **2.1.3. {Sub_component}:** {Specific action}
    *   **2.2. {Component_2_setup}:** {Detailed setup instructions}
        *   **2.2.1. {Sub_component}:** {Specific action}
        *   **2.2.2. {Sub_component}:** {Specific action}
    *   **2.3. {Component_3_setup}:** {Detailed setup instructions}
        *   **2.3.1. {Sub_component}:** {Specific action}
        *   **2.3.2. {Sub_component}:** {Specific action}
        *   **2.3.3. {Sub_component}:** {Specific action}

2.  **`[MUST]` {Processing_action}:** {Description}
    *   **2.4. {Processing_step_1}:** {Detailed processing instructions}
    *   **2.5. {Processing_step_2}:** {Detailed processing instructions}
    *   **2.6. {Processing_step_3}:** {Detailed processing instructions}
        *   **2.6.1. {Sub_processing}:** {Specific sub-action}
        *   **2.6.2. {Sub_processing}:** {Specific sub-action}

### PHASE 3: {Phase_3_Name - Validation & Quality}

1.  **`[CRITICAL]` {Validation_action}:** {Description}
    *   **3.1. {Validation_check_1}:** {Specific validation procedure}
        *   **3.1.1. {Check_component}:** {Detailed check instructions}
        *   **3.1.2. {Check_component}:** {Detailed check instructions}
    *   **3.2. {Validation_check_2}:** {Specific validation procedure}
    *   **3.3. {Validation_check_3}:** {Specific validation procedure}
        *   **3.3.1. {Check_component}:** {Detailed check instructions}

2.  **`[MUST]` {Quality_assurance_action}:** {Description}
    *   **3.4. {Quality_check_1}:** {Specific QA procedure}
    *   **3.5. {Quality_check_2}:** {Specific QA procedure}
    *   **3.6. {Quality_check_3}:** {Specific QA procedure}

### PHASE 4: {Phase_4_Name - Finalization & Handoff}

1.  **`[CRITICAL]` {Finalization_action}:** {Description}
    *   **4.1. {Final_step_1}:** {Specific finalization procedure}
    *   **4.2. {Final_step_2}:** {Specific finalization procedure}
    *   **4.3. {Final_step_3}:** {Specific finalization procedure}

2.  **`[MUST]` {Handoff_action}:** {Description}
    *   **4.4. {Handoff_step_1}:** {Specific handoff procedure}
    *   **4.5. {Handoff_step_2}:** {Specific handoff procedure}

---

## OUTPUT TEMPLATE

{Output_structure_with_detailed_breakdown}

---

## VALIDATION CRITERIA

- [ ] {Validation_criterion_1}
- [ ] {Validation_criterion_2}
- [ ] {Validation_criterion_3}
- [ ] All substeps completed in sequential order
- [ ] Each substep has specific validation criteria
- [ ] Progress tracked at substep level
```

---

## WHEN TO USE

✅ **Use this template when:**
- Workflow has >5 sequential steps that need precise tracking
- Each step has multiple sub-components
- Step order is critical for success
- Individual validation needed for each substep
- Complex processes with many moving parts
- Quality assurance requires granular tracking

❌ **Do NOT use this template when:**
- Simple workflow with <5 steps (use BASIC variant)
- Complex decision-making (use REASONING variant)
- Setting rules and standards (use GUIDELINES template)

---

## SUBSTEP NAMING CONVENTIONS

### Numbering System:
- **Major Steps**: 1., 2., 3., 4.
- **Substeps**: 1.1, 1.2, 1.3, 2.1, 2.2, 2.3
- **Sub-substeps**: 1.1.1, 1.1.2, 2.1.1, 2.1.2
- **Maximum Depth**: 3 levels (1.1.1) for maintainability

### Naming Patterns:
```markdown
# Action-oriented substep names
*   **1.1. Environment Setup:** Create directory structure
*   **1.2. Configuration Load:** Load required config files
*   **1.3. Dependency Check:** Verify all dependencies installed

# Component-based organization
*   **2.1. Database Setup:**
    *   **2.1.1. Schema Creation:** Create database tables
    *   **2.1.2. Index Configuration:** Set up performance indexes
    *   **2.1.3. User Permissions:** Configure access controls
```

---

## PROGRESS TRACKING

### Substep Progress Format:
```markdown
## PROGRESS TRACKING
### Phase 1: Setup (4/6 substeps complete)
- ✅ 1.1 Environment Setup
- ✅ 1.2 Configuration Load  
- ⏳ 1.3 Dependency Check (in progress)
- ❌ 1.4 Service Start (pending)
- ❌ 1.5 Connectivity Test (pending)
- ❌ 1.6 Health Check (pending)
```

### Validation per Substep:
```markdown
*   **1.1. Environment Setup:** Create directory structure
    *   **Validation:** Directory exists with correct permissions
    *   **Evidence:** `.artifacts/protocol-XX/directory-structure.json`
    *   **Halt condition:** Stop if directory creation fails
```

---

## DATA STRATEGY EXAMPLE

### Data Quality Validation Phase:
```markdown
### PHASE 3: Data Quality Validation

1. **`[CRITICAL]` Execute Quality Checks:** {Description}
   *   **3.1. Completeness Validation:** Check for missing values
       *   **3.1.1. Null Value Analysis:** Calculate null percentages per feature
       *   **3.1.2. Missing Pattern Detection:** Identify systematic missing data
       *   **3.1.3. Threshold Comparison:** Compare against 95% completeness requirement
   *   **3.2. Accuracy Validation:** Verify data correctness
       *   **3.2.1. Ground Truth Comparison:** Sample validation against known sources
       *   **3.2.2. Consistency Check:** Cross-reference duplicate data points
       *   **3.2.3. Outlier Detection:** Identify statistical anomalies
   *   **3.3. Timeliness Validation:** Check data freshness
       *   **3.3.1. Timestamp Analysis:** Analyze data age distribution
       *   **3.3.2. Update Frequency Verification:** Confirm regular data updates
       *   **3.3.3. Currency Assessment:** Verify data meets recency requirements

2. **`[MUST]` Generate Quality Reports:** {Description}
   *   **3.4. Completeness Report:** Document missing data analysis
   *   **3.5. Accuracy Report:** Document validation results
   *   **3.6. Timeliness Report:** Document data freshness analysis
```

---

## ERROR HANDLING

### Substep-level Error Recovery:
```markdown
*   **2.3. Data Transformation:** Apply transformation logic
    *   **Validation:** All transformations complete without errors
    *   **Evidence:** Transformation logs and output samples
    *   **Error Recovery:** If transformation fails, revert to last known good state and retry with adjusted parameters
    *   **Halt condition:** Stop if >3 consecutive transformation failures
```

---

## QUALITY GATES

### Substep Completion Criteria:
```markdown
### QUALITY GATES
#### Gate 1: Phase Completion
- **Phase 1**: All 6 substeps complete with validation passed
- **Phase 2**: All 12 substeps complete with validation passed  
- **Phase 3**: All 9 substeps complete with validation passed
- **Phase 4**: All 5 substeps complete with validation passed

#### Gate 2: Substep Quality
- Each substep must have specific validation criteria
- Failed substeps must be documented and retried
- Maximum 3 retries per substep before escalation
```

---

*Substeps Execution Template - For detailed, multi-step workflows*

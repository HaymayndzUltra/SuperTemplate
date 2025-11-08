# Template: Execution with Reasoning

**Source**: EXECUTION-FORMATS.md (REASONING variant)  
**Use Case**: Complex decision-making workflows requiring documented rationale  
**Key Features**:
- PHASE 1-4 structure with [REASONING] blocks
- Decision documentation with alternatives
- Risk assessment and mitigation
- Evidence-based decision tracking

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

### PHASE 1: {Phase_1_Name - Discovery/Analysis}

1.  **`[CRITICAL]` {Critical_analysis_action}:** {Description}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}

2.  **`[MUST]` {Analysis_action}:** {Description}

### PHASE 2: {Phase_2_Name - Strategic Decisions}

1.  **`[MUST]` {Major_decision_action}:**
    **[REASONING]**
    - **Premises:** {What we know from analysis}
    - **Constraints:** {Limitations and requirements}
    - **Alternatives Considered:**
      A) {Option A description} (rejected - {specific reason})
      B) {Option B description} (selected - {specific reason})
      C) {Option C description} (rejected - {specific reason})
    - **Decision:** {Chosen approach with justification}
    - **Evidence:** {Supporting data or precedent}
    - **Risks & Mitigations:**
      - Risk: {Risk description} → Mitigation: {Mitigation strategy}
      - Risk: {Risk description} → Mitigation: {Mitigation strategy}
    - **Acceptance Link:** {Reference to requirements or standards}

2.  **`[MUST]` {Second_decision_action}:**
    **[REASONING]**
    - **Premises:** {Context for this decision}
    - **Constraints:** {Specific limitations}
    - **Alternatives Considered:**
      A) {Option A} (selected - {reason})
      B) {Option B} (rejected - {reason})
    - **Decision:** {Final choice}
    - **Evidence:** {Supporting information}
    - **Risks & Mitigations:**
      - Risk: {Risk} → Mitigation: {Strategy}

### PHASE 3: {Phase_3_Name - Implementation Planning}

1.  **`[CRITICAL]` {Planning_action}:** {Description}
    *   **{Sub-step_number}. {Sub-step_title}:** {Detailed instructions}
    *   **{Sub-step_number}. {Sub-step_title}:** {Detailed instructions}

2.  **`[MUST]` {Resource_allocation_action}:**
    **[REASONING]**
    - **Premises:** {Resource requirements from decisions}
    - **Constraints:** {Budget, time, personnel limitations}
    - **Alternatives Considered:**
      A) {Resource option A} (selected - {efficiency reason})
      B) {Resource option B} (rejected - {cost/complexity reason})
    - **Decision:** {Resource allocation strategy}
    - **Evidence:** {Resource availability data}
    - **Risks & Mitigations:**
      - Risk: {Resource constraint} → Mitigation: {Contingency plan}

### PHASE 4: {Phase_4_Name - Validation & Finalization}

1.  **`[CRITICAL]` {Validation_action}:** {Description}
    *   **{Sub-step_number}. {Validation_step}:** {Instructions}
    *   **{Sub-step_number}. {Quality_check}:** {Instructions}

2.  **`[MUST]` {Finalization_action}:** {Description}

---

## OUTPUT TEMPLATE

{Output_structure_with_decision_documentation}

---

## VALIDATION CRITERIA

- [ ] {Validation_criterion_1}
- [ ] {Validation_criterion_2}
- [ ] {Validation_criterion_3}
- [ ] All major decisions include [REASONING] blocks
- [ ] Risk assessments documented with mitigations
- [ ] Evidence cited for all decision choices
```

---

## WHEN TO USE

✅ **Use this template when:**
- Complex strategic decisions require documentation
- Multiple alternatives need evaluation and justification
- Risk assessment is critical for success
- Decision audit trail is important
- Stakeholder approval requires transparent reasoning

❌ **Do NOT use this template when:**
- Simple workflow execution (use BASIC variant)
- Many detailed substeps need tracking (use SUBSTEPS variant)
- Setting rules and standards (use GUIDELINES template)

---

## REASONING BLOCK STRUCTURE

### Complete [REASONING] Block Format:
```markdown
**[REASONING]**
- **Premises:** {What we know as facts}
- **Constraints:** {Limitations we must work within}
- **Alternatives Considered:**
  A) {Option A} (selected/rejected - {specific reason})
  B) {Option B} (selected/rejected - {specific reason})
- **Decision:** {Final choice with clear justification}
- **Evidence:** {Data, precedents, or standards supporting choice}
- **Risks & Mitigations:**
  - Risk: {Specific risk} → Mitigation: {Concrete strategy}
- **Acceptance Link:** {Reference to requirements or stakeholder needs}
```

### Reasoning Quality Standards:
- **Premises**: Must be factual and verifiable
- **Constraints**: Must be realistic and specific
- **Alternatives**: Minimum 2 options considered
- **Decision**: Clear statement with justification
- **Evidence**: Specific data or references cited
- **Risks**: At least 1 risk identified per major decision
- **Mitigations**: Concrete actions for each risk

---

## DATA STRATEGY EXAMPLE

### Data Source Selection Decision:
```markdown
1. **`[MUST]` Select Primary Data Sources:**
   **[REASONING]**
   - **Premises**: Use cases require customer behavior data, transaction history, and product attributes
   - **Constraints**: Budget limited to $50K for data acquisition, timeline 8 weeks
   - **Alternatives Considered:**
     A) Purchase external data (selected - comprehensive coverage, proven quality)
     B) Build data collection infrastructure (rejected - 6-month timeline exceeds project window)
     C) Use only internal data (rejected - insufficient feature coverage for model accuracy)
   - **Decision**: Purchase curated external dataset with internal data augmentation
   - **Evidence**: External vendor provides 95% feature coverage with 99% data quality SLA
   - **Risks & Mitigations:**
     - Risk: Vendor dependency → Mitigation: Data escrow agreement with internal backup
     - Risk: Integration complexity → Mitigation: Dedicated 2-week integration sprint
   - **Acceptance Link**: Use case requirements specify minimum 90% feature coverage
```

---

## DECISION TRACKING

### Decision Log Format:
```markdown
## DECISION LOG
| Decision ID | Date | Decision | Alternatives | Rationale | Risk Rating |
|-------------|------|----------|--------------|-----------|-------------|
| D-001 | 2025-01-08 | Use external data vendor | A) External (selected) B) Build (rejected) C) Internal only (rejected) | Timeline and coverage requirements | Medium |
```

---

*Reasoning Execution Template - For complex decision-making workflows*

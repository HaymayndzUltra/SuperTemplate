# Template: Basic Protocol Execution

**Source**: EXECUTION-FORMATS.md  
**Use Case**: Standard protocol execution workflows  
**Key Features**:
- PHASE 1-4 structure
- Simple action/sub-step format
- Directive markers ([CRITICAL], [MUST], [GUIDELINE], [NEW])
- Task decomposition templates
- Final output template

---

## PROTOCOL STRUCTURE

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

### PHASE 1: {Phase_1_Name - Initial Setup/Discovery/Preparation}

1.  **`[CRITICAL]` {Critical_action_title}:** {Description of critical action and why it's non-negotiable}
    *   **{Sub-step_number}. {Sub-step_title}:** {Detailed sub-step instructions}
    *   **{Sub-step_number}. {Sub-step_title}:** {Detailed sub-step instructions}
    *   **{Sub-step_number}. {Sub-step_title}:** {Detailed sub-step instructions}

2.  **{Action_title}:** {Action description and instructions}

3.  **`[MUST]` {Required_action_title}:** {Description of required action with specific instructions}

4.  **{Action_title}:** {Action description with contextual guidance}
    *   *{Example or clarification}*

5.  **{Action_title}:** {Action description}

6.  **{Optional_action_title} (Optional):** {Optional action description with user confirmation guidance}

### PHASE 2: {Phase_2_Name - Analysis/Processing/Development}

1.  **`[CRITICAL]` {Critical_action_title}:** {Description}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}

2.  **`[MUST]` {Required_action_title}:** {Description}

3.  **{Action_title}:** {Description}

### PHASE 3: {Phase_3_Name - Validation/Refinement/Testing}

1.  **`[CRITICAL]` {Critical_action_title}:** {Description}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}

2.  **`[MUST]` {Required_action_title}:** {Description}

3.  **{Action_title}:** {Description}

### PHASE 4: {Phase_4_Name - Finalization/Output/Handoff}

1.  **`[CRITICAL]` {Critical_action_title}:** {Description}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}
    *   **{Sub-step_number}. {Sub-step_title}:** {Instructions}

2.  **`[MUST]` {Required_action_title}:** {Description}

3.  **{Action_title}:** {Description}

---

## OUTPUT TEMPLATE

{Output_template_structure}

---

## VALIDATION CRITERIA

- [ ] {Validation_criterion_1}
- [ ] {Validation_criterion_2}
- [ ] {Validation_criterion_3}
```

---

## WHEN TO USE

✅ **Use this template when:**
- Standard workflow execution with clear phases
- Sequential step-by-step process
- Simple decision-making without complex reasoning blocks
- Straightforward input → process → output flow

❌ **Do NOT use this template when:**
- Complex decision-making requires detailed reasoning documentation
- Many detailed substeps need precise tracking (use SUBSTEPS variant)
- Setting rules and standards (use GUIDELINES template)

---

## CUSTOMIZATION GUIDELINES

### Phase Names
Choose descriptive phase names:
- **Discovery**: Initial analysis and requirements gathering
- **Preparation**: Setup and resource allocation  
- **Development**: Core creation/building work
- **Validation**: Testing and quality assurance
- **Finalization**: Completion and handoff preparation

### Directive Markers
- **`[CRITICAL]`**: Safety-critical, non-negotiable actions
- **`[MUST]`**: Required actions for protocol success
- **`[GUIDELINE]`**: Strong recommendations with flexibility
- **`[NEW]`**: New or experimental features

### Sub-step Structure
Use numbered sub-steps (1.1, 1.2, 1.3) when:
- Action requires multiple sequential operations
- Each sub-step has distinct verification criteria
- Error handling needed at sub-step level

---

*Basic Execution Template - For straightforward protocol workflows*

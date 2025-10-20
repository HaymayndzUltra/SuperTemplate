---
description: "{TAGS_PLACEHOLDER} | {TRIGGERS_PLACEHOLDER} | {SCOPE_PLACEHOLDER} | DESCRIPTION: {Description_Placeholder}"
alwaysApply: {boolean_value}
---

# {Protocol_Title}: {Protocol_Name}

## 1. {Section_1_Name}

{Section_1_Description}.

## 2. {Section_2_Name}

{Section_2_Description}.

-   **{Mode_1_Name}:** {Mode_1_Description}.
-   **[{Marker}] {Mode_2_Name}:** {Mode_2_Description}.

---

## 3. {Section_3_Name}

**[{Marker}] {Section_3_Description}.**

1.  **{Step_1}** {Step_1_Description}.
2.  **[{Marker}] {Step_2}:** {Step_2_Description}.
3.  **{Step_3}:** {Step_3_Description}.
4.  **{Step_4}** {Step_4_Description}.
5.  **{Step_5}.**
6.  {Step_6}.

{Closing_Statement}.

---

## 3.5. {Section_3_5_Name}

**[{Marker}] {Section_3_5_Description}.**

1.  **{Subsection_1_Name}:** {Subsection_1_Description}.
2.  **{Subsection_2_Name}:**
    *   {Instruction_1}.
    *   **{Instruction_2}.** {Instruction_2_Description}.
    *   **{Subsection_2_3_Name}:**
        1.  `{Message_Template_1}`
        2.  `{Message_Template_2}`
    *   **{Instruction_3}** {Instruction_3_Description}.

---

## 4. {Section_4_Name}

**[{Marker}] {Section_4_Description}.**

### STEP 1: {Step_4_1_Name}
*   **[STRICT]** {Step_4_1_Description}.

### STEP 2: {Step_4_2_Name}
*   **[STRICT]** {Step_4_2_Description}.

---

## 5. {Section_5_Name}

**{Loop_Condition}:**

### STEP 1: {Step_5_1_Name}
1.  **{Substep_1_1_Name}:** {Substep_1_1_Description}.
2.  **{Substep_1_2_Name}:**
    *   **[{Marker}]** {Substep_1_2_1}.
    *   **[STRICT]** {Substep_1_2_2}.
    *   **[STRICT]** {Substep_1_2_3}: `{message_template}`.
3.  **{Substep_1_3_Name}:**
    *   **[STRICT]** {Substep_1_3_Description}.
4.  **{Substep_1_4_Name}:**
    *   {Substep_1_4_Description}: `{message_template}`.

### STEP 2: {Step_5_2_Name}
1.  **{Substep_2_1_Name}:** {Substep_2_1_Description}.
    *   **[GUIDELINE] {Substep_2_1_1_Name}:** {Substep_2_1_1_Description}.
2.  **{Substep_2_2_Name}:** {Substep_2_2_Description}:
    - **{Rule_1}:** {Rule_1_Description}
    - **{Rule_2}:** {Rule_2_Description}
3.  **{Substep_2_3_Name}:** {Substep_2_3_Description}.
4.  **{Substep_2_4_Name}:**
    - **{Check_1_Name}:** {Check_1_Description}:
      - {Check_1_Action_1}: `{command_template}`
      - {Check_1_Action_2}
      - {Check_1_Action_3}
    - **{Check_2_Name}:** {Check_2_Description}:
      - {Check_2_Action_1}
      - {Check_2_Action_2}
      - {Check_2_Action_3}
    - **{Check_3_Name}:** {Check_3_Description}:
      - **{Check_3_1_Name}:** {Check_3_1_Description}
      - **{Check_3_2_Name}:** {Check_3_2_Description}
      - **{Check_3_3_Name}:** {Check_3_3_Description}
6.  **{Substep_2_6_Name}:** {Substep_2_6_Description}:
    - **{Validation_1}:** {Validation_1_Description}
    - **{Validation_2}:** {Validation_2_Description}
    - **{Validation_3}:** {Validation_3_Description}
7.  **{Substep_2_7_Name}:** {Substep_2_7_Description}.

### STEP 3: {Step_5_3_Name}
1.  **[{Marker}] {Substep_3_1_Name}:**
    *   **[MANDATORY]** {Substep_3_1_1}.
    *   **[STRICT]** {Substep_3_1_2}.
    *   {Substep_3_1_3}.
    *   **[REMINDER]** {Substep_3_1_4}.

2.  **[{Marker}] {Substep_3_2_Name}:**
    *   **[{Marker}]** {Substep_3_2_1}:
        - **[MANDATORY]** {Substep_3_2_1_1}
        - **{Label}**: `{format_template}`
        - **{Examples_Label}**: 
          - `{example_1}`
          - `{example_2}`
          - `{example_3}`
        - **[CRITICAL]** {Substep_3_2_1_2}
    
3.  **{Substep_3_3_Name}:**
    *   {Substep_3_3_1}.
    *   **[STRICT] {Substep_3_3_2}**: {Substep_3_3_2_Description}
    *   **[CRITICAL] {Substep_3_3_3}:**
        - **[MANDATORY]** {Action_1}
        - **[STRICT]** {Action_2}: `{command_template}`
        - **[REQUIRED]** {Action_3}
        - **[COMMUNICATION]** `{message_template_1}`
        - **[VALIDATION]** {Action_4}: `{message_template_2}`
    *   **[{Marker}] {Substep_3_3_4}:**
        - **{Context_1}**: {Context_1_Description}
        - **{Context_2}**: {Context_2_Description}
        - **{Context_3}**: {Context_3_Description}
    *   **{Substep_3_3_5}:**
        1.  `{flow_message_1}`
        2.  `{flow_message_2}`
        3.  `{flow_message_3}`
        4.  **[{Marker}]** `{flow_message_4}`
        5.  **[STRICT]** {flow_instruction}.

4.  **[{Marker}] {Substep_3_4_Name}:**
    *   **{Consideration_1}**: {Consideration_1_Description}
        - `{pattern_1}`
        - `{pattern_2}`
    *   **{Consideration_2}**: {Consideration_2_Description}
        - `{pattern_3}`
    *   **{Consideration_3}**: {Consideration_3_Description}
        - `{pattern_4}`
        - `{pattern_5}`
    *   **{Consideration_4}**: {Consideration_4_Description}
        - `{pattern_6}`
    *   **{Consideration_5}**: {Consideration_5_Description}
        - `{pattern_7}`
        - `{pattern_8}`
    *   **{Consideration_6}**: {Consideration_6_Description}
        - `{pattern_9}`

### STEP 4: {Step_5_4_Name}
1.  **{Substep_4_1_Name}:** {Substep_4_1_Question}
2.  **{Substep_4_2_Name}:**
    *   **{Mode_A_Name}:**
        *   **{Context_A_1}:** `{message_template_A_1}`
        *   **{Context_A_2}:** `{message_template_A_2}`
    *   **{Mode_B_Name}:**
        *   {Context_B_1}.
        *   **{Context_B_2}:** `{message_template_B}`
3.  **[{Marker}] {Substep_4_3_Name}:**
    *   **[CRITICAL]** {Action_1}
    *   **[COMMUNICATION]** `{message_template_1}`
    *   **[VALIDATION]** {Action_2}
    *   **[REPORT]** `{message_template_2}`
4.  **{Substep_4_4_Name}:** {Substep_4_4_Description}.

**{Loop_End_Marker}**

---

## 6. {Section_6_Name}

-   **{Directive_1_Name}:** {Directive_1_Description}.
-   **{Directive_2_Name}:** {Directive_2_Description}.
-   **{Directive_3_Name}:** {Directive_3_Description}.

---

## VALIDATION CRITERIA
- [ ] {Validation_Criterion_1}
- [ ] {Validation_Criterion_2}
- [ ] {Validation_Criterion_3}
- [ ] {Validation_Criterion_4}
- [ ] {Validation_Criterion_5}

---

**{Protocol_Purpose_Statement}** 
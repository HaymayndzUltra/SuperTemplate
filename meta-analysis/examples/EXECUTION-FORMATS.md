# TEMPLATE FORMAT 2: BASIC PROTOCOL EXECUTION

**Source:** FORMAT3.md  
**Use Case:** Standard protocol execution workflows  
**Key Features:**
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

### PHASE 2: {Phase_2_Name - Generation/Validation/Analysis}

1.  **{Action_title}:** {Action description}

2.  **{Action_title}:** {Action description}
    *   **[GUIDELINE] {Guideline_principle}:** {Guideline description and reasoning}

3.  **`[NEW]` {New_feature_title}:** {Description of new feature or enhancement}
    *   {Format specification or requirement}
    *   {Focus areas or key considerations}
    *   {Example with specific format}

4.  **{Action_title}:** {Action description with dependency or relationship guidance}
    *   *{Example scenario}*
    *   {Output format specification with example}
    *   {Guidance on parallel execution or dependencies}

5.  **{Assessment_action_title}:** {Assessment description}
    *   **{Category_1}**: {Category description}
    *   **{Category_2}**: {Category description}

6.  **{Validation_checkpoint_title} (Await "{User_confirmation_keyword}"):**
    *   {What to present to user}
    *   {Announcement text to deliver}
    *   **HALT AND AWAIT** {Explicit confirmation requirement}

### PHASE 3: {Phase_3_Name - Detailed Implementation/Breakdown}

1.  **{Primary_action_title}:** {Action description with iteration instructions}
    *   **`[CRITICAL]` {Critical_sub-action_title}:** {Description of how to apply rules, references, or validation}

2.  **{Assignment_action_title}:** {Description of how to assign work, personas, or responsibilities}

3.  **{Template_selection_action_title}:**
    *   {Condition_1}, use the **{Template_A_name}**.
    *   {Condition_2}, use the **{Template_B_name}**.
    *   {Condition_3}, use the **{Template_C_name}**.

4.  **{Placeholder_replacement_title}:** {Instructions for replacing placeholders with actual values}

5.  **{Finalization_title}:** {Assembly and saving instructions}

### PHASE 4: {Phase_4_Name - Automation/Enhancement/Validation}

1.  **`[MUST]` {Automation_action_title}:** {Description of automation or enhancement requirement}
    *   **{Sub-step_number}. {Sub-step_title}:** {Sub-step instructions}
        *   **[GUIDELINE] {Prioritization_guidance_title}:**
            *   **{Priority_category_1}:** {Examples or descriptions}
            *   **{Priority_category_2}:** {Examples or descriptions}
    *   **{Sub-step_number}. {Metadata_annotation_title}:** {Annotation instructions}
        *   **Format:** `{Metadata_format_specification}`
        *   **Types:** `{Type_1}`, `{Type_2}`
        *   **Examples:**
            *   `{Example_1}`
            *   `{Example_2}`
        *   **[CRITICAL]** {Critical requirement for metadata}

2.  **`[MUST]` {Validation_action_title}:** {Validation instructions}
    ```bash
    {Validation_command_or_script}
    ```

3.  **`[MUST]` {Update_action_title}:** {Update instructions for templates or references}

---

## DECOMPOSITION TEMPLATES

### Template A: {Template_Category_Name} (`{Template_Scope}`)

- [ ] {Task_number}. {High-level_task_title} (`{artifact_name}`).
  - [ ] {Sub-task_number}. **{Sub-task_title}:** {Sub-task_description}. [APPLIES RULES: {rule_references}]
  - [ ] {Sub-task_number}. **{Sub-task_title}:** {Sub-task_description}. [APPLIES RULES: {rule_references}]
  - [ ] {Sub-task_number}. **{Sub-task_category_title}:**
      - [ ] {Nested_sub-task_number}. {Nested_description}. [APPLIES RULES: {rule_references}]
      - [ ] {Nested_sub-task_number}. {Nested_description}. [APPLIES RULES: {rule_references}]

### Template B: {Template_Category_Name} (`{Template_Scope}`)

- [ ] {Task_number}. {High-level_task_title} in the `{service_name}`.
  - [ ] {Sub-task_number}. **{Sub-task_category_title}:**
      - [ ] {Nested_number}. {Nested_description}. [APPLIES RULES: {rule_references}]
      - [ ] {Nested_number}. {Nested_description}. [APPLIES RULES: {rule_references}]

---

## FINAL OUTPUT TEMPLATE

# {Document_Title}

Based on {Source_document_reference}: `{Link_to_source_file}`

> **Note on {Strategic_guidance_topic}:** {Strategic note or recommendation}
> *   **{Persona_1_Name} ({Model_identifier}):** {Persona_description_and_strengths}
> *   **{Persona_2_Name} ({Model_identifier}):** {Persona_description_and_strengths}

## {Section_title}

### {Subsection_1_title}
*   `{File_path_or_artifact_1}`

### {Subsection_2_title}
*   `{File_path_or_artifact_2}`

## {Main_content_section_title}

-   [ ] {Task_number}. **{High-level_task_title}** [{Complexity_indicator}]
> **WHY:** {Business_value_statement}
> **{Metadata_label_1}:** `{Metadata_value}`
> **{Metadata_label_2}:** `{Rule_reference_1}`, `{Rule_reference_2}`
> **{Automation_label}:** {Automation_type}:{Command_path}
    -   *({Note_about_template_usage})*
```

---

**When to use:**  
- Standard protocol workflows without complex reasoning
- Task-based execution plans
- Simple automation workflows# TEMPLATE FORMAT 3: PROTOCOL WITH NUMBERED SUBSTEPS

**Source:** FORMATS.md (lines 232-453)  
**Use Case:** Protocols requiring detailed step tracking with numbered substeps  
**Key Features:**
- PHASE 1-4 structure
- Numbered substeps (1.1, 1.2, 1.3, etc.)
- Detailed decomposition templates
- Automation metadata
- Execution tracking

---

## PROTOCOL STRUCTURE

```markdown
---
description: {Protocol_Short_Description}
auto_execution_mode: {execution_mode_number}
---

# PROTOCOL {NUMBER}: {PROTOCOL_NAME}

## AI ROLE

You are a **{Role_Title}**. {Role_Description}.

**{Output_Format_Expectation}**

## INPUT

-   {Input_Item_1}
-   {Input_Item_2}

---

## {ALGORITHM_SECTION_NAME}

### PHASE 1: {Phase_1_Name}

1.  **`[CRITICAL]` {Step_1_Action}:** {Step_1_Description}.
    *   **1.1. {Substep_1_1_Action}:** {Substep_1_1_Description}.
    *   **1.2. {Substep_1_2_Action}:** {Substep_1_2_Description}.
    *   **1.3. {Substep_1_3_Action}:** {Substep_1_3_Description}.

2.  **{Step_2_Action}:** {Step_2_Description}.

3.  **`[MUST]` {Step_3_Action}:** {Step_3_Description}.

4.  **{Step_4_Action}:** {Step_4_Description}.
    *   *{Example_Placeholder}*

5.  **{Step_5_Action}:** {Step_5_Description}.

6.  **{Step_6_Action}:** {Step_6_Description}.

### PHASE 2: {Phase_2_Name}

1.  **{Step_1_Action}:** {Step_1_Description}.

2.  **{Step_2_Action}:** {Step_2_Description}.
    *   **[GUIDELINE] {Guideline_Name}:** {Guideline_Description}.

3.  **`[NEW]` {Step_3_Action}:** {Step_3_Description}.
    *   Format: `{Format_Placeholder}`
    *   Focus on: {Focus_Areas_Placeholder}
    *   Example: `{Example_Placeholder}`

4.  **{Step_4_Action}:** {Step_4_Description}.
    *   *{Example_Placeholder}*
    *   {Format_Requirement}.
    *   {Execution_Note}.

5.  **{Step_5_Action}:** {Step_5_Description}:
    *   **{Complexity_Level_1}**: {Complexity_Description_1}
    *   **{Complexity_Level_2}**: {Complexity_Description_2}

6.  **{Step_6_Action}:**
    *   {Substep_Description_1}.
    *   Announce: "{Announcement_Message}"
    *   **{Action_Marker}** {Action_Description}.

### PHASE 3: {Phase_3_Name}

1.  **{Step_1_Action}:** {Step_1_Description}.
    *   **`[CRITICAL]` {Substep_Action}:** {Substep_Description}.

2.  **{Step_2_Action}:** {Step_2_Description}.

3.  **{Step_3_Action}:**
    *   If {Condition_1}, use the **{Template_1_Name}**.
    *   If {Condition_2}, use the **{Template_2_Name}**.
    *   If {Condition_3}, use the **{Template_3_Name}**.

4.  **{Step_4_Action}:** {Step_4_Description}.

5.  **{Step_5_Action}:** {Step_5_Description}.

### PHASE 4: {Phase_4_Name}

1.  **`[MUST]` {Step_1_Action}:** {Step_1_Description}.
    *   **4.1. {Substep_1_Action}:** {Substep_1_Description}.
        *   **[GUIDELINE] {Guideline_Name}:**
            *   **{Category_1}:** {Category_1_Description}
            *   **{Category_2}:** {Category_2_Description}
            *   **{Category_3}:** {Category_3_Description}
    *   **4.2. {Substep_2_Action}:** {Substep_2_Description}.
        *   **Format:** `{Format_Pattern}`
        *   **Types:** `{Type_1}`, `{Type_2}`
        *   **Examples:**
            *   `{Example_1}`
            *   `{Example_2}`
        *   **[CRITICAL]** {Critical_Requirement}.
    *   **4.3. {Substep_3_Action}:** {Substep_3_Description}.

2.  **`[MUST]` {Step_2_Action}:** {Step_2_Description}.
    ```bash
    {Command_Placeholder}
    ```

3.  **`[MUST]` {Step_3_Action}:** {Step_3_Description}.

---

## {TEMPLATES_SECTION_NAME}

### Template A: {Template_A_Name}

- [ ] X.0 {Task_Description}.
  - [ ] X.1 **{Subtask_1_Name}:** {Subtask_1_Description}. [APPLIES RULES: {rule-placeholder}]
  - [ ] X.2 **{Subtask_2_Name}:** {Subtask_2_Description}. [APPLIES RULES: {rule-placeholder}]
  - [ ] X.3 **{Subtask_3_Name}:** {Subtask_3_Description}. [APPLIES RULES: {rule-placeholder}]
  - [ ] X.4 **{Subtask_4_Name}:**
      - [ ] X.4.1 {Subtask_4_1_Description}. [APPLIES RULES: {rule-placeholder}]
      - [ ] X.4.2 {Subtask_4_2_Description}. [APPLIES RULES: {rule-placeholder-1}, {rule-placeholder-2}]
      - [ ] X.4.3 {Subtask_4_3_Description}. [APPLIES RULES: {rule-placeholder}]

### Template B: {Template_B_Name}

- [ ] Y.0 {Task_Description}.
  - [ ] Y.1 **{Subtask_1_Name}:**
      - [ ] Y.1.1 {Subtask_1_1_Description}. [APPLIES RULES: {rule-placeholder}]
      - [ ] Y.1.2 {Subtask_1_2_Description}. [APPLIES RULES: {rule-placeholder}]
  - [ ] Y.2 **{Subtask_2_Name}:**
      - [ ] Y.2.1 {Subtask_2_1_Description}. [APPLIES RULES: {rule-placeholder-1}, {rule-placeholder-2}]
      - [ ] Y.2.2 {Subtask_2_2_Description}. [APPLIES RULES: {rule-placeholder-1}, {rule-placeholder-2}]

---

## {FINAL_OUTPUT_SECTION_NAME}

# {Output_Document_Title}

Based on {Input_Reference}: `{Input_Link_Placeholder}`

> **{Note_Title_1}:** {Note_Description_1}.
> *   **{Persona_1_Name} ({Model_1_Name}):** {Persona_1_Description}
> *   **{Persona_2_Name} ({Model_2_Name}):** {Persona_2_Description}

## {Execution_Plan_Section_Name}

-   [ ] 1.0 **{High_Level_Task_1}** [COMPLEXITY: {Complexity_Level}]
> **WHY:** {Business_Value_Statement}
> **Recommended Model:** `{Persona_Name}`
> **Rules to apply:** `{rule_list_placeholder}`
> **Automation:** {automation_hook_1}
> **Automation:** {automation_hook_2}
    -   *({Template_Usage_Note})*

-   [ ] 2.0 **{High_Level_Task_2}** [COMPLEXITY: {Complexity_Level}] [DEPENDS ON: {dependency_list}]
> **WHY:** {Business_Value_Statement}
> **Recommended Model:** `{Persona_Name}`
> **Rules to apply:** `{rule_list_placeholder}`
    -   [ ] 2.1 {Subtask_Description} [APPLIES RULES: {rule-placeholder}]
```

---

**When to use:**  
- Protocols requiring precise step tracking
- Complex workflows with many substeps
- Projects needing detailed execution traces
- Automation-heavy workflows# TEMPLATE FORMAT 4: PROTOCOL WITH REASONING BLOCKS

**Source:** FORMATS2.md  
**Use Case:** Protocols requiring detailed decision-making documentation and reasoning  
**Key Features:**
- [REASONING] blocks after each step
- [STRICT] and [GUIDELINES] markers
- Premises → Decision → Evidence → Acceptance pattern
- Detailed decomposition templates (Frontend, Backend, Global State)
- System instruction integration

---

## REASONING BLOCK STRUCTURE

This drop-in block is used after **every step** following [STRICT]/[GUIDELINES]:

```markdown
[REASONING]
- Premises: {facts from PRD/@rules}
- Constraints: {tech/ops/legal/time}
- Alternatives Considered: {A|B|C + short tradeoffs}
- Decision: {chosen path + why}
- Evidence: {links to PRD sections, benchmarks, prior components}
- Risks & Mitigations: {risk → guardrail/test}
- Acceptance Link: {how this maps to SuccessMetrics/Invariants}
```

---

## PROTOCOL STRUCTURE

```markdown
## AI ROLE
You are a **{Role_Title}** producing a structured action plan from a PRD using project `@rules`.

[STRICT] Provide a "DO" Example:
[GUIDELINES]:
[REASONING]
- Premises:
- Constraints:
- Alternatives Considered:
- Decision:
- Evidence:
- Risks & Mitigations:
- Acceptance Link:

## INPUT
- {Input_Item_1}
- {Input_Item_2}

[STRICT] Provide a "DO" Example:
[GUIDELINES]:
[REASONING]
- Premises:
- Constraints:
- Alternatives Considered:
- Decision:
- Evidence:
- Risks & Mitigations:
- Acceptance Link:

---

## GENERATION ALGORITHM

### PHASE 1: {Phase_1_Name}

1. **`[MUST]` {Action_Title}:** {Action_Description}
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

2. **{Action_Title}:** {Action_Description}
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

3. **`[MUST]` {Action_Title}:** {Action_Description}
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

### PHASE 2: {Phase_2_Name}

1. **{Action_Title}:** {Action_Description}
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

2. **{Action_Title}:** {Action_Description}
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

3. **{Validation_Checkpoint} (Await "Go"):**
   * Present this to the user.
   * Announce: "{Announcement_Message}"
   * **HALT AND AWAIT** explicit user confirmation.
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

### PHASE 3: {Phase_3_Name}

1. **{Decomposition_Action}:** Once "Go" is received, break down each high-level task.
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

2. **{Assignment_Action}:** Determine which LLM persona is best suited.
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

3. **{Template_Selection}:**
   * If task relates to **Frontend**, use the **Frontend Decomposition Template**.
   * If task relates to **Backend**, use the **Backend Decomposition Template**.
   * If task involves **Global State**, use the **Global State Decomposition Template**.
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

4. **{Placeholder_Replacement}:** Systematically replace placeholders.
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:

5. **{Finalization}:** Assemble and save the task file.
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises:
   - Constraints:
   - Alternatives Considered:
   - Decision:
   - Evidence:
   - Risks & Mitigations:
   - Acceptance Link:
```

---

## DECOMPOSITION TEMPLATES

### Template A: Frontend Decomposition

```markdown
- [ ] X.0 Develop the "{ComponentName}" component (`{componentName}`).
  [STRICT] Provide a "DO" Example:
  [GUIDELINES]:
  [REASONING]
  - Premises:
  - Constraints:
  - Alternatives Considered:
  - Decision:
  - Evidence:
  - Risks & Mitigations:
  - Acceptance Link:

  - [ ] X.1 **File Scaffolding:** Create the complete file structure.
    [STRICT] Provide a "DO" Example:
    [GUIDELINES]:
    [REASONING]
    - Premises:
    - Constraints:
    - Alternatives Considered:
    - Decision:
    - Evidence:
    - Risks & Mitigations:
    - Acceptance Link:

  - [ ] X.2 **Base HTML:** Implement the static HTML structure.
    [STRICT] Provide a "DO" Example:
    [GUIDELINES]:
    [REASONING]
    - Premises:
    - Constraints:
    - Alternatives Considered:
    - Decision:
    - Evidence:
    - Risks & Mitigations:
    - Acceptance Link:

  - [ ] X.3 **Internationalization:** Create and populate locale files.
    [STRICT] Provide a "DO" Example:
    [GUIDELINES]:
    [REASONING]
    - Premises:
    - Constraints:
    - Alternatives Considered:
    - Decision:
    - Evidence:
    - Risks & Mitigations:
    - Acceptance Link:

  - [ ] X.4 **JavaScript Logic:**
      [STRICT] Provide a "DO" Example:
      [GUIDELINES]:
      [REASONING]
      - Premises:
      - Constraints:
      - Alternatives Considered:
      - Decision:
      - Evidence:
      - Risks & Mitigations:
      - Acceptance Link:
      - [ ] X.4.1 Implement component initialization function.
      - [ ] X.4.2 Implement API/service calls with error handling.
      - [ ] X.4.3 Implement event handlers for user interactions.

  - [ ] X.5 **CSS Styling:** Apply styles respecting theming and responsive design.
  - [ ] X.6 **Documentation:** Write the component's README.md.
```

### Template B: Backend Decomposition

```markdown
- [ ] Y.0 Develop the "{RoutePurpose}" route in the `{serviceName}` service.
  [STRICT] Provide a "DO" Example:
  [GUIDELINES]:
  [REASONING]
  - Premises:
  - Constraints:
  - Alternatives Considered:
  - Decision:
  - Evidence:
  - Risks & Mitigations:
  - Acceptance Link:

  - [ ] Y.1 **Route Scaffolding:**
      - [ ] Y.1.1 Create the directory `src/routes/{routePath}/`.
      - [ ] Y.1.2 Create necessary files following conventions.
      - [ ] Y.1.3 Run build script to register the new route.

  - [ ] Y.2 **Handler Logic:**
      - [ ] Y.2.1 Implement middleware and validate request body.
      - [ ] Y.2.2 Implement orchestration logic and format response.

  - [ ] Y.3 **Business Logic:**
      - [ ] Y.3.1 Create dedicated module for business logic (if complex).
      - [ ] Y.3.2 Implement external dependency calls.

  - [ ] Y.4 **Testing:**
      - [ ] Y.4.1 Write integration tests for the new route.
      - [ ] Y.4.2 Write unit tests for business logic module.
```

### Template C: Global State Management Decomposition

```markdown
- [ ] Z.0 Implement "{DomainName}" Global State Management.

  - [ ] Z.1 **Store Creation:** Create `stores/{domainName}.ts`
      - [ ] Z.1.1 Define TypeScript interfaces.
      - [ ] Z.1.2 Create primary atom store with initial state.
      - [ ] Z.1.3 Implement actions object with mutation methods.
      - [ ] Z.1.4 Create computed stores and subscriptions.

  - [ ] Z.2 **Service Integration:** Create or update `lib/{domainName}.ts`
      - [ ] Z.2.1 Implement `initialize()` method.
      - [ ] Z.2.2 Implement `startListener()` method.
      - [ ] Z.2.3 Integrate service methods with store actions.

  - [ ] Z.3 **Application Integration:** Update main app component
      - [ ] Z.3.1 Add store initialization call with error handling.
      - [ ] Z.3.2 Add listener startup and cleanup function.
      - [ ] Z.3.3 Add cleanup in `disconnectedCallback()`.

  - [ ] Z.4 **Component Integration:**
      - [ ] Z.4.1 Add subscriptions with proper cleanup.
      - [ ] Z.4.2 Use actions for state mutations.
      - [ ] Z.4.3 Handle loading and error states.

  - [ ] Z.5 **Documentation:** Update README files
      - [ ] Z.5.1 Document store structure.
      - [ ] Z.5.2 Provide usage examples.
      - [ ] Z.5.3 Document integration architecture.
```

---

## SYSTEM INSTRUCTION (Drop-in for AI agents)

```markdown
## Role & Scope
- You are a **{Role_Title}**. Transform a PRD into a structured, actionable plan.
- **Do not remove or rewrite** any lines that start with `[STRICT]` or `[GUIDELINES]`. Keep them verbatim.
- Under every section, **append** a `[REASONING]` block with all required fields.
- Follow **why-before-how**. All actions must reference PRD facts and `@rules`.

## Process Constraints
- **Phase 1**: Run context discovery, summarize key rules. Read PRD. Identify LLM personas. Map layers.
- **Phase 2**: Generate top-level tasks + complexity. **HALT** after presenting and await "Go".
- **Phase 3**: Upon "Go", decompose using correct template, assign personas, populate placeholders.

## Output Contract
- Output a **structured action plan**, not prose.
- Use the exact Markdown checklist templates provided.
- Keep placeholders intact until values exist in the PRD.
- Every task includes: `[STRICT]`, `[GUIDELINES]`, and `[REASONING]` blocks.

## Quality Gates
- Trace WHY→HOW in each `[REASONING]`'s **Acceptance Link**.
- No tech lock-in during scaffolding.
- Security, i18n/a11y, observability must appear where specified.
- Stop if info is missing; insert a **clearly labeled placeholder**.

## Failure Modes to Avoid
- Removing or paraphrasing the `[STRICT]` / `[GUIDELINES]` lines.
- Collapsing steps or mixing layers without noting dependencies.
- Writing free-form paragraphs without checklists.
```

---

**When to use:**  
- Protocols requiring documented decision-making
- Complex projects with multiple alternatives
- Task generation with reasoning traces
- Projects needing full audit trails
- Monorepo-aware technical task generation
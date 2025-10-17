# PROTOCOL 2: TECHNICAL TASK GENERATION

## AI ROLE

You are a **Tech Lead**. Transform a PRD into a simple, actionable plan. Guide implementation with minimum viable steps.

**Your output should be a structured action list, not prose.**

## INPUT

-   A PRD file (e.g., `prd-my-cool-feature.md`).
-   Implicit or explicit information about the **primary implementation layer** (e.g., Frontend App, Backend Service) as determined during the PRD creation.

---

## GENERATION ALGORITHM

### PHASE 1: Rule Indexing and Context Preparation

1.  **`[CRITICAL]` Build Rule Index:** Before any other action, you **MUST** systematically discover and index all project rules.
    *   **1.1. Find Rule Directories:** Dynamically locate all rule directories using `find . -name "*rules" -type d`.
    *   **1.2. Parse Rule Metadata:** For every file within these directories, read its content to find the `description:` line. You **MUST** parse this line to extract the structured metadata.
    *   **1.3. Create Index:** Store the parsed metadata (file path, TAGS, TRIGGERS, SCOPE, and DESCRIPTION) in an in-memory index for later use. This index is the foundation for ensuring compliance.

2.  **Read the PRD:** Fully analyze the PRD to understand the goals, constraints, and specifications, keeping the discovered rules in mind.

3.  **`[MUST]` Identify Top LLM Models & Personas:** To ensure up-to-date results and avoid using stale training data, perform a web search explicitly for the **current year**. Your search query should resemble: "best LLM for code generation <current_year>". Identify the 2-3 best-in-class models for code generation and software architecture. For each model, define a "persona" summarizing its core strengths (e.g., "System Integrator" for broad ecosystem knowledge, "Code Architect" for deep logical consistency).

4.  **Identify Implementation Layers:** Determine which codebases in the monorepo will be affected. There will always be a **primary layer** (where most of the work happens) and potentially **secondary layers**.
    *   *Example: A new UI page that calls a new backend endpoint. Primary: Frontend App. Secondary: Backend Service.*
5.  **Duplicate Prevention (for UI):** If the primary layer is a frontend application, perform a search using a codebase search tool (in accordance with the **Tool Usage Protocol**) to find similar existing components. If candidates are found, propose reuse (through inspiration/copy) to the user.
6.  **Git Branch Proposal (Optional):** Suggest creating a dedicated Git branch for the feature (e.g., `feature/feature-name`). Await user confirmation.

### PHASE 2: High-Level Task Generation and Validation

1.  **Create Task File:** Create a `tasks-[prd-name].md` file in a relevant `/tasks` or `/docs` directory.
2.  **Generate High-Level Tasks:** Create a list of top-level tasks that structure the development effort (e.g., "Develop UI Component," "Create Support Endpoint," "Integration Testing," "Documentation").
    *   **[GUIDELINE] Avoid Over-Engineering:** The task list should represent the most direct path to a Minimum Viable Product (MVP). Defer non-essential features, premature optimizations, or overly complex architectural patterns. Focus on delivering core functionality first.
3.  **`[NEW]` Add WHY Context for High-Level Tasks:** For each high-level task, add a concise WHY statement that explains the business value and objective. This enables better context switching, intelligent decision-making, and quality execution by AI agents.
    *   Format: `> **WHY:** [Business value statement in 1-2 lines explaining the objective and impact]`
    *   Focus on: Developer experience improvement, business capability enablement, technical debt reduction, or system reliability enhancement
    *   Example: `> **WHY:** Enable any developer to understand and choose the right SaaS pattern in <5min, eliminating architecture decision paralysis`
4.  **Identify Task Dependencies:** For each high-level task, identify its prerequisites from the list of other generated tasks. This is crucial for enabling parallel execution by AI agents.
    *   *Example: A task `3.0 End-to-End Integration Tests` will likely depend on `1.0 Develop UI Component` and `2.0 Create Backend Route`.*
    *   The output format MUST clearly state these dependencies using the task numbers (e.g., `[DEPENDS ON: 1.0, 2.0]`).
    *   Tasks with no dependencies are candidates for immediate parallel execution.
5.  **Task Complexity Assessment:** For each high-level task, assign a complexity level:
    *   **Simple**: Well-defined changes with minimal dependencies (e.g., adding a basic component, simple CRUD endpoint)
    *   **Complex**: Multi-system changes, architectural modifications, or security-critical implementations
6.  **High-Level Validation (Await "Go"):**
    *   Present this high-level list with WHY statements, complexity assessments, and dependencies to the user.
    *   Announce: "I have generated the high-level tasks with WHY context, complexity assessments, and dependencies based on the PRD, which will allow for safe parallel execution of independent tasks. Ready to break these down into detailed sub-tasks? Please reply 'Go' to continue."
    *   **HALT AND AWAIT** explicit user confirmation.

### PHASE 3: Detailed Breakdown by Layer

1.  **Decomposition and Rule Application:** Once "Go" is received, iterate through each high-level task. For each one, break it down into atomic, actionable sub-tasks using the templates below.
    *   **`[CRITICAL]` Apply Rules to Sub-Tasks:** For **every sub-task** generated, you **MUST** scan the rule index created in Phase 1. Based on the sub-task's description and the rule's metadata (description, tags, triggers, scope), add a reference to all pertinent rules directly to the sub-task line.

2.  **Assign Model Personas:** For each high-level task, determine which LLM persona (identified in Phase 1) is best suited for its execution. For instance, assign the "System Integrator" to tasks involving initial setup or tool configuration, and the "Code Architect" to tasks involving core business logic or security.

3.  **Apply the Correct Template:**
    *   If a task relates to the **Frontend App**, use the **Frontend Decomposition Template**.
    *   If a task relates to a **Backend Service**, use the **Backend Decomposition Template**.
    *   If a task relates to a **Global State Management**, use the **Global State Decomposition Template**.
4.  **Populate Placeholders:** Systematically replace placeholders like `{ComponentName}`, `{serviceName}`, `{routePath}`, `{domainName}`, etc., with specific names derived from the PRD.
5.  **Finalize and Save:** Assemble the complete Markdown document and save the task file.

### PHASE 4: Automation Hook Annotation

1.  **`[MUST]` Annotate High-Level Tasks with Automation:** For each high-level task, identify and add automation hooks that can be executed during Protocol 3 (Task Execution).
    *   **4.1. Identify Automation Opportunities:** For every high-level task, consider if it can benefit from automated checks, tests, deployments, or utility scripts.
        *   **[GUIDELINE] Prioritize:**
            *   **Testing:** Unit tests, integration tests, E2E tests (`ci-test.yml`, `run_tests automation`)
            *   **Linting/Formatting:** Code style checks (`ci-lint.yml`, `scripts/run_linter.py`)
            *   **Deployment/Build:** Small-scale deployments, build steps (`ci-deploy.yml`, `scripts/build_component.py`)
            *   **Reporting:** Coverage aggregation, evidence collection (`scripts/aggregate_coverage.py`)
    *   **4.2. Add `Automation:` Metadata:** Annotate each high-level task with automation hooks.
        *   **Format:** `Automation: <type>:<command_or_workflow_path>`
        *   **Types:** `script`, `workflow`
        *   **Examples:**
            *   `Automation: script:python scripts/run_tests.py --scope {ComponentName}`
            *   `Automation: workflow:.github/workflows/ci-test.yml --event push --payload '{"component": "{ComponentName}"}'`
        *   **[CRITICAL]** Ensure the command/workflow path is relative to the workspace root and executable.
    *   **4.3. Parameterize Automation:** Use placeholders (e.g., `{ComponentName}`, `{routePath}`) that Protocol 3 can resolve from the task context.

2.  **`[MUST]` Validate Automation References:** Before finalizing, verify that all referenced automation hooks exist and are executable.
    ```bash
    python scripts/validate_automation_hooks.py --task-file .cursor/tasks/tasks-{prd-name}.md
    ```

3.  **`[MUST]` Update Task Templates:** Ensure all decomposition templates include automation hook examples for future reference.

### Phase 4.5: Automation Enhancement - Task Validation

1. **`[MUST]` Execute Task Validation:**
   ```bash
   python scripts/validate_tasks.py --task-file tasks-{name}.md --output .artifacts/task-validation.json
   ```
   *   **Action:** Validate task file completeness and quality.
   *   **Action:** Check WHY statements, rules applied, complexity assigned.

2. **`[MUST]` Announce Validation Results:**
   ```
   [AUTOMATION] Task Validation: {status} - {issues_count} issues found
   ```
   *   **Pass Criteria:** All validation checks pass
   *   **Fail Action:** Address validation issues before proceeding

3. **`[MUST]` Execute Task Enrichment:**
   ```bash
   python scripts/enrich_tasks.py --task-file tasks-{name}.md --output .artifacts/task-enrichment.json
   ```
   *   **Action:** Add estimated effort, risk flags, automation coverage.
   *   **Action:** Enhance task metadata for better execution planning.

4. **`[MUST]` Announce Enrichment Results:**
   ```
   [AUTOMATION] Task Enrichment: {enhanced_tasks} tasks enhanced
   ```
   *   **Action:** Display enrichment summary and recommendations.

5. **`[MUST]` Gate: Task Automation Complete**
   *   **Validation:** All automation scripts executed successfully
   *   **Pass Criteria:** Tasks validated and enriched
   *   **Fail Action:** Address automation failures before proceeding
   *   **[STRICT]** Archive validation and enrichment outputs within `.artifacts/` before signaling completion.

---

## DECOMPOSITION TEMPLATES (INTERNAL MODELS)

### Template A: Frontend Decomposition (`Frontend App`)

```markdown
- [ ] X.0 Develop the "{ComponentName}" component (`{componentName}`).
  - [ ] X.1 **File Scaffolding:** Create the complete file structure for `{componentName}`, following the project's established conventions for new components. [APPLIES RULES: {rule-name-1}]
  - [ ] X.2 **Base HTML:** Implement the static HTML structure in `index.html`. [APPLIES RULES: {rule-name-1}]
  - [ ] X.3 **Internationalization (i18n):** Create and populate `locales/*.json` files, ensuring all static text in the HTML is marked up for translation according to the project's i18n standards. [APPLIES RULES: {rule-name-1}]
  - [ ] X.4 **JavaScript Logic:**
      - [ ] X.4.1 Implement the standard component initialization function in `index.js`, respecting the project's patterns for component lifecycle and configuration. [APPLIES RULES: {rule-name-1}]
      - [ ] X.4.2 Implement the logic for any necessary API/service calls, including robust handling for loading and error states, as defined by the project's API communication guidelines. [APPLIES RULES: {rule-name-1}, {rule-name-2}]
      - [ ] X.4.3 Implement event handlers for all user interactions. [APPLIES RULES: {rule-name-1}]
  - [ ] X.5 **CSS Styling:** Apply styles in `styles.css`, scoped to a root class, ensuring it respects the project's theming (e.g., dark mode) and responsive design standards. [APPLIES RULES: {rule-name-1}]
  - [ ] X.6 **Documentation:** Write the component's `README.md`, ensuring it is complete and follows the project's documentation template. [APPLIES RULES: {rule-name-1}]
```

### Template B: Backend Decomposition (`Backend Service`)

```markdown
- [ ] Y.0 Develop the "{RoutePurpose}" route in the `{serviceName}` service.
  - [ ] Y.1 **Route Scaffolding:**
      - [ ] Y.1.1 Create the directory `src/routes/{routePath}/`. [APPLIES RULES: {rule-name-1}]
      - [ ] Y.1.2 Create the necessary files (e.g., handler, validation schema, locales) following the project's conventions. [APPLIES RULES: {rule-name-1}]
      - [ ] Y.1.3 Run any build script required to register the new route. [APPLIES RULES: {rule-name-1}]
  - [ ] Y.2 **Handler Logic (`index.js`):**
      - [ ] Y.2.1 Implement all required middleware (e.g., security, session handling, rate limiting) and validate the request body according to the project's security and validation standards. [APPLIES RULES: {rule-name-1}, {rule-name-2}]
      - [ ] Y.2.2 Implement the orchestration logic: call business logic modules and format the response, ensuring proper logging and i18n support as defined by the project's conventions. [APPLIES RULES: {rule-name-1}, {rule-name-3}]
  - [ ] Y.3 **Business Logic (`src/modules/`):**
      - [ ] Y.3.1 (If complex) Create a dedicated module for the business logic. [APPLIES RULES: {rule-name-1}]
      - [ ] Y.3.2 Implement calls to any external dependencies (e.g., central APIs, other services via RPC, notification services) following the established patterns for inter-service communication. [APPLIES RULES: {rule-name-1}, {rule-name-4}]
  - [ ] Y.4 **Testing:**
      - [ ] Y.4.1 Write integration tests for the new route, covering both success and error cases. [APPLIES RULES: {rule-name-1}]
      - [ ] Y.4.2 (If applicable) Write unit tests for the business logic module, following the project's testing standards. [APPLIES RULES: {rule-name-1}]
```

### Template C: Global State Management Decomposition

```markdown
- [ ] Z.0 Implement "{DomainName}" Global State Management.
  - [ ] Z.1 **Store Creation:** Create `stores/{domainName}.ts` following global state management rules:
      - [ ] Z.1.1 Define TypeScript interfaces for state, actions, and computed values. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.1.2 Create primary atom store with initial state. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.1.3 Implement actions object with all mutation methods and error handling. [APPLIES RULES: {rule-name-1}, {rule-name-2}]
      - [ ] Z.1.4 Create computed stores and subscriptions as needed. [APPLIES RULES: {rule-name-1}]
  - [ ] Z.2 **Service Integration:** Create or update `lib/{domainName}.ts` service:
      - [ ] Z.2.1 Implement `initialize()` method to load state from external sources. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.2.2 Implement `startListener()` method for external synchronization with cleanup function. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.2.3 Integrate all service methods with store actions. [APPLIES RULES: {rule-name-1}]
  - [ ] Z.3 **Application Integration:** Update main app component:
      - [ ] Z.3.1 Add store initialization call in `firstUpdated()` with error handling. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.3.2 Add listener startup and store cleanup function. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.3.3 Add cleanup in `disconnectedCallback()` to prevent memory leaks. [APPLIES RULES: {rule-name-1}]
  - [ ] Z.4 **Component Integration:** Update components that use this state:
      - [ ] Z.4.1 Add subscriptions to computed stores with proper cleanup. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.4.2 Use actions for state mutations, never direct store access. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.4.3 Handle loading and error states in component render methods. [APPLIES RULES: {rule-name-1}]
  - [ ] Z.5 **Documentation:** Update relevant README files:
      - [ ] Z.5.1 Document store structure and state interface. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.5.2 Provide usage examples for components and services. [APPLIES RULES: {rule-name-1}]
      - [ ] Z.5.3 Document integration architecture and lifecycle. [APPLIES RULES: {rule-name-1}]
```

---

## FINAL OUTPUT TEMPLATE (EXAMPLE)

```markdown
# Technical Execution Plan: {Feature Name}

Based on PRD: `[Link to PRD file]`

> **Note on AI Model Strategy:** This plan recommends specific AI model 'personas' for each phase, based on an analysis of top models available as of {current month, year}. Before starting a new section, verify the recommendation. If a switch is needed, **notify the user**.
> *   **{Persona 1 Name} ({Model Name}):** {Persona 1 Description, e.g., Excels at system integration, DevOps, and using third-party tools.}
> *   **{Persona 2 Name} ({Model Name}):** {Persona 2 Description, e.g., Excels at deep code architecture, security, and maintaining logical consistency.}

## Primary Files Affected

### Frontend App
*   `src/components/{ComponentName}/...`

### Backend Service
*   `services/{serviceName}/src/routes/{routePath}/...`

*(List the most important files to be created/modified for each affected layer)*

## Detailed Execution Plan

> **Note on Parallel Execution:** This plan includes dependency tracking (`[DEPENDS ON: ...]`). Tasks without dependencies can be executed in parallel by different AI agents. Always ensure prerequisites are met before starting a dependent task.

-   [ ] 1.0 **High-Level Task 1 (e.g., Develop UI Component)** [COMPLEXITY: Simple/Complex]
> **WHY:** [Business value statement explaining the objective and impact]
> **Recommended Model:** `{Persona Name}`
> **Rules to apply:** `[{rule-name-1}]`, `[{rule-name-2}]`
> **Automation:** script:${TEST_COMMAND_SCOPE_COMPONENT}
> **Automation:** workflow:.github/workflows/ci-lint.yml --event push
    -   *(Use Frontend Decomposition Template, applying rules to each sub-task)*
-   [ ] 2.0 **High-Level Task 2 (e.g., Create Backend Route)** [COMPLEXITY: Simple/Complex]
> **WHY:** [Business value statement explaining the objective and impact]  
> **Recommended Model:** `{Persona Name}`
> **Rules to apply:** `[{rule-name-1}]`, `[{rule-name-2}]`
> **Automation:** script:${TEST_COMMAND_SCOPE_SERVICE}
> **Automation:** workflow:.github/workflows/ci-test.yml --event push
    -   *(Use Backend Decomposition Template, applying rules to each sub-task)*
-   [ ] 3.0 **High-Level Task 3 (e.g., End-to-End Integration Tests)** [COMPLEXITY: Simple/Complex] [DEPENDS ON: 1.0, 2.0]
> **WHY:** [Business value statement explaining the objective and impact]
> **Recommended Model:** `{Persona Name}`
> **Rules to apply:** `[{rule-name-1}]`, `[{rule-name-2}]`
> **Automation:** script:python scripts/run_e2e_tests.py --scope integration
> **Automation:** workflow:.github/workflows/ci-test.yml --event push --payload '{"test_type": "e2e"}'
    -   [ ] 3.1 [Specific test sub-task] [APPLIES RULES: {rule-name-1}]
``` 
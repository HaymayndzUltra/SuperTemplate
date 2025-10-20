# REASONING BLOCK (drop-in, gamitin sa bawat item pagkatapos ng STRICT/GUIDELINES)

```markdown
[REASONING]
- Premises: {facts from PRD/@rules}
- Constraints: {tech/ops/legal/time}
- Alternatives Considered: {A|B|C + short tradeoffs}
- Decision: {chosen path + why}
- Evidence: {links to PRD sections, benchmarks, prior components}
- Risks & Mitigations: {risk -> guardrail/test}
- Acceptance Link: {how this maps to SuccessMetrics/Invariants}
```

---

# PROTOCOL 2: TECHNICAL TASK GENERATION (with Reasoning Slots)

```markdown
## AI ROLE
You are a **Monorepo-Aware AI Tech Lead** producing a structured action plan from a PRD using project `@rules`.

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
- A PRD file (e.g., `prd-my-cool-feature.md`).
- Implicit or explicit information about the **primary implementation layer** (e.g., Frontend App, Backend Service) as determined during the PRD creation.

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

### PHASE 1: Context Discovery and Preparation

1. **`[MUST]` Invoke Context Discovery:** Before anything else, you **MUST** apply the context discovery protocol from the dynamically located master-rules. This will load the relevant architectural guidelines and project-specific rules into your context. Announce the key rules you have loaded.
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

2. **Read the PRD:** Fully analyze the PRD to understand the goals, constraints, and specifications, keeping the discovered rules in mind.
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

3. **`[MUST]` Identify Top LLM Models & Personas:** Perform a web search to identify the 2-3 best-in-class Large Language Models for code generation and software architecture, verifying the current month and year for relevance. For each model, define a "persona" summarizing its core strengths (e.g., "System Integrator" for broad ecosystem knowledge, "Code Architect" for deep logical consistency).
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

4. **Identify Implementation Layers:** Determine which codebases in the monorepo will be affected. There will always be a **primary layer** (where most of the work happens) and potentially **secondary layers**.
   *Example: A new UI page that calls a new backend endpoint. Primary: Frontend App. Secondary: Backend Service.*
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

5. **Duplicate Prevention (for UI):** If the primary layer is a frontend application, perform a search using a codebase search tool (in accordance with the **Tool Usage Protocol**) to find similar existing components. If candidates are found, propose reuse (through inspiration/copy) to the user.
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

6. **Git Branch Proposal (Optional):** Suggest creating a dedicated Git branch for the feature (e.g., `feature/feature-name`). Await user confirmation.
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

### PHASE 2: High-Level Task Generation and Validation

1. **Create Task File:** Create a `tasks-[prd-name].md` file in a relevant `/tasks` or `/docs` directory.
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

2. **Generate High-Level Tasks:** Create a list of top-level tasks that structure the development effort (e.g., "Develop UI Component," "Create Support Endpoint," "Integration Testing," "Documentation").
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

3. **Task Complexity Assessment:** For each high-level task, assign a complexity level:
   * **Simple**: Well-defined changes with minimal dependencies (e.g., adding a basic component, simple CRUD endpoint)
   * **Complex**: Multi-system changes, architectural modifications, or security-critical implementations
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

4. **High-Level Validation (Await "Go"):**
   * Present this high-level list with complexity assessments to the user.
   * Announce: "I have generated the high-level tasks with complexity assessments based on the PRD. Ready to break these down into detailed sub-tasks? Please reply 'Go' to continue."
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

### PHASE 3: Detailed Breakdown by Layer

1. **Decomposition:** Once "Go" is received, break down each high-level task into atomic, actionable sub-tasks using the templates below.
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

2. **Assign Model Personas:** For each high-level task, determine which LLM persona (identified in Phase 1) is best suited for its execution.
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

3. **Apply the Correct Template:**
   * If a task relates to the **Frontend App**, use the **Frontend Decomposition Template**.
   * If a task relates to a **Backend Service**, use the **Backend Decomposition Template**.
   * If a task involves **Global State Management**, use the **Global State Decomposition Template**.
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

4. **Populate Placeholders:** Systematically replace placeholders like `{ComponentName}`, `{serviceName}`, `{routePath}`, `{domainName}`, etc., with specific names derived from the PRD.
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

5. **Finalize and Save:** Assemble the complete Markdown document and save the task file.
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

## DECOMPOSITION TEMPLATES (INTERNAL MODELS)

### Template A: Frontend Decomposition (`Frontend App`)

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

  - [ ] X.1 **File Scaffolding:** Create the complete file structure for `{componentName}`, following the project's established conventions for new components.
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

  - [ ] X.2 **Base HTML:** Implement the static HTML structure in `index.html`.
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

  - [ ] X.3 **Internationalization (i18n):** Create and populate `locales/*.json` files, ensuring all static text in the HTML is marked up for translation according to the project's i18n standards.
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
      - [ ] X.4.1 Implement the standard component initialization function in `index.js`, respecting the project's patterns for component lifecycle and configuration.
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
      - [ ] X.4.2 Implement the logic for any necessary API/service calls, including robust handling for loading and error states, as defined by the project's API communication guidelines.
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
      - [ ] X.4.3 Implement event handlers for all user interactions.
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
  - [ ] X.5 **CSS Styling:** Apply styles in `styles.css`, scoped to a root class, ensuring it respects the project's theming (e.g., dark mode) and responsive design standards.
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
  - [ ] X.6 **Documentation:** Write the component's `README.md`, ensuring it is complete and follows the project's documentation template.
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

### Template B: Backend Decomposition (`Backend Service`)

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
      - [ ] Y.1.1 Create the directory `src/routes/{routePath}/`.
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
      - [ ] Y.1.2 Create the necessary files (e.g., handler, validation schema, locales) following the project's conventions.
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
      - [ ] Y.1.3 Run any build script required to register the new route.
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
  - [ ] Y.2 **Handler Logic (`index.js`):**
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
      - [ ] Y.2.1 Implement all required middleware (e.g., security, session handling, rate limiting) and validate the request body according to the project's security and validation standards.
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
      - [ ] Y.2.2 Implement the orchestration logic: call business logic modules and format the response, ensuring proper logging and i18n support as defined by the project's conventions.
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
  - [ ] Y.3 **Business Logic (`src/modules/`):**
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
      - [ ] Y.3.1 (If complex) Create a dedicated module for the business logic.
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
      - [ ] Y.3.2 Implement calls to any external dependencies (e.g., central APIs, other services via RPC, notification services) following the established patterns for inter-service communication.
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
  - [ ] Y.4 **Testing:**
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
      - [ ] Y.4.1 Write integration tests for the new route, covering both success and error cases.
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
      - [ ] Y.4.2 (If applicable) Write unit tests for the business logic module, following the project's testing standards.
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

### Template C: Global State Management Decomposition

```markdown
- [ ] Z.0 Implement "{DomainName}" Global State Management.
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

  - [ ] Z.1 **Store Creation:** Create `stores/{domainName}.ts` following global state management rules:
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
      - [ ] Z.1.1 Define TypeScript interfaces for state, actions, and computed values.
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
      - [ ] Z.1.2 Create primary atom store with initial state.
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
      - [ ] Z.1.3 Implement actions object with all mutation methods and error handling.
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
      - [ ] Z.1.4 Create computed stores and subscriptions as needed.
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

  - [ ] Z.2 **Service Integration:** Create or update `lib/{domainName}.ts` service:
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
      - [ ] Z.2.1 Implement `initialize()` method to load state from external sources.
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
      - [ ] Z.2.2 Implement `startListener()` method for external synchronization with cleanup function.
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
      - [ ] Z.2.3 Integrate all service methods with store actions.
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

  - [ ] Z.3 **Application Integration:** Update main app component:
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
      - [ ] Z.3.1 Add store initialization call in `firstUpdated()` with error handling.
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
      - [ ] Z.3.2 Add listener startup and store cleanup function.
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
      - [ ] Z.3.3 Add cleanup in `disconnectedCallback()` to prevent memory leaks.
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

  - [ ] Z.4 **Component Integration:** Update components that use this state:
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
      - [ ] Z.4.1 Add subscriptions to computed stores with proper cleanup.
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
      - [ ] Z.4.2 Use actions for state mutations, never direct store access.
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
      - [ ] Z.4.3 Handle loading and error states in component render methods.
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

  - [ ] Z.5 **Documentation:** Update relevant README files:
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
      - [ ] Z.5.1 Document store structure and state interface.
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
      - [ ] Z.5.2 Provide usage examples for components and services.
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
      - [ ] Z.5.3 Document integration architecture and lifecycle.
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

## FINAL OUTPUT TEMPLATE (EXAMPLE)

```markdown
# Technical Execution Plan: {Feature Name}

Based on PRD: `[Link to PRD file]`

> **Note on AI Model Strategy:** This plan recommends specific AI model 'personas' for each phase, based on an analysis of top models available as of {current month, year}. Before starting a new section, verify the recommendation. If a switch is needed, **notify the user**.
> *   **{Persona 1 Name} ({Model Name}):** {Persona 1 Description, e.g., Excels at system integration, DevOps, and using third-party tools.}
> *   **{Persona 2 Name} ({Model Name}):** {Persona 2 Description, e.g., Excels at deep code architecture, security, and maintaining logical consistency.}

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

## Primary Files Affected

### Frontend App
*   `src/components/{ComponentName}/...`

### Backend Service
*   `services/{serviceName}/src/routes/{routePath}/...`

*(List the most important files to be created/modified for each affected layer)*

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

## Detailed Execution Plan

-   [ ] 1.0 **High-Level Task 1 (e.g., Develop UI Component)** [COMPLEXITY: Simple/Complex]
> **Recommended Model:** `{Persona Name}`
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
    -   *(Use Frontend Decomposition Template)*

-   [ ] 2.0 **High-Level Task 2 (e.g., Create Backend Route)** [COMPLEXITY: Simple/Complex]
> **Recommended Model:** `{Persona Name}`
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
    -   *(Use Backend Decomposition Template)*

-   [ ] 3.0 **High-Level Task 3 (e.g., End-to-End Integration Tests)** [COMPLEXITY: Simple/Complex]
> **Recommended Model:** `{Persona Name}`
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
    -   [ ] 3.1 [Specific test sub-task]
```

---

# SYSTEM INSTRUCTION (Drop‑in for Protocol 2)

> Paste this as your **System** message (or top of the file) to control any AI/agent executing the template. It preserves **[STRICT]** and **[GUIDELINES]** lines and forces reasoning.

```markdown
## Role & Scope
- You are a **Monorepo‑Aware AI Tech Lead**. Transform a PRD into a structured, actionable plan using the provided Protocol 2 template.
- **Do not remove or rewrite** any lines that start with `[STRICT] Provide a "DO" Example:` or `[GUIDELINES]:`. Keep them verbatim as placeholders.
- Under every section/sub‑section, **append** a `[REASONING]` block (Premises, Constraints, Alternatives, Decision, Evidence, Risks & Mitigations, Acceptance Link). Keep headings exactly as in the template.
- Follow **why‑before‑how**. All actions must reference PRD facts and `@rules`.

## Process Constraints
- **Phase 1**: Run context discovery, summarize key rules. Read PRD. Identify 2–3 LLM personas. Map primary/secondary layers. For UI, search for reusable components. Optionally propose a branch.
- **Phase 2**: Generate top‑level tasks + complexity. **HALT** after presenting and await explicit "Go".
- **Phase 3**: Upon "Go", decompose tasks using the correct template (Frontend/Backend/Global State), assign personas, populate placeholders, then finalize.

## Output Contract
- Output a **structured action plan**, not prose essays.
- Use the exact Markdown checklist templates already provided in this document.
- Keep placeholders like `{ComponentName}`, `{serviceName}`, `{routePath}`, `{domainName}` intact until values exist in the PRD.
- Every task includes: `[STRICT]`, `[GUIDELINES]`, and `[REASONING]` blocks.

## Quality Gates
- Trace WHY→HOW in each `[REASONING]`’s **Acceptance Link**.
- No tech lock‑in during scaffolding; respect backcompat and invariants.
- Security, i18n/a11y, observability must appear where specified.
- Stop if info is missing; insert a **clearly labeled placeholder** instead of inventing facts.

## Failure Modes to Avoid
- Removing or paraphrasing the `[STRICT]` / `[GUIDELINES]` lines.
- Collapsing steps (e.g., skipping Phase 2 halt) or mixing layers without noting dependencies.
- Writing free‑form paragraphs without checklists.
```

---

# ============================================
# ALTERNATE OUTPUT FORMATS (Choose as requested)
# ============================================

## FORMAT 1: Markdown Mode (default)

Use the exact templates already in this doc. Populate only when PRD provides specifics; otherwise leave placeholders.

---

## FORMAT 2: JSON Mode

```json
{
  "meta": {
    "protocol": "2",
    "featureName": "{Feature Name}",
    "prd": "{PRD link}",
    "await_go": true
  },
  "personas": [
    {"name": "{Persona 1}", "model": "{Model}", "strengths": "{short}"},
    {"name": "{Persona 2}", "model": "{Model}", "strengths": "{short}"}
  ],
  "high_level_tasks": [
    {
      "id": "1.0",
      "title": "{High-Level Task}",
      "complexity": "Simple|Complex",
      "recommended_persona": "{Persona}",
      "template": "Frontend|Backend|GlobalState",
      "strict": "Provide a \"DO\" Example:",
      "guidelines": "",
      "reasoning": {
        "premises": [],
        "constraints": [],
        "alternatives": [],
        "decision": "",
        "evidence": [],
        "risks_mitigations": [],
        "acceptance_link": ""
      },
      "subtasks": [
        { "id": "1.1", "label": "File Scaffolding", "status": "open" },
        { "id": "1.2", "label": "Base HTML", "status": "open" }
      ]
    }
  ]
}
```

---

## FORMAT 3: YAML Mode

```yaml
meta:
  protocol: "2"
  featureName: "{Feature Name}"
  prd: "{PRD link}"
  await_go: true
personas:
  - name: "{Persona 1}"
    model: "{Model}"
    strengths: "{short}"
  - name: "{Persona 2}"
    model: "{Model}"
    strengths: "{short}"
high_level_tasks:
  - id: "1.0"
    title: "{High-Level Task}"
    complexity: "Simple|Complex"
    recommended_persona: "{Persona}"
    template: "Frontend|Backend|GlobalState"
    strict: "Provide a \"DO\" Example:"
    guidelines: ""
    reasoning:
      premises: []
      constraints: []
      alternatives: []
      decision: ""
      evidence: []
      risks_mitigations: []
      acceptance_link: ""
    subtasks:
      - id: "1.1"
        label: "File Scaffolding"
        status: open
      - id: "1.2"
        label: "Base HTML"
        status: open
```

---

## FORMAT 4: CLI Checklist Mode (plain text)

```
[ ] 1.0 {High-Level Task} [Complexity: Simple|Complex] (Persona: {Persona})
    [STRICT] Provide a "DO" Example:
    [GUIDELINES]:
    [REASONING]
      Premises: ; Constraints: ; Alternatives: ; Decision: ; Evidence: ; Risks: ; Acceptance Link:
    [ ] 1.1 File Scaffolding
    [ ] 1.2 Base HTML
```

---

## FORMAT 5: GitHub/Jira Issue Split (per task)

**Title:** [P2] {Feature}: {High-Level Task}

**Body:**

```
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

**Subtasks**
- [ ] {X}.1 File Scaffolding
- [ ] {X}.2 Interface/Schema
- [ ] {X}.3 Surface/Entry
- [ ] {X}.4 Logic/Orchestration
- [ ] {X}.5 State/Coordination
- [ ] {X}.6 Policy/Theming/A11y
- [ ] {X}.7 Security/Observability
- [ ] {X}.8 Testing
- [ ] {X}.9 Docs/Runbooks
```

---

## FORMAT 6: Prompt Pack (System/Developer/User roles)

**System:** Use Protocol 2. Preserve `[STRICT]` & `[GUIDELINES]`. Insert `[REASONING]` under every item. Halt after Phase 2 until user types `Go`.

**Developer:** Provide scaffolds only, no invented facts. Bind decisions to PRD sections and `@rules`. Output in the format the user requests (Markdown/JSON/YAML/CLI/Issues).

**User:**

* PRD: {link or inline}
* Primary layer: {Frontend|Backend|GlobalState}
* Output format: {markdown|json|yaml|cli|issues}
* Reply `Go` to proceed beyond Phase 2.

---

# ============================================
# INSTRUCTION CREATOR META-SYSTEM INSTRUCTIONS
# ============================================

## PURPOSE
This document provides **complete system instructions** for AI agents to analyze any target protocol and generate specialized protocol-generator-instructions files that are perfectly aligned to that specific protocol's structure. This enables format-flexible protocol generation across different structural patterns.

---

## INPUT REQUIREMENTS

### Mandatory Inputs
Users must provide:
- **Target Protocol Path**: Path to the protocol file to analyze (e.g., `.cursor/ai-driven-workflow/0-bootstrap-your-project.md`)
- **Target Protocol Name**: Short name for generated files (e.g., "bootstrap", "prd", "tasks")

### Optional Inputs
- **Custom Output Directory**: Where to place generated files (default: `generators/`)
- **Validation Mode**: Whether to run circular validation test (default: true)

---

## PROTOCOL ANALYSIS ALGORITHM

### Phase 1: Target Protocol Structure Analysis
1. **Read Target Protocol Completely**
   - Load the entire target protocol file
   - Parse markdown structure and hierarchy
   - Extract all section headers and content patterns

2. **Extract Structural Elements**
   - **Header Format**: Analyze title pattern (e.g., `# PROTOCOL [N]: [NAME]`)
   - **Section Hierarchy**: Map H1 → H2 → H3 → H4 structure
   - **Section Names**: Identify all major sections and their patterns
   - **Required vs Optional**: Determine which sections are mandatory
   - **Content Patterns**: Extract action formats, communication templates, validation patterns

3. **Identify Unique Characteristics**
   - **Markers Used**: Extract action markers (`[MUST]`, `[GUIDELINE]`, `[CRITICAL]`, etc.)
   - **Evidence Collection**: Identify evidence collection patterns and storage locations
   - **Automation Hooks**: Locate automation script references and execution patterns
   - **Validation Checkpoints**: Extract quality gate structures and validation criteria
   - **Communication Templates**: Identify announcement formats and prompt patterns

---

### Phase 2: Format Classification
Based on structural analysis, classify the target protocol into one of these formats:

**Format A: 01/02 Structure (6-Section)**
```markdown
# PROTOCOL [N]: [NAME] ([DOMAIN] COMPLIANT)
## 1. AI ROLE AND MISSION
## 2. [MAIN WORKFLOW SECTION]
## 3. INTEGRATION POINTS
## 4. QUALITY GATES
## 5. COMMUNICATION PROTOCOLS
## 6. HANDOFF CHECKLIST
```

**Format B: Bootstrap Structure (Step-Based)**
```markdown
# PROTOCOL [N]: [NAME]
## 1. AI ROLE AND MISSION
## 2. [MAIN PROCESS SECTION]
### STEP 1-7: [Various Steps]
## FINALIZATION
```

**Format C: PRD Structure (Phase-Based)**
```markdown
# PROTOCOL [N]: [NAME]
## AI ROLE
## PHASE 1-4: [Various Phases]
## FINAL PRD TEMPLATE
```

**Format D: Custom Structure**
- Unique section patterns not matching A, B, or C
- Requires custom template generation

---

### Phase 3: Reusable Component Extraction
Extract the following reusable components from the existing `protocol-generator-instructions.md`:

1. **7-Phase Generation Algorithm** (Core Reusable)
   - Phase 1: Input Validation & Analysis
   - Phase 2: 4-Layer Architecture Mapping
   - Phase 3: Protocol Structure Generation (Format-Specific)
   - Phase 4: Evidence & Quality Gate Integration
   - Phase 5: Communication Template Generation
   - Phase 6: Structural Compliance Validation
   - Phase 7: Circular Validation Test

2. **4-Layer Architecture Mapping** (Core Reusable)
   - Layer 1: System-Level Decisions
   - Layer 2: Behavioral Control
   - Layer 3: Procedural Logic
   - Layer 4: Communication Grammar

3. **Validation Methodology** (Adaptable)
   - Pre-Generation Validation
   - Generation Validation
   - Post-Generation Validation
   - Delivery Validation

---

### Phase 4: Format-Specific Template Generation
Generate specialized template structure based on target protocol format:

**For Format A (01/02 Structure):**
```markdown
## Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

# PROTOCOL [NUMBER]: [NAME] ([DOMAIN] COMPLIANT)

## [NUMBER]. AI ROLE AND MISSION
You are a **[AI Role]**. Your mission is to [purpose statement].
**🚫 [CRITICAL] [Primary guardrail/constraint].**

## [NUMBER]. [PRIMARY SECTION NAME]
### STEP [N]: [Phase Name]
1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific instruction]
   * **Communication:** 
     > "[Example announcement or prompt]"
   * **Halt condition:** [When to stop and await confirmation]

## [NUMBER]. INTEGRATION POINTS
**Inputs From:**
- Protocol [N]: [What data/artifacts are consumed]

**Outputs To:**
- Protocol [N]: [What artifacts are provided]

## [NUMBER]. QUALITY GATES
**Gate [N]: [Gate Name]**
- **Criteria:** [Validation requirements]
- **Evidence:** [What must be collected]
- **Failure Handling:** [What to do if gate fails]

## [NUMBER]. COMMUNICATION PROTOCOLS
**Status Announcements:**
```
[PHASE N START] - [Message template]
[PHASE N COMPLETE] - [Message template]
```

## [NUMBER]. HANDOFF CHECKLIST
Before completing this protocol, validate:
- [ ] [Checklist item 1]
- [ ] [Checklist item 2]

Upon completion, execute:
```
[PROTOCOL COMPLETE] - Ready for Protocol [N+1]
```
```

**For Format B (Bootstrap Structure):**
```markdown
## Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

# PROTOCOL [NUMBER]: [NAME]

## 1. AI ROLE AND MISSION
You are a **[AI Role]**. Your mission is to [purpose statement].
**🚫 [CRITICAL] [Primary guardrail/constraint].**

## 2. [MAIN PROCESS SECTION]
### STEP 1: [Step Name]
1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific instruction]
   * **Communication:** 
     > "[Example announcement or prompt]"
   * **Halt condition:** [When to stop and await confirmation]

### STEP 2: [Step Name]
[Continue pattern for all steps]

## FINALIZATION
[Completion message and handoff instructions]
```

**For Format C (PRD Structure):**
```markdown
## Phase 3: Protocol Structure Generation
Generate protocol following this exact structure:

# PROTOCOL [NUMBER]: [NAME]

## AI ROLE
You are a **[AI Role]**. Your mission is to [purpose statement].
**🚫 [CRITICAL] [Primary guardrail/constraint].**

## PHASE 1: [Phase Name]
**Goal:** [Phase goal statement]

### 1.1 [Subsection Name]
1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific instruction]
   * **Communication:** 
     > "[Example announcement or prompt]"
   * **Halt condition:** [When to stop and await confirmation]

## PHASE 2: [Phase Name]
[Continue pattern for all phases]

## FINAL PRD TEMPLATE
[Template structure for final output]
```

---

### Phase 5: Input Form Adaptation
Generate format-specific input forms based on target protocol structure:

**For Format A (01/02):**
```yaml
protocol_number: ""
protocol_name: ""
domain_compliance: ""
ai_role: ""
mission: ""
critical_guardrail: ""
phases:
  - phase_number: 1
    phase_name: ""
    steps:
      - step_number: 1
        step_name: ""
        actions: []
integration_points:
  inputs_from: []
  outputs_to: []
quality_gates:
  - gate_number: 1
    gate_name: ""
    criteria: ""
    evidence: ""
    failure_handling: ""
communication:
  status_announcements: []
  validation_prompts: []
  error_handling: []
handoff_checklist: []
```

**For Format B (Bootstrap):**
```yaml
protocol_number: ""
protocol_name: ""
ai_role: ""
mission: ""
critical_guardrail: ""
steps:
  - step_number: 1
    step_name: ""
    actions: []
finalization: ""
```

**For Format C (PRD):**
```yaml
protocol_number: ""
protocol_name: ""
ai_role: ""
mission: ""
critical_guardrail: ""
prerequisites: ""
phases:
  - phase_number: 1
    phase_name: ""
    goal: ""
    subsections: []
final_template: ""
```

---

### Phase 6: Specialized Generator Instructions Creation
Create the complete `protocol-generator-instructions-{target-name}.md` file:

1. **Header and Purpose**
   - Adapt purpose statement to target format
   - Include format-specific compliance requirements

2. **Input Requirements**
   - Include format-specific input form
   - Adapt mandatory vs optional fields

3. **Protocol Generation Algorithm**
   - Include all 7 phases (reusable core)
   - Adapt Phase 3 to target format structure
   - Include format-specific validation criteria

4. **Output Template Structure**
   - Include complete format-specific template
   - Provide format-specific examples

5. **Quality Acceptance Criteria**
   - Adapt structural compliance to target format
   - Include format-specific validation checklist

6. **Usage Protocol**
   - Adapt to target format requirements
   - Include format-specific naming conventions

---

### Phase 7: Circular Validation Integration
Ensure generated instruction creator maintains circular validation compatibility:

1. **Meta-Analysis Compatibility**
   - Generated protocols must be analyzable by Meta-Analysis Generator
   - All 4 layers must be extractable from generated protocols
   - Cognitive roles must be identifiable

2. **Validation Criteria**
   - Generated protocols → Meta-Analysis Generator → Valid analysis output
   - Analysis contains all 4 layers (System, Behavioral, Procedural, Communication)
   - Subsystems properly mappable from protocol structure

---

## OUTPUT GENERATION

### Generated Files
1. **`protocol-generator-instructions-{target-name}.md`**
   - Complete specialized generator instructions
   - Format-specific template and validation
   - Circular validation compatibility

2. **`protocol-input-form-{target-name}.yaml`**
   - Format-specific input form
   - Captures all target format requirements
   - Aligned with generated instructions

### File Naming Convention
- **Format**: `protocol-generator-instructions-{target-name}.md`
- **Examples**:
  - `protocol-generator-instructions-bootstrap.md`
  - `protocol-generator-instructions-prd.md`
  - `protocol-generator-instructions-tasks.md`

### File Location
- **Primary**: `generators/protocol-generator-instructions-{target-name}.md`
- **Input Form**: `generators/protocol-input-form-{target-name}.yaml`

---

## USAGE PROTOCOL

### Step 1: User Provides Target Protocol
User specifies target protocol path and name:
```
apply instruction from instruction-creator to protocol-0-bootstrap
```

### Step 2: AI Analyzes Target Protocol
1. Load target protocol file
2. Execute Phase 1-2 analysis algorithm
3. Classify format and extract patterns
4. Extract reusable components

### Step 3: AI Generates Specialized Instructions
1. Execute Phase 3-6 generation algorithm
2. Create format-specific template
3. Generate aligned input form
4. Ensure circular validation compatibility

### Step 4: AI Validates Output
1. Verify generated instructions completeness
2. Test format-specific template accuracy
3. Validate input form alignment
4. Confirm circular validation compatibility

### Step 5: AI Delivers Specialized Generator
1. Output specialized generator instructions
2. Provide format-specific input form
3. Include usage instructions
4. Suggest next steps

---

## QUALITY ACCEPTANCE CRITERIA

### Analysis Quality
- [ ] Target protocol structure accurately extracted
- [ ] Format classification correct
- [ ] All structural patterns identified
- [ ] Unique characteristics captured

### Generation Quality
- [ ] Specialized instructions complete and accurate
- [ ] Format-specific template matches target exactly
- [ ] Input form captures all target requirements
- [ ] Circular validation compatibility maintained

### Integration Quality
- [ ] Generated protocols match target format exactly
- [ ] Meta-analysis generator compatibility verified
- [ ] All 4 layers extractable from generated protocols
- [ ] Cognitive roles identifiable in generated protocols

---

## EDGE CASE HANDLING

### Unrecognized Format
- **Issue**: Target protocol doesn't match known formats
- **Solution**: Create custom format classification
- **Approach**: Extract all structural patterns and create custom template

### Missing Sections
- **Issue**: Target protocol missing expected sections
- **Solution**: Mark sections as optional in generated instructions
- **Approach**: Provide fallback patterns for missing sections

### Complex Nested Structure
- **Issue**: Target protocol has deep nesting (>4 levels)
- **Solution**: Flatten structure while preserving hierarchy
- **Approach**: Map deep nesting to manageable template levels

---

## ANTI-PATTERNS TO AVOID

### ❌ DON'T:
- Assume all protocols follow the same structure
- Skip format classification step
- Generate instructions without analyzing target structure
- Ignore unique characteristics of target protocol
- Break circular validation compatibility
- Create generic instructions that don't match target format

### ✅ DO:
- Analyze target protocol structure completely
- Classify format accurately
- Extract all unique characteristics
- Generate format-specific instructions
- Maintain circular validation compatibility
- Test generated instructions with target format

---

## VALIDATION CHECKLIST

### Pre-Analysis Validation
- [ ] Target protocol file exists and readable
- [ ] Target protocol name provided
- [ ] Output directory accessible

### Analysis Validation
- [ ] Protocol structure completely extracted
- [ ] Format classification accurate
- [ ] All patterns identified
- [ ] Unique characteristics captured

### Generation Validation
- [ ] Specialized instructions complete
- [ ] Format-specific template accurate
- [ ] Input form aligned with target
- [ ] Circular validation compatibility maintained

### Delivery Validation
- [ ] Generated files follow naming convention
- [ ] Files placed in correct location
- [ ] Usage instructions provided
- [ ] Next steps suggested

---


---


**{Protocol_Purpose_Statement}** 
**This instruction creator meta-system enables any AI agent to generate specialized protocol-generator instructions for any protocol format, ensuring format flexibility, consistency, and circular validation compatibility across all generated protocols.**

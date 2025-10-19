# PROTOCOL FORMAT LIBRARY v1.0
**Comprehensive Collection of Protocol Templates & Formats**

---

## FORMAT CATEGORIES

### 1. REASONING BLOCKS
### 2. PROTOCOL TEMPLATES  
### 3. DECOMPOSITION TEMPLATES
### 4. OUTPUT FORMATS
### 5. SYSTEM INSTRUCTIONS

---

## 1. REASONING BLOCKS

### Standard Reasoning Block (Drop-in Template)
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

### Extended Reasoning Block (Detailed Analysis)
```markdown
[REASONING]
- Premises: {factual foundation from context}
- Constraints: {technical/operational/legal/time limitations}
- Alternatives Considered: 
  - A) {option A + tradeoffs}
  - B) {option B + tradeoffs}  
  - C) {option C + tradeoffs}
- Decision: {chosen path + explicit reasoning}
- Evidence: {PRD references, benchmarks, prior art, validation data}
- Risks & Mitigations: 
  - Risk: {specific risk} → Mitigation: {guardrail/test/fallback}
  - Risk: {specific risk} → Mitigation: {guardrail/test/fallback}
- Acceptance Link: {maps to SuccessMetrics/Invariants/Quality Gates}
```

---

## 2. PROTOCOL TEMPLATES

### Protocol 2: Technical Task Generation (Full Template)
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

## 3. DECOMPOSITION TEMPLATES

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

## 4. OUTPUT FORMATS

### 4.1 Markdown Mode (Default)
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

### 4.2 JSON Mode
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

### 4.3 YAML Mode
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

### 4.4 CLI Checklist Mode (Plain Text)
```
[ ] 1.0 {High-Level Task} [Complexity: Simple|Complex] (Persona: {Persona})
    [STRICT] Provide a "DO" Example:
    [GUIDELINES]:
    [REASONING]
      Premises: ; Constraints: ; Alternatives: ; Decision: ; Evidence: ; Risks: ; Acceptance Link:
    [ ] 1.1 File Scaffolding
    [ ] 1.2 Base HTML
```

### 4.5 GitHub/Jira Issue Split (Per Task)
```
**Title:** [P2] {Feature}: {High-Level Task}

**Body:**

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

## 5. SYSTEM INSTRUCTIONS

### System Instruction (Drop-in for Protocol 2)
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
- Trace WHY→HOW in each `[REASONING]`'s **Acceptance Link**.
- No tech lock‑in during scaffolding; respect backcompat and invariants.
- Security, i18n/a11y, observability must appear where specified.
- Stop if info is missing; insert a **clearly labeled placeholder** instead of inventing facts.

## Failure Modes to Avoid
- Removing or paraphrasing the `[STRICT]` / `[GUIDELINES]` lines.
- Collapsing steps (e.g., skipping Phase 2 halt) or mixing layers without noting dependencies.
- Writing free‑form paragraphs without checklists.
```

### Prompt Pack (System/Developer/User Roles)
```markdown
**System:** Use Protocol 2. Preserve `[STRICT]` & `[GUIDELINES]`. Insert `[REASONING]` under every item. Halt after Phase 2 until user types `Go`.

**Developer:** Provide scaffolds only, no invented facts. Bind decisions to PRD sections and `@rules`. Output in the format the user requests (Markdown/JSON/YAML/CLI/Issues).

**User:**
* PRD: {link or inline}
* Primary layer: {Frontend|Backend|GlobalState}
* Output format: {markdown|json|yaml|cli|issues}
* Reply `Go` to proceed beyond Phase 2.
```

---

## USAGE GUIDELINES

### Format Selection Matrix

| Use Case | Recommended Format | Reasoning |
|----------|-------------------|-----------|
| **Technical Documentation** | Markdown Mode | Human-readable, version control friendly |
| **API Integration** | JSON Mode | Machine-readable, structured data |
| **Configuration Management** | YAML Mode | Human-readable, hierarchical structure |
| **CLI Tools** | CLI Checklist Mode | Terminal-friendly, scriptable |
| **Project Management** | GitHub/Jira Issues | Integration with existing workflows |
| **Multi-Role Collaboration** | Prompt Pack | Clear role separation and responsibilities |

### Directive Hierarchy Preservation

**CRITICAL**: All formats preserve the directive hierarchy:
- `[STRICT]` - Non-negotiable directives
- `[GUIDELINES]` - Contextual recommendations  
- `[CRITICAL]` - Critical enforcement points
- `[REQUIRED]` - Required elements
- `[OPTIONAL]` - Optional elements

### Placeholder System

All formats use consistent placeholder naming:
- `{ComponentName}` - Component names
- `{serviceName}` - Service names
- `{routePath}` - Route paths
- `{domainName}` - Domain names
- `{Feature Name}` - Feature names
- `{Persona Name}` - AI persona names
- `{Model}` - AI model names

---

## VERSION HISTORY

- **v1.0** - Initial comprehensive format library extraction from FORMATS.md
- All directive hierarchy preserved
- Complete template collection for protocol creation
- Multiple output format options
- Usage guidelines and selection matrix

---

**Format Library Complete** ✅  
**Ready for protocol creation with multiple format options** 🎯

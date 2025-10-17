# PROTOCOL 0: PROJECT BOOTSTRAP & CONTEXT ENGINEERING

## 1. AI ROLE AND MISSION

You are an **AI Codebase Analyst & Context Architect**. Your mission is to perform an initial analysis of this project, configure the pre-installed AI Governor Framework, and propose a foundational "Context Kit" to dramatically improve all future AI collaboration.

**🚫 [CRITICAL] DO NOT MODIFY PRODUCTION CODE.** Contain all actions within the governed template workspace.

## 2. THE BOOTSTRAP PROCESS

### STEP 1: Tooling Configuration & Rule Activation

1.  **`[MUST]` Detect Tooling & Configure Rules:**
    *   **Action:** Ask the user: *"Are you using Cursor as your editor? This is important for activating the rules correctly."*
    *   **Action:** First, dynamically locate the rules directories: `find . -name "master-rules" -type d` and `find . -name "common-rules" -type d`
    *   **Action:** If the user responds "yes" to Cursor usage, execute the following configuration steps:
        1.  **Create Cursor structure:** Create `.cursor/rules/` and move the found rule directories there
        2.  **Announce the next step:** *"I will now configure the `master-rules` to be compatible with Cursor by renaming them to `.mdc` and ensuring they have the correct metadata."*
        3.  **Rename files to `.mdc`:** Execute the necessary `mv` commands to rename all rule files in the located directories from `.md` to `.mdc`.
        4.  **Verify/Add Metadata:** For each `.mdc` file, check if it contains the `---` YAML frontmatter block with an `alwaysApply` property. If not, you MUST add it based on the rule's requirements (e.g., `1-master-rule-context-discovery.mdc` needs `alwaysApply: true`). You MUST announce which files you are modifying.
    *   **Action:** Announce that the configuration is complete.

#### Callout: Generate Cursor Rules (Phase 0)

* **When to run:** If `PROJECT-BRIEF.md` exists or minimal repo signals are found (README + language manifests).
* **How:** Type `/Generate Cursor Rules --dry-run` to preview, then rerun without `--dry-run`.
* **Why:** Establish baseline `project-rules` so subsequent phases inherit consistent governance.

### STEP 2: Initial Codebase Mapping

1.  **`[MUST]` Announce the Goal:**
    > "Now that the framework is configured, I will perform an initial analysis of your codebase to build a map of its structure and identify the key technologies."
2.  **`[MUST]` Map the Codebase Structure and Identify Key Files:**
    *   **Action 1: Perform Recursive File Listing.** List all files and directories to create a complete `tree` view of the project.
    *   **Action 2: Propose an Analysis Plan.** From the file tree, identify key files that appear to be project pillars (e.g., `package.json`, `pom.xml`, `main.go`, `index.js`, core configuration files). Propose these to the user as a starting point.
    *   **[GUIDELINE]** Keep the plan concise—focus on the smallest file set that gives complete architectural coverage.
    *   **Action 3: Validate Plan with User.** Present the proposed file list for confirmation.
        > "I have mapped your repository. To build an accurate understanding, I propose analyzing these key files: `package.json`, `src/main.tsx`, `vite.config.ts`, `README.md`. Does this list cover the main pillars of your project?"
    *   **Halt and await user confirmation.**
3.  **`[MUST]` Analyze Key Files and Confirm Stack:**
    *   **Action:** Read and analyze the content of the user-approved files to confirm the technology stack, dependencies, and build scripts.
    *   **Action:** Save detected stack information for template discovery.
        ```bash
        mkdir -p .cursor/bootstrap
        echo '{"languages": ["python", "javascript"], "frameworks": ["react", "fastapi"]}' > .cursor/bootstrap/detected-stack.json
        ```

### STEP 3: Thematic Investigation Plan

1.  **`[MUST]` Generate and Announce Thematic Questions:**
    *   **Action:** Based on the confirmed stack, generate a list of key architectural questions, grouped by theme.
    *   **Communication:** Announce the plan to the user.
        > "To understand your project's conventions, I will now investigate the following key areas:
        > - **Security:** How are users authenticated and sessions managed?
        > - **Data Flow:** How do different services communicate?
        > - **Conventions:** What are the standard patterns for error handling, data validation, and logging?
        > I will now perform a deep analysis of the code to answer these questions autonomously."

### STEP 4: Autonomous Deep Dive & Synthesis

1.  **`[MUST]` Perform Deep Semantic Analysis:**
    *   **Action:** For each thematic question, use a **semantic search tool** (in accordance with the **Tool Usage Protocol**) to investigate core architectural processes. The goal is to find concrete implementation patterns in the code.
2.  **`[MUST]` Synthesize Findings into Principles:**
    *   **Action:** For each answer found, synthesize the code snippets into a high-level architectural principle.
    *   **[GUIDELINE] Avoid Over-Engineering:** The synthesized principle should represent the simplest, most direct solution to the problem observed. Do not abstract prematurely or introduce patterns that are not explicitly present and justified in the codebase. Favor pragmatic, clear conventions over complex, theoretical ones.
    *   **Example:**
        *   **Finding:** "The code shows a `validateHmac` middleware on multiple routes."
        *   **Synthesized Principle:** "Endpoint security relies on HMAC signature validation."

### STEP 3.6: Brief Fast-Path Generation (Conditional)

1.  **`[MUST]` Detect `brief.md`:** If a project brief with valid frontmatter exists (e.g., `docs/briefs/{project-name}/brief.md`).
    *   **Action:** Parse and validate frontmatter keys (at minimum: `name`, `project_type`, and stack selectors such as `frontend`/`backend`).
    *   **Action:** If invalid or missing, skip this fast-path and proceed with the standard flow.

2.  **`[GUIDELINE]` Offer Immediate Scaffold Generation:**
    *   **Communication:**
        > "A valid `brief.md` was detected. Would you like me to generate the initial scaffold now using the Project Generator, or continue with the standard documentation → rules flow first?"
    *   **Note:** To preserve this repository as a reusable template, the recommended default is to generate into a sibling output directory (e.g., `../generated-projects/{brief.name}`) rather than in-place.

3.  **`[MUST]` If User Confirms, Execute Generator:**
    *   **Action:** Jump to the automation package in **Step 7.6** to run the appropriate generator command exactly once.

4.  **`[MUST]` Sync Artifacts to Context Kit:**
    *   **Action:** Write a summary of generated outputs (paths, selected templates, CI workflows) to `.cursor/context-kit/README.md`.
    *   **Action:** If rules/READMEs were generated, reference them in the context kit and (optionally) re-run rule audit from STEP 6.5 to capture evidence.

5.  **Flow Control:**
    *   If fast-path was executed, you may continue with STEP 5 for validation and then proceed to STEP 6/7 to align docs and rules with the generated scaffold.
    *   If declined or no valid `brief.md`, continue with the standard flow (STEP 4 onward) and optionally revisit generation at STEP 7.6.

### STEP 5: Collaborative Validation (The "Checkpoint")

1.  **`[MUST]` Present a Consolidated Report for Validation:**
    *   **Action:** Present a clear, consolidated report to the user.
    *   **Communication:**
        > "My analysis is complete. Here is what I've understood. Please validate, correct, or complete this summary.
        >
        > ### ✅ My Understanding (Self-Answered)
        > - **Authentication:** It appears you use HMAC signatures for securing endpoints.
        > - **Error Handling:** Errors are consistently returned in a `{ success: false, error: { ... } }` structure.
        >
        > ### ❓ My Questions (Needs Clarification)
        > - **Inter-service Communication:** I have not found a clear, consistent pattern. How should microservices communicate with each other?
        >
        > I will await your feedback before building the Context Kit."
    *   **Halt and await user validation.**

### STEP 5.5: Context Kit Initialization

1.  **`[MUST]` Create Context Kit Structure:** Prepare directories for context artifacts.
    ```bash
    mkdir -p .cursor/context-kit
    ```

### STEP 6: Iterative Generation Phase 1: Documentation (READMEs)

1.  **`[MUST]` Announce the Goal:**
    > "Thank you for the validation. I will now create or enrich the `README.md` files to serve as a human-readable source of truth for these architectural principles."
2.  **`[MUST]` Generate, Review, and Validate READMEs:**
    *   Propose a plan of `README.md` to create/update.
    *   Generate each file iteratively, based on the **validated principles** from STEP 4, and await user approval for each one.

> Integration Gate: Steps 6.5, 7.5 ensure automation alignment.

### STEP 6.5: Rule Normalization & Audit (Automation)

1.  **`[MUST]` Normalize Rule Metadata:** Ensure all rule files conform to Cursor metadata spec.
    ```bash
    python scripts/normalize_project_rules.py --target .cursor/rules/
    ```
2.  **`[MUST]` Generate Rule Audit Report:** Validate rule metadata and store audit evidence.
    ```bash
    python scripts/rules_audit_quick.py --output .cursor/rules/audit-$(date +%Y-%m-%d).md
    ```
3.  **`[MUST]` Update Context Kit with Governance Status:** Append governance status and audit link to `.cursor/context-kit/README.md`.

### STEP 7: Iterative Generation Phase 2: Project Rules

1.  **`[MUST]` Announce the Goal:**
    > "With the documentation in place as our source of truth, I will now generate the corresponding `project-rules` to enforce these conventions programmatically."
2.  **`[MUST]` Generate, Review, and Validate Rules from READMEs:**
    *   Propose a plan of rules to create, explicitly linking each rule to its source `README.md`.
    *   Generate each rule iteratively, ensuring it follows the rule creation guidelines found in the `master-rules` directory, and await user approval.

### STEP 7.5: Post-Rules Validation & Template Discovery (Automation)

1.  **`[MUST]` Re-run Rule Audit:** Validate newly generated/updated project rules.
    *   **Action:** Invoke the automation from **Step 6.5** with updated timestamps and attach the latest report link.
2.  **`[MUST]` Surface Template Inventory:** Discover available template packs aligned with the detected stack and update the context kit.
    ```bash
    python -c "from project_generator.template_registry import TemplateRegistry; print(TemplateRegistry.list_all())" > .cursor/context-kit/template-inventory.md
    ```
3.  **`[MUST]` Update Context Kit:**
    * Add "Available Template Packs" with high/medium priority recommendations
    * Note Project Generator availability and version

### STEP 7.6: Optional Project Generation (Automation)

1.  **`[GUIDELINE]` Offer Project Generation:** Based on detected stack and template inventory, offer to generate initial project scaffolding.
    *   **Action:** Present template recommendations to user:
        > "Based on your detected stack, I recommend these template packs: [list high-priority templates]. Would you like me to generate initial project scaffolding using the Project Generator?"
    *   **Action:** Await user confirmation before proceeding.

2.  **`[MUST]` Collect Generation Parameters:** If user confirms, gather necessary parameters for project generation.
    *   **Action:** Ask for project name, industry, and any specific requirements.
    *   **Action:** Use detected stack information from STEP 3 for default selections.

3.  **`[MUST]` Execute Project Generator:** Run the appropriate generator script based on user input.
    *   **Option A - Brief-based Generation:**
        ```bash
        python scripts/generate_from_brief.py --brief docs/briefs/{project-name}/brief.md --output-root ../generated-projects --force --yes
        ```
    *   **Option B - Interactive Generation:**
        ```bash
        python scripts/generate_client_project.py --name {project-name} --industry {industry} --project-type {type} --interactive
        ```
    *   **Option C - Bootstrap Generation:**
        ```bash
        python scripts/bootstrap_project.py --name {project-name} --industry {industry} --project-type {type} --update-config
        ```

4.  **`[MUST]` Update Context Kit with Generated Assets:**
    *   **Action:** Reference generated project structure in context kit README
    *   **Action:** Include links to generated documentation and rules
    *   **Action:** Note any compliance artifacts or CI/CD workflows created
    *   **[STRICT]** Ensure every automation outcome is captured inside `.cursor/context-kit/README.md` before closing the protocol.

### FINALIZATION
> "The initial context bootstrapping is complete. We now have a solid 'Version 1.0' of the project's knowledge base, containing both human-readable documentation and machine-actionable rules.
>
> This is a living system. Every future implementation will give us an opportunity to refine this context through the `5-implementation-retrospective.md` protocol, making our collaboration progressively more intelligent and efficient.
>
> You are now ready to use the main development workflow, starting with `1-create-prd.md`." 


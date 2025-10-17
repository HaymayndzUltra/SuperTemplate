# PROTOCOL 4: QUALITY AUDIT ORCHESTRATOR

## ⚡ **ENHANCED STATIC REVIEW ORCHESTRATOR**

**This protocol is the execution engine for the unified `/review` system.** Its sole responsibility is to orchestrate the execution of specialized review protocols based on user input and project context.

**🚫 [CRITICAL] DO NOT SKIP PRE-AUDIT AUTOMATION.** Every downstream review depends on these artifacts.

- **Interactive protocol selection** via the `/review` command
- **Smart context analysis** via git change detection
- **Automatic custom/generic fallback** via the centralized router
- **Unified reporting** with enhanced precision

## AI Persona
I am a **Senior Quality Engineer** acting as an **Audit Orchestrator**. My mission is to execute the correct quality validation protocol based on the provided mode, using the project's specific context to ensure the most relevant and efficient review.

## Mission
To conduct a systematic quality audit by loading and executing the appropriate specialized protocol from the `@review-protocols/` directory based on the user-selected mode.

## EXECUTION FLOW

### Pre-Audit: Automation Enhancement - Workflow Execution

> Pre-Audit Gate: Ensure automation evidence exists before routing to specialized review modes.

1. **`[MUST]` Execute CI Workflow Orchestration:**
   ```bash
   for workflow in ci-test.yml ci-lint.yml; do
     python scripts/run_workflow.py --workflow "$workflow" --wait --output .artifacts/${workflow%.yml}-results.json
   done
   ```
   *   **Action:** Execute CI workflows and wait for completion.
   *   **Action:** Capture workflow results for quality audit integration.

2. **`[MUST]` Announce Workflow Execution:**
   ```
   [AUTOMATION] CI Workflows Executed: ci-test.yml ✅, ci-lint.yml ✅
   ```
   *   **Action:** Display CI workflow status and results.

3. **`[MUST]` Execute Coverage Aggregation:**
   ```bash
   python scripts/aggregate_coverage.py --output .artifacts/coverage-report.json
   ```
   *   **Action:** Aggregate test coverage data from CI workflows.
   *   **Action:** Generate comprehensive coverage report.

4. **`[MUST]` Announce Coverage Results:**
   ```
   [AUTOMATION] Coverage Aggregated: {coverage_percentage}% overall coverage
   ```
   *   **Action:** Display coverage summary for audit integration.
   *   **[STRICT]** Store coverage artifacts inside `.artifacts/` with timestamped filenames.

### 1. Mode Determination
This orchestrator is activated with a specific `--mode` flag (e.g., `quick`, `security`, `comprehensive`).

### 2. Context Analysis & Protocol Routing
Based on the mode, I will use the **Centralized Router** to determine the correct protocol file to apply. The router handles the intelligent fallback from custom to generic protocols.

**[GUIDELINE]** Prefer the narrowest review scope that satisfies the user's intent before escalating to `comprehensive`.

**Router**: `.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md`

### 3. Protocol Execution
I will load the instructions from the determined protocol file (e.g., `@review-protocols/security-check.md`) and execute them precisely. All detailed validation logic, checklists, and report formats are defined within those specialized files.

### 4. Unified Reporting
After the specialized protocol has been executed, I will consolidate the findings into a standardized report format to ensure consistency.

## EXECUTION MODES (Via Unified `/review`)

### Mode: `quick` ("/review" → "Code Review")
```yaml
Focus: Design compliance + Code quality core
Protocol: Loads and executes instructions from `@review-protocols/code-review.md` (or its custom equivalent).
```

### Mode: `security` ("/review" → "Security Check")
```yaml
Focus: Security + Module/Component boundaries
Protocol: Loads and executes instructions from `@review-protocols/security-check.md` (or its custom equivalent).
```

### Mode: `architecture` ("/review" → "Architecture Review")
```yaml
Focus: High-level design + Performance architecture
Protocol: Loads and executes instructions from `@review-protocols/architecture-review.md` (or its custom equivalent).
```

### Mode: `design` ("/review" → "Design System Compliance")
```yaml
Focus: Design system compliance + Component usage
Protocol: Loads and executes instructions from `@review-protocols/design-system.md` (or its custom equivalent).
```

### Mode: `ui` ("/review" → "UI/UX & Accessibility")
```yaml
Focus: Accessibility + User experience validation
Protocol: Loads and executes instructions from `@review-protocols/ui-accessibility.md` (or its custom equivalent).
```

### Mode: `deep-security` ("/review" → "Pre-Production Security")
```yaml
Focus: Complete security validation with testing
Protocol: Loads and executes instructions from `@review-protocols/pre-production.md` (or its custom equivalent).
```

### Mode: `comprehensive` ("/review" → "🚀 Run All")
```yaml
Focus: Complete quality validation across all layers.
Protocol: This mode is special. It sequentially executes ALL the above protocols (quick, security, architecture, etc.) to produce a complete, multi-faceted audit report.
```

## TOOL INTEGRATION
This orchestrator leverages the tool integrations defined within each specialized protocol it calls.



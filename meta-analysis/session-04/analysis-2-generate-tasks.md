# Meta-Instruction Analysis: .cursor/ai-driven-workflow/2-generate-tasks.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Fix the agent as a Tech Lead delivering action lists only.
- Reasoning: The protocol assigns the Tech Lead role and bans prose outputs to enforce implementation-focused sequencing.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L3-L8】
- Meta-heuristic: Role specialization to constrain deliverable format.

**Step 2:** Mandate comprehensive rule indexing before interpreting the PRD.
- Reasoning: Phase 1 orders discovery of rule directories, metadata parsing, and in-memory indexing as a `[CRITICAL]` prerequisite before any other action.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L18-L24】
- Meta-heuristic: Compliance-first bootstrapping to anchor downstream logic in governance constraints.

**Step 3:** Require external calibration of LLM personas for current-year capability alignment.
- Reasoning: Step 3 forces a current-year web search for top LLMs and persona synthesis to update execution strategy before planning.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L27-L28】
- Meta-heuristic: Dynamic capability refresh to avoid stale automation assumptions.

### Layer 2: Behavioral Control
**Step 4:** Delimit affected implementation layers and enforce reuse detection.
- Reasoning: Steps 4-5 direct the agent to map primary/secondary layers and, when UI is primary, search for reusable components before continuing.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L29-L32】
- Meta-heuristic: Scope triangulation combined with anti-duplication checks to minimize redundant build paths.

**Step 5:** Create high-level MVP tasks with WHY context, dependencies, and complexity.
- Reasoning: Phase 2 dictates creating a tasks file, constraining to MVP path, adding WHY statements, dependency tags, and complexity ratings.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L36-L50】
- Meta-heuristic: Value-aligned scaffolding ensuring each behavior is justified and sequenced for parallelism.

**Step 6:** Gate progression on user confirmation after presenting the annotated task list.
- Reasoning: The protocol requires announcing readiness and halting until an explicit "Go" is received before deeper breakdown.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L51-L54】
- Meta-heuristic: Human-in-the-loop checkpoint to validate behavioral alignment before expansion.

### Layer 3: Procedural Logic
**Step 7:** Decompose each task using rule-index-driven templates with persona alignment.
- Reasoning: Phase 3 compels per-task decomposition, rule referencing from the index, persona assignments, template selection by layer, and placeholder resolution before assembly.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L57-L68】
- Meta-heuristic: Template-governed proceduralization linking compliance metadata to actionable sub-tasks.

**Step 8:** Annotate automation hooks and validate their existence for every high-level task.
- Reasoning: Phase 4 mandates identifying automation opportunities, annotating metadata with executable references, and verifying their presence and parameterization.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L71-L87】
- Meta-heuristic: Automation-first orchestration to guarantee future execution leverage.

**Step 9:** Run validation and enrichment scripts to certify automation readiness.
- Reasoning: Phase 4.5 enforces running validation/enrichment Python scripts, announcing results, gating on success, and archiving artifacts before completion.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L94-L127】
- Meta-heuristic: Evidence-backed closure ensuring the procedural loop ends with auditable artifacts.

### Layer 4: Communication Grammar
**Step 10:** Render deliverables via a canonical Markdown plan with persona, rule, and automation annotations.
- Reasoning: The final template prescribes structured Markdown with WHY notes, recommended models, rule lists, automation tags, and dependency markers to standardize communication.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L198-L241】
- Meta-heuristic: Grammar standardization for interoperable downstream consumption.

## META-ARCHITECTURE DIAGRAM
```
System: Protocol 2 - Technical Task Generation (L1-L241)
├── Subsystem A: Mission & Compliance Primers (L3-L33)
│   ├── Rule A1: Assign Tech Lead role and action-list output (L3-L8)
│   └── Rule A2: Perform rule indexing before PRD reading (L18-L24)
├── Subsystem B: Capability & Scope Alignment (L27-L33)
│   ├── Rule B1: Refresh LLM personas via current-year search (L27-L28)
│   └── Rule B2: Map implementation layers and duplicate checks (L29-L32)
├── Subsystem C: High-Level Task Framing (L36-L54)
│   ├── Rule C1: Generate MVP-oriented tasks with WHY and dependencies (L36-L50)
│   └── Rule C2: Halt for user confirmation before decomposition (L51-L54)
├── Subsystem D: Layered Decomposition Engine (L57-L68)
│   └── Rule D1: Apply templates with rule index references and personas (L57-L68)
├── Subsystem E: Automation Hook Integration (L71-L87)
│   └── Rule E1: Annotate and verify automation metadata per task (L71-L87)
├── Subsystem F: Validation & Enrichment Pipeline (L94-L127)
│   ├── Rule F1: Execute validation and enrichment scripts (L96-L119)
│   └── Rule F2: Gate completion on successful automation outputs (L120-L127)
└── Subsystem G: Standardized Output Template (L198-L241)
    └── Rule G1: Provide canonical Markdown execution plan (L198-L241)
```

## COMMENTARY
**Architectural Dependencies:**
- Subsystem A’s rule index feeds Subsystem D’s decomposition, as every sub-task must cite indexed rules, ensuring compliance continuity.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L18-L24】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L57-L68】
- Persona calibration in Subsystem B informs Subsystem G’s Recommended Model annotations, aligning execution grammar with capability mapping.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L27-L32】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L221-L238】
- Subsystem C’s dependency graph enables automation layering in Subsystem E by clarifying parallelization candidates for hook assignment.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L36-L50】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L71-L83】
- Validation scripts in Subsystem F rely on the automation metadata set in Subsystem E to assess coverage and produce artifacts.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L71-L87】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L94-L127】
- The final template (Subsystem G) aggregates outputs from prior subsystems, embedding rules, personas, automation, and dependencies into a coherent deliverable.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L198-L241】

**Meta-Engineering Heuristics:**
- Compliance-first indexing ensures governance knowledge precedes task synthesis.
- Continuous capability refresh via persona identification enforces adaptive tooling.
- MVP-focused task framing curbs scope inflation by tethering steps to WHY value statements.
- Automation-first metadata ensures Protocol 3 inherits executable hooks without rework.
- Evidence capture requirements embed telemetry as a closing condition rather than a post-hoc step.

**Cognitive Role Modularity:**
- Planner: Phases 1-2 orchestrate planning and sequencing of tasks.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L18-L54】
- Executor: Phase 3 templates dictate actionable breakdown per implementation layer.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L57-L68】
- Validator: Phase 4.5 scripts and gating perform validation duties.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L94-L127】
- Auditor: Final template’s structured annotations enable human/AI auditability.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L198-L241】

## INFERENCE SUMMARY
This protocol represents a compliance-driven orchestration framework with dynamic capability calibration. Key characteristics include:
1. Governance bootstrapping before contextual analysis ensures all subsequent reasoning is rule-aware.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L18-L24】
2. Planning steps are value-justified and dependency-aware to enable parallel execution without sacrificing MVP focus.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L36-L50】
3. Automation and validation are embedded as mandatory closure activities, converting plans into execution-ready assets.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L71-L127】

Design philosophy: deterministic orchestration that fuses compliance indexing, capability calibration, and automation-readiness into a single planning pipeline.

## OUTPUT INSTRUCTIONS
- Format: Markdown with all sections present.
- Preserve ASCII diagram indentation exactly as defined.
- Include explicit line references for traceability of each deduction.
- Do not omit any section or compress content; render PHASE MAP through OUTPUT INSTRUCTIONS in full detail.

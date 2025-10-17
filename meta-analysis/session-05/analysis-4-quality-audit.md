# Meta-Instruction Analysis: .cursor/ai-driven-workflow/4-quality-audit.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Fix the persona as a Senior Quality Engineer orchestrating unified reviews.
- Reasoning: The protocol frames the agent as an Audit Orchestrator whose mission is to route to the correct specialized protocol for each `/review` mode.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L14-L19】
- Meta-heuristic: Role-anchored orchestration to keep governance centralized.

**Step 2:** Gate all reviews behind mandatory pre-audit automation evidence.
- Reasoning: The `[CRITICAL]` pre-audit section requires running CI workflows, aggregating coverage, and storing artifacts before any routing occurs.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L54】
- Meta-heuristic: Evidence-first validation to guarantee telemetry continuity from earlier automation hooks.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L71-L127】

**Step 3:** Bind the orchestrator to the centralized router for deterministic protocol selection.
- Reasoning: Execution flow explicitly defers to the router utility to resolve the narrowest matching protocol per mode.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L58-L64】
- Meta-heuristic: Deterministic dispatch to maintain review coverage discipline across modes.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L154-L183】

### Layer 2: Behavioral Control
**Step 4:** Require explicit mode flags to scope the audit horizon.
- Reasoning: Mode determination insists on a declared `--mode` flag, enumerating options from `quick` to `comprehensive` with scoped intents.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L55-L113】
- Meta-heuristic: Intent-scoped branching to prevent unnecessary review load.

**Step 5:** Prefer specialized protocols before escalating to multi-pass audits.
- Reasoning: The guideline mandates using the narrowest protocol satisfying the request prior to invoking comprehensive sweeps.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L61-L113】
- Meta-heuristic: Minimal sufficient governance to balance rigor with efficiency.

**Step 6:** Constrain behavior to router-led fallbacks when custom protocols are absent.
- Reasoning: Router description highlights automatic fallback from project-specific rules to generic templates when needed.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L58-L64】
- Meta-heuristic: Resilient routing ensures audits never stall on missing bespoke assets.

### Layer 3: Procedural Logic
**Step 7:** Execute CI and coverage scripts sequentially and persist results.
- Reasoning: Commands for `run_workflow.py` and `aggregate_coverage.py` specify waiting for completion and saving JSON outputs inside `.artifacts/`.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L26-L54】
- Meta-heuristic: Scripted automation pipelines to standardize audit prerequisites.

**Step 8:** Load chosen protocol instructions verbatim and execute them end-to-end.
- Reasoning: Protocol execution stage insists on executing instructions defined within the routed specialized file without deviation.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L65-L67】
- Meta-heuristic: Delegated procedure execution to preserve domain-specific rigor.

**Step 9:** Consolidate outputs into unified audit reports after protocol completion.
- Reasoning: Unified reporting stage mandates aggregating specialized findings into a standardized output channel.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L68-L70】
- Meta-heuristic: Post-processing normalization for comparable audit telemetry.

### Layer 4: Communication Grammar
**Step 10:** Broadcast automation completions using fixed `[AUTOMATION]` announcements.
- Reasoning: Steps 2 and 4 of pre-audit require explicit status messages with structured placeholders (coverage, workflow status).【F:.cursor/ai-driven-workflow/4-quality-audit.md†L35-L52】
- Meta-heuristic: Structured signaling to synchronize humans with machine-run checks.

**Step 11:** Communicate review routing and reporting through `/review` taxonomy.
- Reasoning: Mode listings map `/review` intents to protocol names, reinforcing consistent messaging for stakeholders.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L71-L113】
- Meta-heuristic: Controlled vocabulary to avoid audit ambiguity.

**Step 12:** Surface router dependencies when explaining execution context.
- Reasoning: Router reference explicitly calls out `.cursor/.../_review-router.md`, clarifying provenance when the agent describes routing decisions.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L58-L64】
- Meta-heuristic: Transparency grammar to maintain trust in automated selection.

## META-ARCHITECTURE DIAGRAM
```
System: Protocol 4 - Quality Audit Orchestrator
├── Subsystem: Pre-Audit Automation Gate
│   ├── CI Workflow Runner [Lines 26-38]
│   └── Coverage Aggregator & Artifact Vault [Lines 41-54]
├── Subsystem: Mode & Router Control
│   ├── Mode Flag Intake [Lines 55-61]
│   └── Centralized Router Fallback [Lines 58-64]
├── Subsystem: Specialized Protocol Execution
│   └── Delegated Review Runner [Lines 65-67]
└── Subsystem: Unified Reporting Channel
    └── Standardized Audit Consolidation [Lines 68-113]
```

## COMMENTARY
**Architectural Dependencies:**
- Pre-audit automation artifacts provide the telemetry foundation consumed by downstream review protocols, mirroring the automation hooks annotated during task generation.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L54】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L71-L127】
- Mode routing depends on the router utility to resolve context-aware protocol selection, enabling reuse of the session capsules constructed in task execution workflows.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L58-L67】【F:.cursor/ai-driven-workflow/3-process-tasks.md†L16-L145】
- Unified reporting consolidates specialized outputs so retrospectives inherit normalized evidence, feeding the continuous improvement loop of Protocol 5.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L68-L113】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L49-L62】

**Meta-Engineering Heuristics:**
- Evidence-first orchestration mandates verifiable CI and coverage before subjective review, extending the compliance-first planning ethos.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L54】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L18-L33】
- Deterministic routing avoids ad-hoc reviewer selection, reinforcing reproducible governance across review types.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L58-L113】
- Telemetry normalization ensures every audit yields comparable metrics, supporting retrospective analytics and rule tuning.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L68-L113】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L49-L99】

**Cognitive Role Modularity:**
- Planner: Router utility coordinates which specialized auditor to activate.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L58-L64】
- Executor: Specialized protocol instructions perform domain-specific validations.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L65-L113】
- Validator: Pre-audit automation scripts confirm readiness via CI telemetry.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L54】
- Auditor: Unified reporting synthesizes findings into stakeholder-facing outputs.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L68-L113】

## INFERENCE SUMMARY
This protocol implements a deterministic audit orchestration framework characterized by:
1. Mandatory automation evidence gating prior to any human-readable review stages.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L54】
2. Router-driven specialization that matches review depth to declared intent while preserving fallbacks.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L58-L113】
3. Standardized reporting pipelines that prepare artifacts for continuous improvement loops.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L68-L113】

Design philosophy: Compliance-first quality assurance with telemetry-backed routing that keeps audits reproducible and ready for retrospective analysis.

## OUTPUT INSTRUCTIONS
- Format: Markdown with all five sections present.
- Preserve ASCII diagram indentation exactly as shown.
- Include explicit citations for every inference tied to source protocol lines.
- Maintain cross-protocol references to uphold the automation telemetry chain.

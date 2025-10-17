# Meta-Instruction Analysis: .cursor/ai-driven-workflow/3-process-tasks.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Define the agent as an AI Paired Developer executing tasks sequentially.
- Reasoning: The mission statement restricts autonomy and enforces looped execution until tasks finish or commands change.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L3-L6】
- Meta-heuristic: Role constrainment for deterministic execution discipline.

**Step 2:** Lock execution into Focus Mode with optional continuous mode escalation.
- Reasoning: Section 2 mandates Focus Mode and describes continuous mode only upon explicit user directive, shaping top-level operating parameters.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L7-L13】
- Meta-heuristic: Controlled context windows to manage cognitive load.

**Step 3:** Enforce the “one parent task, one chat” structure integrated with downstream protocols.
- Reasoning: Section 3 requires each parent task to run in its own session with automatic Protocol 4 and 5 handoffs before restarting, structuring the macro workflow.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L16-L26】
- Meta-heuristic: Session partitioning to preserve context integrity across lifecycle stages.

### Layer 2: Behavioral Control
**Step 4:** Execute pre-flight model confirmation before any work begins.
- Reasoning: Section 3.5 compels identifying the target task, announcing the recommended model, and halting until user replies “Go.”【F:.cursor/ai-driven-workflow/3-process-tasks.md†L31-L43】
- Meta-heuristic: Human-verified model alignment as a safety checkpoint.

**Step 5:** Perform environmental and production-readiness validations prior to execution.
- Reasoning: Section 4 mandates environment checks and production-readiness commitments as `[CRITICAL]` steps before entering the loop.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L46-L55】
- Meta-heuristic: Baseline assurance ensuring infrastructure and standards readiness.

**Step 6:** Govern each iteration with rule loading, documentation consultation, and strict communication prefixes.
- Reasoning: Step 1 of the execution loop requires rule retrieval per sub-task, documentation research, and standardized announcements, constraining behavior within each cycle.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L58-L75】【F:.cursor/ai-driven-workflow/3-process-tasks.md†L222-L226】
- Meta-heuristic: Just-in-time compliance injection with rigid communication grammar.

### Layer 3: Procedural Logic
**Step 7:** Update task files and follow the hybrid commit strategy after each actionable unit.
- Reasoning: Step 3 outlines mandatory status updates in the task file, granular commit proposals, and parent task checkpoints with quality audits and CI checks.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L99-L145】
- Meta-heuristic: State synchronization coupled with version control rigor to support traceable progress.

**Step 8:** Synchronize automation state and capture evidence artifacts post-sub-task.
- Reasoning: Steps 3.5 and 3.6 require running automation scripts for task state sync and evidence capture, including announcements and artifact attachment.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L154-L183】
- Meta-heuristic: Automated telemetry harvesting for downstream audits.

**Step 9:** Apply domain-specific commit heuristics for MicroSaaS architectures.
- Reasoning: Section 3.6’s MicroSaaS considerations dictate commit grouping patterns for gateways, migrations, services, and infrastructure to maintain rollback precision.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L185-L199】
- Meta-heuristic: Architecture-aware change management to preserve isolation boundaries.

### Layer 4: Communication Grammar
**Step 10:** Conduct enhanced quality gate communications with explicit status syntax.
- Reasoning: Step 4 prescribes phrasing for focus vs continuous mode updates, mandatory quality gate announcements, and readiness reports before continuation.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L202-L216】
- Meta-heuristic: Telemetry-standardized messaging for consistent human oversight.

## META-ARCHITECTURE DIAGRAM
```
System: Protocol 3 - Controlled Task Execution (L1-L226)
├── Subsystem A: Mission & Mode Governance (L3-L26)
│   ├── Rule A1: Define Paired Developer role and sequential mission (L3-L6)
│   ├── Rule A2: Enforce Focus/Continuous mode parameters (L7-L13)
│   └── Rule A3: Partition sessions per parent task with Protocol 4/5 chaining (L16-L26)
├── Subsystem B: Pre-Execution Safeguards (L31-L55)
│   ├── Rule B1: Confirm recommended model before starting (L31-L43)
│   └── Rule B2: Validate environment and production readiness (L46-L55)
├── Subsystem C: Execution Loop Controls (L58-L145)
│   ├── Rule C1: Load rules and documentation per sub-task with standardized communication (L58-L76, L222-L226)
│   ├── Rule C2: Maintain task file status and granular commits (L99-L115)
│   └── Rule C3: Run parent task quality audits and CI checks (L116-L145)
├── Subsystem D: Automation Synchronization (L154-L199)
│   ├── Rule D1: Sync task state via automation scripts (L154-L166)
│   ├── Rule D2: Capture evidence artifacts and attach logs (L169-L183)
│   └── Rule D3: Apply MicroSaaS-specific commit heuristics (L185-L199)
└── Subsystem E: Quality Gate Communications (L202-L226)
    └── Rule E1: Use standardized checkpoint messaging per execution mode (L202-L216, L222-L226)
```

## COMMENTARY
**Architectural Dependencies:**
- Subsystem A’s session partitioning drives Subsystem C’s loop boundaries, ensuring each execution cycle maps to a single parent task with enforced quality gates.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L16-L26】【F:.cursor/ai-driven-workflow/3-process-tasks.md†L99-L145】
- Pre-execution safeguards in Subsystem B must complete before the loop logic of Subsystem C activates, guaranteeing the chosen model and environment are validated.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L31-L55】【F:.cursor/ai-driven-workflow/3-process-tasks.md†L58-L76】
- Subsystem C’s quality audit triggers feed directly into Subsystem D’s automation scripts, which archive artifacts required for Protocol 5 retrospectives.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L116-L145】【F:.cursor/ai-driven-workflow/3-process-tasks.md†L154-L183】
- MicroSaaS heuristics in Subsystem D inform how Subsystem E’s communication of completion status references commit structure, ensuring stakeholders understand rollback posture.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L185-L199】【F:.cursor/ai-driven-workflow/3-process-tasks.md†L202-L216】

**Meta-Engineering Heuristics:**
- Session isolation reduces cognitive interference and enforces deterministic context resets.
- Human-confirmed model selection operates as a security gate against unintended capability drift.
- Hybrid commit strategy emphasizes traceability and audit-ready change segmentation.
- Automation-first evidence capture ensures retrospectives and audits rely on pre-generated artifacts rather than recollection.
- Domain-specific commit heuristics embed architectural awareness into change management.

**Cognitive Role Modularity:**
- Planner: Pre-flight checks orchestrate readiness validation before execution.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L31-L55】
- Executor: The core loop handles rule-driven task completion.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L58-L115】
- Validator: Quality audits and CI verification enforce correctness per parent task.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L116-L145】
- Auditor: Automation synchronization and evidence capture provide audit trails for retrospectives.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L154-L183】

## INFERENCE SUMMARY
This protocol implements a deterministic execution framework centered on session isolation and evidence-driven validation. Distinguishing characteristics include:
1. Mandatory pre-flight gating aligns resources, models, and environments before any code changes occur.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L31-L55】
2. Execution loops are tightly bound to rule reloading and state synchronization, preventing drift from the authoritative plan.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L58-L115】
3. Quality audits, automation sync, and evidence capture convert each parent task into a fully validated, auditable deliverable.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L116-L199】

Design philosophy: deterministic, audit-centric execution where each parent task becomes a sealed unit of validated work supported by synchronized automation artifacts.

## OUTPUT INSTRUCTIONS
- Produce responses in Markdown, preserving section order and headings.
- Keep ASCII diagrams indented exactly to maintain structural clarity.
- Reference relevant line ranges for every architectural claim.
- Ensure all five sections are present without omission or compression.

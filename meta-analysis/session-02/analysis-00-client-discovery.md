# Meta-Instruction Analysis: 00-client-discovery.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1: Declare mission boundaries before action** (ref. L5-L12)
- Reasoning: The author anchors the agent as a Client Discovery Specialist with an explicit prohibition against implementation, forcing all downstream behavior to remain in exploratory briefing scope.
- Meta-heuristic: Mission primacy—define role and guardrails first to prevent scope drift.

**Step 2: Decompose discovery into gated phases** (ref. L17-L297)
- Reasoning: The protocol structures seven phases with hard validation gates, ensuring sequential completion that mirrors consulting engagements from intake through client validation.
- Meta-heuristic: Deterministic pipeline orchestration with mandatory exit criteria.

### Layer 2: Behavioral Control
**Step 3: Normalize input evidence before reasoning** (ref. L19-L53)
- Reasoning: Intake commands require capturing raw data, domain hints, and creating a normalized artifact before analysis can proceed, establishing traceability.
- Meta-heuristic: Evidence-first governance—no reasoning without canonicalized inputs.

**Step 4: Couple signal extraction with domain adaptation** (ref. L56-L99, L342-L401)
- Reasoning: The protocol mandates structured extraction of objectives, users, deliverables, and then adapts questioning via domain adapters, ensuring contextual nuance.
- Meta-heuristic: Contextual heuristics—augment generic analysis with domain-specific overlays.

**Step 5: Institutionalize risk and automation checks before handoff** (ref. L129-L295)
- Reasoning: Risks, dependencies, and automated validations must be completed and announced prior to client review, preventing premature handoffs.
- Meta-heuristic: Pre-handoff validation stack—risk mitigation and automation enforced as governance layers.

### Layer 3: Procedural Logic
**Step 6: Generate multi-artifact documentation set** (ref. L171-L227, L403-L624)
- Reasoning: The author prescribes creation of multiple Markdown artifacts plus templates, ensuring every analytical output is codified and reusable.
- Meta-heuristic: Knowledge crystallization—convert reasoning into structured artifacts for downstream protocols.

**Step 7: Enforce communication protocols for every phase** (ref. L217-L241, L627-L740)
- Reasoning: Standard prefixes and reporting formats are mandated, providing consistent signaling to humans and systems about progress and gate status.
- Meta-heuristic: Controlled messaging grammar—communication is standardized to maintain auditability.

**Step 8: Align deliverables with follow-on protocol prerequisites** (ref. L767-L799)
- Reasoning: A pre-handoff checklist confirms readiness for PRD creation by verifying artifacts, approvals, and traceability.
- Meta-heuristic: Dependency-aware readiness—validate upstream outputs against downstream needs.

### Layer 4: Communication Grammar
**Step 9: Script status annunciations with templates** (ref. L234-L241, L637-L659)
- Reasoning: The text supplies explicit message templates for gate announcements and progress reports, ensuring consistent language when interacting with clients or orchestrators.
- Meta-heuristic: Linguistic determinism—predefine utterances to minimize ambiguity.

**Step 10: Provide exemplar transcripts illustrating compliance** (ref. L665-L740)
- Reasoning: The correct-execution example demonstrates how communications should look end-to-end, reinforcing desired conversational tone and content.
- Meta-heuristic: Behavioral mirroring—use exemplars to shape agent dialog patterns.

## META-ARCHITECTURE DIAGRAM
```
System: Protocol 00 - Client Discovery & Project Briefing
├── Mission Layer (L5-L12)
│   └── Role Definition & Guardrails
├── Phased Workflow (L17-L297)
│   ├── Phase 0 Intake & Gate (L19-L53)
│   ├── Phase 1 Signal Extraction & Gate (L56-L87)
│   ├── Phase 2 Clarification & Gate (L90-L126)
│   ├── Phase 3 Risks & Gate (L129-L166)
│   ├── Phase 4 Draft Assembly & Gate (L169-L203)
│   ├── Phase 5 Review & Automation Gate (L206-L295)
│   └── Phase 6 Client Validation & Gate (L297-L339)
├── Domain Adapters (L342-L401)
│   └── Domain-specific signal/question overlays
├── Artifact Templates (L403-L624)
│   ├── brief.md (L405-L457)
│   ├── acceptance-criteria.md (L459-L480)
│   ├── open-questions.md (L483-L503)
│   ├── stakeholders.md (L505-L528)
│   ├── constraints.md (L530-L559)
│   ├── risk-register.md (L561-L585)
│   └── one-pager.md (L587-L623)
└── Communication & Handoff Controls (L627-L799)
    ├── Messaging Prefixes & Formats (L627-L659)
    ├── Execution Examples (L665-L740)
    └── Handoff Checklist & Command (L767-L786)
```

## COMMENTARY
**Architectural Dependencies:**
- Mission Layer governs Phased Workflow by constraining actions to discovery tasks, preventing implementation leakage.
- Phased Workflow outputs feed Artifact Templates, as each gate requires populated documents to satisfy validation.
- Domain Adapters augment Phase 1 and Phase 2, ensuring extracted signals and questions reflect domain-specific heuristics before artifacts are finalized.
- Communication & Handoff Controls depend on preceding phases to report accurate status, and in turn enable transition to Protocol 1 by verifying readiness.

**Meta-Engineering Heuristics:**
- Evidence-first intake ensures no analysis occurs without captured source context.
- Gate-driven sequencing enforces deterministic progress with measurable pass/fail states.
- Automation reinforcement (validation scripts) embeds quality checks prior to human review, aligning with evidence-based governance.
- Template proliferation standardizes deliverables, reinforcing reproducibility across engagements.

**Cognitive Role Modularity:**
- Planner: Phases 0-2 craft the discovery plan and information model.
- Executor: Phases 3-5 assemble artifacts, run automations, and consolidate evidence.
- Validator: Gates and automation scripts verify completeness and quality.
- Auditor: Communication directives and templates capture traceable records for external review.

## INFERENCE SUMMARY
This protocol embodies a contract-driven discovery framework emphasizing deterministic orchestration and traceable evidence:
1. Sequential gates ensure no phase advances without validated artifacts.
2. Domain adapters tailor analysis while preserving standard process control.
3. Communication templates institutionalize audit-ready reporting and client alignment.

Design philosophy: Governance-centric discovery that prioritizes evidence capture, risk mitigation, and readiness certification before product requirements development.

## OUTPUT INSTRUCTIONS
- Format: Markdown with preserved headings and bullet indentation.
- Include line references for traceability in each analytical claim.
- Maintain ASCII diagram indentation exactly as shown.
- Ensure all five sections remain fully expanded—no abbreviated summaries.

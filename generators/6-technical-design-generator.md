# Protocol 6 Generator Instructions — Technical Design & Architecture Specification

## 1. Purpose & Context
- **Goal:** Transform the filled requirements form (`protocol-input-form-6-technical-design.yaml`) into `6-technical-design-architecture.md`.
- **Scope:** Bridge PRD outputs from Protocol 01 into architecture artifacts for Protocol 2. Maintain strict alignment with governor workflow style.
- **Guardrails:** Preserve `[MUST]`/`[GUIDELINE]` markers, evidence pathways, and communication grammar from canonical protocols.

## 2. Required Inputs
1. `protocol-input-form-6-technical-design.yaml`
2. `PROJECT-BRIEF.md`, `project-brief-validation-report.json`, `BRIEF-APPROVAL-RECORD.json`
3. Discovery artifacts referenced in the form (for cross-checking integration points)

## 3. Output Targets
Generate **one** markdown file:
- `.cursor/ai-driven-workflow/6-technical-design-architecture.md`

Ensure sections appear in this order:
1. `# PROTOCOL 6: ...`
2. `## 1. AI ROLE AND MISSION`
3. `## 2. TECHNICAL DESIGN WORKFLOW`
4. `## 3. INTEGRATION POINTS`
5. `## 4. QUALITY GATES`
6. `## 5. COMMUNICATION PROTOCOLS`
7. `## 6. HANDOFF CHECKLIST`

## 4. 4-Layer Architecture Mapping
| Layer | Content Source | Generator Expectations |
|-------|----------------|------------------------|
| **L1 – System Decisions** | `ai_role`, `primary_guardrail`, `purpose` | Craft mission paragraph plus `[CRITICAL]` guardrail. |
| **L2 – Behavioral Control** | `quality_gate`, `prerequisites`, `halt_condition` | Ensure gates reference evidence artifacts and recovery handling. |
| **L3 – Procedural Logic** | `phases.steps`, `automation_hooks`, `evidence_collection` | Render steps with `[MUST]/[GUIDELINE]`, actions, communication, evidence, automation. |
| **L4 – Communication Grammar** | `communication_template`, `outputs_to`, `inputs_from` | Produce status announcements, validation prompts, and error handling narratives. |

## 5. Template Assembly Algorithm
1. **Header Block:** Compose protocol title with domain tag `(Design Governance Compliant)`.
2. **Role & Mission:** Two sentences max. Include mission, context, and guardrail as separate paragraph.
3. **Workflow Construction:**
   - Loop over phases sequentially.
   - For each step, render ordered list item with emphasis exactly as: `1. **`[MUST]``. Preserve numbering.
   - Append automation command as inline code bullet where provided.
   - Evidence bullet line should start with `* **Evidence:**` when present.
4. **Integration Points:** Split into `Inputs From` and `Outputs To` subsections. Mirror artifact names from the form.
5. **Quality Gates:** Use heading `**Gate N: Name**` plus criteria/evidence/failure-handling bullets.
6. **Communication Protocols:**
   - Produce code block for Status Announcements containing one line per phase start/complete from the form or derived text.
   - Provide Validation Prompts and Error Handling bullets.
7. **Handoff Checklist:** Render checkbox list, then closing code block announcing readiness.

## 6. Quality Validation Checklist
- [ ] All headings and numbering match canonical protocols (H1 → H2 → H3).
- [ ] Every phase step contains Action + Communication + (Halt condition or evidence) as required.
- [ ] Evidence files live under `.artifacts/design/` or `.cursor/context-kit/` as declared.
- [ ] Integration references Protocol 01 upstream and Protocol 2 downstream.
- [ ] Quality gates named Intake, Design Integrity, Sign-Off.
- [ ] Communication templates include `[PHASE X START]` messages.
- [ ] Final checklist contains five items plus completion code block.

## 7. Circular Validation Prep
Before marking generator output complete:
1. Run Meta-Analysis generator to confirm 4-layer extraction recognizes mission, gates, steps, and communication.
2. Verify subsystem mapping highlights Intake → Drafting → Review.
3. Ensure cognitive roles (Architect, Reviewer) are evident in wording.

## 8. Automation Hook Notes
- Commands referenced must stay verbatim to align with scripts directory.
- Do **not** invent additional tooling beyond what form specifies.
- If a hook is optional, annotate as `[GUIDELINE]` step rather than `[MUST]`.

Following this playbook guarantees consistent architecture protocols for Batch 1.

# Generator Playbook: Protocol 6 – Technical Design & Architecture Specification

## 1. Mission Alignment
- **Goal:** Produce `6-technical-design-architecture.md` that matches protocol structure in `.cursor/ai-driven-workflow/`.
- **Source Inputs:** `generators/protocol-input-form-6-technical-design.yaml`, upstream artifacts from Protocols 01 and 02.
- **Guardrails:** Enforce stakeholder approval requirement, evidence capture paths, and integration with Protocols 02 & 07.

## 2. 4-Layer Architecture Mapping
| Layer | Content to Extract | Output Expectation |
|-------|-------------------|--------------------|
| **L1 – System Decisions** | Mission, AI role, guardrails, workflow sequencing | Intro section with role, mission, and CRITICAL guardrail |
| **L2 – Behavioral Control** | Prerequisites, quality gates, halt conditions, approvals | Quality gate section with criteria/evidence/failure handling |
| **L3 – Procedural Logic** | Phase objectives, MUST/GUIDELINE steps, automation hooks | Three step groups with detailed actions and evidence collection |
| **L4 – Communication Grammar** | Status announcements, validation prompts, error messages | Communication section with code blocks and error list |

## 3. Template Blueprint
Follow this outline exactly:
1. `# PROTOCOL 6: ...`
2. `## 1. AI ROLE AND MISSION`
3. `## 2. ARCHITECTURE AUTHORING WORKFLOW`
   - `### STEP 1`, `STEP 2`, `STEP 3`
   - Each step contains ordered actions with `[MUST]`/`[GUIDELINE]` markers, Action/Communication/Halt triples.
   - Include **Evidence Collection** sublist and **Quality Gate** paragraph after each phase.
4. `## 3. INTEGRATION POINTS`
5. `## 4. QUALITY GATES`
6. `## 5. COMMUNICATION PROTOCOLS`
   - Status announcements, validation prompts, error handling.
7. `## 6. HANDOFF CHECKLIST`

## 4. Automation & Evidence Hooks
- Reference `design_artifact_audit.py` in automation messaging.
- Ensure evidence paths use `.artifacts/design/`.
- Maintain alignment with integration targets: Protocol 02 and Protocol 07.

## 5. Quality Acceptance Criteria
- Section headings exactly match numbering (1–6).
- Every action includes both **Action** and **Communication** bullet items.
- Evidence collection lists at least two artifacts per phase.
- Quality gates mirrored in both phase detail and Section 4 summary.
- Error codes match those defined in the input form.

## 6. Validation Checklist for Generator
- [ ] All four layers represented and traceable.
- [ ] No missing MUST actions from form.
- [ ] All evidence paths point to `.artifacts/design/` (or documentation for handbook output).
- [ ] Integration points include both inputs and outputs with protocol numbers.
- [ ] Communication templates wrapped in fenced code blocks where required.
- [ ] Closing checklist references downstream protocols (02 & 07).

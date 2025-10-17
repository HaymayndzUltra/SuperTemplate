# Protocol 6 Generator - Technical Design & Architecture Specification

## 🎯 Purpose
Guide the AI generator in transforming the filled requirements form (`protocol-input-form-6-technical-design.yaml`) into a fully compliant architecture protocol that bridges the PRD and downstream task planning. The resulting file must live at `.cursor/ai-driven-workflow/6-technical-design-architecture.md` and pass circular validation.

## 📥 Required Inputs
- Completed `protocol-input-form-6-technical-design.yaml`
- `PROJECT-BRIEF.md` and validation artifacts from Protocol 01
- `PRD.md`, acceptance criteria, and non-functional requirement inventory from Protocol 1
- Any existing architecture reference material (optional for examples)

## 🧠 4-Layer Mapping Blueprint
1. **Layer 1 – System-Level Decisions**
   - Mission: Solutions Architect persona converting requirements to architecture
   - Guardrails: No implementation before approval, traceability enforcement
   - Dependencies: Protocol 01 + Protocol 1 inputs
2. **Layer 2 – Behavioral Control**
   - Gates: Input Integrity, Architecture Integrity, Approval & Risk
   - Halt conditions: Missing artifacts, conflicting requirements, validation failures
   - Approval workflow and risk ownership capture
3. **Layer 3 – Procedural Logic**
   - Phases: Requirements Alignment → Architecture Modeling → Validation & Sign-off
   - Evidence capture (traceability matrix, diagrams, decision records)
   - Automation hooks (plan_from_brief, generate_consistency_report, validate_workflow_integration)
4. **Layer 4 – Communication Grammar**
   - Status templates for each phase
   - Approval and conflict resolution prompts
   - Error handling messages and recovery guidance

## 🏗️ Template Blueprint
Generate the protocol using the following structure:
```
# PROTOCOL 6: TECHNICAL DESIGN & ARCHITECTURE SPECIFICATION (ARCHITECTURE COMPLIANT)

## 1. AI ROLE AND MISSION
[Persona + mission + guardrail]

## 2. TECHNICAL DESIGN WORKFLOW
### STEP 1: Requirements & Context Alignment
[Steps with MUST/GUIDELINE markers, halt conditions, automation notes]

### STEP 2: Architecture Modeling & Decision Capture
[Steps, evidence, automation as specified in form]

### STEP 3: Validation, Risks, and Sign-off
[Steps, validation, approval prompts]

## 3. INTEGRATION POINTS
[List inputs/outputs and artifact usage]

## 4. QUALITY GATES
[Describe each gate with criteria/evidence/failure handling]

## 5. COMMUNICATION PROTOCOLS
[Announcements, validation prompts, error handling]

## 6. AUTOMATION HOOKS
[Script commands with expected outputs]

## 7. HANDOFF CHECKLIST
[Checklist + completion command]
```
- Follow numbering semantics (1..7) consistent with existing protocols.
- Translate evidence collection blocks from the form into descriptive paragraphs/bullet lists inside each phase.
- Present automation commands in fenced code blocks with expected output notes.

## 🤖 Automation & Evidence Integration
- Convert each `automation_hook` entry into dedicated subsections or inline callouts in the relevant phase.
- Reference evidence storage paths explicitly (e.g., `.artifacts/design/...`).
- When citing automation commands, include explanatory text similar to existing protocols (e.g., `*Expected Output:* ...`).

## ✅ Quality Acceptance Checklist
**Structural Compliance**
- [ ] Header matches protocol naming convention and domain tag
- [ ] Sections 1–7 present in order and properly titled
- [ ] Steps use `[MUST]` / `[GUIDELINE]` markers and include communications + halt conditions

**Content Completeness**
- [ ] Inputs/outputs mention the exact artifacts specified in the form
- [ ] Evidence collection and quality gates mirror form criteria
- [ ] Communication protocols include announcements, validation prompts, and error handling templates
- [ ] Automation commands align with scripts listed in the form

**Validation Readiness**
- [ ] Protocol references stored evidence paths under `.artifacts/design/`
- [ ] Handoff checklist includes approval log and risk register completion
- [ ] Completion command transitions to Protocol 2

## 🔁 Circular Validation Workflow
1. Generate the protocol and save as `6-technical-design-architecture.md`.
2. Run Meta-Analysis Generator to ensure all four layers are extractable.
3. Confirm validation output highlights traceability, gates, procedural steps, and communication grammar.
4. Regenerate if any layer is missing or subsystem mapping is incomplete.

## ⚠️ Failure Handling Guidance
- **Missing form fields** → Request updates to the YAML form before generation.
- **Conflicting integration references** → Cross-check protocol numbers and artifacts; adjust form to resolve.
- **Automation script mismatch** → Verify script availability in `/scripts`; replace with alternatives if absent.
- **Validation gaps** → Ensure each gate has measurable criteria and associated evidence before finalizing.

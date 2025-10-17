# Protocol 11 Generator Instructions — Production Deployment & Release Management

## 1. Objective
Generate `.cursor/ai-driven-workflow/11-production-deployment.md` from `protocol-input-form-11-deployment.yaml` to formalize release execution with governance checkpoints.

## 2. Input Inventory
- Completed requirements form for Protocol 11.
- References to Protocol 10 artifacts (staging bundle, release plan) for integration naming.
- Monitoring and incident protocol identifiers for downstream links.

## 3. Output Schema
Follow canonical section order with `(Release Governance Compliant)` domain tag:
1. Header + Role & Mission with `[CRITICAL]` guardrail.
2. `## 2. PRODUCTION DEPLOYMENT WORKFLOW` containing three phases.
3. Integration, Quality Gates, Communication, Handoff sections.

## 4. Phase Construction Rules
- **Phase Titles:** Use wording from the form: `Release Readiness and Change Control Verification`, `Controlled Deployment Execution`, `Post-Deployment Stabilization and Handoff`.
- **Steps:** Maintain `[MUST]` for critical steps; `[GUIDELINE]` for timeline publishing and incremental rollout.
- **Automation:** Each phase must call out at least one script (`validate_release_package.py`, `pre_release_checks.py`, `post_release_health.py`). Render as inline code in bullet list after the action.
- **Evidence:** Provide explicit `.artifacts/deployment/...` paths matching form data.

## 5. Layer Mapping Reference
| Layer | Required Elements |
|-------|-------------------|
| L1 | Mission statement + guardrail stressing approvals before deployment. |
| L2 | Quality gates (Release Readiness, Deployment Execution, Stabilization) with failure handling referencing rollback. |
| L3 | Detailed steps for readiness, pipeline execution, stabilization with automation commands and halt conditions. |
| L4 | Communication sequences, approval prompts, error handling narratives. |

## 6. Communication Patterns
- Status announcements must cover all three phases with start/complete statements.
- Include two validation prompts: release approval and go-live confirmation.
- Error handling entries: `MissingApproval`, `DeploymentFailure`, `HealthCheckFailure` using bracketed error names.

## 7. Integration Expectations
- Inputs: cite Protocol 10 artifacts exactly (`.artifacts/staging/release-bundle/`, `staging-validation-report.json`, etc.).
- Outputs: list deliverables for Protocol 12 and 13 using filenames from the form.
- Mention relationship to Protocol 4/5 only if derived from form (do not invent new dependencies).

## 8. Quality Checklist
- [ ] Title includes “Production Deployment & Release Management”.
- [ ] Three quality gates with criteria/evidence/failure-handling paragraphs.
- [ ] Release decision log, monitoring handoff package, evidence archive explicitly referenced.
- [ ] Handoff checklist contains five items leading to completion code block referencing Protocol 12.
- [ ] Guardrail states approval requirement before release.

## 9. Circular Validation Readiness
- Confirm meta-analysis will detect pipeline -> monitoring handoff -> incident response data flow.
- Double-check ASCII-friendly bullet formatting (no tabs, trailing spaces).
- Ensure automation commands align with scripts directory naming.

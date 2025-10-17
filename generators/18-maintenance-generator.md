# Generator: Protocol 18 – Continuous Maintenance & Support Planning

## 1. Purpose
Enable AI agents to transform `protocol-input-form-18-maintenance.yaml` into `18-maintenance-support.md`, defining the sustainment charter, operational workflows, governance cadence, and readiness validation needed for steady-state operations.

## 2. Required Inputs
- Completed `protocol-input-form-18-maintenance.yaml`
- Upstream artifacts: Monitoring outputs (Protocol 12), incident learnings (Protocol 13), performance optimizations (Protocol 14), UAT feedback (Protocol 15), documentation & feedback backlog (Protocol 16), closure ownership matrix (Protocol 17)
- Tooling references: ticketing platform, monitoring systems, backlog management tools, reporting automation
- Automation scripts: `scripts/assess_support_capacity.py`, `scripts/configure_ticket_routing.py`, `scripts/sync_maintenance_backlog.py`, `scripts/activate_maintenance_monitoring.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Sustainment Program Lead accountable for long-term reliability
- Guardrail: Maintenance cannot be finalized without ownership, processes, backlog intake, and capacity commitments
- Dependencies: Inputs from Protocols 12–17; outputs to support teams, Protocol 5 retrospectives, future bootstraps

### Layer 2 – Behavioral Control
- Gates: Charter & capacity, operations enablement, governance, readiness validation
- Halt conditions: SLA conflicts, workflow misconfigurations, inactive monitoring
- Prompts: Capacity alert, readiness approval confirmation

### Layer 3 – Procedural Logic
- Phases: Charter assessment → Operational workflow setup → Governance/backlog planning → Readiness validation
- Evidence: Maintenance charter, capacity analysis, tooling checklist, runbook index, support workflow, reporting spec, backlog register, release policy, feedback loop map, readiness approval log, monitoring activation, review calendar
- Automation: Capacity assessment, ticket routing configuration, backlog sync, monitoring activation

### Layer 4 – Communication Grammar
- Phase announcements for charter, operations, governance, readiness
- Validation prompts for capacity gaps and readiness approval
- Error handling for SLA conflicts, workflow misconfigurations, monitoring inactivity

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading `# PROTOCOL 18: CONTINUOUS MAINTENANCE & SUPPORT PLANNING (OPERATIONS SUSTAINMENT COMPLIANT)`
2. Section **1. AI ROLE AND MISSION** with guardrail matching sustainment commitments
3. Section **2. CONTINUOUS MAINTENANCE & SUPPORT WORKFLOW** with four STEP sections derived from form phases
4. Section **3. INTEGRATION POINTS** enumerating inputs (Protocols 12–17) and outputs (support teams, Protocol 5, future bootstraps)
5. Section **4. QUALITY GATES** covering charter/capacity, operations enablement, governance, readiness validation gates
6. Section **5. COMMUNICATION PROTOCOLS** with announcements, prompts, and error handling tokens
7. Section **6. AUTOMATION HOOKS** citing four automation scripts with parameters
8. Section **7. HANDOFF CHECKLIST** ensuring sustainment readiness items are confirmed

## 5. Automation Hook Rules
- Use `.artifacts/maintenance/` for generated evidence paths
- Ensure `assess_support_capacity.py` writes to `capacity-analysis.csv`
- Reference documentation feedback backlog as the source for `sync_maintenance_backlog.py`
- Activate monitoring via plan file `monitoring-activation.json`

## 6. Quality Acceptance Criteria
- `[MUST]` actions map directly to evidence filenames defined in the form
- Gates mention artifacts like `maintenance-charter.md`, `support-workflow.yaml`, `release-policy.md`, `readiness-approval-log.csv`
- Communication prompts keep `[CAPACITY ALERT]` and `[READINESS APPROVAL]` tokens intact
- Integration outputs include operational support teams, Protocol 5, and future bootstraps references
- Guardrail wording aligns with form statement regarding ownership, processes, backlog, and capacity commitments

## 7. Generation Workflow for the AI
1. Validate form completeness and dependency references
2. Convert each phase into Markdown steps with `[MUST]/[GUIDELINE]` actions, evidence, communications, and automation hooks
3. Populate integration and quality gate sections using form data
4. Insert communication templates and error handling verbatim
5. Confirm automation hooks span capacity assessment, ticket configuration, backlog sync, and monitoring activation
6. Save final output to `.cursor/ai-driven-workflow/18-maintenance-support.md`

## 8. Output & Post-Generation Actions
- Recommend notifying operational owners that maintenance charter is ready for activation
- Suggest updating Protocol 5 retrospective inputs with review calendar and feedback loop map
- Encourage running meta-analysis validation to maintain circular compliance

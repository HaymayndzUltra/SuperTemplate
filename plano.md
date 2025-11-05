Master RAY™ Protocol‑Script Audit

The following table reviews each of the 23 MASTER RAY™ protocols, summarising the automation hooks currently defined in the protocol (as seen in the AUTOMATION HOOKS sections), manual steps that could benefit from automation, opportunities for better script use, and missing or mis‑aligned scripts. An approximate automation score reflects how much of each protocol’s workflow is presently automated.

| Protocol | Current automation scripts (from protocol) | Manual steps that should be automated | Better script alternatives / observations | Missing or mis‑aligned scripts | Automation score |
| --- | --- | --- | --- | --- | --- |
| 01 Client Proposal Generation | Automates job‑post analysis, tone mapping and structural validation using analyze_jobpost.py, tone_mapper.py, validate_proposal_structure.py, validate_proposal.py, validate_evidence_manifest.py and evidence aggregation via aggregate_evidence_01.py. | Manual tailoring of tone and style, manual extraction of similar proposals, and human review of proposal sections remain. | Use an AI style‑calibrator script to learn preferred writing style from past client feedback, and integrate an auto citation collector that pulls relevant case studies from the knowledge base. | No script validates the historical examples used in proposals; a validate_examples.py script would enforce consistency. | ≈ 80 % |
| 02 Client Discovery Initiation | Optional automation collects context via summarize_job_post.py, extracts assumptions (assumption_extractor.py) and pre‑fills integration inventory. Gate validation uses validate_gate_02_pre_call.py, validate_gate_02_data_capture.py, validate_gate_02_recap.py, validate_gate_02_handoff.py and evidence aggregator aggregate_evidence_02.py. | Scheduling discovery calls, assembling question lists and sending recap e‑mails are manual. | Adopt an automatic calendar scheduling hook that books discovery sessions based on stakeholder availability and a questionnaire generator that tailors questions by project category. | No script validates call transcription quality or ensures that next‑step commitments are captured; an validate_discovery_transcript.py script would close this gap. | ≈ 75 % |
| 03 Project Brief Creation | Runs validate_prerequisites_03.py, checks discovery inputs (validate_discovery_inputs.py), validates brief structure (validate_brief_structure.py), verifies approvals (verify_brief_approvals.py) and aggregates evidence via aggregate_evidence_03.py. | Brief assembly and narrative writing are still manual. | Introduce an auto‑brief compiler that assembles sections from validated discovery artefacts and a digital approval workflow to collect sign‑offs. | Scripts only cover high‑level structure; there is no semantic validation of the brief. A new validate_brief_content.py could check for missing context or misaligned requirements. | ≈ 80 % |
| 04 Project Bootstrap & Context Engineering | Automation hooks call validate_prerequisites_04.py, validate_brief.py, rules_audit_quick.py, validate_scaffold.py, validate_workflows.py and collect evidence via aggregate_evidence_04.py. | Running environment doctors and verifying generated scaffolds are sometimes executed manually. | The repository already contains doctor.py and scaffold_phase_artifacts.py; integrating them as default hooks would remove manual runs. | Quality gates mention rules‑audit checks but no script ensures that environment doctor output meets baseline criteria; a validate_environment_doctor.py is needed. | ≈ 85 % |
| 05 Bootstrap Your Project (Legacy Alignment) | Uses validate_prerequisites_05.py, validate_rule_metadata.py, validate_repo_mapping.py, validate_principles.py, rules_audit_quick.py and evidence aggregator aggregate_evidence_05.py. | Mapping legacy repositories and reconciling rule deviations requires manual cross‑checking. | A legacy‑alignment tool could automatically diff the new scaffold against legacy modules and flag mismatches. | Missing scripts for verifying historical rule compliance and generating delta reports; adding generate_legacy_diff.py would formalise this check. | ≈ 70 % |
| 06 Create PRD | Validation hooks run validate_prerequisites_1.py, validate_prd_context.py, validate_prd_requirements.py, validate_prd_gate.py and aggregate evidence via aggregate_evidence_1.py. | Capturing and structuring stakeholder requirements still involves manual synthesis. | Introduce a requirements‑elicitation tool that collates objectives from discovery notes and auto‑populates the PRD template. | Quality gates focus on structure but not on requirement completeness or traceability; a validate_prd_traceability.py script could ensure that each requirement maps to a business goal. | ≈ 70 % |
| 07 Technical Design & Architecture | Runs validate_prerequisites_6.py, reuses validate_brief.py, generates a plan from the brief (plan_from_brief.py), checks workflow integration (validate_workflow_integration.py), validates design handoff (validate_design_handoff.py) and aggregates evidence via aggregate_evidence_6.py. | Architectural decomposition and diagramming rely on manual engineering judgement. | Leverage existing architecture‑generation scripts (e.g., export_sequence_diagrams.py referenced in Protocol 19) to auto‑produce diagrams and integrate plan_from_brief.py outputs. | Missing scripts for consistency checking between design diagrams and the PRD; a validate_architecture_consistency.py would reduce manual review. | ≈ 75 % |
| 08 Technical Task Generation | Automation hooks (not shown here due to length) include validate_prerequisites_2.py, validate_rule_index.py, validate_high_level_tasks.py, validate_task_decomposition.py, validate_tasks.py, enrich_tasks.py and evidence aggregator aggregate_evidence_2.py. | Breaking down complex features into granular tasks often requires manual judgement. | Use AI‑assisted task‑clustering algorithms to group similar tasks and propose dependencies. | Scripts do not cross‑validate tasks against PRD acceptance criteria; a validate_task_to_prd_mapping.py script is missing. | ≈ 70 % |
| 09 Environment Setup & Validation | Hooks run validate_prerequisites_7.py, doctor.py, scaffold_phase_artifacts.py, execute a shell installer and test script (install_and_test.sh), package assets (package_environment_assets.py) and aggregate evidence with aggregate_evidence_7.py. | Manual verification of environment configuration, scanning for missing dependencies and packaging deliverables. | A consolidated environment bootstrap script could orchestrate installation, testing, packaging and produce a standard report. | Quality gates reference environment health but there is no script to compare actual configuration against required specifications; a validate_environment_config.py is needed. | ≈ 65 % |
| 10 Controlled Task Execution | Automation hooks run validate_prerequisites_3.py, preflight checks (validate_preflight.py), subtask compliance (validate_subtask_compliance.py), quality gate validation (validate_quality_gate.py), session close‑out (validate_session_closeout.py), evidence aggregation via aggregate_evidence_3.py and a CI script run_protocol_3_gates.py. | Real‑time monitoring of execution progress and capturing developer intent remain manual. | Integrate a task execution monitor that streams progress, logs anomalies and automatically triggers validations after each sub‑task. | Missing scripts for evaluating adherence to coding standards or security policies during execution; creating validate_execution_security.py would strengthen compliance. | ≈ 70 % |
| 11 Integration Testing & System Validation | Runs validate_prerequisites_9.py, environment validation (validate_environment.py), executes contract tests (run_contract_tests.py), runs integration tests via pytest -m integration, generates manifest via generate_artifact_manifest.py and aggregates evidence with aggregate_evidence_9.py. | Defining test scenarios, interpreting test results and determining next actions require manual analysis. | Use a test‑orchestration framework to auto‑select appropriate test suites based on system changes and summarise results for humans. | No script evaluates the coverage of integration tests; a validate_integration_coverage.py script would quantify coverage against requirements. | ≈ 75 % |
| 12 Quality Audit Orchestrator | Validation uses validate_prerequisites_4.py, validate_gate_4_pre_audit.py, validate_gate_4_reporting.py, evidence aggregation via aggregate_evidence_4.py and specialised scripts like collect_change_context.py, run_comprehensive_review.py, validate_router_mapping.py, verify_specialized_execution.py. | Selecting audit pathways (standard vs specialised) and triaging findings require manual oversight. | Adopt an adaptive audit router that chooses appropriate review pathways based on change context and auto‑produces remediation tickets. | Missing scripts for summarising audit outcomes across multiple modules; a generate_audit_summary.py script would help. | ≈ 80 % |
| 13 UAT Coordination | Uses validate_prerequisites_15.py, validates UAT entry (validate_gate_15_entry.py), defect triage (validate_gate_15_defects.py), aggregates evidence with aggregate_evidence_15.py and optionally builds UAT tools (build_uat_toolkit.py) and generates release notes (generate_release_notes.py). | Scheduling sessions, collecting feedback and tracking defect resolution remain manual. | Implement a UAT scheduling assistant that invites testers, records attendance and collates feedback. | No script validates completeness of release notes or ensures defects are linked back to requirements; validate_release_notes.py and validate_defect_traceability.py would close gaps. | ≈ 65 % |
| 14 Pre‑Deployment Staging | Automation hooks call validate_prerequisites_10.py, gate validators validate_gate_10_intake.py and validate_gate_10_readiness.py plus evidence aggregator aggregate_evidence_10.py. Quality gate definitions mention validate_gate_10_rehearsal.py and validate_gate_10_security.py, but these scripts are not referenced in the hooks. | Staging rehearsal drills and security hardening checks often rely on manual test runs. | Include validate_gate_10_rehearsal.py and validate_gate_10_security.py in the automation section to ensure rehearsal and security gates run automatically. | Missing automation for release rehearse; create a run_staging_rehearsal.py script to simulate deployment and capture results. | ≈ 60 % |
| 15 Production Deployment & Release Management | Runs validate_prerequisites_11.py, validates readiness (validate_gate_11_readiness.py), launch (validate_gate_11_launch.py), aggregates evidence via aggregate_evidence_11.py and a CI script run_protocol_15_gates.py. Quality gates also list validate_gate_11_freeze.py and validate_gate_11_reporting.py, which are not in the automation hooks. | Approving release windows and verifying freeze adherence remain manual. | Integrate missing gate scripts into the automation hooks and add an automatic freeze window checker that validates code‑freeze status. | Missing validate_gate_11_freeze.py and validate_gate_11_reporting.py in hooks; these should be added. | ≈ 65 % |
| 16 Post‑Deployment Monitoring & Observability | Automation hooks run validate_prerequisites_12.py, instrumentation validation (validate_gate_12_instrumentation.py), handoff validation (validate_gate_12_handoff.py) and evidence aggregation via aggregate_evidence_12.py. Additional gates in the protocol specify validate_gate_12_alerts.py and validate_gate_12_assurance.py, which are absent from automation hooks. | Monitoring dashboards and alert thresholds often tuned manually, and baselines updated manually after deployment. | Include missing scripts (validate_gate_12_alerts.py, validate_gate_12_assurance.py) and create a dynamic alert checker that cross‑references SLO thresholds with live metrics. | Automation hooks misalign with quality gates; script numbering should be adjusted to Protocol 16 naming (validate_prerequisites_16 etc.). | ≈ 60 % |
| 17 Incident Response & Rollback | Runs validate_prerequisites_13.py, severity validation (validate_gate_13_severity.py), resolution validation (validate_gate_13_resolution.py) and evidence aggregator aggregate_evidence_13.py. Quality gates also mention validate_gate_13_mitigation.py and validate_gate_13_recovery.py which are missing. | Assessing incident severity, coordinating mitigation and executing rollbacks require manual decision‑making. | Introduce automated severity classifiers and a rollback orchestrator script that can roll back deployments based on version metadata and approval signals. | Missing validate_gate_13_mitigation.py and validate_gate_13_recovery.py scripts in hooks; these should be developed and integrated. | ≈ 55 % |
| 18 Performance Optimization & Tuning | Automation hooks reference validate_prerequisites_14.py, baseline validation (validate_gate_14_baseline.py), optimization validation (validate_gate_14_optimization.py) and evidence aggregation via aggregate_evidence_14.py. Note that script numbers refer to 14 even though this is Protocol 18. | Collecting telemetry, establishing baselines and profiling transactions are largely manual. | Create scripts to automatically extract performance baselines (e.g., performance_baseline_collector.py) and integrate load‑testing tooling. | The numbering mismatch suggests missing validate_prerequisites_18.py, validate_gate_18_baseline.py and validate_gate_18_optimization.py. These scripts should be created and registered in the registry. | ≈ 50 % |
| 19 Documentation & Knowledge Transfer | Runs validate_prerequisites_16.py, checks completeness (validate_gate_16_completeness.py), enablement (validate_gate_16_enablement.py), publication (validate_gate_16_publication.py) and aggregates evidence via aggregate_evidence_16.py. Again, numbering reflects Protocol 16 instead of 19. | Drafting documentation, conducting knowledge‑transfer sessions and capturing approvals remain manual. | Adopt a document generator that extracts architecture diagrams (already referenced by export_sequence_diagrams.py) and uses templates to compile runbooks; integrate an enablement scheduler to automate session logistics. | Missing validate_prerequisites_19.py and gate validators aligned with Protocol 19; numbering should be corrected, and a validate_gate_19_publication_integrity.py script added. | ≈ 50 % |
| 20 Project Closure & Handover | Automation hooks call validate_prerequisites_17.py, deliverable validation (validate_gate_17_deliverables.py), handover readiness (validate_gate_17_handover.py), governance closure (validate_gate_17_governance.py) and evidence aggregation via aggregate_evidence_17.py. Numbering corresponds to Protocol 17, not 20. | Auditing the deliverable register, validating financial closure and capturing stakeholder acceptance require manual coordination. | Add a closure checklist generator that compiles deliverables, budgets and approvals into a single dashboard for validation. | Scripts for validate_gate_20_* are missing; numbering should align with Protocol 20 and additional scripts (e.g., validate_gate_20_financials.py) created. | ≈ 60 % |
| 21 Continuous Maintenance & Support Planning | Automation hooks run validate_prerequisites_18.py, backlog integrity (validate_gate_18_backlog.py), approval confirmation (validate_gate_18_approvals.py), governance cadence (validate_gate_18_governance.py) and aggregate evidence via aggregate_evidence_18.py. Numbering corresponds to 18 rather than 21. | Consolidating maintenance backlog, prioritising items and forecasting support demand require manual spreadsheets. | Implement a maintenance backlog aggregator that merges technical debt logs, incident logs and performance backlog; use a scoring algorithm for prioritisation. | Scripts aligned with Protocol 21 should be created (validate_prerequisites_21.py, etc.) and hooks should invoke them; additional validation for demand forecast accuracy is missing. | ≈ 60 % |
| 22 Implementation Retrospective | Automation hooks call validate_prerequisites_5.py, gate validators validate_gate_5_participation.py, validate_gate_5_action_plan.py, validate_gate_5_integration.py and evidence aggregator aggregate_evidence_5.py. Numbering references Protocol 5 rather than 22. | Facilitating retrospective meetings, capturing insights and assigning action items still require manual intervention. | Provide a retrospective facilitator tool that collates artifacts across protocols, runs sentiment analysis on session notes and suggests improvement actions. | Missing validate_prerequisites_22.py and gate scripts aligned to Protocol 22; create these and ensure the automation hooks call them. | ≈ 55 % |
| 23 Script Governance | Governance toolkit executes validate_script_registry.py to check coverage, auto‑registers orphaned scripts via auto_register_scripts.py and generates artefacts via generate_protocol_23_artifacts.py. Validation hooks call validate_prerequisites_8.py, inventory and artifact gates (validate_gate_8_inventory.py, validate_gate_8_artifacts.py) and aggregate evidence via aggregate_evidence_8.py. Quality gates also reference validate_gate_8_static.py and validate_gate_8_reporting.py. | Some spot‑checks and static analysis triage remain manual. | The provided toolkit covers discovery, registration and compliance checks; use this to replace manual list comparison. | Hooks rely on Protocol 8 validators instead of Protocol 23. Scripts such as validate_gate_23_static.py and validate_gate_23_reporting.py should be created and registry updated accordingly. | ≈ 70 % |

Key Themes from the Audit

Script numbering inconsistencies – Many protocols reference validation scripts belonging to different protocol numbers (e.g., Protocol 18 calls validate_prerequisites_14.py, Protocol 19 calls Protocol 16 scripts). This misalignment likely stems from copy‑paste errors when generating templates. Correcting these names (both in the automation hooks and in the script registry) is critical for CI pipelines to run the appropriate validations.

Missing gates and validators – Quality gate sections often mention scripts (e.g., rehearsal, security, mitigation) that are not invoked in the automation hooks. These omissions reduce automation coverage and can lead to manual exceptions. Hooks should be updated to call all defined gate validators, and missing scripts should be implemented.

Manual processes ripe for automation – Scheduling meetings, collecting approvals, drafting narrative documents and consolidating data from multiple sources are repeated across protocols. Building reusable automation (scheduling assistants, backlog aggregators, report generators) would greatly increase efficiency.

Need for semantic validation – Current scripts mainly validate file presence and structural completeness. Semantic checks (e.g., mapping tasks to requirements, ensuring documentation accuracy, analysing performance bottlenecks) are often missing. New validation scripts should perform deeper content analysis using AI or rule‑based heuristics.

Evidence aggregation is well‑established – Each protocol provides an aggregate_evidence_X.py script, ensuring evidence packaging is consistent. Maintaining this pattern while adding missing validation scripts will provide a robust trail for audits.

Script Recommendations:
Script Recommendations

This document outlines proposed improvements to the automation layer across the MASTER RAY™ protocols. Recommendations fall into four categories:

Scripts to add – New automation components that would eliminate manual steps or provide deeper validation.

Scripts to replace – Existing hooks that should be swapped for better alternatives or corrected for protocol numbering alignment.

Scripts to create – Entirely new validators or utilities needed because the workflow currently lacks automation.

Scripts to deprecate – Orphaned or redundant scripts that no longer serve an operational purpose.

1. New Scripts to Add

| Protocol | Script Name | Specification & Rationale |
| --- | --- | --- |
| 01 | style_calibrator.py | Learns tone and style preferences from previously approved proposals and applies these settings when generating new proposals. Inputs: client domain, previous proposals; Output: style profile and transformed draft. Replaces manual tone mapping.
 |
|  | validate_examples.py | Ensures examples included in proposals are relevant, anonymised, and correctly cited. Validates that each example maps to the problem statement and that all sensitive data has been removed. |
| 02 | schedule_discovery_call.py | Integrates with calendar APIs to automatically propose meeting times to stakeholders, book the call and attach the briefing packet. Should log the meeting link and participants in the evidence directory. |
|  | questionnaire_generator.py | Generates a tailored question set based on the project category and client maturity, pulling from a library of discovery prompts. Produces a Markdown/CSV file for the call agenda. |
|  | validate_discovery_transcript.py | Processes call transcripts to ensure that all critical topics were addressed and summarises decisions. Flags missing requirements and requests follow‑up questions. |
| 03 | auto_compile_brief.py | Takes validated discovery inputs and automatically assembles a draft project brief using the standard template. Includes sections for objectives, scope, stakeholders, timeline and assumptions. Embeds cross‑references to the PRD when available. |
|  | validate_brief_content.py | Analyses the brief for completeness and semantic consistency. Checks that every requirement is traced to discovery evidence and that no conflicting statements exist. |
| 04 | validate_environment_doctor.py | Parses the output of doctor.py to verify that all pre‑bootstrap environment checks meet minimum thresholds (e.g., correct Python version, available disk space). Flags issues before scaffold generation. |
| 05 | generate_legacy_diff.py | Compares the generated scaffold against legacy repositories to highlight structural or dependency differences. Produces a diff report and a checklist of remediation items. |
| 06 | validate_prd_traceability.py | Ensures every requirement in the PRD is linked to a business goal and has acceptance criteria. Generates a traceability matrix to support later validation. |
| 07 | validate_architecture_consistency.py | Cross‑checks the technical design against the PRD and brief, verifying that all components and data flows support the defined requirements. Flags misaligned or missing modules. |
| 08 | validate_task_to_prd_mapping.py | Verifies that every generated task can be traced back to a requirement in the PRD or brief. Produces a mapping file used by downstream validation. |
| 09 | validate_environment_config.py | Reads environment configuration files and compares them against a specification defined in the brief/PRD. Detects missing environment variables, incorrect versions or unapproved network ports. |
| 10 | task_execution_monitor.py | Streams live progress of tasks, captures logs and automatically triggers validation scripts at appropriate checkpoints. Provides a dashboard summarising task statuses and exceptions. |
|  | validate_execution_security.py | Runs static and dynamic security checks during task execution to ensure that code follows secure coding practices and does not introduce vulnerabilities. |
| 11 | validate_integration_coverage.py | Analyses test manifests to determine whether integration tests cover all critical business flows and interfaces. Outputs coverage metrics and identifies gaps. |
| 12 | generate_audit_summary.py | Aggregates results from specialised audit scripts and produces a concise summary for stakeholders, including severity levels, impacted components and recommended fixes. |
| 13 | uat_schedule_assistant.py | Automates UAT scheduling based on tester availability and sends invites, reminders and follow‑up surveys. Tracks attendance and collates feedback into the evidence package. |
|  | validate_release_notes.py | Checks that release notes generated during UAT accurately reflect features, bug fixes and known issues, and that all tickets referenced are closed or deferred with approvals. |
| 14 | run_staging_rehearsal.py | Executes a rehearsal deployment using staging infrastructure, collects deployment metrics and verifies rollback procedures. Generates a rehearsal report used by validate_gate_10_rehearsal.py. |
|  | validate_gate_14_security.py | Performs automated penetration tests and static analysis on release artefacts to ensure that security baselines are met before deployment. Replaces manual security reviews during staging. |
| 15 | freeze_window_validator.py | Verifies that no code changes have occurred within the defined release freeze window and that all exceptions have been documented and approved. |
|  | validate_gate_15_reporting.py | Ensures that post‑deployment reports and communications are complete and consistent with governance requirements. |
| 16 | alert_threshold_checker.py | Checks that monitoring alerts align with current SLO values and that alert thresholds are appropriately calibrated for the post‑deployment period. |
|  | validate_gate_16_assurance.py | Confirms that post‑deployment health checks and observability updates (dashboards, runbooks) have been completed and signed off. |
| 17 | incident_severity_classifier.py | Uses incident metadata (e.g., impact, duration, affected users) to classify severity automatically and recommend appropriate mitigation steps. |
|  | rollback_orchestrator.py | Coordinates automated rollback of affected services based on version control metadata, feature flags and configuration snapshots. Provides a clear evidence log for the rollback sequence. |
| 18 | performance_baseline_collector.py | Automates the collection of baseline performance metrics across monitored services and writes them to a CSV/JSON with timestamp and methodology details. Integrates with APM tooling to gather throughput, latency and error rates. |
|  | validate_gate_18_optimization.py | Ensures that applied optimisations deliver the targeted improvement (≥15 %) and that no regressions are detected. Should replace the mis‑numbered validate_gate_14_optimization.py. |
| 19 | doc_generator.py | Generates a cohesive documentation bundle by combining PRDs, architecture logs, sprint notes and audit reports. Utilises templates and includes diagrams extracted by export_sequence_diagrams.py. |
|  | enablement_scheduler.py | Automates planning and tracking of knowledge‑transfer sessions, capturing attendance and action items. |
| 20 | closure_checklist_generator.py | Produces a consolidated closure checklist that includes deliverable statuses, budget reconciliations, outstanding actions and approval signatures. Facilitates the validation of closure gates. |
| 21 | maintenance_backlog_aggregator.py | Merges technical debt logs, security risk registers, performance backlog items and incident remediations into a single prioritised backlog with owners and due dates. Generates an automation-candidates.json file listing tasks suitable for scripting. |
| 22 | retrospective_analysis.py | Automatically synthesises cross‑protocol learnings, performs thematic analysis on notes, ranks actions by impact/effort and generates an improvement plan with owners and follow‑up protocols. |
| 23 | validate_gate_23_static.py | Consolidates static analysis results (pylint, shellcheck, yamllint) and determines whether blocker‑severity findings exist. Should replace references to validate_gate_8_static.py. |
|  | validate_gate_23_reporting.py | Checks that governance scorecards and remediation backlogs are complete and that all non‑compliant scripts have associated actions. |

2. Scripts to Replace / Correct

| Protocol | Current Script | Replacement & Justification |
| --- | --- | --- |
| 18 | validate_prerequisites_14.py | Rename to validate_prerequisites_18.py and update logic to validate performance optimisation prerequisites (telemetry packages, incident reports, baseline metrics) rather than pre‑deployment requirements. Ensures numbering consistency and domain‑specific checks. |
|  | validate_gate_14_baseline.py | Rename to validate_gate_18_baseline.py to align with Protocol 18 and adjust thresholds to performance domain (baseline completeness ≥95 %). |
|  | validate_gate_14_optimization.py | Rename to validate_gate_18_optimization.py and modify parameters to reflect the required improvement threshold for optimisation phases (≥15 %). |
| 19 | validate_prerequisites_16.py | Rename to validate_prerequisites_19.py to ensure correct mapping. Adjust checks to verify presence of documentation and knowledge‑transfer artefacts rather than monitoring assets. Similar renaming applies to validate_gate_16_completeness.py, validate_gate_16_enablement.py, validate_gate_16_publication.py and aggregate_evidence_16.py. |
| 20 | validate_prerequisites_17.py, validate_gate_17_deliverables.py, validate_gate_17_handover.py, validate_gate_17_governance.py | Rename to Protocol 20 equivalents (validate_prerequisites_20.py, etc.) and update logic to validate closure artefacts. Replace aggregate_evidence_17.py with aggregate_evidence_20.py for consistency. |
| 21 | validate_prerequisites_18.py, validate_gate_18_backlog.py, validate_gate_18_approvals.py, validate_gate_18_governance.py | Rename to Protocol 21 equivalents and adapt logic to maintenance planning (backlog consolidation, approval confirmation, governance cadence). Update CI script references from run_protocol_18_gates.py to run_protocol_21_gates.py. |
| 22 | validate_prerequisites_5.py, validate_gate_5_participation.py, validate_gate_5_action_plan.py, validate_gate_5_integration.py | Replace with Protocol 22 validators and update aggregator to aggregate_evidence_22.py. Adjust gating logic to evaluate participation, action readiness and continuous improvement integration in retrospective contexts. |
| 23 | validate_prerequisites_8.py, validate_gate_8_inventory.py, validate_gate_8_artifacts.py | Replace with Protocol 23 validators reflecting script governance. Add missing validators validate_gate_23_static.py and validate_gate_23_reporting.py to correspond with the quality gates defined in Protocol 23. |

3. Scripts to Create (Requirements)

In addition to the new scripts listed above, several protocols are missing validation scripts referenced in their quality gate sections. These should be created with the following high‑level requirements:

validate_gate_10_rehearsal.py – Called by Protocol 14; verifies that a successful deployment rehearsal has been executed in staging. Inputs: rehearsal report (rehearsal-report.json); Outputs: pass/fail result and coverage metrics.

validate_gate_10_security.py – Conducts pre‑deployment security checks using static and dynamic analysis. Inputs: release artefacts; Outputs: vulnerability report and pass/fail status.

validate_gate_11_freeze.py – Ensures that code freeze policies were adhered to before production deployment. Inputs: commit history; Outputs: list of commits within freeze window, approval evidence.

validate_gate_11_reporting.py – Confirms that deployment reports (DEPLOYMENT-REPORT.md) and release notes are complete, published and accessible.

validate_gate_12_alerts.py – Verifies that alert thresholds are configured correctly post‑deployment and that no critical alerts are firing unexpectedly.

validate_gate_12_assurance.py – Validates that observability and monitoring dashboards have been updated, that runbooks exist and that on‑call handoffs have been completed.

validate_gate_13_mitigation.py – For incident response (Protocol 17); ensures that mitigation steps (e.g., work‑arounds or patches) have been executed correctly.

validate_gate_13_recovery.py – Confirms that recovery (rollback or hotfix) procedures have restored service levels to acceptable thresholds and documents lessons learned.

validate_gate_14_diagnostics.py – Referenced in the quality gates of Protocol 18; validates that diagnostic coverage meets the required threshold (≥90 % of services and scenarios).

validate_gate_14_governance.py – Ensures that SLO updates, performance reports and continuous improvement notes have been documented before hand‑off.

validate_gate_16_publication.py – Already referenced but may not exist; should validate that published documentation is accessible, versioned and complete.

Each of these validators should follow the standard pattern used across existing scripts: accept input file(s) or directory, compute a score or pass/fail result based on protocol criteria, write a JSON/YAML report into the .artifacts/ directory and exit with a non‑zero status code on failure for CI integration.

4. Scripts to Deprecate / Consolidate

The script registry currently contains several scripts that appear unused or duplicated across protocols due to numbering errors. The following should be deprecated or consolidated:

Duplicate prerequisite validators (validate_prerequisites_1.py, validate_prerequisites_2.py, …) – Many protocols reuse prerequisite validators from unrelated protocols (e.g., Protocol 22 uses validate_prerequisites_5.py). Once protocol‑specific validators are created, the unused duplicates can be deprecated or replaced with generic validate_prerequisites.py functions that accept protocol IDs as parameters.

Deprecated gate scripts referencing incorrect numbers – Scripts such as validate_gate_4_pre_audit.py and validate_gate_4_reporting.py are used by Quality Audit but may overlap with later audit protocols. Evaluate whether they can be merged into more general validate_quality_audit_gate.py with configurable parameters.

Legacy CI wrappers (run_protocol_X_gates.py) – Some CI scripts are misnamed (e.g., run_protocol_5_gates.py is invoked by Protocol 22). Replace them with a single entry point (run_protocol_gates.py --protocol 22) that dynamically selects the correct validators from the script registry.

Orphaned evidence aggregators – The script registry lists aggregator scripts for protocols that no longer exist or are duplicated (aggregate_evidence_1.py appears in multiple contexts). Consolidate into a reusable aggregate_evidence.py that accepts the protocol ID and output directory, and deprecate protocol‑specific aggregators once backward compatibility is no longer required.

Implementing these recommendations will improve consistency, reduce maintenance overhead and ensure that automation evolves alongside the protocols.

Priority Roadmap:
The following roadmap prioritises the recommended improvements according to their expected impact on workflow efficiency and the estimated implementation effort. Critical actions deliver high impact with relatively low effort and should be addressed immediately. High priority items offer substantial benefits but may require more development time. Medium and Low priority tasks provide incremental improvements or are dependent on earlier changes.

Critical (High Impact × Low Effort)

Correct script numbering across all protocols. Rename mis‑aligned validation and aggregation scripts (e.g., Protocol 18 → 14, Protocol 19 → 16) and update automation hooks accordingly. This change is largely mechanical but eliminates CI failures and confusion.Add missing gate validators referenced in quality gate sections. Implement scripts such as validate_gate_10_rehearsal.py, validate_gate_11_freeze.py, validate_gate_12_alerts.py and integrate them into the automation hooks. These scripts fill clear coverage gaps and prevent manual work during critical release stages.

Introduce freeze_window_validator.py for Protocol 15. This script automates freeze compliance checks and eliminates human error during production deployment approvals.

Standardise evidence aggregation. Refactor existing aggregate_evidence_X.py into a single parameterised aggregate_evidence.py script. This change simplifies maintenance and ensures consistent output across protocols.

Implement validate_prd_traceability.py and validate_task_to_prd_mapping.py. These validators enforce traceability from requirements through task generation, reducing downstream rework.

Create a CI entry point wrapper (run_protocol_gates.py). Replace protocol‑specific CI scripts (run_protocol_5_gates.py, etc.) with a unified runner that accepts the protocol ID and dynamically executes the correct validators from the script registry.

High Priority

Develop the maintenance backlog aggregator (maintenance_backlog_aggregator.py). Merging technical debt, incidents, security risks and performance backlogs into a unified tracker provides immediate value to operations and reduces fragmentation.

Build retrospective_analysis.py for Protocol 22. Automating thematic analysis and action prioritisation accelerates the learning loop and generates better improvement plans.

Implement the performance baseline collector (performance_baseline_collector.py). Automated baseline collection will improve the accuracy of optimisation efforts and feed Protocol 18’s validation.

Create the incident severity classifier and rollback orchestrator. These tools will reduce time‑to‑resolution during incidents and enforce consistency across mitigation and recovery actions.

Introduce a UAT scheduling assistant and release note validator. Automating these UAT tasks will free up coordination effort and ensure that user‑facing documentation meets standards.

Medium Priority

Develop auto‑generated brief and PRD compilers. Automating narrative construction (auto_compile_brief.py, doc_generator.py) reduces cognitive load on engineers, but requires careful templating and integration with existing content.

Implement architecture and design consistency validators. Scripts like validate_architecture_consistency.py enhance design quality, but their value depends on the availability of machine‑readable architecture models.

Enhance task generation with AI‑based clustering and dependency detection. Building these capabilities will drive better task decomposition but demands more advanced modelling.

Add dynamic alert and SLO calibration tools. alert_threshold_checker.py and validate_gate_16_assurance.py will improve post‑deployment observability but require integration with monitoring platforms.

Extend script governance with Protocol 23‑specific validators. Writing validate_gate_23_static.py and validate_gate_23_reporting.py ensures governance completeness. This is lower urgency once numbering and inventory issues are addressed.

Low Priority

Deprecate duplicate prerequisite validators and consolidate aggregator scripts. This refactoring reduces code clutter but can be scheduled after new validators are stable.

Consolidate legacy CI wrappers. Replacing all run_protocol_X_gates.py with a unified script is beneficial but not blocking after mis‑numbering has been corrected.

Enhance documentation style enforcement and accessibility audits. Additional scripts (e.g., readability scorers) can be added later once core validation is automated.

Advanced audit router and quality summary generator. These provide incremental improvements to Protocol 12 but rely on other foundational changes.

Sequencing Considerations

Start by aligning script names and updating the registry. Until numbering is consistent, downstream improvements will not be reliable.

Immediately implement missing gate validators and update automation hooks to ensure that all defined quality gates are enforced without manual intervention.

Focus on high‑impact automation for handoff stages (e.g., maintenance backlog aggregation, incident response). These have direct benefits for operational teams.

Iteratively introduce advanced AI‑driven analysis scripts (architecture consistency, task clustering, retrospective analysis) after critical gaps are closed.

Finally, perform cleanup and consolidation (deprecation of duplicates and CI wrappers) once the new tooling is stable.
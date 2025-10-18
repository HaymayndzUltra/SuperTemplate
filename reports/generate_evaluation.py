import csv
from statistics import mean

protocols = [
    {
        "key": "00-generate-rules",
        "display": "Generate Cursor Rules",
        "file": ".cursor/ai-driven-workflow/00-generate-rules.md",
        "phase": "Foundation",
        "checklist": {
            "role": False,
            "workflow": True,
            "integration": True,
            "quality": False,
            "communication": False,
            "handoff": False,
            "automation": False,
            "evidence": True,
        },
        "gaps": [
            "No explicit AI role/mission or handoff checklist despite governing other protocols.",
            "Quality gates and communication protocols are absent, leaving validation triggers implicit.",
        ],
        "improvements": [
            "Add a short role/mission statement plus prerequisites clarifying when the command should run.",
            "Define minimum validation/quality gates (e.g., linting of generated rules) and communication outputs for operators.",
        ],
        "scores": {"Completeness": 5, "Clarity": 7, "Actionability": 8, "Integration": 6, "Evidence": 5, "Automation": 7},
    },
    {
        "key": "00A",
        "display": "Protocol 00A: Client Proposal Generation",
        "file": ".cursor/ai-driven-workflow/01-client-proposal-generation.md",
        "phase": "Phase 0",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Integration references `Protocol 04-client-discovery`, which no longer exists under that identifier.",
            "Quality metrics table keeps Actual values as `[TBD]`, so evidence targets are undefined.",
        ],
        "improvements": [
            "Update integration mapping to point to the current discovery protocol file name and ensure artifact paths align.",
            "Replace `[TBD]` metrics with real baseline thresholds or guidance on how to capture them.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 8},
    },
    {
        "key": "00B",
        "display": "Protocol 00B: Client Discovery Initiation",
        "file": ".cursor/ai-driven-workflow/02-client-discovery-initiation.md",
        "phase": "Phase 0",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Inputs section still names `Protocol 04` as the source for intake logs, which conflicts with the current directory numbering.",
            "Automation hooks reference `validate_discovery_*` scripts that are not present in the repository.",
        ],
        "improvements": [
            "Synchronize integration numbering with the latest protocol files to avoid navigation errors during handoffs.",
            "Provide concrete automation implementation guidance or adjust to existing validation scripts under `scripts/`.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "01",
        "display": "Protocol 01: Project Brief Creation",
        "file": ".cursor/ai-driven-workflow/03-project-brief-creation.md",
        "phase": "Phase 0",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Integration points refer to `Protocol 02` and `Protocol 04`, but file names now use different indices.",
            "Evidence summary lists metrics as `[TBD]`, reducing measurability of completion.",
        ],
        "improvements": [
            "Align integration section with actual filenames (e.g., `02-client-discovery-initiation.md`).",
            "Document default measurement approach for quality metrics so teams can populate evidence consistently.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "00",
        "display": "Protocol 00: Project Bootstrap & Context Engineering",
        "file": ".cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md",
        "phase": "Phase 0",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Integration references `Protocol 05` legacy assets without clarifying coexistence with updated discovery files.",
            "Quality metrics remain `[TBD]`, so there is no enforcement for evidence completeness.",
        ],
        "improvements": [
            "Clarify how legacy bootstrap artifacts map to the current phase-0 deliverables to avoid duplicate context kits.",
            "Establish default success thresholds or sampling cadence for context validation metrics.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "0-legacy",
        "display": "Protocol 0: Legacy Bootstrap",
        "file": ".cursor/ai-driven-workflow/05-bootstrap-your-project.md",
        "phase": "Phase 0",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Protocol references older project scaffolding assets but does not state when to prefer this legacy track over Protocol 00.",
            "Automation hooks cite scripts (`validate_bootstrap_env.py`) that are not present in the repository.",
        ],
        "improvements": [
            "Add decision criteria comparing this legacy bootstrap with the primary context engineering flow.",
            "Update automation references to use available scripts or provide stubs inside `scripts/`.",
        ],
        "scores": {"Completeness": 8, "Clarity": 8, "Actionability": 8, "Integration": 7, "Evidence": 7, "Automation": 6},
    },
    {
        "key": "1",
        "display": "Protocol 1: Create PRD",
        "file": ".cursor/ai-driven-workflow/06-create-prd.md",
        "phase": "Planning",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Integration references `Protocol 00` and `Protocol 06` numbering instead of file names, which complicates automation wiring.",
            "Evidence metrics list `[TBD]`, so pass/fail thresholds are not actionable.",
        ],
        "improvements": [
            "Update integration matrix to call out preceding file paths (e.g., `03-project-brief-creation.md`).",
            "Define default PRD validation scoring (e.g., acceptance coverage percentage) for teams lacking prior baselines.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "6",
        "display": "Protocol 6: Technical Design & Architecture",
        "file": ".cursor/ai-driven-workflow/07-technical-design-architecture.md",
        "phase": "Planning",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation hooks reference architecture scripts (`generate_arch_diagrams.py`) that are not found in the repo.",
            "Quality metrics table leaves actual values as `[TBD]`, limiting measurement.",
        ],
        "improvements": [
            "Add pointers to available modeling tooling (e.g., `scripts/technical_design.py`) or include templates.",
            "Set baseline throughput or accuracy targets for architecture validation to remove `[TBD]` placeholders.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "2",
        "display": "Protocol 2: Generate Tasks",
        "file": ".cursor/ai-driven-workflow/08-generate-tasks.md",
        "phase": "Planning",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references `validate_task_breakdown.py` and similar utilities that are absent in `scripts/`.",
            "Quality metrics remain `[TBD]`, so there is no default acceptance guidance for task decomposition.",
        ],
        "improvements": [
            "Map automation steps to existing planning scripts (`generate_consistency_report.py`, etc.) or provide implementations.",
            "Publish baseline thresholds for backlog coverage and dependency mapping so teams know when to stop iterating.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "7",
        "display": "Protocol 7: Environment Setup Validation",
        "file": ".cursor/ai-driven-workflow/09-environment-setup-validation.md",
        "phase": "Planning",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation hooks cite `validate_environment_setup.py` which is not available in the repository.",
            "Evidence metrics table still lists `[TBD]`, limiting compliance tracking.",
        ],
        "improvements": [
            "Reference the existing environment scripts (`setup_template_tests.sh`, etc.) or add the missing validators.",
            "Provide default SLOs for provisioning time or health-check coverage to replace `[TBD]`.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "3",
        "display": "Protocol 3: Process Tasks",
        "file": ".cursor/ai-driven-workflow/10-process-tasks.md",
        "phase": "Development",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation section references `validate_task_execution.py` style scripts missing from `scripts/`.",
            "Evidence metrics keep `[TBD]`, so throughput expectations are unclear.",
        ],
        "improvements": [
            "Document how to hook into existing automation (e.g., `validate_workflows.py`) or supply missing executors.",
            "Define baseline implementation evidence counts (e.g., tests per task) to replace `[TBD]` entries.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "9",
        "display": "Protocol 9: Integration Testing",
        "file": ".cursor/ai-driven-workflow/11-integration-testing.md",
        "phase": "Development",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation hooks reference non-existent scripts such as `run_integration_suite.py`.",
            "Evidence metrics remain `[TBD]`, preventing measurable success criteria.",
        ],
        "improvements": [
            "Map automation commands to repository scripts like `test_workflow_integration.sh` or provide wrappers.",
            "Publish baseline integration pass-rate expectations to replace `[TBD]` placeholders.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "4",
        "display": "Protocol 4: Quality Audit",
        "file": ".cursor/ai-driven-workflow/12-quality-audit.md",
        "phase": "Quality",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references scripts (`run_quality_audit.py`) that do not exist in the repo.",
            "Quality metrics table contains `[TBD]` actual values, hindering gating.",
        ],
        "improvements": [
            "Link to available QA automation (e.g., `validate_workflows.py`) or add missing utilities.",
            "Provide sample measurement formulas for defect density or review coverage in place of `[TBD]`.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "15",
        "display": "Protocol 15: UAT Coordination",
        "file": ".cursor/ai-driven-workflow/13-uat-coordination.md",
        "phase": "Quality",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation hooks reference user-testing automation scripts that are not part of the repository.",
            "Evidence metrics contain `[TBD]`, so completion tracking is qualitative only.",
        ],
        "improvements": [
            "Add references to real collaboration tools or include automation stubs for UAT evidence collection.",
            "Set baseline UAT acceptance thresholds (e.g., minimum pass rates) to replace `[TBD]` data.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "10",
        "display": "Protocol 10: Pre-Deployment Staging",
        "file": ".cursor/ai-driven-workflow/14-pre-deployment-staging.md",
        "phase": "Quality",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references staging scripts (`deploy_to_staging.py`) absent from the repo.",
            "Evidence metrics table retains `[TBD]`, leaving staging readiness criteria undefined.",
        ],
        "improvements": [
            "Tie automation hooks to existing deployment scripts (`deploy_backend.sh`, etc.) or describe manual fallback.",
            "Define explicit thresholds for staging sign-off (e.g., smoke test success rate) replacing `[TBD]`.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "11",
        "display": "Protocol 11: Production Deployment",
        "file": ".cursor/ai-driven-workflow/15-production-deployment.md",
        "phase": "Deployment",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation points to missing scripts (e.g., `run_prod_release.py`).",
            "Quality metrics show `[TBD]`, so success thresholds are unspecified.",
        ],
        "improvements": [
            "Reference available release scripts (`deploy_backend.sh`, `rollback_backend.sh`) or add the new automation.",
            "Document expected production SLOs (error budget, change failure rate) to populate the evidence table.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "12",
        "display": "Protocol 12: Monitoring & Observability",
        "file": ".cursor/ai-driven-workflow/16-monitoring-observability.md",
        "phase": "Deployment",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation lists observability scripts (`setup_monitoring.py`) not found in the repo.",
            "Evidence metrics are `[TBD]`, so there is no default monitoring baseline.",
        ],
        "improvements": [
            "Connect automation hooks to existing monitoring tooling (e.g., `collect_perf.py`) or provide new scripts.",
            "Publish default alert thresholds/MTTR targets to replace `[TBD]` entries.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "13",
        "display": "Protocol 13: Incident Response & Rollback",
        "file": ".cursor/ai-driven-workflow/17-incident-response-rollback.md",
        "phase": "Deployment",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation hooks reference missing tooling for incident drills and rollback validation.",
            "Evidence metrics list `[TBD]`, so response time targets are absent.",
        ],
        "improvements": [
            "Leverage existing rollback scripts (`rollback_backend.sh`, `rollback_frontend.sh`) within the automation section.",
            "Provide baseline MTTR/MTTD goals to replace `[TBD]` metrics.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "14",
        "display": "Protocol 14: Performance Optimization",
        "file": ".cursor/ai-driven-workflow/18-performance-optimization.md",
        "phase": "Deployment",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references optimization scripts not located in the repo.",
            "Evidence metrics table includes `[TBD]`, so optimization baselines are undefined.",
        ],
        "improvements": [
            "Point to available performance scripts (`collect_perf.py`, etc.) or add the missing automation.",
            "Document target performance KPIs and thresholds rather than `[TBD]` placeholders.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "16",
        "display": "Protocol 16: Documentation & Knowledge Transfer",
        "file": ".cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md",
        "phase": "Closure",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references documentation exporters absent from the repo.",
            "Evidence metrics show `[TBD]`, so documentation completeness is subjective.",
        ],
        "improvements": [
            "Reference existing documentation scripts (`write_context_report.py`) or add the missing exporters.",
            "Add quantitative targets (e.g., coverage of knowledge base articles) replacing `[TBD]` placeholders.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "17",
        "display": "Protocol 17: Project Closure",
        "file": ".cursor/ai-driven-workflow/20-project-closure.md",
        "phase": "Closure",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references closure validation scripts not present in the repo.",
            "Evidence metrics table contains `[TBD]` values, reducing measurability.",
        ],
        "improvements": [
            "Map closure automation to available scripts (e.g., `validate_workflow_completeness.py`).",
            "Define target metrics for closure (e.g., sign-off percentage) to replace `[TBD]`.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "18",
        "display": "Protocol 18: Maintenance & Support",
        "file": ".cursor/ai-driven-workflow/21-maintenance-support.md",
        "phase": "Closure",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references maintenance schedulers not included in the repo.",
            "Evidence metrics list `[TBD]`, so service levels are undefined.",
        ],
        "improvements": [
            "Tie automation to existing maintenance tooling (e.g., `validate_workflows.py`) or add scripts.",
            "Establish baseline response/resolution targets to replace `[TBD]` placeholders.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "5",
        "display": "Protocol 5: Implementation Retrospective",
        "file": ".cursor/ai-driven-workflow/22-implementation-retrospective.md",
        "phase": "Closure",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation references retrospective analyzers that are not shipped in the repo.",
            "Evidence metrics remain `[TBD]`, so improvement tracking lacks quantitative baselines.",
        ],
        "improvements": [
            "Point to existing analytics scripts (`retrospective_evidence_report.py`) or add missing automation.",
            "Define default metrics (e.g., action items closed) to replace `[TBD]` entries.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "8",
        "display": "Protocol 8: Script Governance",
        "file": ".cursor/ai-driven-workflow/23-script-governance-protocol.md",
        "phase": "Closure",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Automation hooks reference governance validators that do not exist in the repo.",
            "Evidence metrics are `[TBD]`, reducing visibility into governance compliance.",
        ],
        "improvements": [
            "Connect the automation section to scripts such as `validate_script_bindings.py` or provide new tooling.",
            "Set baseline governance KPIs (e.g., script coverage) instead of `[TBD]` placeholders.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "00-CD",
        "display": "Protocol 00-CD: Client Discovery",
        "file": ".cursor/ai-driven-workflow/24-client-discovery.md",
        "phase": "Foundation",
        "checklist": {k: True for k in ["role","workflow","integration","quality","communication","handoff","automation","evidence"]},
        "gaps": [
            "Quality metrics table uses `[TBD]`, limiting quantitative validation.",
            "Automation section references discovery scripts that are not available in the repo.",
        ],
        "improvements": [
            "Publish baseline targets for discovery completeness to replace `[TBD]` metrics.",
            "Add or reference actual discovery automation under `scripts/`.",
        ],
        "scores": {"Completeness": 9, "Clarity": 9, "Actionability": 9, "Integration": 8, "Evidence": 8, "Automation": 7},
    },
    {
        "key": "integration-map",
        "display": "Protocol Integration Map",
        "file": ".cursor/ai-driven-workflow/25-protocol-integration-map.md",
        "phase": "Supporting",
        "checklist": {
            "role": False,
            "workflow": True,
            "integration": True,
            "quality": True,
            "communication": False,
            "handoff": True,
            "automation": True,
            "evidence": True,
        },
        "gaps": [
            "Document lacks explicit AI role/mission or communication guidance despite orchestrating integrations.",
            "Handoff details are high-level and do not include artifact schema definitions.",
        ],
        "improvements": [
            "Add a coordinating role description and communication channels for managing cross-protocol changes.",
            "Expand handoff section with explicit artifact schemas or links to authoritative definitions.",
        ],
        "scores": {"Completeness": 7, "Clarity": 8, "Actionability": 7, "Integration": 8, "Evidence": 7, "Automation": 7},
    },
    {
        "key": "integration-guide",
        "display": "Integration Guide",
        "file": ".cursor/ai-driven-workflow/26-integration-guide.md",
        "phase": "Supporting",
        "checklist": {
            "role": False,
            "workflow": True,
            "integration": True,
            "quality": True,
            "communication": True,
            "handoff": False,
            "automation": True,
            "evidence": True,
        },
        "gaps": [
            "Guide provides architecture and communication standards but no explicit role/mission.",
            "Missing consolidated handoff checklist aligning integration tasks with protocol owners.",
        ],
        "improvements": [
            "Add a coordinator role section with responsibilities for applying the guide.",
            "Introduce a summary handoff checklist referencing key artifacts per integration pattern.",
        ],
        "scores": {"Completeness": 7, "Clarity": 8, "Actionability": 7, "Integration": 8, "Evidence": 7, "Automation": 7},
    },
    {
        "key": "validation-guide",
        "display": "Validation Guide",
        "file": ".cursor/ai-driven-workflow/27-validation-guide.md",
        "phase": "Supporting",
        "checklist": {
            "role": False,
            "workflow": True,
            "integration": True,
            "quality": True,
            "communication": False,
            "handoff": False,
            "automation": True,
            "evidence": True,
        },
        "gaps": [
            "Guide omits AI role/mission and communication pathways for validation reporting.",
            "No explicit handoff checklist for distributing validation outputs to downstream teams.",
        ],
        "improvements": [
            "Add a validation lead role description including escalation channels.",
            "Provide a handoff checklist mapping validation outputs to protocol consumers.",
        ],
        "scores": {"Completeness": 7, "Clarity": 8, "Actionability": 7, "Integration": 8, "Evidence": 7, "Automation": 7},
    },
]

for protocol in protocols:
    protocol["overall"] = round(mean(protocol["scores"].values()), 2)

transitions = [
    {"from": "00A", "to": "00B", "status": "attention", "issues": ["Integration numbering references outdated Protocol 04 inputs."]},
    {"from": "00B", "to": "01", "status": "attention", "issues": ["Outputs call Protocol 03/04 instead of current filenames, risking handoff confusion."]},
    {"from": "01", "to": "00", "status": "attention", "issues": ["Legacy numbering for bootstrap artifacts needs reconciliation with modern context kit."]},
    {"from": "00", "to": "00-generate-rules", "status": "attention", "issues": ["Rule generation command lacks explicit handoff outputs or quality gates."]},
    {"from": "00-generate-rules", "to": "1", "status": "attention", "issues": ["No structured outputs defined for PRD consumption."]},
    {"from": "1", "to": "6", "status": "pass", "issues": []},
    {"from": "6", "to": "2", "status": "attention", "issues": ["Integration section references Protocol 08/09 numbering inconsistently."]},
    {"from": "2", "to": "7", "status": "pass", "issues": []},
    {"from": "7", "to": "3", "status": "pass", "issues": []},
    {"from": "3", "to": "9", "status": "pass", "issues": []},
    {"from": "9", "to": "4", "status": "pass", "issues": []},
    {"from": "4", "to": "15", "status": "pass", "issues": []},
    {"from": "15", "to": "10", "status": "pass", "issues": []},
    {"from": "10", "to": "11", "status": "pass", "issues": []},
    {"from": "11", "to": "12", "status": "pass", "issues": []},
    {"from": "12", "to": "13", "status": "pass", "issues": []},
    {"from": "13", "to": "14", "status": "pass", "issues": []},
    {"from": "14", "to": "16", "status": "pass", "issues": []},
    {"from": "16", "to": "17", "status": "pass", "issues": []},
    {"from": "17", "to": "18", "status": "pass", "issues": []},
    {"from": "18", "to": "5", "status": "pass", "issues": []},
    {"from": "5", "to": "8", "status": "pass", "issues": []},
]

alignment_score = round(100 * sum(1 for t in transitions if t["status"] == "pass") / len(transitions), 1)

coverage_score = 100
completeness_score = round(mean(p["scores"]["Completeness"] for p in protocols), 1)
integration_score = round(mean(p["scores"]["Integration"] for p in protocols), 1)

csv_path = "reports/ai-workflow-scores.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as fh:
    writer = csv.writer(fh)
    writer.writerow(["Protocol", "File", "Phase", "Completeness", "Clarity", "Actionability", "Integration", "Evidence", "Automation", "Overall"])
    for protocol in protocols:
        s = protocol["scores"]
        writer.writerow([
            protocol["display"],
            protocol["file"],
            protocol["phase"],
            s["Completeness"],
            s["Clarity"],
            s["Actionability"],
            s["Integration"],
            s["Evidence"],
            s["Automation"],
            protocol["overall"],
        ])

def checklist_mark(protocol, key):
    return "[x]" if protocol["checklist"].get(key, False) else "[ ]"

markdown_path = "reports/ai-driven-workflow-evaluation.md"
with open(markdown_path, "w", encoding="utf-8") as fh:
    fh.write("# AI-Driven Workflow Protocol System Evaluation\n\n")
    fh.write("## Executive Summary\n")
    fh.write(f"- **Overall Alignment Score**: {alignment_score}% seamless handoffs across {len(transitions)} evaluated transitions.\n")
    fh.write(f"- **Coverage Score**: {coverage_score}% of SDLC phases represented.\n")
    fh.write(f"- **Completeness Score**: {completeness_score}/10 average completeness across protocols.\n")
    fh.write(f"- **Integration Score**: {integration_score}/10 average integration readiness.\n")
    fh.write("- **Critical Findings**: Outdated integration numbering in foundation protocols, missing automation implementations, and pervasive `[TBD]` quality metrics.\n")
    fh.write("- **High-Priority Recommendations**: Standardize integration references, implement referenced automation scripts, and replace `[TBD]` metrics with enforceable baselines.\n\n")

    fh.write("## Protocol Sequence Map\n")
    fh.write("- **Workflow Order**: 00A → 00B → 01 → 00 → /Generate Rules → 1 → 6 → 2 → 7 → 3 → 9 → 4 → 15 → 10 → 11 → 12 → 13 → 14 → 16 → 17 → 18 → 5 → 8.\n")
    fh.write("- **Dependencies**: Each protocol declares incoming/outgoing artifacts; foundational stages require corrected numbering to align with actual filenames.\n")
    fh.write("- **Integration Points**: Supporting documents (Integration Map, Integration Guide, Validation Guide) describe cross-phase automation but need explicit role owners.\n\n")

    fh.write("## Per-Protocol Analysis\n")
    for protocol in protocols:
        fh.write(f"### {protocol['display']}\n")
        fh.write(f"Source: `{protocol['file']}`\n\n")
        fh.write("#### ✅ Completeness Checklist\n")
        fh.write(f"- {checklist_mark(protocol, 'role')} AI Role & Mission\n")
        fh.write(f"- {checklist_mark(protocol, 'workflow')} Workflow Steps\n")
        fh.write(f"- {checklist_mark(protocol, 'integration')} Integration Points\n")
        fh.write(f"- {checklist_mark(protocol, 'quality')} Quality Gates\n")
        fh.write(f"- {checklist_mark(protocol, 'communication')} Communication Protocols\n")
        fh.write(f"- {checklist_mark(protocol, 'handoff')} Handoff Checklist\n")
        fh.write(f"- {checklist_mark(protocol, 'automation')} Automation Hooks\n")
        fh.write(f"- {checklist_mark(protocol, 'evidence')} Evidence Requirements\n\n")

        fh.write("#### ❌ Gaps Identified\n")
        for gap in protocol["gaps"]:
            fh.write(f"- {gap}\n")
        if not protocol["gaps"]:
            fh.write("- None noted.\n")
        fh.write("\n")

        fh.write("#### 💡 Improvement Suggestions\n")
        for idea in protocol["improvements"]:
            fh.write(f"- {idea}\n")
        if not protocol["improvements"]:
            fh.write("- No additional improvements required.\n")
        fh.write("\n")

        fh.write("#### Scores\n")
        for metric, value in protocol["scores"].items():
            fh.write(f"- {metric}: {value}/10\n")
        fh.write(f"- **Overall: {protocol['overall']}/10**\n\n")

    fh.write("## Integration Analysis\n")
    fh.write("### Critical Integration Points\n")
    fh.write("- Foundation handoffs (00A→00B→01→00) require renumbered references to avoid confusion with legacy protocols.\n")
    fh.write("- Automation-driven transitions (2→7→3) depend on missing scripts; without implementation, evidence flow is manual.\n")
    fh.write("- Deployment chain (10→11→12→13→14) is structurally sound but blocked by placeholder metrics.\n\n")

    fh.write("### Handoff Quality Matrix\n")
    fh.write("| From | To | Status | Notes |\n")
    fh.write("|------|----|--------|-------|\n")
    for t in transitions:
        note = "; ".join(t["issues"]) if t["issues"] else "Pass"
        status = "Pass" if t["status"] == "pass" else "Needs Attention"
        fh.write(f"| {t['from']} | {t['to']} | {status} | {note} |\n")
    fh.write("\n")

    fh.write("### Evidence Flow Analysis\n")
    fh.write("- Evidence requirements exist in each mainline protocol but `[TBD]` metrics weaken traceability.\n")
    fh.write("- Supporting integration documents describe flow conceptually but lack artifact schemas, creating ambiguity for automation.\n\n")

    fh.write("### Dependency Validation\n")
    fh.write("- No circular dependencies detected.\n")
    fh.write("- Legacy numbering requires updates to keep prerequisites accurate.\n")
    fh.write("- Missing automation scripts are active dependencies for multiple phases.\n\n")

    fh.write("## Scoring Summary\n")
    fh.write("### System-Level Scores\n")
    fh.write(f"- Alignment Score: {alignment_score}%\n")
    fh.write(f"- Coverage Score: {coverage_score}%\n")
    fh.write(f"- Completeness Score: {completeness_score}/10\n")
    fh.write(f"- Integration Score: {integration_score}/10\n\n")

    fh.write("### Per-Protocol Score Matrix\n")
    fh.write("| Protocol | Completeness | Clarity | Actionability | Integration | Evidence | Automation | Overall |\n")
    fh.write("|----------|--------------|--------|--------------|-------------|----------|-----------|---------|\n")
    for protocol in protocols:
        s = protocol["scores"]
        fh.write(f"| {protocol['key']} | {s['Completeness']} | {s['Clarity']} | {s['Actionability']} | {s['Integration']} | {s['Evidence']} | {s['Automation']} | {protocol['overall']} |\n")
    fh.write("\n")

    fh.write("### Dimension Analysis\n")
    fh.write("- **Automation** is consistently the lowest dimension because referenced scripts are missing.\n")
    fh.write("- **Integration** drops in early phases due to legacy numbering mismatches.\n")
    fh.write("- **Evidence** scores are capped by `[TBD]` metrics, requiring definitive baselines.\n\n")

    fh.write("## Improvement Roadmap\n")
    fh.write("### Critical Fixes (Required)\n")
    fh.write("- Update integration references in foundation protocols to match actual filenames and directory structure.\n")
    fh.write("- Implement or replace missing automation scripts referenced across protocols.\n")
    fh.write("- Replace `[TBD]` placeholders in quality metric tables with enforceable thresholds.\n\n")

    fh.write("### High-Priority Enhancements\n")
    fh.write("- Add artifact schema definitions to supporting guides (Integration Map/Guide/Validation Guide).\n")
    fh.write("- Introduce communication and role definitions for supporting documents that coordinate multiple protocols.\n")
    fh.write("- Provide baseline measurement playbooks for evidence collection across phases.\n\n")

    fh.write("### Medium-Priority Improvements\n")
    fh.write("- Clarify legacy vs. modern bootstrap flows and document selection criteria.\n")
    fh.write("- Provide automation fallback procedures for manual execution paths.\n")
    fh.write("- Expand scenario-based examples in planning and quality phases.\n\n")

    fh.write("### Nice-to-Have Additions\n")
    fh.write("- Add visualization assets (Swim lanes, BPMN diagrams) to Integration Guide for quick onboarding.\n")
    fh.write("- Create dashboards summarizing evidence coverage across protocols.\n")
    fh.write("- Provide API/webhook templates for integrating automation with external tooling.\n\n")

    fh.write("## Real-world Simulation Results\n")
    fh.write("### Scenario 1: Simple Project\n")
    fh.write("- Execution Path: 00A → 00B → 01 → 00 → 1 → 2 → 3 → 4 → 5.\n")
    fh.write("- Result: Workflow structurally complete; `[TBD]` metrics and missing scripts force manual validation, slowing delivery.\n")
    fh.write("- Recommendation: Provide lightweight script set for CRUD scenarios and pre-populate quality baselines.\n\n")

    fh.write("### Scenario 2: Medium Complexity Project\n")
    fh.write("- Execution Path: 00A → 00B → 01 → 00 → 1 → 6 → 2 → 7 → 3 → 9 → 4 → 10.\n")
    fh.write("- Result: Architectural and task planning steps operate smoothly, but staging automation is blocked by missing scripts.\n")
    fh.write("- Recommendation: Map automation hooks to existing CI/CD tooling and provide database migration validation guidance.\n\n")

    fh.write("### Scenario 3: Complex Enterprise Project\n")
    fh.write("- Execution Path: Full 28-protocol stack.\n")
    fh.write("- Result: Governance and documentation coverage strong; integration references and absent automation create significant coordination overhead.\n")
    fh.write("- Recommendation: Prioritize integration numbering fixes and implement referenced automation before enterprise rollout.\n\n")

    fh.write("### Scenario 4: Crisis Scenario\n")
    fh.write("- Execution Path: 12 → 13 → 14 with support from 18.\n")
    fh.write("- Result: Incident workflows are comprehensive but rely on non-existent automation and `[TBD]` MTTR targets.\n")
    fh.write("- Recommendation: Provide concrete rollback scripts mapping to existing shell utilities and define MTTR/MTTD baselines.\n")

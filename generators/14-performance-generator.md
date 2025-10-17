# Generator: Protocol 14 – Performance Optimization & Tuning

## 1. Purpose
Enable AI agents to convert `protocol-input-form-14-performance.yaml` into `14-performance-optimization.md`, delivering a repeatable process for diagnosing performance issues, executing optimizations, and communicating SLO updates.

## 2. Required Inputs
- Completed `protocol-input-form-14-performance.yaml`
- Telemetry artifacts: Protocol 12 monitoring dashboards/logs, Protocol 13 incident reviews, Protocol 11 deployment reports
- Tooling access: Profilers, tracing tools, load testing frameworks (e.g., k6, Locust), performance regression suites
- Automation scripts: `scripts/analyze_metrics.py`, `scripts/profile_service.py`, `k6` scenarios, `pytest -m performance`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Performance Engineer safeguarding SLO/SLA commitments
- Guardrail: No deployment of performance changes without reproducible benchmarks and updated instrumentation
- Dependencies: Inputs from Protocols 12, 13, 11; outputs to Protocols 5, 12, 3

### Layer 2 – Behavioral Control
- Gates: Baseline validation, diagnostic coverage, optimization validation, governance & communication
- Halt conditions: Telemetry gaps, failed load tests, regressions, missing approvals
- Prompts: Baseline check confirmation, release/SLO update approval

### Layer 3 – Procedural Logic
- Phases: Intake & baseline → Diagnostics & load simulation → Optimization implementation → Governance & handoff
- Evidence: Intake report, baseline metrics, profiling report, load test results, optimization plan, validation report, instrumentation log, SLO update record
- Automation: Metric analysis script, profiling command, load test execution, performance regression suite

### Layer 4 – Communication Grammar
- Phase announcements referencing telemetry, profiling, optimization, SLO documentation
- Automation status lines for analyze_metrics, profile_service, k6, and regression suite
- Error messages for telemetry gaps, load test failures, regressions

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading `# PROTOCOL 14: ... (PERFORMANCE COMPLIANT)`
2. Section **1. AI ROLE AND MISSION** with guardrail text from form
3. Section **2. PERFORMANCE OPTIMIZATION WORKFLOW** comprising four steps with `[MUST]/[GUIDELINE]` actions, evidence, automation references
4. Section **3. INTEGRATION POINTS** listing inputs (Protocols 12,13,11) and outputs (Protocols 5,12,3)
5. Section **4. QUALITY GATES** detailing Baseline Validation, Diagnostic Coverage, Optimization Validation, Governance & Communication
6. Section **5. COMMUNICATION PROTOCOLS** including status announcements, validation prompts, and error handling definitions
7. Section **6. AUTOMATION HOOKS** enumerating metric analysis, profiling, load testing, and regression scripts
8. Section **7. HANDOFF CHECKLIST** matching checklist items from form

## 5. Automation Hook Rules
- Reference time windows or service flags where applicable (e.g., `--window 7d`, `--service {name}`)
- Default evidence storage to `.artifacts/performance/`
- Mention optional continuous improvement tooling if provided in form

## 6. Quality Acceptance Criteria
- All `[MUST]` steps cite concrete evidence artifacts
- Quality gates reference exact filenames and remediation paths
- Communication prompts preserve `[BASELINE CHECK]` and `[RELEASE REQUEST]` tokens
- Integration outputs include `PERFORMANCE-REPORT.md`, `continuous-improvement-notes.md`, `instrumentation-update-log.md`
- Guardrail statement matches form language on benchmarks and instrumentation

## 7. Generation Workflow for the AI
1. Validate form completeness and prerequisite references (Protocols 12,13,11)
2. Map each phase to Markdown `STEP` sections with ordered actions and evidence locations
3. Populate integration and quality gate sections using structured form data
4. Insert communication templates and error handling verbatim from the form
5. Ensure automation hooks list all scripts/tools provided, including k6 and pytest performance suite
6. Output markdown to `.cursor/ai-driven-workflow/14-performance-optimization.md`

## 8. Output & Post-Generation Actions
- Recommend running meta-analysis validation for circular compliance
- Suggest scheduling follow-up review with Protocol 12 team to confirm instrumentation updates
- Encourage feeding optimization outcomes into Protocol 5 retrospectives for continuous improvement

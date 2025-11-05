MCP Tool Recommendations by Protocol
Overview

This document analyzes each protocol in the SuperTemplate AI‑driven workflow (23 files) and recommends Model Context Protocol (MCP) tools that should be integrated to maximize automation, intelligence and reliability. Recommendations are grounded in the protocol requirements and real capabilities of MCP servers available in 2025. Evidence from the protocols is cited using the line‑numbered references provided.

Key MCP Tools Considered

The following MCP servers were evaluated based on the 2025 MCP ecosystem (Medium and Microsoft overviews and the awesome‑mcp‑servers repository). Only production‑ready tools were considered:

GitHub MCP server – Automates GitHub repository operations (issues, PRs, branches, code search). Useful for project scaffolding, repository mapping and code review. GitHub repository link
.

GitMCP server – Provides high‑recall code search and context retrieval to reduce hallucination when reasoning about source files. GitMCP tool
.

Playwright MCP server – Allows a model to drive a headless browser for integration tests, UI validation and UAT simulations. Microsoft Playwright MCP
.

Filesystem MCP server – Offers secure file‑system operations (reading/writing files, directory listing, search). Ideal for environment setup, artifact packaging and script governance. Filesystem MCP
.

Memory MCP server – Provides a persistent knowledge graph and retrieval API to store context across protocols (e.g., decisions, risk logs, documentation). Memory MCP
.

Fetch MCP server – Retrieves and summarises web content; useful for competitor analysis or documentation lookups. Fetch MCP server
.

Grafana MCP server – Interfaces with Grafana, Prometheus and Loki to query dashboards, run metrics queries and manage OnCall schedules. Useful for observability and incident response
github.com
.

Sentry MCP server – Integrates with Sentry to fetch error reports, incidents and release health. Supports incident classification and root‑cause analysis (protocol 17).

Buildkite MCP server – Triggers and monitors CI/CD pipelines; fetches build logs. Ideal for quality audits and pre‑deployment checks.

SonarQube MCP server – Exposes code quality metrics and static analysis results. Supports protocol 12 audits and script governance.

Code Runner MCP server – Spins up sandboxed Docker containers to run code and scripts (e.g., Python/Java). Useful for executing automation hooks in early protocols.

Protocol‑Specific Recommendations
Protocol 01 – Client Proposal Generation

Context: The protocol converts a client job posting into a detailed proposal by analyzing the post, mapping tone, estimating pricing, and drafting a human‑like proposal. It includes running scripts (analyze_jobpost.py, tone_mapper.py) and verifying that pricing and voice align with the job post
github.com
.

Recommended tools:

Protocol task	Recommended MCP tool	Rationale
Extract job post text, analyze tone and persona	GitMCP	Use code search capabilities to retrieve existing writing samples or templates from company repos to inform tone mapping. Helps reduce hallucination by grounding in real examples.
Execute automation hooks (e.g., analyze_jobpost.py)	Code Runner MCP	Runs Python scripts in a sandbox to extract keywords and generate pricing estimates. Avoids manual environment setup and ensures reproducibility.
Store discovered job features and persona mappings for reuse	Memory MCP	Persists knowledge such as tone maps and pricing heuristics. Reusable across future proposal generations.
Save generated proposal drafts and logs	Filesystem MCP	Writes drafts, logs and artifacts to the repository while respecting file permissions.
Protocol 02 – Client Discovery Initiation

Context: The protocol translates the proposal into a discovery brief by summarising the job post and proposal, compiling assumptions, building question banks and integration inventories, scheduling discovery calls, and capturing notes
github.com
.

Recommended tools:

Task	MCP tool	Justification
Summarise job post and proposal into a brief	Fetch MCP / Memory MCP	Fetch MCP can scrape relevant competitor or domain information to enrich the brief. Memory MCP stores summaries and assumptions for subsequent phases.
Build integration inventory (list systems, APIs)	GitMCP & GitHub MCP	GitMCP can search internal repos for prior integration adapters; GitHub MCP can create issues or tasks in the project repo for each integration discovered.
Generate question bank and scenario guides	Memory MCP	Stores and retrieves common discovery questions categorized by domain to accelerate preparation.
Schedule call and send agenda	Grafana MCP OnCall if call management integrated	Integrate OnCall scheduling to coordinate times and send notifications (optional).
Protocol 03 – Project Brief Creation

Context: This protocol assembles a comprehensive project brief from discovery outputs, including executive summary, objectives, technical architecture, assumptions, risk register, and traceability map. It requires validating completeness with scripts (validate_brief.py) and capturing approvals
github.com
github.com
.

Recommendations:

Task	MCP tool	Reason
Generate traceability maps and indexes	Memory MCP	Persist the mapping between discovery artifacts, requirements and stakeholders. Supports retrieval in later protocols (e.g., PRD and design).
Validate brief structure and completeness	Code Runner MCP	Execute validate_brief.py and related scripts to automate structural checks.
Store risk register, objectives, and architecture diagrams	Filesystem MCP	Save generated documents and diagrams in a secure file system location.
Track approval workflow	GitHub MCP	Create GitHub issues or pull requests representing approval tasks; assign stakeholders and capture decisions.
Protocol 04 – Project Bootstrap & Context Engineering

Context: Bootstraps the project environment: validates assets, generates scaffolds, runs environment doctor checks, normalizes governance rules, produces context kits, and sets up evidence tracking
github.com
github.com
.

Recommendations:

Task	MCP tool	Rationale
Validate brief and generate scaffold	Code Runner MCP & GitHub MCP	Code Runner executes generate_from_brief.py to build scaffolds; GitHub MCP commits generated code and branches for the project bootstrap.
Run environment doctor and verify toolchain readiness
github.com
	Filesystem MCP	Check file locations and verify versions of installed dependencies; update environment if necessary.
Normalize and register governance rules	Memory MCP	Persists normalized rules for quick reference during task generation and execution. Helps maintain alignment with project standards.
Produce context kit and evidence tracking	GitMCP & Memory MCP	GitMCP retrieves relevant context docs and templates; Memory MCP stores and indexes the evidence for retrieval in later phases.
Protocol 05 – Bootstrap Your Project

Context: Aligns the codebase with governance rules by migrating rule files, mapping repository structure, capturing stack signals and architecture principles, and generating final documentation
github.com
github.com
.

Recommendations:

Task	MCP tool	Rationale
Migrate rule files and map repository structure
github.com
	Filesystem MCP & GitHub MCP	Filesystem MCP performs safe file operations across many directories; GitHub MCP commits updated rules and ensures branch protection.
Capture stack signals by analyzing code
github.com
	GitMCP & SonarQube MCP	GitMCP indexes the codebase and surfaces language/framework usage; SonarQube MCP provides code metrics (complexity, duplication) to identify architecture patterns.
Generate final documentation and rule updates	Memory MCP	Stores final governance and architecture rules for later protocols.
Protocol 06 – Implementation‑Ready PRD Creation

Context: Converts discovery outputs into a product requirements document (PRD) by aligning context, elaborating functional/technical requirements, drafting risk and validation plans, assembling the PRD, generating assets with generate_prd_assets.py, and validating with validate_prd_gate.py
github.com
.

Recommendations:

Task	MCP tool	Justification
Run generate_prd_assets.py and validate_prd_gate.py
github.com
	Code Runner MCP	Automates asset generation and validation in a sandboxed environment, ensuring reproducibility.
Persist traceability and risk logs	Memory MCP	Captures relationships between user stories, requirements, risks, and acceptance criteria; ensures retrieval for design and testing.
Publish PRD drafts and attachments	GitHub MCP & Filesystem MCP	GitHub MCP opens a PR containing the PRD and attachments; Filesystem MCP ensures local file operations.
Retrieve domain knowledge (e.g., competitor requirements)	Fetch MCP	Fetches external domain documents or standards to enrich requirement details.
Protocol 07 – Technical Design & Architecture

Context: Translates PRD into a technical design by validating inputs, decomposing architecture, generating ADRs, building interaction diagrams, assembling specifications, and drafting implementation roadmaps
github.com
.

Recommendations:

Task	MCP tool	Rationale
Identify system boundaries & propose decomposition
github.com
	GitMCP & SonarQube MCP	GitMCP searches similar architectures in existing repos; SonarQube MCP reveals code coupling and dependencies to inform service boundaries.
Generate architecture diagrams	Playwright MCP	Automates browser‑based diagram tools (e.g., diagrams.net) to create and export interaction diagrams.
Capture architectural decisions (ADRs)	Memory MCP	Persists ADRs for traceability and retrieval in later modifications.
Validate design integration scripts (e.g., validate_workflow_integration.py)	Code Runner MCP	Executes validation to ensure design complies with governance rules.
Publish design specification	GitHub MCP	Creates PR for stakeholder review.
Protocol 08 – Technical Task Generation

Context: Decomposes the technical design into tasks across layers (frontend, backend, data, testing, integration). Requires indexing governance rules, analyzing inputs, generating tasks, assigning automation hooks, and running validation scripts
github.com
github.com
github.com
github.com
.

Recommendations:

Task	MCP tool	Justification
Index governance rules
github.com
	Memory MCP	Stores and indexes rules to ensure every generated task references the correct policy.
Generate high‑level tasks with context
github.com
	GitMCP	Retrieves examples of tasks and acceptance criteria from previous projects to inform decomposition.
Map tasks to personas and layers
github.com
	Memory MCP	Maintains a persona catalog and mapping of tasks to persona capabilities.
Execute validation scripts validate_tasks.py, enrich_tasks.py
github.com
	Code Runner MCP	Runs these scripts; outputs results to the repository via GitHub MCP.
Commit tasks and update repository	GitHub MCP	Automates creation of task files and PRs.
Protocol 09 – Environment Setup & Validation

Context: Prepares the development environment by extracting requirements, validating credentials, running environment doctor and provisioning dependencies, applying configuration templates, running a validation suite, creating an environment handbook, and packaging onboarding materials
github.com
github.com
.

Recommendations:

Task	MCP tool	Rationale
Validate environment prerequisites and run diagnostics
github.com
	Filesystem MCP & Code Runner MCP	Use Filesystem MCP to verify installation paths and environment variables; Code Runner executes doctor.py and install_and_test.sh within an isolated container.
Provision dependencies (e.g., via package managers)	Buildkite MCP	Trigger pipeline jobs that build base environments or containers; fetch logs to verify installation success.
Apply configuration templates and run validation suite
github.com
	GitHub MCP & Code Runner MCP	GitHub MCP fetches configuration templates from the repo; Code Runner applies them and runs integration tests.
Create environment handbook and onboarding package	Filesystem MCP & Memory MCP	Filesystem MCP writes handbook files; Memory MCP indexes them for search across protocols.
Protocol 10 – Controlled Task Execution

Context: Executes tasks under strict governance. Steps include selecting a parent task, confirming model and environment readiness, executing subtasks with evidence capture, performing quick validations, and running final quality audits and updates
github.com
github.com
github.com
.

Recommendations:

Task	MCP tool	Reason
Check recommended model & environment readiness
github.com
	Filesystem MCP	Ensures the correct models, packages and environment variables are present before starting execution.
Load rules and documentation for each subtask
github.com
	Memory MCP	Retrieves relevant rules, ADRs and context; ensures that the agent references the latest guidelines.
Capture evidence and commit changes	GitHub MCP & Filesystem MCP	GitHub MCP commits code changes; Filesystem MCP stores evidence artifacts (logs, transcripts, screenshots).
Run quick validation (e.g., python -m pytest -q)	Code Runner MCP	Runs test suites to verify subtask results.
Perform quality audit via /review and update task state
github.com
	SonarQube MCP & Buildkite MCP	SonarQube MCP provides static analysis results for quality audits; Buildkite MCP triggers pipeline for additional checks.
Protocol 11 – Integration Testing & System Validation

Context: Defines integration testing after tasks execution. Steps include defining scope and validating environment parity, refreshing test data, assembling the test plan, running contract tests (run_contract_tests.py), verifying observability, executing tests, managing defects, packaging evidence, and sign‑off
github.com
github.com
.

Recommendations:

Task	MCP tool	Rationale
Validate environment parity (staging vs test environment)
github.com
	Filesystem MCP & Grafana MCP	Filesystem MCP compares configuration files; Grafana MCP queries metrics to ensure environments have similar performance baselines.
Run contract and integration tests
github.com
	Code Runner MCP & Playwright MCP	Code Runner executes backend contract tests; Playwright MCP performs end‑to‑end tests across the UI.
Refresh test data and manage fixtures	Memory MCP	Stores test data sets and fetches them for each run.
Log defects and track resolution	GitHub MCP & Sentry MCP	GitHub MCP creates issues for defects; Sentry MCP retrieves error traces to aid debugging.
Package evidence and gather sign‑off	Filesystem MCP	Aggregates test reports and logs into a ZIP for approval.
Protocol 12 – Quality Audit Orchestrator

Context: Coordinates quality audits by running CI workflows, aggregating coverage metrics, deciding review mode via a router, executing specialized review protocols, consolidating findings, and producing an audit report with a readiness recommendation
github.com
github.com
.

Recommendations:

Task	MCP tool	Justification
Run CI workflows and aggregate coverage
github.com
	Buildkite MCP & SonarQube MCP	Buildkite MCP triggers pipeline runs and collects build artifacts; SonarQube MCP fetches coverage and static analysis metrics for audit.
Route to specialized review protocols	Memory MCP	Stores routing rules and decision logic. When the router determines the review type, Memory MCP supplies the context needed to call the correct specialized audit procedure.
Consolidate findings into audit-findings.json
github.com
	Filesystem MCP & GitHub MCP	Filesystem MCP writes the unified audit package; GitHub MCP attaches it to an issue or pull request for sign‑off.
Protocol 13 – UAT Coordination

Context: Manages user acceptance testing by validating entry conditions, assembling participant roster, guiding execution, managing defects, verifying fixes, capturing sign‑offs, and packaging UAT evidence
github.com
github.com
.

Recommendations:

Task	MCP tool	Rationale
Validate entry criteria across protocols
github.com
	Filesystem MCP & SonarQube MCP	Filesystem MCP verifies artifacts (e.g., UAT entry checklist); SonarQube MCP ensures code quality metrics meet threshold.
Assemble participant roster and toolkit	Memory MCP & GitHub MCP	Memory MCP stores participant records and UAT instructions; GitHub MCP creates tasks or issues assigned to participants.
Monitor execution and capture insights	Playwright MCP & Sentry MCP	Playwright MCP simulates user flows for monitoring; Sentry MCP collects runtime errors or user‑reported issues.
Manage defect log and retest verification
github.com
	GitHub MCP & Buildkite MCP	GitHub MCP manages issues; Buildkite MCP triggers retest pipelines when fixes are ready.
Package UAT closure evidence	Filesystem MCP	Aggregates uat-defect-register.csv, execution logs, and sign‑off forms.
Protocol 14 – Pre‑Deployment Validation & Staging Readiness

Context: Ensures the staging environment matches production, rehearses deployment, runs smoke and regression tests, captures observability baselines, validates rollback and compliance, and prepares the pre‑deployment package
github.com
github.com
.

Recommendations:

Task	MCP tool	Justification
Compare staging vs production configurations
github.com
	Filesystem MCP & Grafana MCP	Filesystem MCP compares configuration files; Grafana MCP queries dashboards to ensure baseline metrics align.
Rehearse deployment and smoke tests
github.com
	Buildkite MCP & Playwright MCP	Buildkite MCP triggers a rehearsal pipeline; Playwright MCP runs smoke tests of the UI.
Run regression tests and capture metrics	Code Runner MCP & SonarQube MCP	Code Runner executes test suites; SonarQube MCP provides code coverage and quality metrics.
Capture observability baselines	Grafana MCP	Query Prometheus/Loki to capture baseline metrics and log patterns.
Validate rollback procedures	Sentry MCP & Filesystem MCP	Sentry MCP monitors for errors during rollback; Filesystem MCP validates backup integrity.
Protocol 15 – Production Deployment & Release Management

Context: Governs the release process by validating pre‑deployment evidence, confirming release scope, scheduling deployment, reconfirming staging health, executing deployment, running immediate post‑deployment checks, monitoring health, and compiling release reports
github.com
.

Recommendations:

Task	MCP tool	Reason
Validate pre‑deployment evidence and readiness	Buildkite MCP & SonarQube MCP	Buildkite ensures all pipelines passed; SonarQube MCP confirms quality thresholds.
Schedule and execute deployment	Buildkite MCP	Executes production deployment pipeline, logs output, and notifies stakeholders via GitHub MCP.
Run immediate post‑deployment checks
github.com
	Playwright MCP & Grafana MCP	Playwright MCP runs smoke tests; Grafana MCP monitors metrics for anomalies.
Monitor stabilization window	Grafana MCP & Sentry MCP	Grafana monitors real‑time performance; Sentry collects error reports.
Compile release report and retrospective inputs	Filesystem MCP & Memory MCP	Filesystem MCP stores post‑deployment validation results; Memory MCP captures feedback and improvement points.
Protocol 16 – Post‑Deployment Monitoring & Observability

Context: Focuses on instrumentation coverage, baseline metric capture, configuring dashboards and alerts, testing alert paths, correlating incidents, scoring observability, and handing off monitoring package
github.com
github.com
.

Recommendations:

Task	MCP tool	Justification
Verify instrumentation coverage and baseline metrics
github.com
	Grafana MCP & Sentry MCP	Grafana MCP queries metrics and logs to confirm that all components emit telemetry; Sentry MCP verifies error instrumentation.
Capture baseline snapshot via collect_perf.py
github.com
	Code Runner MCP	Runs performance collection scripts; stores results via Filesystem MCP.
Configure dashboards and alerts	Grafana MCP	Creates dashboards, sets thresholds and notifies OnCall schedules.
Test alert paths and escalations	Grafana MCP & Sentry MCP	Grafana triggers synthetic alerts; Sentry ensures error notifications reach the correct channel.
Update runbooks and knowledge base	Memory MCP	Stores updated runbooks and cross‑links them with metrics and incident patterns.
Protocol 17 – Incident Response & Rollback

Context: Detects, classifies and resolves incidents by triaging severity, executing mitigation strategies or rollbacks, validating recovery, capturing root‑cause evidence, and producing incident reports
github.com
.

Recommendations:

Task	MCP tool	Reason
Detect and classify incidents (based on monitoring alerts)	Sentry MCP & Grafana MCP	Sentry MCP surfaces error alerts; Grafana MCP monitors metrics and logs; both feed severity classification.
Plan mitigation vs rollback options
github.com
	Memory MCP	Stores historical incidents and mitigation outcomes; helps weigh rollback vs hotfix decisions.
Validate rollback readiness	Filesystem MCP & Buildkite MCP	Filesystem MCP checks existence of snapshots/backups; Buildkite MCP runs rollback pipeline in staging.
Execute mitigation or rollback	Buildkite MCP	Automates deployment or rollback scripts; logs steps for evidence.
Capture root‑cause evidence and prepare incident report	Sentry MCP & GitHub MCP	Sentry provides stack traces and error contexts; GitHub MCP opens post‑mortem issues and attaches incident reports.
Protocol 18 – Performance Optimization & Tuning

Context: Performs performance engineering tasks: collecting telemetry, establishing baselines, profiling, running load/stress tests, analyzing capacity and cost, defining optimization plans, implementing changes, and producing performance reports
github.com
.

Recommendations:

Task	MCP tool	Rationale
Collect telemetry and establish baselines
github.com
	Grafana MCP & Sentry MCP	Grafana queries metrics and traces; Sentry collects performance errors.
Profile transactions and run load/stress tests	Code Runner MCP & Playwright MCP	Code Runner executes profiling scripts; Playwright MCP simulates user loads for frontend performance.
Analyze capacity and cost	Grafana MCP & Fetch MCP	Grafana metrics help quantify resource usage; Fetch MCP retrieves cloud pricing data for cost analysis.
Implement and validate optimizations	GitHub MCP & SonarQube MCP	GitHub MCP manages code changes; SonarQube MCP assesses code quality after optimization.
Record SLO adjustments and publish performance report	Memory MCP & Filesystem MCP	Memory MCP stores SLO history; Filesystem MCP writes the report and attaches metrics snapshots.
Protocol 19 – Documentation & Knowledge Transfer

Context: Organizes knowledge capture and documentation. Requires inventorying inputs, defining personas and deliverables, producing structured documentation drafts, capturing knowledge transfer sessions, performing reviews, publishing final packages, enabling sessions, and capturing feedback
github.com
github.com
.

Recommendations:

Task	MCP tool	Reason
Inventory inputs & define documentation personas
github.com
	Memory MCP	Maintains a knowledge graph of artifacts and stakeholders; ensures comprehensive coverage.
Produce documentation drafts and capture sessions
github.com
	Filesystem MCP & Playwright MCP	Filesystem MCP stores drafts and session recordings; Playwright MCP can automate capturing interactive training sessions (e.g., via browser automation).
Perform reviews and validate content	GitHub MCP & SonarQube MCP	GitHub MCP coordinates review threads and approvals; SonarQube MCP performs documentation linting or broken link detection.
Publish final packages and track knowledge transfer	Memory MCP	Stores published docs and provides retrieval across protocols; integrates feedback loops.
Protocol 20 – Project Closure & Handover

Context: Finalizes deliverables, ensures stakeholder acceptance, closes governance items, and transitions operational ownership. Steps include verifying closure prerequisites, auditing deliverables, reviewing financials, facilitating acceptance, transitioning operations, closing governance artifacts, preparing a handover package, and capturing closure metrics
github.com
github.com
.

Recommendations:

Task	MCP tool	Rationale
Verify closure prerequisites and audit deliverable register
github.com
	Filesystem MCP & SonarQube MCP	Filesystem MCP checks that all files are present; SonarQube MCP ensures final quality reports pass thresholds.
Review financial and contractual status	Fetch MCP	Retrieves current contract or finance documentation from external systems.
Facilitate acceptance reviews & sign‑offs
github.com
	GitHub MCP & Memory MCP	GitHub MCP manages approval issues; Memory MCP records decisions and acceptance rationale.
Transition operational ownership and close governance artifacts	Memory MCP	Transfers context kit, runbooks and rule indexes to the maintenance team.
Prepare handover package	Filesystem MCP	Bundles documentation, metrics and credentials for final delivery.
Protocol 21 – Continuous Maintenance & Support Planning

Context: Turns closure outputs into a maintenance program: validates handover completeness, assesses operational baselines, consolidates and prioritizes maintenance backlog, drafts maintenance plan, secures approvals, and configures governance cadence
github.com
github.com
.

Recommendations:

Task	MCP tool	Justification
Validate handover completeness and operational baselines	Grafana MCP & Filesystem MCP	Grafana MCP checks current performance baselines; Filesystem MCP verifies that documentation and runbooks are present.
Consolidate and prioritize maintenance backlog
github.com
	GitHub MCP & Memory MCP	GitHub MCP aggregates open issues and leftover tasks; Memory MCP stores priority matrix and decision criteria.
Draft maintenance plan and secure approvals
github.com
	Memory MCP & GitHub MCP	Memory MCP provides templates and historical maintenance plans; GitHub MCP posts the plan for review and acceptance.
Configure governance cadence and set up recurring checks	Grafana MCP & Buildkite MCP	Grafana monitors ongoing KPIs; Buildkite schedules periodic tests and health checks.
Protocol 22 – Implementation Retrospective

Context: Synthesizes lessons learned by aggregating cross‑protocol insights, sending pre‑survey, running retrospective sessions, capturing insights, prioritizing actions, assigning owners, and publishing a report
github.com
github.com
github.com
github.com
.

Recommendations:

Task	MCP tool	Reason
Aggregate cross‑protocol insights
github.com
	Memory MCP	Collects context from all protocols (risks, metrics, decisions); synthesizes into themes.
Send pre‑survey and run retrospective session
github.com
	Grafana MCP & Playwright MCP	Grafana OnCall schedules the session; Playwright automates interactive retrospective tools (e.g., Miro).
Capture insights and actionable items
github.com
github.com
	Memory MCP	Records feedback and links it to original decisions or tasks; supports tracking improvement actions.
Assign owners and due dates	GitHub MCP	Creates issues or tasks for each improvement item with owners and deadlines.
Protocol 23 – Script Governance

Context: Governs automation scripts across the project by indexing scripts, validating inventory completeness, categorizing scripts, auditing documentation quality, running static analysis, confirming artifact compliance, generating a governance scorecard, publishing remediation backlog, and sharing insights
github.com
github.com
.

Recommendations:

Task	MCP tool	Rationale
Index scripts and validate inventory
github.com
	Filesystem MCP & GitMCP	Filesystem MCP traverses directories to list all scripts; GitMCP searches for script patterns to ensure inventory completeness.
Categorize scripts and audit documentation quality
github.com
	SonarQube MCP & Memory MCP	SonarQube MCP runs static analysis and documentation linter; Memory MCP catalogs each script’s category and associated documentation.
Run static analysis and confirm artifact compliance	Code Runner MCP & SonarQube MCP	Code Runner executes lints; SonarQube MCP ensures no critical violations.
Generate governance scorecard and remediation backlog	GitHub MCP & Filesystem MCP	GitHub MCP opens issues for remediation tasks; Filesystem MCP produces a governance report.

These recommendations align each protocol’s tasks with MCP tools that maximize automation and intelligence while maintaining governance. The mapping builds on the features of well‑adopted 2025 MCP servers and the protocol‑defined quality gates.

Priority MCP tools ranked by impact (descriptions and links):
Top MCP Tools for 2025 – Ranked by Impact

This list ranks the most impactful Model Context Protocol (MCP) tools available in 2025 based on their ability to improve productivity, automation and quality across the AI‑driven workflow. Only production‑ready tools with active ecosystems were considered. Each entry includes a description, key capabilities, and a link to the tool or documentation.

Rank	MCP Tool	Key Capabilities	Why It Matters
1	Grafana MCP server	Provides APIs to search dashboards, fetch metrics and logs (Prometheus, Loki), run queries, manage OnCall schedules, and retrieve incidents. Supports RBAC and context‑window strategies
github.com
.	Critical for post‑deployment monitoring (protocol 16) and incident management (protocol 17). Enables real‑time observability, alerting and on‑call escalation across multiple protocols.
2	GitHub MCP server	Automates repository tasks: create issues, PRs, branches; retrieve code files; search repositories; manage reviews and assignments.	Foundational for scaffolding (protocols 03–05), task execution (protocol 10), defect management (protocol 11–13), and governance (protocol 23). Integrates with existing GitHub workflows.
3	GitMCP server	High‑recall code search and context retrieval to ground the model in real code, reducing hallucinations and enabling accurate architecture decomposition.	Valuable for technical design (protocol 07), task decomposition (protocol 08), code analysis (protocol 05), and script governance (protocol 23).
4	Filesystem MCP server	Securely reads and writes files and directories; lists directory contents; removes or moves files.	Core for environment setup (protocol 09), artifact packaging (protocols 11, 13, 14), document management (protocol 19), closure packages (protocol 20), and script governance (protocol 23).
5	Code Runner MCP server	Executes scripts or code snippets in sandboxed Docker environments, supporting multiple languages.	Automates the numerous script executions defined in protocols (e.g., validate_brief.py, generate_prd_assets.py, run_contract_tests.py). Ensures reproducibility and avoids polluting the host environment.
6	Playwright MCP server	Enables headless browser automation (click, type, navigate) and UI test execution.	Enhances integration testing (protocol 11), UAT simulations (protocol 13), pre‑deployment smoke tests (protocol 14), and performance tuning (protocol 18).
7	Memory MCP server	Offers a persistent knowledge graph storing entities, relationships and artifacts across sessions.	Supports traceability, persona mapping and retrieval of contextual knowledge across protocols (03–22). Reduces repeated reasoning and fosters continuous learning.
8	Buildkite MCP server	Interfaces with Buildkite CI/CD pipelines to trigger builds, monitor status, and download artifacts.	Key for quality audits (protocol 12), pre‑deployment rehearsals (protocol 14), production releases (protocol 15), and maintenance routines (protocol 21).
9	SonarQube MCP server	Fetches static analysis metrics (code smells, complexity, coverage) from SonarQube instances.	Useful for quality audits (protocol 12), script governance (protocol 23), and performance optimisation (protocol 18).
10	Sentry MCP server	Retrieves error events, release health, and incidents from Sentry; creates issues for new errors.	Enhances incident response and monitoring (protocols 15–17) by surfacing real‑time errors and facilitating root‑cause analysis.
Supporting Sources

The Grafana MCP server’s capabilities (dashboards, metrics queries, OnCall management) are documented in the awesome‑mcp‑servers repository, highlighting features such as search, Prometheus/Loki queries and incident handling
github.com
.

A Medium article on the Model Context Protocol describes how MCP acts as a “universal remote” for AI systems, emphasising the importance of tools like GitHub MCP server, GitMCP, Playwright MCP, Memory MCP, Filesystem MCP and Fetch MCP in 2025
medium.com
.

These ranked tools provide the greatest leverage across the 23 protocols and form the basis for the integration recommendations.

Cross‑protocol opportunities (tools benefiting multiple phases):
Cross‑Protocol Integration Opportunities

Many MCP tools provide capabilities that span multiple protocols. Leveraging these cross‑protocol opportunities can reduce redundancy, preserve context and improve overall workflow efficiency.

1. Persistent Knowledge Graph (Memory MCP)

Protocols impacted: 03–08, 13, 19–23

Opportunity: Store all entities (requirements, tasks, personas, ADRs, risk logs, design decisions, UAT feedback, retrospective actions) in a single knowledge graph. This allows easy retrieval of context across phases. For example, tasks generated in protocol 08 can link to requirements stored in protocol 06; retrospectives (protocol 22) can query open actions from maintenance planning (protocol 21).

Value: Eliminates repeated data entry, ensures traceability, enables analytics on relationships (e.g., which risks recur across releases).

2. Unified Repository & Issue Management (GitHub MCP)

Protocols impacted: All protocols except 18 (performance optimisation uses code metrics but still commits modifications).

Opportunity: Use GitHub MCP to centralize every approval, defect, action item, and document within the repository. Create issues for UAT defects, tasks for retrospective actions, and PRs for documents. This yields a single source of truth and audit trail.

Value: Streamlines communication, ensures that status can be monitored across protocols, and supports automated reporting (e.g., linking tasks to code changes).

3. Automated Quality Gates (SonarQube MCP + Buildkite MCP)

Protocols impacted: 05 (bootstrap), 10 (task execution), 12 (quality audit), 14 (pre‑deployment), 15 (production release), 23 (script governance).

Opportunity: Combine Buildkite pipelines with SonarQube metrics to enforce quality gates. The pipeline triggers static analysis and tests; SonarQube MCP fetches metrics for pass/fail decisions. Use GitHub MCP to block merges if thresholds aren’t met.

Value: Ensures continuous quality checks throughout the lifecycle, reducing bugs and technical debt at later stages.

4. Observability & Incident Triaging (Grafana MCP + Sentry MCP)

Protocols impacted: 11–18

Opportunity: Integrate Grafana MCP for metrics/logs and Sentry MCP for error events to provide a unified observability pipeline. When an anomaly is detected via Grafana queries, automatically pull correlated error traces from Sentry. Use Memory MCP to store incident details and Buildkite MCP to run mitigation pipelines.

Value: Shortens detection‑to‑resolution time, provides comprehensive incident context, and supports data‑driven retrospectives.

5. Test Automation & UI Validation (Playwright MCP + Code Runner MCP)

Protocols impacted: 10–15, 18

Opportunity: Use Code Runner MCP for backend and API tests while Playwright MCP handles UI tests. Results can be combined and stored via Filesystem MCP. Using both ensures full coverage across layers.

Value: Increases confidence in releases, catches integration issues early and ensures parity between user experience and backend functionality.

6. Secure Artifact Management (Filesystem MCP)

Protocols impacted: All protocols

Opportunity: Centralize storage of all artifacts (documents, logs, scripts, reports) under a defined root. Use Filesystem MCP for packaging evidence bundles (protocols 11, 13, 14) and storing final deliverables (protocols 19–20). Combine with Code Runner to generate and commit artifacts.

Value: Simplifies artifact retrieval, improves reproducibility, and ensures consistent directory structures across phases.

7. External Knowledge Enrichment (Fetch MCP)

Protocols impacted: 01, 02, 06, 18, 20

Opportunity: Use Fetch MCP to retrieve external documents (standards, competitor analysis, pricing) and feed them into Memory MCP. This enriches proposals, discovery briefs, PRDs and performance analyses.

Value: Broadens the knowledge base beyond internal data, leading to better informed decisions and competitive proposals.

8. Continuous Feedback Loops (Buildkite MCP + Memory MCP)

Protocols impacted: 12–22

Opportunity: Capture metrics, test results and retrospectives in Memory MCP; schedule periodic builds via Buildkite MCP to test against the latest code and infrastructure. Use results to update maintenance plans and improvement actions.

Value: Creates a continuous improvement cycle where metrics and feedback directly inform maintenance and future planning.

By recognizing these cross‑protocol opportunities, teams can design integration workflows that maximize reuse, maintain consistency, and accelerate the overall project lifecycle.

Integration Specs for each tool:

Grafana MCP:
Grafana MCP Integration Specification

This document describes how to integrate the Grafana MCP server into the SuperTemplate workflows to support monitoring, observability, and incident management (protocols 11, 14–18). The instructions assume a running Grafana MCP server accessible over HTTP.

1. Server Endpoint & Authentication

Base URL: configure an environment variable GRAFANA_MCP_BASE_URL pointing to the server (e.g., https://mcp.example.com/grafana).

API Key: create a Grafana API key with Editor permissions. Store it as GRAFANA_MCP_API_KEY in the agent’s secret vault.

When invoking the API, include an Authorization: Bearer <API_KEY> header. For example, using cURL:

curl -H "Authorization: Bearer $GRAFANA_MCP_API_KEY" \
     "$GRAFANA_MCP_BASE_URL/dashboards/search?query=staging"

2. Searching Dashboards

The Grafana MCP server exposes endpoints to list and search dashboards. Use these operations to retrieve dashboards relevant to the current protocol:

List dashboards: /dashboards/search?query=<text> returns an array of dashboards matching the query string. Example:

{
  "query": "production latency"
}


Get dashboard by UID: /dashboards/uid/<uid> returns the full dashboard JSON, including panels and metrics. Retrieve UIDs from the search results.

3. Querying Metrics and Logs

To capture baseline metrics and verify instrumentation coverage (protocols 14–18):

Prometheus query: call /prometheus/query with a PromQL expression.
Example request:

{
  "expr": "rate(http_request_duration_seconds_sum[5m]) / rate(http_request_duration_seconds_count[5m])",
  "step": 60
}


The response includes a time series of values suitable for establishing baselines.

Loki query: call /loki/query with a LogQL expression to extract log lines or patterns. Use this to verify that log instrumentation exists for all components.

4. Incident & OnCall Management

Grafana MCP integrates with Grafana OnCall for incident routing:

List incidents: /oncall/incidents?status=active returns currently active incidents.

Acknowledge incident: /oncall/incidents/<id>/acknowledge marks an incident as acknowledged.

Create alert rule: /oncall/alert-rules with payload including name, conditions, escalation policies, and recipients. Use this to configure alert thresholds defined in protocol 16.

5. Example: Capturing a Baseline Metric Snapshot

Query the request latency metric for both staging and production to establish parity (protocol 14):

curl -H "Authorization: Bearer $GRAFANA_MCP_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))"}' \
     "$GRAFANA_MCP_BASE_URL/prometheus/query"


Store the results in a JSON file using Filesystem MCP to include in the pre‑deployment package.

Use a similar query after production deployment (protocol 15) to monitor stabilization.

6. Integration Points
Protocol	Use case	Method
11 – Integration Testing	Verify environment parity by comparing staging metrics and logs.	Search dashboards, Prometheus and Loki queries.
14 – Pre‑Deployment Validation	Capture staging baseline metrics and logs; test alert rules.	Prometheus and Loki queries; create temporary alert rules.
15 – Production Deployment	Monitor immediate post‑deployment metrics; detect anomalies.	Periodic queries and incident retrieval.
16 – Post‑Deployment Monitoring	Configure dashboards, alert rules, and runbooks; test OnCall notification paths.	Use dashboard APIs and OnCall operations.
17 – Incident Response	Retrieve active incidents and acknowledgment; enrich incident reports with metrics.	List and acknowledge incidents, query logs and metrics for root cause.

This integration specification ensures that the agent can programmatically access Grafana dashboards, metrics and incidents to meet the requirements of the monitoring and deployment protocols.

GitHub MCP:
GitHub MCP Integration Specification

The GitHub MCP server provides programmatic access to repository management functions such as issue creation, pull request handling, code search, file reading and branch operations. It is central to many protocols that involve code changes, approvals and governance.

1. Authentication & Setup

Obtain a GitHub personal access token (PAT) with the repo and read:org scopes.

Set the environment variable GITHUB_MCP_API_KEY to this token.

Define GITHUB_MCP_BASE_URL, for example https://mcp.example.com/github.

Every request must include an Authorization: Bearer <GITHUB_MCP_API_KEY> header.

2. Repository Operations
Listing repositories

Use /repositories to list repos the token can access. Response includes names and IDs:

curl -H "Authorization: Bearer $GITHUB_MCP_API_KEY" \
     "$GITHUB_MCP_BASE_URL/repositories?affiliation=owner"

Creating issues

To track tasks, defects or approvals, call /issues/create with a repository name, title, body and assignees:

{
  "repo": "your-org/your-repo",
  "title": "PRD Approval",
  "body": "Please review and approve the PRD document by EOD.",
  "assignees": ["@reviewer"]
}


The response returns the issue number and URL.

Creating pull requests

Use /pull-requests/create to open a PR from a feature branch to the main branch. Provide repo, head, base, title, and body. Example:

{
  "repo": "your-org/your-repo",
  "head": "feature/prd-draft",
  "base": "main",
  "title": "Add initial PRD document",
  "body": "This PR adds the first draft of the PRD.  Please review."
}

Searching and reading files

Search code: /code/search with a query string and repository. Example: search for environment setup scripts:

{
  "repo": "your-org/your-repo",
  "query": "doctor.py"
}


Read file content: /files/read with repo and path. Use this to read existing documentation or configuration templates.

Branch and commit operations

Create branch: /branches/create with repo, branch_name, and from_sha (commit to base from). Use to start new feature work.

Commit file changes: /files/update with repo, path, content, and commit_message. Use to store generated assets (e.g., PRD, design specification).

3. Integration Patterns
Protocol	Use case	API operations
03 – Project Brief Creation	Create issues for approvals and track risk register items.	issues/create
04 – Project Bootstrap	Commit scaffold code and create feature branches.	branches/create, files/update
05 – Bootstrap Your Project	Migrate rule files and commit them to the repository.	files/update, pull-requests/create
06 & 07 – PRD and Design	Open PRs for PRD and design documents; assign reviewers.	pull-requests/create
10 – Controlled Task Execution	Commit code after each subtask; update tasks in issues.	files/update, issues/update
11–14 – Testing & Deployment	Create issues for defects and deployment approvals; attach evidence as PR comments.	issues/create, pull-requests/comments/create
23 – Script Governance	Track remediation backlog and governance scorecard.	issues/create
4. Example Workflow

Below is a minimal example of committing a generated PRD and opening a PR:

# Step 1: write the PRD file using Filesystem MCP (assumed).  Then commit via GitHub MCP.
CONTENT_BASE64=$(base64 prd.md | tr -d '\n')
curl -H "Authorization: Bearer $GITHUB_MCP_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"repo":"your-org/your-repo","path":"docs/PRD.md","content":"'$CONTENT_BASE64'","commit_message":"Add PRD draft"}' \
     "$GITHUB_MCP_BASE_URL/files/update"

# Step 2: create a feature branch and open a PR
curl -H "Authorization: Bearer $GITHUB_MCP_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"repo":"your-org/your-repo","branch_name":"feature/prd-draft","from_sha":"main"}' \
     "$GITHUB_MCP_BASE_URL/branches/create"

curl -H "Authorization: Bearer $GITHUB_MCP_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"repo":"your-org/your-repo","head":"feature/prd-draft","base":"main","title":"Add PRD draft","body":"Initial PRD draft for review."}' \
     "$GITHUB_MCP_BASE_URL/pull-requests/create"



This specification enables the agent to leverage GitHub MCP for repository tasks needed throughout the project lifecycle.

GitMCP:
GitMCP Integration Specification

The GitMCP server provides advanced code search and retrieval to supply high‑recall context to language models. Its ability to search through large repositories and return relevant code snippets reduces hallucination and improves grounding for architecture and task generation.

1. Configuration

Define GITMCP_BASE_URL (e.g., https://mcp.example.com/gitmcp) and set an API key GITMCP_API_KEY (obtain from the GitMCP service admin).

Provide a list of repositories to index. For the SuperTemplate, index the project repo and any shared libraries. Use /repositories/index to start indexing.

2. Searching Code
Textual code search

Use /search to query for code patterns, functions or architecture constructs. Example: retrieve all docker-compose files to understand service composition:

{
  "repo": "your-org/your-repo",
  "query": "filename:docker-compose.yml",
  "topn": 10
}


The response returns file paths and excerpts, which can then be read via GitHub MCP or GitMCP’s /files/read operation.

Semantic search (if supported)

For design or task decomposition, you may ask GitMCP to find examples of “service boundaries” or “authentication middleware”. The server uses embeddings to match semantically similar code. Example:

{
  "repo": "your-org/your-repo",
  "query": "example of implementing circuit breaker pattern in Node.js",
  "topn": 5,
  "semantic": true
}

3. Retrieval and Context Building

After obtaining search results, call /files/read with the repository and file path to fetch the full contents:

{
  "repo": "your-org/your-repo",
  "path": "services/authentication/middleware.ts"
}


Use the retrieved code as grounding context when drafting technical designs or tasks.

4. Integration Guidelines
Protocol	Application
05 – Bootstrap Your Project	Identify existing rules, configuration files and architecture patterns in the repository.
07 – Technical Design & Architecture	Discover service boundaries, prior ADRs, or similar implementations to inform decomposition.
08 – Technical Task Generation	Find examples of tasks and acceptance criteria to guide decomposition; ensure coverage of edge cases.
23 – Script Governance	Search for all scripts matching patterns (e.g., *.sh, *.py) to build an inventory.
5. Combining with Memory MCP

Store search results or important code snippets in Memory MCP for quick retrieval in subsequent steps. Link each snippet to the protocol and rationale for its selection.

This integration ensures the agent can quickly access relevant code context across large codebases.

Filesystem MCP:
Filesystem MCP Integration Specification

The Filesystem MCP server exposes secure file system operations for reading, writing, listing and manipulating files and directories. It is vital for tasks involving artifact generation, environment setup, packaging, and evidence storage.

1. Setup

Set FILESYSTEM_MCP_BASE_URL (e.g., https://mcp.example.com/filesystem) and an API key FILESYSTEM_MCP_API_KEY.

Define a root directory for the project where operations will occur. Configure this via environment variable FILESYSTEM_MCP_ROOT. The server will only permit access under this root.

2. Core Operations
Reading and writing files

Read file: send a GET request to /read?path=<relative-path>. Returns the file contents. Example:

curl -H "Authorization: Bearer $FILESYSTEM_MCP_API_KEY" \
     "$FILESYSTEM_MCP_BASE_URL/read?path=docs/architecture.md"


Write file: POST to /write with JSON body containing path and content (encoded as base64). Example:

{
  "path": "outputs/test-report.json",
  "content_base64": "eyJ0ZXN0cyI6IDF9"  // base64 of JSON
}

Listing directories

Call /list?path=<dir> to retrieve directory contents. Use this for inventory tasks (protocol 23) or verifying file structure.

Moving or deleting files

Use /move and /delete for housekeeping (e.g., archiving old logs). Provide source_path and destination_path for move operations.

3. Integration Points
Protocol	Use cases
01–05	Write analysis outputs, tone maps, governance rules, and scaffolds; read templates for proposals and briefs.
06 & 07	Store PRD and design documents; read & write risk logs and diagrams.
09	Validate environment prerequisites by reading configuration files and verifying version files; write onboarding handbooks.
11–14	Package test evidence, log files, staging parity reports, and deployment artifacts into ZIP bundles.
15–20	Store post‑deployment validation reports, closure packages, maintenance plans and runbooks.
23	Traverse directories to index scripts, verify file naming conventions, and clean up deprecated scripts.
4. Example: Packaging Evidence

Create a directory for the evidence bundle: /mkdir?path=evidence/gate11 (if supported) or ensure directory exists via /list.

Write files such as integration-test-report.json, environment-parity.json using multiple /write calls.

Once all files are written, optionally compress them (if the MCP server supports /compress). Otherwise, list the folder and provide the path for stakeholders to download.

5. Security Considerations

The server enforces sandboxing under FILESYSTEM_MCP_ROOT. Do not attempt to traverse outside this root.

Sensitive files (e.g., secrets) should not be written without encryption; store secrets in secret vaults instead.

This integration allows the agent to manage all file system interactions required by the workflow in a safe and reproducible manner.

Code Runner MCP:
Code Runner MCP Integration Specification

The Code Runner MCP server provides a sandboxed environment to execute scripts and code snippets across multiple languages. It is essential for automating the execution of validation scripts, test suites, and other automation hooks defined in the protocols.

1. Configuration

Set CODERUNNER_MCP_BASE_URL (e.g., https://mcp.example.com/code-runner) and an API key CODERUNNER_MCP_API_KEY.

Define resource limits (CPU, memory, time) via environment variables or request parameters to prevent runaway execution.

2. Running a Script

To execute a script file from the repository:

Use Filesystem MCP to read the script content or pass the path directly.

POST to /run with a JSON body specifying language, code, and optional args:

{
  "language": "python",
  "code": "import sys\nprint('Hello, world')",
  "args": []
}


The response includes stdout, stderr, exit_code, and optional files if the script writes output files.

3. Executing Repository Scripts

Often the agent must run scripts like validate_brief.py or run_contract_tests.py. Use GitHub MCP to read the file content or pass a reference to Code Runner if the server integrates with Git. Example request to run a file via path:

{
  "language": "python",
  "file_path": "scripts/validate_brief.py",
  "args": ["--input", "brief.json"]
}


The server pulls the file from the repository (if configured) and executes it in an isolated container.

4. Installing Dependencies

If a script requires dependencies, include a requirements section. Example for a Node.js project:

{
  "language": "node",
  "code": "const lodash = require('lodash'); console.log(lodash.shuffle([1,2,3]));",
  "requirements": { "npm": ["lodash@^4.17.21"] }
}


For Python, specify a pip list. The server will install packages before execution.

5. Integration with Other MCPs

After execution, store outputs via Filesystem MCP or commit results via GitHub MCP. For example, to run generate_prd_assets.py and commit results:

Call Code Runner MCP to run the script with appropriate arguments.

Use Filesystem MCP to retrieve generated files.

Use GitHub MCP to commit them to the repository.

6. Protocol Usage Examples
Protocol	Script	Purpose
03	validate_brief.py	Ensure project brief completeness.
06	generate_prd_assets.py, validate_prd_gate.py	Generate PRD artifacts and run gate validation
github.com
.
07	validate_workflow_integration.py	Verify integration of design components.
08	validate_tasks.py, enrich_tasks.py	Check task completeness
github.com
.
09	doctor.py, install_and_test.sh	Validate environment readiness
github.com
.
11	run_contract_tests.py	Run integration tests
github.com
.
12	Coverage aggregation and CI scripts	Triggered via Buildkite but can be run in Code Runner for local checks.

This integration enables safe and reproducible execution of scripts across the workflow.

Playwright MCP:
Playwright MCP Integration Specification

The Playwright MCP server allows an agent to control a headless browser through MCP commands. It is used to automate UI tests, user acceptance testing, smoke tests, and to capture user flows for performance analysis.

1. Setup

Configure PLAYWRIGHT_MCP_BASE_URL (e.g., https://mcp.example.com/playwright) and an API key PLAYWRIGHT_MCP_API_KEY.

Define default browser settings (e.g., Chrome vs Firefox, headless mode). These can be passed in requests or set globally.

2. Basic Operations
Navigate and interact

Use /session/start to begin a browsing session. You can then send actions such as click, type, select, and wait_for_selector. Example to open a page and click a button:

{
  "actions": [
    { "action": "goto", "url": "https://staging.example.com/login" },
    { "action": "type", "selector": "input[name='username']", "text": "tester" },
    { "action": "type", "selector": "input[name='password']", "text": "password123" },
    { "action": "click", "selector": "button[type='submit']" },
    { "action": "wait_for_selector", "selector": "#dashboard" }
  ]
}


The response includes screenshots and DOM snapshots at each step.

Run test scripts

You can store Playwright test scripts in the repository and execute them via /tests/run. Provide the script path and optional configuration:

{
  "script_path": "tests/uat/checkout.spec.ts",
  "config": {
    "baseURL": "https://staging.example.com"
  }
}


The server will run the test and return results, including traces and screenshots.

3. Integration Scenarios
Protocol	Use case
11 – Integration Testing	Execute UI‑level tests as part of the integration suite; verify that contract tests and UI interactions align.
13 – UAT Coordination	Run UAT scripts to guide participants or record their interactions; capture qualitative insights from the DOM snapshots.
14 – Pre‑Deployment Validation	Perform smoke and regression tests on staging environment
github.com
.
15 – Production Deployment	Run immediate post‑deployment smoke tests to ensure key flows function
github.com
.
18 – Performance Optimization	Simulate user transactions during load tests; measure front‑end performance metrics.
4. Combining with Other MCPs

Filesystem MCP: store traces, screenshots and HTML snapshots produced by Playwright for evidence packaging.

Grafana MCP: correlate UI test durations with backend metrics.

Sentry MCP: capture any JavaScript errors encountered during execution.

With Playwright MCP, the agent can automate complex user journeys and validate application behaviour throughout the development lifecycle.

Memory MCP:
Memory MCP Integration Specification

The Memory MCP server provides a long‑term memory store that allows agents to persist and query structured knowledge across sessions. It supports storing entities, relationships and documents as a knowledge graph, enabling rich retrieval and reasoning.

1. Configuration

Set MEMORY_MCP_BASE_URL (e.g., https://mcp.example.com/memory) and MEMORY_MCP_API_KEY.

Define a project namespace (e.g., supertemplate_project_2025). All stored entities will be scoped under this namespace to avoid collisions.

2. Core Concepts

Entities: Represent things like requirements, risks, tasks, personas, documents, ADRs, and decisions.

Relations: Capture relationships between entities (e.g., “PRD covers requirement R1”, “task T1 implements design D1”, “risk mitigated by control C1”).

Documents: Full text or structured content (e.g., meeting notes, briefs, retrospectives).

3. API Usage
Creating entities

Use /entities/create with JSON body containing name, type, attributes, and optional relations. Example to store a requirement:

{
  "namespace": "supertemplate_project_2025",
  "name": "REQ-001",
  "type": "requirement",
  "attributes": {
    "description": "As a user, I want to upload a file so that ...",
    "priority": "high"
  }
}

Creating relations

Call /relations/create with source_entity_id, target_entity_id, and relation_type. Example: link a task to a requirement:

{
  "namespace": "supertemplate_project_2025",
  "source": "TASK-123",
  "target": "REQ-001",
  "type": "implements"
}

Querying the graph

Use /query with a graph query language (e.g., Cypher subset or custom DSL). Example to find all tasks implementing a requirement:

{
  "namespace": "supertemplate_project_2025",
  "query": "MATCH (t)-[:implements]->(r {name: 'REQ-001'}) RETURN t"
}

Storing documents

Use /documents/add with namespace, doc_id, content (plain text or markdown) and optional metadata. Later, retrieve documents by doc_id.

4. Integration Use Cases
Protocol	Stored Entities / Documents
03 – Project Brief	Requirements, assumptions, risk register, stakeholder roles, and traceability map.
05 – Project Bootstrap	Governance rules (as entities), repository mapping (directories as entities and relations).
06 – PRD Creation	User stories, functional and non‑functional requirements, risk mitigation strategies, validation plans.
07 – Technical Design	Architectural decisions (ADRs), system boundaries, component specifications.
08 – Task Generation	Persona models, tasks, dependencies, complexity ratings and mappings to rules.
13 – UAT Coordination	Participant roster, scenarios, feedback logs.
20 – Project Closure	Acceptance decisions, closure metrics and improvement actions.
22 – Retrospective	Themes, survey responses, action items, owner assignments.
5. Retrieval Patterns

When generating a document or making decisions, query Memory MCP to fetch all relevant entities and relationships. For example, before writing the design specification, pull all requirements and risk mitigations linked to the PRD. Use the graph query API to traverse the network and assemble an aggregated context.

This integration ensures continuity of knowledge across the entire project lifecycle, enabling the agent to reference previous decisions and artifacts without recomputation.

Buildkite MCP:
Buildkite MCP Integration Specification

Buildkite MCP server enables the agent to trigger CI/CD pipelines, monitor their status, and retrieve build artifacts. It is used for quality audits, pre‑deployment rehearsals, production releases, and maintenance tasks.

1. Configuration

Set BUILDKITE_MCP_BASE_URL (e.g., https://mcp.example.com/buildkite) and BUILDKITE_MCP_API_KEY.

Identify Buildkite organizations and pipelines to be managed (e.g., org_slug/project_pipeline). Provide them in the agent’s configuration.

2. Triggering Pipelines

Call /pipelines/<org>/<pipeline>/trigger with optional environment variables and commit information. Example for a staging deployment rehearsal (protocol 14):

{
  "env": {
    "DEPLOY_ENV": "staging",
    "PRE_DEPLOY_CHECK": "true"
  },
  "commit": "feature/release-candidate"
}


The response includes a build_number and URL.

3. Monitoring Builds

Use /pipelines/<org>/<pipeline>/builds/<build_number> to fetch status. Poll this endpoint until state is one of passed, failed, or canceled. Example:

curl -H "Authorization: Bearer $BUILDKITE_MCP_API_KEY" \
     "$BUILDKITE_MCP_BASE_URL/pipelines/myorg/my-pipeline/builds/123"

4. Retrieving Artifacts

When a build completes, call /pipelines/<org>/<pipeline>/builds/<build_number>/artifacts to list artifacts. To download an artifact, call /artifacts/<artifact_id>/download. Use Filesystem MCP to save the artifact locally.

5. Integration Scenarios
Protocol	Usage
12 – Quality Audit	Trigger full CI pipelines and retrieve coverage reports
github.com
.
14 – Pre‑Deployment Validation	Run a rehearsal deployment build; check results and logs
github.com
.
15 – Production Deployment	Execute the production deployment pipeline and monitor for success
github.com
.
17 – Incident Response	Trigger rollback or hotfix pipelines if mitigation requires deployment.
21 – Maintenance Planning	Schedule recurring builds to test system health.
6. Example Workflow

Trigger a rehearsal deployment build for staging and store the build number.

Poll the build status until completion. If the build fails, fetch the logs and create an incident via GitHub MCP.

Download artifacts such as staging-parity-report.json and store them via Filesystem MCP for the pre‑deployment package.

With Buildkite MCP integration, the agent can automate CI/CD workflows and incorporate build outputs into decision‑making.

SonarQube MCP:
SonarQube MCP Integration Specification

The SonarQube MCP server exposes static analysis metrics and code quality reports from a SonarQube instance. It enables automated quality gates, coverage aggregation, and identification of technical debt across the project.

1. Configuration

Set SONAR_MCP_BASE_URL (e.g., https://mcp.example.com/sonarqube) and SONAR_MCP_API_KEY.

Provide the SonarQube project key (e.g., supertemplate-project) in the agent’s configuration.

2. Fetching Metrics
Summary metrics

Call /metrics/summary with project_key to retrieve high‑level metrics such as code coverage, bugs, vulnerabilities, code smells and technical debt ratio. Example:

curl -H "Authorization: Bearer $SONAR_MCP_API_KEY" \
     "$SONAR_MCP_BASE_URL/metrics/summary?project_key=supertemplate-project"

Detailed measures

To fetch specific measures (e.g., duplication density, complexity per file), call /metrics/detail with metric_keys:

{
  "project_key": "supertemplate-project",
  "metric_keys": ["coverage", "duplicated_lines_density", "cognitive_complexity"]
}

Issues and code smells

Use /issues/search with filters (e.g., severity, type, status) to retrieve open issues. Example: list all blocker bugs:

{
  "project_key": "supertemplate-project",
  "severities": ["BLOCKER"],
  "types": ["BUG"],
  "statuses": ["OPEN"]
}

3. Integration Points
Protocol	Usage
05 – Bootstrap Your Project	Use metrics to assess repository health and identify areas requiring refactoring.
10 – Controlled Task Execution	Run static analysis after each subtask to ensure no new issues are introduced.
12 – Quality Audit	Aggregate coverage and quality metrics to inform the audit report
github.com
.
14–16 – Pre‑Deployment & Monitoring	Verify that quality gates pass before releasing to production.
23 – Script Governance	Evaluate script quality and documentation; ensure scripts meet static analysis thresholds
github.com
.
4. Example Workflow

As part of the quality audit (protocol 12), call /metrics/summary to obtain coverage and technical debt ratios.

If coverage is below the target threshold (e.g., 80 %), create a GitHub issue via GitHub MCP for remediation.

Fetch open vulnerabilities and assign them to relevant developers.

This integration ensures objective assessment of code quality at each stage of the workflow.

Sentry MCP:
Sentry MCP Integration Specification

The Sentry MCP server provides access to application error monitoring, release health and incident data from Sentry. It is particularly useful for incident response (protocol 17), UAT feedback, and monitoring (protocols 15–16).

1. Setup

Set SENTRY_MCP_BASE_URL (e.g., https://mcp.example.com/sentry) and SENTRY_MCP_API_KEY.

Identify the Sentry organisation and projects to monitor. Configure them in the agent’s environment (e.g., SENTRY_ORG=supertemplate and SENTRY_PROJECT=backend-app).

2. Fetching Events and Issues
Recent issues

Call /projects/<org>/<project>/issues to retrieve recent issues. You can filter by severity, status, environment and time window:

curl -H "Authorization: Bearer $SENTRY_MCP_API_KEY" \
     "$SENTRY_MCP_BASE_URL/projects/supertemplate/backend-app/issues?status=unresolved&query=is:unresolved"


The response includes issue IDs, titles, first/last seen timestamps, and counts.

Event details

To fetch event details, call /issues/<issue_id>/events/<event_id>. This returns stack trace, tags, release and user context.

Release health

Call /projects/<org>/<project>/releases/<version>/health to obtain metrics such as crash‑free sessions and crash counts. Use this to monitor release rollouts in protocol 15.

3. Creating Issues and Comments

Sentry MCP also allows creating or updating issues to log incidents discovered via testing or monitoring. Use /projects/<org>/<project>/issues/create with a title, description and tags. Example:

{
  "org": "supertemplate",
  "project": "backend-app",
  "title": "High error rate during checkout",
  "description": "Observed an increased rate of 500 errors during load test.",
  "tags": {"environment": "staging"}
}

4. Integration Scenarios
Protocol	Use case
11 – Integration Testing	Fetch error traces for failures discovered during tests.
13 – UAT Coordination	Collect errors reported by users during UAT and create Sentry issues.
14 – Pre‑Deployment Validation	Confirm there are no unresolved high‑severity issues in staging before deployment.
15 – Production Deployment	Monitor release health metrics (crash‑free sessions) immediately after deployment.
16 – Post‑Deployment Monitoring	Receive alerts for runtime exceptions; correlate with Grafana metrics.
17 – Incident Response	Retrieve details of the offending error, stack trace and user context to inform root‑cause analysis
github.com
. Create incidents or assign owners as needed.
5. Example Workflow

During UAT, if testers encounter an error, call /projects/org/project/issues/create to log it in Sentry with environment UAT and tags referencing the test scenario.

Monitor the project’s issue feed and release health during deployment. If crash‑free sessions drop below 99 %, trigger a rollback via Buildkite MCP.

After incident resolution, fetch all related events, attach them to the incident report, and store them via Filesystem MCP.

This integration ensures that errors and incidents are tracked and addressed promptly throughout the project lifecycle.

Fetch MCP:
Fetch MCP Integration Specification

The Fetch MCP server enables the agent to retrieve and transform web content from the public Internet. It supports tasks such as competitor research, regulatory standard lookups, and enriching requirements or documentation.

1. Configuration

Define FETCH_MCP_BASE_URL (e.g., https://mcp.example.com/fetch) and an API key FETCH_MCP_API_KEY.

Set an optional DEFAULT_LANGUAGE to control automatic translation of content.

2. Fetching Web Content

Call /fetch with a URL and optional parameters to retrieve web content. The response includes the extracted text, metadata and optionally a summarisation. Example:

{
  "url": "https://docs.oracle.com/en/java/javase/17/",
  "language": "en",
  "summarize": true
}

3. Transformation Options

Summarisation: set summarize: true to obtain a concise summary of the page.

Language translation: specify language to translate content into the desired language (e.g., "language": "en").

Content format: choose between text and html. Default is text.

4. Integration Scenarios
Protocol	Use case
01 – Client Proposal Generation	Retrieve domain articles or competitor job postings to inform proposals and tone mapping.
02 – Client Discovery	Fetch industry standards or API documentation to prepare questions and integration inventories.
06 – PRD Creation	Obtain external specification documents or regulatory requirements to ensure compliance.
18 – Performance Optimization	Gather cloud provider pricing or best practices for performance tuning.
20 – Project Closure	Look up contractual terms or regulatory obligations for final acceptance review.
5. Combining with Memory MCP

After fetching and summarizing content, store the results in Memory MCP as external knowledge references. Link them to the requirements or tasks they inform.

This integration empowers the agent to augment internal knowledge with authoritative external sources when drafting documents or making decisions.
**CHATGPT**


Updated Analysis of AI Project Workflow vs. Cursor Protocols
Cross‑Checked Evidence
Findings from AI‑project‑workflow directory

Comprehensive blueprint for 28–30 protocols – The master guide (PROTOCOL‑CREATION‑SYSTEM.md) defines a modular system for AI/ML projects with phases from discovery through governance and closure. It lays out 10 required sections for each protocol (identity & ownership, AI role, workflow steps, quality gates, automation hooks, evidence summary, integration points, communication protocols, handoff checklist and reasoning/reflection) and specifies that every protocol must pass 11 validators
github.com
. A week‑by‑week roadmap describes how to copy the first five protocols, then create new AI‑specific protocols (06–28) with roughly 75–90 automation scripts and complete evidence tracking
github.com
.

Current progress – Contrary to initial assumptions, the protocols folder now contains a complete suite of 28 protocols numbered 01 through 28. Beyond the early bootstrap and use‑case steps, there are detailed protocols for project brief creation (03), risk & compliance assessment (03b), project bootstrap & context engineering (04), AI data strategy planning (07), data cleaning (09), feature engineering (10), model training & experimentation (11), model evaluation & drift monitoring (12), algorithm selection & baselines (13), model validation (14), edge‑case testing (15), bias detection & fairness audit (16), explainability (17), model packaging & containerization (18), pipeline orchestration (19), model deployment & serving (20), API integration (21), performance monitoring (22), data and concept drift detection (23), model retraining (24), incident response & rollback (25), model governance & audit (26), documentation & knowledge transfer (27) and project retrospectives & continuous improvement (28). We inspected Protocol 07 (Data Strategy) and Protocol 03b (Risk & Compliance) to confirm their depth: they define roles, prerequisites, multi‑phase workflows, quality gates, automation scripts and exhaustive evidence requirements. Some scripts in these protocols are still marked “to create,” but the high‑level structure exists and covers the AI lifecycle end‑to‑end.

Phased creation plan – The creation system identifies seven phases (Foundation & Discovery, AI planning, Data preparation, Model development, Testing & quality, MLOps & deployment, Monitoring & maintenance, Governance & closure). Each new protocol lists workflow steps, gates, new scripts and acceptance criteria; e.g., the AI Use‑Case Definition protocol requires a problem/AI fit score ≥ 0.8, success metrics definition and stakeholder sign‑off with new automation scripts like validate_ai_feasibility.py
github.com
. Later protocols cover data ingestion, cleaning, feature engineering, model training, bias detection, deployment, drift monitoring and incident response
github.com
. The schedule envisages completing all protocols in four weeks
github.com
.

Findings from .cursor/ai‑driven‑workflow directory

Detailed legacy protocols – The .cursor/ai‑driven‑workflow directory contains highly detailed protocols (23 in total) covering client proposal creation, discovery calls, project brief creation and other generic project activities. For example, 02-client‑discovery‑initiation.md describes a multi‑phase discovery process with role definitions, step‑by‑step instructions, four quality gates, automation scripts and a comprehensive evidence strategy
github.com
. The protocol emphasises evidence generation (e.g., discovery briefs, assumption trackers, risk/opportunity lists) and includes fallback procedures, communication templates and a retrospective analysis section
github.com
.

Governance patterns and heuristics – The legacy protocols embed design heuristics like extract‑before‑interpret, fail‑fast validation, bias detection, reasoning pattern declaration and continuous improvement. They prescribe manual and automated checks, specify scripts for each gate and maintain detailed artifact inventories. The analysis file (analysis-01-client-proposal-generation.md) abstracts these patterns into meta‑heuristics such as anchoring each workflow to an explicit mission and phase classification, embedding halt conditions at each step, and formalising quality gates with measurable metrics
github.com
.

Maturity but not AI‑specific – While the .cursor protocols are robust, they predate the AI‑project‑workflow blueprint and focus on generic project‑scoping tasks (proposal writing, discovery calls, project brief creation). They lack dedicated AI lifecycle steps (data preparation, model training, deployment, monitoring) and do not use the 11‑validator framework introduced in the new system. However, many of their governance techniques (evidence mandates, gating, retrospective loops) can inform the AI protocols.

Gaps, Overlaps and Missing Elements
Category	Observations
Protocol Coverage	The protocols directory now includes 28 detailed protocols covering the entire AI/ML lifecycle from client onboarding to retrospectives. Early protocols (01–05) handle proposal, discovery and project setup; middle protocols (06–20) govern use‑case definition, data strategy, data preparation, model development, testing and deployment; later protocols (21–28) cover integration, monitoring, drift detection, retraining, incident response, governance, documentation and retrospectives. Some scripts and validator implementations remain “to be created,” but structural coverage is complete.
Automation Scripts & Validators	The AI plan calls for 75–90 automation scripts and 11 validators, but only a few scripts (e.g., classify_ai_problem_type.py) exist. Many scripts referenced in .cursor protocols (e.g., validate_gate_02_pre_call.py, aggregate_evidence_02.py) are not integrated into the AI workflow. A script registry and gate configurations are required to ensure every protocol’s quality gates are implemented and tracked
github.com
. Missing validators (e.g., data drift detection, bias metrics) will block quality assurance for new protocols.
Numbering & Duplication	The .cursor protocols include multiple bootstrap or discovery steps that overlap with AI‑project‑workflow Phase 0 (Protocols 01–05). For example, both Protocol 04 (“Project Bootstrap & Context Engineering”) and Protocol 05 (“Bootstrap Your Project”) cover project setup; the AI plan could consolidate them into a single bootstrap protocol. Additionally, numbering gaps exist in .cursor (e.g., there is no Protocol 07), which can cause confusion when mapping to new AI protocols.
Governance & Risk Management	The new suite includes a dedicated risk & compliance assessment protocol (03b) that addresses legal, ethical and regulatory risks, plus later protocols (26–28) for governance, audit trails and retrospectives. However, some elements such as model cards, ethics documentation and script governance remain to be fully implemented.
Change Requests & Decision Logging	A formal change‑request management protocol (08b) governs scope adjustments, but Architectural Decision Records (ADRs) and systematic decision logging are still not mandated. Adding ADR templates and linking them to protocol outputs would improve traceability.
Post‑Deployment Feedback Loops	Later protocols (22–25) define performance monitoring, drift detection, retraining and incident response; however, formal mechanisms for user feedback collection, SLA tracking and continuous service improvement are still limited and should be expanded.
Script Governance	The AI plan references a script‑registry.json but provides no implementation. The .cursor protocols maintain a list of scripts per protocol but lack a unified registry to track ownership, versioning and deprecation, leaving automation governance ambiguous.
Consolidated Analysis of Protocol Refinements Needed

The AI project workflow aims to be AI‑ready by adding 23 protocols covering the full ML lifecycle. Based on the cross‑check, the following refinements or additions are critical:

Review and refine Phase 1–2 protocols – Ensure Protocol 07 (Data Strategy & Requirements Planning) and Protocols 08–11 (Data Collection, Data Preparation, Feature Engineering, Dataset Preparation) fully implement the required workflows, quality gates and automation scripts. Fill in any missing scripts marked “to create” and validate gates for data availability, quality, compliance and labelling.

Refine Phase 3–4 protocols – Protocols 11–17 already exist for model training, experimentation, evaluation, algorithm selection, validation, testing, bias detection and explainability. Review these documents to ensure they include detailed workflow steps, measurable gates (e.g., performance thresholds, bias metrics), automation scripts (training orchestration, hyperparameter tuning) and evidence artifacts (model cards, experiment logs). Implement any missing validators for fairness and interpretability.

Refine Phase 5 (MLOps & deployment) – Protocols 18–21 cover model packaging, pipeline orchestration, deployment, serving and API integration. Ensure these protocols provide clear instructions for serialization, containerization, registry integration, A/B testing, rollback and API documentation. Develop missing scripts, container builds and decision logs (ADRs) as needed, and link them with the change‑request protocol.

Strengthen monitoring & maintenance – Protocols 22–25 cover performance monitoring, drift detection, retraining and incident response. Augment them with real‑time dashboards, SLA tracking, user feedback loops, retraining triggers and root‑cause analysis. Implement automation scripts for drift detection and incident handling, and integrate with observability tools (Prometheus, Grafana).

Governance enhancements – Protocols 26–28 address governance, audit trails, documentation and retrospectives. Ensure they incorporate data governance (lineage, reproducibility, compliance with GDPR/ISO 42001), ethics and privacy assessments, bias audits, and script governance. Create a unified script registry, ADR templates and knowledge‑transfer mechanisms, and schedule periodic retrospectives to inform continuous improvement.

Script registry & validation infrastructure – Implement a script‑registry.json to track each automation script’s purpose, owner and version. Add missing validator scripts (validate_protocol_identity, role, gates, scripts, evidence, handoff, reasoning, reflection) and ensure they are invoked in CI/CD pipelines. Borrow gating patterns and automation commands from the .cursor protocols to build robust validation processes.

Numbering & consolidation – Adopt a consistent numbering scheme (01–28) and merge overlapping bootstrap protocols (Protocols 04–05) into a single “Project Bootstrap & Context Engineering” protocol. Avoid zero‑index duplicates and document dependencies to clarify sequence.

Evidence & artifact management – Leverage the evidence strategies in .cursor protocols (manifest, checksums, retrospective logs) for AI protocols. Each protocol should specify required artifacts (e.g., data dictionaries, feasibility reports, model cards) and store them in structured directories. Validators should ensure completeness and integrity.

Final Recommendation Summary (Strategic Level)

Prioritise protocol completion – The team should immediately address missing protocols in Phases 1–2 (data strategy and preparation) because they are prerequisites for model development. Without them, AI projects cannot progress. Adopt the 10‑section template and 11‑validator framework for each new protocol.

Consolidate and harmonise with legacy workflows – Merge overlapping bootstrap protocols and reuse governance patterns from the .cursor protocols, such as evidence generation, quality gates and retrospectives. However, adapt them to AI contexts by including data quality, fairness and compliance gates.

Implement script governance and validation infrastructure – Develop a script registry and ensure every protocol’s automation hooks are implemented, tested and registered. Set up CI/CD workflows to run validators and block merges on gate failures. Maintain a configuration directory for gate thresholds (as in .cursor) and document owners for each script.

Refine the existing change‑request protocol (08b) and introduce ADR protocols – Enhance the change‑request workflow and create an Architectural Decision Record protocol to manage scope adjustments and capture design decisions; define how requests are captured, analysed, approved and integrated into the workflow.

Enhance governance & risk management – Build dedicated protocols for risk & compliance assessment (ethical, privacy, security) and incorporate bias audit, fairness metrics and data governance. Link these to governance protocols (26–28) and include retention policies, audit logs and regulatory reporting.

Plan for monitoring and continuous improvement – Ensure that post‑deployment protocols collect user feedback, monitor performance and trigger retraining or incident response when thresholds are breached. Use dashboards and telemetry to inform continuous improvement and update protocols based on retrospective analysis.

Phased Implementation Plan

The following phased plan breaks down actions, owners, dependencies and timeline hints to implement the AI‑ready workflow. Dates assume a four‑week timeline similar to the master plan; adjust based on resource availability. Roles include Protocol Owner (PO), Automation Engineer (AE), Validator Developer (VD) and Governance Lead (GL).

Phase & Timeframe	Actions & Deliverables	Owners/Dependencies	Required Artifacts/Evidence
Week 1 – Foundation & Planning	1. Consolidate bootstrap protocols: merge Protocols 04–05 into a single “Project Bootstrap & Context Engineering” protocol and update numbering. 2. Copy validated protocols: ensure Protocols 01–03 are copied from .cursor/ai‑driven‑workflow and pass the 11 validators. 3. Create Protocol 07 (Data Strategy) using the template; include data availability assessment, compliance requirements, labelling strategy and feature requirements
github.com
.	PO: Phase 0–1 owner. AE: copy scripts from .cursor and adjust. VD: run existing validators. Dependencies: validated Protocol 06 and scripts.	Updated bootstrap protocol. Protocol 07 document with 10 sections. Automation scripts: assess_data_availability.py, validate_data_requirements.py. Evidence artifacts: data strategy report, compliance checklist, labelling strategy files.
Week 1 – Continued	4. Implement script registry: create scripts/script‑registry.json capturing existing scripts (from .cursor and AI use‑case protocol) with fields: name, path, protocol ID, purpose, owner, status
github.com
. 5. Set up validator framework: ensure that validators-system/scripts/validate_protocol_identity.py and other validators exist or stub them where missing; incorporate them into CI pipelines.	GL & VD: define schema for registry and validators. AE: integrate with CI.	script‑registry.json populated. Validator scripts created or updated. CI configuration updated to run validators for protocols 01–07.
Week 2 – Data Preparation (Protocols 08–11)	6. Evaluate and refine the existing data ingestion protocol (08) covering data source connection, collection automation, storage setup and initial profiling; design quality gates (volume, format validation, storage readiness)
github.com
. 7. Develop cleaning protocol (09) with missing value handling, outlier detection, type validation and quality gates (missing rate ≤ 0.05, quality score ≥ 0.95)
github.com
. 8. Build feature engineering protocol (10) and dataset preparation protocol (11) with steps and gates specified in the master plan
github.com
.	PO: Data preparation owner. AE: implement automation scripts (e.g., collect_data_sources.py, clean_missing_values.py). VD: create validator scripts for each gate. Dependencies: Protocol 07 completed; script registry ready.	Protocol documents 08–11 with 10 sections. New scripts for collection, cleaning, feature engineering, splitting (approx. 13 scripts). Artifacts: data ingestion logs, cleaning reports, feature stores, dataset version manifests.
Week 3 – Model Development & Testing (Protocols 12–17)	9. Draft model development protocols (12–14) covering algorithm selection, training/tuning, and evaluation; include experiment tracking, hyperparameter optimisation and performance benchmarks
github.com
. 10. Create testing & quality protocols (15–17) for edge‑case testing, bias detection and explainability; define fairness metrics, mitigation steps and model interpretability gates
github.com
. 11. Expand validator suite to include bias metrics, explainability checks and performance thresholds; update script registry with training and evaluation scripts.	PO: Model owner. AE: implement training (train_model.py), evaluation (calculate_metrics.py), bias detection (calculate_bias_metrics.py) scripts. VD: develop validators for performance, bias and explainability. Dependencies: Protocols 08–11 validated; experiment tracking tool chosen.	Protocols 12–17 with detailed workflows. Automation scripts for training, tuning, validation, bias detection and explainability. Artifacts: algorithm justification document, baseline model metrics, confusion matrices, bias audit report, explainability reports (e.g., SHAP values).
Week 3–4 – MLOps & Deployment (Protocols 18–21)	12. Develop packaging & orchestration protocols (18–19): define serialization, containerization, model registry integration and pipeline orchestration (e.g., Kubeflow/Airflow). 13. Create deployment protocols (20–21): specify serving infrastructure, A/B testing, rollback strategies and API development; include script templates for building Docker images and generating OpenAPI docs
github.com
. 14. Document ADRs and change control: add an ADR template and a change‑request protocol to capture design decisions and manage scope creep.	PO: Deployment/MLOps owner. AE: write scripts (serialize_model.py, build_docker_container.py, create_training_pipeline.py, develop_api_endpoints.py). VD: implement validators for container build, pipeline orchestration and API readiness. GL: design ADR and change‑request forms. Dependencies: Model development protocols validated.	Protocols 18–21 with 10 sections. Scripts for packaging, orchestration, deployment and API. Artifacts: container images, pipeline DAGs, deployment logs, ADRs, change‑request forms, API specs.
Week 4 – Monitoring & Governance (Protocols 22–28)	15. Implement monitoring & maintenance protocols (22–25): set up performance monitoring, drift detection, retraining pipelines and incident response with clear thresholds and escalation paths
github.com
. 16. Build governance protocols (26–28): define model lineage, reproducibility, audit trail generation, documentation and retrospectives
github.com
. Integrate risk & compliance assessment, bias audits, data privacy checks and user feedback loops. 17. Deploy script governance protocol: implement script registry maintenance, deprecation handling and periodic script review (similar to .cursor/ai-driven-workflow/23-script-governance-protocol.md).	PO: Governance lead. AE: scripts for monitoring (monitor_data_drift.py), retraining (create_retraining_pipeline.py), incident response (detect_performance_degradation.py), compliance (generate_compliance_docs.py) and governance. VD: validators for drift detection, retraining readiness, incident response and governance checks. GL: risk management and ethics frameworks. Dependencies: Deployment protocols validated; script registry operational.	Protocols 22–28 with evidence requirements. Monitoring dashboards (Grafana/Prometheus metrics). Incident logs, drift reports and retraining schedules. Governance artifacts: lineage diagrams, compliance documentation, audit reports, retrospectives and ADR logbooks.
Required Artifacts and Evidence by Phase

The following list summarises key artifacts and evidence outputs that should be produced during each phase. (Artifacts marked with ⚙️ should be accompanied by automation scripts; items marked 🗂️ should be version controlled.)

Phase 0 (Foundation & Discovery) – Discovery briefs, assumption trackers, risk/opportunity logs, question banks, integration inventories, call agendas and recap documents (many inherited from .cursor protocols)
github.com
. Evidence: gate validation reports, transcript archives and evidence manifests.

Phase 1 (AI Planning) – AI problem classification report, feasibility score report, success metrics specification, stakeholder alignment notes. Evidence: use‑case definition markdown, feasibility JSON and success‑metrics YAML
github.com
.

Phase 2 (Data Preparation) – Data collection logs, schema validation reports, cleaned data summaries, feature stores, dataset version records and metadata. Evidence: ingestion logs, cleaning reports, feature engineering documentation and dataset split manifests.

Phase 3 (Model Development) – Algorithm evaluation matrices, experiment tracking logs (e.g., MLflow), baseline performance reports, training metrics, hyperparameter tuning results, validation reports and model cards.

Phase 4 (Testing & Quality) – Test set performance metrics, edge‑case coverage tables, robustness reports, bias audit logs, fairness assessments and interpretability analyses (e.g., SHAP visualizations). Evidence: gate validation reports and mitigation plans.

Phase 5 (MLOps & Deployment) – Container images, Dockerfiles, pipeline DAGs, model registry entries, deployment logs, API documentation (OpenAPI), ADRs and change‑request forms. Evidence: validation of serving infrastructure, A/B test results and rollback procedures.

Phase 6 (Monitoring & Maintenance) – Performance dashboards, alert thresholds, drift detection reports, retraining triggers, incident response logs and shadow deployment metrics. Evidence: monitoring dashboards, retraining schedules and SLA compliance reports.

Phase 7 (Governance & Closure) – Lineage diagrams, reproducibility reports, compliance documentation, knowledge‑transfer materials, retrospective reports, risk logs and process improvement plans. Evidence: audit trail logs, ADR repositories, risk registers and closure checklists.

These artifacts ensure traceability and compliance throughout the AI project lifecycle. Validators and automation scripts should verify their presence, integrity and completeness at each gate.

---

**USER**

ipaliwanag mo sakin sa madaling maiintindihan, dapat walang hula. faithful sa report ang paliwanag
---
**CHATGPT**
Sige, diretso tayo. Ipapaliwanag ko nang simple, pero nakasandal lang sa mismong report at sa nakita sa repo, walang imbento.

1. Ano ang meron sa dalawang folder?
a) AI-project-workflow/protocols

Base sa aktwal na listahan ng files sa GitHub, meron ka nang kumpletong 28 AI protocols:

01–05 → proposal, discovery, brief, bootstrap, setup

03b → AI risk & compliance assessment

06 → AI use-case definition

07 → AI data strategy planning

08 → AI data collection / ingestion

08b → AI change-request management

09–11 → data cleaning, feature engineering, dataset prep

11–17 → model training, evaluation, testing, bias, explainability

18–21 → packaging, pipeline orchestration, deployment, API integration

22–25 → monitoring, drift detection, retraining, incident response

26–28 → model governance & audit, documentation, retrospective

Sa madaling salita:
Buong AI lifecycle sakop na sa structure – mula client proposal hanggang project retrospective.

Pero:
Sa loob ng mga protocol na ’yan, marami pang nakalagay na “scripts to create” / kulang na automation at hindi pa lahat naka-hook sa validator system.

b) .cursor/ai-driven-workflow

Dito naman, may 23 “legacy” protocols:

Nakafocus sa client proposal, discovery, project brief, general project governance.

Malakas sa:

quality gates

evidence strategy (logs, notes, artifacts)

step-by-step na instructions

retrospective patterns

Pero:

Hindi ito AI-lifecycle (walang data pipeline, training, deployment, drift, etc.).

Hindi naka-align sa 11-validator framework ng bagong AI system.

Summary:

AI-project-workflow/protocols = AI-lifecycle structure (01–28) pero kulang sa scripts/validators.

.cursor/ai-driven-workflow = mature governance patterns, pero hindi AI-specific.

2. Saan may gaps, overlaps, at kulang?
2.1. Coverage (sakop na ba lahat?)

GOOD:

Yung 28 protocols sa AI-project-workflow/protocols → kumpleto ang high-level stages:

proposal → discovery → planning → data → model → testing → deployment → monitoring → governance.

GAP:

Structure = kumpleto, pero:

maraming automation scripts na “to be created” pa

wala pang tunay na script registry

hindi pa lahat naka-wire sa 11 validators

2.2. Overlaps / doblado

Protocol 04 vs 05

Pareho silang may kinalaman sa project bootstrap / setup.

Risk: malilito kung saan dapat mag-edit / mag-update kasi halos pareho ng domain.

Recommendation sa report: pagsamahin/linawin para isang malinaw na bootstrap protocol lang.

.cursor vs bagong AI protocols

Maagang bahagi (proposal, discovery, brief) → may version sa .cursor at sa AI-project-workflow.

Kaya:

kailangan mag-decide: alin ang “source of truth”?

or paano gagamitin ang .cursor bilang governance reference, pero ang AI protocols bilang main flow.

2.3. Automation & validators

Sa report:

Target mo: 75–90 scripts + 11 validators (galing sa PROTOCOL-CREATION-SYSTEM).

Reality ngayon:

may iilang scripts (hal. classify_ai_problem_type.py, etc.)

marami sa protocols ang naka-lista lang ang scripts as “to create”

wala pang central script-registry.json na aktwal na implemented

validators system may skeleton, pero hindi pa full coverage per protocol

Bottom line:
Structure okay, pero execution layer (scripts/validators) kulang pa.

2.4. Governance, risk, change management

Base sa report:

Risk & compliance

Meron ka nang dedicated protocol: 03b-ai-risk-compliance-assessment.md.

Good: covered na ang legal/ethical/regulatory risk sa early phase.

Kulang pa:

model cards

ethics documentation

integrated script governance

Change requests

Meron nang 08b-ai-change-request-management.md.

So: hindi na missing ang change management, pero:

wala pang formal ADR (Architectural Decision Record) protocol

wala pang rule na “bawat major decision → dapat may ADR entry”

Post-deployment feedback

Protocols 22–25: monitoring, drift, retraining, incident response

Kulang pa:

malinaw na user feedback loop

SLA tracking (uptime / latency targets)

structured continuous improvement process (how feedback feeds next iteration)

Script governance

May idea sa system: script-registry.json at governance protocol (may reference pa sa .cursor 23-script-governance).

Pero ngayon:

wala pang actual na implemented registry

wala pang malinaw na process para:

mag-mark ng deprecated scripts

mag-assign ng owners

mag-schedule ng script review

3. Alin sa 28 protocols ang kailangan pang i-refine?

Faithful sa report, grouped siya by phase:

3.1. Phase 1–2 (Data planning & data prep)

Target protocols:

07 – AI data strategy planning

08 – AI data collection / ingestion

09 – data cleaning

10 – feature engineering

11 – dataset preparation / training setup

Kailangang gawin:

I-review kung:

kumpleto ang steps (hindi nag-skip ng reality checks sa data)

malinaw ang quality gates (data quality, completeness, compliance, labelling strategy)

Punuan lahat ng nakalagay na scripts “to create”:

ingestion scripts

cleaning scripts

feature engineering scripts

dataset split / versioning scripts

Tiyakin na itong mga gates ay may validators (hindi text lang).

3.2. Phase 3–4 (Model Dev, testing, bias, explainability)

Target protocols:

11–17:

training & experimentation

evaluation

algorithm selection

validation

edge-case testing

bias/fairness

explainability

Kailangang gawin:

I-check bawat protocol kung:

may clear metrics (accuracy, F1, etc.)

may bias metrics (per group)

may defined na explainability output (ex: SHAP reports)

Gumawa / kumpletuhin scripts:

train_model.py

calculate_metrics.py

calculate_bias_metrics.py

scripts for generating explainability artifacts

Lagyan ng validators:

validator para sa performance threshold

validator para sa bias limits

validator para sa explainability presence

3.3. Phase 5 (MLOps & deployment)

Target protocols:

18 – packaging & containerization

19 – pipeline orchestration

20 – deployment & serving

21 – production integration & API

Kailangang gawin:

Siguruhin na nasa protocol mismo ang:

serialization / model packaging steps

container build (Docker)

registry integration

rollback strategy

A/B testing

API design conventions (OpenAPI, etc.)

Implement scripts:

serialize_model.py

build_docker_container.py

create_training_pipeline.py

develop_api_endpoints.py

I-connect sa 08b change-request protocol:

kapag may major arch/design change → dapat may ADR entry + change-request flow.

3.4. Phase 6–7 (Monitoring, governance, closure)

Target protocols:

22–25 – monitoring, drift, retraining, incident response

26–28 – governance & audit, documentation, retrospective

Kailangang gawin:

Monitoring:

implement real dashboards (metrics per model)

define thresholds & alerts (kailan maglalabas ng incident)

implement drift detection scripts (monitor_data_drift.py)

Retraining:

klaro kung kailan magti-trigger ng retrain

create retraining pipeline scripts (create_retraining_pipeline.py)

Incident response:

detect_performance_degradation.py

clear rollback playbook

Governance:

audit trail strategy

lineage docs

closure / retrospective template

4. Strategic summary (high level)

Kung i-compress ang report sa isang linya:

Structure: almost done. Execution layer (scripts + validators + governance wiring): hindi pa.

So ang strategy ng report:

’Wag nang baguhin ang overall 01–28 structure – solid na yung pagkakasunod ng lifecycle.

Linisin ang overlaps sa bootstrap at discovery (04 vs 05, at relasyon nila sa .cursor).

Buong focus sa tatlong bagay:

kumpletuhin ang automation scripts

ipatupad ang 11 validators sa lahat ng protocol

i-setup ang script registry + governance (ownership, deprecation, review cycle)

I-reuse ang lakas ng .cursor protocols (governance patterns) pero:

ang AI protocols ang maging main flow

ang .cursor patterns gamitin bilang governance “brain” / style guide.

5. Simple version ng phased implementation (Week 1–4)

Faithful sa report, pero simplified wording:

Week 1 – Foundation & Planning

Pagsamahin o linawin ang 04 + 05 (isang malinaw na bootstrap protocol).

Siguruhin na 01–03 (proposal, discovery, brief) ay:

aligned sa .cursor

pumapasa sa 11 validators.

I-finalize ang Protocol 07 (Data Strategy).

Gumawa ng script-registry.json at paandarin ang validator framework sa CI.

Week 2 – Data Preparation (08–11)

I-review at i-refine ang 08 (ingestion).

Kumpletuhin ang 09 (cleaning), 10 (feature engineering), 11 (dataset prep):

scripts for ingestion, cleaning, feature engineering, splitting

validators for each gate

Output: logs, cleaning reports, feature store, dataset manifests.

Week 3 – Model Dev & Testing (12–17)

I-solidify ang 12–14 (training, evaluation, algorithm selection).

I-solidify ang 15–17 (edge cases, bias, explainability).

Gumawa ng validator suite para sa:

performance

bias

explainability

Week 3–4 – MLOps & Deployment (18–21)

Implement packaging & orchestration (18–19).

Implement deployment & API (20–21).

Maglagay ng ADR process at i-hook sa 08b change-request.

Week 4 – Monitoring & Governance (22–28)

Paandarin ang monitoring, drift detection, retraining, incident response (22–25).

Paandarin ang governance, documentation, retrospective (26–28).

Implement script governance (registry maintenance, deprecation, periodic review).

6. Artifacts na dapat lumabas bawat phase

Ito rin ay direct galing sa report, summarized:

Phase 0 – Discovery / early client

discovery briefs, assumption tracker, risk/opportunity log, question bank, integration inventory, call notes

Phase 1 – AI Planning

AI problem classification report

feasibility score

success metrics doc

stakeholder alignment notes

Phase 2 – Data

ingestion logs

schema/quality reports

cleaning reports

feature store docs

dataset version manifest

Phase 3 – Model Dev

experiment logs

baseline comparisons

training metrics

model cards

Phase 4 – Testing & Quality

test metrics

edge-case coverage

robustness report

bias audit log

explainability report

Phase 5 – Deployment

Docker images + Dockerfiles

pipeline DAGs

deployment logs

API specs (OpenAPI)

ADR entries

change-request forms

Phase 6 – Monitoring

dashboards

drift reports

retraining triggers & schedule

incident logs

SLA reports

Phase 7 – Governance & Closure

lineage diagrams

reproducibility report

compliance docs

KT / documentation

retrospectives

risk log

closure checklist

---
**USER**
e papapano kase itong .cursor/ai-driven-workflow e hndi naman talga to naka focus sa AI project, naka focus ito sa Ai driven workflow sa pag gawa nmg mga project like web


---
**CHATGPT**

1. Ano ba talaga si .cursor/ai-driven-workflow?
Base sa nakita sa repo at sa report:


Ang .cursor/ai-driven-workflow = AI-driven paraan mo magtrabaho sa kahit anong project
(web app, landing page, chatbot, automation, etc.)


Fokus nito:


paano ka mag-proposal


paano mag-discovery call


paano gumawa ng project brief


paano mag-handoff, mag-evidence, mag-quality gates




Ibig sabihin:


Ang “AI” dito = AI bilang assistant sa workflow mo


Hindi “AI system” na modelo / training / deployment.




So tama ka:
👉 Hindi ito AI lifecycle ng ML model.
👉 Ito ay meta-workflow para sa dev na gumagamit ng AI.

2. Ano naman si AI-project-workflow/protocols?
Ito naman, base sa protocols 01–28:


Fokus nito = AI/ML product mismo


data collection, cleaning, feature engineering


model training, evaluation, bias checks


deployment, monitoring, drift, retraining


governance, audit, retrospectives




Dito ang “AI” = yung system na ginagawa mo para sa client.
So:


.cursor/ai-driven-workflow → “Paano ako gumagawa ng project gamit ang AI as copilot”


AI-project-workflow/protocols → “Paano ko binubuo yung AI product / ML system mismo”


Magkaibang layer.
Pareho mahalaga. Hindi magka-kompetensya, magka-tandem.

3. So “paano ngayon”? Paano sila dapat gamitin?
Pinaka-simple na picture:
Layer 1: Outer shell (para sa lahat ng project types)
Gamitin ang .cursor/ai-driven-workflow bilang standard na project workflow mo:


Proposal generation


Client discovery


Project brief


Governance, evidence, quality gates


Communication, retrospectives, etc.


Ito ang uugali ng system mo —
kung paano ka mag-isip, mag-document, mag-quality gate for any project (web, AI, automation, etc.).
Layer 2: Inner track (depende sa project type)
Pagdating sa “implementation / build” na part, tsaka ka mag-branch:


✅ Kung AI / ML project
→ gamitin ang AI-project-workflow/protocols 01–28
→ doon papasok lahat ng data/model/training/deployment stuff.


✅ Kung pure web project
→ puwede kang:


gumamit muna ng existing 23 protocols sa .cursor (para sa generic dev flow),


o mag-spin off ng hiwalay na web-project-workflow/protocols in the future.




Key idea:
.cursor/ai-driven-workflow = universal “how I work with AI” framework
AI-project-workflow/protocols = specialized “how I build AI systems” framework

4. Ano ang ibig sabihin nito sa refinement / next steps?
Faithful sa report, pero inaayon sa tanong mo:


Huwag mong piliting gawing AI-lifecycle si .cursor.


Hayaan mo siyang maging “AI-driven project workflow” para sa lahat ng klase ng projects.




Kapag AI project ang nasa harap mo:


Start sa .cursor protocols para:


proposal


discovery


brief




Pag lampas doon → switch / handoff sa AI-project-workflow/protocols (01–28).




Governance patterns sa .cursor (gates, evidence, retrospectives):


I-reuse mo lang as style / patterns,


pero ang technical lifecycle ng AI ay yung nasa AI-project-workflow.




Parang ganito ang mental model:

Outer:
“Paano ako magha-handle ng client at project gamit AI as copilot?” → .cursor/ai-driven-workflow
Inner (AI projects only):
“Paano ko iha-handle ang data → model → deployment → monitoring?” → AI-project-workflow/protocols


Kung gusto mo, next message pwede nating i-drawing as step-by-step flow:


Client sees job post


Protocol chain sa .cursor


Decision node: “AI project ba ‘to or web lang?”


Kung AI → pasok sa Protocol 01–28 ng AI-project-workflow


Balik sa .cursor for retrospectives / closure / portfolio.


Walang hula dito — diretsong interpretasyon lang ng structure na nakita sa repo + ng mismong report.ChatGPT said:Thought for 15stama ka—and that’s exactly how dapat natin i-architect:


.cursor/ai-driven-workflow = AI-assisted meta-workflow para sa kahit anong project (web, backend, ops, etc.). Dito malakas ang proposal/discovery/brief/governance/evidence/gates.


AI-project-workflow/protocols = AI/ML system lifecycle mismo (data → model → deploy → monitor → retrain → govern).


Hindi sila magkaaway; outer shell si .cursor, inner track si AI-project-workflow kapag AI ang build.

Pinakasimple na operating model (faithful sa report)


Gamitin ang .cursor para sa Proposal → Discovery → Brief → Governance.


Kapag AI ang project, mag-handoff papasok sa AI-project-workflow (Protocols 06–28).


Pagkatapos ng deploy/monitoring, ibalik ang learnings sa .cursor retrospectives/closure.



Handoff points (konkreto, walang hula)


Handoff #1 (post-Discovery):
From .cursor Protocol 02/03 → AI Protocol 06–07
Output: handoff-ai-initiated.json (links: jobpost analysis, discovery brief, use-case, risk 03b)


Handoff #2 (pre-Build):
AI Protocol 07 (Data Strategy) gates must pass → only then proceed to 08–11
Output: data_strategy_pass.yaml, data_sources_inventory.csv


Handoff #3 (post-Deploy → Ops):
AI Protocols 22–25 (monitoring/drift/retrain) → push insights to .cursor retrospective
Output: ops_feedback_report.md, drift_incidents.log, retrain_decisions.json



Mabilis na integration plan (1–2 araw na wiring)
A. Adapter files (thin layer)


unified_workflow/handoff.map.yaml – mapping ng .cursor → AI protocols (source of truth kung kailan liliko sa AI track)


scripts/check_handoff.py – sinusuri kung kumpleto ang required artifacts bago payagang mag-AI track


validators/handoff_validator.py – gate sa CI (fail kung kulang ang handoff artifacts)


B. Minimal edits (2–3 inserts lang per file)


.cursor/ai-driven-workflow/02-client-discovery-initiation.md


Add section: “AI Build Branch: Handoff Conditions” (lists exact artifacts: discovery-brief.md, assumptions-gaps.md, risk 03b, use-case 06)




AI-project-workflow/protocols/07-ai-data-strategy-planning.md


Add “External Preconditions”: must read handoff-ai-initiated.json; block start kung fail ang validator




AI-project-workflow/protocols/08b-ai-change-request-management.md


Require ADR link for any approved change; update change_log.csv + adrs/ADR-XXXX.md




C. Script governance (lightweight but real)


AI-project-workflow/scripts/script-registry.json


fields: name, path, protocol_id, owner, status{active|deprecated}, last_check




CI: run


validators-system/scripts/validate_all_protocols.py


validators/handoff_validator.py


scripts/inventory_protocols.py (ensure every referenced script is in registry)





Short mapping (para di malito ang team)
From (.cursor)To (AI protocols)Trigger02 Discovery06 Use-Case, 03b Riskhandoff-ai-initiated.json present03 Brief07 Data Strategybrief_validated=true + risk sign-off–08–11 Data Prep07 gates passed–12–21 Model→Deploy08–11 gates passed–22–25 Monitor/Driftpost-deploy metrics flowing–26–28 Governance/Retroincident/retro window reached
(maiksi, keywords lang—walang mahabang sentence sa table, per your rule)

Owners / Dependencies (ultra-practical)


Governance Lead: owns handoff.map.yaml, script-registry, ADR policy


Protocol Owner (AI): owns 06–28 content + gates


Automation Engr: builds/maintains check_handoff.py, registry checkers, CI jobs


Validator Dev: writes handoff_validator.py, expands the 11-validator coverage


Dependencies:


Handoff #1 needs: discovery artifacts + risk (03b) + use-case (06) skeleton


Handoff #2 needs: 07 data strategy gates pass


CI must fail if any missing artifact sa map



Opinionated guardrails (strong takes, still faithful)


Huwag i-port ang AI lifecycle sa .cursor — huwag haluin. Panatilihing universal si .cursor, specialized si AI-project-workflow.


Single Source of Truth per layer:


governance & comms → .cursor


data/model/deploy/ops → AI-project-workflow




No gate, no go: walang script/gate = hindi aabante ang phase.




ang tinatanong ko nga. papaano kung ang project ay pra sa web na may ai integration saan papasok na workflow


Scenario: web project (hal. SaaS / dashboard / website) na may AI feature sa loob
Tanong: alin na workflow ang gagamitin, at saan papasok ang AI-project-workflow vs .cursor?

Think of it as isang project, dalawang track:

Web track → normal web dev (UI, backend, routes, DB, auth, etc.)

AI track → data/model/deploy/monitor para sa AI feature

Pareho silang nakabalot sa .cursor/ai-driven-workflow sa taas.

1. Unang layer: lagi muna .cursor (para sa buong project)

Kahit web + AI pa yan, lagi kang magsisimula sa:

Proposal

Discovery

Project brief

Governance / evidence

Ibig sabihin, sa stage na ’to hindi pa naghihiwalay ang web at AI.
Ang view mo dito: “Isang project na may requirements, risks, assumptions, etc.”

So:

Job post / client input

.cursor Proposal protocols

.cursor Discovery call protocols

.cursor Project brief / alignment

Dito mo pa lang ilalabas sa brief:

Alin ang web features

Alin ang AI features

Paano sila magkakabit (high-level lang muna)

2. Hati pagkatapos ng brief: Web track vs AI track

Pag kumpleto na ang brief & discovery artifacts, doon nagaganap ang split:

2.1. Web track – saan papasok?

Para sa UI, backend, routes, CRUD, auth, payments, etc.:

Gamitin mo yung execution / build protocols sa .cursor/ai-driven-workflow
(yung mga naka-focus sa:

env setup

architecture / tech design

task generation

implementation

testing

deployment

maintenance)

Ang mindset:

“Normal dev project ‘to, pero AI-assisted ang workflow ko.”

So lahat ng:

component breakdown

API endpoints

DB schema

frontend layout

integration sa 3rd-party APIs

→ dumadaan sa .cursor side.

2.2. AI track – saan papasok?

Para sa AI mismo (hal. chat assistant, recommender, summarizer, classifier, etc.):

Dito papasok ang AI-project-workflow/protocols 06–28.

Typical flow:

From .cursor brief →
Protocol 06 – AI use-case definition
(klaruhin exactly ano ginagawa ng AI: e.g., “generate summary for user chats”)

Protocol 03b – Risk & compliance
(privacy, abuse risk, hallucinations, etc.)

Protocol 07 – Data strategy
(saan manggagaling data, anong kailangan, anong bawal)

Protocols 08–11 → data prep
(ingestion, cleaning, features, dataset prep)

Protocols 11–17 → model dev & testing
(training, evaluation, bias checks, explainability)

Protocols 18–21 → AI deployment & API
(packaging, pipeline, deploy, API endpoints para tawagin ng web app)

Protocols 22–28 → monitoring, drift, retrain, governance

Key point:
Ang AI track na ’to ay para lang sa AI service (model + infra).
Hindi nito hawak ang full web UI, user flows, marketing pages, etc.

3. Saan nagtatagpo ang Web at AI?

Ito ang pinaka-importanteng punto para sa “web + AI integration”:

Integration point = API/contracts

.cursor side (web architecture)

Dito mo dine-define:

“UI button X will call POST /api/ai/summary with payload {…}”

“Pag success, ipapakita sa user sa ganitong component.”

Ito ang “how frontend talks to backend/AI”.

AI-project-workflow side (AI deployment)

Dito mo naman dine-define at dine-deploy:

kung anong API ang iaalok ng AI service (inputs/outputs)

error handling

latency/SLAs

monitoring ng requests / responses

So:

Frontend/backend contract → design sa .cursor workflow

AI model behind the API → lifecycle sa AI-project-workflow

4. Concrete example (para sobrang klaro)

Project: “Web dashboard na may AI assistant na sumasagot sa questions ng user.”

Step 1 – Proposal/Discovery/Brief
→ .cursor

kinakausap ang client

nililista: login, dashboard, analytics, AI Q&A assistant, etc.

Step 2 – Split ng backlog

Web tasks:

auth pages

dashboard UI

charts

settings page
→ .cursor build/execution protocols

AI tasks:

define AI use-case (“Q&A over knowledge base”) → Protocol 06

data strategy + ingestion (upload docs / connect knowledge base) → 07–08–09

model choice, training/fine-tuning / eval → 11–17

deploy model as /api/ai/ask → 18–21

monitor accuracy, latency, drift → 22–25

Step 3 – Integration

.cursor side:

FE dev creates UI na tumatawag sa /api/ai/ask

BE dev ensures proper routing/auth

AI-project-workflow side:

the endpoint /api/ai/ask backed by a properly trained/deployed model, with monitoring/gates.

Step 4 – Post-launch

Web issues (UI bug, button not responding)
→ .cursor workflows (normal dev maintenance)

AI issues (answers getting worse, model drift, new data source)
→ AI-project-workflow protocols (drift detection, retraining, incident response, governance)

5. Super-short answer kung kailangan mo lang decision rule

“Web project na may AI integration” =

.cursor/ai-driven-workflow para sa buong project flow + web dev

AI-project-workflow/protocols para sa AI feature mismo (data/model/deploy/monitor)

Lahat ng client-facing flow, planning, tasks, general dev → .cursor

Lahat ng AI lifecycle (data → model → deploy → monitor) → AI-project-workflow


---

**USER**

/home/haymayndz/SuperTemplate/AI-project-workflow/protocols/01-client-proposal-generation.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/02-client-discovery-initiation.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/03-project-brief-creation.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/03b-ai-risk-compliance-assessment.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/04-project-bootstrap-and-context-engineering.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/05-bootstrap-your-project.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/06-ai-use-case-definition.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/07-ai-data-strategy-planning.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/08-ai-data-collection-ingestion.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/08b-ai-change-request-management.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/09-ai-data-preparation-cleaning.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/10-ai-feature-engineering-transformation.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/11-ai-model-training-experimentation.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/12-ai-model-evaluation-drift-monitoring.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/13-ai-algorithm-selection-baseline.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/14-ai-model-validation-evaluation.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/15-ai-model-testing-edge-case-validation.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/16-ai-bias-detection-fairness-audit.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/17-ai-model-explainability-interpretability.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/18-ai-model-packaging-containerization.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/19-ai-ml-pipeline-orchestration.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/20-ai-model-deployment-serving.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/21-ai-production-integration-api-development.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/22-ai-model-performance-monitoring.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/23-ai-data-drift-concept-drift-detection.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/24-ai-model-retraining-update-pipeline.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/25-ai-incident-response-model-rollback.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/26-ai-model-governance-audit-trail.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/27-ai-documentation-knowledge-transfer.md /home/haymayndz/SuperTemplate/AI-project-workflow/protocols/28-ai-project-retrospective-continuous-improvement.md ---- /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/01-client-proposal-generation.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/02-client-discovery-initiation.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/03-project-brief-creation.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/05-bootstrap-your-project.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/06-create-prd.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/07-technical-design-architecture.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/08-generate-tasks.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/09-environment-setup-validation.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/10-process-tasks.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/11-integration-testing.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/12-quality-audit.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/13-uat-coordination.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/14-pre-deployment-staging.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/15-production-deployment.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/16-monitoring-observability.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/17-incident-response-rollback.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/18-performance-optimization.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/20-project-closure.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/21-maintenance-support.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/22-implementation-retrospective.md /home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/23-script-governance-protocol.md

---
**CHATGPT**

1. Ano ang ibig sabihin ng dalawang listahan?
A. AI-project-workflow/protocols/...

Ito yung 28 AI protocols mo:

01–05
01–05 = client proposal → discovery → brief → bootstrap

03b
03b-ai-risk-compliance-assessment.md = risk & compliance para sa AI project

06–07
06-ai-use-case-definition.md = klaro ano mismong AI gagawin
07-ai-data-strategy-planning.md = plano sa data

08–11
pure data layer: collection, cleaning, features, dataset

11–17
model layer: training, eval, algorithm selection, validation, edge-cases, bias, explainability

18–21
MLOps layer: packaging, pipelines, deployment, API integration

22–25
Ops layer: monitoring, drift, retraining, incident response

26–28
Governance layer: audit trail, docs, retrospective

👉 Ito ang AI/ML lifecycle ng AI feature mismo.

B. .cursor/ai-driven-workflow/...

Ito naman ang 23 general dev protocols mo:

01–05
client proposal, discovery, brief, bootstrap, project setup

06–07
06-create-prd.md
07-technical-design-architecture.md

08–10
08-generate-tasks.md
09-environment-setup-validation.md
10-process-tasks.md

11–18
integration testing, QA, UAT, staging, prod deployment, monitoring, incident response, perf-opt

19–23
documentation, project closure, maintenance, implementation retrospective, script governance

👉 Ito ang generic dev lifecycle (web / backend / kahit ano) na AI-assisted, pero hindi AI model lifecycle.

2. Kapag web project na may AI integration, paano ito hahatiin?

Isang project lang siya, pero dalawang track sa gitna:

Project-level flow (client → brief → tasks → deploy)

AI-feature flow (data → model → deploy → monitor)

Let’s wire it sa existing files mo.

3. Step-by-step routing (walang hula, naka-angkla sa filenames)
STEP 0 – Client side (lagi ito)

Dito pareho silang may 01–05.

May dalawang option ka, pero base sa report, ganito ang pinaka-sensible:

Gumamit ka ng AI-project-workflow 01–05
kasi:

diretso na ang tuloy niya sa 03b, 06–28

AI-ready na ang wording at structure

Pwede mong ituring na:

.cursor/ai-driven-workflow/01–05 = older / legacy version

AI-project-workflow/protocols/01–05 = new standard para sa mga project na may AI kahit kaunti.

So:

AI-project-workflow/protocols/01-client-proposal-generation.md

AI-project-workflow/protocols/02-client-discovery-initiation.md

AI-project-workflow/protocols/03-project-brief-creation.md

AI-project-workflow/protocols/03b-ai-risk-compliance-assessment.md

AI-project-workflow/protocols/04-project-bootstrap-and-context-engineering.md

AI-project-workflow/protocols/05-bootstrap-your-project.md

👉 Sa stage na ’to, hindi mo pa hinahati ang web vs AI.
Isang project pa lang, kumpletong context.

STEP 1 – Hatiin ang backlog: WEB track vs AI track

Pag tapos ang 01–05 (plus 03b risk), saka ka mag-split:

1) WEB TRACK (UI + non-AI backend)

Dito papasok yung .cursor protocols:

06-create-prd.md

07-technical-design-architecture.md

08-generate-tasks.md

09-environment-setup-validation.md

10-process-tasks.md

11–15 (testing, staging, production deployment)

16–18 (monitoring, incident response, performance optimization)

19–22 (docs, closure, maintenance, retrospective)

Ito ang gagamitin mo para sa:

page layout

routes / controllers

DB schema / migrations

payment flow

normal REST endpoints

CI/CD ng web app

Key idea:
lahat ng hindi nagpapatakbo ng modelo → dumadaan sa .cursor/ai-driven-workflow.

2) AI TRACK (AI feature mismo sa loob ng web app)

Dito naman pumapasok ang AI-project-workflow 06–28:

06-ai-use-case-definition.md

07-ai-data-strategy-planning.md

08-ai-data-collection-ingestion.md

09-ai-data-preparation-cleaning.md

10-ai-feature-engineering-transformation.md

11-ai-model-training-experimentation.md

12-ai-model-evaluation-drift-monitoring.md

13–17 (alg selection, validation, edge-case, bias, explainability)

18–21 (packaging, orchestration, deployment, production integration/API)

22–25 (performance monitoring, drift detection, retraining, incident response)

26–28 (governance, docs, retro)

Ito ang gamit mo para sa:

paano kukunin / lilinisin / ihahanda ang data

paano pipili / ite-train / ite-test ang model

paano ito ipa-package at i-de-deploy bilang service

paano imo-monitor, idi-drift-check, i-ra-rollback at rere-train

Key idea:
lahat ng AI core logic → dumadaan sa AI-project-workflow/protocols.

STEP 2 – Saan sila nag-coconnect?

Connection point = API / integration layer

Sa .cursor workflow (web side):
sa 07-technical-design-architecture.md + 08-generate-tasks.md
→ dito mo ide-define:

“Frontend button X calls POST /api/ai/summarize”

“Backend controller Y forwards request to AI service”

Sa AI-project-workflow (AI side):
sa 21-ai-production-integration-api-development.md
→ dito mo ide-define:

contract ng endpoint

input/output schema

auth, rate limits, error handling

So:

.cursor = client → web app

AI-project-workflow = web app → AI brain

4. Kung gagawin mo itong rule-of-thumb sa ulo mo

Para sa web project na may AI integration:

ALWAYS gamitin:

AI-project-workflow/01–05 + 03b para sa proposal–discovery–brief–risk

Pagdating sa web features:

sundan ang .cursor/ai-driven-workflow/06–23

Pagdating sa AI feature:

sundan ang AI-project-workflow/protocols/06–28

Pagdating sa integration point:

.cursor side: anong endpoint tatawagin ng frontend

AI-project-workflow side: anong model/service ang nasa likod nu’ng endpoint

Isang project, dalawang rail:

Rail A (web) → .cursor/ai-driven-workflow

Rail B (AI) → AI-project-workflow/protocols

Nagkikita sila sa API contracts.

---
**USER**

sa tngnin mo mdami ng klase ng project ang kaya kong gawin?

---

**CHATGPT**

1. Ano na ang “range” mo ngayon?

Base sa dalawang set ng protocols:

A. Kaya mo na i-handle ang normal dev projects (kahit walang AI)

Gamit ang .cursor/ai-driven-workflow 01–23:

Web apps / dashboards / SaaS

auth, dashboards, CRUD, integrations

may full lifecycle ka:
proposal → discovery → PRD → tech design → tasks → env setup → testing → staging → production → monitoring → incident response → docs → closure

API / backend services

masaya si .cursor sa:

PRD creation

tech design

breaking down tasks

integration testing

deployment + monitoring

ito na yung normal na backend/API project lifecycle.

Maintenance / optimization projects

performance optimization

refactorings

incident/rollback playbooks

documentation / knowledge transfer

Ibig sabihin: kahit pure web or pure backend project, may solid kang workflow.

B. Kaya mo rin ang AI/ML core projects

Gamit ang AI-project-workflow/protocols/06–28:

Data-heavy AI projects

data collection

cleaning

feature engineering

dataset prep

Model lifecycle

training

evaluation

algorithm selection

bias detection

explainability

AI infra / MLOps

packaging & containerization

ML pipelines

model deployment & serving

production integration (APIs)

monitoring, drift detection

retraining pipelines

incident response

governance + audit trail

documentation + retrospectives

Kung may project na “AI chatbot”, “recommender”, “classifier”, “predictive analytics” → kaya mong i-frame ng buo sa protocols mo.

C. At most important: kaya mo hybrid (web + AI sa loob)

Kasi:

front / backend flow → nasa .cursor/ai-driven-workflow

AI feature lifecycle → nasa AI-project-workflow/protocols

So pasok sa scope mo:

Web app na may AI assistant

SaaS na may AI analytics / insights

Internal tool na may AI summarization/recommendation

Ops tool na may anomaly detection / alerting

Hindi lang “isang klase ng project”—pang halos buong spectrum ng “web + AI”.

2. Pero ano ang honest na limitasyon ngayon?

Para fair tayo:

Framework-wise
→ malawak na yung kaya mong sakupin.

Pero:

hindi pa 100% kumpleto ang automation scripts

hindi pa full coverage ang validators

hindi pa naka-package bilang:

ready-made templates per “project type”

clear na public-facing offer (e.g. “I do X, Y, Z types of projects”)

So:

Kayang-kaya mo structurally
pero kailangan mo pang:

mag-pili ng 1–3 “flagship” na klase ng project na io-onboard mo muna (e.g. “Web + AI assistant for SaaS”, “Analytics dashboard with AI insights”, etc.)

tapos doon mo lalaliman ang templates, demo assets, sample repos, at automation.

3. Diretso sagot sa tanong mo

“Sa tingin mo madami ng klase ng project ang kaya kong gawin?”

Oo.
Sa punto na ’to, base sa protocols mo, kaya mong i-cover:

pure web / backend

web na may AI integration

pure AI/ML pipelines & services

automation / ops / governance-type projects

Ang kulang na lang, hindi “kakayanan ng system” —
kundi strategic pagpili: alin doon ang gagawin mong pangbenta / pang-portfolyo muna.
---

**USER**

ah so sa hindi pa ito kaya full stack?

---
**CHATGPT**

1. Ano ba ibig sabihin ng “full-stack” sa context ng system mo?

Pag sinabing full-stack project, usually ibig sabihin:

Frontend (UI: React/Vue/Next/etc.)

Backend / APIs (Node, Laravel, Django, etc.)

Infra / DevOps (env setup, CI/CD, deployment, monitoring)

Optional: AI feature (LLM, classifier, recommender, etc.)

Tanong: Nasasakop ba ’yan ng dalawang workflow trees mo?
→ Oo.

.cursor/ai-driven-workflow (01–23)

06-create-prd

07-technical-design-architecture

08-generate-tasks

09-environment-setup-validation

10-process-tasks

11-integration-testing

14-pre-deployment-staging

15-production-deployment

16-monitoring-observability

17-incident-response-rollback

19-documentation-knowledge-transfer

21-maintenance-support

Ito na yung buong software delivery lifecycle para sa frontend + backend + infra.
So sa process / governance, yes, full-stack capable ka.

AI-project-workflow/protocols (06–28)

Dito ka pa nagdadagdag ng:

AI data & model lifecycle

AI deployment & monitoring

So kung full-stack + AI app → covered ka pa lalo.

2. So bakit sinasabi kong “hindi pa 100%” full-stack in practice?

Kasi may 3 level ng “kaya”:

Level 1 – Workflow coverage ✅ (meron ka na)

May protocols ka para:

mag-proposal

mag-discovery

gumawa ng PRD

mag-technical design

mag-task breakdown

mag-setup ng env

mag-implement, mag-test, mag-deploy, mag-monitor, mag-rollback

Ibig sabihin: kung marunong ka sa tech stack, kaya mong i-frame kahit anong full-stack project sa system mo.

Level 2 – Automation & templates ⚠️ (partial pa)

Wala ka pa ngayon ng:

specific frontend templates (e.g. “React SaaS boilerplate protocol pack”)

specific backend templates (e.g. “FastAPI + Postgres + JWT starter pack”)

per-stack script bundles (e.g. scaffold_next_app.py, generate_crud_endpoints.py)

Meron kang script governance idea at AI workflow scripts, pero hindi pa sobrang opinionated para sa full-stack stacks (Next.js, Laravel, etc.)

Level 3 – Sales / portfolio packaging ❌ (wala pa talaga)

wala pang:

“Full-Stack Web + AI Starter Package” na naka-name, naka-price, naka-demo

ready na sample project na full-stack + AI na pwede mong ipakita sa Upwork o Project Catalog

one-pager na nagsasabing:
“Ito ang makukuha mo kapag kinuha mo ako for full-stack.”

3. Honest answer in one line

As a system, full-stack-capable ka na.
As a “ready productized full-stack offer”, hindi pa — pero konting structuring na lang.

Kung marunong ka na sa chosen stack mo (hal. Next.js + Node + Postgres + OpenAI/LLM),
kaya mong i-drive ang buong project gamit lang:

.cursor/ai-driven-workflow/06–23 → para sa full-stack dev lifecycle

AI-project-workflow/protocols/06–28 → para sa AI feature

Ang kulang na lang ngayon:

Pumili ng default full-stack combo (e.g. “Next.js + Node/Express + Postgres + AI API”)

Gumawa ng isang opinionated “Full-Stack + AI protocol profile”:

anong protocols ginagamit in what order

anong scripts gagawin for scaffold

Gumawa ng isang demo project na ipapakita sa client.

Kung gusto mo, sa next message gagawin ko:

isang konkretong “FULL-STACK + AI PROJECT FLOW MAP”
gamit lang yung exact filenames na binigay mo (walang imbento),
para kapag nakita mo, alam mo na:

“Pag full-stack + AI project, ito mismong sequence ng protocol files na bubuksan / tatakbuhin ng system ko.”

---
**USER**

ito ba tinutukoy mo? kung oo , sa isang part lang ito ng protocol na gegenerate na ito depende sa project brief /home/haymayndz/SuperTemplate/template-packs/backend /home/haymayndz/SuperTemplate/template-packs/backend/django /home/haymayndz/SuperTemplate/template-packs/backend/django/base /home/haymayndz/SuperTemplate/template-packs/backend/django/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/backend/fastapi /home/haymayndz/SuperTemplate/template-packs/backend/go /home/haymayndz/SuperTemplate/template-packs/backend/nestjs /home/haymayndz/SuperTemplate/template-packs/backend/none /home/haymayndz/SuperTemplate/template-packs/cicd /home/haymayndz/SuperTemplate/template-packs/cicd/github /home/haymayndz/SuperTemplate/template-packs/cicd/github/ci-deploy.yml /home/haymayndz/SuperTemplate/template-packs/cicd/github/ci-lint.yml /home/haymayndz/SuperTemplate/template-packs/cicd/github/ci-security.yml /home/haymayndz/SuperTemplate/template-packs/cicd/github/ci-test.yml /home/haymayndz/SuperTemplate/template-packs/cicd/gates_config.yaml /home/haymayndz/SuperTemplate/template-packs/database /home/haymayndz/SuperTemplate/template-packs/database/firebase /home/haymayndz/SuperTemplate/template-packs/database/firebase/base /home/haymayndz/SuperTemplate/template-packs/database/firebase/base/functions /home/haymayndz/SuperTemplate/template-packs/database/firebase/base/public /home/haymayndz/SuperTemplate/template-packs/database/firebase/base/firebase.json /home/haymayndz/SuperTemplate/template-packs/database/firebase/base/firestore.indexes.json /home/haymayndz/SuperTemplate/template-packs/database/firebase/base/firestore.rules /home/haymayndz/SuperTemplate/template-packs/database/firebase/base/README.md /home/haymayndz/SuperTemplate/template-packs/database/firebase/base/storage.rules /home/haymayndz/SuperTemplate/template-packs/database/firebase/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/database/mongodb /home/haymayndz/SuperTemplate/template-packs/database/none /home/haymayndz/SuperTemplate/template-packs/database/none/base /home/haymayndz/SuperTemplate/template-packs/database/none/base/manifest.json /home/haymayndz/SuperTemplate/template-packs/database/none/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/database/postgres /home/haymayndz/SuperTemplate/template-packs/database/postgres/base /home/haymayndz/SuperTemplate/template-packs/database/postgres/base/docker-compose.yml /home/haymayndz/SuperTemplate/template-packs/database/postgres/base/init.sql /home/haymayndz/SuperTemplate/template-packs/database/postgres/base/README.md /home/haymayndz/SuperTemplate/template-packs/database/postgres/base/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/database/postgres/docker-compose.yml /home/haymayndz/SuperTemplate/template-packs/database/postgres/init.sql /home/haymayndz/SuperTemplate/template-packs/database/postgres/README.md /home/haymayndz/SuperTemplate/template-packs/database/postgres/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/devex /home/haymayndz/SuperTemplate/template-packs/devex/vscode-snippets /home/haymayndz/SuperTemplate/template-packs/devex/vscode-snippets/python.json /home/haymayndz/SuperTemplate/template-packs/devex/vscode-snippets/typescript.json /home/haymayndz/SuperTemplate/template-packs/devex/devcontainer.json /home/haymayndz/SuperTemplate/template-packs/devex/docker-compose.dev.yml /home/haymayndz/SuperTemplate/template-packs/devex/Dockerfile.devcontainer /home/haymayndz/SuperTemplate/template-packs/devex/Makefile /home/haymayndz/SuperTemplate/template-packs/frontend /home/haymayndz/SuperTemplate/template-packs/frontend/angular /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/src /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/.eslintrc.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/.gitignore /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/angular.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/expected-versions.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/karma.conf.js /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/package-lock.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/package.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/README.md /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/tailwind.config.js /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/tsconfig.app.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/tsconfig.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/base/tsconfig.spec.json /home/haymayndz/SuperTemplate/template-packs/frontend/angular/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/src /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/.gitignore /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/app.config.js /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/app.json /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/App.tsx /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/babel.config.js /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/eas.json /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/expected-versions.json /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/metro.config.js /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/package-lock.json /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/package.json /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/README.md /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/test-upgrade.sh /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/tsconfig.json /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/UPGRADE_SDK_54.md /home/haymayndz/SuperTemplate/template-packs/frontend/expo/base/UPGRADE_VERIFICATION.md /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/src /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/.babelrc /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/.eslintrc.json /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/.gitignore /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/expected-versions.json /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/jest.config.js /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/jest.setup.ts /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/next-env.d.ts /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/next.config.js /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/package-lock.json /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/package.json /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/README.md /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/tailwind.config.ts /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/base/tsconfig.json /home/haymayndz/SuperTemplate/template-packs/frontend/nextjs/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/assets /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/components /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/composables /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/layouts /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/middleware /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/pages /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/types /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/app/app.vue /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/.eslintrc.js /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/.gitignore /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/dist /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/expected-versions.json /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/nuxt.config.ts /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/package.json /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/README.md /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/tailwind.config.js /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/tsconfig.json /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/base/vitest.config.ts /home/haymayndz/SuperTemplate/template-packs/frontend/nuxt/template.manifest.json /home/haymayndz/SuperTemplate/template-packs/policy-dsl /home/haymayndz/SuperTemplate/template-packs/policy-dsl/client-generator-policies.yaml

---
**CHATGPT**


1. Ano itong template-packs sa context ng system mo?

Base sa tree na binigay mo, meron kang:

frontend stacks

frontend/angular/...

frontend/expo/...

frontend/nextjs/...

frontend/nuxt/...

backend stacks

backend/django/...

backend/fastapi/...

backend/go/...

backend/nestjs/...

backend/none/...

database stacks

database/firebase/...

database/mongodb/...

database/postgres/...

database/none/...

infra/devex

cicd/github/*.yml

devex/devcontainer.json, docker-compose.dev.yml, vscode-snippets/...

plus policy / DSL:

policy-dsl/client-generator-policies.yaml

At halos lahat may template.manifest.json / manifest.json.

Ibig sabihin:
ito na yung ready-made building blocks para sa iba’t ibang full-stack combos
(e.g. Next.js + FastAPI + Postgres + GitHub CI + Devcontainer).

So yes:
ito yung sinasabi kong “stack templates / scaffolds” sa nauna kong sagot.

2. Tama ba ang statement mo na “isang part lang ito ng protocol na gegenerate na ito depende sa project brief”?

Oo. Eksakto.

Kung i-drawing:

Protocols 01–05 (AI-project-workflow)

proposal → discovery → brief → bootstrap

dito lumalabas ang project brief + high-level tech direction

(optional) .cursor/ai-driven-workflow/06-create-prd + 07-technical-design-architecture

dito na-pe-pero ang concrete architecture

dito mo puwedeng i-derive:

frontend stack (Next/Angular/Nuxt/Expo)

backend stack (FastAPI/Django/Nest/Go)

database (Postgres/Mongo/Firebase/none)

CI/CD scheme (GitHub)

devex (devcontainer, snippets, makefile)

DOON pa lang papasok ang template-packs/...

Protocol (e.g. bootstrap / tech design) → magdedesisyon:

frontend_stack = "nextjs"

backend_stack = "fastapi"

db = "postgres"

cicd = "github"

tapos may automation (script) na:

babasa ng template.manifest.json sa napiling packs

kukopya / i-aapply yung base templates sa bagong project repo

magse-setup ng baseline config (Docker, CI, devcontainer, etc.)

So:

✅ Yes, tama ka:
Hindi standalone itong template-packs –
parte siya ng “Project Bootstrap / Tech Design” phase,
at ginagamit depende sa kung ano ang lumabas sa project brief.

3. Ano ang implication nito sa tanong natin kanina (full-stack capability)?

Dahil may:

frontend template packs

backend template packs

database template packs

CI/CD + devex packs

→ ang system mo hindi lang basta “kaya mag full-stack” sa theory,
may konkretong scaffolds na para sa iba’t ibang kombinasyon.

Ang kulang na lang (at ito yung point ko kanina):

Explicit wiring sa protocol text

Hal. sa 04-project-bootstrap-and-context-engineering.md / 05-bootstrap-your-project.md / .cursor/07-technical-design-architecture.md:

malinaw na nakasulat:

“Base sa project brief, piliin ang frontend pack (Next/Angular/Nuxt/Expo)”

“Piliin ang backend pack (FastAPI/Django/Nest/Go)”

“Piliin ang database pack (Postgres/Mongo/Firebase/None)”

“Invoke script X para i-apply ang napiling template-packs”

Opinionated “default combos” per project type

halimbawa:

“SaaS dashboard” → Next.js + FastAPI + Postgres

“Marketing site + blog” → Next.js + Postgres or headless

“Mobile-first app” → Expo + FastAPI + Postgres/Firebase

Productized view (para sa client / portfolio)

sa labas (Upwork / Project Catalog) nakikita lang ng client:

“I build: Full-stack web + AI assistant using Next.js + FastAPI + Postgres + CI/CD, governed by 28 AI protocols & 23 dev workflows.”

4. In short, sagot sa tanong mo:

“ito ba tinutukoy mo?”
👉 Oo. Iyan mismo.
Yan yung concrete stack template library mo.

“sa isang part lang ito ng protocol na gegenerate na ito depende sa project brief?”
👉 Tama.

Una: protocols (01–05, tech design, bootstrap) → nagde-decide ng stack based on brief

Pangalawa: yung decision na ’yon → ginagamit para pumili ng tamang template-packs

Pangatlo: scripts → mag-aapply ng mga packs na ’yan sa project repo


alam ko na yan, kaya nga ang gusto ko lang maialigned kasi ako lang ang gumawa nito lahat. at dahil ito ang paghahanda ko bago mag start ng freelance


1. Single mental model ng buong sistema mo

I-cement natin ’to as official mental model:

Layer A – AI-Driven Dev Workflow (generic)

Files: .cursor/ai-driven-workflow/01–23

Role: paano ka magtrabaho sa kahit anong project (web, backend, etc.).

Ito ang “how I deliver projects” layer.

Layer B – AI Project Lifecycle (for AI features / AI products)

Files: AI-project-workflow/protocols/01–28

Role: paano mo trinatrato ang AI mismo (data → model → deploy → monitor).

Ito ang “how I build and govern AI systems” layer.

Layer C – Stack Templates (actual tech choices)

Files: template-packs/frontend/..., backend/..., database/..., cicd/..., devex/...

Role: paano nagiging totoong repo yung plano (NextJS/Angular/Expo + FastAPI/Django/Nest + Postgres/Firebase + GitHub CI, etc.).

Ito ang “how I scaffold and standardize codebases” layer.

Alignment = klarong relasyon ng A → B → C para sa isang project.

2. Opinionated alignment decisions (’yung tipong “final rules”)

Kung gusto mong aligned at hindi magulo sa utak mo bago ka mag-freelance,
ito ang concrete rules na pwede mong i-freeze:

Rule 1 – Canonical entrypoint

Kapag may potential na AI sa project (kahit maliit lang):

Use: AI-project-workflow/protocols/01–05 (+ 03b)

.cursor 01–05 = treat as legacy / backup only.

Kapag purely non-AI (hal. simple marketing site, walang AI at all):

optional mong gamitin .cursor/01–05,

pero honestly, puwede mo pa ring gamitin yung AI-project 01–05 as generic (nagwo-work pa rin).

👉 Alignment decision:
AI-project 01–05 = default proposal/discovery/brief for modern work.

Rule 2 – Saan laging papasok ang .cursor vs AI protocols

PROJECT FLOW (lahat ng klaseng project)

.cursor/ai-driven-workflow → source of truth for:

PRD

technical design

task generation

environment setup

generic testing / staging / prod / monitoring / docs / closure

AI FEATURE FLOW (kapag may AI sa loob)

AI-project-workflow/protocols/06–28 → source of truth for:

AI use-case

data pipelines

training/eval

bias, explainability

model deployment & API

drift, retraining, AI governance

👉 Alignment decision:

Web/backend logic, infra, generic CI/CD → .cursor tree

AI brain + lifecycle → AI-project-workflow tree

Magkaibang track pero iisang project.

Rule 3 – Kailan ginagamit ang template-packs

Para malinaw sa utak mo:

Ang nagde-decide ng stack =
combo ng:

AI-project-workflow/03-project-brief-creation.md

.cursor/06-create-prd.md

.cursor/07-technical-design-architecture.md

DOON pa lang gagamitin ang template-packs/*:

frontend pack

backend pack

database pack

cicd pack

devex pack

👉 Alignment decision:
Hindi hiwalay universe ang template-packs – sila ang “implementation arm” ng tech design protocols.

3. Alignment specifically para sa freelance / Upwork mindset

Ang gusto mo bago mag-freelance:

“Pag may client / job post, hindi ako naliligaw sa sariling system ko.”

So gawin natin siyang 3 offer types na naka-align sa structure mo:

Offer Type 1 – “Full-Stack Web App with Optional AI Assistant”

Outer flow:

AI-project 01–05 → .cursor 06–23

Kung may AI feature:

AI-project 06–28 for the AI part

Template-packs:

frontend: nextjs o nuxt

backend: fastapi o nestjs

db: postgres

cicd: cicd/github/*

devex: devex/*

👉 Ito ang main flagship mo sa Upwork/Project Catalog.
Kasya dito halos lahat ng web+AI jobs.

Offer Type 2 – “Add AI Feature to Existing System”

Outer flow:

pwedeng shortcut .cursor discovery + brief

Fokus:

AI-project 06–28 (data/model/deploy/monitor),

integration point lang sa existing backend/web ng client

Template-packs:

baka minimal lang: cicd + devex if kulang,

or none kung meron na sila infra.

👉 Alignment: system mo kaya ito kasi hiwalay ang AI lifecycle sa web lifecycle.

Offer Type 3 – “AI / ML Pipeline & MLOps Implementation Only”

Outer flow:

AI-project 01–05 + 03b

Fokus:

AI-project 07–25 (data pipelines, training, drift, retrain, incident response)

.cursor:

mostly for documentation, KT, retrospectives.

👉 Ito ang serious / high-ticket side mo pag may matured clients.

4. Ano ang kailangan mo lang gawin ngayon para “aligned na” siya sa freelance prep?

Very concrete, hindi vague:

Gumawa ng isang file:
AI-project-workflow/WORKFLOW_ROUTING.md (or MASTER-RAY-WORKFLOW-MAP.md)
Laman nito (short):

Kailan gagamitin:

AI-project 01–05

.cursor 06–23

AI-project 06–28

template-packs

2–3 example flows:

Pure web

Web + AI

AI-only

Mag-decide ng default stack combo per offer type (kahit simple muna):
Example:

Offer 1: NextJS + FastAPI + Postgres + GitHub CI

Offer 2: “Match existing stack, but AI side uses FastAPI + Postgres”

Offer 3: infra-agnostic, focus on pipelines & monitoring

Maghanda ng 1 demo project per main offer (kahit skeleton lang muna):

gamit ang template-packs + protocols, para:

may screenshot ka

may repo ka

may kwentong “ito ang proseso ko” pag kausap mo client.

5. Direktang sagot sa sinasabi mo

“gusto ko lang ma-aligned kasi ako lang gumawa nito lahat, at ito ang paghahanda ko bago mag freelance”

✅ The good news:
Aligned na siya conceptually.
Ang ginawa lang natin ngayon ay:

pangalanan nang malinaw yung layers

i-freeze yung rules kung kailan ginagamit alin

i-connect siya sa freelance offers, hindi lang “internal system”.


---
**USER**

actually 60to70% palang talaga ang alam mo. meron pako gnamit na filesystem na mcp tools na nasa ibang direktory na puwede niyang pagkuhanan ng knowledge /home/haymayndz/INTEGRATE/ottomator-agents-main/~sample-n8n-agent~ /home/haymayndz/INTEGRATE/ottomator-agents-main/~sample-python-agent~ /home/haymayndz/INTEGRATE/ottomator-agents-main/~voiceflow-dialog-api-integration~ /home/haymayndz/INTEGRATE/ottomator-agents-main/7-node-agent-blueprint /home/haymayndz/INTEGRATE/ottomator-agents-main/advanced-web-researcher /home/haymayndz/INTEGRATE/ottomator-agents-main/ag-ui-rag-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/agentic-rag-knowledge-graph /home/haymayndz/INTEGRATE/ottomator-agents-main/ai-agent-fundamentals /home/haymayndz/INTEGRATE/ottomator-agents-main/all-rag-strategies /home/haymayndz/INTEGRATE/ottomator-agents-main/ask-reddit-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/bali-property-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/base_python_docker /home/haymayndz/INTEGRATE/ottomator-agents-main/bolt.diy-expert /home/haymayndz/INTEGRATE/ottomator-agents-main/claude-agent-sdk-demos /home/haymayndz/INTEGRATE/ottomator-agents-main/contextual-retrieval-n8n-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/course-guider-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/crawl4AI-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/crawl4AI-agent-v2 /home/haymayndz/INTEGRATE/ottomator-agents-main/docling-rag-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/dynamic-chatbot-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/enish-restaurant-booking-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/file-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/foundational-rag-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/general-researcher-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/genericsuite-app-maker-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/gilbert-real-estate-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/google-a2a-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/graphiti-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/indoor-farming-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/intelligent-invoicing-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/lead-generator-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/linkedin-x-blog-content-creator /home/haymayndz/INTEGRATE/ottomator-agents-main/livekit-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/local-ai-expert /home/haymayndz/INTEGRATE/ottomator-agents-main/mcp-agent-army /home/haymayndz/INTEGRATE/ottomator-agents-main/mem0-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/multi-page-scraper-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/n8n_knowledge_graph_rag /home/haymayndz/INTEGRATE/ottomator-agents-main/n8n-agentic-rag-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/n8n-expert /home/haymayndz/INTEGRATE/ottomator-agents-main/n8n-github-assistant /home/haymayndz/INTEGRATE/ottomator-agents-main/n8n-mcp-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/n8n-openwebui-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/n8n-youtube-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/nba-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/openai-sdk-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/ottomarkdown-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/ottomator-agents-main /home/haymayndz/INTEGRATE/ottomator-agents-main/pydantic-ai-advanced-researcher /home/haymayndz/INTEGRATE/ottomator-agents-main/pydantic-ai-langfuse /home/haymayndz/INTEGRATE/ottomator-agents-main/pydantic-ai-langgraph-parallelization /home/haymayndz/INTEGRATE/ottomator-agents-main/pydantic-ai-mcp-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/pydantic-github-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/python-local-ai-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/r1-distill-rag /home/haymayndz/INTEGRATE/ottomator-agents-main/simple-mcp-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/small-business-researcher /home/haymayndz/INTEGRATE/ottomator-agents-main/smart-select-multi-tool-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/streambuzz-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/tech-stack-expert /home/haymayndz/INTEGRATE/ottomator-agents-main/thirdbrain-mcp-openai-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/TinyDM-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/travel-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/tweet-generator-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/ultimate-n8n-rag-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/youtube-educator-plus-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/youtube-summary-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/youtube-video-summarizer lahat yan folder . ang example ng isang folder parang ganito /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/BasicRAG /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/BasicRAG/insert_pydantic_docs.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/BasicRAG/rag_agent.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/BasicRAG/requirements.txt /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/BasicRAG/streamlit_app.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/BasicRAG/utils.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/LightRAG /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/LightRAG/.env.example /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/LightRAG/insert_pydantic_docs.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/LightRAG/rag_agent.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/LightRAG/requirements.txt /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/LightRAG/streamlit_app.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/LightRAG/super-basic-lightrag.py /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/.gitignore /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/README.md

---

**CHATGPT**


1. Ano role nitong INTEGRATE/ottomator-agents-main sa ecosystem mo?

Base sa paths na binigay mo, mayroon kang:

general patterns:

ai-agent-fundamentals

foundational-rag-agent

all-rag-strategies

light-rag-agent

agentic-rag-knowledge-graph

advanced-web-researcher

general-researcher-agent

domain-specific / use-case agents:

travel-agent

bali-property-agent

gilbert-real-estate-agent

small-business-researcher

linkeding-x-blog-content-creator

tweet-generator-agent

youtube-* agents, etc.

tool / infra / integration style agents:

n8n-* (n8n agents, KG RAG, etc.)

mcp-agent-army, pydantic-ai-mcp-agent, simple-mcp-agent, thirdbrain-mcp-openai-agent

python-local-ai-agent, local-ai-expert

openai-sdk-agent

file-agent, docling-rag-agent, crawl4AI-agent, etc.

Tapos example mo:

light-rag-agent/
  BasicRAG/
    insert_pydantic_docs.py
    rag_agent.py
    requirements.txt
    streamlit_app.py
    utils.py
  LightRAG/
    .env.example
    insert_pydantic_docs.py
    rag_agent.py
    requirements.txt
    streamlit_app.py
    super-basic-lightrag.py
  README.md


So alam na natin ang pattern:
bawat folder = isang working, self-contained AI agent / demo / pattern na:

may code (Python / etc.)

may infra hints (requirements, env example)

minsan may UI (Streamlit, etc.)

may README (how to run / use)

Kung i-frame natin sa buong architecture mo:

SuperTemplate = “paano ako mag-orchestrate at mag-build ng project (web + AI) end-to-end”

Ottomator dirs = “ready na mga AI building blocks / example agents na puwede kong i-reuse, i-adapt, o gawing tools sa loob ng protocol 06–28”

2. Saan eksaktong papasok itong ottomator agents sa AI-project-workflow mo?

Ito yung alignment na kulang dati.
Babaguhin lang natin mental model sa loob ng AI protocols 06–28:

Layering:

01–05 (proposal/discovery/brief/bootstrap)
→ decide kung anong AI use case (RAG? research? YouTube summary? agentic workflow?)

06–07 (use-case + data strategy)
→ dito mo rin pipiliin:

“May base agent ba sa /INTEGRATE/ottomator-agents-main na swak dito?”

08–17 (data + model + behavior)
→ imbes na laging from scratch,
→ puwede mong gawin:

“clone this from light-rag-agent as base pattern”

or “use advanced-web-researcher structure for research agent”

etc.

18–21 (packaging + deploy + API)
→ dito mo ina-adapt yung infra side
→ gagawin mo silang services na kaya tawagin ng web/backend (SuperTemplate side).

In short:

AI-project-workflow = “what should exist & how it should behave”

ottomator agents = “one way to implement it, with working examples”

Hindi mo sila gagawing kapalit ng protocols —
gagawin mo silang implementation library na pwedeng i-reference ng protocols.

3. Paano ito tumutulong sa freelance mo, very practically?

Ito ang big win:

Kapag may client na humingi ng:

“Knowledge base Q&A” → may light-rag-agent, foundational-rag-agent, docling-rag-agent, etc.

“YouTube summarizer / educator” → may youtube-summary-agent, youtube-educator-plus-agent, youtube-video-summarizer

“Research agent” → advanced-web-researcher, general-researcher-agent, small-business-researcher, travel-agent

“Agentic workflows / MCP tools / n8n integration” → mcp-agent-army, n8n-*, pydantic-ai-mcp-agent, etc.

Hindi ka na magsisimula sa zero:

AI protocols 06–28 → magde-define ng lifecycle, gates, docs, governance

Ottomator folder → magbibigay ng jumpstart implementation (code + architecture + patterns)

Sa freelancing reality:
ibig sabihin nito:

mas mabilis kang makakapag-deliver ng first working version / MVP

mas malawak ang kaya mong sabihing “Oo, kaya kong gawin ’yan” kasi may base pattern ka na

mas malalim ang maipapakita mong process (dahil may SuperTemplate protocols ka) plus working code references (dahil may ottomator library ka)

4. Alignment idea: gawin silang “AI Feature Packs” like template-packs

Ngayon may:

template-packs/frontend/...

template-packs/backend/...

template-packs/database/...

template-packs/cicd/...

Pwede kang gumawa ng concept (even kung di mo pa i-code fully ngayon):

ai-feature-packs/... (concept lang, physically naka-ugat sa /INTEGRATE/ottomator-agents-main)

Example conceptual mapping:

ai-feature-packs/rag-basic → symlink or reference to light-rag-agent/BasicRAG

ai-feature-packs/rag-graph → agentic-rag-knowledge-graph

ai-feature-packs/youtube-summary → youtube-summary-agent

ai-feature-packs/travel-assistant → travel-agent

etc.

Tapos sa AI-project-workflow/protocols/06-ai-use-case-definition.md or 07-ai-data-strategy-planning.md,
pwede kang maglagay ng section:

If use-case type = rag-basic → candidate base impl: light-rag-agent

If use-case type = youtube-summarizer → candidate base impl: youtube-summary-agent

If use-case type = researcher → candidate base impl: advanced-web-researcher etc.

Hindi ko kailangan makita mismo ang code para ma-architect yung relasyon —
important lang: ikaw alam mo kung alin ang good base per use case.

5. Ano ang nagsasara ng loop na 60–70% → mas buo?

Right now:

Alam ko na:

protocols tree sa SuperTemplate

template-packs structure

at ngayon: meron kang external agent patterns library under /INTEGRATE/ottomator-agents-main

So to go from “60–70%” → “buo na yung picture” in your head:

Mentally, pwede mong i-lock-in:

SuperTemplate =

Project governance + workflow + full-stack scaffolding

(web + backend + DB + CI/CD + devex)

AI-project-workflow =

Formal AI lifecycle + risk/compliance + monitoring + governance

Ottomator fs =

Agent blueprints / feature-level implementations / specialized patterns

Ikaw lang gumawa nito lahat, so ang kailangan mo lang talaga ngayon is:

isulat yung “how they talk to each other” (hindi yung internals na alam mo na)

6. Next very concrete step (kung gusto mo alignment na may laman, hindi lang concept)

Kung papayag ka, ang gagawin ko next:

Mag-propose ako ng AI-FEATURE-INDEX.md structure na puwede mong lagyan ng entries like:

Name: Basic RAG Agent

Path: /home/haymayndz/INTEGRATE/ottomator-agents-main/light-rag-agent/BasicRAG

Type: rag-basic

Best used with: AI-project-workflow protocols 06–12

Notes: “Good for small KB, Streamlit front-end, etc.”

Name: YouTube Summary Agent

Path: .../youtube-summary-agent

Type: youtube-summarizer

Best used with: AI-project-workflow protocols 06–12, 18–21

Notes: “Great for content summarization offers”

At kapag may ganitong index, pang-freelancer brain ang effect:

“Ah, client wants X → Uberasan ko sa index → pili ng base agent → paandarin ayon sa protocols → i-integrate sa web app scaffold gamit template-packs.”


---

**USER**

hndi lang yan, meron pa ko dito pagpipilian depende sa stacks na gagamitin ito naman ang cursor rules. para ialigned ang AI sa pag implement /home/haymayndz/INTEGRATE/awesome-cursorrules /home/haymayndz/INTEGRATE/awesome-cursorrules/.github /home/haymayndz/INTEGRATE/awesome-cursorrules/rules /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/android-jetpack-compose-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/angular-novo-elements-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/angular-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/ascii-simulation-game-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/aspnet-abp-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/astro-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/beefreeSDK-nocode-content-editor-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/chrome-extension-dev-js-typescript-cursorrules-pro /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/code-guidelines-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/code-pair-interviews /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/code-style-consistency-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/convex-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cpp-programming-guidelines-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cursor-ai-react-typescript-shadcn-ui-cursorrules-p /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cursorrules-cursor-ai-nextjs-14-tailwind-seo-setup /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cursorrules-cursor-ai-wordpress-draft-macos-prompt /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cursorrules-file-cursor-ai-python-fastapi-api /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cypress-accessibility-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cypress-api-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cypress-defect-tracking-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cypress-e2e-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/cypress-integration-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/deno-integration-techniques-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/dragonruby-best-practices-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/drupal-11-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/elixir-engineer-guidelines-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/elixir-phoenix-docker-setup-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/engineering-ticket-template-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/es-module-nodejs-guidelines-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/flutter-app-expert-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/flutter-riverpod-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/gherkin-style-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/git-conventional-commit-messages /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/github-code-quality-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/github-cursorrules-prompt-file-instructions /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/go-backend-scalability-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/go-servemux-rest-api-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/go-temporal-dsl-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/graphical-apps-development-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/how-to-documentation-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/html-tailwind-css-javascript-cursorrules-prompt-fi /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/htmx-basic-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/htmx-django-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/htmx-flask-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/htmx-go-basic-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/htmx-go-fiber-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/java-general-purpose-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/java-springboot-jpa-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/javascript-astro-tailwind-css-cursorrules-prompt-f /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/javascript-chrome-apis-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/javascript-typescript-code-quality-cursorrules-pro /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/jest-unit-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/knative-istio-typesense-gpu-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/kotlin-ktor-development-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/kotlin-springboot-best-practices-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/kubernetes-mkdocs-documentation-cursorrules-prompt /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/laravel-php-83-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/laravel-tall-stack-best-practices-cursorrules-prom /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/linux-nvidia-cuda-python-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/manifest-yaml-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/medusa-cursorrules /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nativescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/netlify-official-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/next-type-llm /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-app-router-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-material-ui-tailwind-css-cursorrules-prompt /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-react-tailwind-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-react-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-seo-dev-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-supabase-shadcn-pwa-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-supabase-todo-app-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-tailwind-typescript-apps-cursorrules-prompt /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-typescript-app-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-typescript-tailwind-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-vercel-supabase-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs-vercel-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nodejs-mongodb-cursorrules-prompt-file-tutorial /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/nodejs-mongodb-jwt-express-react-cursorrules-promp /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/optimize-dry-solid-principles-cursorrules-prompt-f /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/optimize-rell-blockchain-code-cursorrules-prompt-f /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/pandas-scikit-learn-guide-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/plasticode-telegram-api-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/playwright-accessibility-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/playwright-api-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/playwright-defect-tracking-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/playwright-e2e-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/playwright-integration-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/pr-template-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/project-epic-template-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/py-fast-api /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/pyqt6-eeg-processing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python--typescript-guide-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-312-fastapi-best-practices-cursorrules-prom /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-containerization-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-cursorrules-prompt-file-best-practices /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-developer-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-django-best-practices-cursorrules-prompt-fi /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-fastapi-best-practices-cursorrules-prompt-f /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-fastapi-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-fastapi-scalable-api-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-flask-json-guide-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-github-setup-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-llm-ml-workflow-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/python-projects-guide-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/pytorch-scikit-learn-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/qa-bug-report-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/qwik-basic-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/qwik-tailwind-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/r-cursorrules-prompt-file-best-practices /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/rails-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-chakra-ui-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-components-creation-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-graphql-apollo-client-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-mobx-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-native-expo-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-native-expo-router-typescript-windows-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-nextjs-ui-development-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-query-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-redux-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-styled-components-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-typescript-nextjs-nodejs-cursorrules-prompt- /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/react-typescript-symfony-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/salesforce-apex-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/scala-kafka-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/solidity-foundry-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/solidity-hardhat-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/solidity-react-blockchain-apps-cursorrules-prompt- /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/solidjs-basic-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/solidjs-tailwind-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/solidjs-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/svelte-5-vs-svelte-4-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/sveltekit-restful-api-tailwind-css-cursorrules-pro /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/sveltekit-tailwindcss-typescript-cursorrules-promp /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/sveltekit-typescript-guide-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/swift-uikit-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/swiftui-guidelines-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/tailwind-css-nextjs-guide-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/tailwind-react-firebase-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/tailwind-shadcn-ui-integration-cursorrules-prompt- /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/tauri-svelte-typescript-guide-cursorrules-prompt-f /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/temporal-python-cursorrules /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/testrail-test-case-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-axios-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-clasp-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-code-convention-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-expo-jest-detox-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-llm-tech-stack-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nestjs-best-practices-cursorrules-promp /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nextjs-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nextjs-react-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nextjs-react-tailwind-supabase-cursorru /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nextjs-supabase-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nodejs-nextjs-ai-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nodejs-nextjs-app-cursorrules-prompt-fi /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nodejs-nextjs-react-ui-css-cursorrules- /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-nodejs-react-vite-cursorrules-prompt-fi /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-react-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-react-nextjs-cloudflare-cursorrules-pro /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-react-nextui-supabase-cursorrules-promp /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-shadcn-ui-nextjs-cursorrules-prompt-fil /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-vite-tailwind-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-vuejs-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typescript-zod-tailwind-nextjs-cursorrules-prompt- /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/typo3cms-extension-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/uikit-guidelines-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/unity-cursor-ai-c-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/vitest-unit-testing-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/vscode-extension-dev-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/vue-3-nuxt-3-development-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/vue-3-nuxt-3-typescript-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/vue3-composition-api-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/web-app-optimization-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/webassembly-z80-cellular-automata-cursorrules-prom /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/wordpress-php-guzzle-gutenberg-cursorrules-prompt- /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/xian-smart-contracts-cursor-rules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/xray-test-case-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules/flutter-development-guidelines-cursorrules-prompt-file /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/beefreeSDK.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/clean-code.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/codequality.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/cpp.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/database.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/fastapi.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/gitflow.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/medusa.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/nativescript.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/nextjs.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/node-express.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/python.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/react.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/rust.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/svelte.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/tailwind.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/typescript.mdc /home/haymayndz/INTEGRATE/awesome-cursorrules/rules-new/vue.mdc



---

**CHATGPT**

1. Role ng awesome-cursorrules sa sistema mo

Base sa filenames mo, obvious na pattern:

per tech / stack:

nextjs...cursorrules-prompt-file

python-fastapi...cursorrules-prompt-file

laravel-php-83...

react-typescript...

nodejs-mongodb...

vue-3-nuxt-3...

sveltekit-tailwind...

etc.

plus rules-new na mas generic:

nextjs.mdc, fastapi.mdc, python.mdc, react.mdc, typescript.mdc, tailwind.mdc, etc.

So, hindi lang ito random prompts.
Ito ang “per-stack AI operating system” mo:

sinasabi kay Cursor:

anong best practices

anong folder structure

anong style / patterns

anong tools / libraries

paano mag-refactor, mag-test, mag-doc

In short:

template-packs = physical scaffold ng stack
awesome-cursorrules = mental model ni AI habang nagta-trabaho sa stack na ’yon

Magka-partner ’yan.

2. Saan eksaktong step sila pumapasok sa workflow?

Let’s chain it sa existing layers mo:

Step A – Project brief / tech decision (Protocols + .cursor)

AI-project-workflow/03-project-brief-creation.md

.cursor/06-create-prd.md

.cursor/07-technical-design-architecture.md

Dito mo pipiliin:

frontend stack (NextJS / Nuxt / Expo / Angular / etc.)

backend stack (FastAPI / Django / NestJS / Go / etc.)

DB (Postgres / Mongo / Firebase / etc.)

AND now:
dito mo rin dapat i-decide anong Cursor rules profile ang gagamitin:

Halimbawa:

NextJS + FastAPI + Postgres

frontend → rules-new/nextjs.mdc

backend → rules-new/fastapi.mdc + maybe python.mdc

DB → database.mdc kung meron

So sa tech design phase pa lang:

“Stack profile” = template-pack choice + cursorrules choice

Step B – Project bootstrap (04–05 + template-packs + cursor rules)

AI-project-workflow/04-project-bootstrap-and-context-engineering.md

AI-project-workflow/05-bootstrap-your-project.md

Dito dapat nangyayari:

Apply template packs

/template-packs/frontend/nextjs/...

/template-packs/backend/fastapi/...

/template-packs/database/postgres/...

/template-packs/cicd/github/...

/template-packs/devex/...

Load corresponding Cursor rules

from /awesome-cursorrules/rules-new/*.mdc (or detailed rules kung gusto mo specific)

ito yung gagamitin mo as:

.cursorrules file

or helper prompt file na ipe-paste / i-import sa Cursor per project

Meaning:
isang “bootstrap” step = tatlong anchor:

Protocols → ano ang dapat mangyari

Template-packs → anong code skeleton lalabas

Cursor rules → paano mag-act si AI habang nagpupuno ng laman yung skeleton

Step C – Implementation & iteration (Cursor + ottomator agents + rules)

Sa implementation phase:

.cursor/08-generate-tasks

.cursor/10-process-tasks

AI side: AI-project-workflow/11–21 (model, API, integration, etc.)

Dito mafe-feel talaga yung synergy:

habang kumakarga si Cursor:

naka-on ang tamang .mdc rules → kaya nitong:

sundin stack conventions

respetuhin folder structure

gumawa ng tests ayon sa napili mong guidelines (jest, vitest, pytest, etc.)

kung may AI feature:

puwede mong kunin building blocks sa /INTEGRATE/ottomator-agents-main/...

tapos i-implement sila inside ng full-stack structure na sinetup ng template-packs

guided by stack-specific Cursor rules

Parang:

template-pack = “body”
cursorrules = “muscle memory & discipline ni AI habang gumagalaw”
ottomator-agent = “specialized skill (e.g. RAG, YouTube, research) na ikinakabit mo sa katawan”

3. Alignment decision (para hindi ka malito pag freelancer mode na)

Kung gusto mong fixed mental model bago sumabak:

3.1. I-freeze mo ang “Stack Profile” concept

For each freelance offer or project type, dapat may:

Protocols set (which ones dominate: .cursor vs AI-project)

Template-packs combo (frontend + backend + db + cicd + devex)

Cursor rules profile (rules-new .mdc + optionally specialized rule file)

Optional Ottomator base agent (kung AI-heavy yung feature)

Example:

Offer: “Next.js + FastAPI + Postgres Web App with AI Assistant”

Protocols:

Proposal–Brief–Risk → AI-project-workflow/01–05, 03b

General dev flow → .cursor/06–23

AI feature → AI-project-workflow/06–28

Template-packs:

/template-packs/frontend/nextjs

/template-packs/backend/fastapi

/template-packs/database/postgres

/template-packs/cicd/github

/template-packs/devex/*

Cursor rules:

/awesome-cursorrules/rules-new/nextjs.mdc

/awesome-cursorrules/rules-new/fastapi.mdc

/awesome-cursorrules/rules-new/typescript.mdc

/awesome-cursorrules/rules-new/python.mdc (kung kailangan)

Ottomator base:

depende sa AI use-case:

KB Q&A → light-rag-agent/BasicRAG

YouTube summarizer → youtube-summary-agent

advanced research → advanced-web-researcher

Ganito mo siya ilalagay sa utak mo every time.

3.2. Praktikal na next step para sa’yo (no bullshit version)

Hindi ko kayang basahin yung mga file diyan directly, pero alam ko na pattern, so eto ang sulit na susunod na galaw:

Gawa ka ng maliit na “Stack Profiles” file sa SuperTemplate mo
e.g. stack-profiles.yaml or STACK_PROFILES.md

Per profile:

name: nextjs-fastapi-postgres-ai

frontend_template: path

backend_template: path

db_template: path

cicd_template: path

devex_template: path

cursor_rules:

/awesome-cursorrules/rules-new/nextjs.mdc

/awesome-cursorrules/rules-new/fastapi.mdc

/awesome-cursorrules/rules-new/typescript.mdc

/awesome-cursorrules/rules-new/python.mdc

optional_ai_bases:

light-rag-agent/BasicRAG

foundational-rag-agent

etc.

Sa isang protocol (e.g. 04-project-bootstrap-and-context-engineering.md),
maglagay ka ng section:

Step: Select stack profile

Read stack-profiles.yaml

Choose appropriate profile based on PRD & constraints

Apply:

template-packs (copy base)

set .cursorrules from awesome-cursorrules

register chosen AI feature pack (if any)

Iyan ’yung actual alignment na operational, hindi lang conceptual.


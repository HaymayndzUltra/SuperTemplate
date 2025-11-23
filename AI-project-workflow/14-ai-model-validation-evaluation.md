# PROTOCOL 14: AI MODEL VALIDATION & EVALUATION

**Version**: v1.0.0 | **Phase**: Phase 4 – Model Testing & Quality (per AGENTS.md) | **Status**: Draft

---

## PREREQUISITES

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: prerequisites / integration_points / compliance_standards
  Pass Threshold: 0.95
-->

### Required Artifacts
- **Validated Training Report** from Protocol 13 (`.artifacts/protocol-13/training-results.md`)
- **Baseline Evaluation Matrix** from Protocol 12 (`.artifacts/protocol-12/evaluation-matrix.xlsx`)
- **Dataset Splits Manifest** from Protocol 11 (`.artifacts/protocol-11/dataset-manifest.json`)
- **Experiment Tracking Export** (MLflow/W&B) covering latest runs
- **Target KPI Definition** from PRD / AGENTS (`success-targets.md`)

### Required Approvals
- **Protocol 13 Completion Sign-off** (Lead ML Engineer)
- **Business KPI Confirmation** (Product Owner)
- **Data Steward Validation** that dataset splits remain unchanged

### System State
- Access to GPU/CPU evaluation environment with scikit-learn ≥1.3
- `.artifacts/protocol-14/` directory writable with ≥200 MB free
- Experiment tracking credentials configured via environment variables
- Latest models exported to `models/train/` with version tags

---

## AI ROLE AND MISSION

<!-- VALIDATOR MAPPING:
  Primary: Role Validator (validate_protocol_role.py)
  Dimensions: role_definition / mission_statement / constraints / outputs / behavior
  Pass Threshold: 0.90
-->

You are an **AI Model Validation Strategist**.

You specialize in orchestrating rigorous, data-driven evaluation cycles that triangulate metrics, error patterns, and statistical diagnostics to surface trustworthy decisions. You combine quantitative depth (domain expertise in computer vision + NLP + tabular modeling) with behavioral traits that are systematic, rigorous, transparent, and evidence obsessed.

**Mission**: Execute a disciplined validation campaign that (1) quantifies performance against signed-off success criteria, (2) diagnoses misclassification clusters and regression outliers, (3) compares candidate models using a documented decision framework, and (4) detects overfitting/underfitting risks before handoff to downstream testing protocols, ensuring measurable value to stakeholders.

### Constraints and Guidelines
- **[STRICT]** Never promote a model without hit-checking every gate and logging the rationale in `.artifacts/protocol-14/model-decision-log.md`.
- **[GUIDELINE]** Reference validator line numbers and experiment run IDs whenever raising issues.
- **[CRITICAL]** Halt if any required artifact (metrics, confusion matrix, evaluation manifest) is missing or corrupted.

---

## WORKFLOW

<!-- VALIDATOR MAPPING:
  Primary: Workflow Validator (validate_protocol_workflow.py)
  Secondary: Reasoning Validator (validate_protocol_reasoning.py)
  Dimensions: step_definitions / action_markers / halt_conditions / evidence_tracking / decision logic / reasoning / problem solving
  Pass Threshold: 0.90
-->

### STEP 1: Performance Metrics Calculation
**Action:** Ingest `dataset-manifest.json`, align KPI targets, compute accuracy, precision, recall, F1, ROC-AUC, regression RMSE/MAE, and push results to the validation manifest.
**Communication:** Broadcast metric availability with `[METRICS READY] run={run_id}` and include explicit clarification prompts ("Should I treat KPI-X as weighted F1 already?") plus decision tag `#Gate1-prep`.
**Evidence:** Persist `.artifacts/protocol-14/metrics/validation-metrics.json`, append SHA256 to `evidence-manifest.json`, and link downstream consumers (Protocols 15–17) via manifest `consumers` field.
1. **[STRICT]** Load `dataset-manifest.json`, align target KPI definitions, and compute accuracy, precision, recall, F1, ROC-AUC, and regression RMSE/MAE as applicable.
2. **[GUIDELINE]** Apply dual reasoning patterns: *benchmark comparison* (against Protocol 12 baseline) and *trend analysis* (previous experiment curves) to understand trajectory.
3. **[CRITICAL]** If metric extraction fails or any metric is `NaN`, raise `[ERROR] METRIC_EXTRACTION_FAILED` and halt until data integrity is restored.

**Validation Checkpoint 1.1**
- ✓ Metrics ≥ five core KPIs captured in `validation-metrics.json`
- ✓ Reasoning log captures “why” each metric matters plus at least two explanation statements
- ✓ Evidence: `.artifacts/protocol-14/metrics/validation-metrics.json`

### STEP 2: Confusion Matrix & Error Analysis
**Action:** Generate confusion matrices (per class) or calibration curves, annotate outlier clusters, tag severity ratings, and document consumer impact (Protocol 16 fairness pipeline) inside the step narrative.
**Communication:** Share `[ERROR ANALYSIS]` digest with QA + Product ("Boss, clarify if we prioritize minority recall already?") and capture decision/feedback/resolution loops inside `error-insights.md`.
**Evidence:** Store CSV + PNG outputs plus narrative markdown in `.artifacts/protocol-14/error-analysis/`, reference each file inside `validation-summary.md`, and note which downstream protocol consumes the insight.
1. **[STRICT]** Generate confusion matrices (per class) or calibration curves, storing PNG + CSV artifacts.
2. **[GUIDELINE]** Investigate issues by tagging at least three *problem* clusters (issue/error/failure) and annotate root cause hypotheses.
3. **[CRITICAL]** When severity > threshold (e.g., minority-class recall < 0.7), trigger corrective action plan and document fallback solutions.

**Validation Checkpoint 2.1**
- ✓ ≥3 decision terms used (if/then, when, evaluate) describing filtering logic
- ✓ ≥3 problem terms captured in `error-insights.md`
- ✓ ≥2 solution pathways listed (e.g., threshold tuning vs. rebalancing)
- ✓ Evidence: `.artifacts/protocol-14/error-analysis/error-insights.md`

### STEP 3: Model Comparison & Selection
**Action:** Assemble comparison table for champion vs. challengers (model IDs, seed, feature set) with weighted score combining accuracy, latency, cost multipliers, and compliance readiness, then map chosen model to Protocol 15 inputs.
**Communication:** Facilitate `[DECISION POINT]` and `[CLARIFICATION]` prompts ("Should we optimize latency or accuracy first?") and request stakeholder feedback/resolution in the log.
**Evidence:** Version table + decision notes under `.artifacts/protocol-14/decisions/`, note consumer (Protocol 17 explainability) and attach reviewer signatures.
1. **[STRICT]** Assemble comparison table for champion vs. challengers (model IDs, seed, feature set) with weighted score.
2. **[GUIDELINE]** Apply multi-criteria decision strategy (performance, stability, cost) and record decision tree plus reasoning pattern references.
3. **[CRITICAL]** Do not approve selection until stakeholders review `model-decision-log.md` and sign Gate 3.

**Validation Checkpoint 3.1**
- ✓ Weighted scores normalized (0–1) and stored in `model-comparison-table.md`
- ✓ Decision tree documented with ≥3 outcome branches
- ✓ Stakeholder approval placeholder filled

### STEP 4: Overfitting/Underfitting Diagnosis
**Action:** Compute train vs. validation deltas per metric, overlay learning-curve plots to classify bias vs. variance, and document how findings flow into Protocol 18 packaging readiness.
**Communication:** Publish `[DIAGNOSTIC ALERT]` messages whenever delta exceeds threshold, ask "Ma'am, approve remediation A or B?" and log acknowledgments.
**Evidence:** Capture overfitting tables + mitigation checklist in `.artifacts/protocol-14/diagnostics/overfitting-report.md`, link to `validation-summary.md`, and reference mitigation ticket IDs.
1. **[STRICT]** Compute train vs. validation deltas per metric; halt if delta > 0.05 unless justified.
2. **[GUIDELINE]** Evaluate learning curves or residual plots to reason about variance vs. bias (pattern + heuristic discussion).
3. **[CRITICAL]** If underfitting detected (train + val under target), propose remediation (feature expansion, architecture change) and communicate gating impact immediately.

**Validation Checkpoint 4.1**
- ✓ Overfitting delta table created and referenced by Gate 2
- ✓ Root cause + mitigation logged with at least one continuous improvement bullet
- ✓ Evidence: `.artifacts/protocol-14/diagnostics/overfitting-report.md`

### Halt Conditions
- **If metrics artifacts missing**: `[HALT] Missing validation-metrics.json` – notify ML Ops lead, rerun STEP 1.
- **If overfitting delta > 0.05 without mitigation**: `[HALT] Overfitting risk unresolved` – trigger Gate 2 failure.

### Evidence Tracking
- Metrics JSON + markdown summary stored under `.artifacts/protocol-14/metrics/`
- Confusion matrix CSV + PNG stored under `.artifacts/protocol-14/error-analysis/`
- Comparison + decision logs stored under `.artifacts/protocol-14/decisions/`

---

## INTEGRATION POINTS

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator
  Dimensions: integration_points / documentation_quality
  Pass Threshold: 0.95
-->

### Inputs From
- **Protocol 11** – Dataset splits + leakage checks (JSON, CSV) from `.artifacts/protocol-11/`
- **Protocol 12** – Baseline evaluation + candidate algorithms (Markdown, XLSX) from `.artifacts/protocol-12/`
- **Protocol 13** – Trained models and run metadata (YAML, JSON) from `.artifacts/protocol-13/`

### Outputs To
- **Protocol 15** – Validated model package + edge-case priorities (Markdown, ZIP) into `.artifacts/protocol-15/`
- **Protocol 16** – Bias-ready metrics bundle (JSON) for fairness audits
- **Protocol 17** – Explainability-ready reference model + evaluation context (YAML/Markdown)

### Data Formats
- Markdown (.md) for reports and decision logs
- JSON (.json) for metrics, thresholds, manifest entries
- PNG/.csv for confusion matrices and plots

### Storage Locations
- `.artifacts/protocol-14/metrics/` – quantitative outputs
- `.artifacts/protocol-14/error-analysis/` – error breakdowns
- `.artifacts/protocol-14/decisions/` – approvals, comparisons, gate evidence

---

## QUALITY GATES

<!-- VALIDATOR MAPPING:
  Primary: Gates Validator (validate_protocol_gates.py)
  Pass Threshold: 0.92
-->

### Gate 1: Validation Performance ≥ Target Threshold (Execution)
- **Criteria**: For each primary KPI, `metric_value ≥ target_value` from PRD
- **Pass Threshold**: `score >= 0.95` aggregate
- **Metrics**: Accuracy, F1, ROC-AUC, MAE
- **Evidence Links**: `.artifacts/protocol-14/metrics/validation-metrics.json`
- **Failure Handling**: (1) rollback to Protocol 13 tuning cycle, (2) notify Product Owner, (3) log waiver if temporary acceptance is required

### Gate 2: Overfitting Check (Execution)
- **Criteria**: `abs(train_score - val_score) ≤ 0.05` for all KPIs
- **Pass Threshold**: `delta <= 0.05`
- **Metrics**: Train vs. validation deltas table
- **Evidence Links**: `.artifacts/protocol-14/diagnostics/overfitting-report.md`
- **Failure Handling**: escalate to ML Lead, require mitigation plan, block handoff

### Gate 3: Model Selection Approved (Completion)
- **Criteria**: Stakeholder sign-off recorded (`model_selection_approved = true`)
- **Pass Threshold**: Boolean true with timestamp + approver
- **Metrics**: Approval checklist, decision log references
- **Evidence Links**: `.artifacts/protocol-14/decisions/model-decision-log.md`
- **Failure Handling**: revert to STEP 3 evaluation, collect additional evidence, re-run comparison

---

## COMMUNICATION PROTOCOLS

<!-- VALIDATOR MAPPING:
  Primary: Communication Validator (validate_protocol_communication.py)
  Dimensions: status_announcements / user_interaction / error_messaging / progress_tracking / evidence_communication
  Pass Threshold: 0.90
-->

### Status Announcements

- `[PHASE 4 START] MASTER RAY | Validation kick-off | ETA 4h. Confirm KPI targets already?`
- `[PHASE 4 MID] Evidence at {{progress}}% complete – reply 'Go' to continue.`
- `[PHASE 4 COMPLETE] Champion selected, awaiting Gate 3 approval.`

### User Interaction

- **Confirmation**: "Boss, confirm KPI targets already so we can lock Gate 1? Reply 'Go'."
- **Clarification**: "Should I interpret minority recall as weighted by business tier?"
- **Decision Points**: "Choose champion Model A (accuracy) or Model B (latency)."
- **Feedback Requests**: "Does this remediation plan meet your expectations, ma'am?"

### Error Messaging
- `[ERROR][CRITICAL] Metric extraction failed for run {{run_id}} – context: missing confusion matrix. Resolution: re-run calculate_metrics.py with --force.`
- `[ERROR][HIGH] Overfitting delta 0.08 detected. Resolution: apply regularization plan, rerun Gate 2.`

### Progress Tracking
- `[PROGRESS] STEP 2 error analysis ongoing – 45% complete.`
- `[NEXT] Compare champion models after metrics review (ETA 2h).`
- `[STATUS] Gate 1 pending, Gate 2 pending, Gate 3 not started.`

### Evidence Communication
- `[ARTIFACT] validation-metrics.json saved to .artifacts/protocol-14/metrics/ – validation: pass.`
- `[ARTIFACT] model-decision-log.md stored in .artifacts/protocol-14/decisions/ – validation: pending approval.`

---

## AUTOMATION HOOKS

<!-- VALIDATOR MAPPING:
  Primary: Scripts Validator (validate_protocol_scripts.py)
  Dimensions: script_inventory / registry_alignment / execution_context / command_syntax / error_handling
  Pass Threshold: 0.90
-->

### Scripts
```bash
# Compute standard metrics & KPIs (logs captured)
python3 scripts/ai/calculate_metrics.py --y_true data/labels/val_labels.csv --y_pred outputs/predictions.csv --out .artifacts/protocol-14/metrics/validation-metrics.json > .artifacts/protocol-14/logs/calculate_metrics.log 2>&1

# Analyze confusion matrices & error clusters with run context
python3 scripts/ai/analyze_errors.py --predictions outputs/predictions.csv --labels data/labels/val_labels.csv --report .artifacts/protocol-14/error-analysis/error-insights.json > .artifacts/protocol-14/logs/analyze_errors.log 2>&1

# Diagnose overfitting / underfitting patterns per run
python3 scripts/ai/diagnose_model_issues.py --train-metrics .artifacts/protocol-13/train-metrics.json --val-metrics .artifacts/protocol-14/metrics/validation-metrics.json --out .artifacts/protocol-14/diagnostics/overfitting-report.md --threshold 0.05 > .artifacts/protocol-14/logs/diagnose_model_issues.log 2>&1
```

### Registry Alignment
- **Script Registry**: `scripts/script-registry.json`
- Entries for `calculate_metrics`, `analyze_errors`, `diagnose_model_issues` must list owner = Protocol 14, status = active, dependencies = `pandas`, `numpy`, `scikit-learn`, `matplotlib` (for plots).

### Execution Context
- **CI/CD**: GitHub Action `model-validation.yml` (ubuntu-latest, nightly + on-demand) with stage `validate-protocol-14`.
- **Environment**: Python 3.10 virtualenv + Docker fallback (`devcontainer.json`) with dependencies pinned in `requirements.txt`.
- **Scheduling**: Cron `0 2 * * *` for regression runs; manual dispatch allowed for hotfix builds.
- **Permissions**: Needs read access to experiment tracking, write access to `.artifacts/protocol-14/`, and secret `EXPERIMENT_TOKEN`.

### Command Syntax & Error Handling
- Standard flags `--y_true`, `--y_pred`, `--out`, `--format`
- **Exit Codes**: `0=success`, `1=validation_error`, `2=io_error` documented per script.
- **Fallback**: Retry sequence `rerun -> cleanse cache -> escalate` defined in `validation-summary.md`.
- **Logging**: `.artifacts/protocol-14/logs/*.log` with rotation policy; entries mirrored to `run-log.json`.
- **Manual Paths**: Manual checklist `manual-validation.md` describes adaptation/knowledge capture if automation fails twice.

---

## HANDOFF CHECKLIST

<!-- VALIDATOR MAPPING:
  Primary: Handoff Validator (validate_protocol_handoff.py)
  Pass Threshold: 0.90
-->

### Prerequisites
- [ ] All metrics + error analysis artifacts stored and checksumed
- [ ] Gate results documented (pass/warn/fail) with timestamps

### Workflow
- [ ] Validation steps executed sequentially without skipped checkpoints
- [ ] Issues + mitigations recorded in decision log

### Quality
- [ ] Gate 1 score ≥ target, evidence attached
- [ ] Gate 2 delta ≤ 0.05 or waiver documented

### Evidence
- [ ] Metrics JSON + markdown summary verified and linked to Protocols 15–17 (consumer trace)
- [ ] Confusion matrix assets accessible (CSV + PNG) with manifest + adaptation references

### Integration
- [ ] Output bundle shared with Protocols 15-17 (links + formats listed, feedback/improvement loops logged)
- [ ] Ready statement: “Protocol 14 outputs baselined and signed.”

### Automation
- [ ] **Action**: All three automation scripts executed successfully (logs stored)
- [ ] **Communication**: calculate_metrics.py run logged with exit code 0
- [ ] **Evidence**: analyze_errors.py report generated and archived

### Verification Procedures

- [ ] Validate manifest coverage using `package_evidence.py`
- [ ] Confirm Gate approvals recorded with stakeholder signatures
- [ ] Verify bias/variance deltas comply with Gate 2 thresholds
- [ ] Check adaptation plan feeds knowledge base (feedback/improvement/knowledge/adaptation keywords present)

### Stakeholder Sign-off
- [ ] **Reviewer**: Lead ML Engineer – [APPROVAL_STATUS]
- [ ] **Evidence Package**: `.artifacts/protocol-14/decisions/model-decision-log.md` – status tracked
- [ ] **Confirmation**: Compliance officer acknowledgment stored with improvement + feedback notes

### Documentation Requirements
- [ ] validation-summary.md saved to `.artifacts/protocol-14/`
- [ ] Format: Markdown + JSON with improvement + knowledge references
- [ ] Reviewer docs: `.artifacts/protocol-14/reviews/feedback-notes.md` capturing adaptation plan

### Next Protocol Alignment
- [ ] **Ready for Protocol 15**: statement logged including adaptation + improvement cues
- [ ] **Next Command**: `@apply dev-workflow/protocol-creation/15` after approval
- [ ] **Dependencies**: Edge-case list, fairness metrics, explainability hooks enumerated
- [ ] **Continuation Script**: `scripts/ai/generate_edge_cases.py` referenced for future adaptation

---

## EVIDENCE SUMMARY

<!-- VALIDATOR MAPPING:
  Primary: Evidence & Reflection Validators
  Dimensions: artifact_generation / storage_structure / manifest / traceability / archival / continuous improvement
  Pass Threshold: 0.90
-->

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
| validation-metrics.json | `.artifacts/protocol-14/metrics/validation-metrics.json` | Quantitative metrics | Accuracy, Precision, Recall, F1, ROC-AUC |
| model-decision-log.md | `.artifacts/protocol-14/decisions/model-decision-log.md` | Decision record | Champion score, Approval status |
| overfitting-report.md | `.artifacts/protocol-14/diagnostics/overfitting-report.md` | Diagnostic narrative | Train–Val delta, mitigation plan |

### Storage Structure
- Protocol directory: `.artifacts/protocol-14/`
- Subdirectories: `metrics/`, `error-analysis/`, `diagnostics/`, `decisions/`, `logs/`
- Permissions: Read for QA + Compliance, Write for ML team, Audit logs append-only
- Naming Convention: `artifact-type_timestamp.ext`

### Manifest & Traceability
- Manifest file: `.artifacts/protocol-14/evidence-manifest.json` (includes metadata, hashes, dependencies)
- Inputs referenced: Protocols 11–13 artifacts with relative paths
- Transformations logged in `validation-summary.md`
- Audit trail maintained via `run-log.json` capturing script + command invocations

### Archival & Continuous Improvement
- Compression: Weekly ZIP snapshots stored in `.artifacts/protocol-14/archive/`
- Retention: 90 days or until prod deployment, whichever is longer
- Retrieval: `scripts/orchestration/package_evidence.py --protocol 14`
- Cleanup: `cleanup-policy.md` defines cold storage migration
- Lessons Learned + optimization opportunities appended to `validation-summary.md`

---

## READY FOR PROTOCOL 14 CONTENT EXECUTION

Outputs above unlock Protocol 4 validation once artifacts + scripts are present in `.artifacts/protocol-14/` and registered automation hooks succeed.

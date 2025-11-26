# MASTER RAY™ AI/ML Workflow Protocols

**Specialized Machine Learning Lifecycle - From Use Case Definition to Model Monitoring**

---

## 🎯 Overview

This directory contains the **AI/ML Track** protocols for machine learning and artificial intelligence projects. These protocols extend the Generic Track with specialized steps for data engineering, model development, and ML operations.

### Key Features

- **15+ ML-Specific Protocols**: Complete ML lifecycle coverage
- **5 ML Phases**: Use Case → Data → Training → Validation → Deployment
- **MLOps Integration**: Production-ready ML workflows
- **Quality Gates**: Model performance and data quality checkpoints
- **Evidence-Driven**: Experiment tracking and model artifacts

---

## 📂 Protocol Map

### Phase 1: Foundation (Shared with Generic)

| Protocol | Name | Purpose |
|----------|------|---------|
| 01 | [Client Proposal Generation](./01-client-proposal-generation.md) | Generate ML project proposals |
| 02 | [Client Discovery Initiation](./02-client-discovery-initiation.md) | ML stakeholder discovery |
| 03 | [Project Brief Creation](./03-project-brief-creation.md) | ML-specific brief synthesis |
| 04 | [Bootstrap & Context Engineering](./04-project-bootstrap-and-context-engineering.md) | ML context initialization |
| 05b | [Protocol Orchestration](./05b-project-protocol-orchestration-v2.md) | **ROUTER**: Selects ML protocols |
| 05c | [Generate Rules](./05c-generate-rules.md) | ML project rules |

### Phase 2: Use Case & Strategy

| Protocol | Name | Purpose |
|----------|------|---------|
| 06 | [AI Use Case Definition & Prioritization](./06-ai-use-case-definition-prioritization.md) | Define and prioritize ML use cases |
| 07 | [AI Data Strategy Planning](./07-ai-data-strategy-planning.md) | Data sourcing and governance strategy |

### Phase 3: Data Pipeline

| Protocol | Name | Purpose |
|----------|------|---------|
| 08 | [AI Data Collection & Ingestion](./08-ai-data-collection-ingestion.md) | Build data ingestion pipelines |
| 09 | [AI Data Cleaning & Validation](./09-ai-data-cleaning-validation.md) | Data quality and preprocessing |
| 10 | [AI Feature Engineering](./10-ai-feature-engineering.md) | Feature extraction and selection |
| 11 | [AI Dataset Preparation & Splitting](./11-ai-dataset-preparation-splitting.md) | Train/val/test splits |

### Phase 4: Model Development

| Protocol | Name | Purpose |
|----------|------|---------|
| 12 | [AI Algorithm Selection & Baseline](./12-ai-algorithm-selection-baseline.md) | Algorithm selection, baseline models |
| 13 | [AI Model Training & Tuning](./13-ai-model-training-tuning.md) | Hyperparameter optimization |
| 14 | [AI Model Validation & Evaluation](./14-ai-model-validation-evaluation.md) | Performance metrics, cross-validation |
| 15 | [AI Model Testing & Edge Case Validation](./15-ai-model-testing-edge-case-validation.md) | Robustness testing |

### Phase 5: MLOps & Deployment

*(Extends Generic Track protocols 14-22 with ML-specific considerations)*

| Generic Protocol | ML Extension |
|------------------|--------------|
| 14: Pre-Deployment Staging | Model staging, A/B test setup |
| 15: Production Deployment | Model serving, inference endpoints |
| 16: Monitoring & Observability | Model drift detection, performance monitoring |
| 17: Incident Response | Model rollback, retraining triggers |
| 18: Performance Optimization | Inference optimization, quantization |

---

## 🔄 ML Workflow Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MASTER RAY™ AI/ML WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────────┘

Phase 1: Foundation                Phase 2: Strategy
┌──────────────────────┐          ┌──────────────────────┐
│  01 → 02 → 03 → 04   │    →     │  06 → 07             │
│  Proposal  Discovery │          │  Use Case  Data      │
│  Brief     Bootstrap │          │  Definition Strategy │
└──────────────────────┘          └──────────────────────┘
                                           │
                                           ▼
Phase 3: Data Pipeline            Phase 4: Model Dev
┌──────────────────────┐          ┌──────────────────────┐
│  08 → 09 → 10 → 11   │    →     │  12 → 13 → 14 → 15   │
│  Collect  Clean      │          │  Algo    Train       │
│  Feature  Split      │          │  Validate  Test      │
└──────────────────────┘          └──────────────────────┘
                                           │
                                           ▼
Phase 5: MLOps                    Phase 6: Operations
┌──────────────────────┐          ┌──────────────────────┐
│  Stage → Deploy →    │    →     │  Monitor → Retrain → │
│  Serve   Inference   │          │  Drift     Optimize  │
└──────────────────────┘          └──────────────────────┘
```

---

## 🧠 ML-Specific Concepts

### Use Case Classification (Protocol 06)

| Use Case Type | Examples | Key Protocols |
|---------------|----------|---------------|
| **Supervised Learning** | Classification, Regression | 06-15 (full pipeline) |
| **Unsupervised Learning** | Clustering, Anomaly Detection | 06-15 (adjusted metrics) |
| **Deep Learning** | Computer Vision, NLP | 06-15 + GPU considerations |
| **Reinforcement Learning** | Game AI, Robotics | 06-15 + simulation protocols |
| **Generative AI** | LLMs, Image Generation | 06-15 + prompt engineering |

### Data Strategy Dimensions (Protocol 07)

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA STRATEGY                            │
├─────────────────────────────────────────────────────────────┤
│  Sources        │  Internal DBs, External APIs, Web Scrape │
│  Volume         │  GB, TB, PB scale considerations         │
│  Velocity       │  Batch, Streaming, Real-time            │
│  Variety        │  Structured, Semi-structured, Unstructured│
│  Veracity       │  Quality, Completeness, Accuracy        │
│  Governance     │  Privacy, Compliance, Retention         │
└─────────────────────────────────────────────────────────────┘
```

### Model Quality Gates

| Gate | Metric | Threshold |
|------|--------|-----------|
| **Data Quality** | Completeness, consistency | ≥95% |
| **Baseline Performance** | Accuracy/F1/RMSE | Better than naive |
| **Cross-Validation** | CV score variance | ≤5% |
| **Test Performance** | Generalization gap | ≤10% |
| **Bias/Fairness** | Demographic parity | Pass audit |
| **Production Readiness** | Latency, throughput | Meet SLAs |

---

## 🔌 Integration with Generic Track

```
                    PROJECT START
                         │
                         ▼
              ┌─────────────────────┐
              │  Generic 01-04      │
              │  Foundation         │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Generic 05b        │
              │  ROUTER             │──── Classifies as ML Project
              └─────────────────────┘
                         │
           ┌─────────────┴─────────────┐
           │                           │
           ▼                           ▼
┌─────────────────────┐    ┌─────────────────────┐
│  Generic Track      │    │  AI/ML Track        │
│  (Infrastructure)   │    │  (ML Pipeline)      │
│                     │    │                     │
│  - Environment      │    │  - Use Case         │
│  - CI/CD            │    │  - Data Pipeline    │
│  - Monitoring       │    │  - Model Dev        │
│  - Deployment       │    │  - MLOps            │
└─────────────────────┘    └─────────────────────┘
           │                           │
           └─────────────┬─────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Generic 19-22      │
              │  Closure            │
              └─────────────────────┘
```

---

## 🛠️ Quick Start for ML Projects

### 1. Discovery Phase

```bash
# Start with Generic Foundation
Protocol 01: Generate ML-focused proposal
Protocol 02: Conduct ML stakeholder discovery
Protocol 03: Create ML project brief
Protocol 04: Bootstrap ML context
Protocol 05b: Router selects ML protocols
```

### 2. ML Pipeline

```bash
# AI/ML Track
Protocol 06: Define ML use cases and KPIs
Protocol 07: Plan data strategy
Protocol 08: Build data ingestion
Protocol 09: Clean and validate data
Protocol 10: Engineer features
Protocol 11: Prepare datasets
Protocol 12: Select algorithms, build baseline
Protocol 13: Train and tune models
Protocol 14: Validate model performance
Protocol 15: Test edge cases
```

### 3. Deployment

```bash
# Generic Track with ML extensions
Protocol 14+: Stage model for A/B testing
Protocol 15+: Deploy to inference endpoint
Protocol 16+: Setup model monitoring
Protocol 17+: Define rollback triggers
```

---

## 📊 Evidence & Artifacts

### ML-Specific Artifacts

| Protocol | Key Artifacts |
|----------|---------------|
| 06 | `use-case-definition.md`, `prioritization-matrix.json` |
| 07 | `data-strategy.md`, `data-governance-plan.md` |
| 08 | `ingestion-pipeline.py`, `data-catalog.json` |
| 09 | `data-quality-report.json`, `cleaning-scripts/` |
| 10 | `feature-definitions.json`, `feature-store-config.yaml` |
| 11 | `dataset-splits.json`, `data-version.dvc` |
| 12 | `algorithm-comparison.md`, `baseline-model.pkl` |
| 13 | `hyperparameter-search.json`, `trained-model.pkl` |
| 14 | `validation-report.md`, `metrics.json` |
| 15 | `edge-case-tests.json`, `robustness-report.md` |

### Experiment Tracking

```
.artifacts/
└── ml/
    ├── experiments/
    │   ├── exp-001/
    │   │   ├── params.json
    │   │   ├── metrics.json
    │   │   └── model.pkl
    │   └── exp-002/
    │       └── ...
    ├── datasets/
    │   └── versions/
    └── models/
        └── registry/
```

---

## ✅ Quality Assurance

### ML Validators

In addition to standard protocol validators, ML protocols are checked for:

| Validator | What It Checks |
|-----------|----------------|
| Data Quality | Schema compliance, completeness, consistency |
| Model Performance | Metrics meet thresholds |
| Reproducibility | Seeds, versions, environment captured |
| Bias/Fairness | Demographic parity, equal opportunity |
| Documentation | Model cards, data sheets |

### ML Quality Gates

```
Gate 1: Data Quality       → ≥95% completeness, schema valid
Gate 2: Feature Quality    → No leakage, correlation analysis
Gate 3: Baseline Achieved  → Better than naive predictor
Gate 4: Validation Pass    → CV score meets threshold
Gate 5: Test Pass          → Generalization gap acceptable
Gate 6: Fairness Audit     → No discriminatory bias
Gate 7: Production Ready   → Latency/throughput SLAs met
```

---

## 📚 Related Documentation

- [Generic Protocols](../.cursor/ai-driven-workflow/) - Standard workflow
- [Validator System](../validators-system/) - Protocol validation
- [Orchestration Scripts](../scripts/orchestration/) - Automation
- [Classification Config](../config/classification-dimensions.yaml) - ML detection
- [ARCHITECTURE.md](../ARCHITECTURE.md) - System architecture

---

## 🔍 ML Project Type Reference

| Scenario | Protocol Selection |
|----------|-------------------|
| **Classification** | 06-15 + standard metrics |
| **Regression** | 06-15 + RMSE/MAE metrics |
| **NLP/LLM** | 06-15 + text preprocessing |
| **Computer Vision** | 06-15 + image augmentation |
| **Time Series** | 06-15 + temporal splitting |
| **Recommendation** | 06-15 + A/B testing focus |

---

**MASTER RAY™ AI/ML Workflow** - Validated machine learning from use case to production.


# PROTOCOL 11-12-13 WORKFLOW INTEGRATION GUIDE
## AI Model Development Phase - Complete Reference

**Version**: 1.0  
**Last Updated**: 2025-01-14  
**Status**: Production-Ready with Enhancements

---

## QUICK REFERENCE: WORKFLOW OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI MODEL DEVELOPMENT PHASE                       │
│                      (Protocols 11, 12, 13)                         │
└─────────────────────────────────────────────────────────────────────┘

PROTOCOL 11: Dataset Preparation & Splitting (50-85 min)
├─ STEP 1: Split Strategy Definition (10-15 min)
│  └─ Output: split-strategy.md, stratification-analysis.json
├─ STEP 2: Data Leakage Prevention (15-25 min)
│  └─ Output: leakage-detection-report.json
├─ STEP 3: Stratification (10-20 min)
│  └─ Output: stratification-results.json, distribution-validation.json
└─ STEP 4: Dataset Versioning (15-25 min)
   └─ Output: version-metadata.json, integrity-validation.json
   
   ↓ [HANDOFF: Train/Val/Test Datasets + Metadata]
   
PROTOCOL 12: Algorithm Selection & Baseline Model (55-90 min)
├─ STEP 1: Algorithm Evaluation Matrix (20-30 min)
│  └─ Output: algorithm-candidates.md, algorithm-evaluation-matrix.json
├─ STEP 2: Baseline Model Creation (15-25 min)
│  └─ Output: baseline-model.pkl, baseline-performance.json
├─ STEP 3: Performance Benchmark (10-15 min)
│  └─ Output: evaluation-metrics.md, baseline-benchmarks.json
└─ STEP 4: Experiment Tracking Setup (10-20 min)
   └─ Output: tracking-config.yaml, baseline-run.json
   
   ↓ [HANDOFF: Baseline Model + Metrics + Tracking Config]
   
PROTOCOL 13: Model Training & Hyperparameter Tuning (75-130 min)
├─ STEP 1: Training Pipeline Setup (15-20 min)
│  └─ Output: data-loader-config.yaml, training-config.yaml
├─ STEP 2: Hyperparameter Optimization (30-60 min)
│  └─ Output: hyperparameter-space.json, optimization-results.json
├─ STEP 3: Cross-Validation Strategy (20-30 min)
│  └─ Output: cv-config.yaml, cv-results.json
└─ STEP 4: Training Monitoring & Checkpointing (10-20 min)
   └─ Output: final-model.pkl, test-performance.json
   
   ↓ [HANDOFF: Trained Model + Performance Metrics]
   
PROTOCOL 14: Model Evaluation & Drift Monitoring (Next Phase)
```

---

## DETAILED INTEGRATION POINTS

### Protocol 11 → Protocol 12 Handoff

#### Artifacts Passed

| Artifact | Location | Protocol 12 Usage | Critical |
|---|---|---|---|
| **Train Dataset** | `.artifacts/protocol-11/datasets/train.parquet` | Algorithm evaluation, baseline training | ✅ YES |
| **Validation Dataset** | `.artifacts/protocol-11/datasets/validation.parquet` | Algorithm evaluation, baseline validation | ✅ YES |
| **Test Dataset** | `.artifacts/protocol-11/datasets/test.parquet` | Baseline performance evaluation | ✅ YES |
| **Version Metadata** | `.artifacts/protocol-11/version-metadata.json` | Data provenance, reproducibility | ⚠️ RECOMMENDED |
| **Leakage Report** | `.artifacts/protocol-11/leakage-detection-report.json` | Data quality assurance | ⚠️ RECOMMENDED |
| **Distribution Report** | `.artifacts/protocol-11/distribution-validation.json` | Class balance verification | ⚠️ RECOMMENDED |

#### Handoff Checklist

```
Protocol 11 Completion:
✅ All 3 quality gates passed
✅ Train/validation/test datasets created
✅ Datasets versioned with checksums
✅ Zero data leakage confirmed
✅ Split ratios within ±2% tolerance

Protocol 12 Prerequisites Satisfied:
✅ Datasets accessible at specified locations
✅ Dataset metadata available
✅ Data characteristics documented
✅ Problem definition clear (from Protocol 3)
✅ Ready to proceed with algorithm evaluation
```

#### Data Format Compatibility

```
Protocol 11 Output Format    →    Protocol 12 Input Format
─────────────────────────────────────────────────────────
Parquet (.parquet)           →    Pandas DataFrame (via pd.read_parquet)
JSON (.json)                 →    Python dict (via json.load)
Markdown (.md)               →    Documentation reference
YAML (.yaml)                 →    Configuration reference
```

---

### Protocol 12 → Protocol 13 Handoff

#### Artifacts Passed

| Artifact | Location | Protocol 13 Usage | Critical |
|---|---|---|---|
| **Baseline Model** | `.artifacts/protocol-12/baseline-model.pkl` | Starting point for optimization | ✅ YES |
| **Evaluation Metrics** | `.artifacts/protocol-12/evaluation-metrics.md` | Performance comparison baseline | ✅ YES |
| **Baseline Benchmarks** | `.artifacts/protocol-12/baseline-benchmarks.json` | Performance improvement target | ✅ YES |
| **Algorithm Selection** | `.artifacts/protocol-12/baseline-selection.md` | Algorithm context, justification | ⚠️ RECOMMENDED |
| **Experiment Config** | `.artifacts/protocol-12/tracking-config.yaml` | Experiment tracking setup | ⚠️ **SHOULD ADD** |
| **Baseline Run ID** | `.artifacts/protocol-12/baseline-run.json` | Experiment tracking reference | ⚠️ RECOMMENDED |

#### Handoff Checklist

```
Protocol 12 Completion:
✅ All 3 quality gates passed
✅ Baseline model trained and saved
✅ Baseline performance > random baseline
✅ Evaluation metrics defined
✅ Experiment tracking configured
✅ Baseline experiment logged

Protocol 13 Prerequisites Satisfied:
✅ Baseline model accessible
✅ Evaluation metrics available
✅ Performance benchmarks documented
✅ Datasets still accessible from Protocol 11
✅ ML training environment ready
✅ GPU/compute resources available
✅ Experiment tracking active
✅ Ready to proceed with hyperparameter optimization
```

#### **⚠️ ENHANCEMENT NEEDED**: Experiment Tracking Configuration

**Current State**: Protocol 12 creates tracking config but Protocol 13 doesn't explicitly reference it.

**Recommended Fix**:
1. Add to Protocol 13 prerequisites:
   ```yaml
   - Experiment Tracking Configuration: `.artifacts/protocol-12/tracking-config.yaml`
   - Baseline Run ID: `.artifacts/protocol-12/baseline-run.json`
   ```

2. Update Protocol 13 STEP 1 to load existing configuration:
   ```python
   # Load existing experiment tracking configuration
   with open('.artifacts/protocol-12/tracking-config.yaml', 'r') as f:
       tracking_config = yaml.safe_load(f)
   ```

3. Update handoff checklist item:
   ```
   - [ ] Experiment tracking configuration loaded from Protocol 12
   - [ ] Baseline run ID referenced for continuity
   ```

---

### Protocol 13 → Protocol 14 Handoff

#### Artifacts to Be Passed

| Artifact | Location | Protocol 14 Usage | Status |
|---|---|---|---|
| **Trained Model** | `.artifacts/protocol-13/final-model.pkl` | Model evaluation, testing | ✅ Ready |
| **Performance Metrics** | `.artifacts/protocol-13/test-performance.json` | Baseline for evaluation | ✅ Ready |
| **Training History** | `.artifacts/protocol-13/training-report.md` | Context, hyperparameters | ✅ Ready |
| **Hyperparameters** | `.artifacts/protocol-13/optimization-results.json` | Model configuration | ✅ Ready |
| **Cross-Validation Results** | `.artifacts/protocol-13/cv-results.json` | Robustness assessment | ✅ Ready |

#### Handoff Checklist Template

```
Protocol 13 Completion:
✅ All 3 quality gates passed
✅ Final model trained with optimized hyperparameters
✅ Model performance > baseline performance
✅ Cross-validation results consistent
✅ Hyperparameter optimization converged

Protocol 14 Prerequisites (To Be Satisfied):
⏳ Trained model accessible
⏳ Performance metrics documented
⏳ Training history available
⏳ Hyperparameter configuration documented
⏳ Ready to proceed with model evaluation
```

#### **⚠️ ACTION REQUIRED**: Create Protocol 14 File

**Current Issue**: Protocol 13 references `14-ai-model-evaluation-drift-monitoring.md` which does not exist.

**Required Actions**:
1. Create file: `/home/haymayndz/SuperTemplate-1/AI-project-workflow/14-ai-model-evaluation-drift-monitoring.md`
2. Include prerequisites that reference Protocol 13 outputs
3. Update Protocol 13 line 487 and 568 with correct file reference
4. Ensure Protocol 14 includes:
   - Model evaluation procedures
   - Drift monitoring setup
   - Performance validation
   - Production readiness assessment

---

## QUALITY GATES PROGRESSION

### Gate Validation Flow

```
Protocol 11 Gates:
├─ Gate 1: Data Leakage Check
│  └─ Blocks if: leakage_detected = true
│  └─ Waiver: NOT PERMITTED (critical)
├─ Gate 2: Split Ratios Validated
│  └─ Blocks if: split_ratios_valid = false
│  └─ Waiver: Permitted if deviation <2% (technical lead approval)
└─ Gate 3: Dataset Versioned
   └─ Blocks if: dataset_versioned = false
   └─ Waiver: NOT PERMITTED (critical)

Protocol 12 Gates:
├─ Gate 1: Baseline Performance > Random Guess
│  └─ Blocks if: baseline_performance ≤ random_baseline
│  └─ Waiver: NOT PERMITTED (critical)
├─ Gate 2: Algorithm Justification Documented
│  └─ Blocks if: justification_documented = false
│  └─ Waiver: Permitted with technical lead approval
└─ Gate 3: Experiment Tracking Configured
   └─ Blocks if: tracking_configured = false
   └─ Waiver: NOT PERMITTED (critical)

Protocol 13 Gates:
├─ Gate 1: Training Completion
│  └─ Blocks if: training_completed = false
│  └─ Waiver: NOT PERMITTED (critical)
├─ Gate 2: Model Improvement > Baseline
│  └─ Blocks if: test_performance ≤ baseline_performance
│  └─ Waiver: Permitted if improvement >1% (technical lead approval)
└─ Gate 3: Hyperparameter Tuning Convergence
   └─ Blocks if: optimization_converged = false
   └─ Waiver: NOT PERMITTED (critical)
```

### Gate Interdependencies

```
Protocol 11 Gate 1 (Leakage Check)
    ↓ (Must pass - blocks downstream)
Protocol 12 Gate 1 (Baseline Performance)
    ↓ (Must pass - blocks downstream)
Protocol 13 Gate 1 (Training Completion)
    ↓ (Must pass - blocks downstream)
Protocol 14 Gate 1 (Evaluation Completion)
```

---

## AUTOMATION SCRIPT EXECUTION SEQUENCE

### Protocol 11 Automation

```bash
# Step 1: Define split strategy (manual or via config)
# No automation script needed

# Step 2: Check for data leakage
python3 scripts/ai/check_data_leakage.py \
  --train-data .artifacts/protocol-11/datasets/train.parquet \
  --val-data .artifacts/protocol-11/datasets/validation.parquet \
  --test-data .artifacts/protocol-11/datasets/test.parquet \
  --target-column target \
  --output-report .artifacts/protocol-11/leakage-detection-report.json

# Step 3: Split dataset with stratification
python3 scripts/ai/split_dataset.py \
  --input-data .artifacts/protocol-10/feature-engineered-data.parquet \
  --train-ratio 0.70 \
  --val-ratio 0.15 \
  --test-ratio 0.15 \
  --stratify-column target \
  --output-dir .artifacts/protocol-11/datasets/ \
  --version v1.0.0

# Step 4: Version datasets
python3 scripts/ai/version_dataset.py \
  --dataset-dir .artifacts/protocol-11/datasets/ \
  --version-method dvc \
  --version-tag v1.0.0 \
  --output-metadata .artifacts/protocol-11/version-metadata.json
```

### Protocol 12 Automation

```bash
# Step 1: Evaluate algorithms
python3 scripts/ai/evaluate_algorithms.py \
  --train-data .artifacts/protocol-11/datasets/train.parquet \
  --val-data .artifacts/protocol-11/datasets/validation.parquet \
  --problem-type classification \
  --output-matrix .artifacts/protocol-12/algorithm-evaluation-matrix.json

# Step 2: Create baseline model
python3 scripts/ai/create_baseline_model.py \
  --train-data .artifacts/protocol-11/datasets/train.parquet \
  --val-data .artifacts/protocol-11/datasets/validation.parquet \
  --algorithm random-forest \
  --output-model .artifacts/protocol-12/baseline-model.pkl \
  --output-metrics .artifacts/protocol-12/baseline-performance.json

# Step 3: Setup experiment tracking
python3 scripts/ai/setup_experiment_tracking.py \
  --platform mlflow \
  --project-name ai-model-training \
  --baseline-model .artifacts/protocol-12/baseline-model.pkl \
  --baseline-metrics .artifacts/protocol-12/baseline-performance.json \
  --output-config .artifacts/protocol-12/tracking-config.yaml
```

### Protocol 13 Automation

```bash
# Step 1: Setup training pipeline (manual configuration)
# No automation script needed - configuration via YAML

# Step 2: Tune hyperparameters
python3 scripts/ai/tune_hyperparameters.py \
  --train-data .artifacts/protocol-11/datasets/train.parquet \
  --val-data .artifacts/protocol-11/datasets/validation.parquet \
  --search-space .artifacts/protocol-13/hyperparameter-space.json \
  --output-results .artifacts/protocol-13/optimization-results.json \
  --optimization-method bayesian

# Step 3: Execute cross-validation
python3 scripts/ai/cross_validate_model.py \
  --train-data .artifacts/protocol-11/datasets/train.parquet \
  --best-hyperparameters .artifacts/protocol-13/optimization-results.json \
  --cv-folds 5 \
  --output-results .artifacts/protocol-13/cv-results.json

# Step 4: Train final model
python3 scripts/ai/train_model.py \
  --train-data .artifacts/protocol-11/datasets/train.parquet \
  --val-data .artifacts/protocol-11/datasets/validation.parquet \
  --test-data .artifacts/protocol-11/datasets/test.parquet \
  --best-hyperparameters .artifacts/protocol-13/optimization-results.json \
  --output-model .artifacts/protocol-13/final-model.pkl \
  --output-metrics .artifacts/protocol-13/test-performance.json
```

---

## COMMON FAILURE MODES & RECOVERY

### Protocol 11 Failures

| Failure | Cause | Recovery |
|---|---|---|
| **Data Leakage Detected** | Feature engineering includes target information | Rollback to Protocol 10, remove leakage sources, re-run Protocol 11 |
| **Split Ratios Invalid** | Stratification or random split produces wrong ratios | Re-execute split with adjusted parameters, validate new ratios |
| **Versioning Failed** | DVC/Git LFS initialization error | Check storage permissions, reinitialize version control, re-add datasets |
| **Insufficient Disk Space** | Dataset too large for storage | Increase storage, use compression, reduce dataset size |

### Protocol 12 Failures

| Failure | Cause | Recovery |
|---|---|---|
| **Baseline Performance < Random** | Algorithm not learning from data | Try different algorithm, check data quality, verify target variable |
| **Algorithm Evaluation Timeout** | Too many algorithms or large dataset | Reduce algorithm candidates, use subset of data, increase timeout |
| **Experiment Tracking Error** | MLflow/W&B credentials invalid | Verify credentials, check platform availability, reconfigure tracking |
| **Memory Error** | Dataset too large for memory | Use data generators, reduce batch size, use distributed training |

### Protocol 13 Failures

| Failure | Cause | Recovery |
|---|---|---|
| **Training Failed** | GPU out of memory or data loading error | Reduce batch size, use CPU, verify data format, check data paths |
| **Optimization Not Converging** | Search space too large or learning rate too high | Reduce search space, adjust learning rate, increase iterations |
| **Model Performance Worse** | Hyperparameters not optimized correctly | Re-run optimization with different method, expand search space |
| **Cross-Validation Inconsistent** | High variance across folds | Increase fold count, check for data issues, verify stratification |

---

## PERFORMANCE OPTIMIZATION TIPS

### Protocol 11 Optimization

- **Parallel Versioning**: Run versioning in parallel with Protocol 12 algorithm evaluation
- **Caching**: Cache leakage detection results if dataset unchanged
- **Batch Processing**: Process large datasets in chunks for memory efficiency

### Protocol 12 Optimization

- **Algorithm Caching**: Cache algorithm evaluation results for dataset reuse
- **Parallel Evaluation**: Evaluate multiple algorithms in parallel
- **Early Stopping**: Stop algorithm evaluation if performance plateaus

### Protocol 13 Optimization

- **Distributed Training**: Use distributed training for large datasets
- **GPU Acceleration**: Leverage GPU for deep learning models
- **Hyperparameter Caching**: Cache hyperparameter search results

---

## MONITORING & OBSERVABILITY

### Key Metrics to Track

| Protocol | Metric | Target | Alert Threshold |
|---|---|---|---|
| **P11** | Data leakage score | 0.0 | >0.1 |
| **P11** | Split ratio deviation | ±2% | >5% |
| **P11** | Versioning success rate | 100% | <95% |
| **P12** | Baseline performance | >random | <random |
| **P12** | Algorithm evaluation time | <30 min | >60 min |
| **P13** | Training time | <2 hours | >4 hours |
| **P13** | Model improvement | >1% | <0% |
| **P13** | Convergence score | >0.9 | <0.7 |

### Logging Best Practices

```python
# All scripts should log:
- Start timestamp
- Input parameters
- Progress checkpoints
- Performance metrics
- Error messages
- End timestamp
- Execution duration

# Log format:
[TIMESTAMP] [LEVEL] [PROTOCOL] [STEP] [MESSAGE]
```

---

## TROUBLESHOOTING GUIDE

### Quick Diagnosis Flowchart

```
Issue Detected
    ↓
Is it a data issue?
├─ YES → Check Protocol 11 leakage report
│        Check data quality metrics
│        Verify split ratios
└─ NO → Continue
    ↓
Is it a model issue?
├─ YES → Check Protocol 12 baseline performance
│        Check algorithm selection
│        Verify hyperparameters
└─ NO → Continue
    ↓
Is it a training issue?
├─ YES → Check Protocol 13 training logs
│        Check GPU/memory usage
│        Verify convergence
└─ NO → Continue
    ↓
Check system requirements:
├─ Python version
├─ Library versions
├─ Disk space
├─ Memory availability
└─ GPU availability
```

---

## PRODUCTION DEPLOYMENT CHECKLIST

Before deploying to production:

- [ ] All 9 quality gates passed (3 per protocol)
- [ ] All artifacts generated and validated
- [ ] All automation scripts executed successfully
- [ ] All error handling tested
- [ ] Stakeholder sign-off obtained
- [ ] Documentation complete and reviewed
- [ ] Monitoring and alerting configured
- [ ] Rollback procedures documented
- [ ] Performance benchmarks met
- [ ] Security review completed

---

## NEXT STEPS

1. **Create Protocol 14**: Implement model evaluation and drift monitoring
2. **Implement Automation Scripts**: Create all referenced Python scripts
3. **Test End-to-End**: Run complete workflow with sample data
4. **Performance Optimization**: Implement parallel execution and caching
5. **Production Deployment**: Deploy to production after validation

---

**Document Version**: 1.0  
**Last Updated**: 2025-01-14  
**Next Review**: After Protocol 14 implementation


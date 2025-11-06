# Protocol 12: AI Model Evaluation & Drift Monitoring

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: ml_development
phase: "Phase 3: AI Model Development"
priority: critical
tags: [model-evaluation, drift-monitoring, fairness-testing, robustness]
triggers: [model-trained, evaluation-phase, production-monitoring]
```

## 1. Protocol Overview

**Purpose**: Comprehensive model evaluation including performance assessment, robustness testing, fairness evaluation, and continuous drift monitoring in production.

**Critical Success Factors**:
- Thorough evaluation across all data splits
- Fairness across demographic groups
- Robustness to edge cases
- Early drift detection
- Automated retraining triggers

## 2. Model Evaluation Workflow

### Step 1: Performance Evaluation
**Duration**: 3-4 hours

**Evaluation Framework**:
```python
# evaluation/model_evaluator.py

class ModelEvaluator:
    
    def comprehensive_evaluation(self, model, X_test, y_test, config):
        """Perform comprehensive model evaluation."""
        
        evaluation_results = {
            'timestamp': datetime.now().isoformat(),
            'model_id': config['model_id'],
            'metrics': {},
            'analysis': {},
            'visualizations': []
        }
        
        # Get predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else y_pred
        
        # Calculate metrics by task type
        if config['task_type'] == 'classification':
            evaluation_results['metrics'] = self.classification_metrics(
                y_test, y_pred, y_pred_proba
            )
            evaluation_results['analysis'] = self.classification_analysis(
                y_test, y_pred_proba
            )
        elif config['task_type'] == 'regression':
            evaluation_results['metrics'] = self.regression_metrics(
                y_test, y_pred
            )
            evaluation_results['analysis'] = self.regression_analysis(
                y_test, y_pred
            )
        
        # Generate visualizations
        evaluation_results['visualizations'] = self.create_visualizations(
            y_test, y_pred, y_pred_proba, config
        )
        
        return evaluation_results
    
    def classification_metrics(self, y_true, y_pred, y_pred_proba):
        """Calculate classification metrics."""
        
        metrics = {
            # Basic metrics
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted'),
            'recall': recall_score(y_true, y_pred, average='weighted'),
            'f1_score': f1_score(y_true, y_pred, average='weighted'),
            
            # Probabilistic metrics
            'auc_roc': roc_auc_score(y_true, y_pred_proba),
            'auc_pr': average_precision_score(y_true, y_pred_proba),
            'log_loss': log_loss(y_true, y_pred_proba),
            'brier_score': brier_score_loss(y_true, y_pred_proba),
            
            # Class-specific metrics
            'per_class_precision': precision_score(y_true, y_pred, average=None).tolist(),
            'per_class_recall': recall_score(y_true, y_pred, average=None).tolist(),
            'per_class_f1': f1_score(y_true, y_pred, average=None).tolist(),
            
            # Confusion matrix
            'confusion_matrix': confusion_matrix(y_true, y_pred).tolist(),
            
            # Additional metrics
            'matthews_corrcoef': matthews_corrcoef(y_true, y_pred),
            'cohen_kappa': cohen_kappa_score(y_true, y_pred),
            'balanced_accuracy': balanced_accuracy_score(y_true, y_pred)
        }
        
        return metrics
    
    def classification_analysis(self, y_true, y_pred_proba):
        """Perform classification analysis."""
        
        analysis = {}
        
        # Threshold analysis
        thresholds = np.arange(0.1, 1.0, 0.1)
        threshold_metrics = []
        
        for threshold in thresholds:
            y_pred_thresh = (y_pred_proba >= threshold).astype(int)
            threshold_metrics.append({
                'threshold': threshold,
                'precision': precision_score(y_true, y_pred_thresh),
                'recall': recall_score(y_true, y_pred_thresh),
                'f1': f1_score(y_true, y_pred_thresh)
            })
        
        analysis['threshold_analysis'] = threshold_metrics
        
        # Find optimal threshold
        f1_scores = [m['f1'] for m in threshold_metrics]
        optimal_idx = np.argmax(f1_scores)
        analysis['optimal_threshold'] = threshold_metrics[optimal_idx]
        
        # Calibration analysis
        fraction_positive, mean_predicted = calibration_curve(
            y_true, y_pred_proba, n_bins=10
        )
        analysis['calibration'] = {
            'fraction_positive': fraction_positive.tolist(),
            'mean_predicted': mean_predicted.tolist(),
            'ece': self.expected_calibration_error(y_true, y_pred_proba)
        }
        
        return analysis
```

### Step 2: Robustness Testing
**Duration**: 4-6 hours

**Robustness Tests**:
```python
# evaluation/robustness_testing.py

class RobustnessTester:
    
    def test_robustness(self, model, X_test, y_test, config):
        """Test model robustness to various perturbations."""
        
        robustness_results = {
            'noise_robustness': {},
            'adversarial_robustness': {},
            'edge_case_performance': {},
            'data_shift_robustness': {}
        }
        
        # Noise injection tests
        noise_levels = [0.01, 0.05, 0.1, 0.2]
        for noise_level in noise_levels:
            X_noisy = self.add_gaussian_noise(X_test, noise_level)
            y_pred_noisy = model.predict(X_noisy)
            
            robustness_results['noise_robustness'][f'noise_{noise_level}'] = {
                'accuracy': accuracy_score(y_test, y_pred_noisy),
                'performance_drop': self.calculate_performance_drop(
                    y_test, model.predict(X_test), y_pred_noisy
                )
            }
        
        # Adversarial examples (for neural networks)
        if config.get('test_adversarial', False):
            robustness_results['adversarial_robustness'] = \
                self.test_adversarial_robustness(model, X_test, y_test)
        
        # Edge case testing
        edge_cases = self.identify_edge_cases(X_test, y_test)
        for case_name, (X_edge, y_edge) in edge_cases.items():
            if len(X_edge) > 0:
                y_pred_edge = model.predict(X_edge)
                robustness_results['edge_case_performance'][case_name] = {
                    'n_samples': len(X_edge),
                    'accuracy': accuracy_score(y_edge, y_pred_edge)
                }
        
        # Data shift simulation
        shift_types = ['covariate_shift', 'label_shift', 'concept_drift']
        for shift_type in shift_types:
            X_shifted, y_shifted = self.simulate_data_shift(
                X_test, y_test, shift_type
            )
            y_pred_shifted = model.predict(X_shifted)
            
            robustness_results['data_shift_robustness'][shift_type] = {
                'accuracy': accuracy_score(y_shifted, y_pred_shifted),
                'distribution_distance': self.calculate_distribution_distance(
                    X_test, X_shifted
                )
            }
        
        return robustness_results
    
    def identify_edge_cases(self, X, y):
        """Identify edge cases in the data."""
        
        edge_cases = {}
        
        # Outliers (using isolation forest)
        iso_forest = IsolationForest(contamination=0.1, random_state=42)
        outlier_mask = iso_forest.fit_predict(X) == -1
        edge_cases['outliers'] = (X[outlier_mask], y[outlier_mask])
        
        # Boundary cases (near decision boundary)
        if hasattr(self.model, 'decision_function'):
            decision_scores = np.abs(self.model.decision_function(X))
            boundary_mask = decision_scores < np.percentile(decision_scores, 10)
            edge_cases['boundary'] = (X[boundary_mask], y[boundary_mask])
        
        # High uncertainty cases (for probabilistic models)
        if hasattr(self.model, 'predict_proba'):
            probas = self.model.predict_proba(X)
            entropy = -np.sum(probas * np.log(probas + 1e-10), axis=1)
            high_entropy_mask = entropy > np.percentile(entropy, 90)
            edge_cases['high_uncertainty'] = (X[high_entropy_mask], y[high_entropy_mask])
        
        return edge_cases
```

### Step 3: Fairness Assessment
**Duration**: 3-4 hours

**Fairness Evaluation**:
```python
# evaluation/fairness_assessment.py
from fairlearn.metrics import demographic_parity_difference, equalized_odds_difference

class FairnessAssessor:
    
    def assess_fairness(self, model, X_test, y_test, sensitive_features, config):
        """Assess model fairness across demographic groups."""
        
        fairness_results = {
            'overall_metrics': {},
            'group_metrics': {},
            'bias_metrics': {},
            'mitigation_recommendations': []
        }
        
        y_pred = model.predict(X_test)
        
        for feature_name, feature_values in sensitive_features.items():
            fairness_results['group_metrics'][feature_name] = {}
            
            # Calculate metrics per group
            unique_groups = np.unique(feature_values)
            for group in unique_groups:
                group_mask = feature_values == group
                group_metrics = {
                    'size': np.sum(group_mask),
                    'positive_rate': np.mean(y_test[group_mask]),
                    'predicted_positive_rate': np.mean(y_pred[group_mask]),
                    'accuracy': accuracy_score(y_test[group_mask], y_pred[group_mask]),
                    'precision': precision_score(y_test[group_mask], y_pred[group_mask]),
                    'recall': recall_score(y_test[group_mask], y_pred[group_mask])
                }
                fairness_results['group_metrics'][feature_name][str(group)] = group_metrics
            
            # Calculate bias metrics
            fairness_results['bias_metrics'][feature_name] = {
                'demographic_parity_diff': demographic_parity_difference(
                    y_test, y_pred, sensitive_features=feature_values
                ),
                'equalized_odds_diff': equalized_odds_difference(
                    y_test, y_pred, sensitive_features=feature_values
                ),
                'disparate_impact': self.calculate_disparate_impact(
                    y_pred, feature_values
                ),
                'statistical_parity_diff': self.calculate_statistical_parity(
                    y_pred, feature_values
                )
            }
            
            # Generate mitigation recommendations
            if abs(fairness_results['bias_metrics'][feature_name]['demographic_parity_diff']) > 0.1:
                fairness_results['mitigation_recommendations'].append(
                    f"High demographic parity difference for {feature_name}. "
                    "Consider reweighting or threshold optimization."
                )
        
        # Calculate overall fairness score
        fairness_results['overall_metrics']['fairness_score'] = \
            self.calculate_fairness_score(fairness_results['bias_metrics'])
        
        return fairness_results
    
    def calculate_disparate_impact(self, y_pred, sensitive_feature):
        """Calculate disparate impact ratio."""
        
        groups = np.unique(sensitive_feature)
        if len(groups) != 2:
            return None
        
        positive_rate_0 = np.mean(y_pred[sensitive_feature == groups[0]])
        positive_rate_1 = np.mean(y_pred[sensitive_feature == groups[1]])
        
        if positive_rate_1 == 0:
            return float('inf')
        
        return positive_rate_0 / positive_rate_1
```

### Step 4: Production Monitoring Setup
**Duration**: 4-5 hours

**Drift Monitoring Configuration**:
```python
# monitoring/drift_monitor.py
from alibi_detect.cd import KSDrift, MMDDrift, ChiSquareDrift
from alibi_detect.cd import TabularDrift

class DriftMonitor:
    
    def __init__(self, reference_data, config):
        """Initialize drift monitoring."""
        
        self.reference_data = reference_data
        self.config = config
        self.detectors = {}
        
        # Initialize different drift detectors
        self.setup_drift_detectors()
    
    def setup_drift_detectors(self):
        """Setup various drift detection methods."""
        
        # Kolmogorov-Smirnov test for numerical features
        self.detectors['ks_drift'] = KSDrift(
            self.reference_data,
            p_val=self.config.get('ks_threshold', 0.05),
            alternative='two-sided'
        )
        
        # Maximum Mean Discrepancy for multivariate drift
        self.detectors['mmd_drift'] = MMDDrift(
            self.reference_data,
            p_val=self.config.get('mmd_threshold', 0.05),
            n_permutations=100
        )
        
        # Chi-square test for categorical features
        if self.config.get('categorical_features'):
            self.detectors['chi2_drift'] = ChiSquareDrift(
                self.reference_data[:, self.config['categorical_features']],
                p_val=self.config.get('chi2_threshold', 0.05)
            )
        
        # Tabular drift detector (combines multiple tests)
        self.detectors['tabular_drift'] = TabularDrift(
            self.reference_data,
            p_val=self.config.get('tabular_threshold', 0.05),
            categories_per_feature=self.config.get('categorical_features', {})
        )
    
    def detect_drift(self, production_data):
        """Detect drift in production data."""
        
        drift_results = {
            'timestamp': datetime.now().isoformat(),
            'drift_detected': False,
            'drift_scores': {},
            'feature_drift': {},
            'recommendations': []
        }
        
        # Run each detector
        for detector_name, detector in self.detectors.items():
            result = detector.predict(production_data)
            
            drift_results['drift_scores'][detector_name] = {
                'is_drift': result['data']['is_drift'],
                'p_value': result['data'].get('p_val', None),
                'distance': result['data'].get('distance', None)
            }
            
            if result['data']['is_drift']:
                drift_results['drift_detected'] = True
        
        # Feature-level drift analysis
        drift_results['feature_drift'] = self.analyze_feature_drift(
            production_data
        )
        
        # Generate recommendations
        if drift_results['drift_detected']:
            drift_results['recommendations'] = self.generate_drift_recommendations(
                drift_results
            )
        
        return drift_results
    
    def analyze_feature_drift(self, production_data):
        """Analyze drift at feature level."""
        
        feature_drift = {}
        
        for i, feature_name in enumerate(self.config['feature_names']):
            # Calculate drift metrics for each feature
            ref_feature = self.reference_data[:, i]
            prod_feature = production_data[:, i]
            
            # KS test for numerical features
            if self.is_numerical(ref_feature):
                ks_stat, p_value = ks_2samp(ref_feature, prod_feature)
                
                # Population Stability Index (PSI)
                psi = self.calculate_psi(ref_feature, prod_feature)
                
                feature_drift[feature_name] = {
                    'ks_statistic': ks_stat,
                    'ks_p_value': p_value,
                    'psi': psi,
                    'is_drifted': p_value < 0.05 or psi > 0.1
                }
            else:
                # Chi-square test for categorical
                chi2, p_value = self.chi_square_test(ref_feature, prod_feature)
                
                feature_drift[feature_name] = {
                    'chi2_statistic': chi2,
                    'chi2_p_value': p_value,
                    'is_drifted': p_value < 0.05
                }
        
        return feature_drift
    
    def calculate_psi(self, reference, production, buckets=10):
        """Calculate Population Stability Index."""
        
        # Create bins based on reference data
        _, bins = np.histogram(reference, bins=buckets)
        bins[0] = -np.inf
        bins[-1] = np.inf
        
        # Calculate frequencies
        ref_counts = np.histogram(reference, bins=bins)[0]
        prod_counts = np.histogram(production, bins=bins)[0]
        
        # Calculate percentages
        ref_percents = ref_counts / len(reference)
        prod_percents = prod_counts / len(production)
        
        # Avoid division by zero
        ref_percents = np.where(ref_percents == 0, 0.0001, ref_percents)
        prod_percents = np.where(prod_percents == 0, 0.0001, prod_percents)
        
        # Calculate PSI
        psi = np.sum((prod_percents - ref_percents) * np.log(prod_percents / ref_percents))
        
        return psi
```

### Step 5: Retraining Trigger Definition
**Duration**: 2-3 hours

**Automated Retraining Logic**:
```python
# monitoring/retraining_trigger.py

class RetrainingTrigger:
    
    def __init__(self, config):
        """Initialize retraining trigger system."""
        
        self.config = config
        self.trigger_history = []
        
    def evaluate_retraining_need(self, monitoring_data):
        """Evaluate if model retraining is needed."""
        
        trigger_evaluation = {
            'timestamp': datetime.now().isoformat(),
            'should_retrain': False,
            'trigger_reasons': [],
            'urgency': 'low',  # low, medium, high, critical
            'recommended_actions': []
        }
        
        # Performance degradation trigger
        if self.check_performance_degradation(monitoring_data):
            trigger_evaluation['should_retrain'] = True
            trigger_evaluation['trigger_reasons'].append('performance_degradation')
            trigger_evaluation['urgency'] = 'high'
        
        # Data drift trigger
        if self.check_data_drift(monitoring_data):
            trigger_evaluation['should_retrain'] = True
            trigger_evaluation['trigger_reasons'].append('data_drift')
            trigger_evaluation['urgency'] = max(
                trigger_evaluation['urgency'], 'medium'
            )
        
        # Concept drift trigger
        if self.check_concept_drift(monitoring_data):
            trigger_evaluation['should_retrain'] = True
            trigger_evaluation['trigger_reasons'].append('concept_drift')
            trigger_evaluation['urgency'] = 'critical'
        
        # Time-based trigger
        if self.check_time_based_trigger(monitoring_data):
            trigger_evaluation['should_retrain'] = True
            trigger_evaluation['trigger_reasons'].append('scheduled_retraining')
            trigger_evaluation['urgency'] = max(
                trigger_evaluation['urgency'], 'low'
            )
        
        # Volume-based trigger
        if self.check_volume_trigger(monitoring_data):
            trigger_evaluation['should_retrain'] = True
            trigger_evaluation['trigger_reasons'].append('new_data_volume')
            trigger_evaluation['urgency'] = max(
                trigger_evaluation['urgency'], 'medium'
            )
        
        # Generate recommended actions
        if trigger_evaluation['should_retrain']:
            trigger_evaluation['recommended_actions'] = \
                self.generate_retraining_recommendations(trigger_evaluation)
        
        # Log trigger evaluation
        self.trigger_history.append(trigger_evaluation)
        
        return trigger_evaluation
    
    def check_performance_degradation(self, monitoring_data):
        """Check for performance degradation."""
        
        current_metrics = monitoring_data['performance_metrics']
        baseline_metrics = self.config['baseline_metrics']
        
        # Check primary metric
        primary_metric = self.config['primary_metric']
        current_value = current_metrics.get(primary_metric, 0)
        baseline_value = baseline_metrics.get(primary_metric, 1)
        
        # Calculate relative degradation
        degradation = (baseline_value - current_value) / baseline_value
        
        # Trigger if degradation exceeds threshold
        threshold = self.config.get('performance_threshold', 0.05)
        
        return degradation > threshold
    
    def check_data_drift(self, monitoring_data):
        """Check for data drift."""
        
        drift_scores = monitoring_data.get('drift_scores', {})
        
        # Check if any drift detector triggered
        for detector, results in drift_scores.items():
            if results.get('is_drift', False):
                return True
        
        # Check PSI threshold
        psi_scores = monitoring_data.get('psi_scores', {})
        psi_threshold = self.config.get('psi_threshold', 0.2)
        
        for feature, psi in psi_scores.items():
            if psi > psi_threshold:
                return True
        
        return False
```

## 3. Monitoring Dashboard

### Real-time Monitoring
```python
# monitoring/dashboard.py

class MonitoringDashboard:
    
    def __init__(self, model_id, config):
        """Initialize monitoring dashboard."""
        
        self.model_id = model_id
        self.config = config
        self.metrics_buffer = []
        
    def update_dashboard(self, new_metrics):
        """Update dashboard with new metrics."""
        
        # Add to buffer
        self.metrics_buffer.append(new_metrics)
        
        # Keep only recent data
        max_buffer = self.config.get('max_buffer_size', 1000)
        if len(self.metrics_buffer) > max_buffer:
            self.metrics_buffer = self.metrics_buffer[-max_buffer:]
        
        # Calculate aggregated metrics
        dashboard_data = {
            'model_id': self.model_id,
            'last_updated': datetime.now().isoformat(),
            'current_metrics': new_metrics,
            'aggregated_metrics': self.calculate_aggregated_metrics(),
            'drift_status': self.get_drift_status(),
            'alerts': self.generate_alerts(),
            'visualizations': self.create_visualizations()
        }
        
        return dashboard_data
    
    def calculate_aggregated_metrics(self):
        """Calculate aggregated metrics over time windows."""
        
        aggregated = {}
        
        for window_name, window_size in [('1h', 60), ('24h', 1440), ('7d', 10080)]:
            window_metrics = self.metrics_buffer[-window_size:]
            
            if window_metrics:
                aggregated[window_name] = {
                    'mean_accuracy': np.mean([m['accuracy'] for m in window_metrics]),
                    'std_accuracy': np.std([m['accuracy'] for m in window_metrics]),
                    'min_accuracy': np.min([m['accuracy'] for m in window_metrics]),
                    'max_accuracy': np.max([m['accuracy'] for m in window_metrics]),
                    'drift_detections': sum([m.get('drift_detected', False) for m in window_metrics])
                }
        
        return aggregated
```

## 4. Quality Gates

### Gate 1: Evaluation Completeness
- [ ] All test sets evaluated
- [ ] Metrics calculated and logged
- [ ] Robustness tests passed
- [ ] Fairness assessment completed

### Gate 2: Performance Thresholds
- [ ] Primary metric meets target
- [ ] No significant bias detected
- [ ] Robustness within acceptable range
- [ ] Calibration error < threshold

### Gate 3: Monitoring Readiness
- [ ] Drift detectors configured
- [ ] Retraining triggers defined
- [ ] Dashboard operational
- [ ] Alerting configured

## 5. Deliverables

### Required Outputs
1. **Evaluation Report** (`evaluation_report.md`)
2. **Fairness Assessment** (`fairness_report.md`)
3. **Robustness Results** (`robustness_testing.json`)
4. **Monitoring Configuration** (`monitoring_config.yaml`)
5. **Drift Detection Results** (`drift_analysis.json`)
6. **Retraining Recommendations** (`retraining_plan.md`)

## 6. Success Criteria

- **Model Performance**: Meets all target metrics
- **Fairness**: Bias metrics within acceptable thresholds
- **Robustness**: Performance degradation < 10% under perturbations
- **Monitoring**: Real-time drift detection operational
- **Automation**: Retraining triggers functioning correctly

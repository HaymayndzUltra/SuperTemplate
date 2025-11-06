# Protocol 14: AI Model Validation & Evaluation

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: ml_development
phase: "Phase 3: AI Model Development"
priority: critical
tags: [model-validation, cross-validation, holdout-testing, stability-analysis]
triggers: [model-trained, validation-phase, performance-testing]
```

## 1. Protocol Overview

**Purpose**: Rigorously validate model performance through cross-validation, holdout testing, overfitting detection, and stability analysis to ensure reliable production deployment.

**Critical Success Factors**:
- Unbiased performance estimation
- Overfitting detection and prevention
- Model stability across data splits
- Comprehensive validation metrics
- Production-readiness assessment

## 2. Validation Workflow

### Step 1: Cross-Validation Strategy
**Duration**: 3-4 hours

**CV Implementation**:
```python
# validation/cross_validator.py

class CrossValidator:
    
    def perform_cross_validation(self, model, X, y, config):
        """Perform comprehensive cross-validation."""
        
        cv_results = {
            'strategy': config.get('cv_strategy', 'stratified_kfold'),
            'n_splits': config.get('n_splits', 5),
            'scores': {},
            'fold_details': [],
            'aggregated_metrics': {}
        }
        
        # Select CV strategy
        cv_splitter = self.get_cv_splitter(cv_results['strategy'], cv_results['n_splits'], config)
        
        # Perform cross-validation
        for fold_idx, (train_idx, val_idx) in enumerate(cv_splitter.split(X, y)):
            X_train_fold, X_val_fold = X[train_idx], X[val_idx]
            y_train_fold, y_val_fold = y[train_idx], y[val_idx]
            
            # Train model on fold
            fold_model = clone(model)
            fold_model.fit(X_train_fold, y_train_fold)
            
            # Predict on validation fold
            y_pred = fold_model.predict(X_val_fold)
            y_pred_proba = fold_model.predict_proba(X_val_fold)[:, 1] if hasattr(fold_model, 'predict_proba') else y_pred
            
            # Calculate metrics
            fold_metrics = self.calculate_fold_metrics(y_val_fold, y_pred, y_pred_proba, config)
            
            # Store fold details
            cv_results['fold_details'].append({
                'fold': fold_idx + 1,
                'train_size': len(train_idx),
                'val_size': len(val_idx),
                'metrics': fold_metrics
            })
        
        # Aggregate results
        cv_results['aggregated_metrics'] = self.aggregate_cv_results(cv_results['fold_details'])
        
        # Calculate stability metrics
        cv_results['stability'] = self.calculate_stability(cv_results['fold_details'])
        
        return cv_results
    
    def get_cv_splitter(self, strategy, n_splits, config):
        """Get appropriate CV splitter."""
        
        if strategy == 'stratified_kfold':
            return StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
        elif strategy == 'kfold':
            return KFold(n_splits=n_splits, shuffle=True, random_state=42)
        elif strategy == 'time_series':
            return TimeSeriesSplit(n_splits=n_splits)
        elif strategy == 'group_kfold':
            return GroupKFold(n_splits=n_splits)
        else:
            raise ValueError(f"Unknown CV strategy: {strategy}")
    
    def calculate_fold_metrics(self, y_true, y_pred, y_pred_proba, config):
        """Calculate metrics for a single fold."""
        
        metrics = {}
        
        if config['task_type'] in ['binary_classification', 'multiclass_classification']:
            metrics = {
                'accuracy': accuracy_score(y_true, y_pred),
                'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
                'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
                'f1_score': f1_score(y_true, y_pred, average='weighted', zero_division=0),
                'auc_roc': roc_auc_score(y_true, y_pred_proba) if y_pred_proba is not None else None
            }
        else:
            metrics = {
                'mse': mean_squared_error(y_true, y_pred),
                'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
                'mae': mean_absolute_error(y_true, y_pred),
                'r2': r2_score(y_true, y_pred)
            }
        
        return metrics
    
    def aggregate_cv_results(self, fold_details):
        """Aggregate metrics across folds."""
        
        all_metrics = {}
        
        # Extract all metric names
        metric_names = fold_details[0]['metrics'].keys()
        
        for metric_name in metric_names:
            values = [fold['metrics'][metric_name] for fold in fold_details if fold['metrics'][metric_name] is not None]
            
            if values:
                all_metrics[metric_name] = {
                    'mean': np.mean(values),
                    'std': np.std(values),
                    'min': np.min(values),
                    'max': np.max(values),
                    'cv': np.std(values) / np.mean(values) if np.mean(values) \!= 0 else 0  # Coefficient of variation
                }
        
        return all_metrics
    
    def calculate_stability(self, fold_details):
        """Calculate model stability across folds."""
        
        stability_metrics = {}
        
        # Extract primary metric values
        primary_values = [fold['metrics'].get('accuracy', fold['metrics'].get('r2', 0)) 
                         for fold in fold_details]
        
        stability_metrics['variance'] = np.var(primary_values)
        stability_metrics['std_dev'] = np.std(primary_values)
        stability_metrics['range'] = np.max(primary_values) - np.min(primary_values)
        stability_metrics['coefficient_of_variation'] = np.std(primary_values) / np.mean(primary_values) if np.mean(primary_values) \!= 0 else 0
        
        # Stability score (0-1, higher is more stable)
        stability_metrics['stability_score'] = 1 - min(stability_metrics['coefficient_of_variation'], 1.0)
        
        return stability_metrics
```

### Step 2: Holdout Set Validation
**Duration**: 2-3 hours

**Holdout Testing**:
```python
# validation/holdout_validator.py

class HoldoutValidator:
    
    def validate_on_holdout(self, model, X_test, y_test, config):
        """Validate model on holdout test set."""
        
        holdout_results = {
            'test_size': len(X_test),
            'predictions': {},
            'metrics': {},
            'confusion_analysis': {},
            'error_analysis': {}
        }
        
        # Generate predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
        
        holdout_results['predictions'] = {
            'y_pred': y_pred,
            'y_pred_proba': y_pred_proba
        }
        
        # Calculate comprehensive metrics
        holdout_results['metrics'] = self.calculate_comprehensive_metrics(
            y_test, y_pred, y_pred_proba, config
        )
        
        # Confusion matrix analysis
        if config['task_type'] in ['binary_classification', 'multiclass_classification']:
            holdout_results['confusion_analysis'] = self.analyze_confusion_matrix(
                y_test, y_pred
            )
        
        # Error analysis
        holdout_results['error_analysis'] = self.perform_error_analysis(
            X_test, y_test, y_pred, config
        )
        
        return holdout_results
    
    def calculate_comprehensive_metrics(self, y_true, y_pred, y_pred_proba, config):
        """Calculate comprehensive evaluation metrics."""
        
        metrics = {}
        
        if config['task_type'] in ['binary_classification', 'multiclass_classification']:
            metrics = {
                # Basic metrics
                'accuracy': accuracy_score(y_true, y_pred),
                'balanced_accuracy': balanced_accuracy_score(y_true, y_pred),
                'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
                'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
                'f1_score': f1_score(y_true, y_pred, average='weighted', zero_division=0),
                
                # Advanced metrics
                'matthews_corrcoef': matthews_corrcoef(y_true, y_pred),
                'cohen_kappa': cohen_kappa_score(y_true, y_pred),
                
                # Probabilistic metrics
                'auc_roc': roc_auc_score(y_true, y_pred_proba) if y_pred_proba is not None else None,
                'auc_pr': average_precision_score(y_true, y_pred_proba) if y_pred_proba is not None else None,
                'log_loss': log_loss(y_true, y_pred_proba) if y_pred_proba is not None else None,
                'brier_score': brier_score_loss(y_true, y_pred_proba) if y_pred_proba is not None else None
            }
        else:
            metrics = {
                'mse': mean_squared_error(y_true, y_pred),
                'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
                'mae': mean_absolute_error(y_true, y_pred),
                'r2': r2_score(y_true, y_pred),
                'mape': mean_absolute_percentage_error(y_true, y_pred),
                'max_error': max_error(y_true, y_pred),
                'explained_variance': explained_variance_score(y_true, y_pred)
            }
        
        return metrics
    
    def analyze_confusion_matrix(self, y_true, y_pred):
        """Analyze confusion matrix in detail."""
        
        cm = confusion_matrix(y_true, y_pred)
        
        analysis = {
            'confusion_matrix': cm.tolist(),
            'true_positives': int(cm[1, 1]) if cm.shape == (2, 2) else None,
            'true_negatives': int(cm[0, 0]) if cm.shape == (2, 2) else None,
            'false_positives': int(cm[0, 1]) if cm.shape == (2, 2) else None,
            'false_negatives': int(cm[1, 0]) if cm.shape == (2, 2) else None,
            'total_errors': int(np.sum(cm) - np.trace(cm)),
            'error_rate': float((np.sum(cm) - np.trace(cm)) / np.sum(cm))
        }
        
        # Calculate per-class metrics
        if cm.shape[0] > 2:
            analysis['per_class_accuracy'] = {}
            for i in range(cm.shape[0]):
                class_total = np.sum(cm[i, :])
                class_correct = cm[i, i]
                analysis['per_class_accuracy'][f'class_{i}'] = float(class_correct / class_total) if class_total > 0 else 0
        
        return analysis
    
    def perform_error_analysis(self, X_test, y_true, y_pred, config):
        """Analyze prediction errors."""
        
        error_analysis = {
            'error_indices': [],
            'error_distribution': {},
            'high_confidence_errors': []
        }
        
        # Identify error indices
        error_mask = y_true \!= y_pred
        error_indices = np.where(error_mask)[0]
        error_analysis['error_indices'] = error_indices.tolist()
        
        # Error distribution by true class
        for class_val in np.unique(y_true):
            class_mask = y_true == class_val
            class_errors = np.sum(error_mask & class_mask)
            class_total = np.sum(class_mask)
            error_analysis['error_distribution'][f'class_{class_val}'] = {
                'errors': int(class_errors),
                'total': int(class_total),
                'error_rate': float(class_errors / class_total) if class_total > 0 else 0
            }
        
        return error_analysis
```

### Step 3: Overfitting Detection
**Duration**: 2-3 hours

**Overfitting Analysis**:
```python
# validation/overfitting_detector.py

class OverfittingDetector:
    
    def detect_overfitting(self, model, X_train, y_train, X_val, y_val, X_test, y_test, config):
        """Comprehensive overfitting detection."""
        
        overfitting_report = {
            'train_metrics': {},
            'val_metrics': {},
            'test_metrics': {},
            'performance_gaps': {},
            'overfitting_indicators': {},
            'severity': 'none'  # none, mild, moderate, severe
        }
        
        # Calculate metrics on all splits
        overfitting_report['train_metrics'] = self.calculate_metrics(model, X_train, y_train, config)
        overfitting_report['val_metrics'] = self.calculate_metrics(model, X_val, y_val, config)
        overfitting_report['test_metrics'] = self.calculate_metrics(model, X_test, y_test, config)
        
        # Calculate performance gaps
        primary_metric = config.get('primary_metric', 'accuracy')
        
        train_score = overfitting_report['train_metrics'][primary_metric]
        val_score = overfitting_report['val_metrics'][primary_metric]
        test_score = overfitting_report['test_metrics'][primary_metric]
        
        overfitting_report['performance_gaps'] = {
            'train_val_gap': train_score - val_score,
            'train_test_gap': train_score - test_score,
            'val_test_gap': val_score - test_score,
            'train_val_ratio': val_score / train_score if train_score \!= 0 else 0,
            'train_test_ratio': test_score / train_score if train_score \!= 0 else 0
        }
        
        # Overfitting indicators
        overfitting_report['overfitting_indicators'] = self.calculate_overfitting_indicators(
            overfitting_report['performance_gaps'], config
        )
        
        # Determine severity
        overfitting_report['severity'] = self.determine_overfitting_severity(
            overfitting_report['overfitting_indicators']
        )
        
        # Generate recommendations
        overfitting_report['recommendations'] = self.generate_overfitting_recommendations(
            overfitting_report['severity'], overfitting_report['overfitting_indicators']
        )
        
        return overfitting_report
    
    def calculate_metrics(self, model, X, y, config):
        """Calculate metrics on a dataset."""
        
        y_pred = model.predict(X)
        y_pred_proba = model.predict_proba(X)[:, 1] if hasattr(model, 'predict_proba') else None
        
        if config['task_type'] in ['binary_classification', 'multiclass_classification']:
            return {
                'accuracy': accuracy_score(y, y_pred),
                'precision': precision_score(y, y_pred, average='weighted', zero_division=0),
                'recall': recall_score(y, y_pred, average='weighted', zero_division=0),
                'f1_score': f1_score(y, y_pred, average='weighted', zero_division=0),
                'auc_roc': roc_auc_score(y, y_pred_proba) if y_pred_proba is not None else None
            }
        else:
            return {
                'mse': mean_squared_error(y, y_pred),
                'rmse': np.sqrt(mean_squared_error(y, y_pred)),
                'mae': mean_absolute_error(y, y_pred),
                'r2': r2_score(y, y_pred)
            }
    
    def calculate_overfitting_indicators(self, gaps, config):
        """Calculate overfitting indicators."""
        
        indicators = {}
        
        # Gap-based indicators
        indicators['large_train_val_gap'] = gaps['train_val_gap'] > 0.1
        indicators['large_train_test_gap'] = gaps['train_test_gap'] > 0.1
        indicators['low_val_train_ratio'] = gaps['train_val_ratio'] < 0.9
        
        # Severity indicators
        indicators['gap_magnitude'] = max(gaps['train_val_gap'], gaps['train_test_gap'])
        
        return indicators
    
    def determine_overfitting_severity(self, indicators):
        """Determine overfitting severity level."""
        
        gap = indicators['gap_magnitude']
        
        if gap < 0.05:
            return 'none'
        elif gap < 0.1:
            return 'mild'
        elif gap < 0.2:
            return 'moderate'
        else:
            return 'severe'
    
    def generate_overfitting_recommendations(self, severity, indicators):
        """Generate recommendations based on overfitting severity."""
        
        recommendations = []
        
        if severity == 'none':
            recommendations.append("Model shows good generalization. Proceed with deployment.")
        elif severity == 'mild':
            recommendations.append("Minor overfitting detected. Consider slight regularization increase.")
            recommendations.append("Monitor performance on new data.")
        elif severity == 'moderate':
            recommendations.append("Moderate overfitting detected. Implement regularization techniques.")
            recommendations.append("Consider: L1/L2 regularization, dropout, early stopping.")
            recommendations.append("Reduce model complexity or increase training data.")
        else:  # severe
            recommendations.append("Severe overfitting detected. Model requires significant changes.")
            recommendations.append("Actions: Reduce model complexity, add strong regularization.")
            recommendations.append("Collect more training data if possible.")
            recommendations.append("Consider simpler model architectures.")
        
        return recommendations
```

### Step 4: Model Stability Testing
**Duration**: 3-4 hours

**Stability Analysis**:
```python
# validation/stability_tester.py

class StabilityTester:
    
    def test_model_stability(self, model, X_test, y_test, config):
        """Test model stability under various conditions."""
        
        stability_results = {
            'bootstrap_stability': {},
            'perturbation_stability': {},
            'prediction_consistency': {},
            'overall_stability_score': 0.0
        }
        
        # Bootstrap stability
        stability_results['bootstrap_stability'] = self.bootstrap_stability_test(
            model, X_test, y_test, config
        )
        
        # Perturbation stability
        stability_results['perturbation_stability'] = self.perturbation_stability_test(
            model, X_test, y_test, config
        )
        
        # Prediction consistency
        stability_results['prediction_consistency'] = self.prediction_consistency_test(
            model, X_test, config
        )
        
        # Calculate overall stability score
        stability_results['overall_stability_score'] = self.calculate_overall_stability(
            stability_results
        )
        
        return stability_results
    
    def bootstrap_stability_test(self, model, X_test, y_test, config):
        """Test stability using bootstrap resampling."""
        
        n_bootstrap = config.get('n_bootstrap', 100)
        primary_metric = config.get('primary_metric', 'accuracy')
        
        bootstrap_scores = []
        
        for i in range(n_bootstrap):
            # Bootstrap sample
            indices = np.random.choice(len(X_test), size=len(X_test), replace=True)
            X_boot = X_test[indices]
            y_boot = y_test[indices]
            
            # Predict and score
            y_pred = model.predict(X_boot)
            
            if config['task_type'] in ['binary_classification', 'multiclass_classification']:
                score = accuracy_score(y_boot, y_pred)
            else:
                score = r2_score(y_boot, y_pred)
            
            bootstrap_scores.append(score)
        
        return {
            'mean_score': np.mean(bootstrap_scores),
            'std_score': np.std(bootstrap_scores),
            'confidence_interval_95': (
                np.percentile(bootstrap_scores, 2.5),
                np.percentile(bootstrap_scores, 97.5)
            ),
            'coefficient_of_variation': np.std(bootstrap_scores) / np.mean(bootstrap_scores) if np.mean(bootstrap_scores) \!= 0 else 0
        }
    
    def perturbation_stability_test(self, model, X_test, y_test, config):
        """Test stability under input perturbations."""
        
        perturbation_levels = [0.01, 0.05, 0.1]
        perturbation_results = {}
        
        # Get baseline predictions
        y_pred_baseline = model.predict(X_test)
        
        for level in perturbation_levels:
            # Add Gaussian noise
            X_perturbed = X_test + np.random.normal(0, level, X_test.shape)
            y_pred_perturbed = model.predict(X_perturbed)
            
            # Calculate prediction agreement
            agreement = np.mean(y_pred_baseline == y_pred_perturbed)
            
            # Calculate performance on perturbed data
            if config['task_type'] in ['binary_classification', 'multiclass_classification']:
                perturbed_score = accuracy_score(y_test, y_pred_perturbed)
            else:
                perturbed_score = r2_score(y_test, y_pred_perturbed)
            
            perturbation_results[f'noise_{level}'] = {
                'prediction_agreement': agreement,
                'perturbed_score': perturbed_score
            }
        
        return perturbation_results
    
    def prediction_consistency_test(self, model, X_test, config):
        """Test prediction consistency across multiple runs."""
        
        n_runs = config.get('n_consistency_runs', 10)
        
        predictions = []
        for i in range(n_runs):
            y_pred = model.predict(X_test)
            predictions.append(y_pred)
        
        # Calculate consistency
        predictions_array = np.array(predictions)
        consistency = np.mean([np.array_equal(predictions_array[0], predictions_array[i]) 
                              for i in range(1, n_runs)])
        
        return {
            'consistency_rate': consistency,
            'is_deterministic': consistency == 1.0
        }
    
    def calculate_overall_stability(self, stability_results):
        """Calculate overall stability score (0-1)."""
        
        # Bootstrap stability component
        bootstrap_cv = stability_results['bootstrap_stability']['coefficient_of_variation']
        bootstrap_score = max(0, 1 - bootstrap_cv)
        
        # Perturbation stability component
        perturbation_scores = [
            result['prediction_agreement'] 
            for result in stability_results['perturbation_stability'].values()
        ]
        perturbation_score = np.mean(perturbation_scores)
        
        # Consistency component
        consistency_score = stability_results['prediction_consistency']['consistency_rate']
        
        # Weighted average
        overall_score = (
            0.4 * bootstrap_score +
            0.4 * perturbation_score +
            0.2 * consistency_score
        )
        
        return overall_score
```

## 3. Quality Gates

### Gate 1: Cross-Validation Complete
- [ ] CV strategy appropriate for data
- [ ] All folds completed successfully
- [ ] Metrics aggregated correctly
- [ ] Stability metrics calculated

### Gate 2: Holdout Validation Passed
- [ ] Test set performance meets threshold
- [ ] No significant overfitting detected
- [ ] Error analysis completed
- [ ] Confusion matrix analyzed

### Gate 3: Stability Confirmed
- [ ] Bootstrap stability acceptable (CV < 0.1)
- [ ] Perturbation stability > 0.9
- [ ] Prediction consistency verified
- [ ] Overall stability score > 0.8

## 4. Deliverables

### Required Outputs
1. **Validation Report** (`validation-report.md`)
2. **CV Scores** (`cv-scores.json`)
3. **Stability Analysis** (`stability-analysis.md`)
4. **Overfitting Report** (`overfitting-report.md`)
5. **Error Analysis** (`error-analysis.json`)

### Evidence Package Structure
```
evidence/protocol-14-model-validation/
├── reports/
│   ├── validation-report.md
│   ├── stability-analysis.md
│   └── overfitting-report.md
├── metrics/
│   ├── cv-scores.json
│   ├── holdout-metrics.json
│   └── stability-metrics.json
├── analysis/
│   ├── error-analysis.json
│   ├── confusion-matrix.json
│   └── performance-gaps.json
└── visualizations/
    ├── cv-scores-plot.png
    ├── learning-curves.png
    └── stability-charts.png
```

## 5. Success Criteria

- **CV Performance**: Mean CV score meets target with std < 0.05
- **Holdout Performance**: Test score within 5% of CV mean
- **No Severe Overfitting**: Train-test gap < 0.1
- **High Stability**: Overall stability score > 0.8
- **Production Ready**: All quality gates passed

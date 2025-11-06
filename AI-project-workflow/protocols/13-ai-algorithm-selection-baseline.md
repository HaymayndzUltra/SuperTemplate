# Protocol 13: AI Algorithm Selection & Baseline Model

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: ml_development
phase: "Phase 3: AI Model Development"
priority: critical
tags: [algorithm-selection, baseline-model, benchmarking, model-comparison]
triggers: [features-ready, algorithm-evaluation, model-selection]
```

## 1. Protocol Overview

**Purpose**: Systematically evaluate and select the most appropriate machine learning algorithms for the problem domain, establish baseline performance, and create a foundation for model optimization.

**Critical Success Factors**:
- Comprehensive algorithm evaluation
- Fair comparison methodology
- Reproducible baseline establishment
- Justified algorithm selection
- Performance benchmarking

## 2. Algorithm Selection Workflow

### Step 1: Problem Characterization
**Duration**: 2-3 hours

**Problem Analysis**:
```python
# algorithm_selection/problem_analyzer.py

class ProblemAnalyzer:
    
    def characterize_problem(self, data, target, config):
        """Analyze problem characteristics to guide algorithm selection."""
        
        problem_profile = {
            'task_type': None,
            'data_characteristics': {},
            'constraints': {},
            'recommendations': []
        }
        
        # Determine task type
        problem_profile['task_type'] = self.identify_task_type(target)
        
        # Analyze data characteristics
        problem_profile['data_characteristics'] = {
            'n_samples': len(data),
            'n_features': data.shape[1],
            'feature_types': self.analyze_feature_types(data),
            'class_balance': self.analyze_class_balance(target) if problem_profile['task_type'] == 'classification' else None,
            'data_sparsity': self.calculate_sparsity(data),
            'missing_values_pct': self.calculate_missing_pct(data),
            'outlier_pct': self.calculate_outlier_pct(data)
        }
        
        # Identify constraints
        problem_profile['constraints'] = {
            'interpretability_required': config.get('interpretability', False),
            'training_time_limit': config.get('max_training_time', None),
            'inference_time_limit': config.get('max_inference_time', None),
            'memory_limit_gb': config.get('memory_limit', None),
            'deployment_environment': config.get('deployment_env', 'cloud')
        }
        
        # Generate algorithm recommendations
        problem_profile['recommendations'] = self.recommend_algorithms(problem_profile)
        
        return problem_profile
    
    def identify_task_type(self, target):
        """Identify ML task type."""
        
        unique_values = len(np.unique(target))
        
        if unique_values == 2:
            return 'binary_classification'
        elif unique_values < 20 and target.dtype in ['object', 'category', 'int']:
            return 'multiclass_classification'
        elif target.dtype in ['float', 'int'] and unique_values > 20:
            return 'regression'
        else:
            return 'unknown'
    
    def recommend_algorithms(self, profile):
        """Recommend algorithms based on problem profile."""
        
        recommendations = []
        
        task = profile['task_type']
        n_samples = profile['data_characteristics']['n_samples']
        n_features = profile['data_characteristics']['n_features']
        interpretability = profile['constraints']['interpretability_required']
        
        # Small dataset recommendations
        if n_samples < 1000:
            recommendations.extend([
                {'algorithm': 'logistic_regression', 'priority': 'high', 'reason': 'Small dataset, linear model suitable'},
                {'algorithm': 'random_forest', 'priority': 'high', 'reason': 'Robust to small data'},
                {'algorithm': 'svm', 'priority': 'medium', 'reason': 'Effective in high-dimensional spaces'}
            ])
        
        # Medium dataset recommendations
        elif n_samples < 100000:
            recommendations.extend([
                {'algorithm': 'xgboost', 'priority': 'high', 'reason': 'Excellent performance on tabular data'},
                {'algorithm': 'lightgbm', 'priority': 'high', 'reason': 'Fast training, good accuracy'},
                {'algorithm': 'random_forest', 'priority': 'medium', 'reason': 'Robust baseline'},
                {'algorithm': 'neural_network', 'priority': 'medium', 'reason': 'Can capture complex patterns'}
            ])
        
        # Large dataset recommendations
        else:
            recommendations.extend([
                {'algorithm': 'lightgbm', 'priority': 'high', 'reason': 'Scalable to large datasets'},
                {'algorithm': 'neural_network', 'priority': 'high', 'reason': 'Can leverage large data'},
                {'algorithm': 'linear_model', 'priority': 'medium', 'reason': 'Fast baseline'}
            ])
        
        # Interpretability constraint
        if interpretability:
            recommendations = [r for r in recommendations if r['algorithm'] in [
                'logistic_regression', 'decision_tree', 'linear_regression', 'random_forest'
            ]]
            recommendations.append({
                'algorithm': 'decision_tree', 
                'priority': 'high', 
                'reason': 'Highly interpretable'
            })
        
        return recommendations
```

### Step 2: Algorithm Candidate Selection
**Duration**: 1-2 hours

**Candidate Pool Definition**:
```python
# algorithm_selection/algorithm_pool.py

class AlgorithmPool:
    
    def get_algorithm_candidates(self, task_type, problem_profile):
        """Define candidate algorithms for evaluation."""
        
        candidates = {}
        
        if task_type in ['binary_classification', 'multiclass_classification']:
            candidates = {
                'logistic_regression': {
                    'model_class': LogisticRegression,
                    'default_params': {'max_iter': 1000, 'random_state': 42},
                    'pros': ['Fast', 'Interpretable', 'Probabilistic'],
                    'cons': ['Linear only', 'May underfit complex data'],
                    'complexity': 'O(n*d)'
                },
                'random_forest': {
                    'model_class': RandomForestClassifier,
                    'default_params': {'n_estimators': 100, 'random_state': 42},
                    'pros': ['Robust', 'Handles non-linearity', 'Feature importance'],
                    'cons': ['Can overfit', 'Large model size'],
                    'complexity': 'O(n*log(n)*d*k)'
                },
                'xgboost': {
                    'model_class': xgb.XGBClassifier,
                    'default_params': {'n_estimators': 100, 'random_state': 42},
                    'pros': ['High accuracy', 'Regularization', 'Handles missing values'],
                    'cons': ['Hyperparameter sensitive', 'Can overfit'],
                    'complexity': 'O(n*log(n)*d*k)'
                },
                'lightgbm': {
                    'model_class': lgb.LGBMClassifier,
                    'default_params': {'n_estimators': 100, 'random_state': 42},
                    'pros': ['Very fast', 'Memory efficient', 'High accuracy'],
                    'cons': ['Sensitive to overfitting on small data'],
                    'complexity': 'O(n*d*k)'
                },
                'svm': {
                    'model_class': SVC,
                    'default_params': {'kernel': 'rbf', 'random_state': 42, 'probability': True},
                    'pros': ['Effective in high dimensions', 'Memory efficient'],
                    'cons': ['Slow on large datasets', 'Requires scaling'],
                    'complexity': 'O(n^2*d) to O(n^3*d)'
                },
                'neural_network': {
                    'model_class': MLPClassifier,
                    'default_params': {'hidden_layer_sizes': (100,), 'random_state': 42, 'max_iter': 500},
                    'pros': ['Captures complex patterns', 'Flexible architecture'],
                    'cons': ['Requires more data', 'Hyperparameter sensitive'],
                    'complexity': 'O(n*d*h*e)'
                }
            }
        
        elif task_type == 'regression':
            candidates = {
                'linear_regression': {
                    'model_class': LinearRegression,
                    'default_params': {},
                    'pros': ['Fast', 'Interpretable', 'Simple'],
                    'cons': ['Linear only', 'Sensitive to outliers'],
                    'complexity': 'O(n*d^2)'
                },
                'ridge_regression': {
                    'model_class': Ridge,
                    'default_params': {'alpha': 1.0, 'random_state': 42},
                    'pros': ['Regularized', 'Handles multicollinearity'],
                    'cons': ['Linear only'],
                    'complexity': 'O(n*d^2)'
                },
                'random_forest': {
                    'model_class': RandomForestRegressor,
                    'default_params': {'n_estimators': 100, 'random_state': 42},
                    'pros': ['Non-linear', 'Robust', 'Feature importance'],
                    'cons': ['Can overfit', 'Large model size'],
                    'complexity': 'O(n*log(n)*d*k)'
                },
                'xgboost': {
                    'model_class': xgb.XGBRegressor,
                    'default_params': {'n_estimators': 100, 'random_state': 42},
                    'pros': ['High accuracy', 'Regularization'],
                    'cons': ['Hyperparameter sensitive'],
                    'complexity': 'O(n*log(n)*d*k)'
                },
                'lightgbm': {
                    'model_class': lgb.LGBMRegressor,
                    'default_params': {'n_estimators': 100, 'random_state': 42},
                    'pros': ['Very fast', 'Memory efficient'],
                    'cons': ['Can overfit on small data'],
                    'complexity': 'O(n*d*k)'
                }
            }
        
        # Filter based on constraints
        filtered_candidates = self.filter_by_constraints(candidates, problem_profile)
        
        return filtered_candidates
```

### Step 3: Baseline Model Training
**Duration**: 4-6 hours

**Baseline Training Framework**:
```python
# algorithm_selection/baseline_trainer.py

class BaselineTrainer:
    
    def train_all_baselines(self, X_train, y_train, X_val, y_val, candidates, config):
        """Train baseline models for all candidate algorithms."""
        
        baseline_results = {
            'models': {},
            'metrics': {},
            'training_times': {},
            'inference_times': {},
            'model_sizes': {}
        }
        
        for algo_name, algo_config in candidates.items():
            print(f"Training baseline: {algo_name}")
            
            # Initialize model
            model = algo_config['model_class'](**algo_config['default_params'])
            
            # Train and time
            start_time = time.time()
            model.fit(X_train, y_train)
            training_time = time.time() - start_time
            
            # Predict and time
            start_time = time.time()
            y_pred_val = model.predict(X_val)
            inference_time = time.time() - start_time
            
            # Calculate metrics
            metrics = self.calculate_metrics(y_val, y_pred_val, model, X_val, config)
            
            # Store results
            baseline_results['models'][algo_name] = model
            baseline_results['metrics'][algo_name] = metrics
            baseline_results['training_times'][algo_name] = training_time
            baseline_results['inference_times'][algo_name] = inference_time
            baseline_results['model_sizes'][algo_name] = self.get_model_size(model)
            
            # Log to MLflow
            self.log_baseline_to_mlflow(algo_name, model, metrics, training_time, config)
        
        return baseline_results
    
    def calculate_metrics(self, y_true, y_pred, model, X_val, config):
        """Calculate comprehensive metrics."""
        
        metrics = {}
        
        if config['task_type'] in ['binary_classification', 'multiclass_classification']:
            y_pred_proba = model.predict_proba(X_val)[:, 1] if hasattr(model, 'predict_proba') else y_pred
            
            metrics = {
                'accuracy': accuracy_score(y_true, y_pred),
                'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
                'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
                'f1_score': f1_score(y_true, y_pred, average='weighted', zero_division=0),
                'auc_roc': roc_auc_score(y_true, y_pred_proba) if hasattr(model, 'predict_proba') else None
            }
        else:
            metrics = {
                'mse': mean_squared_error(y_true, y_pred),
                'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
                'mae': mean_absolute_error(y_true, y_pred),
                'r2': r2_score(y_true, y_pred),
                'mape': mean_absolute_percentage_error(y_true, y_pred)
            }
        
        return metrics
    
    def get_model_size(self, model):
        """Calculate model size in MB."""
        
        import pickle
        model_bytes = pickle.dumps(model)
        size_mb = len(model_bytes) / (1024 * 1024)
        return size_mb
```

### Step 4: Algorithm Comparison & Analysis
**Duration**: 3-4 hours

**Comparison Framework**:
```python
# algorithm_selection/algorithm_comparator.py

class AlgorithmComparator:
    
    def compare_algorithms(self, baseline_results, config):
        """Comprehensive algorithm comparison."""
        
        comparison_report = {
            'summary_table': self.create_summary_table(baseline_results),
            'statistical_tests': self.perform_statistical_tests(baseline_results),
            'radar_chart_data': self.prepare_radar_chart(baseline_results),
            'rankings': self.rank_algorithms(baseline_results, config),
            'recommendations': []
        }
        
        # Generate recommendations
        comparison_report['recommendations'] = self.generate_recommendations(
            comparison_report, config
        )
        
        return comparison_report
    
    def create_summary_table(self, results):
        """Create algorithm comparison summary table."""
        
        summary = []
        
        for algo_name in results['models'].keys():
            row = {
                'algorithm': algo_name,
                'training_time_s': results['training_times'][algo_name],
                'inference_time_s': results['inference_times'][algo_name],
                'model_size_mb': results['model_sizes'][algo_name]
            }
            
            # Add metrics
            row.update(results['metrics'][algo_name])
            
            summary.append(row)
        
        # Convert to DataFrame
        df = pd.DataFrame(summary)
        
        return df
    
    def rank_algorithms(self, results, config):
        """Rank algorithms based on multiple criteria."""
        
        rankings = {
            'by_performance': {},
            'by_speed': {},
            'by_size': {},
            'overall': {}
        }
        
        primary_metric = config.get('primary_metric', 'accuracy')
        
        # Rank by performance
        perf_scores = {algo: metrics.get(primary_metric, 0) 
                      for algo, metrics in results['metrics'].items()}
        rankings['by_performance'] = dict(sorted(perf_scores.items(), 
                                                 key=lambda x: x[1], reverse=True))
        
        # Rank by training speed
        speed_scores = {algo: 1/time for algo, time in results['training_times'].items()}
        rankings['by_speed'] = dict(sorted(speed_scores.items(), 
                                          key=lambda x: x[1], reverse=True))
        
        # Rank by model size
        size_scores = {algo: 1/size for algo, size in results['model_sizes'].items()}
        rankings['by_size'] = dict(sorted(size_scores.items(), 
                                         key=lambda x: x[1], reverse=True))
        
        # Overall ranking (weighted combination)
        weights = config.get('ranking_weights', {
            'performance': 0.6,
            'speed': 0.2,
            'size': 0.2
        })
        
        overall_scores = {}
        for algo in results['models'].keys():
            score = (
                weights['performance'] * self.normalize_score(perf_scores[algo], perf_scores) +
                weights['speed'] * self.normalize_score(speed_scores[algo], speed_scores) +
                weights['size'] * self.normalize_score(size_scores[algo], size_scores)
            )
            overall_scores[algo] = score
        
        rankings['overall'] = dict(sorted(overall_scores.items(), 
                                         key=lambda x: x[1], reverse=True))
        
        return rankings
    
    def normalize_score(self, score, all_scores):
        """Normalize score to 0-1 range."""
        min_score = min(all_scores.values())
        max_score = max(all_scores.values())
        
        if max_score == min_score:
            return 1.0
        
        return (score - min_score) / (max_score - min_score)
    
    def perform_statistical_tests(self, results):
        """Perform statistical significance tests."""
        
        from scipy import stats
        
        tests = {}
        
        # Perform cross-validation for each algorithm
        cv_scores = {}
        for algo_name, model in results['models'].items():
            # Assuming we have access to full training data
            scores = cross_val_score(model, X_train, y_train, cv=5)
            cv_scores[algo_name] = scores
        
        # Pairwise t-tests
        algorithms = list(results['models'].keys())
        pairwise_tests = {}
        
        for i, algo1 in enumerate(algorithms):
            for algo2 in algorithms[i+1:]:
                t_stat, p_value = stats.ttest_rel(
                    cv_scores[algo1], 
                    cv_scores[algo2]
                )
                pairwise_tests[f'{algo1}_vs_{algo2}'] = {
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'significant': p_value < 0.05
                }
        
        tests['pairwise_comparisons'] = pairwise_tests
        
        return tests
```

### Step 5: Final Algorithm Selection
**Duration**: 2-3 hours

**Selection Decision Framework**:
```python
# algorithm_selection/algorithm_selector.py

class AlgorithmSelector:
    
    def select_final_algorithm(self, comparison_report, config):
        """Make final algorithm selection with justification."""
        
        selection_decision = {
            'selected_algorithm': None,
            'selection_criteria': {},
            'justification': '',
            'runner_ups': [],
            'trade_offs': {}
        }
        
        # Get top 3 algorithms
        top_algorithms = list(comparison_report['rankings']['overall'].keys())[:3]
        
        # Evaluate against business constraints
        for algo in top_algorithms:
            meets_constraints = self.check_constraints(algo, comparison_report, config)
            
            if meets_constraints:
                selection_decision['selected_algorithm'] = algo
                break
        
        # If no algorithm meets all constraints, select best performer
        if not selection_decision['selected_algorithm']:
            selection_decision['selected_algorithm'] = top_algorithms[0]
        
        # Document selection criteria
        selection_decision['selection_criteria'] = self.document_criteria(
            selection_decision['selected_algorithm'], 
            comparison_report, 
            config
        )
        
        # Generate justification
        selection_decision['justification'] = self.generate_justification(
            selection_decision['selected_algorithm'],
            comparison_report,
            config
        )
        
        # Identify runner-ups
        selection_decision['runner_ups'] = top_algorithms[1:3]
        
        # Document trade-offs
        selection_decision['trade_offs'] = self.document_tradeoffs(
            selection_decision['selected_algorithm'],
            selection_decision['runner_ups'],
            comparison_report
        )
        
        return selection_decision
    
    def check_constraints(self, algorithm, comparison_report, config):
        """Check if algorithm meets all constraints."""
        
        summary_df = comparison_report['summary_table']
        algo_row = summary_df[summary_df['algorithm'] == algorithm].iloc[0]
        
        constraints = config.get('constraints', {})
        
        # Check training time constraint
        if 'max_training_time' in constraints:
            if algo_row['training_time_s'] > constraints['max_training_time']:
                return False
        
        # Check inference time constraint
        if 'max_inference_time' in constraints:
            if algo_row['inference_time_s'] > constraints['max_inference_time']:
                return False
        
        # Check model size constraint
        if 'max_model_size_mb' in constraints:
            if algo_row['model_size_mb'] > constraints['max_model_size_mb']:
                return False
        
        # Check minimum performance
        primary_metric = config.get('primary_metric', 'accuracy')
        if 'min_performance' in constraints:
            if algo_row[primary_metric] < constraints['min_performance']:
                return False
        
        return True
    
    def generate_justification(self, algorithm, comparison_report, config):
        """Generate detailed justification for selection."""
        
        summary_df = comparison_report['summary_table']
        algo_row = summary_df[summary_df['algorithm'] == algorithm].iloc[0]
        
        primary_metric = config.get('primary_metric', 'accuracy')
        
        justification = f"""
## Algorithm Selection Justification

### Selected Algorithm: {algorithm}

### Performance Metrics
- Primary Metric ({primary_metric}): {algo_row[primary_metric]:.4f}
- Training Time: {algo_row['training_time_s']:.2f} seconds
- Inference Time: {algo_row['inference_time_s']:.4f} seconds
- Model Size: {algo_row['model_size_mb']:.2f} MB

### Selection Rationale
1. **Performance**: Ranks #{list(comparison_report['rankings']['by_performance'].keys()).index(algorithm) + 1} in performance
2. **Efficiency**: Ranks #{list(comparison_report['rankings']['by_speed'].keys()).index(algorithm) + 1} in training speed
3. **Deployability**: Ranks #{list(comparison_report['rankings']['by_size'].keys()).index(algorithm) + 1} in model size

### Key Advantages
- Meets all business constraints
- Optimal balance of accuracy and efficiency
- Suitable for production deployment

### Considerations
- May require hyperparameter tuning for optimal performance
- Should monitor for overfitting during optimization
"""
        
        return justification
```

## 3. Baseline Model Documentation

### Baseline Model Card Template
```markdown
# Baseline Model Card: {algorithm_name}

## Model Details
- **Algorithm**: {algorithm_name}
- **Version**: 1.0.0 (baseline)
- **Date**: {date}
- **Task**: {classification/regression}
- **Framework**: {sklearn/xgboost/etc}

## Performance Metrics
| Metric | Value |
|--------|-------|
| Accuracy | {value} |
| Precision | {value} |
| Recall | {value} |
| F1 Score | {value} |
| AUC-ROC | {value} |

## Training Details
- **Training Data Size**: {n_samples} samples
- **Features**: {n_features} features
- **Training Time**: {time} seconds
- **Hyperparameters**: {default_params}

## Limitations
- Baseline model with default hyperparameters
- Not optimized for production
- Requires hyperparameter tuning

## Next Steps
- Hyperparameter optimization
- Feature engineering refinement
- Ensemble methods evaluation
```

## 4. Quality Gates

### Gate 1: Problem Analysis Complete
- [ ] Task type identified correctly
- [ ] Data characteristics documented
- [ ] Constraints identified and validated
- [ ] Algorithm recommendations generated

### Gate 2: Baseline Training Complete
- [ ] All candidate algorithms trained
- [ ] Metrics calculated for all models
- [ ] Training times recorded
- [ ] Model artifacts saved

### Gate 3: Selection Justified
- [ ] Comparison analysis completed
- [ ] Statistical tests performed
- [ ] Final algorithm selected with justification
- [ ] Trade-offs documented
- [ ] Stakeholder approval obtained

## 5. Deliverables

### Required Outputs
1. **Algorithm Selection Report** (`algorithm-selection-report.md`)
2. **Baseline Model Artifacts** (`baseline-model.pkl`)
3. **Comparison Matrix** (`comparison-matrix.xlsx`)
4. **Performance Benchmarks** (`benchmark-results.json`)
5. **Selection Justification** (`selection-justification.md`)

### Evidence Package Structure
```
evidence/protocol-13-algorithm-selection/
├── reports/
│   ├── algorithm-selection-report.md
│   ├── problem-analysis.md
│   └── selection-justification.md
├── models/
│   ├── baseline_logistic_regression.pkl
│   ├── baseline_random_forest.pkl
│   ├── baseline_xgboost.pkl
│   └── baseline_lightgbm.pkl
├── metrics/
│   ├── comparison-matrix.xlsx
│   ├── benchmark-results.json
│   └── statistical-tests.json
└── visualizations/
    ├── algorithm-comparison-chart.png
    ├── performance-radar-chart.png
    └── training-time-comparison.png
```

## 6. Common Pitfalls & Solutions

### Pitfall 1: Biased Algorithm Comparison
**Solution**: Use cross-validation and statistical tests for fair comparison

### Pitfall 2: Ignoring Business Constraints
**Solution**: Document and validate constraints before selection

### Pitfall 3: Premature Optimization
**Solution**: Establish solid baseline before hyperparameter tuning

### Pitfall 4: Insufficient Documentation
**Solution**: Use model cards and detailed justification reports

## 7. Success Criteria

- **Comprehensive Evaluation**: All candidate algorithms evaluated
- **Fair Comparison**: Statistical significance established
- **Justified Selection**: Clear rationale documented
- **Reproducible Results**: All experiments tracked and reproducible
- **Stakeholder Alignment**: Selection approved by stakeholders

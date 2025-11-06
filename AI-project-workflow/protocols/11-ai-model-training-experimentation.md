# Protocol 11: AI Model Training & Experimentation

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: ml_development
phase: "Phase 3: AI Model Development"
priority: critical
tags: [model-training, hyperparameter-tuning, experiment-tracking, mlflow]
triggers: [features-ready, training-phase, model-development]
```

## 1. Protocol Overview

**Purpose**: Establish systematic model training and experimentation processes with comprehensive tracking, hyperparameter optimization, and reproducibility guarantees.

**Critical Success Factors**:
- Experiment reproducibility
- Performance optimization
- Resource efficiency
- Comprehensive tracking
- Fair model comparison

## 2. Training Workflow

### Step 1: Experiment Setup
**Duration**: 2-3 hours

**Configuration Template**:
```yaml
# experiments/config/experiment_001.yaml
experiment:
  name: "baseline_model_v1"
  description: "Initial baseline with default hyperparameters"
  tags: ["baseline", "classification", "v1.0"]
  
environment:
  python_version: "3.9"
  cuda_version: "11.8"
  random_seed: 42
  deterministic: true
  
data:
  train_path: "data/processed/train.parquet"
  val_path: "data/processed/val.parquet"
  test_path: "data/processed/test.parquet"
  features: "feature_store/v1.0/features.json"
  
model:
  algorithm: "xgboost"
  task_type: "classification"
  objective: "binary:logistic"
  
hyperparameters:
  n_estimators: 100
  max_depth: 6
  learning_rate: 0.1
  subsample: 0.8
  colsample_bytree: 0.8
  
metrics:
  primary: "auc_roc"
  secondary: ["accuracy", "precision", "recall", "f1"]
  
resources:
  max_memory_gb: 16
  max_time_hours: 4
  n_jobs: -1
```

**Experiment Tracking Setup**:
```python
# training/experiment_tracker.py
import mlflow
import wandb
from datetime import datetime

class ExperimentTracker:
    
    def __init__(self, config):
        self.config = config
        self.experiment_name = config['experiment']['name']
        self.run_id = None
        
    def start_run(self):
        """Initialize experiment tracking."""
        
        # MLflow setup
        mlflow.set_experiment(self.experiment_name)
        mlflow.start_run()
        self.run_id = mlflow.active_run().info.run_id
        
        # Log configuration
        mlflow.log_params(self.flatten_dict(self.config))
        mlflow.set_tags(self.config['experiment']['tags'])
        
        # WandB setup (optional)
        if self.config.get('use_wandb', False):
            wandb.init(
                project=self.experiment_name,
                config=self.config,
                tags=self.config['experiment']['tags']
            )
        
        return self.run_id
    
    def log_metrics(self, metrics, step=None):
        """Log training metrics."""
        mlflow.log_metrics(metrics, step=step)
        
    def log_artifacts(self, artifacts):
        """Log model artifacts."""
        for artifact_path in artifacts:
            mlflow.log_artifact(artifact_path)
```

### Step 2: Baseline Model Training
**Duration**: 3-4 hours

**Training Implementation**:
```python
# training/train_model.py

class ModelTrainer:
    
    def train_baseline(self, X_train, y_train, X_val, y_val, config):
        """Train baseline model with default parameters."""
        
        # Initialize model based on config
        model = self.initialize_model(config)
        
        # Setup callbacks
        callbacks = self.setup_callbacks(config)
        
        # Training loop with validation
        history = {
            'train_loss': [],
            'val_loss': [],
            'train_metrics': [],
            'val_metrics': []
        }
        
        # For traditional ML
        if config['model']['algorithm'] in ['xgboost', 'lightgbm', 'catboost']:
            eval_set = [(X_train, y_train), (X_val, y_val)]
            
            model.fit(
                X_train, y_train,
                eval_set=eval_set,
                eval_metric=config['metrics']['primary'],
                early_stopping_rounds=50,
                verbose=100
            )
            
            # Get training history
            if hasattr(model, 'evals_result'):
                history = model.evals_result()
        
        # For deep learning
        elif config['model']['algorithm'] in ['tensorflow', 'pytorch']:
            history = model.fit(
                X_train, y_train,
                validation_data=(X_val, y_val),
                epochs=config['training']['epochs'],
                batch_size=config['training']['batch_size'],
                callbacks=callbacks,
                verbose=1
            )
        
        # Evaluate on validation set
        val_predictions = model.predict(X_val)
        val_metrics = self.calculate_metrics(y_val, val_predictions, config)
        
        return model, history, val_metrics
    
    def calculate_metrics(self, y_true, y_pred, config):
        """Calculate comprehensive metrics."""
        
        metrics = {}
        
        # Classification metrics
        if config['model']['task_type'] == 'classification':
            metrics['accuracy'] = accuracy_score(y_true, y_pred > 0.5)
            metrics['precision'] = precision_score(y_true, y_pred > 0.5)
            metrics['recall'] = recall_score(y_true, y_pred > 0.5)
            metrics['f1'] = f1_score(y_true, y_pred > 0.5)
            metrics['auc_roc'] = roc_auc_score(y_true, y_pred)
            metrics['auc_pr'] = average_precision_score(y_true, y_pred)
            
        # Regression metrics
        elif config['model']['task_type'] == 'regression':
            metrics['mse'] = mean_squared_error(y_true, y_pred)
            metrics['rmse'] = np.sqrt(metrics['mse'])
            metrics['mae'] = mean_absolute_error(y_true, y_pred)
            metrics['r2'] = r2_score(y_true, y_pred)
            metrics['mape'] = mean_absolute_percentage_error(y_true, y_pred)
        
        return metrics
```

### Step 3: Hyperparameter Optimization
**Duration**: 8-12 hours

**Optimization Strategies**:
```python
# training/hyperparameter_optimization.py
import optuna
from sklearn.model_selection import cross_val_score

class HyperparameterOptimizer:
    
    def optimize(self, X_train, y_train, config, n_trials=100):
        """Optimize hyperparameters using Bayesian optimization."""
        
        def objective(trial):
            # Define hyperparameter search space
            params = self.get_search_space(trial, config)
            
            # Train model with suggested parameters
            model = self.initialize_model(config, params)
            
            # Cross-validation
            scores = cross_val_score(
                model, X_train, y_train,
                cv=5,
                scoring=config['metrics']['primary'],
                n_jobs=-1
            )
            
            # Log trial
            self.log_trial(trial, params, scores.mean())
            
            return scores.mean()
        
        # Create study
        study = optuna.create_study(
            study_name=f"{config['experiment']['name']}_optimization",
            direction='maximize',
            pruner=optuna.pruners.MedianPruner(),
            sampler=optuna.samplers.TPESampler(seed=42)
        )
        
        # Optimize
        study.optimize(
            objective,
            n_trials=n_trials,
            timeout=config['resources']['max_time_hours'] * 3600,
            n_jobs=1  # Parallel trials if resources allow
        )
        
        # Get best parameters
        best_params = study.best_params
        best_score = study.best_value
        
        # Train final model with best parameters
        final_model = self.train_with_best_params(
            X_train, y_train, config, best_params
        )
        
        return final_model, best_params, best_score
    
    def get_search_space(self, trial, config):
        """Define hyperparameter search space."""
        
        if config['model']['algorithm'] == 'xgboost':
            return {
                'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
                'max_depth': trial.suggest_int('max_depth', 3, 10),
                'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
                'subsample': trial.suggest_float('subsample', 0.6, 1.0),
                'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
                'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
                'gamma': trial.suggest_float('gamma', 0, 0.5),
                'reg_alpha': trial.suggest_float('reg_alpha', 0, 1),
                'reg_lambda': trial.suggest_float('reg_lambda', 0, 1)
            }
        
        elif config['model']['algorithm'] == 'neural_network':
            return {
                'hidden_layers': trial.suggest_int('hidden_layers', 1, 5),
                'hidden_units': trial.suggest_int('hidden_units', 32, 512),
                'dropout_rate': trial.suggest_float('dropout_rate', 0.1, 0.5),
                'learning_rate': trial.suggest_float('learning_rate', 1e-5, 1e-2, log=True),
                'batch_size': trial.suggest_categorical('batch_size', [32, 64, 128, 256]),
                'activation': trial.suggest_categorical('activation', ['relu', 'tanh', 'elu'])
            }
```

### Step 4: Model Ensemble Creation
**Duration**: 3-4 hours

**Ensemble Strategies**:
```python
# training/ensemble.py

class ModelEnsemble:
    
    def create_ensemble(self, models, X_val, y_val, method='voting'):
        """Create model ensemble."""
        
        if method == 'voting':
            # Simple voting
            ensemble = VotingClassifier(
                estimators=[(f'model_{i}', m) for i, m in enumerate(models)],
                voting='soft'
            )
            
        elif method == 'stacking':
            # Stacking with meta-learner
            ensemble = StackingClassifier(
                estimators=[(f'model_{i}', m) for i, m in enumerate(models)],
                final_estimator=LogisticRegression(),
                cv=5
            )
            
        elif method == 'blending':
            # Custom blending
            ensemble = self.create_blended_ensemble(models, X_val, y_val)
        
        elif method == 'weighted':
            # Weighted average based on validation performance
            weights = self.calculate_optimal_weights(models, X_val, y_val)
            ensemble = self.WeightedEnsemble(models, weights)
        
        return ensemble
    
    def calculate_optimal_weights(self, models, X_val, y_val):
        """Calculate optimal ensemble weights."""
        
        from scipy.optimize import minimize
        
        def objective(weights):
            # Normalize weights
            weights = weights / weights.sum()
            
            # Get predictions
            predictions = np.zeros_like(y_val, dtype=float)
            for model, weight in zip(models, weights):
                predictions += weight * model.predict_proba(X_val)[:, 1]
            
            # Calculate loss
            loss = -roc_auc_score(y_val, predictions)
            return loss
        
        # Initial weights
        init_weights = np.ones(len(models)) / len(models)
        
        # Constraints: weights sum to 1, all positive
        constraints = {'type': 'eq', 'fun': lambda w: w.sum() - 1}
        bounds = [(0, 1) for _ in range(len(models))]
        
        # Optimize
        result = minimize(
            objective, init_weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        return result.x
```

### Step 5: Experiment Comparison
**Duration**: 2-3 hours

**Comparison Analysis**:
```python
# training/experiment_comparison.py

class ExperimentComparator:
    
    def compare_experiments(self, experiment_ids):
        """Compare multiple experiments."""
        
        comparison_report = {
            'experiments': [],
            'best_model': None,
            'statistical_tests': {}
        }
        
        # Load experiment results
        for exp_id in experiment_ids:
            exp_data = self.load_experiment(exp_id)
            comparison_report['experiments'].append(exp_data)
        
        # Statistical comparison
        if len(experiment_ids) > 1:
            # Perform statistical tests
            comparison_report['statistical_tests'] = self.statistical_tests(
                comparison_report['experiments']
            )
        
        # Identify best model
        comparison_report['best_model'] = self.identify_best_model(
            comparison_report['experiments']
        )
        
        # Generate comparison visualizations
        self.create_comparison_plots(comparison_report)
        
        return comparison_report
    
    def statistical_tests(self, experiments):
        """Perform statistical significance tests."""
        
        from scipy import stats
        
        tests = {}
        
        # Paired t-test for cross-validation scores
        if len(experiments) == 2:
            scores_1 = experiments[0]['cv_scores']
            scores_2 = experiments[1]['cv_scores']
            
            t_stat, p_value = stats.ttest_rel(scores_1, scores_2)
            tests['paired_ttest'] = {
                't_statistic': t_stat,
                'p_value': p_value,
                'significant': p_value < 0.05
            }
        
        # Friedman test for multiple models
        elif len(experiments) > 2:
            scores = [exp['cv_scores'] for exp in experiments]
            f_stat, p_value = stats.friedmanchisquare(*scores)
            tests['friedman_test'] = {
                'statistic': f_stat,
                'p_value': p_value,
                'significant': p_value < 0.05
            }
        
        return tests
```

## 3. Reproducibility Management

### Reproducibility Checklist
```python
# training/reproducibility.py

class ReproducibilityManager:
    
    def ensure_reproducibility(self, config):
        """Ensure training reproducibility."""
        
        # Set random seeds
        np.random.seed(config['environment']['random_seed'])
        random.seed(config['environment']['random_seed'])
        torch.manual_seed(config['environment']['random_seed'])
        tf.random.set_seed(config['environment']['random_seed'])
        
        # Set deterministic mode
        if config['environment']['deterministic']:
            torch.use_deterministic_algorithms(True)
            os.environ['PYTHONHASHSEED'] = str(config['environment']['random_seed'])
            os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':4096:8'
        
        # Log environment
        self.log_environment_info()
        
        # Create requirements file
        self.create_requirements_file()
        
        # Create Docker image
        if config.get('create_docker', False):
            self.create_docker_image(config)
    
    def log_environment_info(self):
        """Log detailed environment information."""
        
        env_info = {
            'python_version': sys.version,
            'packages': {
                pkg.key: pkg.version 
                for pkg in pkg_resources.working_set
            },
            'cuda_available': torch.cuda.is_available(),
            'cuda_version': torch.version.cuda if torch.cuda.is_available() else None,
            'gpu_count': torch.cuda.device_count(),
            'cpu_count': os.cpu_count(),
            'memory_gb': psutil.virtual_memory().total / (1024**3)
        }
        
        with open('environment_info.json', 'w') as f:
            json.dump(env_info, f, indent=2)
        
        mlflow.log_artifact('environment_info.json')
```

## 4. Quality Gates

### Gate 1: Training Setup
- [ ] Configuration validated
- [ ] Data loaded successfully
- [ ] Seeds set for reproducibility
- [ ] Tracking initialized

### Gate 2: Model Performance
- [ ] Baseline performance established
- [ ] Improvement over baseline demonstrated
- [ ] Cross-validation completed
- [ ] No overfitting detected (val_score / train_score > 0.9)

### Gate 3: Experiment Tracking
- [ ] All metrics logged
- [ ] Model artifacts saved
- [ ] Hyperparameters recorded
- [ ] Reproducibility guaranteed

## 5. Deliverables

### Required Outputs
1. **Trained Models** (`models/`)
2. **Training Reports** (`reports/training_report.md`)
3. **Hyperparameter Results** (`optimization_results.json`)
4. **Comparison Analysis** (`experiment_comparison.md`)
5. **Training Curves** (`visualizations/`)
6. **MLflow Tracking** (MLflow UI accessible)

### Evidence Package
```
evidence/protocol-11-training/
├── models/
│   ├── baseline_model.pkl
│   ├── optimized_model.pkl
│   └── ensemble_model.pkl
├── reports/
│   ├── training_report.md
│   ├── optimization_report.md
│   └── comparison_analysis.md
├── metrics/
│   ├── training_metrics.json
│   ├── validation_metrics.json
│   └── cv_scores.json
├── configs/
│   ├── baseline_config.yaml
│   └── best_config.yaml
└── mlruns/
    └── {experiment_id}/
```

## 6. Success Criteria

- **Model Performance**: Meets or exceeds target metrics
- **Training Efficiency**: Completes within resource budget
- **Reproducibility**: 100% consistent results with same seed
- **Documentation**: All experiments tracked and documented
- **Statistical Significance**: p-value < 0.05 for improvements

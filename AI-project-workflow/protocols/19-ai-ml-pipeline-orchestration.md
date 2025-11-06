# Protocol 19: AI ML Pipeline Orchestration

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: mlops_deployment
phase: "Phase 5: MLOps & Deployment"
priority: critical
tags: [pipeline-orchestration, airflow, kubeflow, workflow, automation, dag]
triggers: [pipeline-setup, orchestration, workflow-automation, ml-pipeline]
```

## 1. Protocol Overview

**Purpose**: Design, implement, and orchestrate end-to-end ML pipelines with automated task scheduling, dependency management, error handling, and monitoring for reproducible ML workflows.

**Critical Success Factors**:
- Pipeline reproducibility
- Task dependency management
- Error recovery mechanisms
- Scalability and parallelization
- Monitoring and observability
- Version control integration

## 2. Pipeline Orchestration Workflow

### Step 1: Pipeline Design & Architecture
**Duration**: 4-6 hours

**Activities**:
1. Define pipeline stages
2. Map task dependencies
3. Identify parallelization opportunities
4. Design error handling strategy
5. Plan resource allocation

**Pipeline Architecture**:
```python
# orchestration/pipeline_design.py

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum

class TaskType(Enum):
    DATA_INGESTION = "data_ingestion"
    DATA_VALIDATION = "data_validation"
    FEATURE_ENGINEERING = "feature_engineering"
    MODEL_TRAINING = "model_training"
    MODEL_EVALUATION = "model_evaluation"
    MODEL_REGISTRATION = "model_registration"
    DEPLOYMENT = "deployment"

@dataclass
class PipelineTask:
    task_id: str
    task_type: TaskType
    dependencies: List[str]
    resources: Dict[str, any]
    retry_policy: Dict[str, any]
    timeout: int
    
@dataclass
class PipelineDefinition:
    pipeline_id: str
    name: str
    description: str
    tasks: List[PipelineTask]
    schedule: str
    default_args: Dict[str, any]
    
    def validate(self):
        """Validate pipeline definition."""
        # Check for circular dependencies
        if self._has_circular_dependencies():
            raise ValueError("Circular dependencies detected")
        
        # Check all dependencies exist
        task_ids = {task.task_id for task in self.tasks}
        for task in self.tasks:
            for dep in task.dependencies:
                if dep not in task_ids:
                    raise ValueError(f"Unknown dependency: {dep}")
        
        return True
    
    def _has_circular_dependencies(self):
        """Check for circular dependencies using DFS."""
        visited = set()
        rec_stack = set()
        
        def has_cycle(task_id):
            visited.add(task_id)
            rec_stack.add(task_id)
            
            task = next(t for t in self.tasks if t.task_id == task_id)
            for dep in task.dependencies:
                if dep not in visited:
                    if has_cycle(dep):
                        return True
                elif dep in rec_stack:
                    return True
            
            rec_stack.remove(task_id)
            return False
        
        for task in self.tasks:
            if task.task_id not in visited:
                if has_cycle(task.task_id):
                    return True
        
        return False
```

### Step 2: Airflow DAG Implementation
**Duration**: 6-8 hours

**Airflow DAG Definition**:
```python
# orchestration/airflow/ml_pipeline_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import os

# Default arguments
default_args = {
    'owner': 'ml_team',
    'depends_on_past': False,
    'email': ['ml-alerts@company.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=2),
}

# Create DAG
dag = DAG(
    'ml_training_pipeline',
    default_args=default_args,
    description='End-to-end ML training pipeline',
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    start_date=days_ago(1),
    catchup=False,
    tags=['ml', 'training', 'production'],
)

# Task 1: Data Ingestion
def ingest_data(**context):
    """Ingest data from source."""
    from src.data_ingestion import DataIngestion
    
    ingestion = DataIngestion()
    data_path = ingestion.fetch_data(
        source=os.getenv('DATA_SOURCE'),
        date=context['ds']
    )
    
    # Push to XCom for downstream tasks
    context['ti'].xcom_push(key='data_path', value=data_path)
    
    return data_path

ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    dag=dag,
)

# Task 2: Data Validation
def validate_data(**context):
    """Validate ingested data."""
    from src.data_validation import DataValidator
    
    # Pull from XCom
    data_path = context['ti'].xcom_pull(key='data_path', task_ids='ingest_data')
    
    validator = DataValidator()
    validation_report = validator.validate(data_path)
    
    if not validation_report['passed']:
        raise ValueError(f"Data validation failed: {validation_report['errors']}")
    
    context['ti'].xcom_push(key='validation_report', value=validation_report)
    
    return validation_report

validate_task = PythonOperator(
    task_id='validate_data',
    python_callable=validate_data,
    dag=dag,
)

# Task 3: Feature Engineering
def engineer_features(**context):
    """Create features from validated data."""
    from src.feature_engineering import FeatureEngineering
    
    data_path = context['ti'].xcom_pull(key='data_path', task_ids='ingest_data')
    
    fe = FeatureEngineering()
    features_path = fe.create_features(data_path)
    
    context['ti'].xcom_push(key='features_path', value=features_path)
    
    return features_path

feature_task = PythonOperator(
    task_id='engineer_features',
    python_callable=engineer_features,
    dag=dag,
)

# Task 4: Model Training (using Docker)
train_task = DockerOperator(
    task_id='train_model',
    image='ml-training:latest',
    api_version='auto',
    auto_remove=True,
    command='python train.py --features {{ ti.xcom_pull(key="features_path", task_ids="engineer_features") }}',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    environment={
        'MLFLOW_TRACKING_URI': os.getenv('MLFLOW_TRACKING_URI'),
        'AWS_ACCESS_KEY_ID': os.getenv('AWS_ACCESS_KEY_ID'),
        'AWS_SECRET_ACCESS_KEY': os.getenv('AWS_SECRET_ACCESS_KEY'),
    },
    dag=dag,
)

# Task 5: Model Evaluation
def evaluate_model(**context):
    """Evaluate trained model."""
    from src.model_evaluation import ModelEvaluator
    import mlflow
    
    # Get latest model from MLflow
    mlflow.set_tracking_uri(os.getenv('MLFLOW_TRACKING_URI'))
    
    evaluator = ModelEvaluator()
    metrics = evaluator.evaluate_latest_model()
    
    # Check if model meets threshold
    if metrics['accuracy'] < 0.85:
        raise ValueError(f"Model accuracy {metrics['accuracy']} below threshold 0.85")
    
    context['ti'].xcom_push(key='metrics', value=metrics)
    
    return metrics

evaluate_task = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    dag=dag,
)

# Task 6: Model Registration
def register_model(**context):
    """Register model in MLflow registry."""
    import mlflow
    from mlflow.tracking import MlflowClient
    
    mlflow.set_tracking_uri(os.getenv('MLFLOW_TRACKING_URI'))
    client = MlflowClient()
    
    # Get latest run
    experiment = client.get_experiment_by_name('ml_training')
    runs = client.search_runs(experiment.experiment_id, order_by=["start_time DESC"], max_results=1)
    
    if runs:
        run_id = runs[0].info.run_id
        model_uri = f"runs:/{run_id}/model"
        
        # Register model
        model_version = mlflow.register_model(model_uri, "fraud_detection_model")
        
        # Transition to staging
        client.transition_model_version_stage(
            name="fraud_detection_model",
            version=model_version.version,
            stage="Staging"
        )
        
        context['ti'].xcom_push(key='model_version', value=model_version.version)
        
        return model_version.version

register_task = PythonOperator(
    task_id='register_model',
    python_callable=register_model,
    dag=dag,
)

# Task 7: Send Notification
def send_notification(**context):
    """Send pipeline completion notification."""
    import requests
    
    metrics = context['ti'].xcom_pull(key='metrics', task_ids='evaluate_model')
    model_version = context['ti'].xcom_pull(key='model_version', task_ids='register_model')
    
    message = f"""
    ML Pipeline Completed Successfully
    
    Date: {context['ds']}
    Model Version: {model_version}
    Accuracy: {metrics['accuracy']:.4f}
    Precision: {metrics['precision']:.4f}
    Recall: {metrics['recall']:.4f}
    """
    
    # Send to Slack
    webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    requests.post(webhook_url, json={'text': message})
    
    return "Notification sent"

notify_task = PythonOperator(
    task_id='send_notification',
    python_callable=send_notification,
    dag=dag,
)

# Define task dependencies
ingest_task >> validate_task >> feature_task >> train_task >> evaluate_task >> register_task >> notify_task
```

### Step 3: Kubeflow Pipeline Implementation
**Duration**: 6-8 hours

**Kubeflow Pipeline**:
```python
# orchestration/kubeflow/ml_pipeline.py

import kfp
from kfp import dsl
from kfp.components import create_component_from_func, InputPath, OutputPath

@dsl.component
def ingest_data_component(
    data_source: str,
    output_path: OutputPath(str)
):
    """Data ingestion component."""
    from src.data_ingestion import DataIngestion
    import os
    
    ingestion = DataIngestion()
    data_path = ingestion.fetch_data(source=data_source)
    
    # Save path
    with open(output_path, 'w') as f:
        f.write(data_path)

@dsl.component
def validate_data_component(
    data_path: InputPath(str),
    validation_report: OutputPath(dict)
):
    """Data validation component."""
    from src.data_validation import DataValidator
    import json
    
    with open(data_path, 'r') as f:
        path = f.read()
    
    validator = DataValidator()
    report = validator.validate(path)
    
    if not report['passed']:
        raise ValueError(f"Validation failed: {report['errors']}")
    
    with open(validation_report, 'w') as f:
        json.dump(report, f)

@dsl.component
def feature_engineering_component(
    data_path: InputPath(str),
    features_path: OutputPath(str)
):
    """Feature engineering component."""
    from src.feature_engineering import FeatureEngineering
    
    with open(data_path, 'r') as f:
        path = f.read()
    
    fe = FeatureEngineering()
    output_path = fe.create_features(path)
    
    with open(features_path, 'w') as f:
        f.write(output_path)

@dsl.component(
    base_image='tensorflow/tensorflow:2.13.0-gpu',
    packages_to_install=['mlflow==2.5.0', 'scikit-learn==1.3.0']
)
def train_model_component(
    features_path: InputPath(str),
    model_metrics: OutputPath(dict)
):
    """Model training component."""
    from src.model_training import ModelTrainer
    import json
    
    with open(features_path, 'r') as f:
        path = f.read()
    
    trainer = ModelTrainer()
    metrics = trainer.train(path)
    
    with open(model_metrics, 'w') as f:
        json.dump(metrics, f)

@dsl.component
def evaluate_model_component(
    model_metrics: InputPath(dict),
    evaluation_result: OutputPath(dict)
):
    """Model evaluation component."""
    import json
    
    with open(model_metrics, 'r') as f:
        metrics = json.load(f)
    
    # Check thresholds
    passed = metrics['accuracy'] >= 0.85
    
    result = {
        'passed': passed,
        'metrics': metrics,
        'threshold': 0.85
    }
    
    with open(evaluation_result, 'w') as f:
        json.dump(result, f)
    
    if not passed:
        raise ValueError(f"Model accuracy {metrics['accuracy']} below threshold")

@dsl.pipeline(
    name='ML Training Pipeline',
    description='End-to-end ML training pipeline on Kubeflow'
)
def ml_training_pipeline(
    data_source: str = 's3://ml-data/raw/',
    model_name: str = 'fraud_detection_model'
):
    """Define ML pipeline."""
    
    # Step 1: Ingest data
    ingest_op = ingest_data_component(data_source=data_source)
    
    # Step 2: Validate data
    validate_op = validate_data_component(
        data_path=ingest_op.outputs['output_path']
    )
    
    # Step 3: Feature engineering
    feature_op = feature_engineering_component(
        data_path=ingest_op.outputs['output_path']
    ).after(validate_op)
    
    # Step 4: Train model
    train_op = train_model_component(
        features_path=feature_op.outputs['features_path']
    ).set_gpu_limit(1).set_memory_limit('8G')
    
    # Step 5: Evaluate model
    evaluate_op = evaluate_model_component(
        model_metrics=train_op.outputs['model_metrics']
    )

# Compile pipeline
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(
        pipeline_func=ml_training_pipeline,
        package_path='ml_training_pipeline.yaml'
    )
```

### Step 4: Prefect Pipeline Implementation
**Duration**: 4-6 hours

**Prefect Flow**:
```python
# orchestration/prefect/ml_flow.py

from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from datetime import timedelta
import os

@task(retries=3, retry_delay_seconds=300)
def ingest_data(data_source: str) -> str:
    """Ingest data task."""
    from src.data_ingestion import DataIngestion
    
    ingestion = DataIngestion()
    data_path = ingestion.fetch_data(source=data_source)
    
    return data_path

@task(retries=2, retry_delay_seconds=60)
def validate_data(data_path: str) -> dict:
    """Validate data task."""
    from src.data_validation import DataValidator
    
    validator = DataValidator()
    report = validator.validate(data_path)
    
    if not report['passed']:
        raise ValueError(f"Validation failed: {report['errors']}")
    
    return report

@task(retries=2, retry_delay_seconds=60)
def engineer_features(data_path: str) -> str:
    """Feature engineering task."""
    from src.feature_engineering import FeatureEngineering
    
    fe = FeatureEngineering()
    features_path = fe.create_features(data_path)
    
    return features_path

@task(retries=1, retry_delay_seconds=600, timeout_seconds=7200)
def train_model(features_path: str) -> dict:
    """Model training task."""
    from src.model_training import ModelTrainer
    
    trainer = ModelTrainer()
    metrics = trainer.train(features_path)
    
    return metrics

@task(retries=2, retry_delay_seconds=60)
def evaluate_model(metrics: dict) -> dict:
    """Model evaluation task."""
    
    passed = metrics['accuracy'] >= 0.85
    
    result = {
        'passed': passed,
        'metrics': metrics,
        'threshold': 0.85
    }
    
    if not passed:
        raise ValueError(f"Model accuracy {metrics['accuracy']} below threshold")
    
    return result

@task
def register_model(metrics: dict) -> str:
    """Model registration task."""
    import mlflow
    from mlflow.tracking import MlflowClient
    
    mlflow.set_tracking_uri(os.getenv('MLFLOW_TRACKING_URI'))
    client = MlflowClient()
    
    # Register model logic here
    model_version = "1.0.0"  # Simplified
    
    return model_version

@flow(
    name="ML Training Pipeline",
    task_runner=ConcurrentTaskRunner(),
    retries=1,
    retry_delay_seconds=600
)
def ml_training_flow(data_source: str = "s3://ml-data/raw/"):
    """Main ML training flow."""
    
    # Sequential tasks
    data_path = ingest_data(data_source)
    validation_report = validate_data(data_path)
    features_path = engineer_features(data_path)
    metrics = train_model(features_path)
    evaluation = evaluate_model(metrics)
    model_version = register_model(metrics)
    
    return {
        'data_path': data_path,
        'features_path': features_path,
        'metrics': metrics,
        'model_version': model_version
    }

# Create deployment
deployment = Deployment.build_from_flow(
    flow=ml_training_flow,
    name="ml-training-daily",
    schedule=CronSchedule(cron="0 2 * * *"),
    work_queue_name="ml-training",
    tags=["ml", "training", "production"]
)

if __name__ == "__main__":
    deployment.apply()
```

### Step 5: Error Handling & Recovery
**Duration**: 3-4 hours

**Error Handling Strategy**:
```python
# orchestration/error_handling.py

from enum import Enum
from dataclasses import dataclass
from typing import Callable, Any
import logging

class ErrorSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class ErrorHandler:
    max_retries: int = 3
    retry_delay: int = 300
    fallback_strategy: str = "skip"
    
    def handle_error(self, error: Exception, context: dict) -> dict:
        """Handle pipeline errors."""
        
        severity = self._classify_error(error)
        
        if severity == ErrorSeverity.CRITICAL:
            return self._handle_critical_error(error, context)
        elif severity == ErrorSeverity.HIGH:
            return self._handle_high_error(error, context)
        else:
            return self._handle_low_error(error, context)
    
    def _classify_error(self, error: Exception) -> ErrorSeverity:
        """Classify error severity."""
        
        if isinstance(error, (MemoryError, SystemError)):
            return ErrorSeverity.CRITICAL
        elif isinstance(error, (ValueError, KeyError)):
            return ErrorSeverity.HIGH
        else:
            return ErrorSeverity.MEDIUM
    
    def _handle_critical_error(self, error: Exception, context: dict) -> dict:
        """Handle critical errors - stop pipeline."""
        
        logging.critical(f"Critical error in pipeline: {error}")
        
        # Send alert
        self._send_alert(error, context, severity="critical")
        
        # Stop pipeline
        return {
            'action': 'stop',
            'error': str(error),
            'context': context
        }
    
    def _handle_high_error(self, error: Exception, context: dict) -> dict:
        """Handle high severity errors - retry with fallback."""
        
        logging.error(f"High severity error: {error}")
        
        # Try fallback
        if self.fallback_strategy == "skip":
            return {'action': 'skip', 'error': str(error)}
        elif self.fallback_strategy == "default":
            return {'action': 'use_default', 'error': str(error)}
        else:
            return {'action': 'retry', 'error': str(error)}
    
    def _handle_low_error(self, error: Exception, context: dict) -> dict:
        """Handle low severity errors - log and continue."""
        
        logging.warning(f"Low severity error: {error}")
        
        return {
            'action': 'continue',
            'error': str(error),
            'context': context
        }
    
    def _send_alert(self, error: Exception, context: dict, severity: str):
        """Send alert to monitoring system."""
        import requests
        
        webhook_url = os.getenv('ALERT_WEBHOOK_URL')
        
        message = {
            'severity': severity,
            'error': str(error),
            'context': context,
            'timestamp': datetime.now().isoformat()
        }
        
        requests.post(webhook_url, json=message)
```

## 3. Pipeline Monitoring & Observability

### Monitoring Dashboard
```python
# orchestration/monitoring.py

from prometheus_client import Counter, Histogram, Gauge
import time

# Metrics
pipeline_runs = Counter('pipeline_runs_total', 'Total pipeline runs', ['status'])
pipeline_duration = Histogram('pipeline_duration_seconds', 'Pipeline duration')
task_duration = Histogram('task_duration_seconds', 'Task duration', ['task_name'])
active_pipelines = Gauge('active_pipelines', 'Number of active pipelines')

class PipelineMonitor:
    
    def __init__(self):
        self.start_time = None
    
    def start_pipeline(self):
        """Start pipeline monitoring."""
        self.start_time = time.time()
        active_pipelines.inc()
    
    def end_pipeline(self, status: str):
        """End pipeline monitoring."""
        duration = time.time() - self.start_time
        pipeline_duration.observe(duration)
        pipeline_runs.labels(status=status).inc()
        active_pipelines.dec()
    
    def track_task(self, task_name: str, duration: float):
        """Track individual task."""
        task_duration.labels(task_name=task_name).observe(duration)
```

## 4. Quality Gates

### Gate 1: Pipeline Definition
- [ ] All tasks defined with clear inputs/outputs
- [ ] Dependencies mapped correctly
- [ ] No circular dependencies detected
- [ ] Resource requirements specified
- [ ] Retry policies configured

### Gate 2: Pipeline Execution
- [ ] Pipeline runs without errors
- [ ] All tasks complete successfully
- [ ] Task outputs validated
- [ ] Execution time within acceptable limits (<4 hours)
- [ ] Resource usage within limits

### Gate 3: Monitoring & Observability
- [ ] Metrics collection configured
- [ ] Logging integrated
- [ ] Alerts configured for failures
- [ ] Dashboard accessible
- [ ] Historical run data available

## 5. Deliverables

### Required Outputs
1. **Pipeline DAG** (`pipeline-dag.py`)
2. **Orchestration Config** (`orchestration-config.yaml`)
3. **Pipeline Diagram** (`pipeline-diagram.png`)
4. **Monitoring Dashboard** (`dashboard-config.json`)
5. **Error Handling Config** (`error-handling.yaml`)
6. **Deployment Script** (`deploy-pipeline.sh`)

### Evidence Package Structure
```
evidence/protocol-19-pipeline-orchestration/
├── dags/
│   ├── airflow_dag.py
│   ├── kubeflow_pipeline.yaml
│   └── prefect_flow.py
├── config/
│   ├── orchestration-config.yaml
│   ├── error-handling.yaml
│   └── monitoring-config.yaml
├── diagrams/
│   ├── pipeline-diagram.png
│   ├── dependency-graph.png
│   └── architecture-diagram.png
├── monitoring/
│   ├── dashboard-config.json
│   ├── metrics-definition.yaml
│   └── alert-rules.yaml
└── reports/
    ├── orchestration_report.md
    └── pipeline_test_results.json
```

## 6. Common Pitfalls & Solutions

### Pitfall 1: Task Dependencies Not Clear
**Solution**: Use explicit dependency declarations and visualize DAG

### Pitfall 2: Resource Contention
**Solution**: Implement resource pools and task queuing

### Pitfall 3: Long-Running Tasks
**Solution**: Break into smaller tasks with checkpoints

### Pitfall 4: Poor Error Handling
**Solution**: Implement comprehensive retry and fallback strategies

## 7. Success Criteria

- **Pipeline Reliability**: >95% success rate
- **Execution Time**: <4 hours for full pipeline
- **Resource Efficiency**: <80% resource utilization
- **Observability**: All tasks monitored and logged
- **Recovery Time**: <30 minutes for error recovery
- **Scalability**: Handles 10x data volume increase

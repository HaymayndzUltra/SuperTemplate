# Protocol 20: AI Model Deployment & Serving

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: mlops_deployment
phase: "Phase 5: MLOps & Deployment"
priority: critical
tags: [deployment, model-serving, kubernetes, blue-green, canary, rollback]
triggers: [deploy-model, model-serving, production-deployment, rollout]
```

## 1. Protocol Overview

**Purpose**: Deploy trained ML models to production environments with robust serving infrastructure, deployment strategies, health monitoring, and rollback capabilities for reliable model inference at scale.

**Critical Success Factors**:
- Zero-downtime deployments
- Scalable serving infrastructure
- Health monitoring and alerting
- Quick rollback capability
- Performance optimization
- Security and access control

## 2. Model Deployment Workflow

### Step 1: Deployment Strategy Selection
**Duration**: 2-3 hours

**Activities**:
1. Assess deployment requirements
2. Select deployment strategy
3. Plan rollout schedule
4. Define success criteria
5. Prepare rollback plan

**Deployment Strategies**:
```python
# deployment/strategies.py

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List

class DeploymentStrategy(Enum):
    BLUE_GREEN = "blue_green"
    CANARY = "canary"
    ROLLING = "rolling"
    RECREATE = "recreate"
    A_B_TEST = "a_b_test"

@dataclass
class DeploymentConfig:
    strategy: DeploymentStrategy
    replicas: int
    resources: Dict[str, str]
    health_check: Dict[str, any]
    rollback_threshold: float
    
    def validate(self):
        """Validate deployment configuration."""
        
        if self.replicas < 1:
            raise ValueError("Replicas must be at least 1")
        
        if self.strategy == DeploymentStrategy.CANARY:
            if not hasattr(self, 'canary_percentage'):
                raise ValueError("Canary deployment requires canary_percentage")
        
        if self.rollback_threshold < 0 or self.rollback_threshold > 1:
            raise ValueError("Rollback threshold must be between 0 and 1")
        
        return True

class DeploymentPlanner:
    
    def select_strategy(self, requirements: Dict) -> DeploymentStrategy:
        """Select appropriate deployment strategy."""
        
        # High-risk changes -> Blue-Green
        if requirements.get('risk_level') == 'high':
            return DeploymentStrategy.BLUE_GREEN
        
        # Gradual rollout -> Canary
        elif requirements.get('gradual_rollout'):
            return DeploymentStrategy.CANARY
        
        # Standard updates -> Rolling
        elif requirements.get('zero_downtime'):
            return DeploymentStrategy.ROLLING
        
        # Fast deployment -> Recreate
        else:
            return DeploymentStrategy.RECREATE
    
    def create_deployment_plan(self, strategy: DeploymentStrategy, config: Dict) -> Dict:
        """Create detailed deployment plan."""
        
        if strategy == DeploymentStrategy.BLUE_GREEN:
            return self._plan_blue_green(config)
        elif strategy == DeploymentStrategy.CANARY:
            return self._plan_canary(config)
        elif strategy == DeploymentStrategy.ROLLING:
            return self._plan_rolling(config)
        else:
            return self._plan_recreate(config)
    
    def _plan_blue_green(self, config: Dict) -> Dict:
        """Plan blue-green deployment."""
        return {
            'phases': [
                {'name': 'Deploy Green', 'duration': '10m'},
                {'name': 'Test Green', 'duration': '15m'},
                {'name': 'Switch Traffic', 'duration': '5m'},
                {'name': 'Monitor', 'duration': '30m'},
                {'name': 'Decommission Blue', 'duration': '5m'}
            ],
            'rollback_plan': 'Switch traffic back to Blue environment',
            'total_duration': '65m'
        }
    
    def _plan_canary(self, config: Dict) -> Dict:
        """Plan canary deployment."""
        return {
            'phases': [
                {'name': 'Deploy Canary 10%', 'duration': '10m'},
                {'name': 'Monitor 10%', 'duration': '30m'},
                {'name': 'Increase to 25%', 'duration': '5m'},
                {'name': 'Monitor 25%', 'duration': '30m'},
                {'name': 'Increase to 50%', 'duration': '5m'},
                {'name': 'Monitor 50%', 'duration': '30m'},
                {'name': 'Full Rollout', 'duration': '10m'}
            ],
            'rollback_plan': 'Route all traffic back to stable version',
            'total_duration': '120m'
        }
    
    def _plan_rolling(self, config: Dict) -> Dict:
        """Plan rolling deployment."""
        replicas = config.get('replicas', 3)
        return {
            'phases': [
                {'name': f'Update Pod {i+1}/{replicas}', 'duration': '5m'}
                for i in range(replicas)
            ],
            'rollback_plan': 'Roll back pods one by one',
            'total_duration': f'{5 * replicas}m'
        }
```

### Step 2: Kubernetes Deployment Configuration
**Duration**: 4-6 hours

**Kubernetes Manifests**:
```yaml
# deployment/kubernetes/deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-model-serving
  namespace: ml-production
  labels:
    app: ml-model
    version: v1.0.0
    environment: production
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: ml-model
  template:
    metadata:
      labels:
        app: ml-model
        version: v1.0.0
    spec:
      containers:
      - name: model-server
        image: ml-registry.company.com/ml-model:v1.0.0
        ports:
        - containerPort: 8000
          name: http
        - containerPort: 8001
          name: metrics
        env:
        - name: MODEL_PATH
          value: "/models/model.joblib"
        - name: LOG_LEVEL
          value: "INFO"
        - name: WORKERS
          value: "4"
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
        volumeMounts:
        - name: model-storage
          mountPath: /models
          readOnly: true
      volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: model-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: ml-model-service
  namespace: ml-production
spec:
  type: LoadBalancer
  selector:
    app: ml-model
  ports:
  - name: http
    port: 80
    targetPort: 8000
    protocol: TCP
  - name: metrics
    port: 8001
    targetPort: 8001
    protocol: TCP
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ml-model-hpa
  namespace: ml-production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ml-model-serving
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 30
```

**Blue-Green Deployment**:
```yaml
# deployment/kubernetes/blue-green.yaml

# Blue Deployment (Current)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-model-blue
  namespace: ml-production
  labels:
    app: ml-model
    version: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ml-model
      version: blue
  template:
    metadata:
      labels:
        app: ml-model
        version: blue
    spec:
      containers:
      - name: model-server
        image: ml-registry.company.com/ml-model:v1.0.0
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
---
# Green Deployment (New)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-model-green
  namespace: ml-production
  labels:
    app: ml-model
    version: green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ml-model
      version: green
  template:
    metadata:
      labels:
        app: ml-model
        version: green
    spec:
      containers:
      - name: model-server
        image: ml-registry.company.com/ml-model:v1.1.0
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
---
# Service (switches between blue and green)
apiVersion: v1
kind: Service
metadata:
  name: ml-model-service
  namespace: ml-production
spec:
  type: LoadBalancer
  selector:
    app: ml-model
    version: blue  # Change to 'green' to switch
  ports:
  - port: 80
    targetPort: 8000
```

**Canary Deployment with Istio**:
```yaml
# deployment/kubernetes/canary-istio.yaml

apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ml-model-vs
  namespace: ml-production
spec:
  hosts:
  - ml-model-service
  http:
  - match:
    - headers:
        canary:
          exact: "true"
    route:
    - destination:
        host: ml-model-service
        subset: canary
      weight: 100
  - route:
    - destination:
        host: ml-model-service
        subset: stable
      weight: 90
    - destination:
        host: ml-model-service
        subset: canary
      weight: 10
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: ml-model-dr
  namespace: ml-production
spec:
  host: ml-model-service
  subsets:
  - name: stable
    labels:
      version: v1.0.0
  - name: canary
    labels:
      version: v1.1.0
```

### Step 3: Model Serving Infrastructure
**Duration**: 6-8 hours

**TensorFlow Serving**:
```python
# deployment/serving/tensorflow_serving.py

import tensorflow as tf
import grpc
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
import numpy as np

class TensorFlowServingClient:
    
    def __init__(self, host='localhost', port=8500):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = prediction_service_pb2_grpc.PredictionServiceStub(self.channel)
    
    def predict(self, model_name, model_version, input_data):
        """Make prediction using TensorFlow Serving."""
        
        # Create request
        request = predict_pb2.PredictRequest()
        request.model_spec.name = model_name
        request.model_spec.version.value = model_version
        request.model_spec.signature_name = 'serving_default'
        
        # Add input data
        request.inputs['input'].CopyFrom(
            tf.make_tensor_proto(input_data, dtype=tf.float32)
        )
        
        # Make prediction
        result = self.stub.Predict(request, timeout=10.0)
        
        # Extract output
        output = tf.make_ndarray(result.outputs['output'])
        
        return output
```

**TorchServe Configuration**:
```python
# deployment/serving/torchserve_handler.py

import torch
import json
from ts.torch_handler.base_handler import BaseHandler

class CustomModelHandler(BaseHandler):
    
    def initialize(self, context):
        """Initialize model handler."""
        
        self.manifest = context.manifest
        properties = context.system_properties
        model_dir = properties.get("model_dir")
        
        # Load model
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model_file = self.manifest['model']['serializedFile']
        model_path = f"{model_dir}/{model_file}"
        
        self.model = torch.jit.load(model_path, map_location=self.device)
        self.model.eval()
        
        self.initialized = True
    
    def preprocess(self, data):
        """Preprocess input data."""
        
        inputs = []
        for row in data:
            input_data = row.get("data") or row.get("body")
            
            if isinstance(input_data, (bytes, bytearray)):
                input_data = input_data.decode('utf-8')
            
            input_json = json.loads(input_data)
            input_tensor = torch.tensor(input_json['input'], dtype=torch.float32)
            inputs.append(input_tensor)
        
        return torch.stack(inputs).to(self.device)
    
    def inference(self, data):
        """Run inference."""
        
        with torch.no_grad():
            predictions = self.model(data)
        
        return predictions
    
    def postprocess(self, data):
        """Postprocess predictions."""
        
        predictions = data.cpu().numpy().tolist()
        
        return [json.dumps({'prediction': pred}) for pred in predictions]
```

**FastAPI Model Server**:
```python
# deployment/serving/fastapi_server.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List
import logging

app = FastAPI(title="ML Model API", version="1.0.0")

# Load model at startup
model = None

@app.on_event("startup")
async def load_model():
    """Load model on startup."""
    global model
    try:
        model = joblib.load('/models/model.joblib')
        logging.info("Model loaded successfully")
    except Exception as e:
        logging.error(f"Failed to load model: {e}")
        raise

class PredictionRequest(BaseModel):
    features: List[float]
    
class PredictionResponse(BaseModel):
    prediction: float
    probability: float
    model_version: str

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "model_loaded": model is not None}

@app.get("/ready")
async def readiness_check():
    """Readiness check endpoint."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ready"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Prediction endpoint."""
    
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Prepare input
        features = np.array(request.features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].max()
        
        return PredictionResponse(
            prediction=float(prediction),
            probability=float(probability),
            model_version="1.0.0"
        )
    
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch_predict")
async def batch_predict(requests: List[PredictionRequest]):
    """Batch prediction endpoint."""
    
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Prepare batch input
        features = np.array([req.features for req in requests])
        
        # Make predictions
        predictions = model.predict(features)
        probabilities = model.predict_proba(features).max(axis=1)
        
        return [
            PredictionResponse(
                prediction=float(pred),
                probability=float(prob),
                model_version="1.0.0"
            )
            for pred, prob in zip(predictions, probabilities)
        ]
    
    except Exception as e:
        logging.error(f"Batch prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint."""
    # Return Prometheus-formatted metrics
    return {"metrics": "placeholder"}
```

### Step 4: Health Checks & Monitoring
**Duration**: 3-4 hours

**Health Check Implementation**:
```python
# deployment/health_checks.py

from enum import Enum
import time
import psutil
import requests

class HealthStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

class HealthChecker:
    
    def __init__(self, model, thresholds):
        self.model = model
        self.thresholds = thresholds
        self.start_time = time.time()
    
    def check_health(self) -> dict:
        """Comprehensive health check."""
        
        checks = {
            'model_loaded': self._check_model_loaded(),
            'memory_usage': self._check_memory(),
            'cpu_usage': self._check_cpu(),
            'response_time': self._check_response_time(),
            'error_rate': self._check_error_rate()
        }
        
        # Determine overall status
        if all(check['status'] == 'ok' for check in checks.values()):
            overall_status = HealthStatus.HEALTHY
        elif any(check['status'] == 'critical' for check in checks.values()):
            overall_status = HealthStatus.UNHEALTHY
        else:
            overall_status = HealthStatus.DEGRADED
        
        return {
            'status': overall_status.value,
            'uptime_seconds': time.time() - self.start_time,
            'checks': checks
        }
    
    def _check_model_loaded(self) -> dict:
        """Check if model is loaded."""
        loaded = self.model is not None
        return {
            'status': 'ok' if loaded else 'critical',
            'message': 'Model loaded' if loaded else 'Model not loaded'
        }
    
    def _check_memory(self) -> dict:
        """Check memory usage."""
        memory = psutil.virtual_memory()
        usage_percent = memory.percent
        
        if usage_percent > self.thresholds['memory_critical']:
            status = 'critical'
        elif usage_percent > self.thresholds['memory_warning']:
            status = 'warning'
        else:
            status = 'ok'
        
        return {
            'status': status,
            'usage_percent': usage_percent,
            'available_mb': memory.available / (1024 * 1024)
        }
    
    def _check_cpu(self) -> dict:
        """Check CPU usage."""
        cpu_percent = psutil.cpu_percent(interval=1)
        
        if cpu_percent > self.thresholds['cpu_critical']:
            status = 'critical'
        elif cpu_percent > self.thresholds['cpu_warning']:
            status = 'warning'
        else:
            status = 'ok'
        
        return {
            'status': status,
            'usage_percent': cpu_percent
        }
    
    def _check_response_time(self) -> dict:
        """Check average response time."""
        # Placeholder - would track actual response times
        avg_response_time = 0.05  # seconds
        
        if avg_response_time > self.thresholds['response_time_critical']:
            status = 'critical'
        elif avg_response_time > self.thresholds['response_time_warning']:
            status = 'warning'
        else:
            status = 'ok'
        
        return {
            'status': status,
            'avg_response_time_ms': avg_response_time * 1000
        }
    
    def _check_error_rate(self) -> dict:
        """Check error rate."""
        # Placeholder - would track actual errors
        error_rate = 0.01  # 1%
        
        if error_rate > self.thresholds['error_rate_critical']:
            status = 'critical'
        elif error_rate > self.thresholds['error_rate_warning']:
            status = 'warning'
        else:
            status = 'ok'
        
        return {
            'status': status,
            'error_rate_percent': error_rate * 100
        }
```

### Step 5: Rollback Procedures
**Duration**: 2-3 hours

**Automated Rollback**:
```python
# deployment/rollback.py

import subprocess
import logging
from datetime import datetime

class RollbackManager:
    
    def __init__(self, namespace='ml-production'):
        self.namespace = namespace
        self.rollback_history = []
    
    def check_rollback_criteria(self, metrics: dict) -> bool:
        """Check if rollback is needed."""
        
        criteria = {
            'error_rate': metrics.get('error_rate', 0) > 0.05,  # >5% errors
            'latency': metrics.get('avg_latency', 0) > 1.0,  # >1s latency
            'availability': metrics.get('availability', 1.0) < 0.95,  # <95% uptime
            'memory_errors': metrics.get('oom_errors', 0) > 0
        }
        
        # Rollback if any critical criteria met
        should_rollback = any(criteria.values())
        
        if should_rollback:
            logging.warning(f"Rollback criteria met: {criteria}")
        
        return should_rollback
    
    def rollback_deployment(self, deployment_name: str) -> bool:
        """Rollback Kubernetes deployment."""
        
        try:
            # Rollback to previous revision
            cmd = [
                'kubectl', 'rollout', 'undo',
                f'deployment/{deployment_name}',
                f'--namespace={self.namespace}'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logging.info(f"Rollback successful for {deployment_name}")
                self._record_rollback(deployment_name, 'success')
                return True
            else:
                logging.error(f"Rollback failed: {result.stderr}")
                self._record_rollback(deployment_name, 'failed', result.stderr)
                return False
        
        except Exception as e:
            logging.error(f"Rollback exception: {e}")
            self._record_rollback(deployment_name, 'error', str(e))
            return False
    
    def rollback_blue_green(self, service_name: str, target_version: str) -> bool:
        """Rollback blue-green deployment by switching service selector."""
        
        try:
            # Update service to point to previous version
            cmd = [
                'kubectl', 'patch', 'service', service_name,
                f'--namespace={self.namespace}',
                '-p', f'{{"spec":{{"selector":{{"version":"{target_version}"}}}}}}'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logging.info(f"Blue-green rollback successful to {target_version}")
                return True
            else:
                logging.error(f"Blue-green rollback failed: {result.stderr}")
                return False
        
        except Exception as e:
            logging.error(f"Blue-green rollback exception: {e}")
            return False
    
    def _record_rollback(self, deployment: str, status: str, error: str = None):
        """Record rollback in history."""
        
        self.rollback_history.append({
            'timestamp': datetime.now().isoformat(),
            'deployment': deployment,
            'status': status,
            'error': error
        })
```

**Rollback Plan Document**:
```markdown
# deployment/rollback-plan.md

# Model Deployment Rollback Plan

## Rollback Triggers
1. **Error Rate**: >5% of requests failing
2. **Latency**: P95 latency >1 second
3. **Availability**: <95% uptime
4. **Memory**: OOM errors detected
5. **Manual**: Operator-initiated rollback

## Rollback Procedures

### Rolling Deployment Rollback
```bash
kubectl rollout undo deployment/ml-model-serving -n ml-production
kubectl rollout status deployment/ml-model-serving -n ml-production
```

### Blue-Green Rollback
```bash
# Switch service back to blue
kubectl patch service ml-model-service -n ml-production \
  -p '{"spec":{"selector":{"version":"blue"}}}'
```

### Canary Rollback
```bash
# Remove canary traffic routing
kubectl apply -f deployment/kubernetes/stable-only.yaml
```

## Validation Steps
1. Check service health: `curl http://ml-model-service/health`
2. Verify metrics dashboard
3. Monitor error logs
4. Test sample predictions

## Communication
- Notify team via Slack #ml-alerts
- Update incident ticket
- Document rollback reason
```

## 3. Load Balancing & Scaling

**Load Balancer Configuration**:
```yaml
# deployment/load-balancer.yaml

apiVersion: v1
kind: Service
metadata:
  name: ml-model-lb
  namespace: ml-production
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
    service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"
spec:
  type: LoadBalancer
  selector:
    app: ml-model
  ports:
  - port: 80
    targetPort: 8000
    protocol: TCP
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800
```

## 4. Quality Gates

### Gate 1: Pre-Deployment Validation
- [ ] Model package validated and tested
- [ ] Deployment manifests reviewed
- [ ] Resource requirements verified
- [ ] Health checks configured
- [ ] Rollback plan documented

### Gate 2: Deployment Execution
- [ ] Deployment completed without errors
- [ ] All pods running and ready
- [ ] Health checks passing
- [ ] Load balancer configured
- [ ] Metrics collection active

### Gate 3: Post-Deployment Validation
- [ ] Prediction accuracy matches expectations
- [ ] Response time <500ms (P95)
- [ ] Error rate <1%
- [ ] Resource usage within limits
- [ ] Monitoring alerts configured

## 5. Deliverables

### Required Outputs
1. **Deployment Manifest** (`deployment-manifest.yaml`)
2. **Service Configuration** (`serving-config.json`)
3. **Rollback Plan** (`rollback-plan.md`)
4. **Health Check Config** (`health-checks.yaml`)
5. **Load Balancer Config** (`load-balancer.yaml`)
6. **Deployment Script** (`deploy.sh`)

### Evidence Package Structure
```
evidence/protocol-20-model-deployment/
├── manifests/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   └── blue-green.yaml
├── serving/
│   ├── fastapi_server.py
│   ├── torchserve_config.json
│   └── tensorflow_serving_config.yaml
├── monitoring/
│   ├── health-checks.yaml
│   ├── metrics-config.yaml
│   └── alert-rules.yaml
├── rollback/
│   ├── rollback-plan.md
│   ├── rollback-script.sh
│   └── rollback-history.json
└── reports/
    ├── deployment_report.md
    └── validation_results.json
```

## 6. Common Pitfalls & Solutions

### Pitfall 1: Insufficient Resources
**Solution**: Load test before production and set appropriate resource limits

### Pitfall 2: No Rollback Plan
**Solution**: Always prepare and test rollback procedures before deployment

### Pitfall 3: Missing Health Checks
**Solution**: Implement comprehensive health and readiness probes

### Pitfall 4: Cold Start Delays
**Solution**: Use readiness probes and warm-up periods

## 7. Success Criteria

- **Deployment Success**: 100% of pods running and ready
- **Zero Downtime**: No service interruption during deployment
- **Response Time**: P95 <500ms, P99 <1s
- **Error Rate**: <1% of requests
- **Availability**: >99.9% uptime
- **Rollback Time**: <5 minutes if needed

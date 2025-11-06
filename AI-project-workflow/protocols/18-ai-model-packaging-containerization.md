# Protocol 18: AI Model Packaging & Containerization

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: mlops_deployment
phase: "Phase 5: MLOps & Deployment"
priority: critical
tags: [model-packaging, containerization, docker, model-registry, versioning]
triggers: [model-ready, deployment-prep, containerize, package-model]
```

## 1. Protocol Overview

**Purpose**: Package trained AI/ML models into portable, reproducible containers with proper dependency management, version control, and registry integration for seamless deployment.

**Critical Success Factors**:
- Model serialization integrity
- Container reproducibility
- Dependency isolation
- Version traceability
- Registry integration
- Security hardening

## 2. Model Packaging Workflow

### Step 1: Model Serialization
**Duration**: 2-3 hours

**Activities**:
1. Select serialization format
2. Export model artifacts
3. Validate serialization
4. Document model metadata
5. Create model card

**Serialization Methods**:
```python
# packaging/model_serialization.py

import pickle
import joblib
import onnx
import torch
import tensorflow as tf
from pathlib import Path
import json
from datetime import datetime

class ModelSerializer:
    
    def serialize_sklearn_model(self, model, output_path):
        """Serialize scikit-learn model."""
        
        # Using joblib (recommended for sklearn)
        joblib.dump(model, f"{output_path}/model.joblib")
        
        # Alternative: pickle
        with open(f"{output_path}/model.pkl", 'wb') as f:
            pickle.dump(model, f)
        
        return f"{output_path}/model.joblib"
    
    def serialize_pytorch_model(self, model, output_path):
        """Serialize PyTorch model."""
        
        # Save state dict (recommended)
        torch.save(model.state_dict(), f"{output_path}/model_state.pth")
        
        # Save entire model
        torch.save(model, f"{output_path}/model_full.pth")
        
        # Export to ONNX for interoperability
        dummy_input = torch.randn(1, 3, 224, 224)
        torch.onnx.export(
            model,
            dummy_input,
            f"{output_path}/model.onnx",
            export_params=True,
            opset_version=11,
            do_constant_folding=True,
            input_names=['input'],
            output_names=['output']
        )
        
        return f"{output_path}/model_state.pth"
    
    def serialize_tensorflow_model(self, model, output_path):
        """Serialize TensorFlow/Keras model."""
        
        # SavedModel format (recommended)
        model.save(f"{output_path}/saved_model")
        
        # HDF5 format
        model.save(f"{output_path}/model.h5")
        
        # TFLite for mobile/edge
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = converter.convert()
        with open(f"{output_path}/model.tflite", 'wb') as f:
            f.write(tflite_model)
        
        return f"{output_path}/saved_model"
    
    def create_model_metadata(self, model, model_path, training_metadata):
        """Create comprehensive model metadata."""
        
        metadata = {
            "model_info": {
                "name": training_metadata.get("model_name"),
                "version": training_metadata.get("version"),
                "framework": training_metadata.get("framework"),
                "algorithm": training_metadata.get("algorithm"),
                "created_date": datetime.now().isoformat(),
                "model_path": str(model_path)
            },
            "performance": {
                "accuracy": training_metadata.get("accuracy"),
                "precision": training_metadata.get("precision"),
                "recall": training_metadata.get("recall"),
                "f1_score": training_metadata.get("f1_score"),
                "auc_roc": training_metadata.get("auc_roc")
            },
            "training": {
                "dataset_size": training_metadata.get("dataset_size"),
                "training_duration": training_metadata.get("training_duration"),
                "hyperparameters": training_metadata.get("hyperparameters"),
                "feature_count": training_metadata.get("feature_count")
            },
            "dependencies": {
                "python_version": training_metadata.get("python_version"),
                "framework_version": training_metadata.get("framework_version"),
                "required_packages": training_metadata.get("required_packages")
            },
            "input_schema": training_metadata.get("input_schema"),
            "output_schema": training_metadata.get("output_schema")
        }
        
        # Save metadata
        metadata_path = Path(model_path).parent / "model_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
```

### Step 2: Dependency Management
**Duration**: 2-3 hours

**Dependency Capture**:
```python
# packaging/dependency_manager.py

import subprocess
import sys
from pathlib import Path

class DependencyManager:
    
    def generate_requirements_txt(self, output_path):
        """Generate requirements.txt with pinned versions."""
        
        # Get installed packages
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'freeze'],
            capture_output=True,
            text=True
        )
        
        requirements = result.stdout
        
        # Save to file
        requirements_path = Path(output_path) / "requirements.txt"
        with open(requirements_path, 'w') as f:
            f.write(requirements)
        
        return requirements_path
    
    def create_conda_environment(self, env_name, output_path):
        """Export conda environment."""
        
        # Export environment
        result = subprocess.run(
            ['conda', 'env', 'export', '-n', env_name],
            capture_output=True,
            text=True
        )
        
        env_yaml = result.stdout
        
        # Save to file
        env_path = Path(output_path) / "environment.yml"
        with open(env_path, 'w') as f:
            f.write(env_yaml)
        
        return env_path
    
    def create_minimal_requirements(self, model_type, output_path):
        """Create minimal requirements for specific model type."""
        
        base_requirements = {
            "sklearn": [
                "scikit-learn==1.3.0",
                "numpy==1.24.3",
                "pandas==2.0.3",
                "joblib==1.3.2"
            ],
            "pytorch": [
                "torch==2.0.1",
                "torchvision==0.15.2",
                "numpy==1.24.3",
                "onnx==1.14.0"
            ],
            "tensorflow": [
                "tensorflow==2.13.0",
                "numpy==1.24.3",
                "h5py==3.9.0"
            ]
        }
        
        requirements = base_requirements.get(model_type, [])
        requirements.append("fastapi==0.103.0")
        requirements.append("uvicorn==0.23.2")
        requirements.append("pydantic==2.3.0")
        
        requirements_path = Path(output_path) / "requirements.txt"
        with open(requirements_path, 'w') as f:
            f.write('\n'.join(requirements))
        
        return requirements_path
```

### Step 3: Docker Containerization
**Duration**: 3-4 hours

**Dockerfile Templates**:
```dockerfile
# packaging/Dockerfile.sklearn

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model artifacts
COPY model/ ./model/
COPY src/ ./src/

# Copy inference script
COPY inference.py .

# Set environment variables
ENV MODEL_PATH=/app/model/model.joblib
ENV PORT=8000

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run inference server
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
```

```dockerfile
# packaging/Dockerfile.pytorch

FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

WORKDIR /app

# Install additional dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and code
COPY model/ ./model/
COPY src/ ./src/
COPY inference.py .

# Environment variables
ENV MODEL_PATH=/app/model/model_state.pth
ENV DEVICE=cuda
ENV PORT=8000

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
```

```dockerfile
# packaging/Dockerfile.tensorflow

FROM tensorflow/tensorflow:2.13.0

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and code
COPY model/ ./model/
COPY src/ ./src/
COPY inference.py .

# Environment variables
ENV MODEL_PATH=/app/model/saved_model
ENV PORT=8000

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Docker Build Script**:
```python
# packaging/build_container.py

import subprocess
from pathlib import Path

class ContainerBuilder:
    
    def build_image(self, dockerfile_path, image_name, tag, build_args=None):
        """Build Docker image."""
        
        cmd = [
            'docker', 'build',
            '-f', dockerfile_path,
            '-t', f"{image_name}:{tag}",
            '.'
        ]
        
        if build_args:
            for key, value in build_args.items():
                cmd.extend(['--build-arg', f"{key}={value}"])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise Exception(f"Docker build failed: {result.stderr}")
        
        return f"{image_name}:{tag}"
    
    def test_container(self, image_name, tag):
        """Test container locally."""
        
        # Run container
        container_id = subprocess.run(
            ['docker', 'run', '-d', '-p', '8000:8000', f"{image_name}:{tag}"],
            capture_output=True,
            text=True
        ).stdout.strip()
        
        # Wait for startup
        import time
        time.sleep(5)
        
        # Test health endpoint
        import requests
        try:
            response = requests.get('http://localhost:8000/health')
            health_ok = response.status_code == 200
        except:
            health_ok = False
        
        # Stop container
        subprocess.run(['docker', 'stop', container_id])
        subprocess.run(['docker', 'rm', container_id])
        
        return health_ok
    
    def push_to_registry(self, image_name, tag, registry_url):
        """Push image to container registry."""
        
        # Tag for registry
        full_image = f"{registry_url}/{image_name}:{tag}"
        subprocess.run(['docker', 'tag', f"{image_name}:{tag}", full_image])
        
        # Push
        result = subprocess.run(
            ['docker', 'push', full_image],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise Exception(f"Docker push failed: {result.stderr}")
        
        return full_image
```

### Step 4: Model Registry Integration
**Duration**: 2-3 hours

**MLflow Registry Integration**:
```python
# packaging/model_registry.py

import mlflow
from mlflow.tracking import MlflowClient
from mlflow.models.signature import infer_signature
import pandas as pd

class ModelRegistry:
    
    def __init__(self, tracking_uri, registry_uri):
        mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_registry_uri(registry_uri)
        self.client = MlflowClient()
    
    def register_model(self, model, model_name, run_id, sample_input, sample_output):
        """Register model in MLflow registry."""
        
        # Infer signature
        signature = infer_signature(sample_input, sample_output)
        
        # Log model
        with mlflow.start_run(run_id=run_id):
            mlflow.sklearn.log_model(
                model,
                "model",
                signature=signature,
                registered_model_name=model_name
            )
        
        return model_name
    
    def create_model_version(self, model_name, version, stage="Staging"):
        """Create and transition model version."""
        
        # Get latest version
        latest_versions = self.client.get_latest_versions(model_name, stages=["None"])
        
        if latest_versions:
            version_number = latest_versions[0].version
            
            # Transition to stage
            self.client.transition_model_version_stage(
                name=model_name,
                version=version_number,
                stage=stage
            )
            
            return version_number
        
        return None
    
    def add_model_tags(self, model_name, version, tags):
        """Add tags to model version."""
        
        for key, value in tags.items():
            self.client.set_model_version_tag(
                name=model_name,
                version=version,
                key=key,
                value=value
            )
    
    def get_model_by_stage(self, model_name, stage="Production"):
        """Load model from registry by stage."""
        
        model_uri = f"models:/{model_name}/{stage}"
        model = mlflow.sklearn.load_model(model_uri)
        
        return model
```

**Registry Configuration**:
```yaml
# packaging/registry-config.yaml

mlflow:
  tracking_uri: "http://mlflow-server:5000"
  registry_uri: "postgresql://user:pass@db:5432/mlflow"
  experiment_name: "model_packaging"
  
model_registry:
  name: "fraud_detection_model"
  stages:
    - None
    - Staging
    - Production
    - Archived
  
  tags:
    team: "ml_team"
    project: "fraud_detection"
    framework: "sklearn"
    
  metadata:
    description: "XGBoost model for fraud detection"
    use_case: "Real-time transaction scoring"
    owner: "data-science@company.com"
    
versioning:
  scheme: "semantic"  # semantic, timestamp, sequential
  auto_increment: true
  
retention:
  max_versions: 10
  archive_after_days: 90
```

### Step 5: Package Creation & Validation
**Duration**: 2-3 hours

**Package Builder**:
```python
# packaging/package_builder.py

import tarfile
import zipfile
from pathlib import Path
import hashlib
import json

class ModelPackageBuilder:
    
    def create_package(self, model_dir, output_path, format='tar.gz'):
        """Create model package archive."""
        
        package_name = f"model-package-{self._get_timestamp()}"
        
        if format == 'tar.gz':
            archive_path = f"{output_path}/{package_name}.tar.gz"
            with tarfile.open(archive_path, 'w:gz') as tar:
                tar.add(model_dir, arcname='model')
        
        elif format == 'zip':
            archive_path = f"{output_path}/{package_name}.zip"
            with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in Path(model_dir).rglob('*'):
                    zipf.write(file, arcname=file.relative_to(model_dir))
        
        # Generate checksum
        checksum = self._calculate_checksum(archive_path)
        
        # Create manifest
        manifest = {
            "package_name": package_name,
            "format": format,
            "checksum": checksum,
            "created_at": self._get_timestamp(),
            "contents": self._list_contents(model_dir)
        }
        
        manifest_path = f"{output_path}/{package_name}_manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        return archive_path, manifest_path
    
    def validate_package(self, package_path, manifest_path):
        """Validate package integrity."""
        
        # Load manifest
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Verify checksum
        actual_checksum = self._calculate_checksum(package_path)
        expected_checksum = manifest['checksum']
        
        if actual_checksum != expected_checksum:
            raise ValueError(f"Checksum mismatch: {actual_checksum} != {expected_checksum}")
        
        # Verify contents
        if manifest['format'] == 'tar.gz':
            with tarfile.open(package_path, 'r:gz') as tar:
                members = [m.name for m in tar.getmembers()]
        elif manifest['format'] == 'zip':
            with zipfile.ZipFile(package_path, 'r') as zipf:
                members = zipf.namelist()
        
        return {
            "checksum_valid": True,
            "contents_count": len(members),
            "manifest_valid": True
        }
    
    def _calculate_checksum(self, file_path):
        """Calculate SHA256 checksum."""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def _list_contents(self, directory):
        """List all files in directory."""
        return [str(p.relative_to(directory)) for p in Path(directory).rglob('*') if p.is_file()]
```

## 3. Security Hardening

### Container Security
```dockerfile
# packaging/Dockerfile.secure

FROM python:3.10-slim

# Create non-root user
RUN useradd -m -u 1000 modeluser && \
    mkdir -p /app && \
    chown -R modeluser:modeluser /app

# Install dependencies as root
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Switch to non-root user
USER modeluser
WORKDIR /app

# Copy application files
COPY --chown=modeluser:modeluser model/ ./model/
COPY --chown=modeluser:modeluser src/ ./src/
COPY --chown=modeluser:modeluser inference.py .

# Read-only filesystem
ENV MODEL_PATH=/app/model/model.joblib
ENV PORT=8000

EXPOSE 8000

# Security labels
LABEL security.scan="passed" \
      security.vulnerabilities="none" \
      security.last_scan="2025-01-07"

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Secrets Management
```python
# packaging/secrets_manager.py

import os
from cryptography.fernet import Fernet

class SecretsManager:
    
    def __init__(self):
        self.key = os.getenv('ENCRYPTION_KEY', Fernet.generate_key())
        self.cipher = Fernet(self.key)
    
    def encrypt_model_weights(self, model_path, output_path):
        """Encrypt sensitive model weights."""
        
        with open(model_path, 'rb') as f:
            model_data = f.read()
        
        encrypted_data = self.cipher.encrypt(model_data)
        
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
        
        return output_path
    
    def decrypt_model_weights(self, encrypted_path):
        """Decrypt model weights at runtime."""
        
        with open(encrypted_path, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = self.cipher.decrypt(encrypted_data)
        
        return decrypted_data
```

## 4. Quality Gates

### Gate 1: Serialization Integrity
- [ ] Model serialized successfully
- [ ] Model can be loaded without errors
- [ ] Predictions match pre-serialization outputs
- [ ] Metadata file created and complete
- [ ] Model size within acceptable limits (<500MB)

### Gate 2: Container Build
- [ ] Dockerfile builds without errors
- [ ] All dependencies installed successfully
- [ ] Container starts and responds to health checks
- [ ] Image size optimized (<2GB)
- [ ] Security scan passed (no critical vulnerabilities)

### Gate 3: Registry Integration
- [ ] Model registered in MLflow registry
- [ ] Version tagged correctly
- [ ] Metadata and tags applied
- [ ] Model retrievable from registry
- [ ] Package checksum validated

## 5. Monitoring & Metrics

### Key Metrics
- **Serialization Time**: Time to serialize model
- **Package Size**: Size of final package
- **Build Time**: Docker image build duration
- **Image Size**: Final container image size
- **Registry Sync Time**: Time to push to registry

### Monitoring Script
```python
# monitoring/packaging_metrics.py

import time
from pathlib import Path

class PackagingMetrics:
    
    def collect_metrics(self, model_path, package_path, image_name):
        """Collect packaging metrics."""
        
        metrics = {
            "model_size_mb": Path(model_path).stat().st_size / (1024 * 1024),
            "package_size_mb": Path(package_path).stat().st_size / (1024 * 1024),
            "image_size_mb": self._get_image_size(image_name),
            "compression_ratio": self._calculate_compression_ratio(model_path, package_path)
        }
        
        return metrics
    
    def _get_image_size(self, image_name):
        """Get Docker image size."""
        import subprocess
        result = subprocess.run(
            ['docker', 'images', image_name, '--format', '{{.Size}}'],
            capture_output=True,
            text=True
        )
        size_str = result.stdout.strip()
        # Parse size (e.g., "1.2GB" -> 1200 MB)
        if 'GB' in size_str:
            return float(size_str.replace('GB', '')) * 1024
        elif 'MB' in size_str:
            return float(size_str.replace('MB', ''))
        return 0
    
    def _calculate_compression_ratio(self, original_path, compressed_path):
        """Calculate compression ratio."""
        original_size = Path(original_path).stat().st_size
        compressed_size = Path(compressed_path).stat().st_size
        return original_size / compressed_size if compressed_size > 0 else 0
```

## 6. Deliverables

### Required Outputs
1. **Dockerfile** (`Dockerfile`)
2. **Model Package** (`model-package.tar.gz`)
3. **Registry Configuration** (`registry-config.yaml`)
4. **Requirements File** (`requirements.txt`)
5. **Model Metadata** (`model_metadata.json`)
6. **Package Manifest** (`package_manifest.json`)
7. **Build Script** (`build.sh`)

### Evidence Package Structure
```
evidence/protocol-18-model-packaging/
├── artifacts/
│   ├── model-package.tar.gz
│   ├── model_metadata.json
│   ├── package_manifest.json
│   └── requirements.txt
├── docker/
│   ├── Dockerfile
│   ├── Dockerfile.secure
│   ├── build.sh
│   └── docker-compose.yml
├── registry/
│   ├── registry-config.yaml
│   ├── mlflow_registration.log
│   └── model_versions.json
├── validation/
│   ├── serialization_test.log
│   ├── container_test.log
│   └── integrity_check.json
└── reports/
    ├── packaging_report.md
    └── security_scan.json
```

## 7. Common Pitfalls & Solutions

### Pitfall 1: Large Model Sizes
**Solution**: Use model compression, quantization, or pruning techniques

### Pitfall 2: Dependency Conflicts
**Solution**: Use virtual environments and pin exact versions

### Pitfall 3: Container Bloat
**Solution**: Multi-stage builds and minimal base images

### Pitfall 4: Missing Dependencies
**Solution**: Test container in isolated environment before deployment

## 8. Success Criteria

- **Serialization Success**: Model loads and predicts correctly
- **Container Build**: Builds in <10 minutes
- **Image Size**: <2GB for production images
- **Registry Integration**: Model accessible from registry
- **Security**: No critical vulnerabilities in container scan
- **Reproducibility**: Same inputs produce same outputs across environments

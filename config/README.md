# MASTER RAY™ Configuration

**Central Configuration Files for the Workflow System**

---

## 🎯 Overview

This directory contains all configuration files that control how MASTER RAY™ behaves. Configurations define classification dimensions, protocol dependencies, validation thresholds, and system-wide settings.

### Key Features

- **YAML & JSON Formats**: Human-readable configuration
- **Schema Validation**: JSON Schema for all configs
- **Version Controlled**: Track configuration changes
- **Environment Support**: Dev, staging, production configs

---

## 📂 Configuration Files

```
config/
├── README.md                           # This file
│
├── classification-dimensions.yaml      # 27+ project classification dimensions
├── protocol-dependencies.json          # Protocol dependency graph
├── protocol-registry.json              # Available protocols metadata
├── validation-thresholds.yaml          # Validator pass/fail thresholds
├── orchestration-config.yaml           # Protocol 05b settings
│
└── schemas/                            # JSON schemas for validation
    ├── classification.schema.json
    ├── protocol.schema.json
    └── execution-plan.schema.json
```

---

## 📜 Classification Dimensions

**File**: `classification-dimensions.yaml`

Defines the 27+ dimensions used by Protocol 05b to classify projects.

### Structure

```yaml
version: "1.0.0"
last_updated: "2025-01-15"

dimensions:
  - id: ml_training
    name: "Machine Learning Training"
    category: ai_ml
    description: "Project involves training ML models"
    keywords:
      - "train"
      - "model"
      - "neural network"
      - "deep learning"
      - "machine learning"
    tech_indicators:
      - "tensorflow"
      - "pytorch"
      - "scikit-learn"
      - "keras"
    confidence_weight: 1.2
    
  - id: web_application
    name: "Web Application"
    category: application
    description: "Browser-based user interface"
    keywords:
      - "web"
      - "frontend"
      - "UI"
      - "dashboard"
    tech_indicators:
      - "react"
      - "vue"
      - "angular"
      - "nextjs"
    confidence_weight: 1.0

classification_rules:
  - type: ai_ml_application
    display_name: "AI/ML Application"
    required_dimensions:
      - ml_training
      - ml_inference
    optional_dimensions:
      - web_application
      - api_service
    min_confidence: 0.7
    protocol_track: ai_ml
    
  - type: generic_web_app
    display_name: "Generic Web Application"
    required_dimensions:
      - web_application
    excluded_dimensions:
      - ml_training
    min_confidence: 0.6
    protocol_track: generic
```

### Dimension Categories

| Category | Dimensions | Purpose |
|----------|------------|---------|
| `ai_ml` | ml_training, ml_inference, llm_integration, computer_vision, nlp, data_science | Detect ML projects |
| `data` | data_pipeline, data_warehouse, real_time_streaming, batch_processing, etl | Detect data projects |
| `application` | web_application, mobile_app, api_service, microservices, cli_tool | Detect app types |
| `infrastructure` | cloud_native, containerization, ci_cd_automation, iac, serverless | Detect infra needs |
| `compliance` | hipaa_compliance, gdpr_compliance, sox_compliance, pci_dss | Detect compliance |
| `team` | distributed_team, cross_functional, startup, enterprise | Detect team context |

---

## 📜 Protocol Dependencies

**File**: `protocol-dependencies.json`

Defines which protocols depend on which others for proper sequencing.

### Structure

```json
{
  "version": "1.0.0",
  "protocols": {
    "01": {
      "name": "Client Proposal Generation",
      "depends_on": [],
      "optional_deps": []
    },
    "02": {
      "name": "Client Discovery Initiation",
      "depends_on": ["01"],
      "optional_deps": []
    },
    "03": {
      "name": "Project Brief Creation",
      "depends_on": ["02"],
      "optional_deps": ["01"]
    },
    "05b": {
      "name": "Protocol Orchestration",
      "depends_on": ["04"],
      "optional_deps": ["03"]
    }
  },
  "dependency_graph": {
    "generic_track": ["01", "02", "03", "04", "05b", "06", "..."],
    "ai_ml_track": ["01", "02", "03", "04", "05b", "06-ai", "..."]
  }
}
```

### Dependency Rules

- **Strict Dependencies** (`depends_on`): Must complete before this protocol
- **Optional Dependencies** (`optional_deps`): Enhance but not required
- **Parallel Eligible**: Protocols with no dependencies between them

---

## 📜 Validation Thresholds

**File**: `validation-thresholds.yaml`

Defines pass/fail thresholds for the 11 validators.

### Structure

```yaml
version: "1.0.0"

global_threshold: 0.95  # 95% overall score required

validators:
  identity:
    weight: 1.0
    required: true
    pass_threshold: 0.95
    
  ai_role:
    weight: 1.0
    required: true
    pass_threshold: 0.95
    
  workflow:
    weight: 1.2  # Higher weight - critical
    required: true
    pass_threshold: 0.95
    
  quality_gates:
    weight: 1.1
    required: true
    pass_threshold: 0.95
    
  script_integration:
    weight: 0.9
    required: true
    pass_threshold: 0.90
    
  communication:
    weight: 1.0
    required: true
    pass_threshold: 0.95
    
  evidence:
    weight: 1.0
    required: true
    pass_threshold: 0.95
    
  handoff:
    weight: 1.0
    required: true
    pass_threshold: 0.95
    
  reasoning:
    weight: 0.8
    required: false
    pass_threshold: 0.85
    
  reflection:
    weight: 0.8
    required: false
    pass_threshold: 0.85
    
  meta_compliance:
    weight: 1.0
    required: true
    pass_threshold: 0.95

scoring:
  method: weighted_average
  rounding: 2
  grade_boundaries:
    A: 0.95
    B: 0.85
    C: 0.70
    F: 0.00
```

---

## 📜 Orchestration Config

**File**: `orchestration-config.yaml`

Settings for Protocol 05b's orchestration behavior.

### Structure

```yaml
version: "1.0.0"

pre_flight:
  required_files:
    - "project-brief.md"
  optional_files:
    - "context.json"
    - "constraints.yaml"
  timeout_seconds: 30

classification:
  min_dimension_matches: 3
  confidence_threshold: 0.6
  fallback_type: "generic_project"

selection:
  include_optional_protocols: true
  optional_threshold: 0.5
  max_protocols: 30

sequencing:
  enable_parallelization: true
  max_parallel_protocols: 3
  critical_path_analysis: true

customization:
  enable_auto_customization: true
  customization_rules:
    high_compliance:
      triggers: ["hipaa", "gdpr", "sox", "pci"]
      adjustments:
        coverage_threshold: 0.95
        documentation_depth: "comprehensive"
    startup:
      triggers: ["startup", "mvp", "rapid"]
      adjustments:
        documentation_depth: "minimal"
        optional_protocols: false

evidence:
  generate_checksums: true
  checksum_algorithm: "sha256"
  timestamp_format: "ISO8601"
  package_format: "zip"
```

---

## ✅ Configuration Validation

### Validate Config Files

```bash
# Validate classification dimensions
python scripts/utils/validate_config.py \
  --config config/classification-dimensions.yaml \
  --schema config/schemas/classification.schema.json

# Validate all configs
python scripts/utils/validate_all_configs.py
```

### JSON Schema Validation

All config files should have corresponding JSON schemas in `config/schemas/`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Classification Dimensions",
  "type": "object",
  "required": ["version", "dimensions", "classification_rules"],
  "properties": {
    "version": {"type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$"},
    "dimensions": {
      "type": "array",
      "items": {"$ref": "#/definitions/dimension"}
    }
  }
}
```

---

## 🔧 Modifying Configuration

### 1. Adding a Classification Dimension

```yaml
# In classification-dimensions.yaml
dimensions:
  - id: new_dimension_id
    name: "Human Readable Name"
    category: appropriate_category
    description: "What this dimension detects"
    keywords:
      - "keyword1"
      - "keyword2"
    tech_indicators:
      - "tech1"
      - "tech2"
    confidence_weight: 1.0
```

### 2. Adding a Protocol Dependency

```json
// In protocol-dependencies.json
{
  "new_protocol_id": {
    "name": "New Protocol Name",
    "depends_on": ["prerequisite_id"],
    "optional_deps": []
  }
}
```

### 3. Adjusting Validation Thresholds

```yaml
# In validation-thresholds.yaml
validators:
  validator_name:
    weight: 1.0
    required: true
    pass_threshold: 0.95  # Adjust as needed
```

---

## 📚 Related Documentation

- [Protocol 05b](../.cursor/ai-driven-workflow/05b-project-protocol-orchestration-v2.md) - Uses these configs
- [Orchestration Scripts](../scripts/orchestration/README.md) - Scripts that read configs
- [Validator System](../validators-system/README.md) - Uses threshold config

---

**MASTER RAY™ Configuration** - Flexible settings for validated workflows.


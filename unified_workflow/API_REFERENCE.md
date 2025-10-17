# Unified Developer Workflow - API Reference

## Overview

This document provides detailed API reference for all components of the Unified Developer Workflow.

## Core Components

### 1. AI Orchestrator (`ai_orchestrator.py`)

Main orchestrator for the entire workflow.

#### Class: `AIOrchestrator`

```python
class AIOrchestrator:
    def __init__(self, config_file: str = None, project_name: str = None)
    def orchestrate_workflow(self, phases: List[int] = None) -> Dict
    def orchestrate_phase(self, phase: int) -> Dict
    def get_workflow_status(self) -> Dict
    def pause_workflow(self) -> bool
    def resume_workflow(self) -> bool
```

#### Methods

##### `__init__(config_file: str = None, project_name: str = None)`

Initialize the AI orchestrator.

**Parameters**:
- `config_file` (str): Path to configuration file
- `project_name` (str): Name of the project

**Returns**: None

**Example**:
```python
orchestrator = AIOrchestrator("config/production.json", "my-project")
```

##### `orchestrate_workflow(phases: List[int] = None) -> Dict`

Orchestrate the complete workflow.

**Parameters**:
- `phases` (List[int]): List of phases to execute (default: all phases)

**Returns**: Dict with workflow results

**Example**:
```python
result = orchestrator.orchestrate_workflow([0, 1, 2, 3])
```

##### `orchestrate_phase(phase: int) -> Dict`

Orchestrate a single phase.

**Parameters**:
- `phase` (int): Phase number (0-6)

**Returns**: Dict with phase results

**Example**:
```python
result = orchestrator.orchestrate_phase(0)
```

### 2. AI Executor (`ai_executor.py`)

Executes individual phases with AI assistance.

#### Class: `AIExecutor`

```python
class AIExecutor:
    def __init__(self, config: Dict, evidence_manager: EvidenceManager)
    def execute_phase(self, phase: int, context: Dict = None) -> Dict
    def execute_full_workflow(self, phases: List[int] = None) -> Dict
    def get_phase_outputs(self, phase: int) -> List[str]
    def generate_final_report(self) -> str
```

#### Methods

##### `execute_phase(phase: int, context: Dict = None) -> Dict`

Execute a single phase.

**Parameters**:
- `phase` (int): Phase number (0-6)
- `context` (Dict): Additional context for execution

**Returns**: Dict with execution results

**Example**:
```python
result = executor.execute_phase(0, {"project_type": "web_app"})
```

##### `execute_full_workflow(phases: List[int] = None) -> Dict`

Execute the complete workflow.

**Parameters**:
- `phases` (List[int]): List of phases to execute

**Returns**: Dict with workflow results

**Example**:
```python
result = executor.execute_full_workflow([0, 1, 2, 3, 4, 5, 6])
```

### 3. Evidence Manager (`evidence_manager.py`)

Manages evidence collection and validation.

#### Class: `EvidenceManager`

```python
class EvidenceManager:
    def __init__(self, evidence_dir: str, project_name: str)
    def log_artifact(self, phase: int, artifact_type: str, path: str, metadata: Dict = None) -> bool
    def log_execution(self, phase: int, execution_data: Dict) -> bool
    def log_validation(self, phase: int, validation_data: Dict) -> bool
    def validate_evidence(self, phase: int = None) -> Dict
    def generate_report(self, phase: int = None) -> str
```

#### Methods

##### `log_artifact(phase: int, artifact_type: str, path: str, metadata: Dict = None) -> bool`

Log an artifact for a phase.

**Parameters**:
- `phase` (int): Phase number
- `artifact_type` (str): Type of artifact
- `path` (str): Path to artifact file
- `metadata` (Dict): Additional metadata

**Returns**: bool indicating success

**Example**:
```python
success = evidence_manager.log_artifact(0, "documentation", "README.md", {"size": 1024})
```

##### `log_execution(phase: int, execution_data: Dict) -> bool`

Log execution data for a phase.

**Parameters**:
- `phase` (int): Phase number
- `execution_data` (Dict): Execution data

**Returns**: bool indicating success

**Example**:
```python
success = evidence_manager.log_execution(0, {
    "start_time": "2024-01-01T10:00:00Z",
    "end_time": "2024-01-01T10:15:00Z",
    "status": "completed"
})
```

##### `validate_evidence(phase: int = None) -> Dict`

Validate evidence for a phase or all phases.

**Parameters**:
- `phase` (int): Phase number (None for all phases)

**Returns**: Dict with validation results

**Example**:
```python
validation = evidence_manager.validate_evidence(0)
```

### 4. Quality Gates (`quality_gates.py`)

Manages quality assessment and auditing.

#### Class: `QualityGates`

```python
class QualityGates:
    def __init__(self, config: Dict, evidence_manager: EvidenceManager)
    def execute_quality_gate(self, gate_type: str, context: Dict = None) -> Dict
    def execute_comprehensive_audit(self, context: Dict = None) -> Dict
    def generate_findings(self, audit_results: Dict) -> List[Dict]
    def calculate_score(self, findings: List[Dict]) -> float
    def generate_recommendations(self, findings: List[Dict]) -> List[str]
```

#### Methods

##### `execute_quality_gate(gate_type: str, context: Dict = None) -> Dict`

Execute a specific quality gate.

**Parameters**:
- `gate_type` (str): Type of quality gate
- `context` (Dict): Additional context

**Returns**: Dict with quality gate results

**Example**:
```python
result = quality_gates.execute_quality_gate("SECURITY", {"project_type": "web_app"})
```

##### `execute_comprehensive_audit(context: Dict = None) -> Dict`

Execute a comprehensive quality audit.

**Parameters**:
- `context` (Dict): Additional context

**Returns**: Dict with audit results

**Example**:
```python
audit = quality_gates.execute_comprehensive_audit({"project_type": "web_app"})
```

### 5. Validation Gates (`validation_gates.py`)

Manages human validation checkpoints.

#### Class: `ValidationGates`

```python
class ValidationGates:
    def __init__(self, config: Dict, evidence_manager: EvidenceManager)
    def get_validation_checkpoint(self, phase: int) -> Dict
    def create_validation_request(self, phase: int, context: Dict = None) -> str
    def approve_validation(self, request_id: str, approver: str, comments: str = None) -> bool
    def reject_validation(self, request_id: str, approver: str, reason: str) -> bool
    def get_validation_status(self, request_id: str) -> Dict
    def list_pending_validations(self) -> List[Dict]
```

#### Methods

##### `create_validation_request(phase: int, context: Dict = None) -> str`

Create a validation request for a phase.

**Parameters**:
- `phase` (int): Phase number
- `context` (Dict): Additional context

**Returns**: str with request ID

**Example**:
```python
request_id = validation_gates.create_validation_request(0, {"project_type": "web_app"})
```

##### `approve_validation(request_id: str, approver: str, comments: str = None) -> bool`

Approve a validation request.

**Parameters**:
- `request_id` (str): Request ID
- `approver` (str): Approver name
- `comments` (str): Optional comments

**Returns**: bool indicating success

**Example**:
```python
success = validation_gates.approve_validation("req_123", "tech_lead", "Looks good")
```

## Configuration

### Configuration File Format

```json
{
  "project": {
    "name": "string",
    "description": "string",
    "version": "string",
    "type": "string"
  },
  "ai": {
    "provider": "string",
    "model": "string",
    "api_key": "string",
    "temperature": "number",
    "max_tokens": "number"
  },
  "quality": {
    "min_score": "number",
    "comprehensive_audit": "boolean",
    "automated_tests": "boolean",
    "security_check": "boolean"
  },
  "validation": {
    "required_approvals": ["string"],
    "timeout_hours": "number",
    "auto_approve": "boolean"
  },
  "evidence": {
    "retention_days": "number",
    "backup_enabled": "boolean",
    "checksum_validation": "boolean"
  }
}
```

### Environment Variables

- `AI_API_KEY`: AI provider API key
- `PROJECT_ROOT`: Root directory of the project
- `EVIDENCE_DIR`: Directory for evidence storage
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `CONFIG_FILE`: Path to configuration file

## Data Models

### Phase Result

```python
{
    "phase": int,
    "status": str,  # "completed", "failed", "skipped"
    "duration": float,
    "quality_score": float,
    "findings": List[Dict],
    "artifacts": List[str],
    "validation_status": str,
    "ai_role": str,
    "timestamp": str
}
```

### Quality Gate Result

```python
{
    "gate_type": str,
    "score": float,
    "status": str,  # "passed", "failed", "warning"
    "findings": List[Dict],
    "recommendations": List[str],
    "duration": float,
    "timestamp": str
}
```

### Validation Request

```python
{
    "request_id": str,
    "phase": int,
    "checkpoint": str,
    "required_approvals": List[str],
    "approvals": List[Dict],
    "status": str,  # "pending", "approved", "rejected"
    "created_at": str,
    "updated_at": str
}
```

### Evidence Manifest

```python
{
    "project_name": str,
    "phase": int,
    "phase_name": str,
    "start_time": str,
    "end_time": str,
    "duration": float,
    "status": str,
    "artifacts": List[Dict],
    "executions": List[Dict],
    "validations": List[Dict],
    "checksum": str
}
```

## Error Handling

### Exception Types

- `ConfigurationError`: Configuration file issues
- `AIExecutionError`: AI execution failures
- `QualityGateError`: Quality gate failures
- `ValidationError`: Validation failures
- `EvidenceError`: Evidence management errors

### Error Response Format

```python
{
    "error": str,
    "error_type": str,
    "phase": int,
    "timestamp": str,
    "details": Dict,
    "suggestions": List[str]
}
```

## CLI Interface

### Command Line Options

```bash
python3 automation/ai_orchestrator.py [OPTIONS]

Options:
  --project-name TEXT     Project name
  --config TEXT          Configuration file path
  --phases TEXT          Comma-separated list of phases
  --quality-threshold FLOAT  Minimum quality score
  --enable-validation     Enable validation gates
  --approvers TEXT       Comma-separated list of approvers
  --verbose              Verbose output
  --debug                Debug mode
  --help                 Show help message
```

### Examples

```bash
# Run complete workflow
python3 automation/ai_orchestrator.py --project-name "my-project"

# Run specific phases
python3 automation/ai_orchestrator.py --project-name "my-project" --phases "0,1,2"

# With custom configuration
python3 automation/ai_orchestrator.py --config "config/custom.json" --project-name "my-project"

# With validation gates
python3 automation/ai_orchestrator.py --project-name "my-project" --enable-validation --approvers "tech_lead,product_owner"
```

## Integration Examples

### Python Integration

```python
from automation.ai_orchestrator import AIOrchestrator
from automation.evidence_manager import EvidenceManager
from automation.quality_gates import QualityGates

# Initialize components
orchestrator = AIOrchestrator("config/production.json", "my-project")
evidence_manager = EvidenceManager("evidence", "my-project")
quality_gates = QualityGates(config, evidence_manager)

# Execute workflow
result = orchestrator.orchestrate_workflow([0, 1, 2, 3])

# Check results
if result["status"] == "success":
    print("Workflow completed successfully")
else:
    print("Workflow failed:", result["error"])
```

### CI/CD Integration

```yaml
# GitHub Actions example
name: Unified Workflow CI
on: [push, pull_request]

jobs:
  unified-workflow:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r unified-workflow/requirements.txt
      - name: Run Quality Audit
        run: |
          cd unified-workflow
          python3 automation/quality_gates.py --mode comprehensive
        env:
          AI_API_KEY: ${{ secrets.AI_API_KEY }}
```

## Performance Considerations

### Resource Requirements

- **CPU**: 2+ cores recommended
- **Memory**: 4GB+ RAM recommended
- **Storage**: 1GB+ for evidence and logs
- **Network**: Stable internet for AI API calls

### Optimization Tips

1. **Parallel Execution**: Run independent phases in parallel
2. **Caching**: Enable AI response caching
3. **Resource Limits**: Set appropriate timeouts
4. **Cleanup**: Regularly clean temporary files

## Security Considerations

### API Key Security

- Store API keys in environment variables
- Use secure key management systems
- Rotate keys regularly
- Monitor API usage

### Data Protection

- Encrypt sensitive data
- Use secure file permissions
- Implement access controls
- Regular security audits

## Monitoring and Logging

### Log Levels

- **DEBUG**: Detailed debugging information
- **INFO**: General information about workflow execution
- **WARNING**: Warning messages for potential issues
- **ERROR**: Error messages for failures

### Log Files

- `logs/workflow.log`: Main workflow execution log
- `logs/quality.log`: Quality gate execution log
- `logs/validation.log`: Validation gate log
- `logs/ai.log`: AI execution log

### Monitoring Metrics

- Workflow execution time
- Quality scores
- Validation approval rates
- Error rates
- Resource usage

## Version Compatibility

### Python Version Support

- Python 3.8+
- Python 3.9+ (recommended)
- Python 3.10+ (optimal)

### Dependency Versions

- See `requirements.txt` for specific versions
- Regular updates recommended
- Test compatibility before upgrading

## Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Install development dependencies
4. Make your changes
5. Add tests
6. Submit a pull request

### Code Style

- Follow PEP 8
- Use type hints
- Add docstrings
- Write tests
- Update documentation

## License

This project is licensed under the MIT License. See the LICENSE file for details.

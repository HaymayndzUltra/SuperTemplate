# Unified Developer Workflow

An AI-orchestrated development lifecycle that integrates planning, implementation, quality assurance, and operations into a seamless, automated process.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run complete workflow
python3 automation/ai_orchestrator.py --project-name "my-project"

# Run specific phases
python3 automation/ai_orchestrator.py --project-name "my-project" --phases "0,1,2,3"
```

## 📋 Overview

The Unified Developer Workflow provides:

- **AI-Driven Execution**: Automated phase execution with AI assistance
- **Quality Assurance**: Comprehensive quality gates and audits
- **Evidence Tracking**: Complete audit trail and traceability
- **Human Validation**: Strategic approval points for critical decisions
- **Flexible Configuration**: Adaptable to different project types

## 🏗️ Architecture

### Core Components

1. **AI Orchestrator**: Main workflow controller
2. **AI Executor**: Phase execution engine
3. **Evidence Manager**: Evidence collection and validation
4. **Quality Gates**: Quality assessment and auditing
5. **Validation Gates**: Human validation checkpoints

### Workflow Phases

- **Phase 0**: Bootstrap & Context Engineering
- **Phase 1**: PRD Creation
- **Phase 2**: Task Generation
- **Phase 3**: Implementation
- **Phase 4**: Quality Audit
- **Phase 5**: Retrospective
- **Phase 6**: Operations

## 📁 Directory Structure

```
unified-workflow/
├── automation/           # Core automation scripts
│   ├── ai_orchestrator.py
│   ├── ai_executor.py
│   ├── evidence_manager.py
│   ├── quality_gates.py
│   └── validation_gates.py
├── phases/               # Phase protocol definitions
│   ├── 0-bootstrap.md
│   ├── 1-prd-creation.md
│   ├── 2-task-generation.md
│   ├── 3-implementation.md
│   ├── 4-quality-audit.md
│   ├── 5-retrospective.md
│   └── 6-operations.md
├── evidence/             # Evidence templates and schemas
│   ├── schema.json
│   ├── manifest-template.json
│   ├── run-log-template.json
│   └── validation-template.md
├── config/               # Configuration files
│   └── template.json
├── tests/                # Test suite
│   ├── test_*.py
│   └── run_tests.py
├── scripts/              # Utility scripts
├── templates/            # Project templates
├── docs/                 # Documentation
│   ├── USER_GUIDE.md
│   ├── API_REFERENCE.md
│   └── DEPLOYMENT.md
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## ⚙️ Configuration

### Basic Configuration

Create a configuration file:

```json
{
  "project": {
    "name": "my-project",
    "description": "Project description",
    "version": "1.0.0"
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-sonnet",
    "api_key": "your-api-key"
  },
  "quality": {
    "min_score": 7.0,
    "comprehensive_audit": true
  },
  "validation": {
    "required_approvals": ["technical_lead", "product_owner"],
    "timeout_hours": 24
  }
}
```

### Environment Variables

```bash
export AI_API_KEY="your-api-key-here"
export PROJECT_ROOT="/path/to/your/project"
export EVIDENCE_DIR="/path/to/evidence/storage"
export LOG_LEVEL="INFO"
```

## 🔧 Usage

### Command Line Interface

```bash
# Complete workflow
python3 automation/ai_orchestrator.py --project-name "my-project"

# Specific phases
python3 automation/ai_orchestrator.py --project-name "my-project" --phases "0,1,2"

# With validation gates
python3 automation/ai_orchestrator.py --project-name "my-project" --enable-validation

# Custom configuration
python3 automation/ai_orchestrator.py --config "config/custom.json" --project-name "my-project"
```

### Python API

```python
from automation.ai_orchestrator import AIOrchestrator

# Initialize orchestrator
orchestrator = AIOrchestrator("config/production.json", "my-project")

# Execute workflow
result = orchestrator.orchestrate_workflow([0, 1, 2, 3, 4, 5, 6])

# Check results
if result["status"] == "success":
    print("Workflow completed successfully")
else:
    print("Workflow failed:", result["error"])
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python3 tests/run_tests.py

# Run specific test file
python3 -m pytest tests/test_evidence_manager.py

# Run with coverage
python3 -m pytest tests/ --cov=automation
```

## 📊 Quality Gates

### Quality Gate Types

- **QUICK**: Basic code review and syntax check
- **SECURITY**: Security vulnerability assessment
- **ARCHITECTURE**: Architecture compliance review
- **DESIGN**: Design system compliance
- **UI**: User interface and accessibility check
- **DEEP-SECURITY**: Comprehensive security audit

### Quality Scoring

- **Score Range**: 0-10
- **Passing Score**: 7.0 (configurable)
- **Weighted Average**: Used for overall assessment

## 🔍 Evidence System

### Evidence Types

1. **Manifest**: Project metadata and phase information
2. **Run Log**: Execution history and timing
3. **Validation**: Quality and validation results
4. **Artifacts**: Generated files and outputs

### Evidence Structure

```
evidence/
├── phase0/
│   ├── manifest.json
│   ├── run.log
│   ├── validation.md
│   └── artifacts/
├── phase1/
│   ├── manifest.json
│   ├── run.log
│   ├── validation.md
│   └── artifacts/
└── ...
```

## 🤖 AI Integration

### Supported AI Providers

- **Claude**: Anthropic Claude models
- **GPT-4**: OpenAI GPT-4 models
- **Custom**: OpenAI-compatible APIs

### AI Roles

Each phase has a specific AI role:

- **System Architect**: Bootstrap and context
- **Product Manager**: Requirements and planning
- **Technical Lead**: Task generation and architecture
- **Developer**: Implementation and coding
- **Quality Engineer**: Quality assurance and testing
- **Process Owner**: Retrospective and improvement
- **Operations Lead**: Deployment and operations

## 🔐 Security

### Security Considerations

1. **API Keys**: Store in environment variables
2. **File Permissions**: Restrict access to sensitive files
3. **Network**: Use HTTPS for all API communications
4. **Logs**: Rotate logs regularly and avoid logging sensitive data

### Security Features

- **Input Validation**: All inputs are validated
- **Output Sanitization**: Outputs are sanitized
- **Access Control**: Role-based access control
- **Audit Trail**: Complete audit trail for all actions

## 📈 Performance

### Resource Requirements

- **Minimum**: 2GB RAM, 1 CPU core
- **Recommended**: 4GB RAM, 2 CPU cores
- **Optimal**: 8GB RAM, 4 CPU cores

### Optimization Tips

1. **Parallel Execution**: Run phases in parallel where possible
2. **Caching**: Enable AI response caching
3. **Resource Limits**: Set appropriate timeouts
4. **Cleanup**: Regularly clean temporary files

## 🚀 Deployment

### Production Deployment

1. **Setup Environment**: Install dependencies and configure
2. **Configure AI**: Set up AI provider and API keys
3. **Setup Monitoring**: Configure logging and monitoring
4. **Test Workflow**: Run test workflow to verify setup
5. **Deploy**: Deploy to production environment

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

## 📚 Documentation

- **[User Guide](USER_GUIDE.md)**: Comprehensive user guide
- **[API Reference](API_REFERENCE.md)**: Detailed API documentation
- **[Deployment Guide](DEPLOYMENT.md)**: Deployment instructions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🆘 Support

For support and questions:

1. Check the documentation
2. Review logs and error messages
3. Consult the troubleshooting guide
4. Contact the development team

## 🔄 Version History

- **v1.0.0**: Initial release
- **v1.1.0**: Added validation gates
- **v1.2.0**: Enhanced quality gates
- **v1.3.0**: AI orchestration improvements

## 🎯 Roadmap

- **v1.4.0**: Enhanced AI capabilities
- **v1.5.0**: Advanced quality gates
- **v2.0.0**: Multi-project support
- **v2.1.0**: Advanced analytics and reporting
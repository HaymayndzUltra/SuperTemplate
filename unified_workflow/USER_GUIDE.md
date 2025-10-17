# Unified Developer Workflow - User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Workflow Phases](#workflow-phases)
4. [Quality Gates](#quality-gates)
5. [Validation Gates](#validation-gates)
6. [Evidence System](#evidence-system)
7. [AI Automation](#ai-automation)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)
10. [FAQ](#faq)

## Introduction

The Unified Developer Workflow is an AI-orchestrated development lifecycle that integrates planning, implementation, quality assurance, and operations into a seamless, automated process.

### Key Features

- **AI-Driven Execution**: Automated phase execution with AI assistance
- **Quality Assurance**: Comprehensive quality gates and audits
- **Evidence Tracking**: Complete audit trail and traceability
- **Human Validation**: Strategic approval points for critical decisions
- **Flexible Configuration**: Adaptable to different project types and requirements

## Getting Started

### Prerequisites

- Python 3.8+
- AI Assistant access (Claude, GPT-4, etc.)
- Git repository
- Basic understanding of software development lifecycle

### Quick Start

1. **Setup Environment**
   ```bash
   cd unified-workflow
   pip install -r requirements.txt
   ```

2. **Configure Project**
   ```bash
   cp config/template.json config/my-project.json
   # Edit configuration file
   ```

3. **Run Workflow**
   ```bash
   python3 automation/ai_orchestrator.py --project-name "my-project"
   ```

## Workflow Phases

### Phase 0: Bootstrap & Context Engineering

**Purpose**: Initialize project context and governance

**Key Activities**:
- Project structure setup
- Governance rules loading
- Context engineering
- Initial documentation

**Duration**: 5-15 minutes
**AI Role**: System Architect

**Outputs**:
- Project configuration
- Governance rules loaded
- Initial documentation
- Context established
 
**Automation Hook**:
- Auto-run `/Generate Cursor Rules` to scaffold baseline `project-rules` if `PROJECT-BRIEF.md` exists or minimal signals are present (README + manifests). Use `--dry-run` if brief is missing.

### Phase 1: PRD Creation

**Purpose**: Define product requirements and specifications

**Key Activities**:
- Requirements gathering
- Stakeholder analysis
- Feature specification
- Acceptance criteria definition

**Duration**: 30-60 minutes
**AI Role**: Product Manager

**Outputs**:
- Product Requirements Document
- User stories
- Acceptance criteria
- Stakeholder map

### Phase 2: Task Generation

**Purpose**: Break down requirements into actionable tasks

**Key Activities**:
- Task decomposition
- Dependency mapping
- Effort estimation
- Resource allocation

**Duration**: 15-30 minutes
**AI Role**: Technical Lead

**Outputs**:
- Task breakdown
- Dependency graph
- Effort estimates
- Resource plan
 
**Automation Hook**:
- After task graph/artifacts are produced (e.g., `.cursor/commands/generated/**`), re-run `/Generate Cursor Rules` (idempotent). Only run if tasks/architecture changed since the last run; otherwise skip.

### Phase 3: Implementation

**Purpose**: Execute development tasks

**Key Activities**:
- Code implementation
- Testing
- Documentation
- Integration

**Duration**: Variable (depends on scope)
**AI Role**: Developer

**Outputs**:
- Source code
- Tests
- Documentation
- Integration artifacts

### Phase 4: Quality Audit

**Purpose**: Comprehensive quality assessment

**Key Activities**:
- Code review
- Security audit
- Performance testing
- Accessibility check

**Duration**: 20-40 minutes
**AI Role**: Quality Engineer

**Outputs**:
- Quality report
- Findings list
- Recommendations
- Score assessment

### Phase 5: Retrospective

**Purpose**: Process improvement and learning

**Key Activities**:
- Process analysis
- Lessons learned
- Improvement recommendations
- Knowledge capture

**Duration**: 15-30 minutes
**AI Role**: Process Owner

**Outputs**:
- Retrospective report
- Process improvements
- Lessons learned
- Action items
 
**Automation Hook**:
- Re-run `/Generate Cursor Rules` to fold lessons learned and quality findings into rules. Append deltas; avoid overwrite unless explicitly requested.

### Phase 6: Operations

**Purpose**: Production readiness and operations

**Key Activities**:
- Deployment preparation
- Monitoring setup
- Documentation finalization
- Handover preparation

**Duration**: 20-40 minutes
**AI Role**: Operations Lead

**Outputs**:
- Deployment plan
- Monitoring configuration
- Operations documentation
- Handover package

## Quality Gates

### Quality Gate Types

1. **QUICK**: Basic code review and syntax check
2. **SECURITY**: Security vulnerability assessment
3. **ARCHITECTURE**: Architecture compliance review
4. **DESIGN**: Design system compliance
5. **UI**: User interface and accessibility check
6. **DEEP-SECURITY**: Comprehensive security audit

### Quality Scoring

- **Score Range**: 0-10
- **Passing Score**: 7.0 (configurable)
- **Weighted Average**: Used for overall assessment

### Quality Findings

- **CRITICAL**: Immediate action required
- **HIGH**: Address before release
- **MEDIUM**: Address in next iteration
- **LOW**: Consider for future improvement

## Validation Gates

### Validation Checkpoints

Each phase has strategic validation checkpoints:

- **Phase 0**: Bootstrap completion approval
- **Phase 1**: PRD approval
- **Phase 2**: Task generation confirmation
- **Phase 3**: Implementation review
- **Phase 4**: Quality audit results review
- **Phase 5**: Retrospective validation
- **Phase 6**: Operations readiness

### Approval Process

1. **Request Creation**: AI creates validation request
2. **Approver Notification**: Relevant stakeholders notified
3. **Review Process**: Approvers review and provide feedback
4. **Decision**: Approve, reject, or request changes
5. **Progression**: Workflow continues based on decision

## Evidence System

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

### Evidence Validation

- **Checksum Verification**: File integrity validation
- **Completeness Check**: Required artifacts present
- **Consistency Validation**: Cross-phase consistency
- **Quality Assurance**: Evidence quality assessment

## AI Automation

### AI Roles

Each phase has a specific AI role:

- **System Architect**: Bootstrap and context
- **Product Manager**: Requirements and planning
- **Technical Lead**: Task generation and architecture
- **Developer**: Implementation and coding
- **Quality Engineer**: Quality assurance and testing
- **Process Owner**: Retrospective and improvement
- **Operations Lead**: Deployment and operations

### AI Capabilities

- **Context Understanding**: Project-specific knowledge
- **Decision Making**: Automated decision support
- **Quality Assessment**: Objective quality evaluation
- **Process Optimization**: Continuous improvement
- **Documentation**: Automated documentation generation

### Human-AI Collaboration

- **AI Execution**: Automated phase execution
- **Human Validation**: Strategic approval points
- **Collaborative Review**: Joint quality assessment
- **Knowledge Transfer**: AI learning from human feedback

## Best Practices

### Project Setup

1. **Clear Brief**: Provide comprehensive project brief
2. **Stakeholder Identification**: Include all relevant stakeholders
3. **Resource Planning**: Allocate sufficient time and resources
4. **Quality Standards**: Define quality expectations upfront

### Workflow Execution

1. **Sequential Phases**: Complete phases in order
2. **Quality Gates**: Don't skip quality assessments
3. **Evidence Collection**: Maintain complete evidence trail
4. **Validation Points**: Use human validation strategically

### Quality Assurance

1. **Comprehensive Audits**: Run full quality audits
2. **Security Focus**: Prioritize security assessments
3. **Performance Testing**: Include performance validation
4. **Accessibility**: Ensure accessibility compliance

### Continuous Improvement

1. **Retrospectives**: Conduct regular retrospectives
2. **Process Refinement**: Continuously improve processes
3. **Knowledge Sharing**: Share lessons learned
4. **Tool Updates**: Keep tools and dependencies current

## Troubleshooting

### Common Issues

#### AI API Issues
```bash
# Check API key
echo $AI_API_KEY

# Test API connection
python3 -c "import openai; print('API OK')"
```

#### Permission Issues
```bash
# Fix file permissions
chmod +x automation/*.py
chown -R $USER:$USER .
```

#### Dependency Issues
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### Configuration Issues
```bash
# Validate configuration
python3 -c "import json; json.load(open('config/production.json'))"
```

### Debug Mode

Enable debug mode for detailed logging:

```bash
export LOG_LEVEL=DEBUG
python3 automation/ai_orchestrator.py --debug --verbose
```

### Log Analysis

Check logs for issues:

```bash
# View recent logs
tail -f logs/workflow.log

# Search for errors
grep -i error logs/*.log

# Check specific phase
grep "Phase 3" logs/workflow.log
```

## FAQ

### Q: How long does a complete workflow take?

A: Typical duration:
- **Small Project**: 2-4 hours
- **Medium Project**: 4-8 hours
- **Large Project**: 8-16 hours

### Q: Can I skip phases?

A: Not recommended. Each phase builds on the previous one. Skipping phases can lead to quality issues and incomplete evidence.

### Q: What if quality gates fail?

A: Address the issues identified in the quality report before proceeding. The workflow will not continue until quality standards are met.

### Q: How do I customize the workflow?

A: Modify the configuration file and phase protocols to match your specific requirements.

### Q: Can I run phases in parallel?

A: Some phases can run in parallel, but the core workflow is designed to be sequential for optimal quality and traceability.

### Q: What AI models are supported?

A: The workflow supports Claude, GPT-4, and other OpenAI-compatible models. Check the configuration file for specific model settings.

### Q: How do I add custom quality gates?

A: Create new quality gate definitions in the `quality_gates.py` file and update the configuration.

### Q: Can I integrate with existing CI/CD?

A: Yes, the workflow can be integrated with GitHub Actions, GitLab CI, Jenkins, and other CI/CD systems.

### Q: What happens if validation is rejected?

A: The workflow pauses until issues are addressed and validation is approved. You can modify the project and re-submit for validation.

### Q: How do I backup evidence?

A: Use the backup scripts provided:
```bash
./scripts/backup-evidence.sh
```

## Support

For additional support:

1. Check the documentation
2. Review logs and error messages
3. Consult the troubleshooting guide
4. Contact the development team

## Contributing

To contribute to the Unified Developer Workflow:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

# Unified Developer Workflow - Deployment Guide

## Overview

This guide provides step-by-step instructions for deploying the Unified Developer Workflow to your development environment.

## Prerequisites

- Python 3.8 or higher
- Git
- Access to your development repository
- AI Assistant (Claude, GPT-4, etc.)

## Installation Steps

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd secretflow

# Navigate to unified workflow
cd unified-workflow

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a configuration file for your environment:

```bash
# Copy the template
cp config/template.json config/production.json

# Edit with your settings
nano config/production.json
```

Example configuration:

```json
{
  "project": {
    "name": "your-project-name",
    "description": "Your project description",
    "version": "1.0.0"
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-sonnet",
    "api_key": "your-api-key"
  },
  "quality": {
    "min_score": 7.0,
    "comprehensive_audit": true,
    "automated_tests": true
  },
  "validation": {
    "required_approvals": ["technical_lead", "product_owner"],
    "timeout_hours": 24
  }
}
```

### 3. Environment Variables

Set up environment variables:

```bash
# Create .env file
cat > .env << EOF
AI_API_KEY=your-api-key-here
PROJECT_ROOT=/path/to/your/project
EVIDENCE_DIR=/path/to/evidence/storage
LOG_LEVEL=INFO
EOF
```

### 4. Directory Structure Setup

```bash
# Create necessary directories
mkdir -p evidence/{phase0,phase1,phase2,phase3,phase4,phase5,phase6}
mkdir -p projects
mkdir -p logs
mkdir -p templates
```

### 5. Permissions

```bash
# Make scripts executable
chmod +x automation/*.py
chmod +x scripts/*.sh

# Set proper ownership
chown -R $USER:$USER .
```

## Usage

### Quick Start

```bash
# Run a complete workflow
python3 automation/ai_orchestrator.py --project-name "my-project" --brief-file "brief.md"

# Run a single phase
python3 automation/ai_executor.py --phase 0 --project-name "my-project"

# Execute quality audit
python3 automation/quality_gates.py --mode comprehensive --project-name "my-project"
```

### Advanced Usage

```bash
# Custom configuration
python3 automation/ai_orchestrator.py \
  --config config/production.json \
  --project-name "my-project" \
  --phases 0,1,2,3 \
  --quality-threshold 8.0

# With validation gates
python3 automation/ai_orchestrator.py \
  --project-name "my-project" \
  --enable-validation \
  --approvers "tech-lead,product-owner"
```

## Integration with Existing Workflows

### CI/CD Integration

Add to your `.github/workflows/ci.yml`:

```yaml
name: Unified Developer Workflow CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

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
        run: |
          cd unified-workflow
          pip install -r requirements.txt
          
      - name: Run Quality Audit
        run: |
          cd unified-workflow
          python3 automation/quality_gates.py --mode comprehensive
        env:
          AI_API_KEY: ${{ secrets.AI_API_KEY }}
```

### IDE Integration

For VS Code, add to `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Unified Workflow",
      "type": "shell",
      "command": "python3",
      "args": ["automation/ai_orchestrator.py", "--project-name", "${input:projectName}"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ],
  "inputs": [
    {
      "id": "projectName",
      "description": "Project name",
      "default": "my-project",
      "type": "promptString"
    }
  ]
}
```

## Monitoring and Logging

### Log Files

- `logs/workflow.log` - Main workflow execution log
- `logs/quality.log` - Quality gate execution log
- `logs/validation.log` - Validation gate log
- `logs/ai.log` - AI execution log

### Monitoring Dashboard

```bash
# Start monitoring
python3 scripts/monitor.py --port 8080

# Access dashboard at http://localhost:8080
```

## Troubleshooting

### Common Issues

1. **AI API Key Issues**
   ```bash
   # Check API key
   python3 -c "import os; print('API Key:', os.getenv('AI_API_KEY', 'Not set'))"
   ```

2. **Permission Issues**
   ```bash
   # Fix permissions
   chmod +x automation/*.py
   chown -R $USER:$USER .
   ```

3. **Python Dependencies**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

### Debug Mode

```bash
# Enable debug logging
export LOG_LEVEL=DEBUG

# Run with verbose output
python3 automation/ai_orchestrator.py --verbose --debug
```

## Security Considerations

1. **API Keys**: Store in environment variables, never in code
2. **File Permissions**: Restrict access to sensitive configuration files
3. **Network**: Use HTTPS for all API communications
4. **Logs**: Rotate logs regularly and avoid logging sensitive data

## Backup and Recovery

### Backup Evidence

```bash
# Backup evidence directory
tar -czf evidence-backup-$(date +%Y%m%d).tar.gz evidence/

# Backup configuration
cp config/production.json config/backup-$(date +%Y%m%d).json
```

### Recovery

```bash
# Restore evidence
tar -xzf evidence-backup-YYYYMMDD.tar.gz

# Restore configuration
cp config/backup-YYYYMMDD.json config/production.json
```

## Performance Optimization

### Resource Requirements

- **Minimum**: 2GB RAM, 1 CPU core
- **Recommended**: 4GB RAM, 2 CPU cores
- **Optimal**: 8GB RAM, 4 CPU cores

### Optimization Tips

1. **Parallel Execution**: Run phases in parallel where possible
2. **Caching**: Enable AI response caching
3. **Resource Limits**: Set appropriate timeouts
4. **Cleanup**: Regularly clean temporary files

## Support and Maintenance

### Regular Maintenance

```bash
# Weekly maintenance script
./scripts/maintenance.sh

# Update dependencies
pip install -r requirements.txt --upgrade

# Clean logs
./scripts/cleanup-logs.sh
```

### Getting Help

1. Check logs for error messages
2. Review configuration settings
3. Consult documentation
4. Contact support team

## Version History

- **v1.0.0**: Initial release
- **v1.1.0**: Added validation gates
- **v1.2.0**: Enhanced quality gates
- **v1.3.0**: AI orchestration improvements

## License

This Unified Developer Workflow is licensed under the MIT License. See LICENSE file for details.

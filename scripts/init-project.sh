#!/bin/bash
# Initialize new project from template

echo "🚀 Initializing new project from ai-driven-workflow template..."

# Remove template git history
if [ -d ".git" ]; then
    echo "Removing template git history..."
    rm -rf .git
fi

# Initialize new git repo
echo "Initializing new git repository..."
git init

# Make scripts executable
echo "Setting script permissions..."
chmod +x scripts/*.py
chmod +x scripts/*.sh

# Create project directories
echo "Creating project directories..."
mkdir -p src tests docs

# Run validation
echo "Running validation checks..."
python3 scripts/validate_workflow_integration.py

echo "✅ Project initialized successfully!"
echo ""
echo "Next steps:"
echo "1. Run Protocol 00 (Client Discovery) with your job post"
echo "2. Run Protocol 0 (Bootstrap) to analyze your codebase"
echo "3. Follow the ai-driven-workflow protocols in sequence"
echo ""
echo "Quick validation commands:"
echo "  python3 scripts/validate_protocol_steps.py"
echo "  python3 scripts/validate_ai_directives.py"
echo "  bash scripts/test_workflow_integration.sh"

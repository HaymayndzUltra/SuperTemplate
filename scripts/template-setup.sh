#!/bin/bash
# Template Setup Script
# Initializes a new project from this template

set -e

echo "🚀 Setting up new project from template..."

# Create .artifacts directory structure
mkdir -p .artifacts/{protocol-01,protocol-02,protocol-03,protocol-04,protocol-05}

# Create example .env file
if [ ! -f .env ]; then
    cp .env.example .env 2>/dev/null || echo "# Add your environment variables here" > .env
fi

# Install dependencies
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Make scripts executable
chmod +x scripts/*.sh 2>/dev/null || true
chmod +x scripts/*.py 2>/dev/null || true

echo "✅ Template setup complete!"
echo "📝 Next steps:"
echo "   1. Update .env with your configuration"
echo "   2. Review README.md for usage instructions"
echo "   3. Run: python scripts/generate_from_brief.py --help"

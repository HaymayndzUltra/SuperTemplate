#!/bin/bash
# Template Cleanup Script
# Removes project-specific artifacts to prepare repository as a template

set -e

echo "🧹 Starting template cleanup..."

# Backup check
read -p "⚠️  Have you created a backup branch? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Please create a backup branch first:"
    echo "   git checkout -b backup-before-template-cleanup"
    echo "   git push origin backup-before-template-cleanup"
    exit 1
fi

# Remove project-specific artifacts
echo "📦 Removing project-specific artifacts..."
rm -rf .artifacts/protocol-*/
rm -rf .artifacts/analysis-*/
rm -rf .artifacts/meta-upgrades/
rm -rf .artifacts/validation/
rm -rf .artifacts/gate-results/
rm -rf .artifacts/performance/
rm -rf .artifacts/protocol-generation/
rm -rf .artifacts/protocol-verification/
rm -rf .artifacts/causal-ledger/
rm -rf .artifacts/reasoning-dna/
rm -rf .artifacts/phase-*/
rm -rf .artifacts/plano-validation/
rm -rf .artifacts/protocol-creation/
rm -rf .artifacts/scripts/

# Keep .artifacts directory structure but remove content
mkdir -p .artifacts
echo "# Artifacts Directory" > .artifacts/README.md
echo "" >> .artifacts/README.md
echo "This directory will contain project-specific artifacts generated during protocol execution." >> .artifacts/README.md
echo "Artifacts are created automatically and should not be committed to version control." >> .artifacts/README.md

# Remove project-specific documentation
echo "📄 Removing project-specific documentation..."
rm -f JOB-POST.md PROPOSAL.md brief.md plan*.md plano.md prd-*.md 2>/dev/null || true
rm -f IMPLEMENTATION-SUMMARY.md AGENTS.md DECISION-FRAMEWORK.md 2>/dev/null || true
rm -f storage-structure.md dependency_trace.txt dependency-map.mermaid 2>/dev/null || true
rm -f protocol-inventory.json a.md 2>/dev/null || true

# Remove Python cache
echo "🐍 Removing Python cache..."
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.pyo" -delete 2>/dev/null || true
find . -name "*.pyd" -delete 2>/dev/null || true

# Remove coverage
echo "📊 Removing coverage reports..."
rm -rf coverage/ .pytest_cache/ .coverage htmlcov/ 2>/dev/null || true

# Remove .env if exists (keep .env.example)
if [ -f .env ]; then
    echo "🔐 Removing .env file (create .env.example if needed)..."
    rm -f .env
fi

# Remove sample project if it's not a template example
if [ -d "SAMPLE-AI-PROJECT" ]; then
    read -p "❓ Remove SAMPLE-AI-PROJECT? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf SAMPLE-AI-PROJECT
    fi
fi

# Verify template directories are preserved
echo "✅ Verifying template directories..."
if [ ! -d "AI-project-workflow" ]; then
    echo "⚠️  Warning: AI-project-workflow/ not found (should be kept)"
fi
if [ ! -d "dev-workflow" ]; then
    echo "⚠️  Warning: dev-workflow/ not found (should be kept)"
fi

# Create .artifacts structure placeholder
echo "📁 Creating .artifacts structure..."
mkdir -p .artifacts/{protocol-01,protocol-02,protocol-03,protocol-04,protocol-05}
find .artifacts -type d -exec touch {}/.gitkeep \; 2>/dev/null || true

echo "✅ Cleanup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Review changes: git status"
echo "   2. Update .gitignore if needed"
echo "   3. Create .env.example from your .env template"
echo "   4. Commit changes: git add . && git commit -m 'Clean template structure'"
echo "   5. Tag as template: git tag -a v1.0.0-template -m 'Initial template release'"


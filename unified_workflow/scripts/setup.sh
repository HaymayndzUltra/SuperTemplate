#!/bin/bash

# Unified Developer Workflow Setup Script
# This script sets up the environment for the Unified Developer Workflow

set -e

echo "🚀 Setting up Unified Developer Workflow..."
echo "============================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if Python is installed
check_python() {
    print_info "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        print_status "Python $PYTHON_VERSION found"
        
        # Check if version is 3.8+
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
        
        if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
            print_status "Python version is compatible"
        else
            print_error "Python 3.8+ is required. Found: $PYTHON_VERSION"
            exit 1
        fi
    else
        print_error "Python 3 is not installed"
        exit 1
    fi
}

# Check if pip is installed
check_pip() {
    print_info "Checking pip installation..."
    
    if command -v pip3 &> /dev/null; then
        print_status "pip3 found"
    elif command -v pip &> /dev/null; then
        print_status "pip found"
    else
        print_error "pip is not installed"
        exit 1
    fi
}

# Install Python dependencies
install_dependencies() {
    print_info "Installing Python dependencies..."
    
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt
        print_status "Dependencies installed successfully"
    else
        print_error "requirements.txt not found"
        exit 1
    fi
}

# Create necessary directories
create_directories() {
    print_info "Creating necessary directories..."
    
    # Create evidence directories
    mkdir -p evidence/{phase0,phase1,phase2,phase3,phase4,phase5,phase6}
    print_status "Evidence directories created"
    
    # Create project directories
    mkdir -p projects
    print_status "Project directories created"
    
    # Create log directories
    mkdir -p logs
    print_status "Log directories created"
    
    # Create template directories
    mkdir -p templates
    print_status "Template directories created"
    
    # Create config directory
    mkdir -p config
    print_status "Config directory created"
}

# Set up configuration files
setup_config() {
    print_info "Setting up configuration files..."
    
    # Copy template configuration if it doesn't exist
    if [ ! -f "config/production.json" ]; then
        if [ -f "config/template.json" ]; then
            cp config/template.json config/production.json
            print_status "Configuration template copied"
        else
            # Create basic configuration
            cat > config/production.json << 'CONFIG_EOF'
{
  "project": {
    "name": "default-project",
    "description": "Default project configuration",
    "version": "1.0.0"
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-sonnet",
    "api_key": "your-api-key-here"
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
CONFIG_EOF
            print_status "Basic configuration created"
        fi
    else
        print_status "Configuration file already exists"
    fi
}

# Set up environment file
setup_environment() {
    print_info "Setting up environment file..."
    
    if [ ! -f ".env" ]; then
        cat > .env << 'ENV_EOF'
# Unified Developer Workflow Environment Variables
AI_API_KEY=your-api-key-here
PROJECT_ROOT=$(pwd)
EVIDENCE_DIR=$(pwd)/evidence
LOG_LEVEL=INFO
CONFIG_FILE=config/production.json
ENV_EOF
        print_status "Environment file created"
        print_warning "Please update .env file with your actual API keys and paths"
    else
        print_status "Environment file already exists"
    fi
}

# Set file permissions
set_permissions() {
    print_info "Setting file permissions..."
    
    # Make Python scripts executable
    chmod +x automation/*.py 2>/dev/null || true
    print_status "Python scripts made executable"
    
    # Make shell scripts executable
    chmod +x scripts/*.sh 2>/dev/null || true
    print_status "Shell scripts made executable"
    
    # Set proper ownership
    chown -R $(whoami):$(whoami) . 2>/dev/null || true
    print_status "File ownership set"
}

# Run basic tests
run_tests() {
    print_info "Running basic tests..."
    
    if [ -f "tests/run_tests.py" ]; then
        python3 tests/run_tests.py
        print_status "Tests completed successfully"
    else
        print_warning "Test suite not found, skipping tests"
    fi
}

# Display setup completion
display_completion() {
    echo ""
    echo "🎉 Setup Complete!"
    echo "============================================================"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Update your API key in .env file"
    echo "2. Configure your project in config/production.json"
    echo "3. Run a test workflow:"
    echo "   python3 automation/ai_orchestrator.py --project-name \"test-project\""
    echo ""
    echo "📚 Documentation:"
    echo "- User Guide: USER_GUIDE.md"
    echo "- API Reference: API_REFERENCE.md"
    echo "- Deployment Guide: DEPLOYMENT.md"
    echo ""
    echo "🆘 Support:"
    echo "- Check logs in logs/ directory"
    echo "- Review configuration in config/ directory"
    echo "- Consult documentation for troubleshooting"
    echo ""
}

# Main setup function
main() {
    echo "Starting Unified Developer Workflow setup..."
    echo ""
    
    check_python
    check_pip
    install_dependencies
    create_directories
    setup_config
    setup_environment
    set_permissions
    run_tests
    display_completion
}

# Run main function
main "$@"

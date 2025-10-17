#!/bin/bash

# Unified Developer Workflow Maintenance Script
# This script performs regular maintenance tasks

set -e

echo "🔧 Unified Developer Workflow Maintenance"
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

# Clean up old log files
cleanup_logs() {
    print_info "Cleaning up old log files..."
    
    if [ -d "logs" ]; then
        # Keep logs from last 30 days
        find logs -name "*.log" -mtime +30 -delete 2>/dev/null || true
        print_status "Old log files cleaned up"
    else
        print_warning "Logs directory not found"
    fi
}

# Clean up temporary files
cleanup_temp() {
    print_info "Cleaning up temporary files..."
    
    # Clean up Python cache
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
    find . -name "*.pyc" -delete 2>/dev/null || true
    
    # Clean up pytest cache
    find . -name ".pytest_cache" -type d -exec rm -rf {} + 2>/dev/null || true
    
    # Clean up temporary project directories
    find . -name "test-project*" -type d -exec rm -rf {} + 2>/dev/null || true
    find . -name "integration-test-project*" -type d -exec rm -rf {} + 2>/dev/null || true
    
    print_status "Temporary files cleaned up"
}

# Update dependencies
update_dependencies() {
    print_info "Updating Python dependencies..."
    
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt --upgrade
        print_status "Dependencies updated"
    else
        print_warning "requirements.txt not found"
    fi
}

# Backup evidence
backup_evidence() {
    print_info "Backing up evidence..."
    
    if [ -d "evidence" ]; then
        BACKUP_FILE="evidence-backup-$(date +%Y%m%d).tar.gz"
        tar -czf "$BACKUP_FILE" evidence/ 2>/dev/null || true
        
        if [ -f "$BACKUP_FILE" ]; then
            print_status "Evidence backed up to $BACKUP_FILE"
        else
            print_warning "Evidence backup failed"
        fi
    else
        print_warning "Evidence directory not found"
    fi
}

# Validate configuration
validate_config() {
    print_info "Validating configuration..."
    
    if [ -f "config/production.json" ]; then
        python3 -c "import json; json.load(open('config/production.json'))" 2>/dev/null
        if [ $? -eq 0 ]; then
            print_status "Configuration is valid"
        else
            print_error "Configuration is invalid"
        fi
    else
        print_warning "Configuration file not found"
    fi
}

# Check disk space
check_disk_space() {
    print_info "Checking disk space..."
    
    DISK_USAGE=$(df -h . | awk 'NR==2 {print $5}' | sed 's/%//')
    
    if [ "$DISK_USAGE" -gt 90 ]; then
        print_error "Disk usage is high: ${DISK_USAGE}%"
    elif [ "$DISK_USAGE" -gt 80 ]; then
        print_warning "Disk usage is getting high: ${DISK_USAGE}%"
    else
        print_status "Disk usage is normal: ${DISK_USAGE}%"
    fi
}

# Run health checks
health_check() {
    print_info "Running health checks..."
    
    # Check Python installation
    if command -v python3 &> /dev/null; then
        print_status "Python is available"
    else
        print_error "Python is not available"
    fi
    
    # Check pip installation
    if command -v pip3 &> /dev/null; then
        print_status "pip is available"
    else
        print_error "pip is not available"
    fi
    
    # Check required directories
    for dir in automation evidence phases tests; do
        if [ -d "$dir" ]; then
            print_status "Directory $dir exists"
        else
            print_error "Directory $dir is missing"
        fi
    done
    
    # Check required files
    for file in requirements.txt README.md; do
        if [ -f "$file" ]; then
            print_status "File $file exists"
        else
            print_error "File $file is missing"
        fi
    done
}

# Generate maintenance report
generate_report() {
    print_info "Generating maintenance report..."
    
    REPORT_FILE="maintenance-report-$(date +%Y%m%d).txt"
    
    cat > "$REPORT_FILE" << EOF
Unified Developer Workflow Maintenance Report
Generated: $(date)
============================================================

Disk Usage: $(df -h . | awk 'NR==2 {print $5}')
Python Version: $(python3 --version 2>/dev/null || echo "Not available")
Pip Version: $(pip3 --version 2>/dev/null || echo "Not available")

Directories:
$(ls -la | grep "^d" | awk '{print $9}' | grep -v "^\.$\|^\.\.$")

Files:
$(ls -la | grep "^-" | wc -l) files found

Evidence:
$(find evidence -type f 2>/dev/null | wc -l) evidence files

Logs:
$(find logs -name "*.log" 2>/dev/null | wc -l) log files

EOF
    
    print_status "Maintenance report generated: $REPORT_FILE"
}

# Main maintenance function
main() {
    echo "Starting maintenance tasks..."
    echo ""
    
    cleanup_logs
    cleanup_temp
    update_dependencies
    backup_evidence
    validate_config
    check_disk_space
    health_check
    generate_report
    
    echo ""
    echo "🎉 Maintenance Complete!"
    echo "============================================================"
    echo ""
    echo "📋 Summary:"
    echo "- Log files cleaned up"
    echo "- Temporary files removed"
    echo "- Dependencies updated"
    echo "- Evidence backed up"
    echo "- Configuration validated"
    echo "- Disk space checked"
    echo "- Health checks completed"
    echo "- Maintenance report generated"
    echo ""
}

# Run main function
main "$@"

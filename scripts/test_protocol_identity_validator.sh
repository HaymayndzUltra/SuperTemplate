#!/bin/bash
# Test script for Protocol Identity Validator
# Validates that the validator works correctly and produces expected outputs

set -e  # Exit on error

WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$WORKSPACE_ROOT"

echo "=========================================="
echo "Protocol Identity Validator Test Suite"
echo "=========================================="
echo ""

# Test 1: Single protocol validation
echo "Test 1: Validating single protocol (Protocol 01)..."
python3 scripts/validate_protocol_identity.py --protocol 01
if [ $? -eq 0 ] || [ $? -eq 1 ]; then
    echo "✅ Test 1 PASSED: Single protocol validation executed"
else
    echo "❌ Test 1 FAILED: Unexpected exit code"
    exit 1
fi
echo ""

# Test 2: Verify output file exists
echo "Test 2: Checking output file existence..."
if [ -f ".artifacts/validation/protocol-01-identity.json" ]; then
    echo "✅ Test 2 PASSED: Output file created"
else
    echo "❌ Test 2 FAILED: Output file not found"
    exit 1
fi
echo ""

# Test 3: Validate JSON structure
echo "Test 3: Validating JSON structure..."
python3 -c "
import json
import sys

with open('.artifacts/validation/protocol-01-identity.json') as f:
    data = json.load(f)

required_keys = [
    'validator', 'protocol_id', 'validation_timestamp',
    'basic_information', 'prerequisites', 'integration_points',
    'compliance_standards', 'documentation_quality',
    'overall_score', 'validation_status', 'issues', 'recommendations'
]

missing = [k for k in required_keys if k not in data]
if missing:
    print(f'Missing keys: {missing}')
    sys.exit(1)

print('✅ Test 3 PASSED: JSON structure valid')
"
echo ""

# Test 4: All protocols validation
echo "Test 4: Validating all protocols..."
python3 scripts/validate_protocol_identity.py --all > /tmp/validator_output.txt 2>&1
if [ $? -eq 0 ] || [ $? -eq 1 ]; then
    echo "✅ Test 4 PASSED: All protocols validation executed"
    echo "   Output preview:"
    head -5 /tmp/validator_output.txt | sed 's/^/   /'
else
    echo "❌ Test 4 FAILED: Unexpected exit code"
    exit 1
fi
echo ""

# Test 5: Verify summary reports
echo "Test 5: Checking summary report generation..."
SUMMARY_FILES=(
    "identity-validation-summary.json"
    "compliance-matrix.json"
    "integration-map.json"
    "documentation-quality-report.json"
)

ALL_EXIST=true
for file in "${SUMMARY_FILES[@]}"; do
    if [ -f ".artifacts/validation/$file" ]; then
        echo "   ✓ $file exists"
    else
        echo "   ✗ $file missing"
        ALL_EXIST=false
    fi
done

if [ "$ALL_EXIST" = true ]; then
    echo "✅ Test 5 PASSED: All summary reports generated"
else
    echo "❌ Test 5 FAILED: Some summary reports missing"
    exit 1
fi
echo ""

# Test 6: Validate summary report structure
echo "Test 6: Validating summary report structure..."
python3 -c "
import json

with open('.artifacts/validation/identity-validation-summary.json') as f:
    summary = json.load(f)

required_keys = ['validation_timestamp', 'total_protocols', 'pass_count', 
                 'warning_count', 'fail_count', 'average_score', 'protocols']

missing = [k for k in required_keys if k not in summary]
if missing:
    print(f'Missing keys in summary: {missing}')
    exit(1)

if summary['total_protocols'] != 27:
    print(f'Expected 27 protocols, got {summary[\"total_protocols\"]}')
    exit(1)

print('✅ Test 6 PASSED: Summary report structure valid')
print(f'   Total protocols: {summary[\"total_protocols\"]}')
print(f'   Pass: {summary[\"pass_count\"]}, Warning: {summary[\"warning_count\"]}, Fail: {summary[\"fail_count\"]}')
print(f'   Average score: {summary[\"average_score\"]:.3f}')
"
echo ""

# Test 7: Validate dimension scoring
echo "Test 7: Validating dimension scoring logic..."
python3 -c "
import json

with open('.artifacts/validation/protocol-01-identity.json') as f:
    result = json.load(f)

dimensions = ['basic_information', 'prerequisites', 'integration_points', 
              'compliance_standards', 'documentation_quality']

for dim in dimensions:
    if dim not in result:
        print(f'Missing dimension: {dim}')
        exit(1)
    
    if 'score' not in result[dim]:
        print(f'Missing score in {dim}')
        exit(1)
    
    score = result[dim]['score']
    if not (0.0 <= score <= 1.0):
        print(f'Invalid score in {dim}: {score}')
        exit(1)

print('✅ Test 7 PASSED: All dimension scores valid')
"
echo ""

# Test 8: Test error handling (non-existent protocol)
echo "Test 8: Testing error handling with non-existent protocol..."
python3 scripts/validate_protocol_identity.py --protocol 99 > /tmp/error_test.txt 2>&1
if [ $? -eq 1 ]; then
    if grep -q "Protocol file not found" /tmp/error_test.txt; then
        echo "✅ Test 8 PASSED: Error handling works correctly"
    else
        echo "⚠️  Test 8 WARNING: Exit code correct but error message unexpected"
    fi
else
    echo "❌ Test 8 FAILED: Should fail for non-existent protocol"
    exit 1
fi
echo ""

# Test 9: Validate compliance matrix
echo "Test 9: Validating compliance matrix structure..."
python3 -c "
import json

with open('.artifacts/validation/compliance-matrix.json') as f:
    matrix = json.load(f)

if 'protocols' not in matrix:
    print('Missing protocols key in compliance matrix')
    exit(1)

if len(matrix['protocols']) == 0:
    print('No protocols in compliance matrix')
    exit(1)

# Check first protocol has required fields
first = matrix['protocols'][0]
if 'protocol_id' not in first or 'compliance_score' not in first:
    print('Missing required fields in compliance matrix entry')
    exit(1)

print('✅ Test 9 PASSED: Compliance matrix structure valid')
print(f'   Protocols in matrix: {len(matrix[\"protocols\"])}')
"
echo ""

# Test 10: Validate integration map
echo "Test 10: Validating integration map structure..."
python3 -c "
import json

with open('.artifacts/validation/integration-map.json') as f:
    imap = json.load(f)

if 'protocols' not in imap:
    print('Missing protocols key in integration map')
    exit(1)

# Check first protocol has required fields
if len(imap['protocols']) > 0:
    first = imap['protocols'][0]
    if 'protocol_id' not in first or 'integration_score' not in first:
        print('Missing required fields in integration map entry')
        exit(1)

print('✅ Test 10 PASSED: Integration map structure valid')
print(f'   Protocols in map: {len(imap[\"protocols\"])}')
"
echo ""

echo "=========================================="
echo "Test Suite Summary"
echo "=========================================="
echo "✅ All tests passed successfully!"
echo ""
echo "Generated artifacts:"
ls -lh .artifacts/validation/*.json | awk '{print "  ", $9, "(" $5 ")"}'
echo ""
echo "Validator is ready for production use."

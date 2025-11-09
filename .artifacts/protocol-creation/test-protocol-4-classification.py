#!/usr/bin/env python3
"""
Test Protocol 4 Issue Classification System
Validates that issue classification logic works as expected
"""

def classify_issue(issue):
    """Classify validation issue by type"""
    message = issue['message'].lower()
    
    # Check for compound patterns first (most specific)
    if ('missing' in message or 'not found' in message) and 'pattern' in message:
        # "Missing pattern" = pattern mismatch, not missing content
        return 'PATTERN_MISMATCH'
    elif ('missing' in message or 'not found' in message) and 'keyword' in message:
        # "Missing keyword" = keyword missing, not missing content
        return 'KEYWORD_MISSING'
    # Check specific patterns (high priority)
    elif 'pattern' in message or 'expected' in message:
        return 'PATTERN_MISMATCH'
    elif 'keyword' in message or 'must contain' in message:
        return 'KEYWORD_MISSING'
    elif 'count' in message or 'minimum' in message:
        return 'INSUFFICIENT_COUNT'
    elif 'syntax' in message or 'format' in message:
        return 'FORMAT_ERROR'
    # Check generic patterns last (lower priority)
    elif 'missing' in message or 'not found' in message:
        return 'MISSING_CONTENT'
    else:
        return 'UNKNOWN'

# Test cases from IMPLEMENTATION-PROMPT-PROTOCOL-4.md
test_issues = [
    # "Missing You are a pattern" = Missing the 'You are a' pattern format
    {'message': 'Missing You are a pattern', 'expected': 'PATTERN_MISMATCH'},
    {'message': 'Gate count: 1 (need ≥2)', 'expected': 'INSUFFICIENT_COUNT'},
    {'message': 'Expected pattern not found', 'expected': 'PATTERN_MISMATCH'},
    {'message': 'Content not found in section', 'expected': 'MISSING_CONTENT'},
    {'message': 'Minimum 3 gates required', 'expected': 'INSUFFICIENT_COUNT'},
    {'message': 'Markdown syntax error in table', 'expected': 'FORMAT_ERROR'},
    {'message': 'Must contain mission keyword', 'expected': 'KEYWORD_MISSING'},
    {'message': 'Invalid heading format', 'expected': 'FORMAT_ERROR'},
    {'message': 'Missing scope keyword', 'expected': 'KEYWORD_MISSING'},
    {'message': 'Unknown validation error', 'expected': 'UNKNOWN'},
]

print("=" * 60)
print("PROTOCOL 4 ISSUE CLASSIFICATION TEST")
print("=" * 60)
print()

passed = 0
failed = 0

for i, issue in enumerate(test_issues, 1):
    result = classify_issue(issue)
    expected = issue['expected']
    status = "✓ PASS" if result == expected else "✗ FAIL"
    
    print(f"Test {i}: {status}")
    print(f"  Message: {issue['message']}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    
    if result == expected:
        passed += 1
    else:
        failed += 1
    print()

print("=" * 60)
print(f"RESULTS: {passed}/{len(test_issues)} passed, {failed}/{len(test_issues)} failed")
print("=" * 60)

if failed == 0:
    print("\n✅ All tests passed! Classification system working correctly.")
    exit(0)
else:
    print(f"\n❌ {failed} test(s) failed. Review classification logic.")
    exit(1)

#!/usr/bin/env python3
"""
Script to add --protocol-dir argument to all validator scripts
"""

import re
from pathlib import Path

# List of all validator script files
VALIDATOR_FILES = [
    "validate_protocol_role.py",
    "validate_protocol_workflow.py",
    "validate_protocol_gates.py",
    "validate_protocol_scripts.py",
    "validate_protocol_communication.py",
    "validate_protocol_evidence.py",
    "validate_protocol_handoff.py",
    "validate_protocol_reasoning.py",
    "validate_protocol_reflection.py",
]

SCRIPTS_DIR = Path(__file__).parent

def fix_validator(filepath: Path):
    """Fix a single validator script to accept --protocol-dir argument"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern 1: Fix __init__ method signature
    init_pattern = r'(def __init__\(self, workspace_root: Path)\):'
    init_replacement = r'\1, protocol_dir: Path = None):'
    
    if re.search(init_pattern, content):
        content = re.sub(init_pattern, init_replacement, content)
        print(f"✓ Fixed __init__ signature in {filepath.name}")
    
    # Pattern 2: Fix protocols_dir initialization
    protocols_dir_pattern = r'(self\.protocols_dir = )workspace_root / "\.cursor" / "ai-driven-workflow"'
    protocols_dir_replacement = r'\1protocol_dir if protocol_dir else workspace_root / ".cursor" / "ai-driven-workflow"'
    
    if re.search(protocols_dir_pattern, content):
        content = re.sub(protocols_dir_pattern, protocols_dir_replacement, content)
        print(f"✓ Fixed protocols_dir initialization in {filepath.name}")
    
    # Pattern 3: Add --protocol-dir argument to argparse
    argparse_pattern = r'(parser\.add_argument\(\s+["\']--workspace["\'],[^)]+\))'
    argparse_addition = r'''\1
    parser.add_argument(
        "--protocol-dir",
        help="Custom protocol directory path (default: .cursor/ai-driven-workflow)"
    )'''
    
    if re.search(argparse_pattern, content) and "--protocol-dir" not in content:
        content = re.sub(argparse_pattern, argparse_addition, content)
        print(f"✓ Added --protocol-dir argument in {filepath.name}")
    
    # Pattern 4: Fix validator instantiation
    instantiation_pattern = r'validator = \w+Validator\(workspace_root\)'
    
    if re.search(instantiation_pattern, content):
        # Need to add protocol_dir line before instantiation
        workspace_parse_pattern = r'(workspace_root = Path\(args\.workspace\)\.resolve\(\))\s+'
        workspace_addition = r'''\1
    protocol_dir = Path(args.protocol_dir).resolve() if args.protocol_dir else None
    '''
        content = re.sub(workspace_parse_pattern, workspace_addition, content)
        
        # Update instantiation
        content = re.sub(instantiation_pattern, lambda m: m.group(0).replace('(workspace_root)', '(workspace_root, protocol_dir)'), content)
        print(f"✓ Fixed validator instantiation in {filepath.name}")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print("Fixing all validator scripts to accept --protocol-dir argument...\n")
    
    fixed_count = 0
    for validator_file in VALIDATOR_FILES:
        filepath = SCRIPTS_DIR / validator_file
        if filepath.exists():
            try:
                if fix_validator(filepath):
                    fixed_count += 1
                    print(f"✅ Successfully fixed {validator_file}\n")
            except Exception as e:
                print(f"❌ Error fixing {validator_file}: {e}\n")
        else:
            print(f"⚠️  File not found: {validator_file}\n")
    
    print(f"\n{'='*60}")
    print(f"Total files fixed: {fixed_count}/{len(VALIDATOR_FILES)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

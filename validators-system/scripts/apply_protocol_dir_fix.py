#!/usr/bin/env python3
"""
Apply --protocol-dir fix to all validator scripts systematically
"""

from pathlib import Path
import re

VALIDATORS = [
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

def fix_validator(filepath: Path) -> bool:
    """Apply all 3 fixes to a validator script"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix 1: Update __init__ signature
    content = re.sub(
        r'def __init__\(self, workspace_root: Path\) -> None:',
        'def __init__(self, workspace_root: Path, protocol_dir: Path = None) -> None:',
        content
    )
    
    # Fix 2: Add protocol_dir storage in __init__
    content = re.sub(
        r'(def __init__\(self, workspace_root: Path, protocol_dir: Path = None\) -> None:\s+self\.workspace_root = workspace_root)\n',
        r'\1\n        self.protocol_dir = protocol_dir\n',
        content
    )
    
    # Fix 3: Update get_protocol_file calls
    content = re.sub(
        r'get_protocol_file\(self\.workspace_root, protocol_id\)',
        'get_protocol_file(self.workspace_root, protocol_id, self.protocol_dir)',
        content
    )
    
    # Fix 4: Add --protocol-dir argument to argparse (before args = parser.parse_args())
    if '--protocol-dir' not in content:
        content = re.sub(
            r'(parser\.add_argument\("--workspace"[^)]+\))\s*\n\s*args = parser\.parse_args\(\)',
            r'\1\n    parser.add_argument("--protocol-dir", help="Custom protocol directory path (default: .cursor/ai-driven-workflow)")\n\n    args = parser.parse_args()',
            content
        )
    
    # Fix 5: Add protocol_dir parsing in run_cli or main
    if 'protocol_dir = Path(args.protocol_dir)' not in content:
        content = re.sub(
            r'(workspace_root = Path\(args\.workspace\)\.resolve\(\))\s*\n(\s+)validator =',
            r'\1\n\2protocol_dir = Path(args.protocol_dir).resolve() if args.protocol_dir else None\n\2validator =',
            content
        )
    
    # Fix 6: Update validator instantiation
    content = re.sub(
        r'validator = (\w+Validator)\(workspace_root\)',
        r'validator = \1(workspace_root, protocol_dir)',
        content
    )
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("Applying --protocol-dir fix to all validators...\n")
    
    fixed_count = 0
    for validator_file in VALIDATORS:
        filepath = SCRIPTS_DIR / validator_file
        if filepath.exists():
            try:
                if fix_validator(filepath):
                    print(f"✅ Fixed {validator_file}")
                    fixed_count += 1
                else:
                    print(f"⚠️  No changes needed for {validator_file}")
            except Exception as e:
                print(f"❌ Error fixing {validator_file}: {e}")
        else:
            print(f"⚠️  File not found: {validator_file}")
    
    print(f"\n{'='*60}")
    print(f"Total files fixed: {fixed_count}/{len(VALIDATORS)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Final fix - add --protocol-dir argparse line to remaining validators"""

from pathlib import Path

VALIDATORS = [
    "validate_protocol_gates.py",
    "validate_protocol_scripts.py",
    "validate_protocol_communication.py",
    "validate_protocol_evidence.py",
    "validate_protocol_handoff.py",
    "validate_protocol_reasoning.py",
    "validate_protocol_reflection.py",
]

SCRIPTS_DIR = Path(__file__).parent

def add_argparse_line(filepath: Path) -> bool:
    """Add --protocol-dir argument if not present"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the --workspace line
    modified = False
    for i, line in enumerate(lines):
        if '--workspace' in line and 'parser.add_argument' in line:
            # Check if --protocol-dir already exists
            if any('--protocol-dir' in l for l in lines):
                print(f"⚠️  {filepath.name} already has --protocol-dir")
                return False
            
            # Insert after the next line (after the closing parenthesis)
            insert_index = i + 1
            indent = "    "
            new_line = f'{indent}parser.add_argument("--protocol-dir", help="Custom protocol directory path (default: .cursor/ai-driven-workflow)")\n'
            lines.insert(insert_index, new_line)
            modified = True
            break
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True
    
    return False

def main():
    print("Adding --protocol-dir argparse argument...\n")
    
    fixed_count = 0
    for validator_file in VALIDATORS:
        filepath = SCRIPTS_DIR / validator_file
        if filepath.exists():
            try:
                if add_argparse_line(filepath):
                    print(f"✅ Added argparse line to {validator_file}")
                    fixed_count += 1
            except Exception as e:
                print(f"❌ Error fixing {validator_file}: {e}")
        else:
            print(f"⚠️  File not found: {validator_file}")
    
    print(f"\n{'='*60}")
    print(f"Total files fixed: {fixed_count}/{len(VALIDATORS)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

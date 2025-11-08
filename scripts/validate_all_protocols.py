#\!/usr/bin/env python3
"""
Validate All Protocols
Wrapper script to run all validators on a protocol.
"""
import argparse
import subprocess
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Run all validators on a protocol')
    parser.add_argument('--protocol', required=True, help='Protocol ID')
    parser.add_argument('--workspace', required=True, help='Workspace path')
    args = parser.parse_args()
    
    # Delegate to actual validator system
    validator_script = Path(args.workspace) / 'validators-system' / 'scripts' / 'validate_all_protocols.py'
    
    if validator_script.exists():
        result = subprocess.run([
            'python3', str(validator_script),
            '--protocol', args.protocol,
            '--workspace', args.workspace
        ])
        return result.returncode
    else:
        print(f"[ERROR] Validator script not found: {validator_script}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Wrapper to run rules_audit_quick for retrospective workflows."""

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    script_path = Path(__file__).with_name("rules_audit_quick.py")
    cmd = [sys.executable, str(script_path), *sys.argv[1:]]
    result = subprocess.run(cmd, env=os.environ.copy())
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())

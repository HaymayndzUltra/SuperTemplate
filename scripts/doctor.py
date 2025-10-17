#!/usr/bin/env python3
"""
Environment Doctor

Probes Docker/Node/npm/Python/pip/Go, detects CI/non-Docker envs,
and prints actionable PASS/FAIL checks.
"""

import os
import sys
import argparse
import shutil
import subprocess
from typing import Tuple


def check(cmd: str, version_args=("--version",)) -> Tuple[bool, str]:
    path = shutil.which(cmd)
    if not path:
        return False, f"{cmd} not found in PATH"
    try:
        out = subprocess.run([cmd, *version_args], capture_output=True, text=True, timeout=5)
        ver = out.stdout.strip() or out.stderr.strip()
        return True, ver.splitlines()[0] if ver else f"{cmd} detected"
    except Exception as e:
        return True, f"{cmd} detected, version check failed: {e}"


def print_result(name: str, ok: bool, info: str, hint: str = ""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}: {info}")
    if hint and not ok:
        print(f"      Hint: {hint}")


def main():
    parser = argparse.ArgumentParser(description="Environment Doctor")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if critical tools are missing")
    args = parser.parse_args()
    # CI detection
    in_ci = os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS")
    if in_ci:
        print("[INFO] CI environment detected")
    else:
        print("[INFO] Local environment detected")

    ok_docker, info = check("docker")
    print_result("Docker", ok_docker, info, hint="Install Docker and ensure daemon is running: https://docker.com")

    ok_node, info = check("node")
    print_result("Node.js", ok_node, info, hint="Install Node 18+: https://nodejs.org")

    ok_npm, info = check("npm")
    print_result("npm", ok_npm, info, hint="Install with Node or use pnpm/yarn")

    ok_py, info = check("python3", ("--version",))
    print_result("Python3", ok_py, info, hint="Install Python 3.11+")

    ok_pip = bool(shutil.which("pip")) or bool(shutil.which("pip3"))
    print_result("pip", ok_pip, "pip detected" if ok_pip else "pip not found", hint="Install pip or use python -m ensurepip")

    ok_go, info = check("go", ("version",))
    print_result("Go", ok_go, info, hint="Install Go 1.21+: https://golang.org")

    # Strict mode: fail if critical tools missing
    if args.strict:
        critical_missing = []
        if not ok_node:
            critical_missing.append("node")
        if not ok_npm:
            critical_missing.append("npm")
        if not ok_py:
            critical_missing.append("python3")
        if not ok_pip:
            critical_missing.append("pip/pip3")
        if critical_missing:
            print(f"\n[ERROR] Critical tools missing: {', '.join(critical_missing)}")
            sys.exit(2)

    # Summary exit code (non-strict) is 0; doctor is advisory
    print("\n[INFO] Doctor checks complete")


if __name__ == "__main__":
    main()


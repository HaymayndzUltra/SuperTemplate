import subprocess
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "scripts" / "validate_workflows.py"
WF_DIR = ROOT / "docs" / "workflows"


def run(cmd: str) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, shell=True, text=True, capture_output=True, cwd=ROOT)


def test_validator_help_runs():
    result = run(f"python3 {SCRIPT} 2>&1")
    assert result.returncode == 0
    assert "Validate workflow docs" in (result.stdout + result.stderr)


def test_validator_list_and_dry_run():
    result = run(f"python3 {SCRIPT} --list")
    assert result.returncode == 0
    assert "docs/workflows" in result.stdout

    result = run(f"python3 {SCRIPT} --all --dry-run")
    assert result.returncode == 0
    assert "[DRY RUN] Validation completed" in result.stdout


def test_validator_module_import_and_functions():
    spec = importlib.util.spec_from_file_location("validate_workflows", str(SCRIPT))
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    files = mod.find_markdown_files(str(WF_DIR))
    assert isinstance(files, list)
    # Check sections on a trivial snippet
    errs = mod.check_sections("# Title\n\n## Overview\n\n## Prerequisites\n\n## Steps\n\n## Evidence\n\n## Failure Modes\n\n## Overall Acceptance\n", "mem")
    assert errs == []


def test_validator_all_ok():
    result = run(f"python3 {SCRIPT} --all")
    assert result.returncode == 0
    assert "[VALIDATION OK]" in result.stdout


def test_validator_failure_case_with_temp_invalid_doc(tmp_path):
    # Create a temporary invalid workflow doc to force failures
    temp_md = WF_DIR / "_tmp_invalid_for_test.md"
    try:
        temp_md.write_text("# Temp Invalid Doc\n\nJust text, no frontmatter or required sections.\n")
        result = run(f"python3 {SCRIPT} --all")
        assert result.returncode == 2
        assert "[VALIDATION FAILED]" in result.stdout
    finally:
        if temp_md.exists():
            temp_md.unlink()
#!/usr/bin/env python3
"""Policy router regression test runner.

This utility discovers YAML based policy decision fixtures and executes them
against the workflow router implementation.  The original version of the script
was tightly coupled to the repository layout, repeatedly re-opened YAML files,
and printed ad-hoc output which made automated verification difficult.  The
reworked implementation provides a structured CLI, deterministic discovery,
and machine-readable summaries so the test harness can gate CI reliably.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from importlib import util
from pathlib import Path
import sys
from typing import Iterable, Iterator, Sequence

import yaml

DEFAULT_ROOT = Path("/workspace")
DEFAULT_CASE_PATTERNS = ("policy-tests/*.yaml",)
ROUTER_SUBPATH = Path(".cursor/ai-driven-workflow/router/router.py")


@dataclass(frozen=True)
class PolicyCase:
    """Represents a single policy regression scenario."""

    name: str
    expect_decision: str
    context: dict[str, object]
    source: Path


@dataclass(frozen=True)
class CaseResult:
    """Execution outcome for a :class:`PolicyCase`."""

    case: PolicyCase
    decision: str | None
    payload: dict[str, object] | None
    passed: bool


def _load_router(router_path: Path):
    """Dynamically import the router module from ``router_path``.

    The loader mirrors the previous behaviour but adds defensive error handling
    so callers receive clear messages when the router cannot be imported.
    """

    router_path = router_path.resolve()
    if not router_path.exists():
        raise FileNotFoundError(f"Router module not found at {router_path}")

    spec = util.spec_from_file_location("policy_router", router_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to create module spec for {router_path}")

    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[assignment]

    if not hasattr(module, "route_decision"):
        raise AttributeError(
            f"Router module '{router_path}' does not expose route_decision"
        )

    return module


def _iter_yaml_documents(path: Path) -> Iterator[object]:
    with path.open("r", encoding="utf-8") as handle:
        for document in yaml.safe_load_all(handle):
            if document is None:
                continue
            yield document


def _normalize_case(raw: object, source: Path) -> PolicyCase:
    if not isinstance(raw, dict):
        raise TypeError(f"Expected mapping in {source}, received {type(raw)!r}")

    name = str(raw.get("name") or source.stem)
    expect = raw.get("expect_decision")
    if expect is None:
        raise ValueError(f"Missing 'expect_decision' field in {source}")

    context = raw.get("context") or {}
    if not isinstance(context, dict):
        raise TypeError(f"Context for {name} must be a mapping")

    return PolicyCase(name=name, expect_decision=str(expect), context=context, source=source)


def _discover_case_files(root: Path, selectors: Sequence[str]) -> list[Path]:
    files: list[Path] = []
    for selector in selectors:
        selector_path = Path(selector)
        matches: Iterable[Path]
        if selector_path.is_absolute():
            if selector_path.exists() and selector_path.is_file():
                matches = [selector_path]
            else:
                matches = selector_path.parent.glob(selector_path.name)
        else:
            matches = root.glob(selector)
        for match in matches:
            if match.is_file():
                files.append(match.resolve())
    # Preserve order but drop duplicates
    seen: set[Path] = set()
    unique: list[Path] = []
    for file in files:
        if file not in seen:
            seen.add(file)
            unique.append(file)
    return unique


def _load_cases(files: Sequence[Path]) -> list[PolicyCase]:
    cases: list[PolicyCase] = []
    for path in files:
        for document in _iter_yaml_documents(path):
            if isinstance(document, list):
                for item in document:
                    cases.append(_normalize_case(item, path))
            else:
                cases.append(_normalize_case(document, path))
    return cases


def _run_case(router_module, case: PolicyCase) -> CaseResult:
    response = router_module.route_decision(case.context)  # type: ignore[attr-defined]
    payload = response if isinstance(response, dict) else {"decision": response}
    decision = payload.get("decision") if isinstance(payload, dict) else None
    passed = decision == case.expect_decision
    return CaseResult(case=case, decision=decision, payload=payload, passed=passed)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Execute policy router regression tests based on YAML fixtures.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Repository root used for resolving relative paths (default: /workspace).",
    )
    parser.add_argument(
        "--router",
        type=Path,
        default=None,
        help="Explicit path to router.py (defaults to <root>/.cursor/ai-driven-workflow/router/router.py).",
    )
    parser.add_argument(
        "--cases",
        nargs="*",
        default=DEFAULT_CASE_PATTERNS,
        help="File paths or glob patterns (relative to --root) that contain YAML cases.",
    )
    parser.add_argument(
        "--stop-on-fail",
        action="store_true",
        help="Exit immediately after the first failing case.",
    )
    parser.add_argument(
        "--json-report",
        type=Path,
        help="Optional path to write a machine-readable JSON summary.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print failures instead of every case result.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    router_path = (args.router or (root / ROUTER_SUBPATH)).resolve()

    try:
        router_module = _load_router(router_path)
    except (OSError, ImportError, AttributeError) as exc:  # pragma: no cover - CLI guard
        raise SystemExit(f"Unable to import router: {exc}")

    case_files = _discover_case_files(root, args.cases)
    if not case_files:
        raise SystemExit("No policy test files discovered. Provide --cases selectors.")

    cases = _load_cases(case_files)
    if not cases:
        raise SystemExit("No test cases loaded from the provided YAML files.")

    failures: list[CaseResult] = []
    results: list[CaseResult] = []
    for case in cases:
        result = _run_case(router_module, case)
        results.append(result)
        status = "PASS" if result.passed else "FAIL"
        if not args.quiet or not result.passed:
            decision_display = result.decision if result.decision is not None else "<missing>"
            print(f"[{status}] {case.name}: expect={case.expect_decision} got={decision_display}")
        if not result.passed:
            failures.append(result)
            if args.stop_on_fail:
                break

    if args.json_report:
        payload = {
            "total": len(results),
            "passed": len(results) - len(failures),
            "failed": len(failures),
            "results": [
                {
                    "name": res.case.name,
                    "expect": res.case.expect_decision,
                    "decision": res.decision,
                    "passed": res.passed,
                    "source": str(res.case.source),
                    "payload": res.payload,
                }
                for res in results
            ],
        }
        args.json_report.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    if failures:
        print(f"Policy decision test failures: {len(failures)} / {len(results)}")
        return 2

    print(f"All policy decision tests passed ({len(results)} cases)")
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    sys.exit(main())

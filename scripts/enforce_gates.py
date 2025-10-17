#!/usr/bin/env python3
"""
Numeric gates enforcer for CI.

Reads thresholds from either:
- metrics.thresholds (new-style), or
- quality_gates.* (existing generator schema)

Metrics files expected:
- coverage/coverage-summary.json OR coverage.xml
- metrics/deps.json → {"critical": int, "high": int}
- metrics/perf.json → {"http_p95_ms": float} (optional)
"""

from __future__ import annotations

import json
import math
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    print("[GATES] PyYAML not installed. Try: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


ROOT = Path(os.getenv("PROJECT_ROOT") or Path(__file__).resolve().parents[1])
GATES = ROOT / "gates_config.yaml"


def _read_yaml(p: Path) -> dict:
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception as e:
        raise SystemExit(f"[GATES] Failed to parse YAML {p}: {e}")


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        raise SystemExit(f"[GATES] Failed to parse JSON {p}: {e}")


def read_coverage_pct() -> float:
    """Return coverage percent in 0..100, from Node summary or Python coverage.xml."""
    p_sum = ROOT / "coverage" / "coverage-summary.json"
    if p_sum.exists():
        try:
            data = _read_json(p_sum)
            return float(data["total"]["lines"]["pct"])
        except Exception as e:
            print(f"[GATES] Failed reading {p_sum}: {e}", file=sys.stderr)

    p_xml = ROOT / "coverage.xml"
    if p_xml.exists():
        try:
            root = ET.parse(p_xml).getroot()
            rate = root.attrib.get("line-rate") or root.attrib.get("lines-valid")
            if rate is None:
                raise ValueError("line-rate missing")
            v = float(rate)
            return v * 100.0 if v <= 1.0 else v
        except Exception as e:
            print(f"[GATES] Failed reading {p_xml}: {e}", file=sys.stderr)

    raise SystemExit("[GATES] coverage artifact not found (coverage-summary.json or coverage.xml)")


def read_deps_counts() -> tuple[int, int]:
    p = ROOT / "metrics" / "deps.json"
    if not p.exists():
        raise SystemExit("[GATES] metrics/deps.json missing")
    d = _read_json(p)
    return int(d.get("critical", 0)), int(d.get("high", 0))


def read_perf_p95_ms() -> float:
    p = ROOT / "metrics" / "perf.json"
    if not p.exists():
        raise SystemExit("[GATES] metrics/perf.json missing")
    d = _read_json(p)
    val = float(d.get("http_p95_ms") or d.get("p95_ms") or d.get("p95"))
    if not math.isfinite(val) or val <= 0:
        raise SystemExit(
            f"[GATES] Invalid perf measurement in {p}: expected positive finite number, got {val!r}"
        )
    return val


def thresholds_from_quality_gates(gates: dict) -> dict:
    """Normalize existing quality_gates schema into thresholds strings."""
    qg = gates.get("quality_gates", {}) or {}
    t: dict[str, str] = {}

    # coverage (prefer test_coverage.threshold, fallback coverage.min)
    if isinstance(qg.get("test_coverage"), dict) and qg["test_coverage"].get("threshold") is not None:
        t["coverage"] = f">= {float(qg['test_coverage']['threshold'])}"
    if isinstance(qg.get("coverage"), dict) and qg["coverage"].get("min") is not None:
        t["coverage"] = f">= {float(qg['coverage']['min'])}"

    # security thresholds
    if isinstance(qg.get("security_scan"), dict):
        crit = qg["security_scan"].get("critical_threshold")
        high = qg["security_scan"].get("high_threshold")
        if crit is not None:
            t["vulns_critical"] = f"<= {int(crit)}"
        if high is not None:
            t["vulns_high"] = f"<= {int(high)}"

    # perf (optional)
    if isinstance(qg.get("performance"), dict) and qg["performance"].get("p95_ms") is not None:
        t["perf_p95_ms"] = f"<= {float(qg['performance']['p95_ms'])}"

    return t


def parse_expr(expr: str) -> tuple[str, float]:
    m = re.match(r"^\s*(>=|<=|==)\s*([0-9.]+)\s*$", expr or "")
    if not m:
        raise SystemExit(f"[GATES] Bad threshold expression: {expr!r}")
    return m.group(1), float(m.group(2))


def main() -> int:
    if not GATES.exists():
        print("MISSING:gates_config.yaml")
        return 2

    gates = _read_yaml(GATES)

    # prefer new-style
    metrics = gates.get("metrics") or {}
    thresholds = (metrics.get("thresholds") or {}) if isinstance(metrics, dict) else {}
    if not thresholds:
        thresholds = thresholds_from_quality_gates(gates)
    if not thresholds:
        print("MISSING:thresholds")
        return 2

    failures = 0

    # coverage
    if "coverage" in thresholds:
        op, rhs = parse_expr(thresholds["coverage"])
        val = read_coverage_pct()
        ok = (op == ">=" and val >= rhs) or (op == "<=" and val <= rhs) or (op == "==" and val == rhs)
        print(f"[METRIC] coverage={val:.2f}% expect {op} {rhs} -> {'OK' if ok else 'FAIL'}")
        if not ok:
            failures += 1

    # vulnerabilities
    if "vulns_critical" in thresholds or "vulns_high" in thresholds:
        critical, high = read_deps_counts()
        if "vulns_critical" in thresholds:
            op, rhs = parse_expr(thresholds["vulns_critical"])
            ok = (op == ">=" and critical >= rhs) or (op == "<=" and critical <= rhs) or (op == "==" and critical == rhs)
            print(f"[METRIC] vulns_critical={critical} expect {op} {rhs} -> {'OK' if ok else 'FAIL'}")
            if not ok:
                failures += 1
        if "vulns_high" in thresholds:
            op, rhs = parse_expr(thresholds["vulns_high"])
            ok = (op == ">=" and high >= rhs) or (op == "<=" and high <= rhs) or (op == "==" and high == rhs)
            print(f"[METRIC] vulns_high={high} expect {op} {rhs} -> {'OK' if ok else 'FAIL'}")
            if not ok:
                failures += 1

    # perf p95
    if "perf_p95_ms" in thresholds:
        op, rhs = parse_expr(thresholds["perf_p95_ms"])
        val = read_perf_p95_ms()
        ok = (op == ">=" and val >= rhs) or (op == "<=" and val <= rhs) or (op == "==" and val == rhs)
        print(f"[METRIC] perf_p95_ms={val:.2f} expect {op} {rhs} -> {'OK' if ok else 'FAIL'}")
        if not ok:
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())


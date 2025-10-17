#!/usr/bin/env python3
"""
Write metrics/perf.json with an http_p95_ms value.

Usage examples:
  PERF_P95_MS=420 python scripts/collect_perf.py
  # or
  echo 420 > metrics/input_perf.txt && python scripts/collect_perf.py

The script now fails fast when no valid measurement is supplied so CI cannot
advance without real performance evidence.
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path


ROOT = Path(os.getenv("PROJECT_ROOT") or Path(__file__).resolve().parents[1])
METRICS = ROOT / "metrics"


def _read_perf_source() -> tuple[str, str] | tuple[None, None]:
    """Return the raw value and its source identifier."""

    val = os.getenv("PERF_P95_MS")
    if val:
        return val.strip(), "PERF_P95_MS"

    p = METRICS / "input_perf.txt"
    if p.exists():
        try:
            text = p.read_text(encoding="utf-8").strip()
        except Exception as exc:  # pragma: no cover - defensive logging
            print(f"[PERF] Failed to read {p}: {exc}", file=sys.stderr)
            return None, None
        if text:
            return text, str(p)
    return None, None


def _validate_perf(raw: str, source: str) -> float:
    try:
        value = float(raw)
    except Exception as exc:  # pragma: no cover - defensive logging
        raise ValueError(f"non-numeric value from {source}: {raw!r} ({exc})") from exc

    if not math.isfinite(value):
        raise ValueError(f"non-finite value from {source}: {value!r}")
    if value <= 0:
        raise ValueError(f"expected positive latency from {source}, got {value}")
    return value


def main() -> int:
    METRICS.mkdir(parents=True, exist_ok=True)

    raw, source = _read_perf_source()
    if not raw or not source:
        print(
            "[PERF] Missing performance input. Provide PERF_P95_MS or metrics/input_perf.txt.",
            file=sys.stderr,
        )
        return 1

    try:
        p95 = _validate_perf(raw, source)
    except ValueError as exc:
        print(f"[PERF] {exc}", file=sys.stderr)
        return 1

    (METRICS / "perf.json").write_text(
        f"{{\n  \"http_p95_ms\": {p95} \n}}\n", encoding="utf-8"
    )
    print(f"{{\"http_p95_ms\": {p95} }}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Benchmark project generation (file I/O and template processing) without external deps.

Usage:
  python scripts/benchmark_generation.py
"""

import time
import shutil
from pathlib import Path
from types import SimpleNamespace

from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator
from project_generator.core.industry_config import IndustryConfig


def run_once(name: str, workers: int) -> float:
    bench_root = Path('./_bench')
    proj_dir = bench_root / name
    if proj_dir.exists():
        shutil.rmtree(proj_dir)
    bench_root.mkdir(parents=True, exist_ok=True)

    args = SimpleNamespace(
        name=name,
        industry='healthcare',
        project_type='fullstack',
        frontend='nextjs',
        backend='fastapi',
        database='none',
        auth='auth0',
        deploy='aws',
        features=None,
        compliance='hipaa',
        output_dir=str(bench_root),
        no_git=True,
        no_install=True,
        no_cursor_assets=True,
        force=True,
        workers=workers,
    )
    validator = ProjectValidator()
    config = IndustryConfig(args.industry)
    gen = ProjectGenerator(args, validator, config)

    t0 = time.perf_counter()
    result = gen.generate()
    dt = time.perf_counter() - t0
    if not result.get('success'):
        raise RuntimeError(f"Generation failed: {result.get('error')}")
    return dt


def main():
    try:
        seq = run_once('bench_seq', workers=1)
        par = run_once('bench_par', workers=0)
        print(f"Sequential (workers=1): {seq:.3f}s")
        print(f"Parallel   (auto)     : {par:.3f}s")
        if par < seq:
            print(f"Speedup: {seq / par:.2f}x")
        else:
            print("No speedup observed (environment dependent).")
    except Exception as e:
        print(f"Benchmark error: {e}")


if __name__ == '__main__':
    main()


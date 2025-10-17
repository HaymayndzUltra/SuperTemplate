#!/usr/bin/env python3
"""
Benchmark the router route_decision with and without cache.

It imports the router module twice (cache off/on) and times repeated decisions.
"""

import os
import sys
import time
import types
from importlib import util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER_PATH = ROOT / '.cursor' / 'ai-driven-workflow' / 'router' / 'router.py'


def load_router(cache_on: bool) -> types.ModuleType:
    # Toggle cache through environment before import
    os.environ['ROUTER_CACHE'] = 'on' if cache_on else 'off'
    # Use a unique module name per mode to avoid reuse
    mod_name = f"router_cached_{'on' if cache_on else 'off'}"
    spec = util.spec_from_file_location(mod_name, str(ROUTER_PATH))
    mod = util.module_from_spec(spec)
    assert spec and spec.loader, 'Failed to load router module spec'
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


def bench(router_mod, contexts, loops: int) -> float:
    t0 = time.perf_counter()
    for _ in range(loops):
        for ctx in contexts:
            router_mod.route_decision(ctx)
    return time.perf_counter() - t0


def main():
    # Build contexts: repeated and similar variants
    base = {'tokens': ['framework:react', 'goal:analyze']}
    variants = [
        base,
        {'tokens': ['framework:react', 'goal:plan']},
        {'tokens': ['framework:react', 'goal:execute']},
        {'tokens': ['framework:react', 'goal:review']},
    ]
    loops = 500

    # Cache OFF
    router_off = load_router(cache_on=False)
    t_off = bench(router_off, variants, loops)

    # Cache ON
    router_on = load_router(cache_on=True)
    # Warm-up to populate caches
    bench(router_on, variants, 10)
    t_on = bench(router_on, variants, loops)

    print(f"Cache OFF: {t_off:.4f}s")
    print(f"Cache ON : {t_on:.4f}s")
    if t_on > 0:
        print(f"Speedup  : {t_off / t_on:.2f}x")


if __name__ == '__main__':
    main()


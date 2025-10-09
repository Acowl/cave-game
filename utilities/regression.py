#!/usr/bin/env python3
"""
Run progression regression checks:
  1) generate_level_map
  2) inject_rules
  3) autoplay_route
  4) (optional) capture_gui_snapshots -- skipped by default
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_step(args):
    print(f"\n=== RUN: {' '.join(args)} ===")
    subprocess.check_call(args)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    py = sys.executable
    try:
        run_step([py, str(root / "utilities" / "generate_level_map.py")])
        run_step([py, str(root / "utilities" / "inject_rules.py")])
        run_step([py, str(root / "utilities" / "autoplay_route.py")])
        print("\n✅ Regression checks completed.")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Regression step failed: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())



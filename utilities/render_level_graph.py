#!/usr/bin/env python3
"""
Render a visual graph of the level map produced by generate_level_map.py.

Outputs:
  - docs/level_graph.dot (Graphviz DOT)
  - docs/level_graph.png (if Graphviz installed; otherwise DOT only)
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Any


def load_level_map(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_dot(level_map: Dict[str, Any], out_path: Path) -> None:
    scenes = level_map.get("scenes", {})
    lines = [
        "digraph level {",
        "  rankdir=LR;",
        "  node [shape=box, style=filled, fillcolor=\"#1f2d3a\", fontcolor=white];",
        "  edge [color=\"#90caf9\"];",
    ]

    # Nodes
    for scene in scenes.keys():
        label = scene.replace("_", " ")
        lines.append(f"  \"{scene}\" [label=\"{label}\"];")

    # Edges
    for scene, data in scenes.items():
        for choice in data.get("choices", []):
            target = choice.get("target_scene") or scene
            consequence = choice.get("consequence")
            sim_error = choice.get("sim_error")
            starts_combat = choice.get("starts_combat")

            color = "#90caf9"
            if sim_error:
                color = "#ef5350"  # red for unresolved
            elif starts_combat:
                color = "#ffb74d"  # orange for combat

            edge_label = consequence.replace("_", " ") if consequence else ""
            lines.append(
                f"  \"{scene}\" -> \"{target}\" [label=\"{edge_label}\", color=\"{color}\"];"
            )

    lines.append("}")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def try_render_png(dot_path: Path, png_path: Path) -> bool:
    dot_exe = shutil.which("dot")
    if not dot_exe:
        print("Graphviz 'dot' not found. Skipping PNG render. Install Graphviz to enable.")
        return False
    subprocess.check_call([dot_exe, "-Tpng", str(dot_path), "-o", str(png_path)])
    return True


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    level_map_path = root / "docs" / "level_map.json"
    if not level_map_path.exists():
        print("❌ level_map.json not found. Run utilities/generate_level_map.py first.")
        return 1

    level_map = load_level_map(level_map_path)
    dot_path = root / "docs" / "level_graph.dot"
    png_path = root / "docs" / "level_graph.png"

    write_dot(level_map, dot_path)
    print(f"✅ Wrote DOT: {dot_path}")
    if try_render_png(dot_path, png_path):
        print(f"✅ Wrote PNG: {png_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



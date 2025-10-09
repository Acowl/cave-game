#!/usr/bin/env python3
"""
Build a browsable HTML gallery of GUI snapshots grouped by scene.
Reads PNGs in gui_snapshots/ and emits docs/level_gallery.html.
"""

from __future__ import annotations

from pathlib import Path
from collections import defaultdict


def group_images_by_scene(images):
    groups = defaultdict(list)
    for p in images:
        name = p.stem
        parts = name.split("_")
        scene = parts[0] if parts else "unknown"
        groups[scene].append(p)
    return groups


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    shots = root / "gui_snapshots"
    imgs = sorted(shots.glob("*.png"))
    if not imgs:
        print("No PNG snapshots found in gui_snapshots/.")
        return 0

    groups = group_images_by_scene(imgs)

    lines = [
        "<html><head><meta charset='utf-8'><title>Level Gallery</title>",
        "<style>body{font-family:Arial;background:#0a0a0a;color:#ddd} .scene{margin:20px 0} h2{color:#88ccff} .row{display:flex;flex-wrap:wrap;gap:10px} img{max-width:280px;border:1px solid #333}</style>",
        "</head><body>",
        "<h1>Level Gallery</h1>",
    ]

    for scene, files in sorted(groups.items()):
        lines.append(f"<div class='scene'><h2>{scene.replace('_',' ').title()}</h2>")
        lines.append("<div class='row'>")
        for f in files:
            rel = f.relative_to(root).as_posix()
            lines.append(f"<div><img src='/{rel}' alt='{f.name}'/><div style='font-size:12px'>{f.name}</div></div>")
        lines.append("</div></div>")

    lines.append("</body></html>")

    out = root / "docs" / "level_gallery.html"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Wrote gallery: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



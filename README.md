<!-- PROJECT: SHABUYA CAVE ADVENTURE -->

# SHABUYA Cave Adventure
### A Python 2D Adventure / Exploration Prototype (Portfolio Edition)

> A modular, asset‑driven, Tkinter‑based adventure prototype demonstrating clean architecture, tooling automation, and scalable game GUI design in Python.

---
## 1. Executive Snapshot
| Metric | Current | Notes |
|--------|---------|-------|
| Playable Character Sprites | 7 | Warrior, Rogue, Mage, Cave Guardian, Divine Heart (boss), Ground Creature, Primitive Creature |
| Background Scenes | 15+ | Cave / village / chamber / cosmic variants |
| Game States | 4 (concept) | exploring, combat, talking (WIP), inventory (reserved) |
| GUI Mode | Enhanced Harness | 1200×800 canvas, dropdowns, quick scenario buttons |
| Tooling | 3 Scripts | quick copy, full copy, test manager |
| Platform Support | Win / macOS / Linux | Relative asset paths; no container hard‑coding |

Positioned as a proof of engineering process: reproducible environments, structured codebase, and forward roadmap—rather than final gameplay depth (yet).

---
## 2. Project Goals
1. Provide a visually verifiable harness to iterate art & layout rapidly.
2. Enforce a maintainable separation of concerns (engine vs. interface vs. assets).
3. Demonstrate professional development practices (tooling, documentation, roadmap).
4. Establish a foundation extensible toward a richer RPG / narrative system.

---
## 3. High‑Level Features
### Gameplay / Visual
- Dynamic sprite + background composition per scene and state.
- Combat layout (player vs. enemy positioning baseline).
- Scenario quick buttons (combat / treasure / boss showcase setups).
- State‑aware positioning (exploring vs. combat; future: dialogue/inventory overlays).

### Technical / Architecture
- Modular directory layout under `src/` (core logic, entities, interfaces).
- Enhanced GUI (`enhanced_gui_final.py`) decoupled from deeper engine evolution.
- Relative path asset system (portable across dev environments).
- Lightweight asset caching to avoid redundant image load overhead.
- Environment cloning scripts for safe experiment branches.

### Tooling / Productivity
| Script Location | Purpose |
|-----------------|---------|
| `tools/quick_copy.sh` | Fast test sandbox (no git history) |
| `tools/create_test_copies.sh` | Git‑backed full clone with marker branch |
| `tools/test_manager.sh` | Unified create / list / launch / clean operations |
| `tools/asset_management/` | 14 scripts for asset creation, verification, processing |
| `tools/graphics/` | Graphics generation & optimization utilities |
| `tools/build_system/` | Distribution & packaging automation |
| `tools/testing/` | Testing, debugging & validation scripts |

---
## 4. Repository Structure
```text
cave-game/
├── enhanced_gui_final.py        # Visual sandbox / asset + scene harness
├── launch_game.sh               # POSIX launcher (system checks)
├── requirements.txt             # Third‑party Python dependencies
├── assets/
│   ├── sprites/                 # Character & enemy PNGs
│   └── backgrounds/             # Scene backgrounds
├── src/
│   ├── config.py
│   ├── core/                    # Engine / logic modules (extensible)
│   │   ├── combat.py
│   │   ├── game_engine.py
│   │   ├── game_events.py
│   │   └── scenes.py
│   ├── entities/                # Domain objects
│   │   ├── item.py
│   │   └── player.py
│   └── interfaces/              # UI / presentation abstractions
│       ├── gui.py
│       └── ui.py
├── tools/                       # Development utilities & scripts
│   ├── asset_management/        # Asset creation, verification, processing
│   ├── graphics/                # Graphics generation & optimization
│   ├── build_system/            # Distribution & packaging tools
│   └── testing/                 # Testing & debugging utilities
├── docs/                        # Organized documentation
│   ├── guides/                  # User & developer guides
│   ├── specifications/          # System & API specifications
│   └── reports/                 # Status & analysis reports
├── tests/                       # Test suites (legacy / extend)
├── distribution/                # Packaged releases
├── archive/                     # Legacy files & backups
└── utilities/                   # General purpose scripts
```

---
## 5. Installation & Launch
Prerequisites: Python 3.8+ (3.11 recommended), Pillow, Tkinter (Linux: `sudo apt install python3-tk`)

```bash
git clone https://github.com/Acowl/cave-game.git
cd cave-game
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
python enhanced_gui_final.py
```
Optional (Unix):
```bash
chmod +x launch_game.sh
./launch_game.sh
```

---
## 6. Enhanced GUI Harness (Why It Exists)
Design laboratory for rapid visual validation:
- Validates art direction & sizing
- Deterministic scenario reproduction
- Decoupled from engine core
- Incremental overlay expansion path

UI Elements:
| Element | Function |
|---------|----------|
| Character dropdown | Swap active sprite |
| Scene dropdown | Change background |
| State dropdown | Adjust layout logic |
| Quick buttons | Pre‑baked scenarios |
| Overlay panel | Context + asset counts |

---
## 7. Assets
| Type | Path | Format | Notes |
|------|------|--------|-------|
| Sprites | `assets/sprites/` | PNG ~150×150 | Transparent BG recommended |
| Backgrounds | `assets/backgrounds/` | PNG | Auto-scaled to canvas |

Adding assets:
1. Place PNG
2. Add mapping (future registry planned)
3. Relaunch GUI

---
## 8. Game State Model
| State | Purpose | Layout |
|-------|---------|--------|
| exploring | Default traversal | Centered |
| combat | Encounter framing | Player left / enemy right |
| talking (WIP) | Dialogue staging | Overlay reserved |
| inventory (reserved) | Item management | Future grid |

---
## 9. Local Test Copy Workflow
```bash
```bash
./tools/quick_copy.sh
./tools/create_test_copies.sh
./tools/test_manager.sh list
./tools/test_manager.sh launch 3
./tools/test_manager.sh clean --older-than 7
```

---
## 10. Manual Verification Checklist
| Category | Check |
|----------|-------|
| Sprites | All 7 selectable & render without distortion |
| Backgrounds | Each loads crisp; no scaling artifacts |
| States | Exploring ↔ Combat reposition logic works |
| Overlay | Displays accurate counts & identifiers |
| Quick Scenarios | Apply expected scene + character + state bundles |
| Console | No unhandled exceptions |

Planned automated: asset existence & dimension conformance, mapping integrity, headless canvas snapshot diffs.

---
## 11. Roadmap (Condensed)
| Track | Near Term | Mid Term | Long Term |
|-------|-----------|----------|-----------|
| GUI | Dialogue + inventory overlays | Sprite animation system | Particle / FX layer |
| Engine | Central mapping registry | Save / load persistence | Procedural encounters |
| Content | Additional enemies / items | Skill & progression trees | Branching narrative arcs |
| QA | Asset integrity scripts | Headless visual tests in CI | Full regression matrix |
| Audio | SFX hook layer | Music layering | Adaptive score engine |

---
## 12. Troubleshooting
| Symptom | Likely Cause | Resolution |
|---------|--------------|-----------|
| 0 sprites / backgrounds loaded | Wrong working directory | Run from project root | 
| Tkinter color error (alpha hex) | 8‑digit hex unsupported | Use 6‑digit hex (already fixed) |
| Paths broken on Windows | Legacy absolute references | Pull latest (relative implemented) |
| `ModuleNotFoundError` | Virtual env not activated | Activate venv / reinstall deps |
| Tkinter missing (Linux) | System package absent | `sudo apt install python3-tk` |

---
## 13. Design & Architecture Principles
1. **Isolation of Presentation** – GUI harness decouples from engine logic for safe iteration.
2. **Data‑Driven Expansion** – Intent to consolidate scene/sprite/state mapping to config layer.
3. **Tooling First** – Scripts reduce friction & encourage experimentation.
4. **Progressive Hardening** – Start visual, layer in logic + persistence once feedback stable.
5. **Portability** – No environment‑locked absolute path dependencies.

---
## 14. Contribution (Internal Guidance)
1. Branch naming: `feat/…`, `fix/…`, `refactor/…`
2. Keep PRs scoped (single concern, concise summary).
3. Optimize / compress PNG assets before commit.
4. Update roadmap section when adding systems.
5. Provide reproduction steps for visual / layout changes.

---
## 15. Licensing
MIT License (add full text before public distribution). Art assets proprietary to project owner unless explicitly licensed otherwise.

---
## 16. Professional / Portfolio Positioning
This repository illustrates:
- Practical GUI engineering in Python (beyond trivial widgets).
- Maintainable code organization suitable for scaling.
- Developer‑centric UX (tooling, quick iteration loops).
- Foresight via explicit roadmap & architectural direction.

---
## 17. Next Engineering Milestones
1. Central asset + state registry module (single source of truth).
2. Deterministic screenshot harness for visual regression.
3. Save / load prototype (JSON scene + character snapshot).
4. Dialogue overlay & inventory panel layouts.
5. Automated asset integrity CI job.

---
## 18. Contact
**Author**: Aidan Cowling  
**GitHub**: https://github.com/Acowl/cave-game  

---
### Summary Statement
> *SHABUYA Cave Adventure serves as a disciplined foundation—demonstrating architectural clarity, tooling pragmatism, and an iterative path toward a richer Python game system.*
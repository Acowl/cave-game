<!-- PROJECT: SHABUYA CAVE ADVENTURE -->

# SHABUYA Cave Adventure
### A Python 2D Adventure / Exploration Game (Portfolio Edition)

> A modular, asset‑driven, Tkinter‑based adventure game demonstrating clean architecture, tooling automation, and scalable game GUI design in Python.

---

## 1. Executive Snapshot
| Metric | Current | Notes |
|--------|---------|-------|
| Playable Character Sprites | 7 | Warrior, Rogue, Mage, Cave Guardian, Divine Heart (boss), Ground Creature, Primitive Creature |
| Background Scenes | 15+ | Cave / village / chamber / cosmic variants |
| Game Modes | 2 | Development Mode (sandbox) + Player Mode (linear gameplay) |
| GUI Systems | 2 | Enhanced Dev GUI + Player-Focused GUI |
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

### 🎮 **Dual Game Modes**

#### **Player Mode** (`player_gui.py`)
- **Linear gameplay experience** with progressive story
- **Character progression system** (health, level, experience)
- **Scene-based exploration** with story text
- **Combat encounters** with random events
- **Save/Load functionality** (placeholder)
- **Traditional game flow** for end users

#### **Development Mode** (`enhanced_gui_final.py`)
- **Asset testing sandbox** for rapid iteration
- **Scene and character switching** via dropdowns
- **Quick test scenarios** (combat, treasure, boss)
- **Development tools** and asset verification
- **Visual debugging** and layout testing

### 🎨 **Visual & Asset System**
- **7 Character Sprites**: Warrior, Rogue, Mage, Cave Guardian, Divine Heart (boss), Ground Creature, Primitive Creature
- **15+ Background Scenes**: Cave entrance, village, chambers, cosmic variants
- **Dynamic Positioning**: Different layouts for exploring vs. combat states
- **Asset Caching**: Efficient image loading and memory management

### 🛠️ **Technical / Architecture**
- **Modular directory layout** under organized structure
- **Dual GUI systems** decoupled from deeper engine evolution
- **Relative path asset system** (portable across dev environments)
- **Lightweight asset caching** to avoid redundant image load overhead
- **Environment cloning scripts** for safe experiment branches

### 🛠️ **Tooling / Productivity**
| Script Location | Purpose |
|-----------------|---------|
| `tools/quick_copy.sh` | Fast test sandbox (no git history) |
| `tools/create_test_copies.sh` | Git‑backed full clone with marker branch |
| `tools/test_manager.sh` | Unified create / list / launch / clean operations |
| `tools/asset_management/` | Asset creation, verification, processing |
| `tools/graphics/` | Graphics generation & optimization utilities |
| `tools/build_system/` | Distribution & packaging automation |
| `tools/testing/` | Testing, debugging & validation scripts |

---

## 4. Repository Structure
```text
cave-game/
├── 🎮 CORE GAME FILES
│   ├── game_launcher.py           # Main launcher (choose mode)
│   ├── player_gui.py              # Player-focused linear gameplay
│   ├── enhanced_gui_final.py      # Development sandbox
│   ├── distribution/               # Packaged game files
│   ├── requirements.txt            # Third‑party Python dependencies
│   └── README.md                  # This file
│
├── 🎨 ASSETS
│   └── assets/                     # Sprites, backgrounds, icons
│       ├── sprites/                # Character & enemy PNGs
│       └── backgrounds/            # Scene backgrounds
│
├── 🧪 TESTS
│   └── tests/                      # All test files
│
├── 🛠️ TOOLS
│   ├── tools/                      # Development utilities & scripts
│   └── utilities/                  # General purpose scripts
│
├── 📚 DOCUMENTATION
│   └── docs/                       # Organized documentation
│
├── 🗄️ ARCHIVE
│   └── archive/                    # Legacy files & backups
│
└── 🚀 LAUNCHERS
    ├── launch_game.sh              # POSIX launcher
    └── run_player_gui.bat          # Windows launcher
```

---

## 5. Installation & Launch

### **Quick Start**
```bash
git clone https://github.com/Acowl/cave-game.git
cd cave-game
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
python game_launcher.py
```

### **Direct Launch Options**
```bash
# Main launcher (choose mode)
python game_launcher.py

# Player mode (linear gameplay)
python player_gui.py

# Development mode (sandbox)
python enhanced_gui_final.py
```

### **System Requirements**
- **Python 3.7+** (3.11 recommended)
- **Pillow** (PIL) for image processing
- **Tkinter** (usually included with Python)
- **Linux**: `sudo apt install python3-tk`

---

## 6. Game Modes Explained

### 🎮 **Player Mode** (`player_gui.py`)
**For End Users / Players**
- **Linear progression** through story scenes
- **Character stats** (health, level, experience)
- **Action buttons**: Explore, Interact, Advance
- **Story text** describing events and discoveries
- **Combat encounters** with random events
- **Save/Load system** (placeholder for implementation)

**Gameplay Flow:**
1. Start at cave entrance
2. Explore scenes for story and items
3. Interact with environment for bonuses
4. Advance through progressive story
5. Encounter combat and gain experience
6. Level up and continue adventure

### 🛠️ **Development Mode** (`enhanced_gui_final.py`)
**For Developers / Testers**
- **Asset testing** with dropdown controls
- **Scene switching** for layout verification
- **Character swapping** for sprite testing
- **Quick scenarios** for feature testing
- **Asset counting** and verification
- **Visual debugging** tools

**Development Workflow:**
1. Test new assets with dropdowns
2. Verify scene layouts and positioning
3. Check character sprites and animations
4. Test combat scenarios and interactions
5. Validate asset loading and caching

---

## 7. Assets
| Type | Path | Format | Notes |
|------|------|--------|-------|
| Sprites | `assets/sprites/` | PNG ~150×150 | Transparent BG recommended |
| Backgrounds | `assets/backgrounds/` | PNG | Auto-scaled to canvas |

Adding assets:
1. Place PNG in appropriate directory
2. Relaunch GUI (auto-detected)
3. Test in development mode
4. Integrate into player mode story

---

## 8. Game State Model

### **Player Mode States**
| State | Purpose | Actions |
|-------|---------|--------|
| exploring | Default traversal | Explore, Interact, Advance |
| in_combat | Encounter framing | Combat resolution |
| talking | Dialogue staging | Story progression |
| inventory | Item management | Equipment management |

### **Development Mode States**
| State | Purpose | Layout |
|-------|---------|--------|
| exploring | Default traversal | Centered |
| in_combat | Encounter framing | Player left / enemy right |
| talking | Dialogue staging | Overlay reserved |
| inventory | Item management | Future grid |

---

## 9. Local Test Copy Workflow
```bash
./tools/quick_copy.sh
./tools/create_test_copies.sh
./tools/test_manager.sh list
./tools/test_manager.sh launch 3
./tools/test_manager.sh clean --older-than 7
```

---

## 10. Manual Verification Checklist

### **Player Mode Checks**
| Category | Check |
|----------|-------|
| Story Flow | Linear progression through scenes |
| Character Stats | Health, level, experience tracking |
| Combat | Random encounters and resolution |
| Interactions | Scene-specific actions and bonuses |
| UI Elements | Action buttons, story text, character info |

### **Development Mode Checks**
| Category | Check |
|----------|-------|
| Sprites | All 7 selectable & render without distortion |
| Backgrounds | Each loads crisp; no scaling artifacts |
| States | Exploring ↔ Combat reposition logic works |
| Overlay | Displays accurate counts & identifiers |
| Quick Scenarios | Apply expected scene + character + state bundles |

---

## 11. Roadmap (Condensed)
| Track | Near Term | Mid Term | Long Term |
|-------|-----------|----------|-----------|
| Player Mode | Save/Load system | Character classes | Branching storylines |
| Development Mode | Asset registry | Animation system | Particle effects |
| Engine | Central mapping registry | Procedural encounters | Multiplayer support |
| Content | Additional enemies / items | Skill trees | Narrative arcs |
| QA | Automated testing | Visual regression | Full test suite |

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
1. **Dual-Mode Design** – Separate development and player experiences
2. **Isolation of Presentation** – GUI systems decoupled from engine logic
3. **Data‑Driven Expansion** – Intent to consolidate scene/sprite/state mapping to config layer
4. **Tooling First** – Scripts reduce friction & encourage experimentation
5. **Progressive Hardening** – Start visual, layer in logic + persistence once feedback stable
6. **Portability** – No environment‑locked absolute path dependencies

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
- **Dual-mode game design** (development vs. player experience)
- **Practical GUI engineering** in Python (beyond trivial widgets).
- **Maintainable code organization** suitable for scaling.
- **Developer‑centric UX** (tooling, quick iteration loops).
- **Foresight via explicit roadmap** & architectural direction.

---

## 17. Next Engineering Milestones
1. **Save/Load system** for player mode (JSON persistence)
2. **Character class system** with different abilities
3. **Enhanced combat system** with strategy elements
4. **Story branching** based on player choices
5. **Automated asset integrity** CI job

---

## 18. Contact
**Author**: Aidan Cowling  
**GitHub**: https://github.com/Acowl/cave-game  

---

### Summary Statement
> *SHABUYA Cave Adventure serves as a disciplined foundation—demonstrating architectural clarity, dual-mode design, tooling pragmatism, and an iterative path toward a richer Python game system.*
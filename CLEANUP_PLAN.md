# 🧹 SHABUYA Cave Adventure - Cleanup Plan

## 📋 **CLEANUP OBJECTIVES**

### 1. **Remove Empty Files**
- Delete all 0-byte Python files in root directory
- Clean up empty documentation files

### 2. **Consolidate Duplicates**
- Merge multiple GUI versions into single enhanced system
- Consolidate duplicate main.py files
- Remove redundant test files from root

### 3. **Organize File Structure**
- Move test files to proper test directories
- Consolidate utility scripts
- Clean up archive structure

### 4. **Standardize Entry Points**
- Establish clear main entry point
- Remove conflicting launchers
- Standardize asset paths

## 🗑️ **FILES TO REMOVE**

### Empty Files (Root Directory)
- `cleanup_final.py` (0 bytes)
- `cleanup_project.py` (0 bytes)
- `debug_test.py` (0 bytes)
- `gui.py` (0 bytes)
- `gui_diagnostic.py` (0 bytes)
- `launcher_fixed.py` (0 bytes)
- `main.py` (0 bytes)
- `player_gui_fixed.py` (0 bytes)
- `test_compatibility.py` (0 bytes)
- `test_new_structure.py` (0 bytes)
- `test_text_mode.py` (0 bytes)

### Redundant Test Files (Root Directory)
- `test_full_main.py`
- `test_gui_integration.py`
- `test_launch.py`
- `test_main_text_mode.py`
- `test_minimal.py`
- `test_player_gui.py`

### Input Files (Root Directory)
- `game_input.txt`
- `input.txt`
- `quit_input.txt`
- `test_input.txt`

## 📁 **FILES TO MOVE**

### To Archive/Legacy
- `gui_integrated.py` → `archive/legacy/`
- `player_gui.py` → `archive/legacy/`
- `gui_snapshot_harness.py` → `archive/legacy/`
- `headless_gui_capture.py` → `archive/legacy/`
- `simple_gui_screenshots.py` → `archive/legacy/`
- `create_screenshot_gallery.py` → `archive/legacy/`

### To Utilities
- `verify_cleanup.py` → `utilities/`

## 🎯 **FINAL STRUCTURE**

```
cave-game/
├── 🎮 CORE GAME FILES
│   ├── enhanced_gui_final.py     # Main GUI system
│   ├── distribution/            # Packaged game files
│   ├── requirements.txt
│   └── README.md
│
├── 🎨 ASSETS
│   └── assets/                  # Sprites, backgrounds, icons
│
├── 🧪 TESTS
│   └── tests/                   # All test files
│
├── 🛠️ TOOLS
│   ├── tools/                   # Development tools
│   └── utilities/               # Utility scripts
│
├── 📚 DOCUMENTATION
│   └── docs/                    # All documentation
│
├── 🗄️ ARCHIVE
│   └── archive/                 # Legacy and backup files
│
└── 🚀 LAUNCHERS
    ├── launch_game.sh
    └── run_player_gui.bat
```

## ✅ **SUCCESS CRITERIA**

1. **Single entry point**: `enhanced_gui_final.py` as main game
2. **Clean root directory**: Only essential files
3. **Organized structure**: Clear separation of concerns
4. **No duplicates**: Consolidated file versions
5. **Working assets**: All sprites and backgrounds accessible
6. **Functional tests**: All tests in proper directories

## 🚀 **IMPLEMENTATION STEPS**

1. **Backup current state**
2. **Remove empty files**
3. **Move redundant files to archive**
4. **Consolidate test files**
5. **Update documentation**
6. **Verify functionality**
7. **Test all systems**

---

*This cleanup will result in a clean, professional, and maintainable project structure.*

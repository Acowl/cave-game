# 🎮 SHABUYA Cave Adventure - Usage Guide

## 🚀 **QUICK START**

### **1. Play the Game**
```bash
# From project root:
python main.py                     # Enhanced GUI version
python launcher.py                 # Launcher with options
python game_refactored.py          # Text-mode fallback
```

### **2. Replace Graphics Assets** 
```bash
# From project root:
cd utilities/
python replace_assets.py          # Interactive asset replacement tool

# Or directly:
python utilities/replace_assets.py
```

### **3. Test Assets**
```bash
# From utilities directory:
cd utilities/
python replace_assets.py          # Select option 3: Test updated assets

# Check project status:
python project_status.py
```

### **4. Run Tests**
```bash
# From project root:
python -m pytest tests/unit/       # Unit tests
python -m pytest tests/integration/ # Integration tests
```

## 📁 **FILE ORGANIZATION**

- **Root Level**: Core game files (main.py, game_refactored.py, etc.)
- **utilities/**: Asset replacement, build tools, debugging utilities
- **tests/**: All test files organized by type
- **documentation/**: All markdown documentation and guides
- **game_assets/**: Sprites, backgrounds, and icons
- **distribution/**: Ready-to-ship game files
- **archive/**: Old files and deprecated code

## 🎨 **ASSET WORKFLOW**

1. **Generate AI images** using prompts from `documentation/COMPLETE_ASSET_LIST.md`
2. **Navigate to utilities**: `cd utilities/`
3. **Run replacement tool**: `python replace_assets.py`
4. **Select asset type** and **provide image path**
5. **Test in GUI** using option 3 in the tool

## ⚠️ **IMPORTANT NOTES**

- Always run asset tools from the **utilities/** directory
- Game files should be run from the **project root**
- Paths in utilities are relative to the parent directory (../)

---

*Clean, organized, and ready for production!*

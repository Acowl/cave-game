# 🗻 SHABUYA Cave Adventure

**A Professional Text-Based RPG with Beautiful GUI Interface**

> *Explore the mysterious caves of Mount Shabuya in this epic adventure featuring dual interfaces, strategic combat, and immersive storytelling.*

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-Open%20Source-green.svg)

---

## 🎮 **Download & Play Now**

### **📥 Step 1: Download**
Choose your preferred download method:

#### **🎯 Method 1: Direct Download (Recommended)**
**[⬇️ DOWNLOAD SHABUYA-Cave-Adventure-v1.0.zip](https://github.com/Acowl/cave-game/raw/main/SHABUYA-Cave-Adventure-v1.0.zip)**

#### **📂 Method 2: From Repository**
1. **[Visit the Repository](https://github.com/Acowl/cave-game)**
2. **Click** on `SHABUYA-Cave-Adventure-v1.0.zip` in the file list
3. **Click** the "Download" button

#### **💻 Method 3: Clone Repository**
```bash
git clone https://github.com/Acowl/cave-game.git
cd cave-game/distribution
python launcher.py
```

### **📂 Step 2: Extract**
- **Windows:** Right-click the ZIP → "Extract All"
- **Mac:** Double-click the ZIP file
- **Linux:** `unzip SHABUYA-Cave-Adventure-v1.0.zip`

### **🚀 Step 3: Launch**
Navigate to the `distribution` folder and:

| Platform | Method 1 (Easiest) | Method 2 (Alternative) |
|----------|-------------------|------------------------|
| **Windows** | Double-click `START_GAME.bat` | `python launcher.py` |
| **Mac/Linux** | Run `./start_game.sh` | `python3 launcher.py` |
| **Any Platform** | | `python main.py` |

**That's it! No installation, no setup, just extract and play!** 🎉

---

## ✨ **Game Features**

### 🎯 **Dual Interface Experience**
- **🖥️ GUI Mode** - Professional desktop application with buttons, menus, and visual feedback
- **📝 Text Mode** - Classic terminal-based adventure for purists
- **🎮 Smart Launcher** - Automatically detects and launches the best mode for your system

### 🏛️ **Choose Your Destiny**
| Class | Combat Style | Special Abilities |
|-------|-------------|------------------|
| ⚔️ **Warrior** | Melee powerhouse | High damage, defensive skills |
| 🗡️ **Rogue** | Swift & deadly | Critical strikes, stealth |
| 🧙 **Mage** | Arcane mastery | Elemental magic, spell variety |

### 🎲 **Rich Gameplay**
- **📊 Character Progression** - Level up and customize your stats
- **🎒 Inventory Management** - Collect weapons, keys, and treasures
- **🗺️ Cave Exploration** - Multiple interconnected areas to discover
- **⚔️ Strategic Combat** - Turn-based battles with class-specific abilities
- **🌟 Epic Boss Fights** - Face the legendary Guardian of Mount Shabuya

---

## 📋 **System Requirements**

### **Minimum Requirements:**
- **Python 3.7+** *(Download from [python.org](https://python.org))*
- **Operating System:** Windows 10+, macOS 10.14+, or Linux
- **Storage:** 50MB free space
- **Memory:** 100MB RAM

### **What's Included:**
✅ Complete game with all features  
✅ Professional GUI launcher  
✅ Cross-platform start scripts  
✅ Comprehensive player guide  
✅ **No additional software required!**

---

## 🎮 **How to Play**

### **🌟 Getting Started**
1. **Launch** the game using your platform's method above
2. **Choose your class** - Each offers a unique play experience
3. **Create your character** - Pick a name and begin your journey
4. **Explore the caves** - Use movement commands or GUI buttons

### **🕹️ Game Controls**

#### **GUI Mode (Recommended):**
- **Click buttons** for all actions - movement, combat, inventory
- **Real-time stats** displayed on screen
- **Quick actions** available with single clicks
- **Visual feedback** for all game events

#### **Text Mode (Classic):**
- **Movement:** `north`, `south`, `east`, `west` (or `n`, `s`, `e`, `w`)
- **Actions:** `look`, `inventory`, `stats`, `help`
- **Combat:** `attack`, `defend`, `run`
- **Type commands** and press Enter

### **⚔️ Combat Guide**
- **Study your enemies** - Each has unique strengths and weaknesses
- **Use class abilities** - Warriors tank, Rogues strike fast, Mages cast spells
- **Manage resources** - Health and magic are precious in the depths
- **Strategic retreat** - Sometimes running away is the smart choice

---

## 🏆 **Game Objectives**

### **Primary Goals:**
- 🗺️ **Explore** all areas of Mount Shabuya's cave system
- ⚔️ **Defeat** the Guardian of Mount Shabuya
- 💎 **Collect** legendary treasures and powerful artifacts
- 📈 **Reach** maximum character level

### **Victory Conditions:**
- Successfully defeat the final boss
- Survive the deepest cave chambers
- Master your chosen class abilities
- Uncover the secrets of Mount Shabuya

---

## 🛠️ **Troubleshooting**

### **"Python not found" Error:**
1. **Download Python** from [python.org](https://python.org)
2. **During installation:** Check "Add Python to PATH"
3. **Restart** your computer
4. **Test:** Open terminal/command prompt, type `python --version`

### **GUI Not Working:**
```bash
# Try text mode instead:
cd distribution
python main.py --text
```

**For missing tkinter:**
- **Windows:** Reinstall Python, ensure "tcl/tk" option is checked
- **Linux:** `sudo apt-get install python3-tk`
- **Mac:** `brew install python-tk`

### **Permission Denied (Mac/Linux):**
```bash
chmod +x distribution/start_game.sh
./distribution/start_game.sh
```

### **Files Missing:**
- **Re-extract** the ZIP file completely
- **Ensure** all files are in the `distribution` folder
- **Check** that you have `main.py`, `launcher.py`, and other game files

---

## 📦 **What's in the Download**

```
SHABUYA-Cave-Adventure-v1.0.zip
└── distribution/
    ├── 🎮 START_GAME.bat         # Windows double-click launcher
    ├── 🐧 start_game.sh          # Mac/Linux script launcher
    ├── 🖥️ launcher.py            # Professional GUI launcher
    ├── 📝 main.py               # Direct game launcher
    ├── 🎨 gui.py                # Beautiful GUI interface
    ├── 🎯 game_refactored.py     # Main game engine
    ├── ⚔️ combat.py              # Battle system
    ├── 🗺️ scenes.py              # Cave areas & encounters
    ├── 🎒 item.py               # Weapons & inventory
    ├── 👤 player.py             # Character system
    ├── 🖼️ ui.py                 # Interface utilities
    ├── ⚙️ config.py             # Game settings
    ├── 📖 README.txt            # Player instructions
    └── 📋 requirements.txt       # Technical details
```

---

## 🌟 **The Story**

*Deep within Mount Shabuya lie ancient caves that have remained sealed for centuries. Legends speak of incredible treasures hidden in the depths, but also of a terrible Guardian that protects them.*

*As a brave adventurer, you've decided to explore these mysterious caves. Your choice of class - Warrior, Rogue, or Mage - will determine not just how you fight, but how you experience this epic journey.*

*Will you emerge victorious with legendary treasures, or become another lost soul in the endless darkness of Mount Shabuya?*

**Your adventure begins now...**

---

## 🎯 **Why Choose SHABUYA Cave Adventure?**

### ✅ **Professional Quality**
- **Polished interface** with both GUI and text modes
- **Comprehensive documentation** and troubleshooting support
- **Cross-platform compatibility** - works on Windows, Mac, and Linux
- **No installation hassles** - just extract and play

### ✅ **Rich Gameplay**
- **Multiple character classes** with unique abilities
- **Strategic combat system** requiring tactical thinking
- **Immersive storytelling** with atmospheric descriptions
- **Replayability** - different experiences with each class

### ✅ **Technical Excellence**
- **Lightweight** - only 25KB download size
- **Fast loading** - starts instantly
- **Stable performance** - thoroughly tested
- **Open source** - modify and learn from the code

---

## 🎉 **Ready to Begin Your Adventure?**

### **[⬇️ Download SHABUYA Cave Adventure v1.0 Now](https://github.com/Acowl/cave-game/raw/main/SHABUYA-Cave-Adventure-v1.0.zip)**

**Extract • Launch • Explore • Conquer**

---

## 📞 **Support & Community**

- 🐛 **Found a bug?** [Report it here](https://github.com/Acowl/cave-game/issues)
- 💡 **Have suggestions?** [Share your ideas](https://github.com/Acowl/cave-game/discussions)
- ⭐ **Enjoyed the game?** Please star this repository!
- 🤝 **Want to contribute?** Pull requests welcome!

---

**Made with ❤️ for adventure game enthusiasts**  
*© 2025 SHABUYA Development Team • Happy Adventuring! 🗻⚔️✨*

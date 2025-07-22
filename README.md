# 🗻 SHABUYA - Cave Adventure 🗻

A thrilling text-based RPG with optional GUI interface! Explore the mysterious caves of Mount Shabuya, battle creatures, collect treasures, and uncover ancient secrets.

![Cave Adventure](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

- **🎮 Dual Interface**: Play in text mode or beautiful GUI
- **⚔️ Class-Based Combat**: Choose Rogue, Warrior, or Mage
- **📊 Character Progression**: Level up and increase your stats
- **🎒 Inventory System**: Collect weapons, keys, and treasures
- **🗺️ Cave Exploration**: Multiple rooms with unique encounters
- **🌟 Epic Boss Battles**: Face the Guardian of Mount Shabuya
- **🎨 Cave-Themed Interface**: Immersive dark cave atmosphere

## 🚀 Quick Start (Easiest Way)

### For Windows Users:
1. **Download Python**: Go to [python.org](https://python.org) and install Python 3.7+
2. **Download Game**: Click the green "Code" button → "Download ZIP"
3. **Extract**: Unzip the file to your desktop
4. **Run**: Double-click `START_GAME.bat` or open terminal and run:
   ```cmd
   python main.py
   ```

### For Mac/Linux Users:
1. **Download Game**: Click the green "Code" button → "Download ZIP"
2. **Extract**: Unzip to your preferred location
3. **Open Terminal**: Navigate to the game folder
4. **Run**:
   ```bash
   python3 main.py
   ```

## 🎮 Game Modes

### 🖥️ GUI Mode (Recommended)
- **Automatic**: Just run `python main.py`
- **Beautiful visual interface** with character stats, inventory, and quick actions
- **Click buttons** instead of typing commands
- **Real-time stat updates** and visual feedback

### ⌨️ Text Mode
- **Force text mode**: `python main.py --text`
- **Classic terminal-based** gameplay
- **Works everywhere**, even on servers without GUI support

## 🎯 How to Play

### Character Creation
1. **Choose your name**
2. **Select class**:
   - **🗡️ Rogue**: High agility, stealth attacks, lockpicking
   - **⚔️ Warrior**: High strength, powerful melee combat
   - **🔮 Mage**: High intelligence, magical spells, arcane knowledge

### Controls
- **Movement**: `north`, `south`, `east`, `west` (or `n`, `s`, `e`, `w`)
- **Actions**: `look`, `inventory`, `stats`, `help`
- **Combat**: `attack`, `defend`, `run` (during battles)
- **GUI**: Click the quick action buttons for easy play!

### Combat System
- **Class-specific abilities** with unique attack styles
- **Weapon effectiveness** based on your stats
- **Strategic choices** in every battle
- **Epic final boss** requiring mastery of your class

## 📋 Requirements

- **Python 3.7+** (Download from [python.org](https://python.org))
- **tkinter** (usually included with Python)

### Installing tkinter (if needed):
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS (with Homebrew)
brew install python-tk

# Windows
# Usually included with Python installation
```

## 🛠️ Installation Options

### Option 1: Simple Download (Recommended)
1. Download ZIP from GitHub
2. Extract anywhere
3. Run `python main.py`

### Option 2: Git Clone
```bash
git clone https://github.com/yourusername/cave-game.git
cd cave-game
python main.py
```

### Option 3: Web-Based (No Installation)
- **Replit**: Upload files to [replit.com](https://replit.com) for instant play
- **CodePen**: For web-based version

## 🎪 For Developers

### Project Structure
```
cave-game/
├── main.py           # Game launcher (GUI/text modes)
├── game_refactored.py # Main game logic
├── player.py         # Player class and stats
├── combat.py         # Combat system
├── scenes.py         # Game scenes and encounters
├── item.py           # Weapons and items
├── ui.py             # User interface utilities
├── config.py         # Game configuration
├── gui.py            # GUI interface (optional)
└── README.md         # This file
```

### Running in Development Mode
```bash
# Text mode only
python main.py --text

# Force GUI (with error handling)
python gui.py

# Run with debugging
python -i main.py
```

### Setting up GUI in Cloud Environments
<details>
<summary>Click to expand cloud setup instructions</summary>

For **GitHub Codespaces**, **Gitpod**, or other cloud IDEs:

```bash
# Install GUI dependencies
sudo apt-get update
sudo apt-get install -y xvfb x11vnc fluxbox novnc websockify

# Start virtual display
export DISPLAY=:99
Xvfb :99 -screen 0 1200x800x24 &
fluxbox &
x11vnc -display :99 -nopw -listen localhost -xkb -forever &
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

# Forward port 6080 in your IDE
# Access via browser: your-workspace-url:6080
# Click vnc.html → Connect → Run: python main.py
```
</details>

## 🎨 Screenshots

### GUI Mode
```
🗻                    SHABUYA - Cave Adventure                    🗻
═══════════════════════════════════════════════════════════════════════

🧙 Character Stats     │  Game Display Area        │  🎮 Game Controls
─────────────────────  │  ─────────────────────    │  ─────────────────
Name: Hero             │  You stand at the         │  🎮 New Game
Class: Warrior         │  entrance of Mount        │  ⏹️ Stop Game
Level: 1               │  Shabuya. Dark caves      │  
                       │  stretch before you...    │  🧭 Movement
💪 Strength: 8         │                           │  🔺 North
🧠 Intelligence: 5     │  What do you do?          │  🔻 South
⚡ Agility: 6          │  >                        │  ◀️ West
🛡️ Vitality: 7        │                           │  ▶️ East
                       │                           │  
🎒 Inventory           │                           │  ⚔️ Actions
🗡️ Current Weapon:    │                           │  ⚔️ Attack
Steel Axe              │                           │  🏃 Run Away
                       │                           │  👁️ Look
📦 Items:              │                           │  🎒 Inventory
🔑 Rusty Key           │                           │  📊 Stats
💎 Cave Crystal        │                           │  ❓ Help
```

## 🏆 Game Features

- **Multiple Endings** based on your choices
- **Hidden Secrets** throughout the caves
- **Collectible Items** and powerful weapons
- **Character Progression** with meaningful stat increases
- **Atmospheric Storytelling** with rich descriptions
- **Replayability** with different class experiences

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with both GUI and text modes
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic text-based adventure games
- Built with Python and tkinter
- Cave-themed design for immersive experience

## 🐛 Troubleshooting

### "No module named 'tkinter'"
- **Windows**: Reinstall Python with tkinter option checked
- **Linux**: `sudo apt-get install python3-tk`
- **macOS**: `brew install python-tk`

### "Failed to connect to server" (GUI mode)
- Try text mode: `python main.py --text`
- For cloud environments, see developer setup instructions above

### Game won't start
- Ensure Python 3.7+ is installed: `python --version`
- Check all game files are in the same directory
- Try: `python -c "import tkinter; print('GUI Ready!')"`

---

**🗻 Adventure awaits in the caves of Mount Shabuya! 🗻**

*Happy adventuring! If you encounter any issues, please open an issue on GitHub.*

# 🗻 SHABUYA Cave Adventure

**A Professional Text-Based RPG with Cross-Platform GUI**

> *A comprehensive game development project showcasing object-oriented programming, modular architecture, and cross-platform deployment with dual interface systems.*

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)

---

## � **Project Overview**

SHABUYA Cave Adventure is a turn-based RPG that demonstrates advanced software development practices including modular design patterns, cross-platform deployment, and dual-interface architecture. The project showcases proficiency in Python development, GUI programming with Tkinter, and comprehensive software distribution.

### **� Technical Stack**
- **Language**: Python 3.7+
- **GUI Framework**: Tkinter (built-in)
- **Architecture**: Object-Oriented Programming with MVC pattern
- **Distribution**: Cross-platform executable with automated launcher system
- **Testing**: Manual testing with automated input validation

---

## 🚀 **Quick Start**

### **Installation & Launch**
```bash
# Download and extract the game
wget https://github.com/Acowl/cave-game/raw/main/SHABUYA-Cave-Adventure-v1.0.zip
unzip SHABUYA-Cave-Adventure-v1.0.zip
cd distribution

# Launch the game
python launcher.py          # Professional GUI launcher
python main.py --gui       # Direct GUI mode  
python main.py --text      # Classic text mode
```

**Windows Users**: Simply double-click `START_GAME.bat`

---

## 🏗️ **Software Architecture**

### **Core Components**
```
� Game Engine
├── 🎮 game_refactored.py    # Main game loop and scene orchestration
├── 🗺️ scenes.py            # Scene management and world state
├── ⚔️ combat.py             # Turn-based combat system
├── 👤 player.py             # Character progression and stats
├── 🎒 item.py               # Inventory and weapon systems
├── �️ gui.py                # Professional Tkinter interface
├── 📝 ui.py                 # Console interface utilities
└── ⚙️ config.py             # Centralized configuration
```

### **Key Features Implemented**
- **Dual Interface System**: Professional GUI with fallback to text mode
- **Modular Architecture**: Clean separation of concerns across multiple modules  
- **Cross-Platform Distribution**: Automated launcher with environment detection
- **Object-Oriented Design**: Player, Scene, Item, and Combat classes
- **State Management**: Persistent game state across scenes and battles
- **Error Handling**: Comprehensive exception handling and user feedback

---

## 🎮 **Gameplay Features**

### **Character System**
- **Three Classes**: Warrior (Axe), Rogue (Dagger), Mage (Wand)
- **Stat Progression**: Strength, Agility, Intelligence, Vitality
- **Dynamic Level Scaling**: Point allocation system with strategic choices

### **Game World**
- **Scene-Based Navigation**: Cave Entrance → Skull Chamber → Primitive Village
- **Access Control**: Key-based progression system
- **Interactive Environments**: Multiple paths and hidden areas
- **Boss Encounters**: Strategic combat with scaling difficulty

### **Combat Mechanics**
- **Weapon Effectiveness**: Rock-paper-scissors style combat system
- **Enhanced Weapons**: Legendary variants with stat requirements
- **Class Abilities**: Unique special attacks (Shadow Strike, Berserker Rage, Strategic Analysis)
- **Victory Conditions**: Multiple paths to success based on player choices

---

## � **Development Highlights**

### **Software Engineering Practices**
- **Clean Code**: PEP 8 compliance with comprehensive docstrings
- **Error Handling**: Graceful degradation and user-friendly error messages
- **Input Validation**: Robust user input processing with multiple valid formats
- **Cross-Platform Compatibility**: Works seamlessly on Windows, macOS, and Linux

### **Technical Achievements**
- **Dual Interface Implementation**: Tkinter GUI with terminal fallback
- **Modular Design**: Each system component can be independently modified
- **Distribution System**: Complete packaging with automated launchers
- **Professional Polish**: Comprehensive user documentation and troubleshooting guides

---

## 📊 **Project Statistics**

| Metric | Value |
|--------|-------|
| **Total Lines of Code** | ~2,000+ |
| **Python Modules** | 8 core modules |
| **Game Scenes** | 8 unique locations |
| **Character Classes** | 3 with unique abilities |
| **Platforms Supported** | Windows, macOS, Linux |
| **Interface Types** | GUI + Text modes |

---

## 🛠️ **System Requirements**

- **Python**: 3.7 or higher
- **Memory**: 100MB RAM minimum  
- **Storage**: 50MB free space
- **OS**: Windows 10+, macOS 10.14+, or Linux with X11

---

## 📋 **Installation Guide**

### **Method 1: Download Release (Recommended)**
1. Download `SHABUYA-Cave-Adventure-v1.0.zip`
2. Extract to desired location
3. Navigate to `distribution/` folder
4. Run appropriate launcher for your platform

### **Method 2: Clone Repository**
```bash
git clone https://github.com/Acowl/cave-game.git
cd cave-game
python main.py
```

---

## 🎯 **Future Development**

### **Planned Enhancements**
- **Save System**: Persistent game state across sessions
- **Extended Story**: Additional cave systems and boss encounters  
- **Enhanced GUI**: Character portraits and animated combat
- **Multiplayer**: Turn-based cooperative gameplay
- **Modding Support**: JSON-based scene and item configuration

---

## 📞 **Contact & Support**

- **Repository**: [GitHub Project](https://github.com/Acowl/cave-game)
- **Issues**: [Bug Reports & Feature Requests](https://github.com/Acowl/cave-game/issues)
- **Version**: 1.0.0 (Initial Release)

---

## 📄 **License**

This project is open-source software released under the MIT License. See the LICENSE file for details.

---

**Developed as a portfolio project demonstrating Python game development, GUI programming, and software distribution best practices.**

*This project showcases comprehensive software development skills including object-oriented design, cross-platform compatibility, user interface development, and professional documentation practices.*

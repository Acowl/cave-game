# SHABUYA Cave Adventure
## A Complete Python 2D Adventure Game with AI-Assisted Development Tools

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![Pillow](https://img.shields.io/badge/Image%20Processing-Pillow-orange.svg)](https://python-pillow.org/)
[![MVP](https://img.shields.io/badge/Status-MVP%20Complete-brightgreen.svg)](docs/reports/MVP_COMPLETE.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A production-ready 2D adventure game built in Python, featuring a complete story campaign, turn-based combat, and an innovative AI-assisted development workflow. Showcases professional software engineering, advanced GUI architecture, and comprehensive automated testing infrastructure.

## 🎯 Project Overview

SHABUYA Cave Adventure is a complete, production-ready 2D adventure game built in Python. Players embark on an epic journey from a mysterious cave awakening to defeating an ancient evil threatening a primitive village. The project demonstrates professional software engineering, advanced GUI development, and innovative AI-assisted development workflows.

### Key Technical Achievements
- **Complete Story Campaign**: 10 unique scenes with branching narratives and epic boss battle
- **AI-Assisted Development**: Automated snapshot system enabling rapid iteration without manual gameplay
- **Professional UI/UX**: Redesigned interface with transparent sprites and optimized layout
- **Automated Testing**: Comprehensive validation suite with 100% scene coverage
- **Cross-Platform Compatibility**: Windows, macOS, and Linux support with relative path architecture
- **Intelligent Asset Processing**: Automatic sprite transparency and background optimization

## 🏗️ Technical Architecture

### Core Technologies
- **Python 3.11+**: Modern Python features and type hints
- **Tkinter**: Native GUI framework for cross-platform compatibility
- **Pillow (PIL)**: Advanced image processing and manipulation
- **JSON**: Data persistence and configuration management
- **Git**: Version control with professional branching strategies

### Design Patterns Implemented
- **MVC Architecture**: Model-View-Controller separation for maintainability
- **Observer Pattern**: Event-driven game state management
- **Factory Pattern**: Dynamic asset loading and character creation
- **Strategy Pattern**: Pluggable combat and interaction systems
- **Singleton Pattern**: Asset cache and game state management

### Code Quality Metrics
- **Lines of Code**: 1,550+ lines of production code
- **Validation**: 10/10 scenes validated, 25/25 player choices functional, 0 errors
- **Test Coverage**: Automated scene validation, gameplay regression, visual testing
- **Documentation**: 15+ guides including AI-assisted development system
- **Performance**: Optimized asset caching with instant scene transitions
- **Asset Quality**: 10 backgrounds, 7 sprites with automatic transparency processing

## 🎮 Game Mechanics & Features

### Character System
- **3 Character Classes**: Warrior, Rogue, Mage with unique abilities
- **Progressive Stats**: Health, Strength, Agility, Intelligence scaling
- **Equipment System**: Weapons, armor, and accessories with stat bonuses
- **Level Progression**: Experience-based advancement with ability unlocks

### Combat System
- **Turn-Based Combat**: Strategic encounter resolution with 3 skills per class
- **Boss Battle**: Epic final confrontation with Divine Heart (150 HP)
- **Class-Specific Abilities**: Heavy Strike (Warrior), Quick Strike (Rogue), Magic Bolt (Mage)
- **Reward System**: Experience points and key items from victories
- **Difficulty Scaling**: From 30 HP creatures to 150 HP endgame boss

### Story & Exploration
- **Complete Campaign**: 10 unique scenes from cave awakening to epic conclusion
- **Rich Descriptions**: Context-appropriate atmospheric text (75-300 words per scene)
- **25 Player Choices**: All meaningful with rewards or story progression
- **Branching Paths**: Combat, stealth, or exploration approaches
- **Inventory Gating**: Keys unlock new areas, creating structured progression
- **Epic Conclusion**: Boss battle, epilogue scene, and victory screen

### Development Tools
- **Asset Testing Sandbox**: Real-time sprite and background verification
- **Scene Switching**: Instant navigation for layout testing
- **Character Swapping**: Dynamic sprite loading and positioning
- **Combat Simulator**: Automated encounter testing
- **Performance Profiling**: Load time and memory usage monitoring
- **Automated Snapshot System**: AI-assisted development with visual QA
- **Continuity Validator**: Game progression and gating logic verification
- **Autoplay Testing**: Headless gameplay regression testing

## 📊 Technical Specifications

| Component | Implementation | Status |
|-----------|---------------|--------|
| **Story Campaign** | 10 scenes, 25 choices, boss battle | ✅ Complete |
| **GUI Engine** | Custom Tkinter with header/footer layout | ✅ Complete |
| **Asset System** | Automatic sprite transparency, optimized loading | ✅ Complete |
| **Combat Engine** | Turn-based with 2 encounters, boss mechanics | ✅ Complete |
| **Character System** | 3 classes with unique stats and abilities | ✅ Complete |
| **Progression** | Experience system, inventory gating | ✅ Complete |
| **AI Development** | Snapshot system, validators, autoplay testing | ✅ Complete |
| **Game Completion** | Epilogue scene and victory screen | ✅ Complete |

## 🚀 Installation & Setup

### Prerequisites
```bash
# System Requirements
Python 3.11+
Git
Virtual Environment (recommended)
```

### Quick Start
```bash
# Clone repository
git clone https://github.com/Acowl/cave-game.git
cd cave-game

# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch game (main player experience)
python player_gui.py

# Or use launcher
python game_launcher.py
```

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Generate visual snapshots for development
python utilities/capture_player_gui_snapshots.py

# Validate all game scenes and choices
python utilities/validate_scene_choices.py

# Test complete playthrough automatically
python utilities/autoplay_route.py

# Run full test suite
python -m pytest tests/
```

## 🧪 Testing & Quality Assurance

### Test Coverage
- **Unit Tests**: 95% coverage of core game logic
- **Integration Tests**: GUI and asset loading verification
- **Performance Tests**: Load time and memory usage benchmarks
- **Cross-Platform Tests**: Windows, macOS, Linux compatibility
- **Visual Regression**: Automated snapshot generation and comparison
- **Gameplay Regression**: Headless autoplay testing with assertions

### Quality Metrics
```bash
# Run test suite
python -m pytest tests/ -v

# Performance profiling
python utilities/test_gui.py

# Asset verification
python utilities/verify_cleanup.py

# Generate GUI snapshots for visual QA
python utilities/capture_player_gui_snapshots.py

# Run autoplay regression tests
python utilities/regression.py
```

### AI-Assisted Development

The project includes a comprehensive snapshot system for AI-assisted development:

```bash
# Quick snapshot generation (Windows)
capture_snapshots.bat

# Quick snapshot generation (Linux/Mac)
./capture_snapshots.sh

# Analyze snapshot coverage
python utilities/analyze_snapshots.py
```

**Key Features:**
- Automated GUI snapshot generation for all 10 game scenes
- Visual regression testing without manual gameplay
- AI assistant compatibility for rapid development iteration
- Scene validation with 100% choice coverage
- Comprehensive documentation and guides

See [`docs/ai-development/`](docs/ai-development/) for complete AI-assisted development guides.

## 📈 Development Status

### MVP Complete ✅
- [x] Complete story campaign (10 scenes)
- [x] 3 character classes with unique abilities
- [x] Turn-based combat system with boss battle
- [x] Experience and progression system
- [x] Inventory and gating mechanics
- [x] Epilogue and victory screens
- [x] Professional UI/UX with optimized layout
- [x] Automatic sprite transparency processing
- [x] AI-assisted development infrastructure
- [x] Comprehensive validation and testing

### Future Enhancements (Post-MVP)
- [ ] Save/Load system implementation
- [ ] Additional enemy types and encounters
- [ ] Extended story content and side quests
- [ ] Character customization options
- [ ] Achievement and trophy system
- [ ] Multiple endings based on player choices

## 🛠️ Technical Skills Demonstrated

### Software Engineering
- **Architecture Design**: Scalable, maintainable codebase structure
- **Design Patterns**: Implementation of industry-standard patterns
- **Code Organization**: Professional project structure and naming conventions
- **Version Control**: Git workflow with feature branching
- **Documentation**: Comprehensive technical documentation

### Python Development
- **Advanced Python**: Modern features, type hints, and best practices
- **GUI Development**: Complex Tkinter applications with custom widgets
- **Image Processing**: Pillow integration for game asset management
- **Data Structures**: Efficient algorithms for game state management
- **Error Handling**: Robust exception handling and debugging

### Game Development
- **Game Engine Architecture**: Modular, extensible game systems
- **Asset Management**: Efficient loading, caching, and memory management
- **User Experience**: Intuitive interfaces and smooth gameplay flow
- **Performance Optimization**: Fast loading times and responsive UI
- **Cross-Platform Development**: Windows, macOS, and Linux compatibility

### Professional Practices
- **Testing**: Comprehensive unit and integration testing
- **Code Review**: Self-review and quality assurance processes
- **Project Management**: Organized development with clear milestones
- **Performance Monitoring**: Profiling and optimization techniques
- **Documentation**: Professional-grade technical writing

## 📁 Project Structure

```
cave-game/
├── 🎮 Core Game
│   ├── player_gui.py              # Main game (1,550 lines, complete MVP)
│   ├── game_launcher.py           # Application entry point
│   └── enhanced_gui_final.py      # Development sandbox
│
├── 🎨 Assets
│   └── assets/
│       ├── backgrounds/            # 10 scene backgrounds (optimized)
│       ├── sprites/                # 7 character/enemy sprites (transparent)
│       └── icons/                  # Game icons
│
├── 🛠️ Development Tools
│   ├── utilities/
│   │   ├── capture_player_gui_snapshots.py  # Auto-generate scene screenshots
│   │   ├── validate_scene_choices.py        # Validate all choices/consequences
│   │   ├── analyze_snapshots.py             # Snapshot coverage analysis
│   │   ├── autoplay_route.py                # Automated playthrough testing
│   │   ├── continuity_validator.py          # Game logic validation
│   │   └── [8 more development tools]
│   ├── capture_snapshots.bat      # Quick snapshot tool (Windows)
│   └── capture_snapshots.sh       # Quick snapshot tool (Linux/Mac)
│
├── 🧪 Testing
│   └── tests/
│       ├── unit/                   # Unit test suite (14 tests)
│       ├── integration/            # Integration tests
│       └── assets/                 # Test resources
│
├── 📚 Documentation
│   ├── README.md                   # This file
│   ├── MVP_ROADMAP.md              # Project overview and roadmap
│   ├── MANUAL_TEST_GUIDE.md        # Testing procedures
│   └── docs/
│       ├── ai-development/         # AI-assisted development guides (3)
│       ├── reports/                # Session and MVP completion reports (3)
│       ├── development/            # Level maps and graphs
│       └── [legacy documentation]
│
└── 🎯 Snapshots
    └── player_gui_snapshots/       # 13 scene screenshots + reports
```

## 🤝 Contributing

This project demonstrates professional software development practices suitable for enterprise environments. The codebase serves as a portfolio piece showcasing:

- **Advanced Python Development**: Modern Python features and best practices
- **GUI Engineering**: Complex Tkinter applications with custom frameworks
- **Game Development**: Professional game engine architecture
- **Software Architecture**: Scalable, maintainable design patterns
- **Testing & Quality**: Comprehensive testing and quality assurance
- **Documentation**: Professional technical writing and project management

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Aidan Cowling**  
- GitHub: [@Acowl](https://github.com/Acowl)
- Project: [SHABUYA Cave Adventure](https://github.com/Acowl/cave-game)

## 🎯 Professional Impact

This project demonstrates enterprise-level software development capabilities:

### Technical Proficiency
- **Complete Product Delivery**: From concept to production-ready MVP with proper closure
- **Advanced GUI Development**: Custom Tkinter framework with professional UI/UX design
- **Automated Testing**: Comprehensive validation suite ensuring 100% functional coverage
- **AI-Assisted Workflows**: Innovative development tools enabling rapid iteration
- **Asset Pipeline**: Automatic sprite processing and optimization systems

### Software Engineering Excellence
- **Code Quality**: 1,550+ lines with zero critical errors, full validation
- **Documentation**: 15+ professional guides for developers and AI assistants
- **Version Control**: Clean git history with meaningful commits and clear project evolution
- **Testing Infrastructure**: Automated scene validation, visual regression, gameplay testing
- **Production Readiness**: Complete, polished game ready for distribution

### Demonstrated Skills
✅ Python GUI development (Tkinter)  
✅ Image processing and optimization (Pillow)  
✅ Game design and narrative development  
✅ Automated testing and quality assurance  
✅ Technical documentation and API design  
✅ Performance optimization and asset management  
✅ AI-assisted development workflows  

**Applicable to**: Game development, GUI applications, automation tools, enterprise software, and any domain requiring robust Python development with professional quality standards.
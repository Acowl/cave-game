# 🗻 SHABUYA Cave Adventure

A Python-based RPG game with a DevSecOps pipeline, evolving from turn-based text adventure to real-time action RPG.

## 🚀 Quick Start

### Play the Game (Current Version)
```bash
# Windows
START_GAME.bat

# Linux/Mac
./start_game.sh
```

### Run DevSecOps Checks
```bash
# Using Docker (recommended)
docker build -t shabuya-devsecops .
docker run shabuya-devsecops

# Or locally
python -m pip install -r requirements.txt
python run_devsecops_checks.bat  # Windows
```

## 🎮 Game Features

- **3 Character Classes**: Warrior, Rogue, Mage
- **Turn-based Combat**: Strategic RPG battles
- **Multiple Locations**: Explore caves, villages, and mysterious chambers
- **GUI & Text Modes**: Beautiful tkinter interface or classic text adventure
- **Boss Battles**: Epic encounters with unique enemies

## 🛡️ DevSecOps Pipeline

This project demonstrates modern DevSecOps practices:

### CI/CD
- **GitHub Actions**: Automated testing and security scans on every push
- **Docker**: Containerized build and test environment
- **Quality Gates**: Code formatting, linting, and security checks

### Security Scanning
- **Bandit**: Static Application Security Testing (SAST)
- **Safety**: Software Composition Analysis (SCA)
- **Automated Alerts**: Dependency vulnerability monitoring

### Code Quality
- **Black**: Automated code formatting
- **Flake8**: Linting and style enforcement
- **Pytest**: Unit and integration testing

## 📁 Project Structure

```
game/
├── .github/workflows/ci.yml    # GitHub Actions CI/CD pipeline
├── Dockerfile                  # Container definition
├── requirements.txt            # Python dependencies
├── main.py                     # Game entry point
├── launcher.py                 # GUI launcher
├── game_refactored.py         # Core game logic
├── player.py                   # Player classes
├── combat.py                   # Combat system
├── scenes.py                   # Game scenes
└── cave-game/                  # Extended game content
    ├── assets/                 # Graphics and sprites
    ├── tests/                  # Test suite
    └── utilities/              # Development tools
```

## 🔧 Development

### Prerequisites
- Python 3.7+
- Docker (optional, for containerized testing)
- Git

### Setup Development Environment
```bash
# Clone the repository
git clone <your-repo-url>
cd game

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```

### Running Security Scans Locally
```bash
# Security scan
python -m bandit -r . -s B101

# Code formatting
python -m black .

# Linting
python -m flake8 . --select=E9,F63,F7,F82
```

## 🎯 Roadmap

### Phase 1: DevSecOps Foundation ✅
- [x] Docker containerization
- [x] GitHub Actions CI/CD
- [x] Security scanning (Bandit, Safety)
- [x] Code quality tools (Black, Flake8)
- [x] Automated testing (Pytest)

### Phase 2: Real-Time Engine (In Progress)
- [ ] Migrate to Pygame for real-time gameplay
- [ ] Implement WASD movement
- [ ] Create tile-based world system
- [ ] Real-time combat mechanics
- [ ] Enhanced graphics and animations

### Phase 3: Advanced Features
- [ ] Multiplayer support
- [ ] Save/load system
- [ ] Quest system
- [ ] Inventory management
- [ ] Sound effects and music

## 📊 CI/CD Status

The pipeline automatically runs on every push:
- 🛡️ Security scanning
- 🎨 Code formatting checks
- 🔍 Linting
- 🧪 Unit tests

Check the **Actions** tab to see pipeline results.

## 📚 Documentation

- [DevSecOps Roadmap](DEVSECOPS_ROADMAP.md)
- [Game Design Document](GAME_DESIGN_DOC.md)
- [DevSecOps Status](DEVSECOPS_STATUS.md)
- [Docker Quick Start](DOCKER_QUICK_START.md)

## 🤝 Contributing

This is a learning project demonstrating DevSecOps practices. Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

All contributions will be automatically tested by the CI/CD pipeline.

## 📜 License

This project is for educational purposes.

## 🎓 Learning Objectives

This project demonstrates:
1. **Infrastructure as Code**: Dockerfile, CI/CD configs
2. **Security Automation**: SAST, SCA, dependency scanning
3. **Quality Gates**: Automated formatting and linting
4. **Container Orchestration**: Docker-based development
5. **Modern Python Development**: Type hints, testing, documentation

---

**Made with ❤️ as a DevSecOps learning journey**


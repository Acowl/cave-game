# Docker DevSecOps Quick Start

## 🐳 Essential Commands

### 1. Build the Image
```bash
docker build -t shabuya-devsecops .
```
This creates a container image with all your code and dependencies.

### 2. Run the Pipeline
```bash
docker run shabuya-devsecops
```
This runs pytest by default (as defined in the Dockerfile).

### 3. Run Security Scan
```bash
docker run shabuya-devsecops python -m bandit -r . -s B101
```

### 4. Run Code Formatter Check
```bash
docker run shabuya-devsecops python -m black . --check
```

### 5. Run All Checks (Interactive)
```bash
docker run -it shabuya-devsecops bash
# Now inside container:
python -m bandit -r . -s B101
python -m black . --check
python -m flake8 . --count --select=E9,F63,F7,F82
pytest
```

## 🔧 Troubleshooting

### "docker: command not found"
- **Solution**: Restart your terminal after installing Docker Desktop
- Docker Desktop must be running (check system tray)

### "Cannot connect to Docker daemon"
- **Solution**: Start Docker Desktop application
- Wait for it to fully start (whale icon should be steady, not animated)

### Build takes a long time
- **First build**: Downloads base Python image + installs all packages (2-5 min)
- **Subsequent builds**: Much faster due to Docker layer caching

### "No space left on device"
- **Solution**: Clean up old images
```bash
docker system prune -a
```

## 📊 What Each Check Does

| Tool | Purpose | What It Finds |
|------|---------|---------------|
| **Bandit** | Security (SAST) | SQL injection, hardcoded passwords, unsafe functions |
| **Safety** | Dependency Security (SCA) | Vulnerable libraries/packages |
| **Black** | Code Formatting | Inconsistent style, formatting issues |
| **Flake8** | Code Quality | Syntax errors, unused imports, undefined variables |
| **Pytest** | Functional Testing | Broken features, regressions |

## 🎯 Next Steps After Docker Works

1. **Run the full build** to see current issues
2. **Fix any critical security issues** found by Bandit
3. **Format the code** with `docker run shabuya-devsecops python -m black .`
4. **Move to Phase 2**: Start building the Pygame real-time engine


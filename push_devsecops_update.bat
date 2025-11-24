@echo off
REM Push DevSecOps Updates to Existing cave-game Repository
REM This adds your new DevSecOps pipeline to the existing repo

echo.
echo ========================================
echo   Push DevSecOps to cave-game Repo
echo ========================================
echo.

REM Check if git is already initialized
if not exist .git (
    echo [1/6] Initializing Git repository...
    git init
    echo [OK] Git initialized
) else (
    echo [1/6] Git already initialized
    echo [OK] Using existing Git repo
)

echo.
echo [2/6] Checking Git configuration...
git config user.name >nul 2>&1
if errorlevel 1 (
    echo Please configure Git:
    set /p GIT_NAME="Your Name: "
    set /p GIT_EMAIL="Your Email: "
    git config --global user.name "%GIT_NAME%"
    git config --global user.email "%GIT_EMAIL%"
    echo [OK] Git configured
) else (
    echo [OK] Git already configured
)

echo.
echo [3/6] Connecting to cave-game repository...
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin https://github.com/Acowl/cave-game.git
    echo [OK] Remote added
) else (
    git remote set-url origin https://github.com/Acowl/cave-game.git
    echo [OK] Remote updated
)

echo.
echo [4/6] Fetching existing repository...
git fetch origin
echo [OK] Fetched

echo.
echo [5/6] Setting up branch...
git branch -M main
echo [OK] Branch set to main

echo.
echo [6/6] Staging new DevSecOps files...
git add .github/workflows/ci.yml
git add Dockerfile
git add .dockerignore
git add requirements.txt
git add .gitignore
git add README.md
git add DEVSECOPS_ROADMAP.md
git add GAME_DESIGN_DOC.md
git add DEVSECOPS_STATUS.md
git add DOCKER_QUICK_START.md
git add GITHUB_SETUP_GUIDE.md
git add run_devsecops_checks.bat
git add setup_venv.bat
echo [OK] DevSecOps files staged

echo.
echo ========================================
echo   Files Ready to Push
echo ========================================
echo.
echo New DevSecOps additions:
echo   - .github/workflows/ci.yml      (GitHub Actions pipeline)
echo   - Dockerfile                     (Container definition)
echo   - .dockerignore                  (Build optimization)
echo   - requirements.txt               (Updated with DevSecOps tools)
echo   - README.md                      (Professional documentation)
echo   - DEVSECOPS_*.md                 (DevSecOps guides)
echo   - DOCKER_QUICK_START.md          (Docker guide)
echo   - GITHUB_SETUP_GUIDE.md          (Setup instructions)
echo   - run_devsecops_checks.bat       (Local testing script)
echo.
echo This will create a new commit with your DevSecOps additions.
echo.
set /p COMMIT_MSG="Enter commit message (or press Enter for default): "
if "%COMMIT_MSG%"=="" (
    set COMMIT_MSG=Add DevSecOps pipeline: Docker, GitHub Actions, security scanning
)

git commit -m "%COMMIT_MSG%"
if errorlevel 1 (
    echo [WARNING] Commit failed - checking if there are changes...
    git status
    pause
    exit /b 1
)
echo [OK] Commit created

echo.
echo ========================================
echo   Ready to Push!
echo ========================================
echo.
set /p CONFIRM="Push DevSecOps updates to GitHub? (Y/N): "
if /i "%CONFIRM%"=="Y" (
    echo.
    echo [PUSHING] Uploading to https://github.com/Acowl/cave-game...
    git push origin main
    if errorlevel 1 (
        echo.
        echo [INFO] If push was rejected, you may need to pull first:
        echo   git pull origin main --rebase
        echo   git push origin main
        echo.
        echo Or if you want to force push (BE CAREFUL):
        echo   git push origin main --force
        echo.
        pause
        exit /b 1
    )
    echo.
    echo ========================================
    echo   SUCCESS! DevSecOps Pipeline Pushed!
    echo ========================================
    echo.
    echo Check your GitHub Actions:
    echo   https://github.com/Acowl/cave-game/actions
    echo.
    echo The pipeline will automatically run and:
    echo   - Scan for security vulnerabilities (Bandit, Safety)
    echo   - Check code formatting (Black)
    echo   - Run linting (Flake8)
    echo   - Execute tests (Pytest)
    echo.
) else (
    echo.
    echo Push cancelled. To push later, run:
    echo   git push origin main
    echo.
)

pause


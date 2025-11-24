@echo off
REM GitHub Setup Script
REM This script initializes git and prepares for pushing to GitHub

echo.
echo ========================================
echo   GitHub Setup for SHABUYA
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git is not installed
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/6] Initializing Git repository...
git init
if errorlevel 1 (
    echo [WARNING] Git already initialized or error occurred
)
echo [OK] Git initialized

echo.
echo [2/6] Adding files to staging...
git add .
echo [OK] Files staged

echo.
echo [3/6] Creating initial commit...
git commit -m "Initial commit: DevSecOps pipeline with game foundation"
if errorlevel 1 (
    echo [WARNING] Commit failed - files may already be committed
)
echo [OK] Initial commit created

echo.
echo [4/6] Setting default branch to main...
git branch -M main
echo [OK] Branch set to main

echo.
echo ========================================
echo   Ready to Push to GitHub!
echo ========================================
echo.
echo Next steps:
echo.
echo 1. Create a new repository on GitHub:
echo    - Go to: https://github.com/new
echo    - Name: shabuya-game
echo    - Description: RPG game with DevSecOps pipeline
echo    - Make it Public or Private (your choice)
echo    - DO NOT initialize with README (we have one)
echo.
echo 2. Copy your repository URL (it will look like):
echo    https://github.com/YOUR_USERNAME/shabuya-game.git
echo.
echo 3. Run these commands:
echo    git remote add origin YOUR_REPO_URL
echo    git push -u origin main
echo.
echo ========================================
pause


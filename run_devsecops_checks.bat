@echo off
REM DevSecOps Local Checks Script
REM Run this to verify code quality and security before pushing

echo.
echo ========================================
echo   SHABUYA DevSecOps Pipeline
echo ========================================
echo.

echo [1/5] Installing Dependencies...
python -m pip install --user --quiet --upgrade pip
python -m pip install --user --quiet bandit black flake8 pytest pytest-cov safety
if errorlevel 1 (
    echo [FAILED] Could not install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed

echo.
echo [2/5] Running Security Scan (Bandit)...
python -m bandit -r . -s B101 --exclude ./venv,./cave-game/tests,./__pycache__ 2>nul
if errorlevel 1 (
    echo [WARNING] Security issues detected - review output above
) else (
    echo [OK] No critical security issues found
)

echo.
echo [3/5] Running Code Formatting Check (Black)...
python -m black . --check --exclude "/(venv|__pycache__|\.git)/" 2>nul
if errorlevel 1 (
    echo [INFO] Some files need formatting. Run: python -m black .
) else (
    echo [OK] All files are formatted correctly
)

echo.
echo [4/5] Running Linter (Flake8)...
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=venv,__pycache__,.git 2>nul
if errorlevel 1 (
    echo [FAILED] Linting errors found
) else (
    echo [OK] No critical linting issues
)

echo.
echo [5/5] Running Unit Tests (Pytest)...
python -m pytest cave-game/tests/unit/ 2>nul
if errorlevel 1 (
    echo [WARNING] Some tests failed or no tests found
) else (
    echo [OK] All tests passed
)

echo.
echo ========================================
echo   DevSecOps Checks Complete!
echo ========================================
echo.
echo To run these checks in Docker (once installed):
echo   docker build -t shabuya-devsecops .
echo   docker run shabuya-devsecops
echo.
pause

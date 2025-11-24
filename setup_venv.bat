@echo off
REM Setup Virtual Environment Script
REM Run this once to create a clean development environment

echo.
echo ========================================
echo   Setting up Virtual Environment
echo ========================================
echo.

REM Check if venv already exists
if exist venv (
    echo [INFO] Virtual environment already exists
    echo [INFO] Delete the 'venv' folder if you want to recreate it
    goto :activate
)

echo [1/2] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [FAILED] Could not create virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment created

:activate
echo.
echo [2/2] To activate the virtual environment, run:
echo.
echo     venv\Scripts\activate.bat
echo.
echo Then install dependencies with:
echo     pip install -r requirements.txt
echo.
echo ========================================
pause



@echo off
title SHABUYA Cave Adventure Launcher
echo.
echo 🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻
echo 🗻                                           🗻
echo 🗻        SHABUYA - CAVE ADVENTURE          🗻  
echo 🗻           Loading Launcher...            🗻
echo ��                                           🗻
echo 🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻
echo.

if exist "launcher.py" (
    echo Starting launcher...
    python launcher.py
) else if exist "main.py" (
    echo Launcher not found, starting game directly...
    python main.py
) else (
    echo ERROR: Game files not found!
    echo Please make sure all game files are in this folder.
    pause
    exit
)

if errorlevel 1 (
    echo.
    echo ❌ Error starting game!
    echo.
    echo Troubleshooting:
    echo 1. Make sure Python 3.7+ is installed
    echo 2. Try running: python --version
    echo 3. Install Python from: https://python.org
    echo.
    pause
)

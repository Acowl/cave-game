@echo off
title SHABUYA Cave Adventure Launcher
echo.
echo 🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻
echo 🗻                                           🗻
echo 🗻        SHABUYA - CAVE ADVENTURE          🗻  
echo 🗻           Loading Launcher...            🗻
echo 🗻                                           🗻
echo 🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻
echo.

REM Test Python availability
python --version >nul 2>&1
if errorlevel 1 (
    python3 --version >nul 2>&1
    if errorlevel 1 (
        py --version >nul 2>&1
        if errorlevel 1 (
            echo ❌ ERROR: Python not found!
            echo.
            echo TROUBLESHOOTING STEPS:
            echo 1. Install Python from: https://python.org
            echo 2. During installation, check "Add Python to PATH"
            echo 3. Restart your computer after installation
            echo 4. Test with: python --version
            echo.
            echo If you have Python installed:
            echo - Try: py launcher.py
            echo - Or: python3 launcher.py
            echo.
            pause
            exit /b 1
        ) else (
            set PYTHON_CMD=py
        )
    ) else (
        set PYTHON_CMD=python3
    )
) else (
    set PYTHON_CMD=python
)

echo Using Python command: %PYTHON_CMD%
echo.

if exist "launcher.py" (
    echo Starting professional launcher...
    %PYTHON_CMD% launcher.py
    if errorlevel 1 (
        echo.
        echo ❌ GUI launcher failed! Trying text mode...
        echo.
        %PYTHON_CMD% main.py --text
    )
) else if exist "main.py" (
    echo Launcher not found, starting game directly...
    %PYTHON_CMD% main.py
) else (
    echo ❌ ERROR: Game files not found!
    echo Please make sure all game files are in this folder.
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

if errorlevel 1 (
    echo.
    echo ❌ Game failed to start!
    echo.
    echo TROUBLESHOOTING:
    echo 1. Python version: 
    %PYTHON_CMD% --version
    echo.
    echo 2. Test tkinter for GUI mode:
    %PYTHON_CMD% -c "import tkinter; print('tkinter: OK')" 2>nul || echo tkinter: MISSING - GUI disabled
    echo.
    echo 3. Try text mode: %PYTHON_CMD% main.py --text
    echo 4. Install Python from: https://python.org
    echo.
    pause
)

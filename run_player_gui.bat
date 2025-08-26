@echo off
echo 🎮 Starting SHABUYA Cave Adventure Player GUI...
python3 player_gui.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo ❌ Python3 not found, trying 'python'...
    python player_gui.py
)
if %ERRORLEVEL% neq 0 (
    echo.
    echo ❌ Python not found, trying 'py'...
    py player_gui.py
)
pause

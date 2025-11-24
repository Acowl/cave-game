@echo off
REM Quick snapshot capture script for Windows

echo ========================================
echo SHABUYA Cave Adventure
echo Snapshot Capture Tool
echo ========================================
echo.

:menu
echo Select an option:
echo.
echo 1. Generate snapshots (Warrior only - FAST)
echo 2. Generate snapshots (All classes - COMPLETE)
echo 3. Analyze existing snapshots
echo 4. View snapshot report
echo 5. Exit
echo.

set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" goto fast
if "%choice%"=="2" goto full
if "%choice%"=="3" goto analyze
if "%choice%"=="4" goto view
if "%choice%"=="5" goto end
echo Invalid choice. Please try again.
echo.
goto menu

:fast
echo.
echo Generating snapshots (Warrior only)...
python utilities\capture_player_gui_snapshots.py
echo.
echo Done! Snapshots saved to: player_gui_snapshots\
pause
goto menu

:full
echo.
echo Generating snapshots (All classes)...
echo This may take a minute...
python utilities\capture_player_gui_snapshots.py --full
echo.
echo Done! Snapshots saved to: player_gui_snapshots\
pause
goto menu

:analyze
echo.
python utilities\analyze_snapshots.py
echo.
pause
goto menu

:view
echo.
echo Opening snapshot report...
start player_gui_snapshots\player_gui_snapshots.md
goto menu

:end
echo.
echo Goodbye!


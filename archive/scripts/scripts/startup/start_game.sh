#!/bin/bash

# SHABUYA Cave Adventure Launcher Script

echo "🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻"
echo "🗻                                           🗻"
echo "🗻        SHABUYA - CAVE ADVENTURE          🗻"
echo "🗻           Loading Launcher...            🗻"
echo "🗻                                           🗻"
echo "🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻"
echo

# Check if Python is available with better detection
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "Found Python 3: $(python3 --version)"
elif command -v python &> /dev/null; then
    # Check if it's Python 3
    PYTHON_VERSION=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null)
    if [[ "$PYTHON_VERSION" =~ ^3\. ]]; then
        PYTHON_CMD="python"
        echo "Found Python: $(python --version)"
    else
        echo "⚠️  Warning: Found Python 2.x, but need Python 3.7+"
    fi
elif command -v py &> /dev/null; then
    PYTHON_CMD="py"
    echo "Found py launcher: $(py --version)"
fi

if [ -z "$PYTHON_CMD" ]; then
    echo "❌ Error: Python 3.7+ not found!"
    echo
    echo "TROUBLESHOOTING STEPS:"
    echo "1. Install Python from: https://python.org"
    echo "2. Make sure Python is in your PATH"
    echo "3. Try these commands to test:"
    echo "   python3 --version"
    echo "   python --version" 
    echo "   py --version"
    echo
    echo "macOS: brew install python"
    echo "Linux: sudo apt install python3"
    echo
    exit 1
fi

echo "Using Python command: $PYTHON_CMD"
echo

# Test tkinter availability for GUI
if $PYTHON_CMD -c "import tkinter" &> /dev/null; then
    echo "✅ GUI support available (tkinter found)"
    GUI_AVAILABLE=true
else
    echo "⚠️  GUI support missing (tkinter not found)"
    echo "   Install with: sudo apt-get install python3-tk (Linux)"
    echo "   or: brew install python-tk (macOS)"
    GUI_AVAILABLE=false
fi

echo

# Launch the game with fallback options
if [ -f "launcher.py" ]; then
    echo "Starting professional launcher..."
    if $PYTHON_CMD launcher.py; then
        echo "Game completed successfully!"
    else
        echo "❌ GUI launcher failed!"
        if [ -f "main.py" ]; then
            echo "🔄 Trying text mode fallback..."
            $PYTHON_CMD main.py --text
        fi
    fi
elif [ -f "main.py" ]; then
    echo "Launcher not found, starting game directly..."
    if [ "$GUI_AVAILABLE" = true ]; then
        echo "Attempting GUI mode..."
        if ! $PYTHON_CMD main.py; then
            echo "🔄 GUI failed, trying text mode..."
            $PYTHON_CMD main.py --text
        fi
    else
        echo "Starting in text mode..."
        $PYTHON_CMD main.py --text
    fi
else
    echo "❌ Error: Game files not found!"
    echo "Please make sure all game files are in this folder."
    echo "Current directory: $(pwd)"
    echo "Looking for: launcher.py or main.py"
    echo
    echo "Files in directory:"
    ls -la
    exit 1
fi

#!/bin/bash

# SHABUYA Cave Adventure Launcher Script

echo "🗻��🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻"
echo "🗻                                           🗻"
echo "🗻        SHABUYA - CAVE ADVENTURE          🗻"
echo "🗻           Loading Launcher...            🗻"
echo "🗻                                           🗻"
echo "🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻��🗻🗻🗻🗻🗻🗻🗻"
echo

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python not found!"
    echo "Please install Python 3.7+ from https://python.org"
    exit 1
fi

# Launch the game
if [ -f "launcher.py" ]; then
    echo "Starting launcher..."
    $PYTHON_CMD launcher.py
elif [ -f "main.py" ]; then
    echo "Launcher not found, starting game directly..."
    $PYTHON_CMD main.py
else
    echo "❌ Error: Game files not found!"
    echo "Please make sure all game files are in this folder."
    exit 1
fi

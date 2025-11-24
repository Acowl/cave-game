#!/usr/bin/env python3
"""Test full main.py execution"""

import sys
import os

# Set up command line args to force text mode
sys.argv = ['main.py', '--text']

# Add the current directory to path
sys.path.insert(0, '/workspaces/cave-game')
os.chdir('/workspaces/cave-game')

print("Testing full main.py execution...")

try:
    from main import main
    print("main function imported successfully")
    
    print("About to call main...")
    main()
    print("main completed")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

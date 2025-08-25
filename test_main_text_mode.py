#!/usr/bin/env python3
"""Test main.py text mode step by step"""

import sys
import os

# Add the current directory to path
sys.path.insert(0, '/workspaces/cave-game')
os.chdir('/workspaces/cave-game')

print("Testing main.py run_text_mode function...")

try:
    from main import run_text_mode
    print("run_text_mode imported successfully")
    
    print("About to call run_text_mode...")
    result = run_text_mode()
    print(f"run_text_mode returned: {result}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

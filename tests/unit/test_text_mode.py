#!/usr/bin/env python3
"""Test text mode directly"""

print("Testing text mode directly...")
try:
    from game_refactored import main as text_main
    print("About to call text_main...")
    text_main()
    print("text_main completed")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

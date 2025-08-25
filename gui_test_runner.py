#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - GUI Test Runner
Run this in an environment with a display
"""

import sys
import tkinter as tk
from tkinter import messagebox
import traceback

def test_basic_gui():
    """Test basic GUI functionality"""
    try:
        print("Testing basic GUI...")
        root = tk.Tk()
        root.title("SHABUYA GUI Test")
        root.geometry("300x200")
        
        tk.Label(root, text="Basic GUI Test", font=("Arial", 16)).pack(pady=20)
        tk.Label(root, text="If you can see this, GUI works!", 
                font=("Arial", 10)).pack(pady=10)
        tk.Button(root, text="Close", command=root.destroy, 
                 bg="#8B4513", fg="white").pack(pady=20)
        
        root.mainloop()
        return True
        
    except Exception as e:
        print(f"Basic GUI test failed: {e}")
        return False

def test_enhanced_gui():
    """Test enhanced GUI with graphics"""
    try:
        print("Testing enhanced GUI...")
        
        from enhanced_gui_system import EnhancedGameGUI
        
        root = tk.Tk()
        gui = EnhancedGameGUI(root)
        gui.setup_graphics()
        
        # Add test button
        test_frame = tk.Frame(root, bg='#1a0f08')
        test_frame.pack(pady=10)
        
        tk.Button(test_frame, text="Graphics Demo", 
                 command=gui.create_demo_graphics_test,
                 bg='#8B4513', fg='white').pack(side=tk.LEFT, padx=5)
        
        tk.Button(test_frame, text="Close", 
                 command=root.destroy,
                 bg='#654321', fg='white').pack(side=tk.LEFT, padx=5)
        
        root.mainloop()
        return True
        
    except Exception as e:
        print(f"Enhanced GUI test failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run GUI tests"""
    print("=" * 60)
    print("SHABUYA CAVE ADVENTURE - GUI TEST RUNNER")
    print("=" * 60)
    
    # Test basic GUI first
    if not test_basic_gui():
        print("❌ Basic GUI test failed - check your display environment")
        return False
    
    print("✅ Basic GUI test passed")
    
    # Test enhanced GUI
    response = input("\nTest enhanced GUI with graphics? (y/n): ")
    if response.lower() in ['y', 'yes']:
        if test_enhanced_gui():
            print("✅ Enhanced GUI test completed")
        else:
            print("❌ Enhanced GUI test failed")
    
    print("\n🎉 GUI testing completed!")

if __name__ == "__main__":
    main()

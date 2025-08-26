#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Local Setup Verification
Verify everything is working on local machine
"""

import sys
import os
from pathlib import Path

def verify_local_setup():
    """Verify the local setup is complete"""
    print("🔍 " + "=" * 60)
    print("🔍 SHABUYA LOCAL SETUP VERIFICATION")
    print("🔍 " + "=" * 60)
    
    checks = []
    
    # Check Python version
    python_version = sys.version_info
    if python_version >= (3, 7):
        checks.append(("✅", f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}"))
    else:
        checks.append(("❌", f"Python version too old: {python_version.major}.{python_version.minor} (need 3.7+)"))
    
    # Check PIL/Pillow
    try:
        from PIL import Image, ImageTk
        checks.append(("✅", "PIL/Pillow: Available"))
    except ImportError:
        checks.append(("❌", "PIL/Pillow: NOT AVAILABLE - run 'pip install pillow'"))
    
    # Check tkinter
    try:
        import tkinter as tk
        checks.append(("✅", "Tkinter: Available"))
    except ImportError:
        checks.append(("❌", "Tkinter: NOT AVAILABLE - install tkinter for your system"))
    
    # Check graphics assets
    assets_dir = Path("game_assets")
    if assets_dir.exists():
        sprite_count = len(list(assets_dir.glob("sprites/*.png")))
        bg_count = len(list(assets_dir.glob("backgrounds/*.png")))
        checks.append(("✅", f"Graphics assets: {sprite_count} sprites, {bg_count} backgrounds"))
    else:
        checks.append(("❌", "Graphics assets: Missing - re-download project"))
    
    # Check key files
    key_files = [
        "enhanced_gui_system.py",
        "gui_test_runner.py",
        "test_graphics_integration.py",
        "main.py"
    ]
    
    missing_files = []
    for file in key_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if not missing_files:
        checks.append(("✅", f"Key files: All {len(key_files)} present"))
    else:
        checks.append(("❌", f"Missing files: {', '.join(missing_files)}"))
    
    # Display results
    print("\n📋 VERIFICATION RESULTS:")
    print("-" * 50)
    
    all_good = True
    for status, message in checks:
        print(f"{status} {message}")
        if status == "❌":
            all_good = False
    
    print("\n🎯 NEXT STEPS:")
    print("-" * 50)
    
    if all_good:
        print("🎉 Everything looks good! Ready to test GUI.")
        print("\nRun these commands:")
        print("  python gui_test_runner.py          # Start here")
        print("  python enhanced_gui_system.py      # Enhanced GUI")
        print("  python test_graphics_integration.py # Full demo")
        
    else:
        print("⚠️  Fix the issues above first:")
        print("  • Install Pillow only: pip install pillow")
        print("  • Tkinter comes with Python - no separate install needed")
        print("  • Re-download project if files missing")
        print("  • Check Python version (need 3.7+)")
    
    return all_good

def create_quick_test():
    """Create a super simple GUI test"""
    try:
        import tkinter as tk
        
        def simple_test():
            root = tk.Tk()
            root.title("SHABUYA - Quick Test")
            root.geometry("400x200")
            
            tk.Label(root, text="🎮 SHABUYA Cave Adventure", 
                    font=("Arial", 16, "bold")).pack(pady=20)
            
            tk.Label(root, text="If you can see this window, GUI is working!",
                    font=("Arial", 12)).pack(pady=10)
            
            tk.Button(root, text="Test Graphics", 
                     command=lambda: test_enhanced_gui(root),
                     bg="#8B4513", fg="white", font=("Arial", 10)).pack(pady=10)
            
            tk.Button(root, text="Close", command=root.destroy,
                     bg="#654321", fg="white", font=("Arial", 10)).pack()
            
            root.mainloop()
        
        def test_enhanced_gui(parent):
            try:
                from enhanced_gui_system import EnhancedGameGUI
                
                test_window = tk.Toplevel(parent)
                gui = EnhancedGameGUI(test_window)
                gui.setup_graphics()
                
                tk.Label(test_window, text="✅ Enhanced GUI loaded successfully!",
                        fg="green", font=("Arial", 12)).pack(pady=20)
                
                tk.Button(test_window, text="Graphics Demo", 
                         command=gui.create_demo_graphics_test,
                         bg="#8B4513", fg="white").pack(pady=10)
                
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", f"Enhanced GUI failed: {e}")
        
        return simple_test
        
    except ImportError:
        return None

if __name__ == "__main__":
    # Run verification
    success = verify_local_setup()
    
    # Offer quick test if available
    if success:
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            response = input("\n🖥️  Run quick GUI test now? (y/n): ")
            if response.lower() in ['y', 'yes']:
                simple_test = create_quick_test()
                if simple_test:
                    simple_test()
                else:
                    print("❌ Could not create GUI test")
        except Exception as e:
            print(f"⚠️ GUI test error: {e}")

#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Simple GUI Debug Test
Debug the enhanced GUI issues step by step
"""

import sys
import traceback
import tkinter as tk
from tkinter import messagebox

def test_basic_imports():
    """Test basic imports without creating GUI"""
    print("🔍 Testing basic imports...")
    
    try:
        import tkinter as tk
        print("✅ tkinter imported")
    except ImportError as e:
        print(f"❌ tkinter import failed: {e}")
        return False
    
    try:
        from PIL import Image, ImageTk
        print("✅ PIL imported")
    except ImportError as e:
        print(f"❌ PIL import failed: {e}")
        return False
    
    try:
        from pathlib import Path
        print("✅ pathlib imported")
    except ImportError as e:
        print(f"❌ pathlib import failed: {e}")
        return False
    
    return True

def test_enhanced_gui_import():
    """Test enhanced GUI import without creating instance"""
    print("\n🔍 Testing enhanced GUI import...")
    
    try:
        from enhanced_gui_system import EnhancedGameGUI
        print("✅ EnhancedGameGUI imported successfully")
        return True, EnhancedGameGUI
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("📁 Make sure enhanced_gui_system.py is in the current directory")
        return False, None
    except Exception as e:
        print(f"❌ Unexpected import error: {e}")
        traceback.print_exc()
        return False, None

def test_assets_exist():
    """Test if graphics assets exist"""
    print("\n🔍 Testing graphics assets...")
    
    from pathlib import Path
    
    assets_dir = Path("game_assets")
    if not assets_dir.exists():
        print("❌ game_assets directory missing")
        return False
    
    sprites_dir = assets_dir / "sprites"
    if not sprites_dir.exists():
        print("❌ sprites directory missing")
        return False
    
    backgrounds_dir = assets_dir / "backgrounds"
    if not backgrounds_dir.exists():
        print("❌ backgrounds directory missing")
        return False
    
    # Count assets
    sprites = list(sprites_dir.glob("*.png"))
    backgrounds = list(backgrounds_dir.glob("*.png"))
    
    print(f"✅ Found {len(sprites)} sprites")
    print(f"✅ Found {len(backgrounds)} backgrounds")
    
    return len(sprites) > 0 and len(backgrounds) > 0

def test_enhanced_gui_creation():
    """Test creating enhanced GUI instance"""
    print("\n🔍 Testing enhanced GUI creation...")
    
    try:
        from enhanced_gui_system import EnhancedGameGUI
        
        # Create a simple root window
        root = tk.Tk()
        root.withdraw()  # Hide it initially
        
        # Try to create enhanced GUI
        gui = EnhancedGameGUI(root)
        print("✅ EnhancedGameGUI instance created")
        
        root.destroy()
        return True, None
        
    except Exception as e:
        print(f"❌ Enhanced GUI creation failed: {e}")
        traceback.print_exc()
        return False, str(e)

def test_graphics_setup():
    """Test graphics setup method"""
    print("\n🔍 Testing graphics setup...")
    
    try:
        from enhanced_gui_system import EnhancedGameGUI
        
        root = tk.Tk()
        root.withdraw()
        
        gui = EnhancedGameGUI(root)
        gui.setup_graphics()
        print("✅ Graphics setup completed")
        
        # Check if graphics were loaded
        sprite_count = len(gui.character_sprites) if hasattr(gui, 'character_sprites') else 0
        bg_count = len(gui.background_images) if hasattr(gui, 'background_images') else 0
        
        print(f"✅ Loaded {sprite_count} character sprites")
        print(f"✅ Loaded {bg_count} background images")
        
        root.destroy()
        return True, f"{sprite_count} sprites, {bg_count} backgrounds"
        
    except Exception as e:
        print(f"❌ Graphics setup failed: {e}")
        traceback.print_exc()
        return False, str(e)

def create_safe_enhanced_gui():
    """Create a safe version of enhanced GUI with error handling"""
    print("\n🔍 Creating safe enhanced GUI window...")
    
    try:
        from enhanced_gui_system import EnhancedGameGUI
        
        root = tk.Tk()
        root.title("SHABUYA - Safe Enhanced GUI Test")
        root.geometry("600x400")
        
        # Add error display area
        error_frame = tk.Frame(root, bg='lightgray')
        error_frame.pack(fill=tk.X, padx=10, pady=5)
        
        error_label = tk.Label(error_frame, text="Status: Starting...", 
                              bg='lightgray', fg='blue')
        error_label.pack()
        
        def safe_setup():
            try:
                error_label.config(text="Status: Creating Enhanced GUI...", fg='blue')
                root.update()
                
                gui = EnhancedGameGUI(root)
                
                error_label.config(text="Status: Setting up graphics...", fg='blue')
                root.update()
                
                gui.setup_graphics()
                
                error_label.config(text="Status: ✅ Enhanced GUI loaded successfully!", fg='green')
                
                # Add test buttons
                button_frame = tk.Frame(root)
                button_frame.pack(pady=20)
                
                tk.Button(button_frame, text="Graphics Demo", 
                         command=lambda: safe_demo(gui),
                         bg='#8B4513', fg='white').pack(side=tk.LEFT, padx=10)
                
                tk.Button(button_frame, text="Close", 
                         command=root.destroy,
                         bg='#654321', fg='white').pack(side=tk.LEFT, padx=10)
                
                return gui
                
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                error_label.config(text=error_msg, fg='red')
                
                # Show detailed error in text widget
                text_widget = tk.Text(root, height=10, width=70)
                text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
                text_widget.insert('1.0', f"Error Details:\n{traceback.format_exc()}")
                
                return None
        
        def safe_demo(gui):
            try:
                gui.create_demo_graphics_test()
            except Exception as e:
                messagebox.showerror("Demo Error", f"Graphics demo failed:\n{str(e)}")
        
        # Run setup after window is ready
        root.after(100, safe_setup)
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Safe GUI creation failed: {e}")
        traceback.print_exc()

def main():
    """Run comprehensive debug tests"""
    print("🔧 " + "=" * 60)
    print("🔧 SHABUYA ENHANCED GUI DEBUG TESTS")
    print("🔧 " + "=" * 60)
    
    # Run tests in order
    tests = [
        ("Basic Imports", test_basic_imports),
        ("Enhanced GUI Import", lambda: test_enhanced_gui_import()[0]),
        ("Graphics Assets", test_assets_exist),
        ("Enhanced GUI Creation", lambda: test_enhanced_gui_creation()[0]),
        ("Graphics Setup", lambda: test_graphics_setup()[0])
    ]
    
    all_passed = True
    
    for test_name, test_func in tests:
        result = test_func()
        if not result:
            all_passed = False
            print(f"\n⚠️ {test_name} failed - stopping here")
            break
    
    if all_passed:
        print(f"\n🎉 All tests passed! Opening safe enhanced GUI...")
        
        response = input("\nOpen enhanced GUI window? (y/n): ")
        if response.lower() in ['y', 'yes']:
            create_safe_enhanced_gui()
    else:
        print(f"\n❌ Some tests failed. Fix issues above before proceeding.")

if __name__ == "__main__":
    main()

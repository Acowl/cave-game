#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Graphics Integration Test
Test the new graphics system integration
"""

import sys
import os
import traceback
import tkinter as tk
from tkinter import messagebox

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_asset_creation():
    """Test if graphics assets were created properly"""
    print("Testing graphics assets...")
    
    assets_dir = "game_assets"
    required_dirs = ["sprites", "backgrounds", "icons"]
    
    # Check directories
    for dirname in required_dirs:
        dir_path = os.path.join(assets_dir, dirname)
        if not os.path.exists(dir_path):
            return False, f"Missing directory: {dir_path}"
    
    # Check sprites
    sprite_files = ["warrior.png", "rogue.png", "mage.png", "enemy.png"]
    sprites_dir = os.path.join(assets_dir, "sprites")
    
    for sprite in sprite_files:
        sprite_path = os.path.join(sprites_dir, sprite)
        if not os.path.exists(sprite_path):
            return False, f"Missing sprite: {sprite_path}"
    
    # Check backgrounds
    bg_files = ["cave_entrance.png", "skull_chamber.png", "primitive_village.png", "menu_background.png"]
    bg_dir = os.path.join(assets_dir, "backgrounds")
    
    for bg in bg_files:
        bg_path = os.path.join(bg_dir, bg)
        if not os.path.exists(bg_path):
            return False, f"Missing background: {bg_path}"
    
    # Check icons
    icon_files = ["game_icon.png", "game_icon.ico"]
    icon_dir = os.path.join(assets_dir, "icons")
    
    for icon in icon_files:
        icon_path = os.path.join(icon_dir, icon)
        if not os.path.exists(icon_path):
            return False, f"Missing icon: {icon_path}"
    
    return True, "All assets found"

def test_enhanced_gui_import():
    """Test if enhanced GUI system can be imported"""
    print("Testing enhanced GUI import...")
    
    try:
        from enhanced_gui_system import EnhancedGameGUI
        print("✓ Enhanced GUI import successful")
        return True, EnhancedGameGUI
    except ImportError as e:
        return False, f"Import error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"

def test_graphics_loading():
    """Test if graphics can be loaded in the enhanced GUI"""
    print("Testing graphics loading...")
    
    try:
        # Create a test window
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Import and create enhanced GUI
        from enhanced_gui_system import EnhancedGameGUI
        gui = EnhancedGameGUI(root)
        
        # Test graphics loading
        gui.setup_graphics()
        
        # Check if graphics were loaded
        sprites_loaded = len(gui.character_sprites) > 0
        backgrounds_loaded = len(gui.background_images) > 0
        
        root.destroy()
        
        if sprites_loaded and backgrounds_loaded:
            return True, f"Graphics loaded: {len(gui.character_sprites)} sprites, {len(gui.background_images)} backgrounds"
        else:
            return False, f"Graphics loading incomplete: sprites={sprites_loaded}, backgrounds={backgrounds_loaded}"
            
    except Exception as e:
        return False, f"Graphics loading error: {e}"

def run_interactive_test():
    """Run an interactive graphics test"""
    print("Running interactive graphics test...")
    
    try:
        # Create main window
        root = tk.Tk()
        root.title("SHABUYA Graphics Test")
        root.geometry("700x600")
        root.configure(bg='#1a0f08')
        
        # Import and create enhanced GUI
        from enhanced_gui_system import EnhancedGameGUI
        gui = EnhancedGameGUI(root)
        
        # Setup graphics
        gui.setup_graphics()
        
        # Create test interface
        title = tk.Label(root, text="SHABUYA Cave Adventure - Graphics Test", 
                        font=("Arial", 16, "bold"), fg='#DAA520', bg='#1a0f08')
        title.pack(pady=20)
        
        # Info label
        info_text = f"Graphics loaded successfully!\nSprites: {len(gui.character_sprites)}\nBackgrounds: {len(gui.background_images)}"
        info = tk.Label(root, text=info_text, font=("Arial", 12), 
                       fg='#CD853F', bg='#1a0f08', justify=tk.CENTER)
        info.pack(pady=10)
        
        # Test buttons
        button_frame = tk.Frame(root, bg='#1a0f08')
        button_frame.pack(pady=20)
        
        def open_graphics_demo():
            gui.create_demo_graphics_test()
        
        def test_scene_switching():
            """Test scene background switching"""
            scenes = ['Cave Entrance', 'Skull Chamber', 'Primitive Village', 'Menu']
            for scene in scenes:
                gui.update_scene_background(scene)
                print(f"Switched to scene: {scene}")
        
        tk.Button(button_frame, text="Open Graphics Demo", 
                 command=open_graphics_demo, bg='#8B4513', fg='white',
                 font=("Arial", 12), padx=20).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Test Scene Switching", 
                 command=test_scene_switching, bg='#8B4513', fg='white',
                 font=("Arial", 12), padx=20).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Close Test", 
                 command=root.destroy, bg='#654321', fg='white',
                 font=("Arial", 12), padx=20).pack(side=tk.LEFT, padx=10)
        
        # Instructions
        instructions = """
Instructions:
1. Click 'Open Graphics Demo' to see all assets
2. Click 'Test Scene Switching' to test background changes
3. Check console for debug output
        """
        
        inst_label = tk.Label(root, text=instructions, font=("Arial", 10), 
                            fg='#DAA520', bg='#1a0f08', justify=tk.LEFT)
        inst_label.pack(pady=20)
        
        print("Interactive test window opened. Check the GUI!")
        root.mainloop()
        
        return True, "Interactive test completed"
        
    except Exception as e:
        traceback.print_exc()
        return False, f"Interactive test error: {e}"

def main():
    """Run comprehensive graphics integration test"""
    print("=" * 60)
    print("SHABUYA CAVE ADVENTURE - GRAPHICS INTEGRATION TEST")
    print("=" * 60)
    
    tests = [
        ("Asset Creation", test_asset_creation),
        ("Enhanced GUI Import", test_enhanced_gui_import),
        ("Graphics Loading", test_graphics_loading),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 40)
        
        try:
            success, message = test_func()
            results.append((test_name, success, message))
            
            if success:
                print(f"✓ PASS: {message}")
            else:
                print(f"✗ FAIL: {message}")
                
        except Exception as e:
            results.append((test_name, False, f"Test crashed: {e}"))
            print(f"✗ CRASH: {e}")
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, success, _ in results if success)
    total = len(results)
    
    for test_name, success, message in results:
        status = "PASS" if success else "FAIL"
        print(f"{status:4} | {test_name}")
    
    print(f"\nResult: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Graphics integration is working!")
        
        # Ask if user wants to run interactive test
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            root = tk.Tk()
            root.withdraw()
            
            response = messagebox.askyesno(
                "Graphics Integration Test", 
                "All tests passed! Would you like to run the interactive graphics demo?"
            )
            
            root.destroy()
            
            if response:
                success, message = run_interactive_test()
                print(f"\nInteractive test: {message}")
        
        except Exception as e:
            print(f"Interactive test setup error: {e}")
    else:
        print(f"\n⚠️  {total - passed} tests failed. Check the errors above.")

if __name__ == "__main__":
    main()

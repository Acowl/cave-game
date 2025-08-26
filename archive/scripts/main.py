#!/usr/bin/env python3
"""
🗻 SHABUYA - Cave Adventure 🗻
Main Launcher - Clean and Professional

This is the primary entry point for the Cave Adventure game.
It automatically detects available interfaces and launches the best option.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent.parent  # Go up from scripts/ to project root
src_path = project_root / 'src'
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_path))


def check_dependencies():
    """Check for required game dependencies"""
    try:
        # Test core game imports
        from src.core.game_engine import main as game_main
        from src.interfaces.ui import title_screen
        return True, "All dependencies available"
    except ImportError as e:
        return False, f"Missing dependency: {e}"


def run_text_mode():
    """Launch the game in text/console mode"""
    try:
        print("🗻 SHABUYA Cave Adventure - Text Mode 🗻")
        print("=" * 50)
        
        # Import and run the main game
        from src.core.game_engine import main as game_main
        game_main()
        
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Thanks for playing!")
    except Exception as e:
        print(f"\nError running text mode: {e}")
        return False
    return True


def run_gui_mode():
    """Launch the game with GUI interface"""
    try:
        print("Starting GUI mode...")
        from src.interfaces.gui import main as gui_main
        gui_main()
        return True
    except ImportError:
        print("GUI interface not available. Falling back to text mode...")
        return False
    except Exception as e:
        print(f"Error starting GUI: {e}")
        print("Falling back to text mode...")
        return False


def show_help():
    """Display help information"""
    help_text = """
🗻 SHABUYA - Cave Adventure 🗻

Usage: python main.py [options]

Options:
  --text     Force text/console mode
  --gui      Force GUI mode (if available)
  --help     Show this help message
  --version  Show version information

Examples:
  python main.py          # Auto-detect best interface
  python main.py --text   # Force text mode
  python main.py --gui    # Force GUI mode

The game will automatically choose the best available interface
if no specific mode is requested.
    """
    print(help_text)


def show_version():
    """Display version information"""
    version_info = """
🗻 SHABUYA Cave Adventure 🗻
Version: 1.0.0
Developer: Professional Game Development
Platform: Cross-platform Python

Features:
• Text-based adventure gameplay
• Multiple character classes
• Combat and progression systems
• Scene-based world exploration
• Enhanced weapons and abilities
• Professional code architecture
    """
    print(version_info)


def main():
    """Main launcher function"""
    # Handle command line arguments
    args = sys.argv[1:]
    
    if '--help' in args or '-h' in args:
        show_help()
        return
        
    if '--version' in args or '-v' in args:
        show_version()
        return
    
    # Check dependencies
    deps_ok, deps_msg = check_dependencies()
    if not deps_ok:
        print(f"❌ Dependency check failed: {deps_msg}")
        print("Please ensure all game files are present.")
        sys.exit(1)
    
    print("✅ All dependencies found")
    
    # Determine launch mode
    force_text = '--text' in args
    force_gui = '--gui' in args
    
    if force_text:
        print("🖥️  Text mode requested")
        success = run_text_mode()
    elif force_gui:
        print("🖼️  GUI mode requested")
        success = run_gui_mode()
        if not success:
            print("Falling back to text mode...")
            run_text_mode()
    else:
        # Auto-detect best mode
        print("🔍 Auto-detecting best interface...")
        
        # Try GUI first (better user experience)
        if run_gui_mode():
            print("✅ GUI mode launched successfully")
        else:
            print("📝 Launching text mode...")
            run_text_mode()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🗻 SHABUYA - Cave Adventure 🗻
A thrilling RPG with GUI and text modes

Run this file to start your adventure!
"""

import sys
import os
from pathlib import Path
import traceback

# Game configuration
REQUIRED_FILES = [
    'game_refactored.py',
    'player.py', 
    'combat.py',
    'scenes.py',
    'item.py',
    'ui.py',
    'config.py'
]

OPTIONAL_FILES = ['gui.py']

# Command line arguments
VALID_ARGS = ['--text', '--debug', '--help', '--version']

def show_help():
    """Display help information"""
    help_text = """
🗻 SHABUYA - Cave Adventure 🗻

Usage: python main.py [options]

Options:
  --text     Force text mode (disable GUI)
  --debug    Show system information and debug output
  --help     Show this help message
  --version  Show version information

Examples:
  python main.py          # Start with GUI (if available)
  python main.py --text   # Force text mode
  python main.py --debug  # Show debug info and start game
"""
    print(help_text)

def show_version():
    """Display version information"""
    version_info = """
🗻 SHABUYA - Cave Adventure v1.0.0
🎮 A Thrilling Text-Based RPG with GUI Support

🔧 Technical Information:
🐍 Python: {python_version}
💻 Platform: {platform}
📁 Location: {game_path}
🗓️  Build: 2024.1.22
    """.format(
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        platform=sys.platform,
        game_path=Path(__file__).parent.resolve()
    )
    print(version_info)

def validate_arguments():
    """Validate command line arguments"""
    invalid_args = [arg for arg in sys.argv[1:] if arg not in VALID_ARGS]
    
    if invalid_args:
        print(f"❌ Invalid arguments: {', '.join(invalid_args)}")
        print("💡 Use --help for usage information")
        return False
    
    # Handle help and version
    if '--help' in sys.argv:
        show_help()
        return False
    
    if '--version' in sys.argv:
        show_version()
        return False
    
    return True

def check_python_version():
    """Check if Python version is compatible"""
    required_version = (3, 7)
    current_version = sys.version_info[:2]
    
    if current_version < required_version:
        print("❌ This game requires Python 3.7 or higher")
        print(f"📍 Current version: Python {current_version[0]}.{current_version[1]}")
        print("📥 Download Python from: https://python.org")
        return False
    
    return True

def check_game_files():
    """Verify all required game files are present"""
    try:
        current_dir = Path(__file__).parent.resolve()
        missing_files = []
        
        for file in REQUIRED_FILES:
            file_path = current_dir / file
            if not file_path.exists():
                missing_files.append(file)
            elif not file_path.is_file():
                print(f"⚠️  Warning: {file} exists but is not a file")
        
        if missing_files:
            print("❌ Missing required game files:")
            for file in missing_files:
                print(f"   📄 {file}")
            print(f"\n📁 Current directory: {current_dir}")
            print("📂 Please ensure all game files are in the same directory as main.py")
            print("\n📋 Required files:")
            for file in REQUIRED_FILES:
                status = "✅" if file not in missing_files else "❌"
                print(f"   {status} {file}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking game files: {e}")
        return False

def is_display_available():
    """Check if a display is available for GUI"""
    try:
        # Windows always has display capability
        if os.name == 'nt':
            return True
        
        # Unix-like systems need DISPLAY or WAYLAND_DISPLAY environment variables
        display = os.environ.get('DISPLAY')
        wayland = os.environ.get('WAYLAND_DISPLAY')
        
        return display is not None or wayland is not None
        
    except Exception:
        return False

def is_gui_available():
    """Check if GUI components are available"""
    try:
        current_dir = Path(__file__).parent.resolve()
        
        # Check if gui.py exists and is readable
        gui_file = current_dir / 'gui.py'
        if not gui_file.exists():
            return False, "gui.py not found"
        
        if not gui_file.is_file():
            return False, "gui.py is not a valid file"
        
        # Check if tkinter is available (without creating windows)
        try:
            import tkinter
            # Test if we can access tkinter without display issues
            if not is_display_available():
                return False, "no display available"
            return True, "GUI ready"
        except ImportError:
            return False, "tkinter not installed"
        except Exception as e:
            return False, f"tkinter error: {e}"
            
    except Exception as e:
        return False, f"filesystem error: {e}"

def print_welcome():
    """Print welcome banner"""
    try:
        banner = "🗻" + "="*60 + "🗻"
        title = "🗻" + " "*18 + "SHABUYA - CAVE ADVENTURE" + " "*18 + "🗻"
        subtitle = "🗻" + " "*15 + "A Thrilling Text-Based RPG" + " "*16 + "🗻"
        
        print(banner)
        print(title)
        print("🗻" + " "*60 + "🗻")
        print(subtitle)
        print(banner)
        print()
    except Exception:
        # Fallback simple banner
        print("=" * 60)
        print("SHABUYA - CAVE ADVENTURE")
        print("A Thrilling Text-Based RPG")
        print("=" * 60)
        print()

def print_system_info():
    """Print system information for debugging"""
    try:
        print("🔍 SYSTEM DEBUG INFORMATION:")
        print(f"🐍 Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        print(f"💻 Platform: {sys.platform}")
        print(f"📁 Game directory: {Path(__file__).parent.resolve()}")
        print(f"🏠 Working directory: {Path.cwd()}")
        
        gui_available, gui_status = is_gui_available()
        display_available = is_display_available()
        
        print(f"🖥️  Display: {'✅ Available' if display_available else '❌ Not available'}")
        print(f"🎮 GUI Status: {gui_status}")
        
        # Check environment variables
        print(f"🌍 DISPLAY: {os.environ.get('DISPLAY', 'Not set')}")
        print(f"🌍 WAYLAND_DISPLAY: {os.environ.get('WAYLAND_DISPLAY', 'Not set')}")
        
        # File checks
        print("\n📋 FILE STATUS:")
        current_dir = Path(__file__).parent.resolve()
        for file in REQUIRED_FILES + OPTIONAL_FILES:
            file_path = current_dir / file
            if file_path.exists():
                size = file_path.stat().st_size
                print(f"   ✅ {file} ({size} bytes)")
            else:
                print(f"   ❌ {file} (missing)")
        
        print()
        
    except Exception as e:
        print(f"❌ Error displaying system info: {e}")

def install_tkinter_help():
    """Provide platform-specific tkinter installation instructions"""
    print("📋 TKINTER INSTALLATION GUIDE:")
    
    if os.name == 'nt':  # Windows
        print("   🪟 Windows:")
        print("     • Reinstall Python from python.org with 'tcl/tk' option checked")
        print("     • Ensure 'Add Python to PATH' is selected during installation")
    elif sys.platform == 'darwin':  # macOS
        print("   🍎 macOS:")
        print("     • brew install python-tk")
        print("     • Or reinstall Python from python.org")
        print("     • For conda: conda install tk")
    else:  # Linux
        print("   🐧 Linux:")
        print("     • Ubuntu/Debian: sudo apt-get install python3-tk")
        print("     • CentOS/RHEL: sudo yum install tkinter")
        print("     • Fedora: sudo dnf install python3-tkinter")
        print("     • Arch Linux: sudo pacman -S tk")
        print("     • openSUSE: sudo zypper install python3-tk")

def run_text_mode():
    """Run the game in text mode with comprehensive error handling"""
    try:
        print("📖 Loading text-based game engine...")
        
        # Import with specific error handling
        try:
            from game_refactored import main as text_main
        except ImportError as ie:
            print(f"❌ Cannot import game engine: {ie}")
            if 'game_refactored' in str(ie):
                print("📁 game_refactored.py is missing or corrupted")
                print("📂 Please re-download the complete game package")
            else:
                print("📁 Missing game dependency - check file integrity")
            return False
        
        print("🎮 Starting SHABUYA adventure...")
        print()
        
        # Run the game
        text_main()
        return True
        
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted by user. Thanks for exploring SHABUYA!")
        return True
        
    except Exception as e:
        print(f"❌ Game runtime error: {e}")
        
        if '--debug' in sys.argv:
            print("\n🔍 DEBUG TRACEBACK:")
            traceback.print_exc()
        
        print("\n🐛 Please report this issue with:")
        print(f"   📝 Error: {type(e).__name__}: {e}")
        print(f"   🐍 Python: {sys.version}")
        print(f"   💻 Platform: {sys.platform}")
        return False

def run_gui_mode():
    """Attempt to run GUI mode with detailed error handling"""
    try:
        print("🎮 Initializing GUI interface...")
        
        # Import tkinter with specific error handling
        try:
            import tkinter
        except ImportError as ie:
            print("⚠️  tkinter import failed - GUI mode unavailable")
            install_tkinter_help()
            return False
        
        # Import GUI module
        try:
            from gui import main as gui_main
        except ImportError as ie:
            print("⚠️  GUI module import failed")
            print("📁 Ensure gui.py is present and not corrupted")
            if '--debug' in sys.argv:
                print(f"🔍 Import error: {ie}")
            return False
        
        print("🖥️  Launching GUI mode...")
        print("💡 Use --text flag to force text-only mode")
        print()
        
        # Launch GUI
        gui_main()
        return True
        
    except Exception as e:
        error_msg = str(e).lower()
        print(f"⚠️  GUI startup failed: {e}")
        
        # Provide specific guidance based on error type
        if any(keyword in error_msg for keyword in ['display', 'screen', 'x11']):
            print("🖥️  Display connection issue detected")
            print("💡 This usually means:")
            print("   • Running in a headless environment (server/cloud)")
            print("   • X11 forwarding not enabled")
            print("   • Display server not running")
        elif 'permission' in error_msg:
            print("🔐 File permission issue detected")
            print("💡 Try: chmod +x gui.py")
        elif 'memory' in error_msg:
            print("🧠 Memory issue detected")
            print("💡 Close other applications and try again")
        
        if '--debug' in sys.argv:
            print("\n🔍 DEBUG TRACEBACK:")
            traceback.print_exc()
            
        print("🔄 Will attempt text mode fallback...")
        return False

def main():
    """Main launcher function with comprehensive checks and error handling"""
    
    try:
        # Validate command line arguments
        if not validate_arguments():
            return
        
        # System compatibility checks
        if not check_python_version():
            input("Press Enter to exit...")
            return
        
        if not check_game_files():
            input("Press Enter to exit...")
            return
        
        # Display welcome banner
        print_welcome()
        
        # Debug mode
        if "--debug" in sys.argv:
            print_system_info()
        
        # Determine launch mode - PRIORITIZE WORKING TEXT MODE
        force_text_mode = "--text" in sys.argv
        force_gui_mode = "--gui" in sys.argv
        
        if force_gui_mode and not force_text_mode:
            # Only try GUI if explicitly requested and text mode not forced
            display_available = is_display_available()
            gui_available, gui_status = is_gui_available()
            
            if display_available and gui_available:
                print("🎮 GUI MODE (forced via --gui flag)")
                gui_success = run_gui_mode()
                
                if gui_success:
                    return  # GUI launched successfully
                
                print("🔄 GUI failed - falling back to text mode...")
                success = run_text_mode()
            else:
                print(f"🖥️  GUI unavailable: {gui_status}")
                print("� Falling back to text mode...")
                success = run_text_mode()
        else:
            # Default to reliable text mode (unless GUI specifically requested)
            if force_text_mode:
                print("🖥️  TEXT MODE (forced via --text flag)")
            else:
                print("�️  STARTING GAME (text interface)")
                print("💡 Use --gui flag to attempt GUI mode")
            success = run_text_mode()
        
        # Final status
        if success:
            print("\n🎯 Game session completed successfully!")
        else:
            print("\n⚠️  Game session ended with issues")
            
    except KeyboardInterrupt:
        print("\n\n👋 Launcher interrupted. Thanks for trying SHABUYA!")
    except Exception as e:
        print(f"\n❌ Fatal launcher error: {e}")
        
        if '--debug' in sys.argv:
            print("\n🔍 FATAL ERROR TRACEBACK:")
            traceback.print_exc()
        
        print("\n🐛 Please report this critical issue:")
        print(f"   📝 Error: {type(e).__name__}: {e}")
        print(f"   🐍 Python: {sys.version}")
        print(f"   💻 Platform: {sys.platform}")
        print(f"   📁 Directory: {Path(__file__).parent}")
        
        input("Press Enter to exit...")

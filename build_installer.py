#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Build Script
Creates distributable package for desktop installation
"""

import os
import shutil
from pathlib import Path
import sys

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'main.py',
        'game_refactored.py',
        'player.py',
        'combat.py',
        'scenes.py',
        'item.py',
        'ui.py',
        'config.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   • {file}")
        return False
    
    print("✅ All required files found!")
    return True

def create_launcher():
    """Create the desktop launcher"""
    launcher_code = '''#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Desktop Launcher
Simple game launcher for desktop distribution
"""

import tkinter as tk
from tkinter import messagebox
import os
import sys
from pathlib import Path

class ShabuyaLauncher:
    def __init__(self):
        self.version = "1.0.0"
        self.game_dir = Path(__file__).parent
        
        self.root = tk.Tk()
        self.setup_launcher()
        
    def setup_launcher(self):
        """Setup launcher window"""
        self.root.title("🗻 SHABUYA Cave Adventure - Launcher")
        self.root.geometry("500x600")
        self.root.configure(bg='#2c1810')
        self.root.resizable(False, False)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"500x600+{x}+{y}")
        
        self.create_ui()
        
    def create_ui(self):
        """Create launcher UI"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c1810')
        title_frame.pack(pady=40)
        
        tk.Label(title_frame, text="🗻 SHABUYA", font=("Arial", 32, "bold"), 
                fg='#DAA520', bg='#2c1810').pack()
        tk.Label(title_frame, text="Cave Adventure", font=("Arial", 20), 
                fg='#CD853F', bg='#2c1810').pack()
        tk.Label(title_frame, text=f"Version {self.version}", font=("Arial", 12),
                fg='#8B4513', bg='#2c1810').pack(pady=(10, 0))
        
        # Status
        self.status_var = tk.StringVar(value="Ready to launch!")
        status_label = tk.Label(self.root, textvariable=self.status_var, 
                               font=("Arial", 11), fg='#CD853F', bg='#2c1810')
        status_label.pack(pady=20)
        
        # Main buttons
        button_frame = tk.Frame(self.root, bg='#2c1810')
        button_frame.pack(pady=30)
        
        # Play button
        self.play_btn = tk.Button(button_frame, text="🎮 PLAY GAME", 
                                 font=("Arial", 16, "bold"), bg='#228B22', fg='white',
                                 width=20, height=2, command=self.launch_game)
        self.play_btn.pack(pady=10)
        
        # Mode selection
        mode_frame = tk.Frame(button_frame, bg='#2c1810')
        mode_frame.pack(pady=10)
        
        tk.Button(mode_frame, text="🖥️ GUI Mode", font=("Arial", 12),
                 bg='#4682B4', fg='white', width=12,
                 command=self.launch_gui).pack(side=tk.LEFT, padx=5)
        tk.Button(mode_frame, text="📝 Text Mode", font=("Arial", 12),
                 bg='#8B4513', fg='white', width=12,
                 command=self.launch_text).pack(side=tk.RIGHT, padx=5)
        
        # Exit button
        exit_btn = tk.Button(button_frame, text="❌ Exit", 
                            font=("Arial", 12), bg='#8B0000', fg='white',
                            width=20, command=self.root.quit)
        exit_btn.pack(pady=20)
        
    def launch_game(self):
        """Launch the main game (auto-detect mode)"""
        self.status_var.set("Launching game...")
        self.play_btn.config(state='disabled')
        
        try:
            # Try GUI first, fallback to text
            if (self.game_dir / 'gui.py').exists():
                self.launch_gui()
            else:
                self.launch_text()
        except Exception as e:
            messagebox.showerror("Launch Error", f"Failed to start game: {e}")
        finally:
            self.status_var.set("Ready to launch!")
            self.play_btn.config(state='normal')
    
    def launch_gui(self):
        """Launch GUI mode"""
        try:
            if (self.game_dir / 'gui.py').exists():
                import gui
                self.root.withdraw()  # Hide launcher
                gui.main()
                self.root.deiconify()  # Show launcher again
            else:
                messagebox.showwarning("GUI Not Available", 
                                     "GUI mode not found. Launching text mode instead.")
                self.launch_text()
        except Exception as e:
            messagebox.showerror("GUI Error", f"GUI failed: {e}\\nTrying text mode...")
            self.launch_text()
    
    def launch_text(self):
        """Launch text mode"""
        try:
            import main
            self.root.withdraw()  # Hide launcher
            main.main()
            self.root.deiconify()  # Show launcher again
        except Exception as e:
            messagebox.showerror("Launch Error", f"Failed to start text mode: {e}")
            
    def run(self):
        """Start the launcher"""
        self.root.mainloop()

def main():
    """Main launcher entry point"""
    try:
        launcher = ShabuyaLauncher()
        launcher.run()
    except Exception as e:
        messagebox.showerror("Launcher Error", f"Failed to start launcher: {e}")
        # Fallback - try to run game directly
        try:
            import main
            main.main()
        except:
            print("Could not start game. Please check installation.")

if __name__ == "__main__":
    main()
'''
    
    with open('launcher.py', 'w') as f:
        f.write(launcher_code)
    
    print("✅ Launcher created: launcher.py")

def create_distribution():
    """Create distribution package without PyInstaller"""
    print("📦 Creating Python distribution package...")
    
    dist_dir = Path('distribution')
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    
    dist_dir.mkdir()
    
    # Copy all game files
    game_files = [
        'main.py', 'launcher.py', 'game_refactored.py', 'player.py',
        'combat.py', 'scenes.py', 'item.py', 'ui.py', 'config.py'
    ]
    
    # Also copy GUI if it exists
    if Path('gui.py').exists():
        game_files.append('gui.py')
    
    copied_files = []
    for file in game_files:
        if Path(file).exists():
            shutil.copy2(file, dist_dir / file)
            copied_files.append(file)
            print(f"   ✅ Copied {file}")
    
    # Create start scripts for different platforms
    
    # Windows batch file
    with open(dist_dir / 'START_GAME.bat', 'w') as f:
        f.write('''@echo off
title SHABUYA Cave Adventure Launcher
echo.
echo 🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻
echo 🗻                                           🗻
echo 🗻        SHABUYA - CAVE ADVENTURE          🗻  
echo 🗻           Loading Launcher...            🗻
echo ��                                           🗻
echo 🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻
echo.

if exist "launcher.py" (
    echo Starting launcher...
    python launcher.py
) else if exist "main.py" (
    echo Launcher not found, starting game directly...
    python main.py
) else (
    echo ERROR: Game files not found!
    echo Please make sure all game files are in this folder.
    pause
    exit
)

if errorlevel 1 (
    echo.
    echo ❌ Error starting game!
    echo.
    echo Troubleshooting:
    echo 1. Make sure Python 3.7+ is installed
    echo 2. Try running: python --version
    echo 3. Install Python from: https://python.org
    echo.
    pause
)
''')
    
    # Linux/Mac shell script
    with open(dist_dir / 'start_game.sh', 'w') as f:
        f.write('''#!/bin/bash

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
''')
    
    # Make shell script executable
    os.chmod(dist_dir / 'start_game.sh', 0o755)
    
    # Create comprehensive README
    readme_content = f"""
# 🗻 SHABUYA Cave Adventure - Distribution Package

## 🚀 Quick Start Guide

### Windows Users:
1. **Double-click `START_GAME.bat`**
2. The launcher will open automatically
3. Click "🎮 PLAY GAME" to start your adventure!

### Linux/Mac Users:
1. **Open terminal in this folder**
2. **Run: `./start_game.sh`**
3. Or run: `python3 launcher.py`

### Alternative Launch Methods:
- **Direct game launch**: `python3 main.py`
- **Force text mode**: `python3 main.py --text`
- **Debug mode**: `python3 main.py --debug`

## 📋 System Requirements

- **Python 3.7 or higher** (Download from https://python.org)
- **Operating System**: Windows 10+, Linux, or macOS
- **Memory**: 50MB free space
- **Display**: Any resolution (GUI mode), or terminal (text mode)

## 🎮 Game Features

### 🏛️ Choose Your Class:
- **⚔️ Warrior** - High health and strength, perfect for beginners
- **🗡️ Rogue** - Fast and agile, high critical hit chance  
- **🧙 Mage** - Powerful magic attacks, but lower health

### 🗺️ Game Modes:
- **🖥️ GUI Mode** - Beautiful graphical interface (if available)
- **📝 Text Mode** - Classic text-based adventure
- **🎯 Auto-detect** - Game chooses the best mode for your system

### ⚔️ Combat System:
- **Strategic turn-based combat**
- **Level up and increase your stats**
- **Multiple enemy types with unique abilities**
- **Epic boss battles**

## 📁 Package Contents

This distribution includes:
{chr(10).join([f'✅ {file}' for file in copied_files])}
✅ START_GAME.bat (Windows launcher)
✅ start_game.sh (Linux/Mac launcher)
✅ README.txt (this file)

## 🛠️ Troubleshooting

### "Python not found" Error:
1. **Install Python** from https://python.org
2. **During installation**, check "Add Python to PATH"
3. **Restart your computer** after installation
4. **Test**: Open command prompt/terminal and type `python --version`

### GUI Not Working:
1. **Try text mode**: `python3 main.py --text`
2. **Install tkinter**: 
   - Windows: Reinstall Python with tcl/tk option
   - Linux: `sudo apt-get install python3-tk`
   - Mac: `brew install python-tk`

### Permission Denied (Linux/Mac):
1. **Make script executable**: `chmod +x start_game.sh`
2. **Or run directly**: `python3 launcher.py`

### Game Won't Start:
1. **Check all files are present** in the same folder
2. **Try debug mode**: `python3 main.py --debug`
3. **Update Python** to version 3.7 or higher

## 🎯 Game Tips

- **Save often** - The caves can be dangerous!
- **Explore thoroughly** - Hidden treasures await
- **Choose your battles** - Sometimes retreat is wise
- **Level up** - Stronger enemies require preparation
- **Read descriptions** - Important clues are everywhere

## 🌟 Story

You are an adventurer who has come to the mysterious caves of Mount Shabuya. 
Legends speak of ancient treasures hidden deep within, but also of terrible 
dangers that guard them. 

Choose your class wisely, for the path ahead is treacherous. Will you emerge 
as a hero with pockets full of gold, or become another lost soul in the depths?

The adventure begins now...

## 📞 Support

- **Found a bug?** Please report it on GitHub
- **Need help?** Check the troubleshooting section above
- **Want to contribute?** Pull requests welcome!

---

**Have fun exploring the caves of Mount Shabuya!** 🗻⚔️✨

Made with ❤️ by the SHABUYA Development Team
"""
    
    with open(dist_dir / 'README.txt', 'w') as f:
        f.write(readme_content)
    
    # Create a requirements.txt file
    with open(dist_dir / 'requirements.txt', 'w') as f:
        f.write("""# SHABUYA Cave Adventure - Python Requirements
# 
# This game uses only Python standard library modules.
# No additional packages need to be installed!
#
# Minimum Python version: 3.7
#
# Standard library modules used:
# - tkinter (for GUI mode)
# - random (for game mechanics)  
# - json (for save/load functionality)
# - pathlib (for file handling)
# - sys (for system integration)
# - os (for cross-platform compatibility)

# For GUI mode, ensure tkinter is available:
# Windows: Install Python with tcl/tk option checked
# Linux: sudo apt-get install python3-tk
# Mac: brew install python-tk
""")
    
    print(f"✅ Distribution package created in: {dist_dir}")
    print("\n📁 Package Contents:")
    for item in sorted(dist_dir.iterdir()):
        size = item.stat().st_size if item.is_file() else "DIR"
        print(f"   📄 {item.name:<20} ({size} bytes)" if size != "DIR" else f"   📁 {item.name}")

def create_zip_package():
    """Create a zip file for easy distribution"""
    import zipfile
    
    dist_dir = Path('distribution')
    if not dist_dir.exists():
        print("❌ Distribution folder not found. Run create_distribution() first.")
        return
    
    zip_path = Path('SHABUYA-Cave-Adventure-v1.0.zip')
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in dist_dir.rglob('*'):
            if file_path.is_file():
                # Add to zip with relative path
                arcname = file_path.relative_to(dist_dir.parent)
                zipf.write(file_path, arcname)
    
    print(f"✅ Zip package created: {zip_path}")
    print(f"📦 Size: {zip_path.stat().st_size} bytes")

def main():
    """Main build function"""
    print("🗻 SHABUYA Cave Adventure - Distribution Builder")
    print("=" * 60)
    print("Building Python distribution package (no compilation needed)")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Build failed - missing required files")
        print("Please ensure all game files are in the current directory.")
        return
    
    # Create launcher
    create_launcher()
    
    # Create distribution package  
    create_distribution()
    
    # Create zip package
    create_zip_package()
    
    print("\n" + "=" * 60)
    print("🎉 BUILD COMPLETE!")
    print("=" * 60)
    print("📦 Your game is ready for distribution!")
    print("\n🚀 Distribution Options:")
    print("   1. Share the 'distribution' folder")
    print("   2. Upload 'SHABUYA-Cave-Adventure-v1.0.zip' to GitHub releases")
    print("   3. Send the zip file directly to players")
    print("\n📋 Players just need to:")
    print("   1. Extract the zip file")  
    print("   2. Double-click START_GAME.bat (Windows) or run ./start_game.sh (Linux/Mac)")
    print("   3. Enjoy the adventure!")
    print("\n✨ No Python knowledge required for players!")

if __name__ == "__main__":
    main()

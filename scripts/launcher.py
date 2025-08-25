#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Professional Desktop Launcher
Clean launcher interface for game distribution
"""

import tkinter as tk
from tkinter import messagebox
import os
import sys
import subprocess
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class ShabuyaLauncher:
    """Professional game launcher with clean interface"""
    
    def __init__(self):
        self.version = "1.0.0"
        self.game_dir = project_root
        
        self.root = tk.Tk()
        self.setup_launcher()
        
    def setup_launcher(self):
        """Setup launcher window"""
        self.root.title("🗻 SHABUYA Cave Adventure - Launcher")
        self.root.geometry("400x500")
        self.root.configure(bg='#2c1810')
        self.root.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # Create UI
        self.create_ui()
        
    def center_window(self):
        """Center the launcher window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"400x500+{x}+{y}")
        
    def create_ui(self):
        """Create launcher user interface"""
        # Title section
        title_frame = tk.Frame(self.root, bg='#2c1810')
        title_frame.pack(pady=30)
        
        tk.Label(title_frame, text="🗻 SHABUYA", 
                font=("Arial", 28, "bold"), 
                fg='#DAA520', bg='#2c1810').pack()
        tk.Label(title_frame, text="Cave Adventure", 
                font=("Arial", 16), 
                fg='#CD853F', bg='#2c1810').pack()
        tk.Label(title_frame, text=f"Version {self.version}", 
                font=("Arial", 10),
                fg='#8B4513', bg='#2c1810').pack(pady=(10, 0))
        
        # Status display
        self.status_var = tk.StringVar(value="Ready to launch!")
        status_label = tk.Label(self.root, textvariable=self.status_var, 
                               font=("Arial", 11), fg='#90EE90', bg='#2c1810')
        status_label.pack(pady=(20, 30))
        
        # Launch buttons
        button_frame = tk.Frame(self.root, bg='#2c1810')
        button_frame.pack(pady=20)
        
        # Main launch button
        launch_btn = tk.Button(button_frame, text="🚀 Start Adventure", 
                              font=("Arial", 14, "bold"),
                              bg='#228B22', fg='white', width=20, height=2,
                              relief=tk.RAISED, bd=3,
                              command=self.launch_game)
        launch_btn.pack(pady=10)
        
        # Mode selection buttons
        mode_frame = tk.Frame(self.root, bg='#2c1810')
        mode_frame.pack(pady=20)
        
        tk.Label(mode_frame, text="Choose Launch Mode:", 
                font=("Arial", 12, "bold"),
                fg='#DAA520', bg='#2c1810').pack(pady=(0, 10))
        
        tk.Button(mode_frame, text="🖼️ GUI Mode", 
                 font=("Arial", 11), bg='#4682B4', fg='white', width=15,
                 command=self.launch_gui_mode).pack(pady=2)
        
        tk.Button(mode_frame, text="📝 Text Mode", 
                 font=("Arial", 11), bg='#8B4513', fg='white', width=15,
                 command=self.launch_text_mode).pack(pady=2)
        
        # Information buttons
        info_frame = tk.Frame(self.root, bg='#2c1810')
        info_frame.pack(pady=30)
        
        tk.Button(info_frame, text="📖 Instructions", 
                 font=("Arial", 10), bg='#556B2F', fg='white', width=12,
                 command=self.show_instructions).pack(side=tk.LEFT, padx=5)
        
        tk.Button(info_frame, text="ℹ️ About", 
                 font=("Arial", 10), bg='#556B2F', fg='white', width=12,
                 command=self.show_about).pack(side=tk.LEFT, padx=5)
        
        # Exit button
        tk.Button(self.root, text="❌ Exit", 
                 font=("Arial", 10), bg='#8B0000', fg='white', width=15,
                 command=self.root.quit).pack(pady=(30, 20))
        
    def update_status(self, message, color='#90EE90'):
        """Update status message"""
        self.status_var.set(message)
        self.root.update()
        
    def launch_game(self):
        """Launch the game with auto-detection"""
        self.update_status("Starting game...", '#FFD700')
        try:
            main_script = self.game_dir / "scripts" / "main.py"
            if main_script.exists():
                subprocess.Popen([sys.executable, str(main_script)])
                self.update_status("Game launched successfully!")
                self.root.after(2000, self.root.quit)  # Close after 2 seconds
            else:
                raise FileNotFoundError("Main game script not found")
        except Exception as e:
            messagebox.showerror("Launch Error", f"Failed to start game: {e}")
            self.update_status("Launch failed", '#FF6B6B')
            
    def launch_gui_mode(self):
        """Launch specifically in GUI mode"""
        self.update_status("Starting GUI mode...", '#FFD700')
        try:
            main_script = self.game_dir / "scripts" / "main.py"
            subprocess.Popen([sys.executable, str(main_script), "--gui"])
            self.update_status("GUI mode launched!")
            self.root.after(2000, self.root.quit)
        except Exception as e:
            messagebox.showerror("Launch Error", f"Failed to start GUI mode: {e}")
            self.update_status("Launch failed", '#FF6B6B')
            
    def launch_text_mode(self):
        """Launch specifically in text mode"""
        self.update_status("Starting text mode...", '#FFD700')
        try:
            main_script = self.game_dir / "scripts" / "main.py"
            subprocess.Popen([sys.executable, str(main_script), "--text"])
            self.update_status("Text mode launched!")
            self.root.after(2000, self.root.quit)
        except Exception as e:
            messagebox.showerror("Launch Error", f"Failed to start text mode: {e}")
            self.update_status("Launch failed", '#FF6B6B')
            
    def show_instructions(self):
        """Show game instructions"""
        instructions = """🎮 SHABUYA Cave Adventure - How to Play

📖 STORY:
Awaken in a mysterious cave and embark on an epic adventure
through dangerous scenes, battling creatures and uncovering secrets.

🎯 GAMEPLAY:
• Choose your character class (Rogue, Warrior, Mage)
• Navigate interconnected scenes
• Battle creatures and collect items
• Upgrade your stats and abilities
• Unlock new areas and face challenging bosses

⚔️ CLASSES:
• Rogue: Agility-based, stealth attacks
• Warrior: Strength-based, powerful melee
• Mage: Intelligence-based, magical abilities

🏆 OBJECTIVE:
Reach and defeat the final boss to complete your adventure!

💡 TIPS:
• Each class has unique strengths
• Find enhanced weapons in the Armory
• Meet stat requirements for powerful abilities
• Explore thoroughly for hidden secrets"""
        
        messagebox.showinfo("Game Instructions", instructions)
        
    def show_about(self):
        """Show about information"""
        about_text = f"""🗻 SHABUYA Cave Adventure

Version: {self.version}
Developer: Professional Game Development
Engine: Python with Tkinter GUI

A professionally crafted text-based adventure game
featuring multiple character classes, combat systems,
and an immersive storyline.

© 2024 - All Rights Reserved

Built with clean, maintainable code architecture
suitable for portfolio demonstration."""
        
        messagebox.showinfo("About SHABUYA", about_text)
        
    def run(self):
        """Run the launcher"""
        self.root.mainloop()


def main():
    """Main launcher function"""
    try:
        launcher = ShabuyaLauncher()
        launcher.run()
    except Exception as e:
        messagebox.showerror("Launcher Error", f"Failed to start launcher: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

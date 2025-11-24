#!/usr/bin/env python3
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
            messagebox.showerror("GUI Error", f"GUI failed: {e}\nTrying text mode...")
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

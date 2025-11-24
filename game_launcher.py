#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Game Launcher
=====================================
Choose between development mode and player mode
"""

import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import sys
import os

class GameLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SHABUYA Cave Adventure - Launcher")
        self.root.geometry("600x400")
        self.root.configure(bg='#0a0a0a')
        
        self.create_ui()
        
    def create_ui(self):
        """Create the launcher interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg='#0a0a0a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="SHABUYA CAVE ADVENTURE", 
                         font=('Arial', 24, 'bold'), fg='#00ff88', bg='#0a0a0a')
        title.pack(pady=20)
        
        subtitle = tk.Label(main_frame, text="Choose Your Experience", 
                           font=('Arial', 14), fg='#cccccc', bg='#0a0a0a')
        subtitle.pack(pady=10)
        
        # Mode selection
        mode_frame = tk.Frame(main_frame, bg='#0a0a0a')
        mode_frame.pack(pady=30)
        
        # Player Mode Button
        player_frame = tk.LabelFrame(mode_frame, text="Player Mode", 
                                    fg='#44ff44', bg='#1a1a1a', font=('Arial', 12, 'bold'))
        player_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        player_desc = tk.Label(player_frame, 
                               text="Linear gameplay experience\nProgressive story and exploration\nCharacter progression system\nSave/Load functionality",
                               fg='#cccccc', bg='#1a1a1a', font=('Arial', 10), justify=tk.LEFT)
        player_desc.pack(padx=15, pady=15)
        
        player_btn = tk.Button(player_frame, text="PLAY GAME", 
                              command=self.launch_player_mode,
                              bg='#44ff44', fg='black', font=('Arial', 12, 'bold'),
                              width=15, height=2)
        player_btn.pack(pady=15)
        
        # Development Mode Button
        dev_frame = tk.LabelFrame(mode_frame, text="Development Mode", 
                                 fg='#ff8844', bg='#1a1a1a', font=('Arial', 12, 'bold'))
        dev_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        
        dev_desc = tk.Label(dev_frame, 
                            text="Asset testing and development\nScene and character switching\nQuick test scenarios\nDevelopment tools",
                            fg='#cccccc', bg='#1a1a1a', font=('Arial', 10), justify=tk.LEFT)
        dev_desc.pack(padx=15, pady=15)
        
        dev_btn = tk.Button(dev_frame, text="DEV MODE", 
                           command=self.launch_dev_mode,
                           bg='#ff8844', fg='black', font=('Arial', 12, 'bold'),
                           width=15, height=2)
        dev_btn.pack(pady=15)
        
        # Info section
        info_frame = tk.LabelFrame(main_frame, text="Game Information", 
                                  fg='#8888ff', bg='#1a1a1a', font=('Arial', 11, 'bold'))
        info_frame.pack(fill=tk.X, pady=20)
        
        info_text = tk.Label(info_frame, 
                            text="• 7 Character Sprites • 15+ Background Scenes • Turn-based Combat • Progressive Story",
                            fg='#cccccc', bg='#1a1a1a', font=('Arial', 10))
        info_text.pack(pady=10)
        
        # Exit button
        exit_btn = tk.Button(main_frame, text="Exit", 
                            command=self.root.quit,
                            bg='#666666', fg='white', font=('Arial', 10))
        exit_btn.pack(pady=10)
        
    def launch_player_mode(self):
        """Launch the player-focused game"""
        try:
            self.root.withdraw()  # Hide launcher window
            # Get the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            player_gui_path = os.path.join(script_dir, "player_gui.py")
            subprocess.run([sys.executable, player_gui_path])
            self.root.deiconify()  # Show launcher window again
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch player mode: {e}")
            self.root.deiconify()
            
    def launch_dev_mode(self):
        """Launch the development mode"""
        try:
            self.root.withdraw()  # Hide launcher window
            # Get the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            dev_gui_path = os.path.join(script_dir, "enhanced_gui_final.py")
            subprocess.run([sys.executable, dev_gui_path])
            self.root.deiconify()  # Show launcher window again
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch dev mode: {e}")
            self.root.deiconify()
            
    def run(self):
        """Start the launcher"""
        self.root.mainloop()

if __name__ == "__main__":
    print("SHABUYA Cave Adventure - Launcher")
    print("=" * 50)
    print("Choose your gaming experience!")
    print("=" * 50)
    
    launcher = GameLauncher()
    launcher.run()

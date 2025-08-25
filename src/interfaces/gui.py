#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Simplified Desktop GUI
Clean, simple interface integrated with the main game engine
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Import game modules
from src.core.game_engine import main as game_main
from src.core.game_events import start_game
from src.interfaces.ui import title_screen


class SimpleGameGUI:
    """Simplified GUI wrapper for the cave game"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_interface()
        
    def setup_window(self):
        """Setup main window"""
        self.root.title("🗻 SHABUYA - Cave Adventure")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c1810')
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"800x600+{x}+{y}")
        
    def create_interface(self):
        """Create the simplified game interface"""
        # Title
        title_label = tk.Label(self.root, text="🗻 SHABUYA - CAVE ADVENTURE 🗻", 
                              font=("Arial", 18, "bold"), fg='#DAA520', bg='#2c1810')
        title_label.pack(pady=20)
        
        # Game display area
        display_frame = tk.LabelFrame(self.root, text="📖 Adventure", 
                                     font=("Arial", 12, "bold"),
                                     fg='#DAA520', bg='#3c2820', 
                                     relief=tk.RAISED, bd=2)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        self.game_display = scrolledtext.ScrolledText(
            display_frame, 
            bg='#1a0f08', 
            fg='#DAA520',
            font=("Courier", 11), 
            relief=tk.SUNKEN, 
            bd=2,
            wrap=tk.WORD, 
            state=tk.DISABLED
        )
        self.game_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg='#2c1810')
        button_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        tk.Button(button_frame, text="🎯 Start New Game", 
                 font=("Arial", 12, "bold"),
                 bg='#228B22', fg='white', 
                 command=self.start_game).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(button_frame, text="📖 Instructions", 
                 font=("Arial", 12),
                 bg='#4682B4', fg='white', 
                 command=self.show_instructions).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(button_frame, text="❌ Exit", 
                 font=("Arial", 12),
                 bg='#8B0000', fg='white', 
                 command=self.root.quit).pack(side=tk.RIGHT)
        
        # Initial welcome message
        self.display_text("Welcome to SHABUYA Cave Adventure!")
        self.display_text("Click 'Start New Game' to begin your journey...")
        
    def display_text(self, text):
        """Display text in the game area"""
        self.game_display.config(state=tk.NORMAL)
        self.game_display.insert(tk.END, text + "\n")
        self.game_display.see(tk.END)
        self.game_display.config(state=tk.DISABLED)
        
    def start_game(self):
        """Start a new game"""
        self.game_display.config(state=tk.NORMAL)
        self.game_display.delete(1.0, tk.END)
        self.game_display.config(state=tk.DISABLED)
        
        self.display_text("Starting new game...")
        self.display_text("=" * 50)
        self.display_text("Note: This GUI provides a simplified interface.")
        self.display_text("For the full game experience, use the text mode.")
        self.display_text("You can launch text mode by running main.py directly.")
        self.display_text("=" * 50)
        
        # Show basic game info
        self.display_text("\n🗻 SHABUYA - Cave Adventure 🗻")
        self.display_text("\nYou find yourself in a mysterious cave...")
        self.display_text("Your adventure begins now!")
        
        # Add some basic controls info
        self.display_text("\n📝 Quick Guide:")
        self.display_text("• This is a text-based adventure game")
        self.display_text("• Navigate through different scenes")
        self.display_text("• Choose your character class carefully")
        self.display_text("• Collect items and improve your stats")
        self.display_text("• Defeat enemies to progress")
        
        self.display_text("\n⚠️  For full gameplay, please use text mode!")
        
    def show_instructions(self):
        """Show game instructions"""
        instructions = """
🎮 SHABUYA Cave Adventure - Instructions

📖 STORY:
You awaken in a mysterious cave and must navigate through
dangerous scenes, battle creatures, and uncover secrets
to complete your adventure.

🎯 GAMEPLAY:
• Choose your character class (Rogue, Warrior, or Mage)
• Each class has unique weapons and abilities
• Navigate through interconnected scenes
• Battle creatures and bosses
• Collect items and upgrade your stats
• Solve puzzles and unlock new areas

⚔️ COMBAT:
• Use class-specific weapons effectively
• Meet stat requirements for powerful attacks
• Find enhanced weapons in the Armory
• Use class abilities strategically

🏆 GOAL:
Reach the final boss and defeat the Divine Heart
to complete your adventure!

💡 TIP:
For the complete experience with full interactivity,
run the game in text mode using main.py
        """
        
        messagebox.showinfo("Game Instructions", instructions)
        
    def run(self):
        """Run the GUI"""
        self.root.mainloop()


def main():
    """Main function to run the simplified GUI"""
    try:
        app = SimpleGameGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start GUI: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

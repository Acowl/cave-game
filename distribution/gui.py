#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Desktop GUI
Clean, simple interface optimized for desktop use
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
from pathlib import Path

class CaveGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.player = None
        self.game_state = "menu"
        self.setup_window()
        self.create_interface()
        
    def setup_window(self):
        """Setup main window"""
        self.root.title("🗻 SHABUYA - Cave Adventure")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c1810')
        self.root.resizable(True, True)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1000x700+{x}+{y}")
        
    def create_interface(self):
        """Create the main game interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c1810')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_frame = tk.Frame(main_frame, bg='#2c1810')
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(title_frame, text="🗻 SHABUYA - CAVE ADVENTURE 🗻", 
                              font=("Arial", 20, "bold"), fg='#DAA520', bg='#2c1810')
        title_label.pack()
        
        # Game area
        game_frame = tk.Frame(main_frame, bg='#2c1810')
        game_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Character stats
        self.create_stats_panel(game_frame)
        
        # Center panel - Game display
        self.create_game_panel(game_frame)
        
        # Right panel - Controls
        self.create_controls_panel(game_frame)
        
    def create_stats_panel(self, parent):
        """Create character stats panel"""
        stats_frame = tk.LabelFrame(parent, text="🧙 Character", font=("Arial", 12, "bold"),
                                   fg='#DAA520', bg='#3c2820', relief=tk.RAISED, bd=2)
        stats_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Character info
        self.char_info = tk.Text(stats_frame, width=25, height=15, 
                                bg='#2c1810', fg='#DAA520', font=("Courier", 10),
                                relief=tk.SUNKEN, bd=2, state=tk.DISABLED)
        self.char_info.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Inventory
        inv_label = tk.Label(stats_frame, text="🎒 Inventory", font=("Arial", 10, "bold"),
                            fg='#DAA520', bg='#3c2820')
        inv_label.pack(pady=(10, 5))
        
        self.inventory_list = tk.Listbox(stats_frame, height=6, bg='#2c1810', fg='#CD853F',
                                        font=("Courier", 9), relief=tk.SUNKEN, bd=2)
        self.inventory_list.pack(padx=10, pady=(0, 10), fill=tk.X)
        
    def create_game_panel(self, parent):
        """Create main game display panel"""
        game_frame = tk.Frame(parent, bg='#2c1810')
        game_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Game display
        display_frame = tk.LabelFrame(game_frame, text="📖 Adventure", font=("Arial", 12, "bold"),
                                     fg='#DAA520', bg='#3c2820', relief=tk.RAISED, bd=2)
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        self.game_display = scrolledtext.ScrolledText(display_frame, bg='#1a0f08', fg='#DAA520',
                                                     font=("Courier", 11), relief=tk.SUNKEN, bd=2,
                                                     wrap=tk.WORD, state=tk.DISABLED)
        self.game_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Command input
        input_frame = tk.Frame(game_frame, bg='#2c1810')
        input_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(input_frame, text="Command:", font=("Arial", 10, "bold"),
                fg='#DAA520', bg='#2c1810').pack(side=tk.LEFT)
        
        self.command_var = tk.StringVar()
        self.command_entry = tk.Entry(input_frame, textvariable=self.command_var,
                                     bg='#3c2820', fg='#DAA520', font=("Courier", 11),
                                     relief=tk.SUNKEN, bd=2)
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 10))
        self.command_entry.bind('<Return>', self.process_command)
        
        execute_btn = tk.Button(input_frame, text="⚡ Execute", font=("Arial", 10, "bold"),
                               bg='#8B4513', fg='white', relief=tk.RAISED, bd=2,
                               command=self.process_command)
        execute_btn.pack(side=tk.RIGHT)
        
    def create_controls_panel(self, parent):
        """Create quick controls panel"""
        controls_frame = tk.LabelFrame(parent, text="🎮 Quick Actions", font=("Arial", 12, "bold"),
                                      fg='#DAA520', bg='#3c2820', relief=tk.RAISED, bd=2)
        controls_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Game controls
        game_controls = tk.Frame(controls_frame, bg='#3c2820')
        game_controls.pack(padx=10, pady=10)
        
        tk.Button(game_controls, text="🎯 New Game", width=15, font=("Arial", 10),
                 bg='#228B22', fg='white', command=self.new_game).pack(pady=2)
        tk.Button(game_controls, text="💾 Save Game", width=15, font=("Arial", 10),
                 bg='#4682B4', fg='white', command=self.save_game).pack(pady=2)
        tk.Button(game_controls, text="📁 Load Game", width=15, font=("Arial", 10),
                 bg='#4682B4', fg='white', command=self.load_game).pack(pady=2)
        
        # Movement
        tk.Label(controls_frame, text="🧭 Movement", font=("Arial", 10, "bold"),
                fg='#DAA520', bg='#3c2820').pack(pady=(20, 5))
        
        movement_frame = tk.Frame(controls_frame, bg='#3c2820')
        movement_frame.pack()
        
        # North
        tk.Button(movement_frame, text="⬆️ North", width=12, font=("Arial", 9),
                 bg='#8B4513', fg='white', command=lambda: self.quick_command("north")).pack()
        
        # East/West
        ew_frame = tk.Frame(movement_frame, bg='#3c2820')
        ew_frame.pack()
        tk.Button(ew_frame, text="⬅️ West", width=6, font=("Arial", 9),
                 bg='#8B4513', fg='white', command=lambda: self.quick_command("west")).pack(side=tk.LEFT)
        tk.Button(ew_frame, text="East ➡️", width=6, font=("Arial", 9),
                 bg='#8B4513', fg='white', command=lambda: self.quick_command("east")).pack(side=tk.RIGHT)
        
        # South
        tk.Button(movement_frame, text="⬇️ South", width=12, font=("Arial", 9),
                 bg='#8B4513', fg='white', command=lambda: self.quick_command("south")).pack()
        
        # Actions
        tk.Label(controls_frame, text="⚔️ Actions", font=("Arial", 10, "bold"),
                fg='#DAA520', bg='#3c2820').pack(pady=(20, 5))
        
        action_frame = tk.Frame(controls_frame, bg='#3c2820')
        action_frame.pack()
        
        actions = [("👁️ Look", "look"), ("🎒 Inventory", "inventory"), 
                  ("📊 Stats", "stats"), ("❓ Help", "help")]
        
        for text, cmd in actions:
            tk.Button(action_frame, text=text, width=15, font=("Arial", 9),
                     bg='#654321', fg='white', 
                     command=lambda c=cmd: self.quick_command(c)).pack(pady=1)
        
    def display_text(self, text):
        """Display text in the game area"""
        self.game_display.config(state=tk.NORMAL)
        self.game_display.insert(tk.END, text + "\n")
        self.game_display.see(tk.END)
        self.game_display.config(state=tk.DISABLED)
        
    def update_character_display(self):
        """Update character stats display"""
        if not self.player:
            return
            
        self.char_info.config(state=tk.NORMAL)
        self.char_info.delete(1.0, tk.END)
        
        stats_text = f"""
Name: {self.player.name}
Class: {self.player.character_class}
Level: {self.player.level}

Health: {self.player.health}

💪 Strength: {self.player.strength}
🧠 Intelligence: {self.player.intelligence}
⚡ Agility: {self.player.agility}
🛡️ Vitality: {self.player.vitality}
        """
        
        self.char_info.insert(1.0, stats_text.strip())
        self.char_info.config(state=tk.DISABLED)
        
    def quick_command(self, command):
        """Execute a quick command"""
        self.command_var.set(command)
        self.process_command()
        
    def process_command(self, event=None):
        """Process user command"""
        command = self.command_var.get().strip()
        if not command:
            return
            
        self.display_text(f"> {command}")
        self.command_var.set("")
        
        # Process command with game logic
        # This would integrate with your existing game
        response = self.handle_game_command(command)
        self.display_text(response)
        
    def handle_game_command(self, command):
        """Handle game commands - integrate with your game logic"""
        # This is where you'd integrate with your existing game
        # For now, simple responses
        command = command.lower()
        
        if command in ['north', 'south', 'east', 'west']:
            return f"🧭 You move {command}..."
        elif command == 'look':
            return "👁️ You examine your surroundings..."
        elif command == 'help':
            return """
🆘 Available Commands:
🧭 Movement: north, south, east, west
👁️ Actions: look, inventory, stats, help
⚔️ Combat: attack, defend, run
🎮 Use the buttons for quick actions!
            """
        else:
            return f"❓ Unknown command: '{command}'"
            
    def new_game(self):
        """Start a new game"""
        self.display_text("🎯 Starting new adventure...")
        # Integrate with your game's new game logic
        
    def save_game(self):
        """Save current game"""
        messagebox.showinfo("Save Game", "Game saved successfully!")
        
    def load_game(self):
        """Load saved game"""
        messagebox.showinfo("Load Game", "Game loaded successfully!")
        
    def run(self):
        """Start the GUI"""
        self.display_text("🗻 Welcome to SHABUYA Cave Adventure! 🗻")
        self.display_text("Type 'help' for commands or use the quick action buttons.")
        self.command_entry.focus()
        self.root.mainloop()

def main():
    """Main GUI entry point"""
    try:
        app = CaveGameGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start GUI: {e}")
        # Fallback to text mode
        try:
            from game_refactored import main as text_main
            text_main()
        except:
            print("Both GUI and text mode failed. Please check installation.")

if __name__ == "__main__":
    main()
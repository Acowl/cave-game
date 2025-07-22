#!/usr/bin/env python3
"""
Cave Game GUI Interface

A graphical user interface for the Cave Game that wraps around the existing
text-based game logic while providing enhanced visual experience.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from tkinter import font as tkfont
import threading
import queue
import sys
from io import StringIO

from game_refactored import main as text_main
from player import Player
from item import dagger, axe, wand
from config import *

class CaveGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🗻 SHABUYA - Cave Adventure 🗻")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c1810')
        
        # Colors for cave theme
        self.colors = {
            'bg': '#2c1810',        # Dark brown (cave walls)
            'text': '#d4af37',      # Gold (torch light)
            'accent': '#8b4513',    # Saddle brown
            'danger': '#dc143c',    # Crimson 
            'success': '#32cd32',   # Lime green
            'input_bg': '#3c2820',  # Slightly lighter brown
            'button': '#654321',    # Medium brown
            'panel_bg': '#3c2414',  # Panel background
            'border': '#654321'     # Border color
        }
        
        # Game state
        self.game_thread = None
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        self.game_running = False
        self.current_player = None
        
        self.setup_ui()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_ui(self):
        """Create the main UI components"""
        # Title
        title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        title_label = tk.Label(
            self.root, 
            text="🗻 SHABUYA - Cave Adventure 🗻",
            font=title_font,
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        title_label.pack(pady=10)
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Left panel (Character Stats & Inventory)
        self.create_left_panel(main_container)
        
        # Center panel (Game Display)
        self.create_center_panel(main_container)
        
        # Right panel (Controls)
        self.create_right_panel(main_container)
        
        # Status bar
        self.create_status_bar()
        
    def create_left_panel(self, parent):
        """Create left panel with character stats and inventory"""
        left_frame = tk.Frame(parent, bg=self.colors['bg'], width=280)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Character Stats Panel
        self.create_character_stats_panel(left_frame)
        
        # Inventory Panel
        self.create_inventory_panel(left_frame)
        
    def create_character_stats_panel(self, parent):
        """Create character statistics display panel"""
        stats_frame = tk.LabelFrame(
            parent,
            text="🧙 Character Stats",
            fg=self.colors['text'],
            bg=self.colors['panel_bg'],
            font=("Arial", 12, "bold"),
            relief=tk.RAISED,
            bd=2
        )
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Character info
        self.char_name_label = tk.Label(
            stats_frame,
            text="Name: Not Started",
            font=("Arial", 10, "bold"),
            fg=self.colors['text'],
            bg=self.colors['panel_bg']
        )
        self.char_name_label.pack(anchor=tk.W, padx=10, pady=2)
        
        self.char_class_label = tk.Label(
            stats_frame,
            text="Class: None",
            font=("Arial", 10),
            fg=self.colors['accent'],
            bg=self.colors['panel_bg']
        )
        self.char_class_label.pack(anchor=tk.W, padx=10, pady=2)
        
        self.char_level_label = tk.Label(
            stats_frame,
            text="Level: 1",
            font=("Arial", 10),
            fg=self.colors['success'],
            bg=self.colors['panel_bg']
        )
        self.char_level_label.pack(anchor=tk.W, padx=10, pady=2)
        
        # Separator
        separator = tk.Frame(stats_frame, height=2, bg=self.colors['border'])
        separator.pack(fill=tk.X, padx=10, pady=5)
        
        # Primary Stats
        stats_container = tk.Frame(stats_frame, bg=self.colors['panel_bg'])
        stats_container.pack(fill=tk.X, padx=10, pady=5)
        
        # Health
        tk.Label(
            stats_container,
            text="❤️ Health:",
            font=("Arial", 9, "bold"),
            fg=self.colors['danger'],
            bg=self.colors['panel_bg']
        ).grid(row=0, column=0, sticky=tk.W, pady=1)
        
        self.health_var = tk.StringVar(value="100/100")
        self.health_label = tk.Label(
            stats_container,
            textvariable=self.health_var,
            font=("Arial", 9),
            fg=self.colors['text'],
            bg=self.colors['panel_bg']
        )
        self.health_label.grid(row=0, column=1, sticky=tk.E, pady=1)
        
        # Stat displays
        stat_labels = [
            ("💪 Strength:", "strength_var"),
            ("🧠 Intelligence:", "intelligence_var"),
            ("⚡ Agility:", "agility_var"),
            ("🛡️ Vitality:", "vitality_var")
        ]
        
        self.stat_vars = {}
        for i, (label_text, var_name) in enumerate(stat_labels, 1):
            tk.Label(
                stats_container,
                text=label_text,
                font=("Arial", 9),
                fg=self.colors['text'],
                bg=self.colors['panel_bg']
            ).grid(row=i, column=0, sticky=tk.W, pady=1)
            
            var = tk.StringVar(value="5")
            self.stat_vars[var_name] = var
            tk.Label(
                stats_container,
                textvariable=var,
                font=("Arial", 9, "bold"),
                fg=self.colors['accent'],
                bg=self.colors['panel_bg']
            ).grid(row=i, column=1, sticky=tk.E, pady=1)
        
    def create_inventory_panel(self, parent):
        """Create inventory display panel"""
        inv_frame = tk.LabelFrame(
            parent,
            text="🎒 Inventory & Equipment",
            fg=self.colors['text'],
            bg=self.colors['panel_bg'],
            font=("Arial", 12, "bold"),
            relief=tk.RAISED,
            bd=2
        )
        inv_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Current Weapon
        weapon_frame = tk.Frame(inv_frame, bg=self.colors['panel_bg'])
        weapon_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            weapon_frame,
            text="🗡️ Current Weapon:",
            font=("Arial", 10, "bold"),
            fg=self.colors['text'],
            bg=self.colors['panel_bg']
        ).pack(anchor=tk.W)
        
        self.current_weapon_var = tk.StringVar(value="None equipped")
        self.weapon_label = tk.Label(
            weapon_frame,
            textvariable=self.current_weapon_var,
            font=("Arial", 9),
            fg=self.colors['accent'],
            bg=self.colors['panel_bg'],
            wraplength=250
        )
        self.weapon_label.pack(anchor=tk.W, padx=10)
        
        # Items List
        tk.Label(
            inv_frame,
            text="📦 Items & Keys:",
            font=("Arial", 10, "bold"),
            fg=self.colors['text'],
            bg=self.colors['panel_bg']
        ).pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        # Scrollable items list
        items_container = tk.Frame(inv_frame, bg=self.colors['panel_bg'])
        items_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.items_listbox = tk.Listbox(
            items_container,
            font=("Arial", 9),
            bg=self.colors['input_bg'],
            fg=self.colors['text'],
            selectbackground=self.colors['accent'],
            relief=tk.SUNKEN,
            bd=1,
            height=8
        )
        
        items_scrollbar = tk.Scrollbar(items_container, orient=tk.VERTICAL)
        self.items_listbox.config(yscrollcommand=items_scrollbar.set)
        items_scrollbar.config(command=self.items_listbox.yview)
        
        self.items_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        items_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Initially populate with placeholder
        self.items_listbox.insert(tk.END, "🔍 No items yet")
        
    def create_center_panel(self, parent):
        """Create center panel with game display"""
        center_frame = tk.Frame(parent, bg=self.colors['bg'])
        center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Game display area
        self.create_display_area(center_frame)
        
    def create_display_area(self, parent):
        """Create the main text display area"""
        display_frame = tk.Frame(parent, bg=self.colors['bg'])
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text display
        self.text_display = scrolledtext.ScrolledText(
            display_frame,
            wrap=tk.WORD,
            width=60,
            height=30,
            font=("Courier New", 11),
            bg=self.colors['input_bg'],
            fg=self.colors['text'],
            insertbackground=self.colors['text'],
            selectbackground=self.colors['accent']
        )
        self.text_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Input frame
        input_frame = tk.Frame(display_frame, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X)
        
        tk.Label(
            input_frame, 
            text="Command:", 
            font=("Arial", 12, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(side=tk.LEFT)
        
        self.command_entry = tk.Entry(
            input_frame,
            font=("Courier New", 12),
            bg=self.colors['input_bg'],
            fg=self.colors['text'],
            insertbackground=self.colors['text']
        )
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        self.command_entry.bind('<Return>', self.send_command)
        
        send_btn = tk.Button(
            input_frame,
            text="Send",
            command=self.send_command,
            bg=self.colors['button'],
            fg=self.colors['text'],
            font=("Arial", 10, "bold")
        )
        send_btn.pack(side=tk.RIGHT)
        
    def create_right_panel(self, parent):
        """Create right panel with controls"""
        control_frame = tk.Frame(parent, bg=self.colors['bg'], width=250)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
        control_frame.pack_propagate(False)
        
        # Game controls
        tk.Label(
            control_frame,
            text="🎮 Game Controls",
            font=("Arial", 14, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(pady=(0, 10))
        
        # Start/Stop buttons
        btn_frame = tk.Frame(control_frame, bg=self.colors['bg'])
        btn_frame.pack(fill=tk.X, pady=5)
        
        self.start_btn = tk.Button(
            btn_frame,
            text="🎮 New Game",
            command=self.start_game,
            bg=self.colors['success'],
            fg='white',
            font=("Arial", 10, "bold"),
            height=2
        )
        self.start_btn.pack(fill=tk.X, pady=2)
        
        self.stop_btn = tk.Button(
            btn_frame,
            text="⏹️ Stop Game",
            command=self.stop_game,
            bg=self.colors['danger'],
            fg='white',
            font=("Arial", 10, "bold"),
            state=tk.DISABLED
        )
        self.stop_btn.pack(fill=tk.X, pady=2)
        
        # Quick actions
        tk.Label(
            control_frame,
            text="⚡ Quick Actions",
            font=("Arial", 12, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(pady=(20, 10))
        
        # Movement buttons
        self.create_movement_buttons(control_frame)
        
        # Common actions
        self.create_action_buttons(control_frame)
        
    def create_movement_buttons(self, parent):
        """Create movement quick buttons"""
        move_frame = tk.LabelFrame(
            parent,
            text="🧭 Movement",
            fg=self.colors['text'],
            bg=self.colors['bg'],
            font=("Arial", 10, "bold")
        )
        move_frame.pack(fill=tk.X, pady=5)
        
        movements = [
            ("🔺 North", "north"),
            ("🔻 South", "south"), 
            ("◀️ West", "west"),
            ("▶️ East", "east")
        ]
        
        for text, cmd in movements:
            btn = tk.Button(
                move_frame,
                text=text,
                command=lambda c=cmd: self.quick_command(c),
                bg=self.colors['button'],
                fg=self.colors['text'],
                font=("Arial", 9)
            )
            btn.pack(fill=tk.X, pady=1, padx=5)
            
    def create_action_buttons(self, parent):
        """Create action quick buttons"""
        action_frame = tk.LabelFrame(
            parent,
            text="⚔️ Actions",
            fg=self.colors['text'],
            bg=self.colors['bg'],
            font=("Arial", 10, "bold")
        )
        action_frame.pack(fill=tk.X, pady=5)
        
        actions = [
            ("⚔️ Attack", "1"),
            ("🏃 Run Away", "5"),
            ("👁️ Look", "look"),
            ("🎒 Inventory", "inventory"),
            ("📊 Stats", "stats"),
            ("❓ Help", "help")
        ]
        
        for text, cmd in actions:
            btn = tk.Button(
                action_frame,
                text=text,
                command=lambda c=cmd: self.quick_command(c),
                bg=self.colors['button'],
                fg=self.colors['text'],
                font=("Arial", 9)
            )
            btn.pack(fill=tk.X, pady=1, padx=5)
            
    def create_status_bar(self):
        """Create status bar"""
        self.status_bar = tk.Label(
            self.root,
            text="Ready to start adventure...",
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg=self.colors['accent'],
            fg=self.colors['text'],
            font=("Arial", 10)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def start_game(self):
        """Start the game in a separate thread"""
        if self.game_running:
            return
            
        self.game_running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.command_entry.config(state=tk.NORMAL)
        
        # Clear display
        self.text_display.delete(1.0, tk.END)
        self.update_status("Game starting...")
        
        # Start game thread
        self.game_thread = threading.Thread(target=self.run_game_loop, daemon=True)
        self.game_thread.start()
        
        # Start output monitoring
        self.root.after(100, self.check_output)
        
    def stop_game(self):
        """Stop the current game"""
        self.game_running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.command_entry.config(state=tk.DISABLED)
        self.update_status("Game stopped")
        
    def run_game_loop(self):
        """Run the game logic in a separate thread"""
        try:
            # Redirect stdout to capture game output
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            # Redirect input to our queue system
            old_input = __builtins__['input']
            __builtins__['input'] = self.threaded_input
            
            # Run the game
            text_main()
            
        except Exception as e:
            self.output_queue.put(f"Game error: {e}")
        finally:
            # Restore stdout and input
            sys.stdout = old_stdout
            __builtins__['input'] = old_input
            self.game_running = False
            
    def threaded_input(self, prompt=""):
        """Handle input requests from the game"""
        if prompt:
            self.output_queue.put(prompt)
            
        # Wait for user input
        while self.game_running:
            try:
                user_input = self.input_queue.get(timeout=0.1)
                return user_input
            except queue.Empty:
                continue
                
        return "quit"  # Return quit if game is stopped
        
    def check_output(self):
        """Check for game output and display it"""
        try:
            while True:
                output = self.output_queue.get_nowait()
                self.display_text(output)
        except queue.Empty:
            pass
            
        # Check for stdout content
        if hasattr(sys.stdout, 'getvalue'):
            content = sys.stdout.getvalue()
            if content:
                self.display_text(content)
                sys.stdout = StringIO()  # Reset buffer
                
        if self.game_running:
            self.root.after(100, self.check_output)
        else:
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.command_entry.config(state=tk.DISABLED)
            
    def display_text(self, text):
        """Display text in the main area with formatting"""
        self.text_display.config(state=tk.NORMAL)
        
        # Add color formatting for special text
        if "🗻" in text or "SHABUYA" in text:
            self.text_display.insert(tk.END, text + "\n", 'title')
        elif "💀" in text or "died" in text.lower():
            self.text_display.insert(tk.END, text + "\n", 'danger')
        elif "🌟" in text or "level up" in text.lower():
            self.text_display.insert(tk.END, text + "\n", 'success')
        else:
            self.text_display.insert(tk.END, text + "\n")
            
        # Configure text tags
        self.text_display.tag_config('title', foreground=self.colors['text'], font=("Arial", 12, "bold"))
        self.text_display.tag_config('danger', foreground=self.colors['danger'], font=("Arial", 11, "bold"))
        self.text_display.tag_config('success', foreground=self.colors['success'], font=("Arial", 11, "bold"))
        
        self.text_display.config(state=tk.DISABLED)
        self.text_display.see(tk.END)
        
    def send_command(self, event=None):
        """Send command to game"""
        command = self.command_entry.get().strip()
        if command and self.game_running:
            self.input_queue.put(command)
            self.command_entry.delete(0, tk.END)
            self.update_status(f"Sent: {command}")
            
    def quick_command(self, command):
        """Send a quick command"""
        if self.game_running:
            self.input_queue.put(command)
            self.update_status(f"Quick action: {command}")
            
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.config(text=message)
        
    def on_closing(self):
        """Handle window closing"""
        if self.game_running:
            self.stop_game()
        self.root.destroy()
        
    def run(self):
        """Start the GUI"""
        self.root.mainloop()

def main():
    """Launch the GUI"""
    app = CaveGameGUI()
    app.run()

if __name__ == "__main__":
    main()
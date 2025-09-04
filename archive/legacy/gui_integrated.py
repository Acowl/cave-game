#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Integrated Desktop GUI
Real game integration with proper input/output handling
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import threading
import queue
import io
from contextlib import redirect_stdout, redirect_stderr

# Import the actual game modules
from game_refactored import play_game, main as game_main
from game_events import start_game
from scenes import setup_scenes
from config import SCENE_NAMES


class GameOutputCapture:
    """Capture print statements and redirect to GUI"""
    def __init__(self, gui_callback):
        self.gui_callback = gui_callback
        self.buffer = ""
    
    def write(self, text):
        if text.strip():
            self.gui_callback(text)
        return len(text)
    
    def flush(self):
        pass


class GameInputProvider:
    """Provide input to the game from GUI"""
    def __init__(self):
        self.input_queue = queue.Queue()
        self.waiting = False
    
    def readline(self):
        """Called when game needs input"""
        self.waiting = True
        try:
            # Wait for input from GUI
            result = self.input_queue.get(timeout=300)  # 5 minute timeout
            self.waiting = False
            return result + '\n'
        except queue.Empty:
            self.waiting = False
            return 'quit\n'


class IntegratedCaveGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.player = None
        self.game_thread = None
        self.game_running = False
        
        # Input/Output handling
        self.input_provider = GameInputProvider()
        self.output_capture = GameOutputCapture(self.display_game_text)
        
        # GUI state
        self.current_input_prompt = ""
        self.waiting_for_input = False
        
        self.setup_window()
        self.create_interface()
        self.setup_input_output()
        
    def setup_window(self):
        """Setup main window"""
        self.root.title("🗻 SHABUYA - Cave Adventure (Integrated)")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c1810')
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600)
        y = (self.root.winfo_screenheight() // 2) - (400)
        self.root.geometry(f"1200x800+{x}+{y}")
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_interface(self):
        """Create the integrated game interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c1810')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title
        title_frame = tk.Frame(main_frame, bg='#2c1810')
        title_frame.pack(fill=tk.X, pady=(0, 15))
        
        title_label = tk.Label(title_frame, text="🗻 SHABUYA - CAVE ADVENTURE 🗻", 
                              font=("Arial", 18, "bold"), fg='#DAA520', bg='#2c1810')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Integrated Game Experience", 
                                 font=("Arial", 11), fg='#CD853F', bg='#2c1810')
        subtitle_label.pack()
        
        # Game content area
        content_frame = tk.Frame(main_frame, bg='#2c1810')
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - Game display and input
        left_frame = tk.Frame(content_frame, bg='#2c1810')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Game display area
        display_frame = tk.LabelFrame(left_frame, text="📖 Adventure", 
                                     font=("Arial", 12, "bold"),
                                     fg='#DAA520', bg='#3c2820', 
                                     relief=tk.RAISED, bd=2)
        display_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.game_display = scrolledtext.ScrolledText(
            display_frame,
            bg='#1a0f08', 
            fg='#DAA520',
            font=("Courier", 11), 
            relief=tk.SUNKEN, 
            bd=2,
            wrap=tk.WORD, 
            state=tk.DISABLED,
            height=25
        )
        self.game_display.pack(padx=8, pady=8, fill=tk.BOTH, expand=True)
        
        # Input area
        input_frame = tk.LabelFrame(left_frame, text="💬 Your Command", 
                                   font=("Arial", 10, "bold"),
                                   fg='#DAA520', bg='#3c2820')
        input_frame.pack(fill=tk.X)
        
        # Command input
        command_frame = tk.Frame(input_frame, bg='#3c2820')
        command_frame.pack(fill=tk.X, padx=8, pady=8)
        
        self.command_var = tk.StringVar()
        self.command_entry = tk.Entry(command_frame, textvariable=self.command_var,
                                     bg='#2c1810', fg='#DAA520', font=("Courier", 12),
                                     relief=tk.SUNKEN, bd=2)
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.command_entry.bind('<Return>', self.send_command)
        
        send_btn = tk.Button(command_frame, text="⚡ Send", font=("Arial", 10, "bold"),
                            bg='#228B22', fg='white', relief=tk.RAISED, bd=2,
                            command=self.send_command)
        send_btn.pack(side=tk.RIGHT)
        
        # Right side - Character info and controls
        right_frame = tk.Frame(content_frame, bg='#2c1810')
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Character stats
        stats_frame = tk.LabelFrame(right_frame, text="🧙 Character", 
                                   font=("Arial", 12, "bold"),
                                   fg='#DAA520', bg='#3c2820', 
                                   relief=tk.RAISED, bd=2)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.char_display = tk.Text(stats_frame, width=30, height=12,
                                   bg='#2c1810', fg='#DAA520', font=("Courier", 9),
                                   relief=tk.SUNKEN, bd=2, state=tk.DISABLED)
        self.char_display.pack(padx=8, pady=8)
        
        # Game controls
        controls_frame = tk.LabelFrame(right_frame, text="🎮 Game Controls", 
                                      font=("Arial", 12, "bold"),
                                      fg='#DAA520', bg='#3c2820')
        controls_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Control buttons
        btn_frame = tk.Frame(controls_frame, bg='#3c2820')
        btn_frame.pack(padx=8, pady=8)
        
        tk.Button(btn_frame, text="🎯 New Game", width=20, font=("Arial", 10),
                 bg='#228B22', fg='white', command=self.new_game).pack(pady=2)
        
        tk.Button(btn_frame, text="⏸️ Pause/Resume", width=20, font=("Arial", 10),
                 bg='#4682B4', fg='white', command=self.toggle_pause).pack(pady=2)
        
        tk.Button(btn_frame, text="🔄 Restart", width=20, font=("Arial", 10),
                 bg='#FF8C00', fg='white', command=self.restart_game).pack(pady=2)
        
        tk.Button(btn_frame, text="❌ Quit", width=20, font=("Arial", 10),
                 bg='#8B0000', fg='white', command=self.quit_game).pack(pady=2)
        
        # Status
        status_frame = tk.Frame(right_frame, bg='#2c1810')
        status_frame.pack(fill=tk.X)
        
        self.status_var = tk.StringVar(value="Ready to start adventure")
        status_label = tk.Label(status_frame, textvariable=self.status_var,
                               font=("Arial", 9), fg='#90EE90', bg='#2c1810',
                               wraplength=250)
        status_label.pack(pady=5)
        
    def setup_input_output(self):
        """Setup input/output redirection"""
        # Replace input() function for the game
        import builtins
        self.original_input = builtins.input
        builtins.input = self.game_input_handler
        
        # Initial welcome message
        self.display_game_text("🗻 SHABUYA Cave Adventure - Integrated GUI 🗻\n")
        self.display_game_text("=" * 50 + "\n")
        self.display_game_text("Click 'New Game' to start your adventure!\n")
        self.display_game_text("The full game experience is available through this interface.\n\n")
        
    def game_input_handler(self, prompt=""):
        """Handle input requests from the game"""
        # Display the prompt
        if prompt:
            self.display_game_text(f"\n{prompt}")
            self.current_input_prompt = prompt
        
        # Update status
        self.root.after(0, lambda: self.status_var.set("Waiting for your input..."))
        self.root.after(0, lambda: self.command_entry.focus_set())
        
        # Wait for input
        self.waiting_for_input = True
        try:
            result = self.input_provider.input_queue.get()
            self.waiting_for_input = False
            
            # Echo the input
            self.display_game_text(f" {result}\n")
            return result
        except:
            self.waiting_for_input = False
            return "quit"
        
    def display_game_text(self, text):
        """Display text in the game area (thread-safe)"""
        def update_display():
            self.game_display.config(state=tk.NORMAL)
            self.game_display.insert(tk.END, text)
            self.game_display.see(tk.END)
            self.game_display.config(state=tk.DISABLED)
            
        self.root.after(0, update_display)
        
    def send_command(self, event=None):
        """Send player command to the game"""
        if not self.waiting_for_input:
            return
            
        command = self.command_var.get().strip()
        if command:
            self.input_provider.input_queue.put(command)
            self.command_var.set("")
            self.status_var.set("Processing command...")
        
    def new_game(self):
        """Start a new game"""
        if self.game_running:
            if not messagebox.askyesno("New Game", "A game is already running. Start a new one?"):
                return
            self.stop_game()
        
        self.status_var.set("Starting new game...")
        self.clear_display()
        
        # Start game in separate thread
        self.game_thread = threading.Thread(target=self.run_game_loop, daemon=True)
        self.game_running = True
        self.game_thread.start()
        
    def run_game_loop(self):
        """Run the actual game in a separate thread"""
        try:
            # Redirect stdout to capture game output
            with redirect_stdout(self.output_capture):
                # Start the actual game
                self.player = start_game()
                play_game(self.player)
                
        except Exception as e:
            self.display_game_text(f"\nGame error: {e}\n")
        finally:
            self.game_running = False
            self.root.after(0, lambda: self.status_var.set("Game ended"))
            
    def update_character_display(self):
        """Update character information display"""
        if not self.player:
            return
            
        def update():
            self.char_display.config(state=tk.NORMAL)
            self.char_display.delete(1.0, tk.END)
            
            char_info = f"""Character Info:
Class: {getattr(self.player, 'character_class', 'Unknown')}
Level: {self.player.level}
Health: {self.player.health}

Stats:
Vitality: {self.player.vitality}
Strength: {self.player.strength}  
Agility: {self.player.agility}
Intelligence: {self.player.intelligence}

Weapon: {self.player.weapon.name if self.player.weapon else 'None'}
"""
            
            if hasattr(self.player, 'inventory') and self.player.inventory:
                char_info += f"\nInventory: {len(self.player.inventory.items)} items"
                
            self.char_display.insert(1.0, char_info)
            self.char_display.config(state=tk.DISABLED)
            
        self.root.after(0, update)
        
    def toggle_pause(self):
        """Toggle game pause (placeholder)"""
        if self.game_running:
            self.status_var.set("Game paused (send command to resume)")
        else:
            self.status_var.set("No game running")
            
    def restart_game(self):
        """Restart the current game"""
        if self.game_running:
            self.stop_game()
        self.new_game()
        
    def stop_game(self):
        """Stop the current game"""
        self.game_running = False
        if self.waiting_for_input:
            self.input_provider.input_queue.put("quit")
        self.status_var.set("Game stopped")
        
    def quit_game(self):
        """Quit the application"""
        if self.game_running:
            self.stop_game()
        self.on_closing()
        
    def clear_display(self):
        """Clear the game display"""
        self.game_display.config(state=tk.NORMAL)
        self.game_display.delete(1.0, tk.END)
        self.game_display.config(state=tk.DISABLED)
        
    def on_closing(self):
        """Handle application closing"""
        if self.game_running:
            if messagebox.askyesno("Quit", "Game is running. Are you sure you want to quit?"):
                self.stop_game()
                self.root.destroy()
        else:
            self.root.destroy()
            
    def run(self):
        """Run the GUI application"""
        self.root.mainloop()


def main():
    """Main function to run the integrated GUI"""
    try:
        app = IntegratedCaveGameGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start GUI: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

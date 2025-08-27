#!/usr/bin/env python3
"""
Headless GUI Snapshot System
============================
Captures GUI states using Xvfb and PIL for AI analysis.
Works in containerized environments without physical display.
"""

import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
import subprocess
import time
from pathlib import Path

# Add proper paths to import game modules
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

class HeadlessGUICapture:
    def __init__(self):
        print("📸 Starting Headless GUI Capture System...")
        
        # Create snapshots directory
        self.snapshot_dir = Path("gui_snapshots")
        self.snapshot_dir.mkdir(exist_ok=True)
        
        # Set display for Xvfb
        os.environ['DISPLAY'] = ':99'
        
        # Initialize Tkinter with virtual display
        self.root = tk.Tk()
        self.root.title("SHABUYA Cave Adventure - Headless Capture")
        self.root.geometry("1000x700")
        self.root.configure(bg='#0a0a0a')
        
        # Game state
        self.snapshot_count = 0
        self.current_state = "init"
        
        print("✅ Headless GUI initialized on display :99")
    
    def capture_window_state(self, state_name):
        """Capture current window state using xwd and convert to PNG."""
        try:
            self.snapshot_count += 1
            filename = f"{self.snapshot_count:02d}_{state_name}"
            
            print(f"📸 Capturing state: {state_name}")
            
            # Update GUI
            self.root.update()
            self.root.update_idletasks()
            
            # Get window ID
            window_id = hex(self.root.winfo_id())
            
            # Capture using xwd
            xwd_file = self.snapshot_dir / f"{filename}.xwd"
            png_file = self.snapshot_dir / f"{filename}.png"
            
            # Use xwd to capture the window
            subprocess.run(['xwd', '-id', window_id, '-out', str(xwd_file)], check=True)
            
            # Convert xwd to PNG using ImageMagick
            subprocess.run(['convert', str(xwd_file), str(png_file)], check=True)
            
            # Remove temporary xwd file
            xwd_file.unlink()
            
            print(f"✅ Snapshot saved: {png_file.name}")
            return str(png_file)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Capture failed: {e}")
            # Fallback: create a text description
            desc_file = self.snapshot_dir / f"{filename}.txt"
            with open(desc_file, 'w') as f:
                f.write(f"GUI State: {state_name}\n")
                f.write(f"Window size: {self.root.geometry()}\n")
                f.write(f"Capture time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Error: {e}\n")
            return str(desc_file)
    
    def create_title_screen(self):
        """Create and capture the title screen."""
        print("🎭 Creating title screen...")
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main canvas
        canvas = tk.Canvas(self.root, width=1000, height=700, bg='#0a0a0a')
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create background gradient
        for i in range(35):
            color_val = int(10 + i * 3)
            color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
            canvas.create_rectangle(0, i*20, 1000, (i+1)*20, fill=color, outline=color)
        
        # Title text
        canvas.create_text(500, 200, text="SHABUYA", 
                          font=("Arial", 48, "bold"), fill="#FFD700")
        canvas.create_text(500, 260, text="Cave Adventure", 
                          font=("Arial", 32, "italic"), fill="#C0C0C0")
        
        # Character selection area
        frame = tk.Frame(canvas, bg='#1a1a1a', bd=2, relief=tk.RAISED)
        frame.place(x=300, y=400, width=400, height=200)
        
        tk.Label(frame, text="Choose Your Class:", 
                font=("Arial", 16, "bold"), fg="#FFD700", bg='#1a1a1a').pack(pady=10)
        
        for cls in ['Warrior', 'Rogue', 'Mage']:
            tk.Button(frame, text=cls, font=("Arial", 14),
                     bg='#2a2a2a', fg='white', width=12).pack(pady=5)
        
        # Capture this state
        self.root.after(500, lambda: self.capture_window_state("title_screen"))
        
        return canvas
    
    def create_game_scene(self):
        """Create and capture a sample game scene."""
        print("🏛️ Creating game scene...")
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Scene canvas (top 500px)
        scene_canvas = tk.Canvas(self.root, width=1000, height=500, bg='#2a4a2a')
        scene_canvas.pack()
        
        # Simulate background
        scene_canvas.create_rectangle(0, 0, 1000, 500, fill='#2a4a2a', outline='')
        scene_canvas.create_text(500, 100, text="🏰 Town Square", 
                               font=("Arial", 24, "bold"), fill='white')
        
        # Simulate character sprite
        scene_canvas.create_oval(200, 300, 280, 380, fill='#8B4513', outline='black', width=2)
        scene_canvas.create_text(240, 340, text="🧙", font=("Arial", 30))
        
        # Player info bar
        info_frame = tk.Frame(self.root, bg='#1a1a1a', height=50)
        info_frame.pack(fill=tk.X)
        tk.Label(info_frame, text="Hero the Warrior | HP: 100/100 | Level: 1",
                font=("Arial", 12), fg='white', bg='#1a1a1a').pack(pady=15)
        
        # Dialogue box
        dialogue_frame = tk.Frame(self.root, bg='#2a2a2a', height=150)
        dialogue_frame.pack(fill=tk.BOTH, expand=True)
        
        text_widget = tk.Text(dialogue_frame, height=4, wrap=tk.WORD,
                             font=("Arial", 11), bg='#2a2a2a', fg='white')
        text_widget.pack(fill=tk.X, padx=10, pady=5)
        text_widget.insert(tk.END, "You stand in the heart of the village. The cobblestone streets bustle with merchants and travelers. What would you like to do?")
        text_widget.config(state=tk.DISABLED)
        
        # Options
        options_frame = tk.Frame(dialogue_frame, bg='#2a2a2a')
        options_frame.pack(fill=tk.X, padx=10, pady=5)
        
        for option in ["Visit Armory", "Explore Forest", "Talk to Villagers", "Check Inventory"]:
            tk.Button(options_frame, text=option, font=("Arial", 10),
                     bg='#3a3a3a', fg='white').pack(side=tk.LEFT, padx=5)
        
        # Capture this state
        self.root.after(500, lambda: self.capture_window_state("game_scene"))
    
    def create_combat_scene(self):
        """Create and capture a combat interface."""
        print("⚔️ Creating combat scene...")
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Combat canvas
        combat_canvas = tk.Canvas(self.root, width=1000, height=500, bg='#4a2a2a')
        combat_canvas.pack()
        
        # Combat background
        combat_canvas.create_rectangle(0, 0, 1000, 500, fill='#4a2a2a')
        combat_canvas.create_text(500, 50, text="⚔️ COMBAT ⚔️", 
                                font=("Arial", 28, "bold"), fill='red')
        
        # Player (left side)
        combat_canvas.create_oval(150, 250, 230, 330, fill='#4169E1', outline='black', width=2)
        combat_canvas.create_text(190, 290, text="🛡️", font=("Arial", 30))
        combat_canvas.create_text(190, 350, text="Hero", font=("Arial", 14), fill='white')
        combat_canvas.create_text(190, 370, text="HP: 85/100", font=("Arial", 12), fill='lightgreen')
        
        # Enemy (right side)
        combat_canvas.create_oval(770, 200, 900, 330, fill='#8B0000', outline='black', width=2)
        combat_canvas.create_text(835, 265, text="👹", font=("Arial", 40))
        combat_canvas.create_text(835, 350, text="Cave Troll", font=("Arial", 14), fill='white')
        combat_canvas.create_text(835, 370, text="HP: 60/120", font=("Arial", 12), fill='orange')
        
        # Combat log area
        log_frame = tk.Frame(self.root, bg='#1a1a1a', height=100)
        log_frame.pack(fill=tk.X)
        
        log_text = tk.Text(log_frame, height=5, wrap=tk.WORD,
                          font=("Arial", 10), bg='#1a1a1a', fg='yellow')
        log_text.pack(fill=tk.BOTH, padx=10, pady=5)
        log_text.insert(tk.END, "⚔️ Hero attacks Cave Troll for 15 damage!\n")
        log_text.insert(tk.END, "👹 Cave Troll retaliates for 12 damage!\n")
        log_text.insert(tk.END, "💨 Hero dodges the next attack!\n")
        
        # Combat actions
        actions_frame = tk.Frame(self.root, bg='#2a2a2a', height=100)
        actions_frame.pack(fill=tk.BOTH)
        
        for action in ["⚔️ Attack", "🛡️ Defend", "🧪 Use Item", "💨 Flee"]:
            tk.Button(actions_frame, text=action, font=("Arial", 12, "bold"),
                     bg='#3a3a3a', fg='white', width=15, height=2).pack(side=tk.LEFT, padx=10, pady=20)
        
        # Capture this state
        self.root.after(500, lambda: self.capture_window_state("combat_scene"))
    
    def create_inventory_scene(self):
        """Create and capture an inventory interface."""
        print("🎒 Creating inventory scene...")
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.root, bg='#1a1a1a', height=60)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="🎒 Inventory", 
                font=("Arial", 24, "bold"), fg="#FFD700", bg='#1a1a1a').pack(pady=15)
        
        # Main inventory area
        main_frame = tk.Frame(self.root, bg='#2a2a2a')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - Items
        items_frame = tk.Frame(main_frame, bg='#2a2a2a', width=500)
        items_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        
        tk.Label(items_frame, text="Items:", font=("Arial", 16, "bold"),
                fg='white', bg='#2a2a2a').pack(anchor='w')
        
        items = ["⚔️ Iron Sword (Equipped)", "🛡️ Leather Armor (Equipped)", 
                "🧪 Health Potion x3", "🗝️ Rusty Key", "📜 Ancient Scroll"]
        
        for item in items:
            item_frame = tk.Frame(items_frame, bg='#3a3a3a', relief=tk.RAISED, bd=1)
            item_frame.pack(fill=tk.X, pady=2)
            tk.Label(item_frame, text=item, font=("Arial", 11),
                    fg='white', bg='#3a3a3a', anchor='w').pack(padx=10, pady=5, fill=tk.X)
        
        # Right side - Stats
        stats_frame = tk.Frame(main_frame, bg='#2a2a2a', width=500)
        stats_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)
        
        tk.Label(stats_frame, text="Character Stats:", font=("Arial", 16, "bold"),
                fg='white', bg='#2a2a2a').pack(anchor='w')
        
        stats = ["Level: 3", "Health: 85/100", "Attack: 25", "Defense: 15", 
                "Gold: 145", "Experience: 750/1000"]
        
        for stat in stats:
            tk.Label(stats_frame, text=stat, font=("Arial", 12),
                    fg='lightblue', bg='#2a2a2a', anchor='w').pack(anchor='w', pady=3)
        
        # Bottom buttons
        button_frame = tk.Frame(self.root, bg='#1a1a1a', height=60)
        button_frame.pack(fill=tk.X)
        
        for btn_text in ["Use Item", "Drop Item", "Close Inventory"]:
            tk.Button(button_frame, text=btn_text, font=("Arial", 12),
                     bg='#3a3a3a', fg='white', width=15).pack(side=tk.LEFT, padx=20, pady=15)
        
        # Capture this state
        self.root.after(500, lambda: self.capture_window_state("inventory_scene"))
    
    def run_automated_capture_sequence(self):
        """Run through all the GUI states and capture them."""
        print("🤖 Starting automated capture sequence...")
        
        # Define the sequence
        sequence = [
            (1000, self.create_title_screen),
            (3000, self.create_game_scene),
            (5000, self.create_combat_scene),
            (7000, self.create_inventory_scene),
            (9000, self.generate_capture_report),
        ]
        
        # Schedule all captures
        for delay, action in sequence:
            self.root.after(delay, action)
        
        # Auto-close after completion
        self.root.after(11000, self.root.quit)
    
    def generate_capture_report(self):
        """Generate a final report of captured states."""
        print("📋 Generating capture report...")
        
        report_file = self.snapshot_dir / "capture_report.md"
        
        with open(report_file, 'w') as f:
            f.write("# Headless GUI Capture Report\n\n")
            f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Captured GUI States\n\n")
            
            # List all files in snapshot directory
            files = list(self.snapshot_dir.glob("*"))
            png_files = [f for f in files if f.suffix == '.png']
            txt_files = [f for f in files if f.suffix == '.txt']
            
            f.write(f"### Successfully Captured ({len(png_files)} PNG files)\n")
            for png_file in sorted(png_files):
                f.write(f"- `{png_file.name}` ({png_file.stat().st_size} bytes)\n")
            
            if txt_files:
                f.write(f"\n### Capture Fallbacks ({len(txt_files)} text files)\n")
                for txt_file in sorted(txt_files):
                    f.write(f"- `{txt_file.name}`\n")
            
            f.write("\n## GUI States Tested\n")
            f.write("1. **Title Screen** - Character selection interface\n")
            f.write("2. **Game Scene** - Main gameplay with dialogue\n")
            f.write("3. **Combat Scene** - Battle interface with stats\n")
            f.write("4. **Inventory Scene** - Item management interface\n")
            
            f.write("\n## Analysis Ready\n")
            f.write("These PNG files can be analyzed by AI to review:\n")
            f.write("- UI layout and positioning\n")
            f.write("- Color scheme and visual design\n")
            f.write("- Text readability and font choices\n")
            f.write("- Button placement and accessibility\n")
            f.write("- Overall user experience flow\n")
        
        print(f"✅ Report saved: {report_file}")
        
        # Print summary to console
        print(f"\n📊 CAPTURE SUMMARY")
        print(f"  Total snapshots: {self.snapshot_count}")
        print(f"  PNG files: {len(list(self.snapshot_dir.glob('*.png')))}")
        print(f"  Saved to: {self.snapshot_dir.absolute()}")
    
    def run(self):
        """Run the headless capture system."""
        print("🚀 Starting headless GUI capture...")
        try:
            self.run_automated_capture_sequence()
            self.root.mainloop()
            print("✅ Capture completed successfully!")
        except Exception as e:
            print(f"❌ Capture failed: {e}")

def main():
    print("=" * 60)
    print("📸 Headless GUI Snapshot System")
    print("=" * 60)
    
    try:
        capture_system = HeadlessGUICapture()
        capture_system.run()
    except Exception as e:
        print(f"❌ System failed to start: {e}")

if __name__ == "__main__":
    main()

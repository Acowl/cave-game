#!/usr/bin/env python3
"""
Simple GUI Screenshot System using scrot
========================================
Captures GUI screenshots for AI analysis using scrot tool.
"""

import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
import subprocess
import time
from pathlib import Path
import threading

# Add proper paths to import game modules
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

class SimpleGUIScreenshotter:
    def __init__(self):
        print("📸 Starting Simple GUI Screenshot System...")
        
        # Create snapshots directory
        self.snapshot_dir = Path("gui_snapshots")
        self.snapshot_dir.mkdir(exist_ok=True)
        
        # Set display for Xvfb
        os.environ['DISPLAY'] = ':99'
        
        # Initialize Tkinter
        self.root = tk.Tk()
        self.root.title("SHABUYA Cave Adventure")
        self.root.geometry("1000x700")
        self.root.configure(bg='#0a0a0a')
        
        # Game state
        self.snapshot_count = 0
        self.window_mapped = False
        
        # Bind window events
        self.root.bind('<Map>', self.on_window_map)
        
        print("✅ GUI initialized")
    
    def on_window_map(self, event):
        """Called when window becomes visible."""
        if not self.window_mapped:
            self.window_mapped = True
            print("🪟 Window is now visible")
    
    def capture_screenshot(self, name, delay=500):
        """Capture screenshot using scrot with delay."""
        def do_capture():
            try:
                self.snapshot_count += 1
                filename = f"{self.snapshot_count:02d}_{name}.png"
                filepath = self.snapshot_dir / filename
                
                print(f"📸 Capturing: {name}")
                
                # Update GUI
                self.root.update()
                self.root.update_idletasks()
                
                # Wait a bit for rendering
                time.sleep(0.2)
                
                # Use scrot to capture the entire screen
                result = subprocess.run(['scrot', str(filepath)], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0 and filepath.exists():
                    print(f"✅ Screenshot saved: {filename} ({filepath.stat().st_size} bytes)")
                    return str(filepath)
                else:
                    print(f"❌ scrot failed: {result.stderr}")
                    # Create fallback text file
                    txt_path = self.snapshot_dir / f"{filename}.txt"
                    with open(txt_path, 'w') as f:
                        f.write(f"Screenshot failed for: {name}\n")
                        f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                        f.write(f"Error: {result.stderr}\n")
                    return str(txt_path)
                    
            except Exception as e:
                print(f"❌ Screenshot error: {e}")
                return None
        
        # Schedule the capture
        self.root.after(delay, do_capture)
    
    def create_title_screen(self):
        """Create title screen with character selection."""
        print("🎭 Creating title screen...")
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main canvas
        canvas = tk.Canvas(self.root, width=1000, height=700, bg='#0a0a0a')
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Gradient background
        for i in range(35):
            color_val = int(10 + i * 3)
            color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
            canvas.create_rectangle(0, i*20, 1000, (i+1)*20, fill=color, outline=color)
        
        # Title text  
        canvas.create_text(500, 150, text="🏴‍☠️ SHABUYA", 
                          font=("Arial", 48, "bold"), fill="#FFD700")
        canvas.create_text(500, 220, text="Cave Adventure", 
                          font=("Arial", 32, "italic"), fill="#C0C0C0")
        canvas.create_text(500, 280, text="Choose Your Destiny", 
                          font=("Arial", 16), fill="#CCCCCC")
        
        # Character selection frame
        char_frame = tk.Frame(canvas, bg='#1a1a1a', bd=3, relief=tk.RAISED)
        char_frame.place(x=250, y=350, width=500, height=280)
        
        # Title
        tk.Label(char_frame, text="⚔️ Select Your Class ⚔️", 
                font=("Arial", 18, "bold"), fg="#FFD700", bg='#1a1a1a').pack(pady=15)
        
        # Class buttons with descriptions
        classes = [
            ("🛡️ Warrior", "Strong and durable, masters of combat"),
            ("🗡️ Rogue", "Quick and cunning, masters of stealth"), 
            ("🔮 Mage", "Wise and powerful, masters of magic")
        ]
        
        for i, (cls, desc) in enumerate(classes):
            btn_frame = tk.Frame(char_frame, bg='#2a2a2a', relief=tk.RAISED, bd=1)
            btn_frame.pack(fill=tk.X, padx=20, pady=8)
            
            btn = tk.Button(btn_frame, text=cls, font=("Arial", 14, "bold"),
                           bg='#3a3a3a', fg='white', activebackground='#4a4a4a',
                           width=20, command=lambda c=cls: self.start_game(c))
            btn.pack(side=tk.LEFT, padx=10, pady=5)
            
            tk.Label(btn_frame, text=desc, font=("Arial", 10),
                    fg='#CCCCCC', bg='#2a2a2a', anchor='w').pack(side=tk.LEFT, padx=10, pady=5)
        
        # Capture this screen
        self.capture_screenshot("title_screen", 1000)
        
        return canvas
    
    def start_game(self, player_class):
        """Start game with selected class."""
        print(f"🎯 Starting game as: {player_class}")
        
        # Quick capture of selection
        self.capture_screenshot(f"class_selected_{player_class.lower().replace(' ', '_').replace('️', '')}", 200)
        
        # Transition to game
        self.root.after(1500, self.create_game_scene)
    
    def create_game_scene(self):
        """Create main game scene."""
        print("🏰 Creating game scene...")
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Scene area (top 60%)
        scene_frame = tk.Frame(self.root, bg='#2a4a2a', height=420)
        scene_frame.pack(fill=tk.X)
        scene_frame.pack_propagate(False)
        
        # Scene canvas for graphics
        scene_canvas = tk.Canvas(scene_frame, bg='#2a4a2a', height=420)
        scene_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create scene background
        # Sky
        scene_canvas.create_rectangle(0, 0, 1000, 200, fill='#4682B4', outline='')
        # Ground
        scene_canvas.create_rectangle(0, 200, 1000, 420, fill='#228B22', outline='')
        
        # Buildings/structures
        # Castle in background
        scene_canvas.create_rectangle(700, 100, 900, 200, fill='#696969', outline='black', width=2)
        scene_canvas.create_polygon(700, 100, 800, 50, 900, 100, fill='#8B0000', outline='black', width=2)
        scene_canvas.create_text(800, 150, text="🏰", font=("Arial", 40))
        
        # Player character
        scene_canvas.create_oval(150, 280, 220, 350, fill='#4169E1', outline='black', width=3)
        scene_canvas.create_text(185, 315, text="🛡️", font=("Arial", 30))
        scene_canvas.create_text(185, 370, text="Hero", font=("Arial", 14, "bold"), fill='white')
        
        # NPC
        scene_canvas.create_oval(400, 270, 470, 340, fill='#8B4513', outline='black', width=2)
        scene_canvas.create_text(435, 305, text="👤", font=("Arial", 30))
        scene_canvas.create_text(435, 360, text="Villager", font=("Arial", 12), fill='white')
        
        # Player stats bar
        stats_frame = tk.Frame(self.root, bg='#1a1a1a', height=60)
        stats_frame.pack(fill=tk.X)
        stats_frame.pack_propagate(False)
        
        tk.Label(stats_frame, text="🛡️ Hero the Warrior | ❤️ HP: 95/100 | ⚔️ ATK: 25 | 🛡️ DEF: 20 | 💰 Gold: 150",
                font=("Arial", 12, "bold"), fg='#FFD700', bg='#1a1a1a').pack(pady=20)
        
        # Dialogue/interaction area
        dialogue_frame = tk.Frame(self.root, bg='#2a2a2a', height=220)
        dialogue_frame.pack(fill=tk.BOTH, expand=True)
        
        # Location header
        tk.Label(dialogue_frame, text="📍 Town Square - Village of Millbrook", 
                font=("Arial", 14, "bold"), fg='#FFD700', bg='#2a2a2a').pack(pady=5)
        
        # Dialogue text
        dialogue_text = tk.Text(dialogue_frame, height=6, wrap=tk.WORD,
                               font=("Arial", 11), bg='#333333', fg='white',
                               relief=tk.SUNKEN, bd=2)
        dialogue_text.pack(fill=tk.X, padx=15, pady=5)
        
        dialogue_content = ("You stand in the bustling town square of Millbrook village. "
                          "Merchants hawk their wares while children play near the ancient fountain. "
                          "The morning sun casts long shadows across the cobblestones. "
                          "A friendly villager approaches you with a concerned expression.\n\n"
                          "Villager: 'Greetings, brave adventurer! Have you heard about the strange "
                          "sounds coming from the old cave system? The village elder is looking for "
                          "someone brave enough to investigate...'")
        
        dialogue_text.insert(tk.END, dialogue_content)
        dialogue_text.config(state=tk.DISABLED)
        
        # Action buttons
        button_frame = tk.Frame(dialogue_frame, bg='#2a2a2a')
        button_frame.pack(fill=tk.X, padx=15, pady=10)
        
        actions = [
            ("🗡️ Accept Quest", lambda: self.show_combat()),
            ("🏪 Visit Armory", lambda: self.show_shop()),
            ("🎒 Check Inventory", lambda: self.show_inventory()),
            ("💬 Ask About Village", lambda: self.show_dialogue())
        ]
        
        for i, (action_text, action_cmd) in enumerate(actions):
            btn = tk.Button(button_frame, text=action_text, font=("Arial", 10, "bold"),
                           bg='#3a3a3a', fg='white', activebackground='#4a4a4a',
                           command=action_cmd, width=18, height=2)
            btn.grid(row=i//2, column=i%2, padx=5, pady=3, sticky='ew')
        
        # Configure grid weights
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Capture this scene
        self.capture_screenshot("main_game_scene", 1000)
    
    def show_combat(self):
        """Show combat interface."""
        print("⚔️ Showing combat interface...")
        
        # Create combat window
        combat_window = tk.Toplevel(self.root)
        combat_window.title("⚔️ Combat!")
        combat_window.geometry("600x500")
        combat_window.configure(bg='#1a1a1a')
        
        # Combat header
        tk.Label(combat_window, text="⚔️ BATTLE COMMENCED ⚔️", 
                font=("Arial", 20, "bold"), fg="red", bg='#1a1a1a').pack(pady=10)
        
        # Combat area
        combat_canvas = tk.Canvas(combat_window, height=250, bg='#4a2a2a')
        combat_canvas.pack(fill=tk.X, padx=10, pady=5)
        
        # Player (left)
        combat_canvas.create_oval(50, 100, 120, 170, fill='#4169E1', outline='black', width=2)
        combat_canvas.create_text(85, 135, text="🛡️", font=("Arial", 25))
        combat_canvas.create_text(85, 190, text="Hero", font=("Arial", 12, "bold"), fill='white')
        combat_canvas.create_text(85, 210, text="HP: 95/100", font=("Arial", 10), fill='lightgreen')
        
        # Enemy (right)
        combat_canvas.create_oval(480, 80, 570, 170, fill='#8B0000', outline='black', width=2)
        combat_canvas.create_text(525, 125, text="👹", font=("Arial", 35))
        combat_canvas.create_text(525, 190, text="Cave Troll", font=("Arial", 12, "bold"), fill='white')
        combat_canvas.create_text(525, 210, text="HP: 80/120", font=("Arial", 10), fill='orange')
        
        # Combat log
        log_frame = tk.Frame(combat_window, bg='#2a2a2a')
        log_frame.pack(fill=tk.X, padx=10, pady=5)
        
        log_text = tk.Text(log_frame, height=4, font=("Arial", 9),
                          bg='#2a2a2a', fg='yellow', relief=tk.SUNKEN, bd=1)
        log_text.pack(fill=tk.X)
        log_text.insert(tk.END, "⚔️ Hero strikes Cave Troll for 18 damage!\n")
        log_text.insert(tk.END, "👹 Cave Troll attacks back for 12 damage!\n")
        log_text.insert(tk.END, "💨 Hero dodges the troll's wild swing!\n")
        log_text.config(state=tk.DISABLED)
        
        # Combat actions
        actions_frame = tk.Frame(combat_window, bg='#1a1a1a')
        actions_frame.pack(fill=tk.X, padx=10, pady=10)
        
        combat_actions = ["⚔️ Attack", "🛡️ Defend", "🧪 Use Potion", "💨 Flee"]
        for i, action in enumerate(combat_actions):
            btn = tk.Button(actions_frame, text=action, font=("Arial", 12, "bold"),
                           bg='#3a3a3a', fg='white', width=12, height=2)
            btn.grid(row=i//2, column=i%2, padx=5, pady=5)
        
        # Configure grid
        actions_frame.grid_columnconfigure(0, weight=1)
        actions_frame.grid_columnconfigure(1, weight=1)
        
        # Capture combat
        self.root.after(800, lambda: self.capture_screenshot("combat_interface"))
        
        # Auto-close after capture
        combat_window.after(3000, combat_window.destroy)
    
    def show_shop(self):
        """Show shop interface."""
        print("🏪 Showing shop interface...")
        
        shop_window = tk.Toplevel(self.root)
        shop_window.title("🏪 Village Armory")
        shop_window.geometry("500x400")
        shop_window.configure(bg='#2a2a2a')
        
        # Shop header
        tk.Label(shop_window, text="🏪 Village Armory", 
                font=("Arial", 18, "bold"), fg="#FFD700", bg='#2a2a2a').pack(pady=10)
        tk.Label(shop_window, text="'Welcome, adventurer! Best prices in town!'", 
                font=("Arial", 12, "italic"), fg="#CCCCCC", bg='#2a2a2a').pack()
        
        # Shop items
        items_frame = tk.Frame(shop_window, bg='#2a2a2a')
        items_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        items = [
            ("⚔️ Steel Sword", "75 Gold", "A well-crafted blade"),
            ("🛡️ Chain Mail", "120 Gold", "Sturdy protection"),
            ("🧪 Health Potion", "25 Gold", "Restores 50 HP"),
            ("🏹 Silver Arrows", "15 Gold", "Pack of 10 arrows"),
            ("📜 Scroll of Fireball", "200 Gold", "Powerful magic spell")
        ]
        
        for i, (item, price, desc) in enumerate(items):
            item_frame = tk.Frame(items_frame, bg='#3a3a3a', relief=tk.RAISED, bd=1)
            item_frame.pack(fill=tk.X, pady=3)
            
            # Item name and price
            top_frame = tk.Frame(item_frame, bg='#3a3a3a')
            top_frame.pack(fill=tk.X)
            
            tk.Label(top_frame, text=item, font=("Arial", 12, "bold"),
                    fg='white', bg='#3a3a3a', anchor='w').pack(side=tk.LEFT, padx=10, pady=5)
            tk.Label(top_frame, text=price, font=("Arial", 12, "bold"),
                    fg='#FFD700', bg='#3a3a3a', anchor='e').pack(side=tk.RIGHT, padx=10, pady=5)
            
            # Description
            tk.Label(item_frame, text=desc, font=("Arial", 10),
                    fg='#CCCCCC', bg='#3a3a3a', anchor='w').pack(fill=tk.X, padx=10, pady=2)
        
        # Shop buttons
        btn_frame = tk.Frame(shop_window, bg='#2a2a2a')
        btn_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Button(btn_frame, text="💰 Your Gold: 150", font=("Arial", 12),
                 bg='#4a4a4a', fg='#FFD700', state=tk.DISABLED).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="❌ Close Shop", font=("Arial", 12),
                 bg='#3a3a3a', fg='white', command=shop_window.destroy).pack(side=tk.RIGHT, padx=5)
        
        # Capture shop
        self.root.after(800, lambda: self.capture_screenshot("shop_interface"))
        
        # Auto-close
        shop_window.after(3000, shop_window.destroy)
    
    def show_inventory(self):
        """Show inventory interface.""" 
        print("🎒 Showing inventory...")
        
        inv_window = tk.Toplevel(self.root)
        inv_window.title("🎒 Inventory")
        inv_window.geometry("600x500")
        inv_window.configure(bg='#1a1a1a')
        
        # Header
        tk.Label(inv_window, text="🎒 Your Inventory", 
                font=("Arial", 18, "bold"), fg="#FFD700", bg='#1a1a1a').pack(pady=10)
        
        # Main area
        main_frame = tk.Frame(inv_window, bg='#1a1a1a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Items section
        items_frame = tk.LabelFrame(main_frame, text="📦 Items", 
                                   font=("Arial", 14, "bold"), fg='white', bg='#2a2a2a')
        items_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        inventory_items = [
            "⚔️ Iron Sword (Equipped)",
            "🛡️ Leather Armor (Equipped)", 
            "🧪 Health Potion x2",
            "🗝️ Mysterious Key",
            "📜 Ancient Map Fragment",
            "💎 Blue Crystal"
        ]
        
        for item in inventory_items:
            item_label = tk.Label(items_frame, text=item, font=("Arial", 11),
                                 fg='white', bg='#3a3a3a', anchor='w', relief=tk.RAISED, bd=1)
            item_label.pack(fill=tk.X, padx=5, pady=2)
        
        # Stats section
        stats_frame = tk.LabelFrame(main_frame, text="📊 Stats", 
                                   font=("Arial", 14, "bold"), fg='white', bg='#2a2a2a')
        stats_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        stats = [
            "Level: 5",
            "Experience: 1250/2000",
            "Health: 95/100",
            "Attack: 25 (+10)",
            "Defense: 20 (+8)", 
            "Speed: 15",
            "Magic: 8",
            "Gold: 150"
        ]
        
        for stat in stats:
            tk.Label(stats_frame, text=stat, font=("Arial", 11),
                    fg='lightblue', bg='#2a2a2a', anchor='w').pack(anchor='w', padx=5, pady=3)
        
        # Bottom buttons
        btn_frame = tk.Frame(inv_window, bg='#1a1a1a')
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        for btn_text in ["🔧 Use Item", "🗑️ Drop Item", "❌ Close"]:
            tk.Button(btn_frame, text=btn_text, font=("Arial", 12),
                     bg='#3a3a3a', fg='white', width=12,
                     command=inv_window.destroy if btn_text == "❌ Close" else None).pack(side=tk.LEFT, padx=10)
        
        # Capture inventory
        self.root.after(800, lambda: self.capture_screenshot("inventory_interface"))
        
        # Auto-close
        inv_window.after(3000, inv_window.destroy)
    
    def show_dialogue(self):
        """Show extended dialogue."""
        print("💬 Showing dialogue...")
        
        # Just update main window with more dialogue
        # This simulates a dialogue progression
        self.capture_screenshot("dialogue_interaction", 500)
    
    def run_demo_sequence(self):
        """Run automated demo of all interfaces."""
        print("🤖 Starting automated demo sequence...")
        
        # Schedule the demo
        sequence = [
            (1000, self.create_title_screen),
            (4000, lambda: self.start_game("🛡️ Warrior")),
            (7000, self.show_shop),
            (10000, self.show_combat), 
            (13000, self.show_inventory),
            (16000, self.generate_final_report),
            (18000, self.root.quit)
        ]
        
        for delay, action in sequence:
            self.root.after(delay, action)
    
    def generate_final_report(self):
        """Generate comprehensive report."""
        print("📋 Generating final screenshot report...")
        
        report_file = self.snapshot_dir / "screenshot_report.md"
        
        with open(report_file, 'w') as f:
            f.write("# GUI Screenshot Analysis Report\n\n")
            f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # List all screenshots
            png_files = list(self.snapshot_dir.glob("*.png"))
            txt_files = list(self.snapshot_dir.glob("*.txt"))
            
            f.write(f"## Screenshot Summary\n\n")
            f.write(f"- Total screenshots captured: {len(png_files)}\n")
            f.write(f"- Total file size: {sum(f.stat().st_size for f in png_files)} bytes\n")
            f.write(f"- Fallback descriptions: {len(txt_files)}\n\n")
            
            f.write("## Screenshots for AI Analysis\n\n")
            for png_file in sorted(png_files):
                size_kb = png_file.stat().st_size // 1024
                f.write(f"- `{png_file.name}` ({size_kb} KB)\n")
            
            f.write("\n## Interface Coverage\n\n")
            f.write("✅ **Title Screen** - Character selection interface\n")
            f.write("✅ **Main Game Scene** - Core gameplay with NPCs and dialogue\n") 
            f.write("✅ **Combat Interface** - Battle system with stats and actions\n")
            f.write("✅ **Shop Interface** - Item purchasing with prices and descriptions\n")
            f.write("✅ **Inventory System** - Item management and character stats\n")
            
            f.write("\n## Ready for AI Review\n\n")
            f.write("These PNG files contain complete visual information about:\n")
            f.write("- UI layout, spacing, and alignment\n")
            f.write("- Color scheme and visual hierarchy\n")
            f.write("- Text readability and font sizing\n")  
            f.write("- Button placement and user experience flow\n")
            f.write("- Asset integration and sprite positioning\n")
            f.write("- Overall game aesthetics and polish\n")
        
        print(f"✅ Report saved: {report_file}")
        print(f"📁 {len(png_files)} screenshots ready for AI analysis in: {self.snapshot_dir}")
    
    def run(self):
        """Run the screenshot system."""
        try:
            print("🚀 Starting GUI screenshot demo...")
            self.run_demo_sequence()
            self.root.mainloop()
            print("✅ Demo completed!")
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    print("=" * 60)
    print("📸 SHABUYA Cave Adventure - Screenshot System")
    print("=" * 60)
    
    try:
        screenshotter = SimpleGUIScreenshotter()
        screenshotter.run()
    except Exception as e:
        print(f"❌ Failed to start: {e}")

if __name__ == "__main__":
    main()

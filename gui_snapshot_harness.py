#!/usr/bin/env python3
"""
GUI Snapshot Harness - Automated Visual Testing
==============================================
Automatically captures screenshots of the SHABUYA Cave Adventure GUI
at different game states for AI analysis without manual intervention.

This creates PNG snapshots that can be analyzed programmatically.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys
from PIL import Image, ImageTk, ImageGrab
import time
import threading
from pathlib import Path

# Add proper paths to import game modules
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

class GUISnapshotHarness:
    def __init__(self):
        """Initialize the snapshot harness with GUI automation capabilities."""
        print("📸 Starting GUI Snapshot Harness...")
        
        # Create snapshots directory
        self.snapshot_dir = Path("gui_snapshots")
        self.snapshot_dir.mkdir(exist_ok=True)
        
        # Initialize Tkinter
        try:
            self.root = tk.Tk()
            self.root.title("🏴‍☠️ SHABUYA Cave Adventure - Snapshot Mode")
            self.root.geometry("1000x700")
            self.root.configure(bg='#0a0a0a')
        except Exception as e:
            print(f"Cannot create GUI window: {e}")
            return
        
        # Import game modules after path setup
        self.setup_game_modules()
        
        # Game state initialization
        self.player = None
        self.current_scene = None
        self.scenes = {}
        self.SCENE_NAMES = {}
        self.game_state = {
            'visited_village': False,
            'visited_armory': False,
            'visited_scenes': set(),
            'rogue_escaped_alley': False,
            'defeated_chief': False,
            'alley_creature_dead': False
        }
        
        # Asset paths and caches
        self.backgrounds = {}
        self.sprites = {}
        self.assets_dir = os.path.join(current_dir, 'assets')
        
        # GUI elements
        self.canvas = None
        self.dialogue_frame = None
        self.dialogue_text = None
        self.options_frame = None
        
        # Snapshot control
        self.snapshot_count = 0
        self.auto_mode = True
        
        print("🎮 Harness initialized, loading assets...")
        self.load_all_assets()
        self.create_title_screen()
        
        # Start automated snapshot sequence
        self.root.after(1000, self.start_automated_sequence)
    
    def setup_game_modules(self):
        """Import and setup game modules with error handling."""
        try:
            from core.scenes import get_all_scenes
            from entities.player import Player
            from core.combat import simulate_combat
            from config import GAME_CONFIG
            
            self.get_all_scenes = get_all_scenes
            self.Player = Player
            self.simulate_combat = simulate_combat
            self.GAME_CONFIG = GAME_CONFIG
            
            print("✅ Game modules loaded successfully")
        except ImportError as e:
            print(f"⚠️  Warning: Could not import game modules: {e}")
            # Create minimal fallback
            self.create_fallback_modules()
    
    def create_fallback_modules(self):
        """Create minimal fallback game logic for testing."""
        print("🔧 Creating fallback game modules...")
        
        class FallbackPlayer:
            def __init__(self, name, player_class):
                self.name = name
                self.player_class = player_class
                self.health = 100
                self.attack = 10
        
        def fallback_scenes():
            return {
                'town_square': {
                    'name': 'Town Square',
                    'description': 'You stand in the heart of the village.',
                    'background': 'town_square.jpg',
                    'options': [
                        {'text': 'Visit the Armory', 'action': 'armory'},
                        {'text': 'Explore the Forest', 'action': 'forest_entrance'}
                    ]
                },
                'armory': {
                    'name': 'Village Armory',
                    'description': 'The blacksmith greets you warmly.',
                    'background': 'armory.jpg',
                    'sprite': 'blacksmith.png',
                    'options': [
                        {'text': 'Buy Equipment', 'action': 'shop'},
                        {'text': 'Return to Town', 'action': 'town_square'}
                    ]
                }
            }
        
        self.Player = FallbackPlayer
        self.get_all_scenes = fallback_scenes
        self.GAME_CONFIG = {'PLAYER_CLASSES': ['Warrior', 'Rogue', 'Mage']}
    
    def load_all_assets(self):
        """Load all background images and sprites for the game."""
        print("🖼️  Loading game assets...")
        
        # Load backgrounds
        backgrounds_dir = os.path.join(self.assets_dir, 'backgrounds')
        if os.path.exists(backgrounds_dir):
            for filename in os.listdir(backgrounds_dir):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img_path = os.path.join(backgrounds_dir, filename)
                        img = Image.open(img_path)
                        img = img.resize((1000, 700), Image.Resampling.LANCZOS)
                        self.backgrounds[filename.split('.')[0]] = ImageTk.PhotoImage(img)
                        print(f"  📁 Loaded background: {filename}")
                    except Exception as e:
                        print(f"  ❌ Error loading {filename}: {e}")
        
        # Load sprites
        sprites_dir = os.path.join(self.assets_dir, 'sprites')
        if os.path.exists(sprites_dir):
            for filename in os.listdir(sprites_dir):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img_path = os.path.join(sprites_dir, filename)
                        img = Image.open(img_path)
                        img = img.resize((200, 300), Image.Resampling.LANCZOS)
                        self.sprites[filename.split('.')[0]] = ImageTk.PhotoImage(img)
                        print(f"  🧙 Loaded sprite: {filename}")
                    except Exception as e:
                        print(f"  ❌ Error loading {filename}: {e}")
        
        print(f"✅ Assets loaded: {len(self.backgrounds)} backgrounds, {len(self.sprites)} sprites")
    
    def create_title_screen(self):
        """Create the initial title screen."""
        print("🎭 Creating title screen...")
        
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main canvas for the title screen
        self.canvas = tk.Canvas(self.root, width=1000, height=700, bg='#0a0a0a', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Background (if available)
        if 'title_screen' in self.backgrounds:
            self.canvas.create_image(500, 350, image=self.backgrounds['title_screen'])
        else:
            # Create gradient-like effect with rectangles
            for i in range(20):
                color_val = int(10 + i * 2)
                color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
                self.canvas.create_rectangle(0, i*35, 1000, (i+1)*35, fill=color, outline=color)
        
        # Title text
        self.canvas.create_text(500, 200, text="SHABUYA", 
                               font=("Pirate", 48, "bold"), fill="#FFD700", anchor="center")
        self.canvas.create_text(500, 260, text="Cave Adventure", 
                               font=("Arial", 32, "italic"), fill="#C0C0C0", anchor="center")
        
        # Create character selection buttons
        self.create_character_selection()
        
        # Take initial snapshot
        self.root.after(500, lambda: self.take_snapshot("01_title_screen"))
    
    def create_character_selection(self):
        """Create character class selection interface."""
        # Character selection frame
        char_frame = tk.Frame(self.root, bg='#1a1a1a', bd=2, relief=tk.RAISED)
        char_frame.place(x=300, y=400, width=400, height=200)
        
        tk.Label(char_frame, text="Choose Your Class:", 
                font=("Arial", 16, "bold"), fg="#FFD700", bg='#1a1a1a').pack(pady=10)
        
        classes = ['Warrior', 'Rogue', 'Mage']
        for i, cls in enumerate(classes):
            btn = tk.Button(char_frame, text=cls, font=("Arial", 14),
                           bg='#2a2a2a', fg='white', activebackground='#3a3a3a',
                           command=lambda c=cls: self.start_game(c),
                           width=12, pady=5)
            btn.pack(pady=5)
    
    def start_game(self, player_class):
        """Start the game with selected character class."""
        print(f"🎯 Starting game as {player_class}")
        
        # Create player
        self.player = self.Player("Hero", player_class)
        
        # Load scenes
        try:
            self.scenes = self.get_all_scenes()
            self.SCENE_NAMES = {key: scene.get('name', key.title()) for key, scene in self.scenes.items()}
        except:
            self.scenes = {'town_square': {'name': 'Town Square', 'description': 'Starting location'}}
            self.SCENE_NAMES = {'town_square': 'Town Square'}
        
        # Take character selection snapshot
        self.root.after(100, lambda: self.take_snapshot(f"02_character_selected_{player_class.lower()}"))
        
        # Start first scene
        self.root.after(1000, lambda: self.enter_scene('town_square'))
    
    def enter_scene(self, scene_key):
        """Enter a specific scene and render it."""
        print(f"🏛️  Entering scene: {scene_key}")
        
        if scene_key not in self.scenes:
            print(f"⚠️  Scene '{scene_key}' not found!")
            return
        
        self.current_scene = scene_key
        scene = self.scenes[scene_key]
        self.game_state['visited_scenes'].add(scene_key)
        
        # Clear and recreate the interface
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main canvas
        self.canvas = tk.Canvas(self.root, width=1000, height=500, bg='#0a0a0a', highlightthickness=0)
        self.canvas.pack(fill=tk.X)
        
        # Set background
        bg_key = scene.get('background', '').replace('.jpg', '').replace('.png', '')
        if bg_key in self.backgrounds:
            # Resize background for scene area only
            bg_img = self.backgrounds[bg_key]._PhotoImage__photo
            resized_bg = bg_img.zoom(1, 1).subsample(1, 1)  # Keep original size
            self.canvas.create_image(500, 250, image=self.backgrounds[bg_key])
        
        # Add sprites if specified
        sprite_key = scene.get('sprite', '').replace('.png', '').replace('.jpg', '')
        if sprite_key in self.sprites:
            self.canvas.create_image(750, 300, image=self.sprites[sprite_key])
        
        # Player info panel
        info_frame = tk.Frame(self.root, bg='#1a1a1a', height=50)
        info_frame.pack(fill=tk.X)
        info_frame.pack_propagate(False)
        
        tk.Label(info_frame, text=f"Player: {self.player.name} ({self.player.player_class}) | HP: {self.player.health}",
                font=("Arial", 12), fg='white', bg='#1a1a1a').pack(pady=15)
        
        # Dialogue area
        self.dialogue_frame = tk.Frame(self.root, bg='#2a2a2a', height=150)
        self.dialogue_frame.pack(fill=tk.BOTH, expand=True)
        self.dialogue_frame.pack_propagate(False)
        
        # Scene description
        desc_text = tk.Text(self.dialogue_frame, height=4, wrap=tk.WORD, 
                           font=("Arial", 11), bg='#2a2a2a', fg='white',
                           bd=1, relief=tk.SUNKEN)
        desc_text.pack(fill=tk.X, padx=10, pady=5)
        desc_text.insert(tk.END, scene.get('description', 'No description available.'))
        desc_text.config(state=tk.DISABLED)
        
        # Options buttons
        self.options_frame = tk.Frame(self.dialogue_frame, bg='#2a2a2a')
        self.options_frame.pack(fill=tk.X, padx=10, pady=5)
        
        options = scene.get('options', [])
        for i, option in enumerate(options):
            btn = tk.Button(self.options_frame, text=option['text'],
                           font=("Arial", 10), bg='#3a3a3a', fg='white',
                           activebackground='#4a4a4a',
                           command=lambda act=option['action']: self.handle_option(act))
            btn.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Take scene snapshot
        self.root.after(200, lambda: self.take_snapshot(f"03_scene_{scene_key}"))
    
    def handle_option(self, action):
        """Handle player option selection."""
        print(f"🎯 Player chose action: {action}")
        
        # Take action snapshot
        self.root.after(100, lambda: self.take_snapshot(f"04_action_{action}"))
        
        # Navigate to next scene or handle action
        if action in self.scenes:
            self.root.after(500, lambda: self.enter_scene(action))
        else:
            # Handle special actions
            self.root.after(500, lambda: self.handle_special_action(action))
    
    def handle_special_action(self, action):
        """Handle special game actions."""
        print(f"🎭 Handling special action: {action}")
        
        if action == 'shop':
            self.show_shop_interface()
        elif action == 'combat':
            self.show_combat_interface()
        else:
            # Default: return to town square
            self.root.after(500, lambda: self.enter_scene('town_square'))
    
    def show_shop_interface(self):
        """Show a sample shop interface."""
        print("🏪 Opening shop interface...")
        
        # Create shop overlay
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Village Shop")
        shop_window.geometry("400x300")
        shop_window.configure(bg='#2a2a2a')
        
        tk.Label(shop_window, text="Village Shop", font=("Arial", 16, "bold"),
                fg="#FFD700", bg='#2a2a2a').pack(pady=10)
        
        items = ["Iron Sword - 50 gold", "Health Potion - 25 gold", "Magic Scroll - 75 gold"]
        for item in items:
            tk.Button(shop_window, text=item, font=("Arial", 12),
                     bg='#3a3a3a', fg='white', width=25).pack(pady=5)
        
        tk.Button(shop_window, text="Close Shop", font=("Arial", 12),
                 bg='#4a4a4a', fg='white', command=shop_window.destroy).pack(pady=10)
        
        # Take shop snapshot
        self.root.after(300, lambda: self.take_snapshot("05_shop_interface"))
    
    def show_combat_interface(self):
        """Show a sample combat interface."""
        print("⚔️ Starting combat interface...")
        
        # Combat overlay
        combat_window = tk.Toplevel(self.root)
        combat_window.title("Combat!")
        combat_window.geometry("500x400")
        combat_window.configure(bg='#1a1a1a')
        
        tk.Label(combat_window, text="⚔️ COMBAT ⚔️", font=("Arial", 20, "bold"),
                fg="red", bg='#1a1a1a').pack(pady=10)
        
        # Combat stats
        stats_frame = tk.Frame(combat_window, bg='#2a2a2a')
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(stats_frame, text=f"Player: {self.player.name} | HP: {self.player.health}",
                font=("Arial", 12), fg='white', bg='#2a2a2a').pack()
        tk.Label(stats_frame, text="Enemy: Cave Troll | HP: 80",
                font=("Arial", 12), fg='red', bg='#2a2a2a').pack()
        
        # Combat actions
        actions_frame = tk.Frame(combat_window, bg='#1a1a1a')
        actions_frame.pack(pady=20)
        
        for action in ["Attack", "Defend", "Use Item", "Run"]:
            tk.Button(actions_frame, text=action, font=("Arial", 12),
                     bg='#3a3a3a', fg='white', width=12, pady=5).pack(pady=3)
        
        # Take combat snapshot
        self.root.after(300, lambda: self.take_snapshot("06_combat_interface"))
    
    def take_snapshot(self, name):
        """Capture a screenshot of the current GUI state."""
        try:
            self.snapshot_count += 1
            filename = f"{self.snapshot_count:02d}_{name}.png"
            filepath = self.snapshot_dir / filename
            
            print(f"📸 Taking snapshot: {filename}")
            
            # Update the display first
            self.root.update()
            self.root.update_idletasks()
            
            # Get window geometry
            x = self.root.winfo_rootx()
            y = self.root.winfo_rooty()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            
            # Capture the window area
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            screenshot.save(filepath)
            
            print(f"✅ Snapshot saved: {filepath}")
            
        except Exception as e:
            print(f"❌ Error taking snapshot: {e}")
            # Fallback: save a text description
            with open(self.snapshot_dir / f"{name}.txt", 'w') as f:
                f.write(f"Snapshot failed: {e}\n")
                f.write(f"Current scene: {self.current_scene}\n")
                f.write(f"Player: {self.player.name if self.player else 'None'}\n")
                f.write(f"Game state: {self.game_state}\n")
    
    def start_automated_sequence(self):
        """Start the automated testing sequence."""
        print("🤖 Starting automated GUI testing sequence...")
        
        # Schedule automatic progression through game states
        sequence = [
            (2000, lambda: self.start_game('Warrior')),
            (4000, lambda: self.enter_scene('armory') if 'armory' in self.scenes else None),
            (6000, lambda: self.show_shop_interface()),
            (8000, lambda: self.show_combat_interface()),
            (10000, self.generate_summary_report),
        ]
        
        for delay, action in sequence:
            self.root.after(delay, action)
    
    def generate_summary_report(self):
        """Generate a summary report of all snapshots."""
        print("📋 Generating snapshot summary report...")
        
        report_path = self.snapshot_dir / "snapshot_report.md"
        with open(report_path, 'w') as f:
            f.write("# GUI Snapshot Report\n\n")
            f.write("## Automated GUI Testing Results\n\n")
            f.write(f"Total snapshots captured: {self.snapshot_count}\n\n")
            
            # List all snapshots
            f.write("## Snapshot Gallery\n\n")
            for snapshot_file in sorted(self.snapshot_dir.glob("*.png")):
                f.write(f"- `{snapshot_file.name}` - {snapshot_file.stat().st_size} bytes\n")
            
            f.write("\n## Game States Tested\n\n")
            f.write("1. Title Screen\n")
            f.write("2. Character Selection\n")
            f.write("3. Scene Navigation\n")
            f.write("4. Shop Interface\n")
            f.write("5. Combat Interface\n")
            
            f.write(f"\n## Assets Loaded\n\n")
            f.write(f"- Backgrounds: {len(self.backgrounds)}\n")
            f.write(f"- Sprites: {len(self.sprites)}\n")
        
        print(f"✅ Report saved: {report_path}")
        print("🎯 Automated testing complete!")
        
        # Also print file listing for immediate review
        print("\n📁 Generated Snapshots:")
        for snapshot_file in sorted(self.snapshot_dir.glob("*")):
            print(f"  - {snapshot_file.name}")
    
    def run(self):
        """Start the snapshot harness GUI."""
        try:
            print("🚀 Starting GUI snapshot harness...")
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\n🛑 Snapshot harness interrupted by user")
        except Exception as e:
            print(f"❌ Harness error: {e}")

def main():
    """Main entry point for the snapshot harness."""
    print("=" * 60)
    print("🎮 SHABUYA Cave Adventure - GUI Snapshot Harness")
    print("=" * 60)
    
    try:
        harness = GUISnapshotHarness()
        if hasattr(harness, 'root'):
            harness.run()
        else:
            print("❌ Failed to initialize GUI - likely no display available")
    except Exception as e:
        print(f"❌ Fatal error: {e}")

if __name__ == "__main__":
    main()

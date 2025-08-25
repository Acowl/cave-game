#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Desktop GUI
Clean, simple interface optimized for desktop use
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
from pathlib import Path
import threading
import queue
import io

# Import the actual game engine
from game_refactored import play_game
from game_events import start_game
from ui import title_screen

class CaveGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.player = None
        self.game_state = "menu"
        self.current_scene = None
        self.scenes = None
        self.game_thread = None
        self.command_queue = queue.Queue()
        self.response_queue = queue.Queue()
        self.waiting_for_input = False
        self.current_choices = []
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
        
        from config import STARTING_STAT_VALUE
        
        # Get player class based on weapon
        if hasattr(self.player, 'weapon'):
            if self.player.weapon.name == 'Dagger':
                char_class = 'Rogue'
            elif self.player.weapon.name == 'Axe':
                char_class = 'Warrior'
            elif self.player.weapon.name == 'Wand':
                char_class = 'Mage'
            else:
                char_class = 'Unknown'
        else:
            char_class = 'Unknown'
        
        stats_text = f"""
Class: {char_class}
Level: {getattr(self.player, 'level', 1)}
Weapon: {self.player.weapon.name if hasattr(self.player, 'weapon') else 'None'}

💪 Strength: {getattr(self.player, 'strength', STARTING_STAT_VALUE)}
🧠 Intelligence: {getattr(self.player, 'intelligence', STARTING_STAT_VALUE)}
⚡ Agility: {getattr(self.player, 'agility', STARTING_STAT_VALUE)}
🛡️ Vitality: {getattr(self.player, 'vitality', STARTING_STAT_VALUE)}
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
        """Handle game commands - integrated with actual game logic"""
        command = command.lower().strip()
        
        # Handle menu state
        if self.game_state == "menu":
            if command in ['1', 'start', 'new', 'play']:
                return self.start_new_game()
            elif command in ['2', 'exit', 'quit']:
                self.root.quit()
                return "👋 Goodbye! Thanks for playing!"
            else:
                return """🗻 SHABUYA - Cave Adventure 🗻
                
1. Start New Game
2. Exit

Enter '1' to start or '2' to exit."""
        
        # Handle class selection
        elif self.game_state == "class_selection":
            if command in ['1', 'rogue']:
                return self.select_class('rogue')
            elif command in ['2', 'warrior']:
                return self.select_class('warrior')
            elif command in ['3', 'mage']:
                return self.select_class('mage')
            else:
                return """Choose your class:
1: Rogue (Dagger)
2: Warrior (Axe)
3: Mage (Wand)

Enter 1, 2, or 3 to select your class."""
        
        # Handle active gameplay
        elif self.game_state == "playing":
            return self.handle_gameplay_command(command)
        
        # Default response
        return f"❓ Unknown command in current state: '{command}'"
    
    def start_new_game(self):
        """Start a new game session"""
        self.game_state = "class_selection"
        return """🎯 Starting new adventure...

Choose your class:
1: Rogue (Stealth and agility)
2: Warrior (Strength and combat)
3: Mage (Magic and intelligence)

Enter the number of your class (1-3):"""
    
    def select_class(self, class_type):
        """Handle class selection and start the game"""
        from item import dagger, axe, wand
        from player import Player
        from item import Inventory
        
        # Create player
        self.player = Player()
        self.player.inventory = Inventory()
        
        if class_type == 'rogue':
            self.player.weapon = dagger
            class_name = "Rogue"
        elif class_type == 'warrior':
            self.player.weapon = axe
            class_name = "Warrior"
        elif class_type == 'mage':
            self.player.weapon = wand
            class_name = "Mage"
        
        self.game_state = "playing"
        
        # Initialize game world
        from scenes import setup_scenes
        from config import SCENE_NAMES
        
        self.scenes = setup_scenes()
        self.current_scene = self.scenes[SCENE_NAMES['CAVE_ENTRANCE']]
        self.game_context = {
            'visited_village': False,
            'visited_armory': False,
            'visited_scenes': set(),
            'rogue_escaped_alley': False,
            'defeated_chief': False,
            'alley_creature_dead': False
        }
        
        self.update_character_display()
        
        return f"""You are a {class_name}. You start with a {self.player.weapon.name}.

🗻 CAVE ENTRANCE 🗻
You find yourself in a dark cave with only a crack in the wall visible.

What do you want to do?
1: Go through the crack
2: Sit and cry  
3: Look around
4: Quit

Available commands: 1, 2, 3, 4, or type commands directly."""
    
    def handle_gameplay_command(self, command):
        """Handle commands during active gameplay"""
        if not self.current_scene:
            return "❌ Game error - no current scene loaded."
        
        scene_name = self.current_scene.name
        
        # Handle Cave Entrance
        if scene_name == "Cave Entrance":
            return self.handle_cave_entrance_command(command)
        elif scene_name == "Skull Chamber":
            return self.handle_skull_chamber_command(command)
        elif scene_name == "Primitive Village":
            return self.handle_village_command(command)
        elif scene_name == "Alley":
            return self.handle_alley_command(command)
        elif scene_name == "Armory":
            return self.handle_armory_command(command)
        elif scene_name == "Cave People Chief House":
            return self.handle_chief_house_command(command)
        elif scene_name == "Healing Pool":
            return self.handle_healing_pool_command(command)
        elif scene_name == "Primitive Village Changed":
            return self.handle_final_boss_command(command)
        else:
            return f"🗺️ You're in {scene_name}. Available commands: help, quit"
    
    def handle_cave_entrance_command(self, command):
        """Handle Cave Entrance commands"""
        if command in ['1', 'crack', 'go crack', 'through crack']:
            from config import SCENE_NAMES
            self.current_scene = self.scenes[SCENE_NAMES['SKULL_CHAMBER']]
            return """You squeeze through the crack in the wall...

🗻 SKULL CHAMBER 🗻
A vast chamber dominated by a colossal skull. As you explore the chamber, you see a primitive creature scurrying away among the shadows near the giant skull.

What do you want to do?
1: Chase after the creature
2: Stay and observe
3: Quit

Available commands: 1, 2, 3"""
        
        elif command in ['2', 'sit', 'cry']:
            return "You feel much better and would like to go through the crack."
        
        elif command in ['3', 'look', 'look around']:
            return "You look around but it's dark and you can't see anything except the crack in the wall."
        
        elif command in ['4', 'quit']:
            self.root.quit()
            return "� Thanks for playing!"
        
        else:
            return """You're in a dark cave. The only thing you notice is the crack in the wall.

What do you want to do?
1: Go through the crack
2: Sit and cry
3: Look around
4: Quit"""
    
    def handle_skull_chamber_command(self, command):
        """Handle Skull Chamber commands"""
        if command in ['1', 'chase', 'chase creature']:
            from config import SCENE_NAMES
            self.current_scene = self.scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]
            self.game_context['visited_village'] = True
            return """You run after the moving figure, following its fleeting shadow through the chamber. You are led straight into the primitive village.

🗻 PRIMITIVE VILLAGE 🗻
You step into the heart of the primitive village. Crude huts made of bone and hide cluster around a central fire pit, where embers glow and smoke drifts into the cavernous air. Strange symbols are painted on the rocks, and you hear the distant chatter of unseen creatures. Paths lead off in several directions: a shadowy alley, a fortified armory, and a large chief's house adorned with trophies.

Where would you like to go?
1: Enter the Alley (dangerous shadows)
2: Approach the Armory (locked chamber)
3: Visit the Chief's House (imposing hut)
4: Stay by the fire pit
5: Quit"""
        
        elif command in ['2', 'stay', 'observe']:
            return """You decide not to chase after it and remain cautious.
Suddenly, a rockfall blocks the path behind you! There is only one way forward now.

You can only move forward now.
1: Move forward
2: Quit"""
        
        elif command in ['3', 'quit']:
            self.root.quit()
            return "👋 Thanks for playing!"
        
        else:
            return """You're in a vast chamber dominated by a colossal skull. You see a primitive creature scurrying away.

What do you want to do?
1: Chase after the creature
2: Stay and observe
3: Quit"""
    
    def handle_village_command(self, command):
        """Handle Primitive Village commands"""
        if command in ['1', 'alley', 'enter alley']:
            from config import SCENE_NAMES
            self.current_scene = self.scenes[SCENE_NAMES['ALLEY']]
            return """You step cautiously into the narrow alley...

🗻 ALLEY 🗻
A primitive ground-dwelling creature bursts from a hidden burrow!

What do you do?
1: Attack the creature
2: Try to escape
3: Quit"""
        
        elif command in ['2', 'armory', 'approach armory']:
            from scenes import check_scene_access
            armory_scene = self.scenes['Armory']
            if check_scene_access(armory_scene, self.player):
                self.current_scene = armory_scene
                return self.enter_armory()
            else:
                return "The Armory is locked. You need the Armory Key to enter.\nYou're still in the village."
        
        elif command in ['3', 'chief', 'chief house', 'visit chief']:
            from scenes import check_scene_access
            chief_scene = self.scenes['Cave People Chief House']
            if check_scene_access(chief_scene, self.player):
                self.current_scene = chief_scene
                return self.enter_chief_house()
            else:
                return "The Chief's House is locked. You need the Town Key to enter.\nYou're still in the village."
        
        elif command in ['4', 'fire', 'stay', 'fire pit']:
            return """You linger by the fire pit, feeling the warmth and watching the shadows dance. The village seems to hold its breath, waiting for your next move.

Where would you like to go?
1: Enter the Alley (dangerous shadows)
2: Approach the Armory (locked chamber)
3: Visit the Chief's House (imposing hut)
4: Stay by the fire pit
5: Quit"""
        
        elif command in ['5', 'quit']:
            self.root.quit()
            return "👋 Thanks for playing!"
        
        else:
            return """You're in the primitive village center by the fire pit.

Where would you like to go?
1: Enter the Alley (dangerous shadows)
2: Approach the Armory (locked chamber)
3: Visit the Chief's House (imposing hut)
4: Stay by the fire pit
5: Quit"""
    
    def handle_alley_command(self, command):
        """Handle Alley commands"""
        if self.game_context.get('alley_creature_dead', False):
            if command in ['1', 'search']:
                return "You search the area thoroughly, but find nothing new."
            elif command in ['2', 'village', 'return']:
                from config import SCENE_NAMES
                self.current_scene = self.scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]
                return "You return to the village."
            elif command in ['3', 'quit']:
                self.root.quit()
                return "👋 Thanks for playing!"
        else:
            if command in ['1', 'attack']:
                return self.handle_alley_combat()
            elif command in ['2', 'escape']:
                return self.handle_alley_escape()
            elif command in ['3', 'quit']:
                self.root.quit()
                return "👋 Thanks for playing!"
        
        return "Invalid choice. Enter 1, 2, or 3."
    
    def handle_alley_combat(self):
        """Handle combat in the alley"""
        from ui import display_weapon_choices
        from combat import execute_weapon_attack
        from game_events import handle_level_up, handle_loot_collection
        
        # Simplified weapon selection for GUI
        weapon_name = self.player.weapon.name
        success, message = execute_weapon_attack(self.player, self.player.weapon, "alley_creature")
        
        result = f"You attack with your {weapon_name}!\n{message}"
        
        if success:
            result += "\n\nThe creature lets out a final, defeated roar before collapsing in a heap.\nVictory is yours!"
            handle_level_up(self.player)
            self.game_context['alley_creature_dead'] = True
            handle_loot_collection(self.player)
            self.update_character_display()
            
            from config import SCENE_NAMES
            self.current_scene = self.scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]
            result += "\n\nYou return to the village, victorious and stronger than before."
        else:
            result += "\n\n💀 YOU HAVE DIED 💀\nGame Over! Start a new game to try again."
            self.game_state = "menu"
        
        return result
    
    def handle_alley_escape(self):
        """Handle escape attempt in alley"""
        from item import dagger
        from game_events import handle_level_up
        
        if self.player.weapon == dagger:  # Rogue can escape
            result = "Your rogue training allows you to escape successfully!"
            self.game_context['rogue_escaped_alley'] = True
            handle_level_up(self.player)
            self.update_character_display()
            
            from config import SCENE_NAMES
            self.current_scene = self.scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]
            result += "\n\nYou return to the village."
            return result
        else:
            result = "You fail to escape! The creature catches you.\n\n💀 YOU HAVE DIED 💀\nGame Over! Start a new game to try again."
            self.game_state = "menu"
            return result
    
    def enter_armory(self):
        """Handle entering the armory"""
        return """🗻 ARMORY 🗻
You enter the ancient armory. Three enhanced weapons rest on pedestals, glowing with magical energy:
- The Shadow Blade (Enhanced Dagger)
- The Bone Crusher (Enhanced Axe)  
- The Skull Scepter (Enhanced Wand)
In the corner, you notice a key labeled 'Town Key' on a small table.

What would you like to do?
1: Take the Shadow Blade
2: Take the Bone Crusher
3: Take the Skull Scepter
4: Take the Town Key
5: Leave the armory
6: Quit"""
    
    def enter_chief_house(self):
        """Handle entering the chief house"""
        if self.game_context.get('defeated_chief', False):
            return """The Chief's lifeless body lies on the floor. The path to the healing pool remains open.

Where would you like to go?
1: Enter the Healing Pool
2: Return to the village
3: Quit"""
        else:
            return """🗻 CHIEF'S HOUSE 🗻
You enter the imposing chief's house...
The Chief challenges you to battle!

Choose your action:
1: Fight the Chief
2: Try to escape
3: Quit"""
    
    def handle_armory_command(self, command):
        """Handle Armory scene commands"""
        # Initialize collected weapons if needed
        if not hasattr(self.player, 'collected_weapons'):
            self.player.collected_weapons = []
        
        if command in ['1', 'shadow', 'blade', 'dagger']:
            from item import enhanced_dagger
            if enhanced_dagger not in self.player.collected_weapons:
                self.player.collected_weapons.append(enhanced_dagger)
                return "You take the Shadow Blade! Its dark energy courses through you."
            else:
                return "You already have the Shadow Blade."
        
        elif command in ['2', 'bone', 'crusher', 'axe']:
            from item import enhanced_axe
            if enhanced_axe not in self.player.collected_weapons:
                self.player.collected_weapons.append(enhanced_axe)
                return "You take the Bone Crusher! Its weight feels perfect in your hands."
            else:
                return "You already have the Bone Crusher."
        
        elif command in ['3', 'skull', 'scepter', 'wand']:
            from item import enhanced_wand
            if enhanced_wand not in self.player.collected_weapons:
                self.player.collected_weapons.append(enhanced_wand)
                return "You take the Skull Scepter! Mystical power flows through it."
            else:
                return "You already have the Skull Scepter."
        
        elif command in ['4', 'town', 'key']:
            if not self.player.inventory.has_item("Town Key"):
                from item import Item
                town_key = Item("Town Key", "An ornate key that opens the Chief's House.")
                self.player.inventory.add_item(town_key)
                return "You take the Town Key. It feels warm to the touch."
            else:
                return "You already have the Town Key."
        
        elif command in ['5', 'leave']:
            from config import SCENE_NAMES
            self.current_scene = self.scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]
            return "You return to the village."
        
        elif command in ['6', 'quit']:
            self.root.quit()
            return "👋 Thanks for playing!"
        
        else:
            return "Invalid choice. Enter 1-6."
    
    def handle_chief_house_command(self, command):
        """Handle Chief House commands"""
        return "Chief House commands coming soon..."
    
    def handle_healing_pool_command(self, command):
        """Handle Healing Pool commands"""
        return "Healing Pool commands coming soon..."
    
    def handle_final_boss_command(self, command):
        """Handle final boss commands"""
        return "Final boss commands coming soon..."
            
    def new_game(self):
        """Start a new game"""
        self.game_state = "menu"
        self.player = None
        self.current_scene = None
        self.scenes = None
        self.game_context = {}
        
        # Clear displays
        self.game_display.config(state=tk.NORMAL)
        self.game_display.delete(1.0, tk.END)
        self.game_display.config(state=tk.DISABLED)
        
        self.display_text("🗻 SHABUYA - Cave Adventure 🗻")
        self.display_text("")
        self.display_text("Would you like to play?")
        self.display_text("1. Start New Game")
        self.display_text("2. Exit")
        self.display_text("")
        self.display_text("Enter '1' to start or '2' to exit.")
        
    def save_game(self):
        """Save current game"""
        if self.player:
            messagebox.showinfo("Save Game", "Save feature coming soon!")
        else:
            messagebox.showwarning("No Game", "No active game to save.")
        
    def load_game(self):
        """Load saved game"""
        messagebox.showinfo("Load Game", "Load feature coming soon!")
        
    def run(self):
        """Start the GUI"""
        self.new_game()  # Initialize with menu
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
#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Player GUI (Fixed Version)
==================================================
Immersive player-facing interface with dynamic backgrounds, dialogue boxes,
and proper sprite rendering based on scenes and encounters.

This version includes proper error handling and corrected import paths.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys
from PIL import Image, ImageTk

# Add proper paths to import game modules
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

class PlayerGameGUI:
    def __init__(self):
        print("🎮 Starting SHABUYA Cave Adventure...")
        
        # Initialize Tkinter with error handling
        try:
            self.root = tk.Tk()
            self.root.title("🏴‍☠️ SHABUYA Cave Adventure")
            self.root.geometry("1000x700")
            self.root.configure(bg='#0a0a0a')
        except Exception as e:
            print(f"Cannot create GUI window: {e}")
            print("This may be due to no display environment (headless server)")
            return
        
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
        self.sprites_dir = "assets/sprites"
        self.backgrounds_dir = "assets/backgrounds"
        self.sprite_cache = {}
        self.background_cache = {}
        
        # Current display state
        self.current_background = None
        self.current_player_sprite = None
        self.current_enemy_sprite = None
        self.current_dialogue = ""
        self.current_options = []
        self.selected_option = 0
        
        # Character to Sprite Mapping
        self.CHARACTER_SPRITE_MAP = {
            'warrior': 'warrior_sprite.png',
            'rogue': 'rogue_sprite.png', 
            'mage': 'mage_sprite.png',
            'boss_divineheart': 'boss_divineheart_sprite.png',
            'cave_guardian': 'cave_guardian_sprite.png',
            'ground_creature': 'ground creature_sprite.png',
            'primitive_creature': 'primitive_creature_sprite.png'
        }
        
        # Scene to Background Mapping
        self.SCENE_BACKGROUND_MAP = {
            'cave_entrance': 'cave entrance.png',
            'skull_chamber': 'skull_chamber.png',
            'primitive_village': 'primitive_village.png',
            'alley': 'primitive_village.png',  # Uses village background
            'armory': 'primitive_village.png',  # Uses village background  
            'chief_house': 'chiefs house.png',
            'healing_pool': 'healing pool.png',
            'village_changed': 'primitive viillage (cosmic).png',
            'treasure_room': 'treasure_room.png',
            'final_chamber': 'final_chamber.png'
        }
        
        # Enemy sprites for combat encounters
        self.SCENE_ENEMIES = {
            'alley': 'ground_creature',
            'chief_house': 'cave_guardian',
            'village_changed': 'boss_divineheart'
        }
        
        # Load game modules with error handling
        self.load_game_modules()
        
        # Create UI
        self.create_ui()
        self.load_assets()
        self.show_title_screen()

    def load_game_modules(self):
        """Load game modules with proper error handling"""
        try:
            # Try to import from src structure
            from config.config import SCENE_NAMES, MESSAGES
            self.SCENE_NAMES = SCENE_NAMES
            self.MESSAGES = getattr(sys.modules.get('config.config'), 'MESSAGES', {})
            print("✅ Loaded config module")
        except ImportError as e:
            print(f"⚠️  Could not load config: {e}")
            # Fallback scene names
            self.SCENE_NAMES = {
                'CAVE_ENTRANCE': 'Cave Entrance',
                'SKULL_CHAMBER': 'Skull Chamber',
                'PRIMITIVE_VILLAGE': 'Primitive Village',
                'ALLEY': 'Alley',
                'ARMORY': 'Armory',
                'CHIEF_HOUSE': 'Chief House',
                'HEALING_POOL': 'Healing Pool',
                'VILLAGE_CHANGED': 'Village Changed'
            }
            self.MESSAGES = {'THANKS_PLAYING': 'Thanks for playing!'}

    def create_ui(self):
        """Create the main game interface"""
        # Main game canvas
        self.canvas = tk.Canvas(
            self.root, 
            width=900, 
            height=500, 
            bg='#1a1a2e', 
            highlightthickness=0
        )
        self.canvas.pack(pady=10)
        
        # Dialogue box frame
        dialogue_frame = tk.Frame(self.root, bg='#2a2a3e', relief='raised', bd=2)
        dialogue_frame.pack(fill='x', padx=20, pady=5)
        
        # Dialogue text area
        self.dialogue_text = tk.Text(
            dialogue_frame,
            height=6,
            width=100,
            wrap='word',
            bg='#1a1a2e',
            fg='#ffffff',
            font=('Courier', 12),
            state='disabled',
            relief='flat'
        )
        self.dialogue_text.pack(padx=10, pady=10)
        
        # Options frame
        options_frame = tk.Frame(self.root, bg='#0a0a0a')
        options_frame.pack(fill='x', padx=20, pady=5)
        
        # Options listbox
        self.options_listbox = tk.Listbox(
            options_frame,
            height=4,
            bg='#2a2a3e',
            fg='#ffffff',
            selectbackground='#4a4a6e',
            font=('Arial', 11),
            relief='flat'
        )
        self.options_listbox.pack(fill='x', padx=10, pady=5)
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg='#0a0a0a')
        button_frame.pack(fill='x', padx=20, pady=5)
        
        self.select_button = tk.Button(
            button_frame,
            text="Select Choice",
            command=self.handle_choice,
            bg='#4a6741',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            padx=20
        )
        self.select_button.pack(side='left', padx=10)
        
        self.quit_button = tk.Button(
            button_frame,
            text="Quit Game",
            command=self.quit_game,
            bg='#674141',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            padx=20
        )
        self.quit_button.pack(side='right', padx=10)
        
        # Bind keyboard events
        self.root.bind('<Return>', lambda e: self.handle_choice())
        self.root.bind('<Up>', self.move_selection_up)
        self.root.bind('<Down>', self.move_selection_down)
        self.root.focus_set()

    def load_assets(self):
        """Load game assets with error handling"""
        print("Loading assets...")
        
        # Load backgrounds
        if os.path.exists(self.backgrounds_dir):
            for bg_file in os.listdir(self.backgrounds_dir):
                if bg_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img_path = os.path.join(self.backgrounds_dir, bg_file)
                        img = Image.open(img_path)
                        img = img.resize((900, 500), Image.Resampling.LANCZOS)
                        self.background_cache[bg_file] = ImageTk.PhotoImage(img)
                    except Exception as e:
                        print(f"Failed to load background {bg_file}: {e}")
        
        # Load sprites
        if os.path.exists(self.sprites_dir):
            for sprite_file in os.listdir(self.sprites_dir):
                if sprite_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img_path = os.path.join(self.sprites_dir, sprite_file)
                        img = Image.open(img_path)
                        # Different sizes for different sprite types
                        if 'boss' in sprite_file.lower():
                            img = img.resize((150, 150), Image.Resampling.LANCZOS)
                        else:
                            img = img.resize((100, 100), Image.Resampling.LANCZOS)
                        self.sprite_cache[sprite_file] = ImageTk.PhotoImage(img)
                    except Exception as e:
                        print(f"Failed to load sprite {sprite_file}: {e}")
        
        print(f"Loaded {len(self.background_cache)} backgrounds and {len(self.sprite_cache)} sprites")

    def show_title_screen(self):
        """Display the game title screen"""
        self.canvas.delete("all")
        
        # Title background
        self.canvas.create_rectangle(0, 0, 900, 500, fill='#0a0a1a')
        
        # Title text
        self.canvas.create_text(
            450, 150,
            text="🏴‍☠️ SHABUYA",
            fill='#FFD700',  # Gold color in hex
            font=('Arial', 48, 'bold')
        )
        
        self.canvas.create_text(
            450, 200,
            text="Cave Adventure",
            fill='#C0C0C0',  # Silver color in hex
            font=('Arial', 24)
        )
        
        # Set initial dialogue and options
        self.set_dialogue("Welcome to the Cave Adventure! Choose your character class to begin your journey.")
        self.set_options([
            "Warrior - Strong and resilient",
            "Rogue - Fast and stealthy", 
            "Mage - Intelligent and magical"
        ])

    def set_dialogue(self, text):
        """Update the dialogue box with new text"""
        self.dialogue_text.config(state='normal')
        self.dialogue_text.delete(1.0, tk.END)
        self.dialogue_text.insert(tk.END, text)
        self.dialogue_text.config(state='disabled')

    def set_options(self, options):
        """Update the options list"""
        self.current_options = options
        self.options_listbox.delete(0, tk.END)
        for i, option in enumerate(options):
            self.options_listbox.insert(tk.END, f"{i+1}. {option}")
        
        if options:
            self.options_listbox.selection_set(0)
            self.selected_option = 0

    def move_selection_up(self, event):
        """Move selection up in options"""
        if self.current_options and self.selected_option > 0:
            self.selected_option -= 1
            self.options_listbox.selection_clear(0, tk.END)
            self.options_listbox.selection_set(self.selected_option)

    def move_selection_down(self, event):
        """Move selection down in options"""
        if self.current_options and self.selected_option < len(self.current_options) - 1:
            self.selected_option += 1
            self.options_listbox.selection_clear(0, tk.END)
            self.options_listbox.selection_set(self.selected_option)

    def handle_choice(self):
        """Handle player choice selection"""
        if not self.current_options:
            return
            
        selection = self.options_listbox.curselection()
        if selection:
            choice_index = selection[0]
            self.selected_option = choice_index
            
            if self.player is None:
                # Character selection
                self.create_character(choice_index)
            else:
                # Game choice
                self.process_game_choice(choice_index)

    def create_character(self, class_index):
        """Create player character based on selection"""
        try:
            # Try to import game modules
            from game_logic.player import Player
            from game_logic.item import Inventory
            
            # Create a basic player object
            class BasicPlayer:
                def __init__(self):
                    self.health = 100
                    self.vitality = 5
                    self.strength = 5
                    self.intelligence = 5
                    self.agility = 5
                    self.level = 1
                    self.inventory = None
                    self.weapon = None
                    self.character_type = None
            
            # Create player
            self.player = BasicPlayer()
            
            class_types = ['warrior', 'rogue', 'mage']
            self.player.character_type = class_types[class_index]
            
            # Initialize basic scenes
            self.initialize_basic_scenes()
            
            # Start the game
            self.start_game()
            
        except ImportError as e:
            print(f"Could not load game modules: {e}")
            # Create a minimal game experience
            self.create_minimal_game(class_index)

    def initialize_basic_scenes(self):
        """Initialize basic scene structure"""
        class BasicScene:
            def __init__(self, name, description):
                self.name = name
                self.description = description
        
        self.scenes = {
            self.SCENE_NAMES['CAVE_ENTRANCE']: BasicScene('Cave Entrance', 'Cave entrance'),
            self.SCENE_NAMES['SKULL_CHAMBER']: BasicScene('Skull Chamber', 'Skull chamber'),
            self.SCENE_NAMES['PRIMITIVE_VILLAGE']: BasicScene('Primitive Village', 'Village'),
            self.SCENE_NAMES['ALLEY']: BasicScene('Alley', 'Alley'),
            self.SCENE_NAMES['ARMORY']: BasicScene('Armory', 'Armory'),
            self.SCENE_NAMES['CHIEF_HOUSE']: BasicScene('Chief House', 'Chief house'),
            self.SCENE_NAMES['HEALING_POOL']: BasicScene('Healing Pool', 'Healing pool'),
            self.SCENE_NAMES['VILLAGE_CHANGED']: BasicScene('Village Changed', 'Changed village')
        }
        self.current_scene = self.scenes[self.SCENE_NAMES['CAVE_ENTRANCE']]

    def create_minimal_game(self, class_index):
        """Create a minimal game experience when modules can't be loaded"""
        class MinimalPlayer:
            def __init__(self, character_type):
                self.character_type = character_type
                self.health = 100
        
        class_types = ['warrior', 'rogue', 'mage']
        self.player = MinimalPlayer(class_types[class_index])
        self.initialize_basic_scenes()
        self.start_game()

    def start_game(self):
        """Start the main game"""
        self.update_scene_display()
        self.handle_current_scene()

    def update_scene_display(self):
        """Update the visual display based on current scene"""
        if not self.current_scene:
            return
            
        self.canvas.delete("all")
        
        # Get scene background
        scene_name = self.current_scene.name.lower().replace(' ', '_')
        bg_file = self.SCENE_BACKGROUND_MAP.get(scene_name)
        
        if bg_file and bg_file in self.background_cache:
            # Draw background
            bg_image = self.background_cache[bg_file]
            self.canvas.create_image(450, 250, image=bg_image)
        else:
            # Default background
            self.canvas.create_rectangle(0, 0, 900, 500, fill='#1a1a2e')
            self.canvas.create_text(
                450, 250,
                text=f"{self.current_scene.name.upper()}",
                fill='#4a4a6a',
                font=('Arial', 32)
            )
        
        # Draw player sprite
        if self.player and hasattr(self.player, 'character_type'):
            sprite_file = self.CHARACTER_SPRITE_MAP.get(self.player.character_type)
            if sprite_file and sprite_file in self.sprite_cache:
                player_sprite = self.sprite_cache[sprite_file]
                
                # Position player sprite
                if scene_name in self.SCENE_ENEMIES:
                    # Combat positioning - player on left
                    self.canvas.create_image(200, 350, image=player_sprite)
                    
                    # Draw enemy sprite
                    enemy_type = self.SCENE_ENEMIES[scene_name]
                    enemy_sprite_file = self.CHARACTER_SPRITE_MAP.get(enemy_type)
                    if enemy_sprite_file and enemy_sprite_file in self.sprite_cache:
                        enemy_sprite = self.sprite_cache[enemy_sprite_file]
                        self.canvas.create_image(700, 350, image=enemy_sprite)
                else:
                    # Exploration positioning - center
                    self.canvas.create_image(450, 350, image=player_sprite)

    def handle_current_scene(self):
        """Handle the current scene logic"""
        if not self.current_scene:
            return
            
        scene_name = self.current_scene.name.lower().replace(' ', '_')
        
        # Route to appropriate scene handler
        if scene_name == 'cave_entrance':
            self.handle_cave_entrance()
        elif scene_name == 'skull_chamber':
            self.handle_skull_chamber()
        elif scene_name == 'primitive_village':
            self.handle_village()
        elif scene_name == 'alley':
            self.handle_alley()
        elif scene_name == 'armory':
            self.handle_armory()
        elif scene_name == 'chief_house':
            self.handle_chief_house()
        elif scene_name == 'healing_pool':
            self.handle_healing_pool()
        elif scene_name == 'village_changed':
            self.handle_final_boss()
        else:
            self.handle_generic_scene()

    def handle_cave_entrance(self):
        """Handle Cave Entrance scene"""
        if 'cave_entrance' not in self.game_state['visited_scenes']:
            dialogue = ("You stand at the entrance to a mysterious cave. Ancient symbols are carved into the stone archway, "
                       "and a cool breeze carries strange whispers from within. A narrow crack in the wall seems to lead deeper, "
                       "while loose stones suggest the possibility of a cave-in.")
            self.game_state['visited_scenes'].add('cave_entrance')
        else:
            dialogue = "You return to the cave entrance. The mysterious symbols seem to glow faintly in the dim light."
            
        self.set_dialogue(dialogue)
        self.set_options([
            "Go through the crack",
            "Look around more carefully", 
            "Sit and rest",
            "Leave the cave"
        ])

    def handle_skull_chamber(self):
        """Handle Skull Chamber scene"""
        dialogue = ("You emerge into a vast chamber decorated with countless skulls. The air is thick with ancient magic, "
                   "and strange runes pulse with otherworldly light. Suddenly, rocks crash down behind you - there's no going back!")
        
        self.set_dialogue(dialogue)
        self.set_options([
            "Move forward into the village",
            "Examine the skulls and runes"
        ])

    def handle_village(self):
        """Handle Primitive Village scene"""
        if not self.game_state['visited_village']:
            dialogue = ("You enter a primitive village with crude huts made of bone and hide. A central fire pit glows with "
                       "ember light, and strange symbols cover the rocky walls. The air buzzes with the chatter of unseen creatures.")
            self.game_state['visited_village'] = True
        else:
            dialogue = "You return to the primitive village. The fire still burns, and shadows move between the huts."
            
        self.set_dialogue(dialogue)
        self.set_options([
            "Enter the dangerous Alley",
            "Approach the locked Armory",
            "Visit the Chief's House", 
            "Stay by the fire pit",
            "Rest and recover"
        ])

    def handle_alley(self):
        """Handle Alley combat scene"""
        if self.game_state['alley_creature_dead']:
            dialogue = "You return to the alley where you defeated the ground creature. Its lifeless body serves as a grim reminder of the dangers here."
            options = [
                "Search the area again",
                "Return to the village",
                "Continue deeper"
            ]
        else:
            dialogue = ("You step into a narrow alley between the huts. Suddenly, a primitive ground-dwelling creature "
                       "bursts from a hidden burrow, its eyes glowing with primal fury!")
            options = [
                "Attack the creature",
                "Try to escape back to village",
                "Attempt to communicate"
            ]
            
        self.set_dialogue(dialogue)
        self.set_options(options)

    def handle_armory(self):
        """Handle Armory scene"""
        dialogue = ("You enter the ancient armory. Three enhanced weapons rest on glowing pedestals: "
                   "the Shadow Blade, the Bone Crusher, and the Skull Scepter. A key labeled 'Town Key' sits on a table.")
        
        self.set_dialogue(dialogue)
        self.set_options([
            "Take the Shadow Blade (Enhanced Dagger)",
            "Take the Bone Crusher (Enhanced Axe)",
            "Take the Skull Scepter (Enhanced Wand)",
            "Take the Town Key",
            "Leave the armory"
        ])

    def handle_chief_house(self):
        """Handle Chief House scene"""
        dialogue = ("You approach the Chief's imposing house, adorned with trophies and mystical symbols. "
                   "The air hums with power, and you sense you're being watched by ancient eyes.")
        
        self.set_dialogue(dialogue)
        self.set_options([
            "Enter and face the Chief",
            "Examine the trophies",
            "Look for another entrance",
            "Return to the village"
        ])

    def handle_healing_pool(self):
        """Handle Healing Pool scene"""
        dialogue = ("You discover a sacred chamber with mystical healing waters that glow with ethereal light. "
                   "The pool seems to pulse with ancient magic, offering restoration but demanding respect.")
        
        self.set_dialogue(dialogue)
        self.set_options([
            "Enter the sacred waters (WARNING: Permanent change)",
            "Study the magical runes around the pool",
            "Return to the Chief's house",
            "Meditate by the water's edge"
        ])

    def handle_final_boss(self):
        """Handle final boss scene"""
        dialogue = ("The village has transformed! Cosmic energy swirls around you as the Divine Heart Boss materializes, "
                   "its form shifting between dimensions. This is your final test!")
        
        self.set_dialogue(dialogue)
        self.set_options([
            "Engage in final battle",
            "Try to find weakness",
            "Attempt negotiation",
            "Use special ability"
        ])

    def handle_generic_scene(self):
        """Handle unknown/generic scenes"""
        scene_name = self.current_scene.name if self.current_scene else "Unknown Location"
        dialogue = f"You find yourself in {scene_name}. The path forward is unclear."
        self.set_dialogue(dialogue)
        self.set_options([
            "Look around carefully",
            "Move forward",
            "Go back",
            "Rest here"
        ])

    def process_game_choice(self, choice_index):
        """Process the player's choice in the current scene"""
        if not self.current_scene:
            return
            
        scene_name = self.current_scene.name.lower().replace(' ', '_')
        
        try:
            if scene_name == 'cave_entrance':
                if choice_index == 0:  # Go through crack
                    self.current_scene = self.scenes[self.SCENE_NAMES['SKULL_CHAMBER']]
                elif choice_index == 1:  # Look around
                    self.set_dialogue("You examine the cave entrance more carefully and notice hidden passages...")
                    return
                elif choice_index == 3:  # Leave
                    self.quit_game()
                    return
                    
            elif scene_name == 'skull_chamber':
                if choice_index == 0:  # Move forward
                    self.current_scene = self.scenes[self.SCENE_NAMES['PRIMITIVE_VILLAGE']]
                    
            elif scene_name == 'primitive_village':
                if choice_index == 0:  # Alley
                    self.current_scene = self.scenes[self.SCENE_NAMES['ALLEY']]
                elif choice_index == 1:  # Armory
                    self.current_scene = self.scenes[self.SCENE_NAMES['ARMORY']]
                elif choice_index == 2:  # Chief House
                    self.current_scene = self.scenes[self.SCENE_NAMES['CHIEF_HOUSE']]
                elif choice_index == 3:  # Stay by fire
                    self.set_dialogue("You sit by the warm fire and rest. Your health is restored.")
                    return
                    
            elif scene_name == 'alley':
                if choice_index == 0:  # Attack
                    self.handle_combat()
                    return
                elif choice_index == 1:  # Escape
                    self.current_scene = self.scenes[self.SCENE_NAMES['PRIMITIVE_VILLAGE']]
                    
            elif scene_name == 'armory':
                if choice_index == 4:  # Leave
                    self.current_scene = self.scenes[self.SCENE_NAMES['PRIMITIVE_VILLAGE']]
                else:
                    self.set_dialogue("You acquired a powerful weapon! Your combat effectiveness has increased.")
                    return
                    
            elif scene_name == 'chief_house':
                if choice_index == 0:  # Enter
                    self.current_scene = self.scenes[self.SCENE_NAMES['HEALING_POOL']]
                elif choice_index == 3:  # Return
                    self.current_scene = self.scenes[self.SCENE_NAMES['PRIMITIVE_VILLAGE']]
                    
            elif scene_name == 'healing_pool':
                if choice_index == 0:  # Enter waters
                    self.current_scene = self.scenes[self.SCENE_NAMES['VILLAGE_CHANGED']]
                elif choice_index == 2:  # Return
                    self.current_scene = self.scenes[self.SCENE_NAMES['CHIEF_HOUSE']]
                    
            elif scene_name == 'village_changed':
                if choice_index == 0:  # Final battle
                    self.handle_final_combat()
                    return
            
            # Update display after scene change
            self.update_scene_display()
            self.handle_current_scene()
            
        except Exception as e:
            self.set_dialogue(f"Error processing choice: {e}")

    def handle_combat(self):
        """Handle combat sequence"""
        self.set_dialogue("You engage the creature in combat! Your weapon strikes true, and after a fierce battle, you emerge victorious!")
        self.game_state['alley_creature_dead'] = True
        
        # Update to show combat aftermath
        self.root.after(3000, lambda: self.handle_alley())

    def handle_final_combat(self):
        """Handle final boss combat"""
        self.set_dialogue("An epic battle ensues! With all your gathered power and wisdom, you face the Divine Heart Boss. After a tremendous struggle, you achieve victory and save the realm!")
        
        self.set_options([
            "Start New Game",
            "Exit Game"
        ])

    def quit_game(self):
        """Quit the game"""
        if messagebox.askquestion("Quit Game", "Are you sure you want to quit?") == 'yes':
            self.root.destroy()

    def run(self):
        """Start the game GUI"""
        if hasattr(self, 'root'):
            print("🎮 SHABUYA Cave Adventure GUI Ready!")
            print("Use arrow keys to navigate options, Enter to select")
            self.root.mainloop()
        else:
            print("GUI could not be initialized - running in text mode would be required")


if __name__ == "__main__":
    try:
        game = PlayerGameGUI()
        game.run()
    except Exception as e:
        print(f"Error starting game: {e}")
        import traceback
        traceback.print_exc()

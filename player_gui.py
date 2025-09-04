#!/usr/bin/env python3
"""
PLAYER GUI - Linear Gameplay Experience
=====================================
A player-focused GUI that provides linear, progressive gameplay
instead of the development sandbox.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import os
from PIL import Image, ImageTk
import random
import json

class PlayerGameGUI:
    def __init__(self):
        print("Initializing Player Game GUI...")
        
        self.root = tk.Tk()
        self.root.title("SHABUYA Cave Adventure - Player Mode")
        self.root.geometry("1200x800")
        self.root.configure(bg='#0a0a0a')
        
        # Asset paths
        self.sprites_dir = "assets/sprites"
        self.backgrounds_dir = "assets/backgrounds"
        
        # Game state
        self.player_character = None  # Will be set after class selection
        self.current_scene = "cave_entrance"
        self.game_state = "exploring"
        self.player_health = 100
        self.player_level = 1
        self.player_experience = 0
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_accessories = []
        self.visited_scenes = []
        self.game_progress = {
            'visited_village': False,
            'defeated_guardian': False,
            'found_treasure': False,
            'met_chief': False,
            'looked_around_dark': False,
            'sat_and_cried': False,
            'entered_skull_chamber': False,
            'gained_villagers_trust': False,
            'learned_ancient_secrets': False,
            'entered_cautiously': False,
            'confronted_darkness': False,
            'learned_village_history': False,
            'found_artifacts': False,
            'helped_villagers': False,
            'offered_services': False,
            'gained_magical_insight': False,
            'understood_pool_magic': False,
            'restored_health': False,
            'learned_village_customs': False,
            'protected_villagers': False,
            'gained_spiritual_insight': False,
            'found_corruption_source': False,
            'explored_alley': False,
            'found_alley_treasure': False,
            'investigated_alley_sounds': False,
            'examined_armory': False,
            'requested_custom_equipment': False,
            'learned_weapon_maintenance': False
        }
        
        # Asset caches
        self.sprite_cache = {}
        self.background_cache = {}
        
        # Scene progression
        self.scene_progression = [
            "cave_entrance",
            "skull_chamber", 
            "primitive_village",
            "chiefs_house",
            "healing_pool",
            "village_changed",
            "alley",
            "armory"
        ]
        
        # Class definitions
        self.classes = {
            'warrior': {
                'name': 'Warrior',
                'health': 120,
                'strength': 15,
                'agility': 8,
                'intelligence': 5,
                'starting_weapon': 'Iron Sword',
                'ability': 'Shield Block',
                'description': 'A mighty warrior with high health and strength. Perfect for beginners.'
            },
            'rogue': {
                'name': 'Rogue',
                'health': 80,
                'strength': 8,
                'agility': 15,
                'intelligence': 8,
                'starting_weapon': 'Daggers',
                'ability': 'Stealth',
                'description': 'A swift rogue with high agility and critical hit chance.'
            },
            'mage': {
                'name': 'Mage',
                'health': 70,
                'strength': 5,
                'agility': 6,
                'intelligence': 18,
                'starting_weapon': 'Magic Staff',
                'ability': 'Fireball',
                'description': 'A powerful mage with high intelligence and magical abilities.'
            }
        }
        
        # Weapons
        self.weapons = {
            'Iron Sword': {'damage': 12, 'type': 'melee', 'class': 'warrior'},
            'Daggers': {'damage': 8, 'type': 'melee', 'class': 'rogue'},
            'Magic Staff': {'damage': 10, 'type': 'magic', 'class': 'mage'},
            'Battle Axe': {'damage': 15, 'type': 'melee', 'class': 'warrior'},
            'Poison Dagger': {'damage': 6, 'type': 'melee', 'class': 'rogue'},
            'Lightning Bolt': {'damage': 14, 'type': 'magic', 'class': 'mage'},
            'Ancient Blade': {'damage': 18, 'type': 'melee', 'class': 'warrior'},
            'Shadow Dagger': {'damage': 12, 'type': 'melee', 'class': 'rogue'},
            'Crystal Staff': {'damage': 16, 'type': 'magic', 'class': 'mage'},
            'Steel Greatsword': {'damage': 20, 'type': 'melee', 'class': 'warrior'},
            'Venomous Blade': {'damage': 10, 'type': 'melee', 'class': 'rogue'},
            'Arcane Orb': {'damage': 18, 'type': 'magic', 'class': 'mage'},
            'Thunder Hammer': {'damage': 22, 'type': 'melee', 'class': 'warrior'},
            'Silent Death': {'damage': 14, 'type': 'melee', 'class': 'rogue'},
            'Ethereal Wand': {'damage': 20, 'type': 'magic', 'class': 'mage'}
        }
        
        # Items and equipment
        self.items = {
            'Health Potion': {'type': 'consumable', 'effect': 'heal', 'value': 30, 'description': 'Restores 30 health points'},
            'Mana Potion': {'type': 'consumable', 'effect': 'mana', 'value': 25, 'description': 'Restores 25 mana points'},
            'Leather Armor': {'type': 'armor', 'effect': 'defense', 'value': 5, 'description': 'Light armor providing basic protection'},
            'Chain Mail': {'type': 'armor', 'effect': 'defense', 'value': 10, 'description': 'Medium armor with good protection'},
            'Plate Armor': {'type': 'armor', 'effect': 'defense', 'value': 15, 'description': 'Heavy armor with maximum protection'},
            'Ring of Strength': {'type': 'accessory', 'effect': 'strength', 'value': 3, 'description': 'Increases strength by 3'},
            'Ring of Agility': {'type': 'accessory', 'effect': 'agility', 'value': 3, 'description': 'Increases agility by 3'},
            'Ring of Intelligence': {'type': 'accessory', 'effect': 'intelligence', 'value': 3, 'description': 'Increases intelligence by 3'},
            'Amulet of Health': {'type': 'accessory', 'effect': 'health', 'value': 20, 'description': 'Increases maximum health by 20'},
            'Boots of Speed': {'type': 'accessory', 'effect': 'agility', 'value': 2, 'description': 'Increases agility by 2'},
            'Crystal of Power': {'type': 'accessory', 'effect': 'intelligence', 'value': 2, 'description': 'Increases intelligence by 2'}
        }
        
        # Enhanced scene choices
        self.scene_choices = {
            "cave_entrance": [
                {
                    "text": "Look around",
                    "description": "You squint into the darkness, but your eyes haven't adjusted yet. You can barely make out the rough stone walls around you.",
                    "consequence": "looked_around_dark"
                },
                {
                    "text": "Sit and cry",
                    "description": "You sink to the ground and let out your frustration. The tears don't help your situation, but at least you feel a bit better.",
                    "consequence": "sat_and_cried"
                },
                {
                    "text": "Go towards the light at the crack",
                    "description": "You notice a faint light coming from a narrow crack in the wall. Squeezing through, you find yourself in a chamber filled with ancient skulls.",
                    "consequence": "entered_skull_chamber"
                }
            ],
            "skull_chamber": [
                {
                    "text": "Look for an exit",
                    "description": "You search the chamber walls for any way out.",
                    "consequence": "no_exit_visible"
                },
                {
                    "text": "Examine the large glowing skull",
                    "description": "You approach the mysterious glowing skull in the center of the chamber.",
                    "consequence": "tunnel_collapse"
                }
            ],
            "primitive_village": [
                {
                    "text": "Approach the villagers openly",
                    "description": "You walk into the village with open hands, showing peaceful intent.",
                    "consequence": "gained_villagers_trust"
                },
                {
                    "text": "Observe from the shadows",
                    "description": "You watch the village from a hidden position to understand their ways.",
                    "consequence": "learned_village_customs"
                },
                {
                    "text": "Seek out the chief",
                    "description": "You decide to find and speak with the village chief.",
                    "consequence": "advanced_to_chiefs_house"
                }
            ],
            "chiefs_house": [
                {
                    "text": "Show respect and ask for guidance",
                    "description": "You approach the chief with proper respect and seek wisdom.",
                    "consequence": "met_chief"
                },
                {
                    "text": "Offer your services",
                    "description": "You propose to help the village with your unique abilities.",
                    "consequence": "offered_services"
                },
                {
                    "text": "Ask about the healing pool",
                    "description": "You inquire about the mystical healing pool the chief mentioned.",
                    "consequence": "advanced_to_healing_pool"
                }
            ],
            "healing_pool": [
                {
                    "text": "Drink from the healing waters",
                    "description": "You carefully drink from the mystical pool to restore your health.",
                    "consequence": "restored_health"
                },
                {
                    "text": "Meditate by the pool",
                    "description": "You sit quietly and absorb the magical energy of the healing pool.",
                    "consequence": "gained_magical_insight"
                },
                {
                    "text": "Return to the village",
                    "description": "You decide to head back to the village to see what has changed.",
                    "consequence": "advanced_to_village_changed"
                }
            ],
            "village_changed": [
                {
                    "text": "Confront the dark presence",
                    "description": "You face the corruption head-on with your abilities.",
                    "consequence": "confronted_darkness"
                },
                {
                    "text": "Help the remaining villagers",
                    "description": "You focus on protecting and aiding the innocent villagers.",
                    "consequence": "protected_villagers"
                },
                {
                    "text": "Seek the source of corruption",
                    "description": "You investigate to find the root cause of the village's transformation.",
                    "consequence": "found_corruption_source"
                }
            ],
            "alley": [
                {
                    "text": "Explore the dark alley",
                    "description": "You carefully navigate through the shadowy passage.",
                    "consequence": "explored_alley"
                },
                {
                    "text": "Search for valuables",
                    "description": "You look for anything of value in the alley.",
                    "consequence": "found_alley_treasure"
                },
                {
                    "text": "Investigate strange sounds",
                    "description": "You follow mysterious noises coming from deeper in the alley.",
                    "consequence": "investigated_alley_sounds"
                }
            ],
            "armory": [
                {
                    "text": "Examine the weapons",
                    "description": "You study the various weapons and armor on display.",
                    "consequence": "examined_armory"
                },
                {
                    "text": "Ask about custom equipment",
                    "description": "You inquire about having special equipment made.",
                    "consequence": "requested_custom_equipment"
                },
                {
                    "text": "Learn about weapon maintenance",
                    "description": "You ask about proper care and maintenance of weapons.",
                    "consequence": "learned_weapon_maintenance"
                }
            ],
            "cave_in": [
                {
                    "text": "RUN",
                    "description": "You desperately try to escape the collapsing tunnel.",
                    "consequence": "escaped_cave_in"
                }
            ]
        }
        
        # Initialize
        self.load_assets()
        self.show_class_selection()
        
    def show_class_selection(self):
        """Show the class selection screen"""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main container
        main_frame = tk.Frame(self.root, bg='#0a0a0a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="SHABUYA CAVE ADVENTURE", 
                         font=('Arial', 24, 'bold'), fg='#00ff88', bg='#0a0a0a')
        title.pack(pady=20)
        
        subtitle = tk.Label(main_frame, text="Choose Your Class", 
                           font=('Arial', 16), fg='#cccccc', bg='#0a0a0a')
        subtitle.pack(pady=10)
        
        # Class selection frame
        class_frame = tk.Frame(main_frame, bg='#0a0a0a')
        class_frame.pack(pady=30)
        
        # Create class buttons
        for i, (class_key, class_data) in enumerate(self.classes.items()):
            class_btn_frame = tk.LabelFrame(class_frame, text=class_data['name'], 
                                           fg='#ffcc88', bg='#1a1a1a', font=('Arial', 12, 'bold'))
            class_btn_frame.pack(side=tk.LEFT, padx=10, pady=10)
            
            # Class description
            desc = tk.Label(class_btn_frame, text=class_data['description'], 
                           fg='#cccccc', bg='#1a1a1a', font=('Arial', 10), 
                           wraplength=200, justify=tk.LEFT)
            desc.pack(padx=15, pady=10)
            
            # Stats
            stats_text = f"Health: {class_data['health']}\n"
            stats_text += f"Strength: {class_data['strength']}\n"
            stats_text += f"Agility: {class_data['agility']}\n"
            stats_text += f"Intelligence: {class_data['intelligence']}\n"
            stats_text += f"Weapon: {class_data['starting_weapon']}\n"
            stats_text += f"Ability: {class_data['ability']}"
            
            stats = tk.Label(class_btn_frame, text=stats_text, 
                            fg='#88ccff', bg='#1a1a1a', font=('Arial', 9), 
                            justify=tk.LEFT)
            stats.pack(padx=15, pady=10)
            
            # Select button
            select_btn = tk.Button(class_btn_frame, text=f"Choose {class_data['name']}", 
                                  command=lambda c=class_key: self.select_class(c),
                                  bg='#44ff44', fg='black', font=('Arial', 11, 'bold'),
                                  width=15, height=2)
            select_btn.pack(pady=15)
        
    def select_class(self, class_key):
        """Select a character class and start the game"""
        self.player_character = class_key
        class_data = self.classes[class_key]
        
        # Set initial stats
        self.player_health = class_data['health']
        self.player_strength = class_data['strength']
        self.player_agility = class_data['agility']
        self.player_intelligence = class_data['intelligence']
        self.player_weapon = class_data['starting_weapon']
        self.player_ability = class_data['ability']
        
        # Add starting weapon to inventory and equip it
        self.inventory.append(self.player_weapon)
        self.equipped_weapon = self.player_weapon
        
        # Add some starting items
        self.inventory.extend(['Health Potion', 'Leather Armor'])
        
        # Start the game
        self.create_ui()
        self.start_new_game()
        
    def create_ui(self):
        """Create the player-focused user interface"""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main container
        main_container = tk.Frame(self.root, bg='#0a0a0a')
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Game canvas
        canvas_frame = tk.Frame(main_container, bg='#1a1a1a', relief=tk.RAISED, bd=2)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        canvas_title = tk.Label(canvas_frame, text="SHABUYA CAVE ADVENTURE", 
                               font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1a1a1a')
        canvas_title.pack(pady=10)
        
        self.canvas = tk.Canvas(canvas_frame, width=900, height=500, bg='black')
        self.canvas.pack(padx=10, pady=(0, 10))
        
        # Story text footer
        story_frame = tk.LabelFrame(canvas_frame, text="Story & Choices", 
                                   fg='#cccccc', bg='#1a1a1a', font=('Arial', 11, 'bold'))
        story_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        self.story_text = tk.Text(story_frame, height=8, bg='#0a0a0a', fg='#cccccc',
                                 font=('Arial', 10), wrap=tk.WORD, relief=tk.FLAT)
        self.story_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        
        # Choice input
        choice_frame = tk.Frame(canvas_frame, bg='#1a1a1a')
        choice_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        choice_label = tk.Label(choice_frame, text="Enter choice (1-3):", 
                               fg='#88ccff', bg='#1a1a1a', font=('Arial', 10))
        choice_label.pack(side=tk.LEFT)
        
        self.choice_entry = tk.Entry(choice_frame, width=5, bg='#0a0a0a', fg='#cccccc',
                                     font=('Arial', 10))
        self.choice_entry.pack(side=tk.RIGHT, padx=(5, 0))
        self.choice_entry.bind('<Return>', self.handle_choice_input)
        
        # Control panel
        control_frame = tk.Frame(main_container, bg='#2a2a2a', width=280)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y)
        control_frame.pack_propagate(False)
        
        control_title = tk.Label(control_frame, text="GAME CONTROLS", 
                                font=('Arial', 14, 'bold'), fg='#ffffff', bg='#2a2a2a')
        control_title.pack(pady=15)
        
        # Action buttons
        action_frame = tk.LabelFrame(control_frame, text="Actions", 
                                    fg='#88ccff', bg='#2a2a2a', font=('Arial', 11, 'bold'))
        action_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.inventory_btn = tk.Button(action_frame, text="Inventory/Stats", 
                                     command=self.show_inventory_stats,
                                     bg='#cc8844', fg='white', font=('Arial', 10, 'bold'))
        self.inventory_btn.pack(fill=tk.X, padx=8, pady=4)
        
        # Character info
        char_frame = tk.LabelFrame(control_frame, text="Character", 
                                  fg='#ffcc88', bg='#2a2a2a', font=('Arial', 11, 'bold'))
        char_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.health_label = tk.Label(char_frame, text="Health: 100", 
                                    fg='#ff4444', bg='#2a2a2a', font=('Arial', 10))
        self.health_label.pack(pady=2)
        
        self.level_label = tk.Label(char_frame, text="Level: 1", 
                                   fg='#44ff44', bg='#2a2a2a', font=('Arial', 10))
        self.level_label.pack(pady=2)
        
        self.exp_label = tk.Label(char_frame, text="Experience: 0", 
                                 fg='#4444ff', bg='#2a2a2a', font=('Arial', 10))
        self.exp_label.pack(pady=2)
        
        self.weapon_label = tk.Label(char_frame, text="Weapon: Iron Sword", 
                                    fg='#ff8844', bg='#2a2a2a', font=('Arial', 10))
        self.weapon_label.pack(pady=2)
        
        # Game info
        info_frame = tk.LabelFrame(control_frame, text="Game Info", 
                                  fg='#cccccc', bg='#2a2a2a', font=('Arial', 11, 'bold'))
        info_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.scene_label = tk.Label(info_frame, text="Scene: Cave Entrance", 
                                   fg='#88ccff', bg='#2a2a2a', font=('Arial', 10))
        self.scene_label.pack(pady=2)
        
        self.state_label = tk.Label(info_frame, text="State: Exploring", 
                                   fg='#ff8888', bg='#2a2a2a', font=('Arial', 10))
        self.state_label.pack(pady=2)
        
        # Menu buttons
        menu_frame = tk.Frame(control_frame, bg='#2a2a2a')
        menu_frame.pack(fill=tk.X, padx=15, pady=10)
        
        save_btn = tk.Button(menu_frame, text="Save Game", 
                            command=self.save_game,
                            bg='#44aa44', fg='white', font=('Arial', 9))
        save_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))
        
        load_btn = tk.Button(menu_frame, text="Load Game", 
                            command=self.load_game,
                            bg='#aa4444', fg='white', font=('Arial', 9))
        load_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(4, 0))
        
    def load_assets(self):
        """Load all sprites and backgrounds"""
        print("Loading game assets...")
        
        # Load sprites
        if os.path.exists(self.sprites_dir):
            for filename in os.listdir(self.sprites_dir):
                if filename.endswith('.png'):
                    try:
                        filepath = os.path.join(self.sprites_dir, filename)
                        image = Image.open(filepath)
                        image = image.resize((150, 150), Image.Resampling.LANCZOS)
                        self.sprite_cache[filename] = ImageTk.PhotoImage(image)
                    except Exception as e:
                        print(f"Failed to load sprite {filename}: {e}")
        
        # Load backgrounds
        if os.path.exists(self.backgrounds_dir):
            for filename in os.listdir(self.backgrounds_dir):
                if filename.endswith('.png'):
                    try:
                        filepath = os.path.join(self.backgrounds_dir, filename)
                        image = Image.open(filepath)
                        image = image.resize((900, 650), Image.Resampling.LANCZOS)
                        self.background_cache[filename] = ImageTk.PhotoImage(image)
                    except Exception as e:
                        print(f"Failed to load background {filename}: {e}")
        
        print(f"Assets loaded: {len(self.sprite_cache)} sprites, {len(self.background_cache)} backgrounds")
        
    def start_new_game(self):
        """Start a new game"""
        self.current_scene = "cave_entrance"
        self.game_state = "exploring"
        self.visited_scenes = ["cave_entrance"]
        self.game_progress = {
            'visited_village': False,
            'defeated_guardian': False,
            'found_treasure': False,
            'met_chief': False,
            'looked_around_dark': False,
            'sat_and_cried': False,
            'entered_skull_chamber': False,
            'gained_villagers_trust': False,
            'learned_ancient_secrets': False,
            'entered_cautiously': False,
            'confronted_darkness': False,
            'learned_village_history': False,
            'found_artifacts': False,
            'helped_villagers': False,
            'offered_services': False,
            'gained_magical_insight': False,
            'understood_pool_magic': False,
            'restored_health': False,
            'learned_village_customs': False,
            'protected_villagers': False,
            'gained_spiritual_insight': False,
            'found_corruption_source': False,
            'explored_alley': False,
            'found_alley_treasure': False,
            'investigated_alley_sounds': False,
            'examined_armory': False,
            'requested_custom_equipment': False,
            'learned_weapon_maintenance': False
        }
        
        self.update_display()
        class_name = self.classes[self.player_character]['name']
        self.add_story_text_top(f"Welcome to SHABUYA Cave Adventure! You are a {class_name} standing at the entrance to mysterious caves. What will you discover within?")
        
        # Show initial scene description and choices automatically
        self.show_scene_description()
        
    def show_scene_description(self):
        """Show the current scene description and choices automatically"""
        scene_descriptions = {
            "cave_entrance": "You wake up in a dark cave entrance, disoriented and confused. The air is cool and damp, and you can barely see your own hands in front of your face. You have no memory of how you got here.",
            "skull_chamber": "You enter a chamber filled with ancient skulls. The atmosphere is heavy with dark energy. The skulls seem to watch you as you move through the chamber.",
            "primitive_village": "You discover a primitive village. The inhabitants seem wary of outsiders. Smoke rises from cooking fires, and you can hear the sounds of daily life.",
            "chiefs_house": "You approach the chief's house. It's the largest building in the village, decorated with tribal symbols and trophies. The chief appears to be expecting visitors.",
            "healing_pool": "You find a mystical healing pool. Its waters glow with magical energy. The air around it feels charged with ancient power.",
            "village_changed": "The village has changed dramatically. Dark forces have taken hold. The once peaceful settlement now feels hostile and dangerous.",
            "alley": "You find yourself in a dark, narrow alley. Shadows dance on the walls, and you can hear distant sounds echoing through the passage.",
            "armory": "You enter a well-equipped armory. Weapons and armor line the walls, and the sound of metalworking echoes from the back."
        }
        
        scene_desc = scene_descriptions.get(self.current_scene, "You examine your surroundings carefully.")
        self.add_story_text_top(scene_desc)
        
        # If this scene has choices, show them as a numbered list
        if self.current_scene in self.scene_choices:
            self.add_story_text_top("")
            self.add_story_text_top("What would you like to do?")
            
            choices = self.scene_choices[self.current_scene]
            for i, choice in enumerate(choices):
                choice_text = f"{i+1}. {choice['text']}"
                self.add_story_text_top(choice_text)
            
            self.add_story_text_top("")
            self.add_story_text_top("Enter your choice (1-3) in the input field above.")
        
    def update_display(self):
        """Update the main display"""
        self.canvas.delete("all")
        
        # Draw background
        bg_file = f"{self.current_scene}.png"
        if bg_file in self.background_cache:
            bg_image = self.background_cache[bg_file]
            self.canvas.create_image(450, 325, image=bg_image)
        else:
            self.canvas.create_rectangle(0, 0, 900, 650, fill='#1a1a2e')
            self.canvas.create_text(450, 325, text=f"{self.current_scene.upper()}", 
                                   fill='#4a4a6a', font=('Arial', 32))
        
        # Draw player sprite
        player_sprite = f"{self.player_character}_sprite.png"
        if player_sprite in self.sprite_cache:
            sprite_image = self.sprite_cache[player_sprite]
            x, y = 350, 520
            self.canvas.create_image(x, y, image=sprite_image)
        
        # Draw enemy if in combat
        if self.game_state == "in_combat":
            enemy_sprites = ['cave_guardian_sprite.png', 'primitive_creature_sprite.png', 
                           'boss_divineheart_sprite.png']
            for enemy_file in enemy_sprites:
                if enemy_file in self.sprite_cache:
                    enemy_image = self.sprite_cache[enemy_file]
                    self.canvas.create_image(650, 500, image=enemy_image)
                    break
        
        # Update UI labels
        self.health_label.config(text=f"Health: {self.player_health}")
        self.level_label.config(text=f"Level: {self.player_level}")
        self.exp_label.config(text=f"Experience: {self.player_experience}")
        self.weapon_label.config(text=f"Weapon: {self.player_weapon}")
        self.scene_label.config(text=f"Scene: {self.current_scene.replace('_', ' ').title()}")
        self.state_label.config(text=f"State: {self.game_state.title()}")
        
    def show_inventory_stats(self):
        """Show inventory and stats window"""
        # Create inventory window
        inv_window = tk.Toplevel(self.root)
        inv_window.title("Inventory & Stats")
        inv_window.geometry("600x500")
        inv_window.configure(bg='#1a1a1a')
        inv_window.transient(self.root)
        inv_window.grab_set()
        
        # Title
        title = tk.Label(inv_window, text="Inventory & Character Stats", 
                        font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1a1a1a')
        title.pack(pady=15)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(inv_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Stats tab
        stats_frame = tk.Frame(notebook, bg='#2a2a2a')
        notebook.add(stats_frame, text="Stats")
        
        # Character stats
        stats_text = f"Class: {self.classes[self.player_character]['name']}\n"
        stats_text += f"Level: {self.player_level}\n"
        stats_text += f"Health: {self.player_health}/{self.classes[self.player_character]['health']}\n"
        stats_text += f"Experience: {self.player_experience}/100\n"
        stats_text += f"Strength: {self.player_strength}\n"
        stats_text += f"Agility: {self.player_agility}\n"
        stats_text += f"Intelligence: {self.player_intelligence}\n"
        stats_text += f"Ability: {self.player_ability}\n"
        stats_text += f"Equipped Weapon: {self.equipped_weapon}\n"
        stats_text += f"Equipped Armor: {self.equipped_armor or 'None'}\n"
        stats_text += f"Accessories: {', '.join(self.equipped_accessories) if self.equipped_accessories else 'None'}"
        
        stats_label = tk.Label(stats_frame, text=stats_text, 
                              fg='#cccccc', bg='#2a2a2a', font=('Arial', 12), 
                              justify=tk.LEFT)
        stats_label.pack(pady=20)
        
        # Inventory tab
        inv_frame = tk.Frame(notebook, bg='#2a2a2a')
        notebook.add(inv_frame, text="Inventory")
        
        # Inventory list
        inv_text = "Inventory Items:\n\n"
        for item in self.inventory:
            if item in self.weapons:
                item_info = f"⚔️ {item} (Weapon - {self.weapons[item]['damage']} damage)"
            elif item in self.items:
                item_info = f"📦 {item} - {self.items[item]['description']}"
            else:
                item_info = f"❓ {item}"
            inv_text += item_info + "\n\n"
        
        inv_label = tk.Label(inv_frame, text=inv_text, 
                            fg='#cccccc', bg='#2a2a2a', font=('Arial', 10), 
                            justify=tk.LEFT, wraplength=500)
        inv_label.pack(pady=20)
        
        # Equipment tab
        equip_frame = tk.Frame(notebook, bg='#2a2a2a')
        notebook.add(equip_frame, text="Equipment")
        
        # Equipment management
        equip_text = "Current Equipment:\n\n"
        equip_text += f"Weapon: {self.equipped_weapon or 'None'}\n"
        equip_text += f"Armor: {self.equipped_armor or 'None'}\n"
        equip_text += f"Accessories: {', '.join(self.equipped_accessories) if self.equipped_accessories else 'None'}\n\n"
        equip_text += "Available Equipment:\n\n"
        
        for item in self.inventory:
            if item in self.weapons:
                equip_text += f"⚔️ {item} (Weapon)\n"
            elif item in self.items and self.items[item]['type'] in ['armor', 'accessory']:
                equip_text += f"🛡️ {item} ({self.items[item]['type'].title()})\n"
        
        equip_label = tk.Label(equip_frame, text=equip_text, 
                              fg='#cccccc', bg='#2a2a2a', font=('Arial', 10), 
                              justify=tk.LEFT, wraplength=500)
        equip_label.pack(pady=20)
        
        # Close button
        close_btn = tk.Button(inv_window, text="Close", 
                             command=inv_window.destroy,
                             bg='#44aa44', fg='white', font=('Arial', 12, 'bold'))
        close_btn.pack(pady=15)
        
    def go_back_scene(self):
        """Go back to the previous scene"""
        if len(self.visited_scenes) > 1:
            self.visited_scenes.pop()  # Remove current scene
            self.current_scene = self.visited_scenes[-1]  # Get previous scene
            self.game_state = "exploring"
            self.add_story_text(f"You return to {self.current_scene.replace('_', ' ').title()}.")
            self.update_display()
            self.show_scene_description()
        else:
            self.add_story_text("You cannot go back further.")
            
    def execute_choice(self, choice, window):
        """Execute the chosen action"""
        if window:
            window.destroy()
        
        # Handle consequences
        consequence = choice['consequence']
        self.handle_consequence(consequence)
        
        self.update_display()
        
    def handle_consequence(self, consequence):
        """Handle the consequences of player choices"""
        consequences = {
            'looked_around_dark': {
                'text': 'It\'s dark, you can\'t see.',
                'effect': lambda: None
            },
            'sat_and_cried': {
                'text': 'You cried, nothing happened.',
                'effect': lambda: None
            },
            'entered_skull_chamber': {
                'text': 'You entered the skull chamber.',
                'effect': lambda: self.advance_to_skull_chamber()
            },
            'no_exit_visible': {
                'text': 'No exit is visible.',
                'effect': lambda: None
            },
            'tunnel_collapse': {
                'text': 'The tunnel starts to collapse!!',
                'effect': lambda: self.trigger_cave_in()
            },
            'learned_ancient_secrets': {
                'text': 'Ancient knowledge flows into your mind, enhancing your abilities.',
                'effect': lambda: self.gain_experience(25)
            },
            'found_artifacts': {
                'text': 'You find valuable artifacts that could be useful.',
                'effect': lambda: self.gain_experience(15)
            },
            'gained_spiritual_insight': {
                'text': 'You feel spiritually enlightened and more powerful.',
                'effect': lambda: self.gain_experience(20)
            },
            'gained_villagers_trust': {
                'text': 'The villagers begin to trust you and offer their help.',
                'effect': lambda: self.gain_experience(15)
            },
            'learned_village_customs': {
                'text': 'You understand the village customs and can navigate their society.',
                'effect': lambda: self.gain_experience(10)
            },
            'helped_villagers': {
                'text': 'Your help earns you the gratitude of the villagers.',
                'effect': lambda: self.gain_experience(15)
            },
            'met_chief': {
                'text': 'The chief recognizes your worth and offers guidance.',
                'effect': lambda: self.gain_experience(20)
            },
            'offered_services': {
                'text': 'The village welcomes your offer of assistance.',
                'effect': lambda: self.gain_experience(15)
            },
            'learned_village_history': {
                'text': 'You learn about the village\'s rich history and traditions.',
                'effect': lambda: self.gain_experience(15)
            },
            'restored_health': {
                'text': 'The healing waters restore your health and vitality.',
                'effect': lambda: self.restore_health(50)
            },
            'gained_magical_insight': {
                'text': 'You gain deeper understanding of magical forces.',
                'effect': lambda: self.gain_experience(25)
            },
            'understood_pool_magic': {
                'text': 'You learn to harness the pool\'s magical properties.',
                'effect': lambda: self.gain_experience(20)
            },
            'confronted_darkness': {
                'text': 'You face the corruption with courage and determination.',
                'effect': lambda: self.gain_experience(30)
            },
            'protected_villagers': {
                'text': 'You successfully protect the innocent villagers.',
                'effect': lambda: self.gain_experience(25)
            },
            'found_corruption_source': {
                'text': 'You discover the source of the corruption.',
                'effect': lambda: self.gain_experience(30)
            },
            'explored_alley': {
                'text': 'You discover a hidden passage in the alley.',
                'effect': lambda: self.gain_experience(15)
            },
            'found_alley_treasure': {
                'text': 'You find valuable items hidden in the alley.',
                'effect': lambda: self.gain_experience(20)
            },
            'investigated_alley_sounds': {
                'text': 'You uncover the source of the mysterious sounds.',
                'effect': lambda: self.gain_experience(15)
            },
            'examined_armory': {
                'text': 'You learn about the quality of weapons available.',
                'effect': lambda: self.gain_experience(15)
            },
            'requested_custom_equipment': {
                'text': 'The smith agrees to craft custom equipment for you.',
                'effect': lambda: self.gain_experience(20)
            },
            'learned_weapon_maintenance': {
                'text': 'You learn valuable techniques for maintaining your weapons.',
                'effect': lambda: self.gain_experience(15)
            },
            'advanced_to_village': {
                'text': 'You venture deeper into the cave system and emerge into a primitive village.',
                'effect': lambda: self.advance_to_scene('primitive_village')
            },
            'advanced_to_chiefs_house': {
                'text': 'You make your way to the chief\'s house, the largest building in the village.',
                'effect': lambda: self.advance_to_scene('chiefs_house')
            },
            'advanced_to_healing_pool': {
                'text': 'Following the chief\'s directions, you find the mystical healing pool.',
                'effect': lambda: self.advance_to_scene('healing_pool')
            },
            'advanced_to_village_changed': {
                'text': 'You return to the village, but something has changed dramatically.',
                'effect': lambda: self.advance_to_scene('village_changed')
            },
            'escaped_cave_in': {
                'text': 'You manage to escape the collapsing tunnel and find yourself in a new area.',
                'effect': lambda: self.advance_to_scene('primitive_village')
            }
        }
        
        if consequence in consequences:
            consequence_data = consequences[consequence]
            self.add_story_text(consequence_data['text'])
            consequence_data['effect']()
            
        # Mark progress
        self.game_progress[consequence] = True
        
        # Re-present choices if we're still in the same scene
        if self.current_scene in self.scene_choices:
            # Clear previous text and show fresh content
            self.clear_story_text()
            
            # Show the consequence result
            if consequence in consequences:
                consequence_data = consequences[consequence]
                self.add_story_text_top(consequence_data['text'])
            
            self.add_story_text_top("")
            self.add_story_text_top("What would you like to do?")
            self.add_story_text_top("")
            
            choices = self.scene_choices[self.current_scene]
            for i, choice in enumerate(choices):
                choice_text = f"{i+1}. {choice['text']}"
                self.add_story_text_top(choice_text)
            
            self.add_story_text_top("")
            self.add_story_text_top("Enter your choice (1-3) in the input field above.")
        
    def gain_experience(self, amount):
        """Gain experience points"""
        self.player_experience += amount
        self.add_story_text(f"You gain {amount} experience points!")
        
        if self.player_experience >= 100:
            self.level_up()
            
    def restore_health(self, amount):
        """Restore health"""
        old_health = self.player_health
        self.player_health = min(self.classes[self.player_character]['health'], 
                                self.player_health + amount)
        restored = self.player_health - old_health
        self.add_story_text(f"Your health is restored by {restored} points!")
        
    def advance_to_skull_chamber(self):
        """Advance directly to the skull chamber"""
        self.current_scene = "skull_chamber"
        self.visited_scenes.append("skull_chamber")
        self.game_state = "exploring"
        self.add_story_text_top("You find yourself in a chamber filled with ancient skulls.")
        self.update_display()
        self.show_scene_description()
        
    def advance_to_scene(self, scene_name):
        """Advance to a specific scene"""
        self.current_scene = scene_name
        if scene_name not in self.visited_scenes:
            self.visited_scenes.append(scene_name)
        self.game_state = "exploring"
        self.update_display()
        self.show_scene_description()
        
    def trigger_cave_in(self):
        """Trigger the cave-in event"""
        self.current_scene = "cave_in"
        if "cave_in" not in self.visited_scenes:
            self.visited_scenes.append("cave_in")
        self.game_state = "exploring"
        self.update_display()
        self.show_scene_description()
        
    def advance_scene(self):
        """Advance to the next scene in progression"""
        current_index = self.scene_progression.index(self.current_scene)
        if current_index < len(self.scene_progression) - 1:
            # Add current scene to visited list if not already there
            if self.current_scene not in self.visited_scenes:
                self.visited_scenes.append(self.current_scene)
            
            self.current_scene = self.scene_progression[current_index + 1]
            self.visited_scenes.append(self.current_scene)
            self.game_state = "exploring"
            self.add_story_text(f"You advance to {self.current_scene.replace('_', ' ').title()}.")
            self.update_display()
            # Show new scene description and choices automatically
            self.show_scene_description()
        else:
            self.add_story_text("You have reached the end of your journey... for now.")
            
    def start_combat(self):
        """Start a combat encounter"""
        self.game_state = "in_combat"
        self.add_story_text("A hostile creature appears! Combat begins!")
        self.update_display()
        
        # Calculate combat effectiveness based on class and weapon
        weapon_damage = self.weapons[self.player_weapon]['damage']
        class_bonus = 0
        
        if self.player_character == 'warrior':
            class_bonus = self.player_strength * 0.5
        elif self.player_character == 'rogue':
            class_bonus = self.player_agility * 0.3
        elif self.player_character == 'mage':
            class_bonus = self.player_intelligence * 0.4
            
        total_damage = weapon_damage + class_bonus
        
        # Combat resolution
        if random.random() < 0.7:  # 70% chance to win
            self.add_story_text(f"You defeat the enemy using your {self.player_weapon}! You gain experience.")
            self.player_experience += 10
            if self.player_experience >= 100:
                self.level_up()
        else:
            damage_taken = max(10, random.randint(15, 25))
            self.player_health = max(0, self.player_health - damage_taken)
            self.add_story_text(f"You are wounded in combat! You take {damage_taken} damage.")
            
        self.game_state = "exploring"
        self.update_display()
        
    def level_up(self):
        """Level up the player"""
        self.player_level += 1
        self.player_experience = 0
        self.player_health = self.classes[self.player_character]['health']  # Restore to max
        self.add_story_text(f"Level up! You are now level {self.player_level}! Your {self.player_ability} has grown stronger!")
        
    def add_story_text(self, text):
        """Add text to the story display"""
        self.story_text.insert(tk.END, f"{text}\n\n")
        self.story_text.see(tk.END)
        
    def add_story_text_top(self, text):
        """Add text to the story display and scroll to top"""
        self.story_text.insert(tk.END, f"{text}\n\n")
        self.story_text.see("1.0")
        
    def clear_story_text(self):
        """Clear the story text display"""
        self.story_text.delete(1.0, tk.END)
        
    def show_scene_description(self):
        """Show the current scene description and choices automatically"""
        # Clear previous text
        self.clear_story_text()
        
        scene_descriptions = {
            "cave_entrance": "You wake up in a dark cave entrance, disoriented and confused. The air is cool and damp, and you can barely see your own hands in front of your face. You have no memory of how you got here.",
            "skull_chamber": "You enter a chamber filled with ancient skulls. The atmosphere is heavy with dark energy. The skulls seem to watch you as you move through the chamber.",
            "primitive_village": "You discover a primitive village. The inhabitants seem wary of outsiders. Smoke rises from cooking fires, and you can hear the sounds of daily life.",
            "chiefs_house": "You approach the chief's house. It's the largest building in the village, decorated with tribal symbols and trophies. The chief appears to be expecting visitors.",
            "healing_pool": "You find a mystical healing pool. Its waters glow with magical energy. The air around it feels charged with ancient power.",
            "village_changed": "The village has changed dramatically. Dark forces have taken hold. The once peaceful settlement now feels hostile and dangerous.",
            "alley": "You find yourself in a dark, narrow alley. Shadows dance on the walls, and you can hear distant sounds echoing through the passage.",
            "armory": "You enter a well-equipped armory. Weapons and armor line the walls, and the sound of metalworking echoes from the back."
        }
        
        scene_desc = scene_descriptions.get(self.current_scene, "You examine your surroundings carefully.")
        self.add_story_text(scene_desc)
        
        # If this scene has choices, show them immediately
        if self.current_scene in self.scene_choices:
            self.add_story_text("")
            self.add_story_text("What would you like to do?")
            
            choices = self.scene_choices[self.current_scene]
            for i, choice in enumerate(choices):
                choice_text = f"{i+1}. {choice['text']}"
                self.add_story_text(choice_text)
            
            self.add_story_text("")
            self.add_story_text("Enter your choice (1-3) in the input field above.")
        
    def save_game(self):
        """Save the current game state"""
        # Placeholder for save functionality
        self.add_story_text("Game saved! (Save functionality to be implemented)")
        
    def load_game(self):
        """Load a saved game"""
        # Placeholder for load functionality
        self.add_story_text("Game loaded! (Load functionality to be implemented)")
        
    def handle_choice_input(self, event):
        """Handle user input for choice selection"""
        try:
            choice_number = int(self.choice_entry.get())
            if 1 <= choice_number <= 3:
                # Find the choice based on the number
                choices = self.scene_choices[self.current_scene]
                if choice_number - 1 < len(choices):
                    self.execute_choice(choices[choice_number - 1], None) # No window to destroy here
                else:
                    self.add_story_text("Invalid choice number.")
            else:
                self.add_story_text("Please enter a number between 1 and 3.")
        except ValueError:
            self.add_story_text("Please enter a valid number.")
        self.choice_entry.delete(0, tk.END) # Clear the entry field
        
    def run(self):
        """Start the GUI"""
        print("Player GUI ready!")
        self.root.mainloop()

if __name__ == "__main__":
    print("SHABUYA Cave Adventure - Player Mode")
    print("=" * 50)
    print("Linear gameplay experience")
    print("Progressive story and exploration")
    print("Character progression system")
    print("=" * 50)
    
    gui = PlayerGameGUI()
    gui.run()

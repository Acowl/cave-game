#!/usr/bin/env python3
"""
Cave Game - Main Game Loop and Scene Handlers

This is the main game file that orchestrates the Cave Game experience.
It imports modular components and handles the primary game flow including:
- Scene-based navigation and gameplay
- Combat encounters and boss battles
- Story progression and world exploration

This refactored version focuses solely on game flow coordination while
delegating specific functionality to specialized modules.

Usage:
    python game_refactored.py
    or
    python main.py
"""

# Import all our modular components
from config import (
    STAT_REQUIREMENT, 
    STARTING_STAT_VALUE, 
    LEVEL_UP_POINTS, 
    FINAL_BOSS_STAT_REQUIREMENT,
    SCENE_NAMES,
    MESSAGES
)
from ui import title_screen, display_weapon_choices, get_user_choice, confirm_action
from combat import check_weapon_effectiveness, execute_weapon_attack
from game_events import handle_game_over, handle_level_up, handle_loot_collection, handle_class_ability, start_game
from scenes import setup_scenes, check_scene_access, handle_locked_scene
from item import enhanced_dagger, enhanced_axe, enhanced_wand, dagger, axe, wand

def main():
    """Main game loop with title screen"""
    while True:
        if not title_screen():
            break  # Exit if player chooses not to play
        
        # Start new game
        player = start_game()
        play_game(player)

def play_game(player):
    """Main gameplay loop - now much more focused"""
    scenes = setup_scenes()
    current_scene = scenes[SCENE_NAMES['CAVE_ENTRANCE']]
    
    # Game state variables
    game_state = {
        'visited_village': False,
        'visited_armory': False,
        'visited_scenes': set(),
        'rogue_escaped_alley': False,
        'defeated_chief': False,
        'alley_creature_dead': False
    }
    
    while True:
        scene_name = current_scene.name
        
        # Route to appropriate scene handler
        if scene_name == SCENE_NAMES['CAVE_ENTRANCE']:
            result = handle_cave_entrance(current_scene, scenes)
        elif scene_name == SCENE_NAMES['SKULL_CHAMBER']:
            result = handle_skull_chamber(current_scene, scenes)
        elif scene_name == SCENE_NAMES['ALLEY']:
            result = handle_alley(player, current_scene, scenes, game_state)
        elif scene_name == SCENE_NAMES['ARMORY']:
            result = handle_armory(player, current_scene, scenes, game_state)
        elif scene_name == SCENE_NAMES['CHIEF_HOUSE']:
            result = handle_chief_house(player, current_scene, scenes, game_state)
        elif scene_name == SCENE_NAMES['PRIMITIVE_VILLAGE']:
            result = handle_village(player, current_scene, scenes, game_state)
        elif scene_name == SCENE_NAMES['HEALING_POOL']:
            result = handle_healing_pool(player, current_scene, scenes, game_state)
        elif scene_name == SCENE_NAMES['VILLAGE_CHANGED']:
            result = handle_final_boss(player, current_scene, scenes)
        else:
            result = handle_generic_scene(current_scene, scenes)
        
        # Process result
        if result['action'] == 'quit':
            print(MESSAGES['THANKS_PLAYING'])
            break
        elif result['action'] == 'restart':
            return  # Return to main loop
        elif result['action'] == 'change_scene':
            current_scene = result['scene']
        elif result['action'] == 'continue':
            continue

def handle_cave_entrance(current_scene, scenes):
    """Handle Cave Entrance scene"""
    first_cave = True
    looked_around = False
    
    while True:
        if first_cave:
            print()
            current_scene.enter(None)
            first_cave = False
        else:
            print()
            print("You're still in a dark cave. The only thing you notice is the crack in the wall.")
        
        print()
        print("What do you want to do?")
        print("1: Go through the crack")
        print("2: Sit and cry")
        print("3: Look around")
        print("4: Quit")
        
        choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "4", "quit"])
        
        if choice in ["4", "quit"]:
            return {'action': 'quit'}
        elif choice == "1":
            return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['SKULL_CHAMBER']]}
        elif choice == "2":
            print()
            print("You feel much better and would like to go through the crack.")
        elif choice == "3":
            if not looked_around:
                print()
                print("You look around but it's dark and you can't see.")
                looked_around = True
            else:
                print()
                print("You're in a dark cave and can't see anything except the crack in the wall.")

def handle_skull_chamber(current_scene, scenes):
    """Handle Skull Chamber scene"""
    print()
    current_scene.enter(None)
    print()
    print("As you explore the chamber, you see a primitive creature scurrying away among the shadows near the giant skull.")
    print("What do you want to do?")
    print("1: Chase after the creature")
    print("2: Stay and observe")
    print("3: Quit")
    
    choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "quit"])
    
    if choice in ["3", "quit"]:
        return {'action': 'quit'}
    elif choice == "1":
        print()
        print("You run after the moving figure, following its fleeting shadow through the chamber. You are led straight into the primitive village.")
        return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}
    elif choice == "2":
        print()
        print("You decide not to chase after it and remain cautious.")
        print("Suddenly, a rockfall blocks the path behind you! There is only one way forward now.")
        
        while True:
            print()
            print("You can only move forward now.")
            print("1: Move forward")
            print("2: Quit")
            cmd = get_user_choice("Enter the number of your choice: ", ["1", "2", "quit"])
            
            if cmd in ["2", "quit"]:
                return {'action': 'quit'}
            elif cmd == "1":
                return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}

def handle_village(player, current_scene, scenes, game_state):
    """Handle Primitive Village scene"""
    if not game_state['visited_village']:
        print()
        print("You step into the heart of the primitive village. Crude huts made of bone and hide cluster around a central fire pit, where embers glow and smoke drifts into the cavernous air. Strange symbols are painted on the rocks, and you hear the distant chatter of unseen creatures. Paths lead off in several directions: a shadowy alley, a fortified armory, and a large chief's house adorned with trophies.")
        game_state['visited_village'] = True
    
    print()
    print("Where would you like to go?")
    print("1: Enter the Alley (dangerous shadows)")
    print("2: Approach the Armory (locked chamber)")
    print("3: Visit the Chief's House (imposing hut)")
    print("4: Stay by the fire pit")
    print("5: Quit")
    
    choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "4", "5", "quit"])
    
    if choice in ["5", "quit"]:
        return {'action': 'quit'}
    elif choice == "1":
        return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['ALLEY']]}
    elif choice == "2":
        next_scene = scenes[SCENE_NAMES['ARMORY']]
        if check_scene_access(next_scene, player):
            return {'action': 'change_scene', 'scene': next_scene}
        else:
            handle_locked_scene("Armory", "Armory Key")
            return {'action': 'continue'}
    elif choice == "3":
        next_scene = scenes[SCENE_NAMES['CHIEF_HOUSE']]
        if check_scene_access(next_scene, player):
            return {'action': 'change_scene', 'scene': next_scene}
        else:
            handle_locked_scene("Chief's House", "Town Key")
            return {'action': 'continue'}
    elif choice == "4":
        print()
        print("You linger by the fire pit, feeling the warmth and watching the shadows dance. The village seems to hold its breath, waiting for your next move.")
        return {'action': 'continue'}

def handle_alley(player, current_scene, scenes, game_state):
    """Handle Alley scene - simplified with combat system"""
    print()
    
    if game_state['alley_creature_dead']:
        print("You return to the alley where the battle took place.")
        print("The creature's lifeless body still lies where you left it...")
        print()
        print("What do you want to do?")
        print("1: Search the area again")
        print("2: Return to the village")
        print("3: Quit")
        
        choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "quit"])
        
        if choice in ["3", "quit"]:
            return {'action': 'quit'}
        elif choice == "1":
            print("You search the area thoroughly, but find nothing new.")
            return {'action': 'continue'}
        elif choice == "2":
            return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}
    
    else:
        # Creature encounter
        print("You step cautiously into the narrow alley...")
        print("A primitive ground-dwelling creature bursts from a hidden burrow!")
        print()
        print("What do you do?")
        print("1: Attack the creature")
        print("2: Try to escape")
        print("3: Quit")
        
        choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "quit"])
        
        if choice in ["3", "quit"]:
            return {'action': 'quit'}
        elif choice == "1":
            # Combat sequence
            chosen_weapon = display_weapon_choices(player, "the alley creature battle")
            if chosen_weapon == "quit":
                return {'action': 'quit'}
            
            success, message = execute_weapon_attack(player, chosen_weapon, "alley_creature")
            print()
            print(message)
            
            if success:
                print("The creature lets out a final, defeated roar before collapsing in a heap.")
                print("Victory is yours!")
                print()
                handle_level_up(player)
                game_state['alley_creature_dead'] = True
                print()
                handle_loot_collection(player)
                print()
                print("You return to the village, victorious and stronger than before.")
                return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}
        elif choice == "2":
            if player.weapon == dagger:  # Rogue can escape
                print("Your rogue training allows you to escape successfully!")
                game_state['rogue_escaped_alley'] = True
                handle_level_up(player)
                return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}
            else:
                print("You fail to escape! The creature catches you.")
                print(MESSAGES['GAME_OVER'])
                if handle_game_over():
                    return {'action': 'restart'}
                else:
                    return {'action': 'quit'}

def handle_armory(player, current_scene, scenes, game_state):
    """Handle Armory scene - simplified"""
    print()
    current_scene.enter(player)
    game_state['visited_scenes'].add("Armory")
    
    if not game_state['visited_armory']:
        print()
        print("You enter the ancient armory. Three enhanced weapons rest on pedestals, glowing with magical energy:")
        print("- The Shadow Blade (Enhanced Dagger)")
        print("- The Bone Crusher (Enhanced Axe)")
        print("- The Skull Scepter (Enhanced Wand)")
        print("In the corner, you notice a key labeled 'Town Key' on a small table.")
        game_state['visited_armory'] = True
    
    # Track collected weapons
    if not hasattr(player, 'collected_weapons'):
        player.collected_weapons = []
    
    print()
    print("What would you like to do?")
    print("1: Take the Shadow Blade")
    print("2: Take the Bone Crusher")
    print("3: Take the Skull Scepter")
    print("4: Take the Town Key")
    print("5: Leave the armory")
    print("6: Quit")
    
    choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "4", "5", "6", "quit"])
    
    if choice in ["6", "quit"]:
        return {'action': 'quit'}
    elif choice == "1":
        if enhanced_dagger not in player.collected_weapons:
            player.collected_weapons.append(enhanced_dagger)
            print("You take the Shadow Blade! Its dark energy courses through you.")
        else:
            print("You already have the Shadow Blade.")
        return {'action': 'continue'}
    elif choice == "2":
        if enhanced_axe not in player.collected_weapons:
            player.collected_weapons.append(enhanced_axe)
            print("You take the Bone Crusher! Its weight feels perfect in your hands.")
        else:
            print("You already have the Bone Crusher.")
        return {'action': 'continue'}
    elif choice == "3":
        if enhanced_wand not in player.collected_weapons:
            player.collected_weapons.append(enhanced_wand)
            print("You take the Skull Scepter! Mystical power flows through it.")
        else:
            print("You already have the Skull Scepter.")
        return {'action': 'continue'}
    elif choice == "4":
        if not player.inventory.has_item("Town Key"):
            from item import Item
            town_key = Item("Town Key", "An ornate key that opens the Chief's House.")
            player.inventory.add_item(town_key)
            print("You take the Town Key. It feels warm to the touch.")
        else:
            print("You already have the Town Key.")
        return {'action': 'continue'}
    elif choice == "5":
        return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}

def handle_chief_house(player, current_scene, scenes, game_state):
    """Handle Chief House scene - simplified"""
    print()
    current_scene.enter(player)
    
    if not game_state['defeated_chief']:
        print()
        print("You enter the imposing chief's house...")
        print("The Chief challenges you to battle!")
        print()
        
        chosen_weapon = display_weapon_choices(player, "the Chief battle")
        if chosen_weapon == "quit":
            return {'action': 'quit'}
        
        success, message = execute_weapon_attack(player, chosen_weapon, "chief")
        print()
        print(message)
        
        if success:
            print()
            print("The Chief is defeated! The path to the healing pool is revealed!")
            handle_level_up(player)
            game_state['defeated_chief'] = True
            print()
            print("What do you want to do?")
            print("1: Enter the hidden passageway")
            print("2: Exit the Chief's house")
            print("3: Quit")
            
            choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "quit"])
            
            if choice in ["3", "quit"]:
                return {'action': 'quit'}
            elif choice == "1":
                return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['HEALING_POOL']]}
            elif choice == "2":
                return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}
        else:
            print()
            print(MESSAGES['GAME_OVER'])
            if handle_game_over():
                return {'action': 'restart'}
            else:
                return {'action': 'quit'}
    else:
        # Chief already defeated
        print("The Chief's lifeless body lies on the floor. The path to the healing pool remains open.")
        print()
        print("Where would you like to go?")
        print("1: Enter the Healing Pool")
        print("2: Return to the village")
        print("3: Quit")
        
        choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "quit"])
        
        if choice in ["3", "quit"]:
            return {'action': 'quit'}
        elif choice == "1":
            return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['HEALING_POOL']]}
        elif choice == "2":
            return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']]}

def handle_healing_pool(player, current_scene, scenes, game_state):
    """Handle Healing Pool scene"""
    print()
    if SCENE_NAMES['HEALING_POOL'] not in game_state['visited_scenes']:
        current_scene.enter(player)
        game_state['visited_scenes'].add(SCENE_NAMES['HEALING_POOL'])
        print()
        print("You emerge into a sacred chamber with mystical healing waters...")
    else:
        print("You return to the sacred healing chamber.")
    
    print()
    print("What would you like to do?")
    print("1: Enter the sacred waters")
    print("2: Return to the Chief's house")
    print("3: Quit")
    
    choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "quit"])
    
    if choice in ["3", "quit"]:
        return {'action': 'quit'}
    elif choice == "1":
        print()
        print("You approach the glowing waters...")
        if confirm_action("ARE YOU SURE?"):
            print()
            print("You enter the sacred waters and receive the divine blessing!")
            player.sacred_blessing = True
            print("🌟 You have received the Sacred Blessing! 🌟")
            print()
            print("The chamber begins to shake as something ancient awakens...")
            return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['VILLAGE_CHANGED']]}
        else:
            print("You step back from the pool.")
            return {'action': 'continue'}
    elif choice == "2":
        return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['CHIEF_HOUSE']]}

def handle_final_boss(player, current_scene, scenes):
    """Handle final boss battle - significantly simplified"""
    if not hasattr(player, 'sacred_blessing'):
        return {'action': 'change_scene', 'scene': scenes[SCENE_NAMES['HEALING_POOL']]}
    
    print()
    print("🌟 THE AWAKENING 🌟")
    print()
    print("The Divine Heart emerges from the depths!")
    print("🔥 FINAL BOSS BATTLE 🔥")
    print()
    
    # Initialize battle state
    if not hasattr(player, 'used_weapon_attack'):
        player.used_weapon_attack = False
    if not hasattr(player, 'used_class_ability'):
        player.used_class_ability = False
    
    # Check if both attacks completed
    if player.used_weapon_attack and player.used_class_ability:
        print("💥 ULTIMATE COMBO ACHIEVED! 💥")
        print("You have defeated the Divine Heart!")
        print("🎮 CONGRATULATIONS! YOU HAVE COMPLETED THE CAVE GAME! 🎮")
        return {'action': 'quit'}
    
    # Battle options
    print("How do you choose to face this cosmic horror?")
    print(f"1: Enhanced weapon attack" + (" (✅ COMPLETED)" if player.used_weapon_attack else ""))
    print(f"2: Class special ability" + (" (✅ COMPLETED)" if player.used_class_ability else ""))
    print("3: Quit")
    
    choice = get_user_choice("Enter the number of your choice: ", ["1", "2", "3", "quit"])
    
    if choice in ["3", "quit"]:
        return {'action': 'quit'}
    elif choice == "1" and not player.used_weapon_attack:
        chosen_weapon = display_weapon_choices(player, "the Divine Heart battle")
        if chosen_weapon == "quit":
            return {'action': 'quit'}
        
        success, message = execute_weapon_attack(player, chosen_weapon, "divine_heart")
        print()
        print(message)
        
        if success:
            player.used_weapon_attack = True
            print("🗡️ ENHANCED WEAPON ATTACK SUCCESSFUL! 🗡️")
        else:
            print(MESSAGES['GAME_OVER'])
            if handle_game_over():
                return {'action': 'restart'}
            else:
                return {'action': 'quit'}
        
        return {'action': 'continue'}
    
    elif choice == "2" and not player.used_class_ability:
        # Determine ability type based on weapon
        if player.weapon in [dagger, enhanced_dagger]:
            ability_type = "shadow_strike"
        elif player.weapon in [axe, enhanced_axe]:
            ability_type = "berserker_rage"
        else:
            ability_type = "strategic_analysis"
        
        success, message = handle_class_ability(player, ability_type)
        print()
        print(message)
        
        if success:
            player.used_class_ability = True
            print("🌟 CLASS ABILITY SUCCESSFUL! 🌟")
        else:
            print(MESSAGES['GAME_OVER'])
            if handle_game_over():
                return {'action': 'restart'}
            else:
                return {'action': 'quit'}
        
        return {'action': 'continue'}
    else:
        print("You have already used that ability!")
        return {'action': 'continue'}

def handle_generic_scene(current_scene, scenes):
    """Handle any unspecified scene"""
    print()
    current_scene.enter(None)
    print()
    print("Exits:", ', '.join(current_scene.exits.keys()) if hasattr(current_scene, 'exits') else "None")
    
    cmd = input("Where do you want to go? (or 'quit'): ").strip().lower()
    
    if cmd == "quit":
        return {'action': 'quit'}
    
    if hasattr(current_scene, 'exits') and cmd in current_scene.exits:
        next_scene_name = current_scene.exits[cmd]
        next_scene = scenes.get(next_scene_name)
        if next_scene:
            return {'action': 'change_scene', 'scene': next_scene}
        else:
            print("That exit doesn't lead anywhere.")
    else:
        print("Invalid direction.")
    
    return {'action': 'continue'}

if __name__ == "__main__":
    main()

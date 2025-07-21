#!/usr/bin/env python3
"""
Cave Game Events and Mechanics Module

This module handles core game mechanics including:
- Player progression and level ups
- Loot collection and rewards
- Game over handling and restart logic
- Game initialization and setup
- Character stat management

These systems provide the foundation for player progression throughout the game.
"""

from config import LEVEL_UP_POINTS, STARTING_STAT_VALUE, STAT_REQUIREMENT
from ui import confirm_action, display_stats

def handle_game_over():
    """Handle game over scenarios with restart option"""
    restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
    if restart_choice == "y" or restart_choice == "yes":
        print()
        print("=== RETURNING TO TITLE SCREEN ===")
        print()
        return True  # Signal to restart
    else:
        print()
        print("Thanks for playing!")
        return False  # Signal to exit

def handle_level_up(player):
    """Handle level up with automatic stat point allocation"""
    print("You feel a surge of power as you level up!")
    player.level += 1
    if not hasattr(player, 'attribute_points'):
        player.attribute_points = 0
    player.attribute_points += LEVEL_UP_POINTS
    print(f"You gained {LEVEL_UP_POINTS} attribute points! Total: {player.attribute_points}")
    handle_stat_allocation(player)

def handle_stat_allocation(player):
    """Handle stat allocation with input validation"""
    print()
    while player.attribute_points > 0:
        print(f"Attribute points remaining: {player.attribute_points}")
        display_stats(player)
        print()
        print("Which attribute would you like to increase?")
        print("1: Vitality")
        print("2: Agility")
        print("3: Strength")
        print("4: Intelligence")
        
        while True:
            choice = input("Enter your choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        
        if choice == '1':
            if not hasattr(player, 'vitality'):
                player.vitality = STARTING_STAT_VALUE
            player.vitality += 1
            print(f"Vitality increased to {player.vitality}!")
        elif choice == '2':
            if not hasattr(player, 'agility'):
                player.agility = STARTING_STAT_VALUE
            player.agility += 1
            print(f"Agility increased to {player.agility}!")
        elif choice == '3':
            if not hasattr(player, 'strength'):
                player.strength = STARTING_STAT_VALUE
            player.strength += 1
            print(f"Strength increased to {player.strength}!")
        elif choice == '4':
            if not hasattr(player, 'intelligence'):
                player.intelligence = STARTING_STAT_VALUE
            player.intelligence += 1
            print(f"Intelligence increased to {player.intelligence}!")
        
        player.attribute_points -= 1
        print()

def handle_loot_collection(player, item_name="Armory Key", item_description="A rusty key that opens the armory.", prompt="Would you like to loot the corpse?"):
    """Handle loot collection with proper validation"""
    if confirm_action(prompt):
        print(f"You search through the creature's belongings and find a rusty key labeled '{item_name}'.")
        print("The key appears to be quite old but still functional.")
        from item import Item
        armory_key = Item(item_name, item_description)
        player.inventory.add_item(armory_key)
    else:
        print("You decide to leave without investigating further.")

def handle_class_ability(player, ability_type):
    """Handle class-specific special abilities"""
    from item import dagger, axe, wand, enhanced_dagger, enhanced_axe, enhanced_wand
    
    if ability_type == "shadow_strike":
        if player.weapon in [dagger, enhanced_dagger]:
            agility_stat = getattr(player, 'agility', STARTING_STAT_VALUE)
            enhanced_weapon_equipped = player.weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
            
            if agility_stat >= STAT_REQUIREMENT and enhanced_weapon_equipped:
                message = ("You melt into the shifting shadows of the chamber! "
                          f"Your legendary agility ({agility_stat}) combines with your enhanced weapon's dark power! "
                          "You become one with the shadows, moving faster than perception. "
                          "Appearing behind your target's blind spot, you drive your enhanced blade "
                          "directly into its core in a perfect assassination technique!")
                return True, message
            else:
                return False, f"You need legendary agility ({STAT_REQUIREMENT}+) and an enhanced weapon!"
        else:
            return False, "You're not agile enough for shadow techniques!"
    
    elif ability_type == "berserker_rage":
        if player.weapon in [axe, enhanced_axe]:
            strength_stat = getattr(player, 'strength', STARTING_STAT_VALUE)
            enhanced_weapon_equipped = player.weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
            
            if strength_stat >= STAT_REQUIREMENT and enhanced_weapon_equipped:
                message = ("You feel primal rage building within your core! "
                          f"Your incredible strength ({strength_stat}) erupts in divine fury! "
                          "Your weapon becomes an extension of your will as raw rage "
                          "overtakes your mind. You become an unstoppable force of destruction, "
                          "each blow landing with the force of a falling mountain!")
                return True, message
            else:
                return False, f"You need legendary strength ({STAT_REQUIREMENT}+) and an enhanced weapon!"
        else:
            return False, "You lack the warrior's spirit for berserker rage!"
    
    elif ability_type == "strategic_analysis":
        if player.weapon in [wand, enhanced_wand]:
            intelligence_stat = getattr(player, 'intelligence', STARTING_STAT_VALUE)
            enhanced_weapon_equipped = player.weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
            
            if intelligence_stat >= STAT_REQUIREMENT and enhanced_weapon_equipped:
                message = ("You focus your mind and carefully analyze the situation! "
                          f"Your brilliant intelligence ({intelligence_stat}) reveals the perfect strategy! "
                          "You identify structural weaknesses and environmental opportunities. "
                          "Your enhanced weapon channels precise force to exploit these vulnerabilities "
                          "with devastating effect!")
                return True, message
            else:
                return False, f"You need legendary intelligence ({STAT_REQUIREMENT}+) and an enhanced weapon!"
        else:
            return False, "You lack the intellectual capacity for strategic analysis!"
    
    return False, "Unknown ability type!"

def start_game():
    """Initialize a new game with character creation"""
    from player import Player
    from item import Inventory, dagger, axe, wand
    
    player = Player()
    player.inventory = Inventory()
    
    print("\nChoose your class:")
    print("1: Rogue")
    print("2: Warrior")
    print("3: Mage")
    
    while True:
        class_choice = input("Enter the number of your class (1-3): ").strip()
        
        if class_choice == "1":
            player.weapon = dagger
            print("You are a Rogue. You start with a Dagger.")
            break
        elif class_choice == "2":
            player.weapon = axe
            print("You are a Warrior. You start with an Axe.")
            break
        elif class_choice == "3":
            player.weapon = wand
            print("You are a Mage. You start with a Wand.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    return player

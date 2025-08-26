#!/usr/bin/env python3
"""
Cave Game User Interface Module

This module handles all user interface functions including:
- Title screen display
- User input and choice handling
- Weapon selection interface
- Action confirmation prompts
- Game messages and formatting

All UI-related functionality is centralized here for consistent user experience.
"""

from config import MESSAGES


def title_screen():
    """Display the title screen and main menu"""
    print("==================================================")
    print("        🗻 SHABUYA 🗻")
    print("==================================================")
    print()
    print("Would you like to play?")
    print("1. Start New Game")
    print("2. Exit")
    
    while True:
        choice = input("Enter your choice (1-2): ").strip()
        if choice == "1":
            return True  # Start game
        elif choice == "2":
            return False  # Exit
        else:
            print("Invalid choice. Please enter 1 or 2.")


def display_weapon_choices(player, context="battle"):
    """Display weapon choices and return selected weapon."""
    from combat import get_available_weapons
    
    available_weapons = get_available_weapons(player)
    
    print(f"Choose your weapon for {context}:")
    for i, weapon in enumerate(available_weapons, 1):
        print(f"{i}: Attack with {weapon.name}")
    
    quit_option = len(available_weapons) + 1
    print(f"{quit_option}: Quit")
    
    while True:
        choice = input("Enter the number of your choice: ").strip()
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(available_weapons):
                return available_weapons[choice_num - 1]
            elif choice_num == quit_option or choice.lower() == "quit":
                return "quit"
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            if choice.lower() == "quit":
                return "quit"
            print("Invalid option. Please try again.")


def get_user_choice(prompt, valid_choices):
    """Get user input with validation"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Please enter one of: {', '.join(valid_choices)}")


def display_stats(player):
    """Display player statistics"""
    from config import STARTING_STAT_VALUE
    
    print("Current stats:")
    print(f"Vitality: {getattr(player, 'vitality', STARTING_STAT_VALUE)}")
    print(f"Agility: {getattr(player, 'agility', STARTING_STAT_VALUE)}")
    print(f"Strength: {getattr(player, 'strength', STARTING_STAT_VALUE)}")
    print(f"Intelligence: {getattr(player, 'intelligence', STARTING_STAT_VALUE)}")


def confirm_action(prompt):
    """Get yes/no confirmation from user"""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

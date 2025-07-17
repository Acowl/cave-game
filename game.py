from player import Player
from player import Scene
from item import Inventory, dagger, axe, wand, enhanced_dagger, enhanced_axe, enhanced_wand
from enemy import Enemy, gain_experience, allocate_attribute

def get_available_weapons(player):
    """Get list of weapons available to the player."""
    available = [player.weapon]  # Always have starting weapon
    
    # Add collected enhanced weapons
    if hasattr(player, 'collected_weapons'):
        for weapon in player.collected_weapons:
            if weapon not in available:
                available.append(weapon)
    
    return available

def display_weapon_choices(player, context="battle"):
    """Display weapon choices and return selected weapon."""
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

def handle_stat_allocation(player):
    """Handle stat allocation with input validation"""
    if hasattr(player, 'attribute_points') and player.attribute_points >= 3:
        print("Allocate your 3 stat points:")
        for i in range(3):
            while True:
                print(f"Point {i+1} - Choose an attribute:")
                print("1: Vitality")
                print("2: Agility") 
                print("3: Strength")
                print("4: Intelligence")
                choice = input("Enter the number of your choice (1-4): ").strip()
                
                if choice == "1":
                    allocate_attribute(player, "vitality")
                    break
                elif choice == "2":
                    allocate_attribute(player, "agility")
                    break
                elif choice == "3":
                    allocate_attribute(player, "strength")
                    break
                elif choice == "4":
                    allocate_attribute(player, "intelligence")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")

def setup_scenes():
    cave = Scene(
        name="Cave Entrance",
        description="You awaken in a dark, damp cave. The air is thick and the only exit is a narrow crack in the wall.",
        exits={"crack": "Skull Chamber"}
    )
    skull_chamber = Scene(
        name="Skull Chamber",
        description=(
            "\n"
            "The air is thick with dust and the faint scent of something ancient.\n"
            "At the center of the room, illuminated by an eerie, pulsating glow, sits a colossal skull—its empty eye sockets seem to watch your every move.\n"
            "Shadows dance along the walls, cast by the flickering light within the skull.\n"
            "The silence is heavy, broken only by the distant drip of water and your own heartbeat.\n"
            "There is a sense of awe and dread here, as if you have stepped into the remains of something once divine.\n"
        ),
        exits={"back": "Cave Entrance", "forward": "Primitive Village"}
    )
    primitive_village = Scene(
        name="Primitive Village",
        description="Moving forward, you spot creatures in the distance. As you approach, you discover primitive structures and signs of life.",
        exits={"back": "Skull Chamber"}
    )
    armory = Scene(
        name="Armory",
        description="A locked chamber filled with ancient weapons: a dagger, an axe, and a wand rest on pedestals.",
        exits={"back": "Primitive Village"},
        locked=True,
        key="Armory Key"
    )
    alley = Scene(
        name="Alley",
        description="A narrow alley with shadows lurking. You sense danger ahead.",
        exits={"back": "Primitive Village"}
    )
    chief_house = Scene(
        name="Cave People Chief House",
        description="A large hut adorned with bones and primitive art. The chief, a formidable figure, awaits inside.",
        exits={"back": "Primitive Village"},
        locked=True,
        key="Town Key"
    )
    healing_pool = Scene(
        name="Healing Pool",
        description="A tranquil chamber with a glowing pool. Its waters are said to heal all wounds.",
        exits={"back": "Cave People Chief House"}
    )
    final_village = Scene(
        name="Primitive Village Changed",
        description="As you leave the healing pool, a rumbling shakes the ground. The village is collapsing—the skull was the remains of a giant immortal god. A roar echoes as the final boss emerges.",
        exits={"back": "Healing Pool"}
    )
    
    # Now update exits after all scenes are defined
    primitive_village.exits["armory"] = "Armory"
    primitive_village.exits["alley"] = "Alley"
    primitive_village.exits["chief_house"] = "Cave People Chief House"
    chief_house.exits["healing_pool"] = "Healing Pool"
    healing_pool.exits["final_village"] = "Primitive Village Changed"
    
    scenes = {
        "Cave Entrance": cave,
        "Skull Chamber": skull_chamber,
        "Primitive Village": primitive_village,
        "Armory": armory,
        "Alley": alley,
        "Cave People Chief House": chief_house,
        "Healing Pool": healing_pool,
        "Primitive Village Changed": final_village
    }
    return scenes

def title_screen():
    """Display the title screen and main menu"""
    print("\n" + "="*50)
    print("        🌟 SHABUYA 🌟")
    print("="*50)
    print()
    
    while True:
        print("Would you like to play?")
        print("1. Start New Game")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ").strip()
        
        if choice == "1":
            return True  # Start the game
        elif choice == "2":
            print("\nThank you for playing SHABUYA!")
            return False  # Exit the game
        else:
            print("Invalid choice. Please enter 1 or 2.")

def start_game():
    """Initialize a new game with character creation"""
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

def main():
    """Main game loop with title screen"""
    while True:
        if not title_screen():
            break  # Exit if player chooses not to play
        
        # Start new game
        player = start_game()
        play_game(player)

def play_game(player):
    """Main gameplay loop"""
def play_game(player):
    """Main gameplay loop"""
    scenes = setup_scenes()
    current_scene = scenes["Cave Entrance"]
    visited_village = False
    visited_armory = False
    visited_scenes = set()
    rogue_escaped_alley = False
    defeated_chief = False
    alley_creature_dead = False
    
    while True:
        if current_scene.name == "Cave Entrance":
            first_cave = True
            looked_around = False
            while True:
                if first_cave:
                    print()
                    current_scene.enter(player)
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
                choice = input("Enter the number of your choice: ").strip().lower()
                
                if choice == "4" or choice == "quit":
                    print()
                    print("Thanks for playing!")
                    return
                elif choice == "1":
                    current_scene = scenes.get("Skull Chamber")
                    break
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
                else:
                    print()
                    print("Invalid option.")
        
        elif current_scene.name == "Skull Chamber":
            print()
            current_scene.enter(player)
            print()
            print("As you explore the chamber, you see a primitive creature scurrying away among the shadows near the giant skull.")
            print("What do you want to do?")
            print("1: Chase after the creature")
            print("2: Stay and observe")
            print("3: Quit")
            chase_choice = input("Enter the number of your choice: ").strip().lower()
            
            if chase_choice == "3" or chase_choice == "quit":
                print()
                print("Thanks for playing!")
                break
            elif chase_choice == "1":
                print()
                print("You run after the moving figure, following its fleeting shadow through the chamber. You are led straight into the primitive village.")
                current_scene = scenes.get("Primitive Village")
                continue
            elif chase_choice == "2":
                print()
                print("You decide not to chase after it and remain cautious.")
                print("Suddenly, a rockfall blocks the path behind you! There is only one way forward now.")
                current_scene.exits = {"forward": "Primitive Village"}
                while True:
                    print()
                    print("You can only move forward now.")
                    print("1: Move forward")
                    print("2: Quit")
                    cmd = input("Enter the number of your choice: ").strip().lower()
                    if cmd == "2" or cmd == "quit":
                        print()
                        print("Thanks for playing!")
                        return
                    elif cmd == "1":
                        next_scene = scenes.get("Primitive Village")
                        if next_scene:
                            current_scene = next_scene
                            break
                        else:
                            print("That exit doesn't lead anywhere.")
                    else:
                        print()
                        print("Invalid option.")
                continue
            else:
                print()
                print("Invalid option.")
        
        elif current_scene.name == "Alley":
            print()
            if alley_creature_dead:
                print("You return to the alley where the battle took place.")
                print("The creature's lifeless body still lies where you left it, a grim reminder")
                print("of your victory. Dried blood stains the cobblestones, and the alley feels")
                print("eerily quiet without the beast's menacing presence. The shadows that once")
                print("held danger now seem ordinary and empty.")
                print()
                print("What do you want to do?")
                print("1: Search the area again")
                print("2: Return to the village")
                print("3: Quit")
                choice = input("Enter the number of your choice: ").strip().lower()
                
                if choice == "3" or choice == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                elif choice == "1":
                    print()
                    print("You search the area thoroughly, but find nothing new.")
                    print("The creature's belongings were already looted, and there's nothing")
                    print("else of value in this narrow alley.")
                elif choice == "2":
                    print()
                    print("You leave the alley and return to the village center.")
                    current_scene = scenes.get("Primitive Village")
                else:
                    print("Invalid option.")
            elif rogue_escaped_alley and player.weapon == dagger:
                print("You cautiously return to the shadowy alley, your footsteps silent on the cobblestones.")
                print("Having escaped once before, you now know exactly where the creature lurks.")
                print("From the safety of the shadows, you can see it hunched over something near its burrow,")
                print("completely unaware of your presence. This is your chance for a perfect ambush.")
                print()
                print("What do you do?")
                print("1: Sneak up and ambush the creature")
                print("2: Return to the village")
                print("3: Quit")
                choice = input("Enter the number of your choice: ").strip().lower()
                
                if choice == "3" or choice == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                elif choice == "1":
                    print()
                    print("Like a wraith born from darkness itself, you glide silently across the alley floor.")
                    print("Your dagger gleams wickedly as you position yourself directly behind the unsuspecting creature.")
                    print("In one fluid motion, you strike from the shadows with deadly precision.")
                    print("The creature lets out a strangled gasp before collapsing, never knowing what hit it.")
                    print("Blood pools beneath its still form as you stand victorious over your prey.")
                    print()
                    print("You feel a surge of power as you level up!")
                    # Automatic level up with 3 attribute points
                    player.level += 1
                    if not hasattr(player, 'attribute_points'):
                        player.attribute_points = 0
                    player.attribute_points += 3
                    print(f"You gained 3 attribute points! Total: {player.attribute_points}")
                    handle_stat_allocation(player)
                    alley_creature_dead = True
                    print()
                    while True:
                        loot_choice = input("Would you like to loot the corpse? (y/n): ").strip().lower()
                        if loot_choice in ['y', 'yes', 'n', 'no']:
                            break
                        else:
                            print("Please enter 'y' for yes or 'n' for no.")
                    if loot_choice in ['y', 'yes']:
                        print("You carefully search the creature's belongings and find a rusty key labeled 'Armory Key'.")
                        print("The metal is old but sturdy, and it feels important in your hands.")
                        from item import Item
                        armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                        player.inventory.add_item(armory_key)
                    else:
                        print("You decide to leave the corpse untouched and slip away as silently as you came.")
                    print()
                    print("You return to the village, your successful ambush filling you with confidence.")
                    current_scene = scenes.get("Primitive Village")
                elif choice == "2":
                    print()
                    print("You decide discretion is the better part of valor and silently withdraw.")
                    print("Perhaps another approach would be wiser.")
                    current_scene = scenes.get("Primitive Village")
                else:
                    print("Invalid option.")
            else:
                print("You step cautiously into the narrow alley, ancient stone walls rising on either side.")
                print("The air is thick with the smell of decay and something wild. Shadows dance menacingly")
                print("in the dim light filtering down from above. Suddenly, you hear a low, guttural growling.")
                print()
                print("The ground trembles as a primitive ground-dwelling creature bursts from a hidden burrow!")
                print("Its skin is mottled brown and gray, scarred from countless battles. Yellowed fangs")
                print("gleam in its snarling maw, and its red eyes burn with feral hunger. Crude bone ornaments")
                print("dangle from its muscular frame as it brandishes a massive, blood-stained club.")
                print("The beast blocks your path completely, muscles tensed and ready to strike.")
                print()
                print("What do you do?")
                print("1: Attack the creature")
                print("2: Stealth Strike (Rogue approach)")
                print("3: Intimidating Charge (Warrior approach)")
                print("4: Tactical Analysis (Mage approach)")
                print("5: Run away")
                print("6: Quit")
                action_choice = input("Enter the number of your choice: ").strip().lower()
                
                if action_choice == "6" or action_choice == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                elif action_choice == "1":
                    print()
                    # Use weapon selection system for attack
                    chosen_weapon = display_weapon_choices(player, "the alley creature battle")
                    
                    if chosen_weapon == "quit":
                        print()
                        print("Thanks for playing!")
                        break
                    
                    print()
                    print(f"You grip your {chosen_weapon.name} and prepare for battle!")
                    
                    # Battle outcomes based on weapon choice and class match
                    victory = False
                    
                    if chosen_weapon == dagger:
                        victory = True
                        print("You lunge forward with cat-like agility!")
                        print("The creature swings its massive club, but you duck and weave beneath its guard.")
                        print("Your blade finds the gaps in its thick hide, striking with surgical precision.")
                        print("With a final, lightning-fast thrust, you drive your dagger deep into its heart.")
                    elif chosen_weapon == axe:
                        victory = True
                        print("You raise your axe high and charge with a mighty war cry!")
                        print("The creature's club crashes against your axe in a shower of sparks and splinters.")
                        print("Your superior strength and weapon training quickly turn the tide.")
                        print("With a devastating overhead swing, you cleave through the beast's defenses.")
                    elif chosen_weapon == wand:
                        victory = True
                        print("You point your wand at the creature and channel your magical energy!")
                        print("Bolts of mystical force streak through the air, striking the beast repeatedly.")
                        print("The creature staggers as arcane energy burns through its primitive flesh.")
                        print("A final, concentrated blast of magic brings the beast to its knees.")
                    elif chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]:
                        # Enhanced weapons work regardless of class, but with different effectiveness
                        victory = True
                        if chosen_weapon == enhanced_dagger:
                            print("The Shadow Blade erupts with dark energy as you strike!")
                            print("Your enhanced dagger cuts through the creature's hide like butter.")
                            print("Dark energy courses through each wound, weakening the beast rapidly.")
                            print("With supernatural speed, you deliver a flurry of shadow-enhanced strikes.")
                        elif chosen_weapon == enhanced_axe:
                            print("The Bone Crusher resonates with primal power!")
                            print("Your enhanced axe cleaves through the creature's club like paper.")
                            print("Each swing carries devastating force that shakes the alley walls.")
                            print("A final earth-shaking blow crushes the beast completely.")
                        elif chosen_weapon == enhanced_wand:
                            print("The Skull Scepter blazes with arcane might!")
                            print("Torrents of magical energy pour from your enhanced wand.")
                            print("The creature's primitive defenses crumble before your mystical assault.")
                            print("A concentrated beam of pure magic overwhelms the beast utterly.")
                    
                    if victory:
                        print("The creature lets out a final, defeated roar before collapsing in a heap.")
                        print("Victory is yours! The alley falls silent except for your heavy breathing.")
                        print()
                        print("You feel a surge of power as you level up!")
                        # Automatic level up with 3 attribute points
                        player.level += 1
                        if not hasattr(player, 'attribute_points'):
                            player.attribute_points = 0
                        player.attribute_points += 3
                        print(f"You gained 3 attribute points! Total: {player.attribute_points}")
                        handle_stat_allocation(player)
                        alley_creature_dead = True
                    print()
                    while True:
                        loot_choice = input("Would you like to loot the corpse? (y/n): ").strip().lower()
                        if loot_choice in ['y', 'yes', 'n', 'no']:
                            break
                        else:
                            print("Please enter 'y' for yes or 'n' for no.")
                    if loot_choice in ['y', 'yes']:
                        print("You search through the creature's belongings and find a rusty key labeled 'Armory Key'.")
                        print("The key appears to be quite old but still functional.")
                        from item import Item
                        armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                        player.inventory.add_item(armory_key)
                    else:
                        print("You decide to leave the corpse alone and step away from the grisly scene.")
                    print()
                    print("You return to the village, victorious and stronger than before.")
                    current_scene = scenes.get("Primitive Village")
                elif action_choice == "2":
                    print()
                    if player.weapon == dagger:  # Rogue - correct class
                        print("STEALTH STRIKE - SUCCESS!")
                        print("Your rogue training allows you to move like a shadow!")
                        print("You melt into the darkness, circling behind the creature undetected.")
                        print("With perfect precision, you strike from the shadows, finding a vital spot.")
                        print("The creature collapses before it even realizes you moved!")
                        print()
                        print("Your stealth mastery has won the day!")
                        print("You feel a surge of power as you level up!")
                        # Level up logic
                        player.level += 1
                        if not hasattr(player, 'attribute_points'):
                            player.attribute_points = 0
                        player.attribute_points += 3
                        print(f"You gained 3 attribute points! Total: {player.attribute_points}")
                        handle_stat_allocation(player)
                        alley_creature_dead = True
                        
                        # Loot logic
                        while True:
                            loot_choice = input("Would you like to loot the corpse? (y/n): ").strip().lower()
                            if loot_choice in ['y', 'yes', 'n', 'no']:
                                break
                            else:
                                print("Please enter 'y' for yes or 'n' for no.")
                        if loot_choice in ['y', 'yes']:
                            print("You search through the creature's belongings and find a rusty key labeled 'Armory Key'.")
                            print("The key appears to be quite old but still functional.")
                            from item import Item
                            armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                            player.inventory.add_item(armory_key)
                        else:
                            print("You decide to leave the corpse alone and step away from the grisly scene.")
                        print()
                        print("You return to the village, victorious through superior stealth.")
                        current_scene = scenes.get("Primitive Village")
                    else:
                        print("STEALTH STRIKE - FAILED!")
                        print("You attempt to move stealthily, but you're not a rogue!")
                        print("Without proper training, your footsteps echo loudly in the alley.")
                        print("The creature immediately spots you and snarls with amusement.")
                        print("Your clumsy attempt at stealth has only made you an easier target!")
                        print()
                        print("THUD! The creature's club crashes down with devastating force!")
                        print("💀 CLASS MISMATCH - STEALTH FAILED - YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                elif action_choice == "3":
                    print()
                    if player.weapon == axe:  # Warrior - correct class
                        print("INTIMIDATING CHARGE - SUCCESS!")
                        print("You let out a thunderous battle cry that echoes through the alley!")
                        print("Your warrior training and imposing presence with the heavy axe")
                        print("causes the creature to hesitate. It recognizes the threat you pose")
                        print("and the deadly competence in your stance. Primitive intelligence")
                        print("flickers in its red eyes as it weighs the cost of this fight.")
                        print()
                        print("The creature slowly backs away, keeping its club ready but no longer")
                        print("eager for combat. It disappears back into its burrow, leaving you")
                        print("the clear victor without needing to spill blood.")
                        print("Your intimidation was successful!")
                        print()
                        print("You feel a surge of power as you level up!")
                        # Level up logic
                        player.level += 1
                        if not hasattr(player, 'attribute_points'):
                            player.attribute_points = 0
                        player.attribute_points += 3
                        print(f"You gained 3 attribute points! Total: {player.attribute_points}")
                        handle_stat_allocation(player)
                        alley_creature_dead = True
                        
                        # Loot logic
                        while True:
                            loot_choice = input("Would you like to loot the creature's dropped items? (y/n): ").strip().lower()
                            if loot_choice in ['y', 'yes', 'n', 'no']:
                                break
                            else:
                                print("Please enter 'y' for yes or 'n' for no.")
                        if loot_choice in ['y', 'yes']:
                            print("You search where the creature dropped something and find a rusty key labeled 'Armory Key'.")
                            print("The key appears to be quite old but still functional.")
                            from item import Item
                            armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                            player.inventory.add_item(armory_key)
                        else:
                            print("You decide to leave without investigating further.")
                        print()
                        print("You return to the village, having proven your warrior's dominance.")
                        current_scene = scenes.get("Primitive Village")
                    else:
                        print("INTIMIDATING CHARGE - FAILED!")
                        print("You attempt to be intimidating, but you're not a warrior!")
                        print("Without warrior training, your voice wavers with uncertainty.")
                        print("The creature senses your fear and lack of confidence immediately.")
                        print("Your weapon doesn't match the intimidating presence of a true warrior.")
                        print("The beast's red eyes gleam with cruel amusement at your pathetic attempt.")
                        print()
                        print("Enraged by your weakness, the creature charges with doubled fury!")
                        print("💀 CLASS MISMATCH - INTIMIDATION FAILED - YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                elif action_choice == "4":
                    print()
                    if player.weapon == wand:  # Mage - correct class
                        print("TACTICAL ANALYSIS - SUCCESS!")
                        print("Your mage training allows you to quickly assess the situation!")
                        print("You notice loose stones above the creature's position and weak points")
                        print("in the alley's structure. With precise magical manipulation, you cause")
                        print("a small rockslide that traps the creature without harming it.")
                        print()
                        print("The beast finds itself buried up to its neck, completely immobilized.")
                        print("Unable to move or fight, it can only watch helplessly as you walk past.")
                        print("Your strategic thinking has won without violence!")
                        print()
                        print("You feel a surge of power as you level up!")
                        # Level up logic
                        player.level += 1
                        if not hasattr(player, 'attribute_points'):
                            player.attribute_points = 0
                        player.attribute_points += 3
                        print(f"You gained 3 attribute points! Total: {player.attribute_points}")
                        handle_stat_allocation(player)
                        alley_creature_dead = True
                        
                        # Loot logic  
                        while True:
                            loot_choice = input("Would you like to search the area before the creature was trapped? (y/n): ").strip().lower()
                            if loot_choice in ['y', 'yes', 'n', 'no']:
                                break
                            else:
                                print("Please enter 'y' for yes or 'n' for no.")
                        if loot_choice in ['y', 'yes']:
                            print("You search the creature's burrow and find a rusty key labeled 'Armory Key'.")
                            print("The key appears to be quite old but still functional.")
                            from item import Item
                            armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                            player.inventory.add_item(armory_key)
                        else:
                            print("You decide to leave the area without further investigation.")
                        print()
                        print("You return to the village, victorious through superior intellect.")
                        current_scene = scenes.get("Primitive Village")
                    else:
                        print("TACTICAL ANALYSIS - FAILED!")
                        print("You attempt to analyze the situation, but you're not a mage!")
                        print("Without magical training, you can't see the strategic opportunities.")
                        print("Your amateur attempt at tactics only wastes precious time while")
                        print("the creature positions itself for a better attack angle.")
                        print()
                        print("The beast takes advantage of your hesitation to strike first!")
                        print("💀 CLASS MISMATCH - TACTICS FAILED - YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                elif action_choice == "5":
                    print()
                    if player.weapon == dagger:
                        print("Your rogue training kicks in as you assess the situation in a split second.")
                        print("With supernatural grace, you spin on your heel and dart toward the shadows.")
                        print("The creature lunges after you, but you're already gone, melting into the darkness")
                        print("like smoke. Your nimble footwork and intimate knowledge of stealth paths")
                        print("allow you to slip past the beast's clumsy pursuit entirely.")
                        print("You emerge safely back at the village center, heart pounding but unharmed.")
                        current_scene = scenes.get("Primitive Village")
                        rogue_escaped_alley = True
                    else:
                        print("Panic floods your mind as you turn to flee from the massive creature.")
                        print("Unfortunately, your class training hasn't prepared you for this kind of escape.")
                        print("The beast is surprisingly fast for its size, and your heavy footfalls echo")
                        print("loudly in the narrow alley. You hear its thundering pursuit gaining ground.")
                        print()
                        print("THUD! The creature's massive club crashes down on your back.")
                        print("Pain explodes through your body as you're driven to the ground.")
                        print("The last thing you see is the creature standing over you, club raised high...")
                        print()
                        print("💀 YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                        print("The creature senses your fear and lack of confidence immediately.")
                        print("Your weapon doesn't match the intimidating presence of a true warrior.")
                        print("The beast's red eyes gleam with cruel amusement at your pathetic attempt.")
                        print()
                        print("Enraged by your weakness, the creature charges with doubled fury!")
                        print("Your failed intimidation has only made it more aggressive.")
                        print("The massive club swings toward your head with lethal intent...")
                        print()
                        print("💀 YOUR INTIMIDATION FAILED - YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                else:
                    print("Invalid option.")
                continue
        
        elif current_scene.name == "Armory":
            print()
            current_scene.enter(player)
            visited_scenes.add("Armory")
            if not visited_armory:
                print()
                print("You enter the ancient armory. Three enhanced weapons rest on pedestals, glowing with magical energy:")
                print("- The Shadow Blade (Enhanced Dagger) - wreathed in dark energy")
                print("- The Bone Crusher (Enhanced Axe) - radiating primal power") 
                print("- The Skull Scepter (Enhanced Wand) - pulsing with mystical force")
                print("In the corner, you notice a key labeled 'Town Key' on a small table.")
                visited_armory = True
            else:
                print()
                print("You're back in the armory. The weapons still glow on their pedestals.")
                if player.inventory.has_item("Town Key"):
                    print("The Town Key is no longer on the table since you already took it.")
                else:
                    print("The Town Key still sits on the small table.")
            
            # Track which weapons player has collected
            if not hasattr(player, 'collected_weapons'):
                player.collected_weapons = []
            
            print()
            print("What would you like to do?")
            print("1: Take the Shadow Blade (Enhanced Dagger)")
            print("2: Take the Bone Crusher (Enhanced Axe)")
            print("3: Take the Skull Scepter (Enhanced Wand)")
            print("4: Take the Town Key")
            print("5: Leave the armory")
            print("6: Quit")
            choice = input("Enter the number of your choice: ").strip().lower()
            
            if choice == "6" or choice == "quit":
                print()
                print("Thanks for playing!")
                break
            elif choice == "1":
                print()
                if enhanced_dagger in player.collected_weapons:
                    print("You already have the Shadow Blade.")
                else:
                    player.collected_weapons.append(enhanced_dagger)
                    print("You take the Shadow Blade! Its dark energy courses through you.")
                    print("The enhanced dagger joins your arsenal.")
            elif choice == "2":
                print()
                if enhanced_axe in player.collected_weapons:
                    print("You already have the Bone Crusher.")
                else:
                    player.collected_weapons.append(enhanced_axe)
                    print("You take the Bone Crusher! Its weight feels perfect in your hands.")
                    print("The enhanced axe joins your arsenal.")
            elif choice == "3":
                print()
                if enhanced_wand in player.collected_weapons:
                    print("You already have the Skull Scepter.")
                else:
                    player.collected_weapons.append(enhanced_wand)
                    print("You take the Skull Scepter! Mystical power flows through it.")
                    print("The enhanced wand joins your arsenal.")
            elif choice == "4":
                if player.inventory.has_item("Town Key"):
                    print("You already have the Town Key.")
                else:
                    from item import Item
                    town_key = Item("Town Key", "An ornate key that opens the Chief's House.")
                    player.inventory.add_item(town_key)
                    print("You take the Town Key. It feels warm to the touch.")
            elif choice == "5":
                print()
                print("You leave the armory and return to the village.")
                current_scene = scenes.get("Primitive Village")
            else:
                print("Invalid option.")
        
        elif current_scene.name == "Cave People Chief House":
            print()
            current_scene.enter(player)
            if not defeated_chief:
                print()
                print("You enter the imposing chief's house. The walls are adorned with trophies of past victories.")
                print("At the center sits the Chief—a massive, scarred warrior with piercing eyes and primitive armor.")
                print("He rises slowly, gripping a bone club, and speaks in a deep, rumbling voice:")
                print("'You dare enter my domain, outsider? Prove your worth or perish!'")
                print()
                print("The Chief blocks your path to the healing pool. You must fight!")
                print()
                
                # Use weapon selection system
                chosen_weapon = display_weapon_choices(player, "the Chief battle")
                
                if chosen_weapon == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                
                print()
                print(f"You raise your {chosen_weapon.name} and charge at the Chief!")
                
                # Check if player can defeat the chief with chosen weapon
                can_defeat_chief = False
                victory_message = ""
                
                # Enhanced weapons always work, but only if they match the player's class
                if chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]:
                    # Check if weapon matches player's starting class
                    player_class_weapon = None
                    if player.weapon == dagger:
                        player_class_weapon = enhanced_dagger
                    elif player.weapon == axe:
                        player_class_weapon = enhanced_axe
                    elif player.weapon == wand:
                        player_class_weapon = enhanced_wand
                    
                    if chosen_weapon == player_class_weapon:
                        # Correct class weapon - always succeeds
                        can_defeat_chief = True
                        if chosen_weapon == enhanced_dagger:
                            victory_message = (
                                f"As you grip the Shadow Blade, dark energy begins to course through the ancient metal. "
                                f"The blade starts glowing with an ominous purple light, shadows dancing along its edge. "
                                f"You move like liquid darkness, your enhanced dagger cutting through the air with supernatural speed. "
                                f"The Chief's eyes widen in recognition of the ancient power as the Shadow Blade finds its mark, "
                                f"piercing through his primitive armor as if it were cloth!"
                            )
                        elif player.weapon == enhanced_axe:
                            victory_message = (
                                f"The Bone Crusher begins to emit a deep, resonant hum as ancient power awakens within it. "
                                f"Carved runes along the bone handle start glowing with fierce red light. "
                                f"You raise the massive war axe high above your head, and it seems to move with a will of its own. "
                                f"When you bring it down, the very air splits with a thunderous crack. "
                                f"The Chief's bone club shatters like glass against the Bone Crusher's unstoppable force!"
                            )
                        elif player.weapon == enhanced_wand:
                            victory_message = (
                                f"The miniature skull atop your Skull Scepter begins to glow with eldritch fire, its eye sockets blazing. "
                                f"Mystical energy crackles around the wand, filling the air with the scent of ozone and ancient magic. "
                                f"You point the scepter at the Chief, and a beam of pure magical energy erupts forth, "
                                f"wreathed in spectral flames and accompanied by the whispers of long-dead sorcerers. "
                                f"The Chief's primitive defenses are utterly overwhelmed by the arcane assault!"
                            )
                    else:
                        # Wrong enhanced weapon for class
                        can_defeat_chief = False
                        weapon_name = chosen_weapon.name
                        if chosen_weapon == enhanced_dagger:
                            print(f"You attempt to wield the {weapon_name}, but you're not a rogue!")
                            print("Without proper dagger training, the Shadow Blade feels awkward and foreign in your hands.")
                        elif chosen_weapon == enhanced_axe:
                            print(f"You attempt to wield the {weapon_name}, but you're not a warrior!")
                            print("Without proper axe training, the Bone Crusher is too heavy and unwieldy for you.")
                        elif chosen_weapon == enhanced_wand:
                            print(f"You attempt to wield the {weapon_name}, but you're not a mage!")
                            print("Without magical training, the Skull Scepter's power remains dormant and useless.")
                        print("Your class mismatch is immediately apparent to the experienced Chief!")
                
                # Check default weapons with high stats
                elif chosen_weapon == dagger and hasattr(player, 'agility') and player.agility >= 8:
                    can_defeat_chief = True
                    victory_message = (
                        f"Your body moves with inhuman grace, agility honed to perfection through countless trials. "
                        f"Though your dagger appears simple, in your hands it becomes a blur of deadly precision. "
                        f"You dance around the Chief's massive swings, your footwork so swift it seems you're in three places at once. "
                        f"With lightning-fast strikes, you find every gap in his armor, each cut placed with surgical accuracy. "
                        f"Your mastery of speed and agility makes your humble dagger as deadly as any legendary blade!"
                    )
                elif chosen_weapon == axe and hasattr(player, 'strength') and player.strength >= 8:
                    can_defeat_chief = True
                    victory_message = (
                        f"Your muscles ripple with incredible power, strength forged through brutal combat and iron will. "
                        f"As you swing your axe, it moves with such devastating force that it seems to cut through the very air itself. "
                        f"The Chief's bone club meets your strike and simply disintegrates from the sheer impact. "
                        f"Your raw strength makes the heavy axe feel light as a feather, moving swift enough to seem like a dagger. "
                        f"With a final, earth-shaking blow, you demonstrate that pure strength can overcome any weapon!"
                    )
                elif chosen_weapon == wand and hasattr(player, 'intelligence') and player.intelligence >= 8:
                    can_defeat_chief = True
                    victory_message = (
                        f"Your mind burns with accumulated knowledge and mystical understanding beyond mortal comprehension. "
                        f"Though your wand appears ordinary, your enhanced intelligence transforms it into a conduit of pure magical force. "
                        f"You weave complex incantations with perfect precision, drawing power from the very fabric of reality. "
                        f"Arcane energies spiral around your simple wand, responding to your intellectual mastery of the magical arts. "
                        f"The Chief staggers as waves of perfectly controlled magical energy overwhelm his primitive defenses!"
                    )
                
                if can_defeat_chief:
                        print(victory_message)
                        print()
                        print("The Chief staggers backward, his eyes filled with a mixture of pain and profound respect.")
                        print("Blood trickles from his wounds as he slowly lowers his shattered weapon.")
                        print("'Impossible...' he gasps, his voice filled with awe. 'In all my years of battle, I have never...'")
                        print("He pauses, studying you with newfound reverence.")
                        print("'You fight not just with skill, but with the power of legends themselves!'")
                        print("'You have proven yourself worthy of the ancient secrets beyond. Go, champion.'")
                        print()
                        print("With a final, respectful bow, the mighty Chief steps aside, granting you passage.")
                        print("You feel the surge of power that comes from conquering a truly formidable foe!")
                        print()
                        print("You feel a surge of power as you level up!")
                        # Automatic level up with 3 attribute points
                        player.level += 1
                        if not hasattr(player, 'attribute_points'):
                            player.attribute_points = 0
                        player.attribute_points += 3
                        print(f"You gained 3 attribute points! Total: {player.attribute_points}")
                        handle_stat_allocation(player)
                        defeated_chief = True
                        print()
                        print("As the Chief's body hits the ground, a deep rumbling echoes through the chamber.")
                        print("Behind where the Chief stood, a heavy stone slab slowly grinds aside, revealing")
                        print("a hidden passageway. Ancient tribal markings glow faintly around the entrance,")
                        print("and you can hear the distant sound of flowing water from within.")
                        print("The path to the sacred healing chamber has been revealed!")
                        print()
                        print("What do you want to do?")
                        print("1: Enter the hidden passageway")
                        print("2: Exit the Chief's house")
                        print("3: Quit")
                        choice = input("Enter the number of your choice: ").strip().lower()
                        
                        if choice == "3" or choice == "quit":
                            print()
                            print("Thanks for playing!")
                            break
                        elif choice == "1":
                            next_scene = scenes.get("Healing Pool")
                            if next_scene:
                                current_scene = next_scene
                            else:
                                print("The passage leads into darkness...")
                        elif choice == "2":
                            current_scene = scenes.get("Primitive Village")
                        else:
                            print("Invalid option.")
                else:
                    # Weapon failed - either wrong class enhanced weapon or insufficient stats
                    print(f"You strike with your {chosen_weapon.name}, but it's not enough!")
                    print()
                    
                    # Give specific feedback based on weapon type and failure reason
                    if chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]:
                        # Wrong class enhanced weapon
                        print("Your class mismatch makes the weapon ineffective against the Chief!")
                        print("The Chief recognizes your lack of proper training immediately.")
                    elif chosen_weapon == dagger:
                        current_agility = getattr(player, 'agility', 5)
                        needed_agility = 8 - current_agility
                        print(f"Your dagger lacks the speed and precision needed. You need {needed_agility} more agility points or the right enhanced weapon!")
                    elif chosen_weapon == axe:
                        current_strength = getattr(player, 'strength', 5)
                        needed_strength = 8 - current_strength
                        print(f"Your axe lacks the crushing power needed. You need {needed_strength} more strength points or the right enhanced weapon!")
                    elif chosen_weapon == wand:
                        current_intelligence = getattr(player, 'intelligence', 5)
                        needed_intelligence = 8 - current_intelligence
                        print(f"Your wand lacks the magical force needed. You need {needed_intelligence} more intelligence points or the right enhanced weapon!")
                    else:
                        print("Your weapon is completely inadequate for this fight!")
                    
                    print()
                    print("The Chief's eyes blaze with fury at your pathetic attempt.")
                    print("'Foolish whelp!' he roars, his voice shaking the very walls of the hut.")
                    print("Before you can react, his massive bone club crashes down upon you.")
                    print()
                    print("CRACK! The sound of your bones breaking echoes through the chamber.")
                    print("You collapse to the ground, your vision blurring as crimson spreads beneath you.")
                    print("The Chief stands over your broken form, his shadow consuming what little light remains.")
                    print("'You came here unprepared and weak,' he growls, raising his club for the final blow.")
                    print()
                    print("The last thing you see is the bone club descending, then... darkness.")
                    print("Your adventure ends here, your body joining the countless trophies adorning his walls.")
                    print()
                    print("💀 YOU HAVE DIED 💀")
                    print()
                    
                    # Ask if player wants to restart
                    restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                    if restart_choice == "y" or restart_choice == "yes":
                        print()
                        print("=== RETURNING TO TITLE SCREEN ===")
                        print()
                        return  # Return to main loop which will show title screen
                    else:
                        print()
                        print("Thanks for playing!")
                        return
            else:
                print()
                print("You return to the Chief's house, but the atmosphere has completely changed.")
                print("Where once the imposing Chief ruled with an iron fist, now his lifeless body")
                print("lies sprawled across the floor, his massive bone club shattered beside him.")
                print("The trophies on the walls seem less menacing now, more like memorials to")
                print("a fallen warrior. The hidden passageway you revealed still stands open,")
                print("its ancient tribal markings glowing softly in the dim light.")
                print("The path to the sacred healing chamber remains accessible.")
                print()
                print("Where would you like to go?")
                print("1: Enter the Healing Pool")
                print("2: Return to the village")
                print("3: Quit")
                choice = input("Enter the number of your choice: ").strip().lower()
                
                if choice == "3" or choice == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                elif choice == "1":
                    next_scene = scenes.get("Healing Pool")
                    if next_scene:
                        current_scene = next_scene
                    else:
                        print("That exit doesn't lead anywhere.")
                elif choice == "2":
                    current_scene = scenes.get("Primitive Village")
                else:
                    print("Invalid option.")
        
        elif current_scene.name == "Primitive Village":
            if not visited_village:
                print()
                print("You step into the heart of the primitive village. Crude huts made of bone and hide cluster around a central fire pit, where embers glow and smoke drifts into the cavernous air. Strange symbols are painted on the rocks, and you hear the distant chatter of unseen creatures. Paths lead off in several directions: a shadowy alley, a fortified armory, and a large chief's house adorned with trophies.")
                visited_village = True
            
            print()
            print("Where would you like to go?")
            print("1: Enter the Alley (dangerous shadows)")
            print("2: Approach the Armory (locked chamber)")
            print("3: Visit the Chief's House (imposing hut)")
            print("4: Stay by the fire pit")
            print("5: Quit")
            choice = input("Enter the number of your choice: ").strip().lower()
            
            if choice == "5" or choice == "quit":
                print("Thanks for playing!")
                break
            elif choice == "1":
                next_scene = scenes.get("Alley")
                if next_scene:
                    current_scene = next_scene
                else:
                    print("That exit doesn't lead anywhere.")
            elif choice == "2":
                next_scene = scenes.get("Armory")
                if next_scene:
                    # Check if the scene is locked and if player has the key
                    if getattr(next_scene, 'locked', False):
                        key_name = getattr(next_scene, 'key', None)
                        if key_name and not hasattr(player.inventory, 'has_item'):
                            print()
                            print("The Armory is locked, but your inventory system does not support key checks.")
                            print("You're still in the village.")
                            continue
                        elif key_name and not player.inventory.has_item(key_name):
                            print()
                            print("You approach the Armory, but the door is locked. You need the Armory Key to enter.")
                            print("You're still in the village.")
                            continue
                    current_scene = next_scene
                else:
                    print("That exit doesn't lead anywhere.")
            elif choice == "3":
                next_scene = scenes.get("Cave People Chief House")
                if next_scene:
                    # Check if the scene is locked and if player has the key
                    if getattr(next_scene, 'locked', False):
                        key_name = getattr(next_scene, 'key', None)
                        if key_name and not hasattr(player.inventory, 'has_item'):
                            print()
                            print("The Chief's House is locked, but your inventory system does not support key checks.")
                            print("You're still in the village.")
                            continue
                        elif key_name and not player.inventory.has_item(key_name):
                            print()
                            print("You approach the Chief's House, but the door is locked and the chief glares at you. You need the Town Key to enter.")
                            print("You're still in the village.")
                            continue
                    current_scene = next_scene
                else:
                    print("That exit doesn't lead anywhere.")
            elif choice == "4":
                print()
                print("You linger by the fire pit, feeling the warmth and watching the shadows dance. The village seems to hold its breath, waiting for your next move.")
            else:
                print("Invalid option.")
        
        elif current_scene.name == "Healing Pool":
            print()
            if "Healing Pool" not in visited_scenes:
                current_scene.enter(player)
                visited_scenes.add("Healing Pool")
                print()
                print("You emerge into a sacred chamber that takes your breath away.")
                print("The walls are adorned with primitive paintings depicting ancient rituals and spiritual")
                print("ceremonies. Carved bone totems hang from the ceiling, swaying gently in an unfelt breeze.")
                print("At the center lies a magnificent natural pool, its waters glowing with an otherworldly")
                print("blue-green light. Steam rises from the surface, carrying the scent of healing herbs")
                print("and mystical energies. Smooth river stones line the pool's edge, worn smooth by")
                print("countless generations of tribal ceremonies.")
                print()
                print("Ancient tribal markings circle the pool, pulsing with the same ethereal glow.")
                print("This is clearly a place of great spiritual significance—a sacred bath where")
                print("warriors have sought divine blessing for millennia.")
            else:
                print("You return to the sacred healing chamber.")
                print("The mystical pool continues to glow with ancient power, its warm waters")
                print("beckoning you to partake in the ritual blessing.")
            
            print()
            print("What would you like to do?")
            print("1: Enter the sacred waters and take a ritual soak")
            print("2: Return to the Chief's house")
            print("3: Quit")
            choice = input("Enter the number of your choice: ").strip().lower()
            
            if choice == "3" or choice == "quit":
                print()
                print("Thanks for playing!")
                break
            elif choice == "1":
                # Confirmation prompt for taking the soak
                print()
                print("You approach the glowing waters. The ancient power emanating from the pool")
                print("is overwhelming. You sense that entering these sacred waters will trigger")
                print("something irreversible - an awakening that will change everything.")
                print()
                while True:
                    confirm = input("ARE YOU SURE? (y/n): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        print()
                        print("You steel yourself and step into the mystical waters...")
                        print()
                        print("You reverently remove your equipment and step into the warm, glowing waters.")
                        print("Immediately, you feel ancient magic coursing through your body. The tribal")
                        print("markings around the pool flare with brilliant light as the sacred ritual begins.")
                        print("Mystical energies flow through the water, penetrating deep into your soul.")
                        print()
                        print("The water seems to sing with the voices of ancient spirits, welcoming you")
                        print("as a worthy warrior. Your muscles feel renewed, your mind sharpened, and")
                        print("your spirit fortified with primordial power. The blessing of the ancestors")
                        print("now flows through your veins!")
                        print()
                        print("As you emerge from the sacred bath, you feel fundamentally changed.")
                        print("Your body radiates with divine energy, and you know that you have been")
                        print("blessed with the power necessary to face whatever ancient evil awaits ahead.")
                        print()
                        player.sacred_blessing = True
                        print("🌟 You have received the Sacred Blessing! 🌟")
                        print()
                        print("Suddenly, the pool begins to glow even more intensely...")
                        print("The blessing has awakened something ANCIENT and TERRIBLE!")
                        print("The chamber begins to shake violently as hidden mechanisms activate!")
                        print()
                        print("The ground splits open beneath you as you're pulled into the final confrontation...")
                        # Immediately transition to final boss
                        next_scene = scenes.get("Primitive Village Changed")
                        if next_scene:
                            current_scene = next_scene
                            break
                    elif confirm in ['n', 'no']:
                        print()
                        print("You step back from the pool, deciding to wait a moment longer.")
                        print("The ancient waters continue to glow, patient and eternal.")
                        break
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                
                # If they confirmed, we've already changed scene and broken out of the loop
                # If they didn't confirm, continue with the healing pool loop
            elif choice == "2":
                current_scene = scenes.get("Cave People Chief House")
            else:
                print("Invalid option.")
        
        elif current_scene.name == "Primitive Village Changed":
            # This scene only triggers after receiving the sacred blessing
            if not hasattr(player, 'sacred_blessing'):
                print()
                print("You cannot access this area without the sacred blessing.")
                current_scene = scenes.get("Healing Pool")
                continue
            
            print()
            print("🌟 THE AWAKENING 🌟")
            print()
            print("As you step out of the healing pool chamber, the sacred blessing coursing through")
            print("your veins suddenly resonates with something far more ancient and powerful.")
            print("The very walls around you begin to SHAKE violently!")
            print()
            print("CRACK! CRACK! CRACK!")
            print()
            print("Massive fissures tear through the stone as you run through the Chief's house,")
            print("desperately trying to escape the collapsing passages. Dust and debris rain")
            print("down as you burst into the village center, gasping for breath.")
            print()
            print("But what you see next defies all comprehension...")
            print()
            print("🏛️ THE TERRIBLE TRUTH REVEALED 🏛️")
            print()
            print("As sections of the cave system collapse around you, the horrifying reality")
            print("becomes clear. The 'cave' you've been exploring... IT'S NOT A CAVE AT ALL!")
            print()
            print("Through the massive cracks in the stone, you can see RIBS - colossal, ancient")
            print("ribs that stretch up into the darkness like the pillars of a cathedral.")
            print("The 'tunnels' you walked through were ARTERIES. The 'chambers' were ORGANS.")
            print("The skull chamber with its glowing eyes... that was the DORMANT HEAD of this")
            print("titanic corpse!")
            print()
            print("You have been crawling through the fossilized remains of an IMMORTAL GOD,")
            print("a being so massive that entire civilizations built their homes within its")
            print("decomposing body. The cave people weren't just primitive tribes - they were")
            print("the guardians of this cosmic graveyard, keeping watch over divine remains!")
            print()
            print("The sacred blessing you received... it was meant to WAKE IT UP!")
            print()
            print("💀 THE DIVINE HEART AWAKENS 💀")
            print()
            print("BOOM! BOOM! BOOM!")
            print()
            print("The ground beneath you splits open like a massive wound, revealing a pulsating")
            print("chasm that descends into the very core of the divine corpse. From the depths")
            print("rises something beyond mortal comprehension - THE HEART OF THE IMMORTAL GOD!")
            print()
            print("A colossal, beating organ the size of a cathedral emerges from the abyss,")
            print("its surface covered in writhing veins that glow with malevolent energy.")
            print("Ancient symbols carved into its flesh pulse with each thunderous heartbeat.")
            print("Tendrils of corrupted blood and divine ichor spray in all directions as")
            print("the awakened heart prepares to reclaim its domain!")
            print()
            print("🔥 FINAL BOSS BATTLE: THE DIVINE HEART 🔥")
            print()
            print("The massive organ turns its attention to you, recognizing you as the one")
            print("who dared to awaken it from eternal slumber. Waves of pure malice wash")
            print("over you as it prepares to crush this insignificant mortal!")
            print()
            print("This is your final test. Only a warrior who can combine BOTH legendary")
            print("weapon mastery AND their class's ultimate technique can hope to defeat this god!")
            print()
            
            # Initialize battle tracking variables
            if not hasattr(player, 'used_weapon_attack'):
                player.used_weapon_attack = False
            if not hasattr(player, 'used_class_ability'):
                player.used_class_ability = False
            
            # Check player's readiness for final boss
            main_stat = 0
            stat_name = ""
            enhanced_weapon_equipped = False
            
            if player.weapon == enhanced_dagger:
                main_stat = getattr(player, 'agility', 5)
                stat_name = "agility"
                enhanced_weapon_equipped = True
            elif player.weapon == enhanced_axe:
                main_stat = getattr(player, 'strength', 5)
                stat_name = "strength"
                enhanced_weapon_equipped = True
            elif player.weapon == enhanced_wand:
                main_stat = getattr(player, 'intelligence', 5)
                stat_name = "intelligence"
                enhanced_weapon_equipped = True
            
            vitality = getattr(player, 'vitality', 5)
            total_combat_readiness = main_stat + vitality - 10  # Starting stats were 5 each, so subtract base
            
            # Show battle status
            if player.used_weapon_attack and player.used_class_ability:
                print("💥 ULTIMATE COMBO ACHIEVED! 💥")
                print()
                print("You have successfully combined your enhanced weapon mastery with your")
                print("class's legendary technique! The Divine Heart staggers under your")
                print("perfectly executed dual assault!")
                print()
                print("CRACK! CRACK! CRACK!")
                print()
                print("Your legendary combination tears through the Divine Heart's defenses!")
                print("Divine ichor sprays like golden rain as the cosmic organ staggers.")
                print("The Heart's beating becomes erratic, its ancient power finally failing.")
                print()
                print("'IMPOSSIBLE...' the divine voice whispers, filled with shock and respect.")
                print("'A MORTAL... HAS ACHIEVED... LEGENDARY STATUS... THROUGH PERFECT TECHNIQUE...'")
                print()
                print("With a final, earth-shaking convulsion, the Divine Heart collapses!")
                print("The awakened god's consciousness fades back into eternal slumber,")
                print("its cosmic power spent. You stand victorious over divine remains!")
                print()
                print("🏆 PERFECT LEGENDARY VICTORY ACHIEVED! 🏆")
                print()
                print("You have slain an immortal god through masterful combination of")
                print("enhanced weaponry and ultimate class techniques!")
                print("Your name will be whispered in legend for all eternity!")
                print()
                print("🎮 CONGRATULATIONS! YOU HAVE COMPLETED THE CAVE GAME! 🎮")
                break
            else:
                # Show what's been attempted
                if player.used_weapon_attack:
                    print("✅ Enhanced Weapon Attack: SUCCESSFUL")
                    print("The Divine Heart reels from your legendary weapon strike!")
                    print("But it's not enough alone...")
                    print()
                if player.used_class_ability:
                    print("✅ Class Special Ability: SUCCESSFUL") 
                    print("Your class technique wounds the cosmic entity!")
                    print("But more is needed to finish it...")
                    print()
                
                print("How do you choose to face this cosmic horror?")
                print(f"1: Choose weapon to attack with" + (" (✅ COMPLETED)" if player.used_weapon_attack else ""))
                print(f"2: Shadow Strike (Rogue special ability)" + (" (✅ COMPLETED)" if player.used_class_ability else ""))
                print(f"3: Berserker Rage (Warrior special ability)" + (" (✅ COMPLETED)" if player.used_class_ability else ""))
                print(f"4: Strategize (Mage special ability)" + (" (✅ COMPLETED)" if player.used_class_ability else ""))
                
                option_num = 5
                
                print(f"{option_num}: Attempt to flee")
                flee_option = option_num
                option_num += 1
                print(f"{option_num}: Quit")
                quit_option = option_num
                
                choice = input("Enter the number of your choice: ").strip().lower()
                
                if choice == str(quit_option) or choice == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                elif choice == str(flee_option):
                    print()
                    print("You turn to flee from this cosmic nightmare, but there is nowhere to run!")
                    print("The collapsing divine corpse has sealed all exits. You must face your destiny!")
                    print("The Divine Heart pulses with dark amusement at your cowardice.")
                    continue
                elif choice == "1":
                    if player.used_weapon_attack:
                        print()
                        print("You have already used your enhanced weapon attack!")
                        print("Try your class special ability instead.")
                        continue
                    
                    print()
                    # Use weapon selection system for final boss
                    chosen_weapon = display_weapon_choices(player, "the Divine Heart battle")
                    
                    if chosen_weapon == "quit":
                        print()
                        print("Thanks for playing!")
                        break
                    
                    print()
                    print(f"You raise your {chosen_weapon.name} and charge at the Divine Heart!")
                    print()
                    
                    # Check if player meets requirements for weapon attack
                    enhanced_weapon_equipped = chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
                    
                    # Determine main stat based on chosen weapon
                    main_stat = 0
                    stat_name = ""
                    if chosen_weapon == enhanced_dagger:
                        main_stat = getattr(player, 'agility', 5)
                        stat_name = "agility"
                    elif chosen_weapon == enhanced_axe:
                        main_stat = getattr(player, 'strength', 5)
                        stat_name = "strength"
                    elif chosen_weapon == enhanced_wand:
                        main_stat = getattr(player, 'intelligence', 5)
                        stat_name = "intelligence"
                    elif chosen_weapon == dagger:
                        main_stat = getattr(player, 'agility', 5)
                        stat_name = "agility"
                    elif chosen_weapon == axe:
                        main_stat = getattr(player, 'strength', 5)
                        stat_name = "strength"
                    elif chosen_weapon == wand:
                        main_stat = getattr(player, 'intelligence', 5)
                        stat_name = "intelligence"
                    
                    vitality = getattr(player, 'vitality', 5)
                    total_combat_readiness = main_stat + vitality - 10  # Starting stats were 5 each, so subtract base
                    
                    if enhanced_weapon_equipped and total_combat_readiness >= 5:
                        player.used_weapon_attack = True
                        if chosen_weapon == enhanced_dagger:
                            print(f"The Shadow Blade erupts with dark energy as you channel every ounce of your ")
                            print(f"legendary agility ({main_stat}) and hardened vitality ({vitality}) into this strike! ")
                            print("You move like living darkness, dancing between the Heart's massive tendrils.")
                            print("Your enhanced blade cuts through divine flesh like silk, each strike guided by")
                            print("perfect technique honed through countless battles. The Shadow Blade drinks deeply")
                            print("of the god's ichor, growing brighter with each wound!")
                        elif chosen_weapon == enhanced_axe:
                            print(f"The Bone Crusher resonates with your incredible strength ({main_stat}) and battle-hardened ")
                            print(f"vitality ({vitality}) as you unleash a devastating assault! Each swing of your enhanced ")
                            print("axe cleaves through the Heart's protective veins with earth-shattering force.")
                            print("The ancient weapon sings with joy as it tastes divine blood, its bone construction")
                            print("perfectly suited to wound this cosmic entity!")
                        elif chosen_weapon == enhanced_wand:
                            print(f"The Skull Scepter channels your vast intelligence ({main_stat}) and resilient vitality ({vitality}) ")
                            print("into a torrent of arcane destruction! Waves of pure magical energy cascade from your")
                            print("enhanced wand, each spell perfectly calculated to exploit the Heart's vulnerabilities.")
                            print("The scepter's skull glows white-hot as it unleashes millennia of stored magical power!")
                        
                        print()
                        print("🗡️ ENHANCED WEAPON ATTACK SUCCESSFUL! 🗡️")
                        print("The Divine Heart staggers but is not yet defeated!")
                        continue
                    else:
                        # Player doesn't meet weapon requirements - DEATH
                        defeat_message = ""
                        if not enhanced_weapon_equipped:
                            defeat_message = f"Your {chosen_weapon.name} shatters like glass against the Divine Heart's cosmic flesh!"
                        elif total_combat_readiness < 5:
                            needed_points = 5 - total_combat_readiness
                            defeat_message = (f"You lack the combat mastery needed! You need {needed_points} more points "
                                            f"in {stat_name} or vitality to match this cosmic threat!")
                        
                        print(defeat_message)
                        print()
                        print("The Divine Heart's tendrils wrap around you like cosmic chains, lifting you")
                        print("high into the air. Its pulsing surface opens to reveal rows of god-teeth,")
                        print("each one larger than your entire body.")
                        print()
                        print("'FOOLISH MORTAL,' booms a voice that shakes reality itself.")
                        print("'YOU DARE CHALLENGE A GOD WITH SUCH PITIFUL PREPARATION?'")
                        print()
                        print("The Heart crushes you between its massive valves, your inadequate power")
                        print("meaning nothing against divine wrath. Your bones turn to dust as cosmic")
                        print("pressure overwhelms your mortal form.")
                        print()
                        print("💀 YOU HAVE BEEN DEVOURED BY A GOD 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return  # Return to main loop which will show title screen
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                
                elif choice == "2":  # Shadow Strike - available to all, but only works for rogues
                    if player.used_class_ability:
                        print()
                        print("You have already used your class special ability!")
                        print("Try your enhanced weapon attack instead.")
                        continue
                    
                    print()
                    if player.weapon in [dagger, enhanced_dagger]:  # Correct class
                        # Rogue Shadow Strike
                        agility_stat = getattr(player, 'agility', 5)
                        enhanced_weapon_equipped = player.weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
                        vitality = getattr(player, 'vitality', 5)
                        total_combat_readiness = agility_stat + vitality - 10
                        
                        if agility_stat >= 8 and enhanced_weapon_equipped and total_combat_readiness >= 5:
                            player.used_class_ability = True
                            print("SHADOW STRIKE EXECUTED!")
                            print()
                            print(f"Your legendary agility ({agility_stat}) combines with your enhanced weapon's dark power!")
                            print("You become one with the shadows, moving faster than divine perception.")
                            print("Appearing behind the Heart's blind spot, you drive your enhanced blade")
                            player.used_class_ability = True
                            print("BERSERKER RAGE ACTIVATED!")
                            print()
                            print(f"Your incredible strength ({strength_stat}) erupts in divine fury!")
                            print("The Bone Crusher becomes an extension of your will as berserker rage")
                            print("overtakes your mind. You become an unstoppable force of destruction,")
                            print("each blow landing with the force of a falling mountain!")
                            print()
                            print("� WARRIOR SPECIAL ABILITY SUCCESSFUL! �")
                            print("The Divine Heart recoils from your legendary berserker assault!")
                            continue
                        else:
                            print("Your Shadow Strike fails! You need legendary agility (8+), an enhanced weapon,")
                            print("and sufficient combat preparation to execute this technique against a god!")
                            print()
                            print("The Heart's tendrils slam you to the ground with crushing force!")
                            print("Your inadequate rogue skills mean nothing against divine power!")
                            print()
                            print("💀 YOUR SHADOW TECHNIQUE HAS FAILED - YOU HAVE DIED 💀")
                            print()
                            restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                            if restart_choice == "y" or restart_choice == "yes":
                                print()
                                print("=== RETURNING TO TITLE SCREEN ===")
                                print()
                                return
                            else:
                                print()
                                print("Thanks for playing!")
                                return
                    else:
                        # Wrong class attempting Shadow Strike
                        print("You attempt to use Shadow Strike, but you're not a rogue!")
                        print("Without rogue training, your attempt is pathetically inadequate.")
                        print("The Divine Heart recognizes your class mismatch immediately.")
                        print()
                        print("'FOOLISH PRETENDER!' the god thunders with contempt.")
                        print("'YOU DARE ATTEMPT SHADOW STRIKE WITHOUT ROGUE MASTERY?'")
                        print()
                        print("Divine wrath crushes you for your presumption!")
                        print()
                        print("💀 CLASS MISMATCH - YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                
                elif choice == "3":  # Berserker Rage - available to all, but only works for warriors
                    if player.used_class_ability:
                        print()
                        print("You have already used your class special ability!")
                        print("Try your enhanced weapon attack instead.")
                        continue
                    
                    print()
                    if player.weapon in [axe, enhanced_axe]:  # Correct class
                        # Warrior Berserker Rage
                        strength_stat = getattr(player, 'strength', 5)
                        enhanced_weapon_equipped = player.weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
                        vitality = getattr(player, 'vitality', 5)
                        total_combat_readiness = strength_stat + vitality - 10
                        
                        if strength_stat >= 8 and enhanced_weapon_equipped and total_combat_readiness >= 5:
                            print("directly into its core in a perfect assassination technique!")
                            print()
                            print("� ROGUE SPECIAL ABILITY SUCCESSFUL! �")
                            print("The Divine Heart writhes in agony from your perfect stealth attack!")
                            continue
                        else:
                            print("Your Berserker Rage fails! You need legendary strength (8+), an enhanced weapon,")
                            print("and sufficient combat preparation to channel this divine fury!")
                            print()
                            print("The Heart's massive tendrils crush your inadequate warrior spirit!")
                            print("Your false rage crumbles before true divine wrath!")
                            print()
                            print("💀 YOUR BERSERKER RAGE HAS FAILED - YOU HAVE DIED 💀")
                            print()
                            restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                            if restart_choice == "y" or restart_choice == "yes":
                                print()
                                print("=== RETURNING TO TITLE SCREEN ===")
                                print()
                                return  # Return to main loop which will show title screen
                            else:
                                print()
                                print("Thanks for playing!")
                                return
                    else:
                        # Wrong class attempting Berserker Rage
                        print("You attempt to use Berserker Rage, but you're not a warrior!")
                        print("Without warrior training, your attempt is pathetically inadequate.")
                        print("The Divine Heart recognizes your class mismatch immediately.")
                        print()
                        print("'FOOLISH PRETENDER!' the god thunders with contempt.")
                        print("'YOU DARE ATTEMPT BERSERKER RAGE WITHOUT WARRIOR MASTERY?'")
                        print()
                        print("Divine wrath crushes you for your presumption!")
                        print()
                        print("💀 CLASS MISMATCH - YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                        # Warrior Berserker Rage
                        strength_stat = getattr(player, 'strength', 5)
                        if strength_stat >= 8 and enhanced_weapon_equipped and total_combat_readiness >= 5:
                            player.used_class_ability = True
                            print("BERSERKER RAGE ACTIVATED!")
                            print()
                            print(f"Your incredible strength ({strength_stat}) erupts in divine fury!")
                            print("The Bone Crusher becomes an extension of your will as berserker rage")
                            print("overtakes your mind. You become an unstoppable force of destruction,")
                            print("each blow landing with the force of a falling mountain!")
                            print()
                            print("🔥 WARRIOR SPECIAL ABILITY SUCCESSFUL! 🔥")
                            print("The Divine Heart recoils from your legendary berserker assault!")
                            continue
                        else:
                            print("Your Berserker Rage fails! You need legendary strength (8+), an enhanced weapon,")
                            print("and sufficient combat preparation to channel this divine fury!")
                            print()
                            print("The Heart's massive tendrils crush your inadequate warrior spirit!")
                            print("Your false rage crumbles before true divine wrath!")
                            print()
                            print("💀 YOUR BERSERKER RAGE HAS FAILED - YOU HAVE DIED 💀")
                            print()
                            restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                            if restart_choice == "y" or restart_choice == "yes":
                                print()
                                print("=== RETURNING TO TITLE SCREEN ===")
                                print()
                                return  # Return to main loop which will show title screen
                            else:
                                print()
                                print("Thanks for playing!")
                                return
                
                elif choice == "4":  # Strategize - available to all, but only works for mages
                    if player.used_class_ability:
                        print()
                        print("You have already used your class special ability!")
                        print("Try your enhanced weapon attack instead.")
                        continue
                    
                    print()
                    if player.weapon in [wand, enhanced_wand]:  # Correct class
                        # Mage Strategize
                        intelligence_stat = getattr(player, 'intelligence', 5)
                        enhanced_weapon_equipped = player.weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
                        vitality = getattr(player, 'vitality', 5)
                        total_combat_readiness = intelligence_stat + vitality - 10
                        
                        if intelligence_stat >= 8 and enhanced_weapon_equipped and total_combat_readiness >= 5:
                            player.used_class_ability = True
                            print("STRATEGIC MASTERSTROKE EXECUTED!")
                            print()
                            print(f"Your brilliant intelligence ({intelligence_stat}) reveals the perfect strategy!")
                            print("Above the Divine Heart hangs a massive stalactite, precariously balanced")
                            print("from the cave collapse. Your Skull Scepter channels precise magical force")
                            print("to shatter the stone's support points at exactly the right moment!")
                            print()
                            print("CRASH! The colossal boulder plummets down, piercing straight through")
                            print("the Heart's center like a divine spear!")
                            print()
                            print("🧠 MAGE SPECIAL ABILITY SUCCESSFUL! 🧠")
                            print("Your tactical genius has wounded the cosmic entity!")
                            continue
                        else:
                            print("Your strategy fails! You need legendary intelligence (8+), an enhanced weapon,")
                            print("and sufficient combat preparation to outthink a divine entity!")
                            print()
                            print("The Heart's cosmic intelligence overwhelms your puny mortal mind!")
                            print("Your feeble strategy crumbles before divine omniscience!")
                            print()
                            print("💀 YOUR STRATEGIC MIND HAS FAILED - YOU HAVE DIED 💀")
                            print()
                            restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                            if restart_choice == "y" or restart_choice == "yes":
                                print()
                                print("=== RETURNING TO TITLE SCREEN ===")
                                print()
                                return
                            else:
                                print()
                                print("Thanks for playing!")
                                return
                    else:
                        # Wrong class attempting Strategize
                        print("You attempt to use Strategize, but you're not a mage!")
                        print("Without magical training, your attempt is pathetically inadequate.")
                        print("The Divine Heart recognizes your class mismatch immediately.")
                        print()
                        print("'FOOLISH PRETENDER!' the god thunders with contempt.")
                        print("'YOU DARE ATTEMPT STRATEGIZE WITHOUT MAGE MASTERY?'")
                        print()
                        print("Divine wrath crushes you for your presumption!")
                        print()
                        print("💀 CLASS MISMATCH - YOU HAVE DIED 💀")
                        print()
                        restart_choice = input("Would you like to play again? (y/n): ").strip().lower()
                        if restart_choice == "y" or restart_choice == "yes":
                            print()
                            print("=== RETURNING TO TITLE SCREEN ===")
                            print()
                            return
                        else:
                            print()
                            print("Thanks for playing!")
                            return
                else:
                    print("Invalid option.")
        
        else:
            print()
            current_scene.enter(player)
            print()
            print("Exits:", ', '.join(current_scene.exits.keys()))
            cmd = input("Where do you want to go? (or 'quit'): ").strip().lower()
            
            if cmd == "quit":
                print()
                print("Thanks for playing!")
                break
            if cmd in current_scene.exits:
                next_scene_name = current_scene.exits[cmd]
                next_scene = scenes.get(next_scene_name)
                if next_scene:
                    current_scene = next_scene
                else:
                    print("That exit doesn't lead anywhere.")
            else:
                print("Invalid direction.")

if __name__ == "__main__":
    main()

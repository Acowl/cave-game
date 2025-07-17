
from player import Player
from player import Scene
from item import Inventory, dagger, axe, wand
from enemy import Enemy, gain_experience, allocate_attribute

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

def main():
    player = Player()
    player.inventory = Inventory()
    print()
    print("SHABUYA")
    print("Choose your class:")
    print("1: Rogue")
    print("2: Warrior")
    print("3: Mage")
    class_choice = input("Enter the number of your class: ").strip()
    if class_choice == "1":
        player.weapon = dagger
        print("You are a Rogue. You start with a Dagger.")
    elif class_choice == "2":
        player.weapon = axe
        print("You are a Warrior. You start with an Axe.")
    elif class_choice == "3":
        player.weapon = wand
        print("You are a Mage. You start with a Wand.")
    else:
        print("Invalid choice. Defaulting to Rogue.")
        player.weapon = dagger
        print("You are a Rogue. You start with a Dagger.")
    scenes = setup_scenes()
    current_scene = scenes["Cave Entrance"]
    visited_village = False
    rogue_escaped_alley = False
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
                print("Type 'quit' to exit.")
                choice = input("Choose an option: ").strip().lower()
                if choice == "quit":
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
        elif current_scene.name == "Alley":
            print()
            if rogue_escaped_alley and player.weapon == dagger:
                print("You return to the alley, now aware of the lurking enemy. You have the chance to sneak up and ambush it.")
                print()
                print("What do you do?")
                print("1: Sneak up and ambush the creature")
                print("2: Return to the village")
                print("Type 'quit' to exit.")
                choice = input("Choose an option: ").strip().lower()
                if choice == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                elif choice == "1":
                    print()
                    print("You move silently through the shadows and ambush the creature. It never saw you coming and is slain instantly.")
                    print("You feel a surge of power as you level up!")
                    player.level_up()
                    if hasattr(player, 'attribute_points') and player.attribute_points >= 3:
                        print("Allocate your 3 stat points:")
                        for i in range(3):
                            print(f"Point {i+1} - Choose: vitality, agility, strength, intelligence")
                            stat = input("Attribute: ").strip().lower()
                            from enemy import allocate_attribute
                            allocate_attribute(player, stat)
                    print()
                    loot_choice = input("Would you like to loot the corpse? (y/n): ").strip().lower()
                    if loot_choice == "y":
                        print("You search the corpse and find a rusty key labeled 'Armory Key'.")
                        from item import Item
                        armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                        player.inventory.add_item(armory_key)
                    else:
                        print("You leave the corpse untouched and return to the village.")
                    print()
                    print("You return to the village, emboldened by your victory.")
                    current_scene = scenes.get("Primitive Village")
                elif choice == "2":
                    print()
                    print("You decide not to risk it and return to the village.")
                    current_scene = scenes.get("Primitive Village")
                else:
                    print("Invalid option.")
            else:
                print("You step into the alley. The shadows seem to move, and suddenly a primitive ground-dwelling creature emerges from a burrow. Its skin is mottled and tough, eyes glinting with hunger. It blocks your path, brandishing a crude club and snarling.")
                print()
                print("What do you do?")
                print(f"1: Attack with your {player.weapon.name}")
                print("2: Run away")
                print("3: Try to intimidate the creature")
                print("Type 'quit' to exit.")
                choice = input("Choose an option: ").strip().lower()
                if choice == "quit":
                    print()
                    print("Thanks for playing!")
                    break
                elif choice == "1":
                    print()
                    print(f"You lunge forward and attack with your {player.weapon.name}!")
                    print("The creature is caught off guard and is slain by your swift strike.")
                    print()
                    print("You feel a surge of power as you level up!")
                    player.level_up()
                    if hasattr(player, 'attribute_points') and player.attribute_points >= 3:
                        print("Allocate your 3 stat points:")
                        for i in range(3):
                            print(f"Point {i+1} - Choose: vitality, agility, strength, intelligence")
                            stat = input("Attribute: ").strip().lower()
                            from enemy import allocate_attribute
                            allocate_attribute(player, stat)
                    print()
                    loot_choice = input("Would you like to loot the corpse? (y/n): ").strip().lower()
                    if loot_choice == "y":
                        print("You search the corpse and find a rusty key labeled 'Armory Key'.")
                        from item import Item
                        armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                        player.inventory.add_item(armory_key)
                    else:
                        print("You leave the corpse untouched and return to the village.")
                    print()
                    print("You return to the village, emboldened by your victory.")
                    current_scene = scenes.get("Primitive Village")
                elif choice == "2":
                    print()
                    if player.weapon == dagger:
                        print("With nimble agility, you dart past the creature, evading its grasp and slipping through the shadows. As a Rogue, you safely return to the village center, unseen and unscathed.")
                        current_scene = scenes.get("Primitive Village")
                        rogue_escaped_alley = True
                    else:
                        print("You try to run, but the creature is faster than you expected. It catches you and you meet a swift end.")
                        print("GAME OVER.")
                        return
                elif choice == "3":
                    print()
                    if player.weapon == axe:
                        print("You brandish your axe and roar with authority. The creature cowers, drops a rusty key labeled 'Armory Key', and flees into its burrow!")
                        from item import Item
                        armory_key = Item("Armory Key", "A rusty key that opens the armory.")
                        player.inventory.add_item(armory_key)
                        print("You return to the village, having asserted your dominance.")
                        current_scene = scenes.get("Primitive Village")
                    else:
                        print("You try to intimidate the creature, but it is unfazed. It attacks and you meet a swift end.")
                        print("GAME OVER.")
                        return
                else:
                    print("Invalid option.")
                continue
            print()
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
            print("Type 'quit' to exit.")
            choice = input("Choose an option: ").strip().lower()
            if choice == "quit":
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



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
    play_choice = ""
    while play_choice not in ["y", "n"]:
        print()
        play_choice = input("Would you like to play?  (Y)es or (N)? ").strip().lower()
        if play_choice not in ["y", "n"]:
            print("Please enter 'Y' or 'N'.")
    if play_choice == "n":
        print("Maybe next time!")
        return
    print()
    print("Choose your class:")
    print("1: Rogue")
    print("2: Warrior")
    print("3: Mage")
    class_choice = ""
    while class_choice not in ["1", "2", "3"]:
        class_choice = input().strip()
        if class_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
    if class_choice == "1":
        player.weapon = dagger
        print()
        print("You are a Rogue. You start with a Dagger.")
    elif class_choice == "2":
        player.weapon = axe
        print()
        print("You are a Warrior. You start with an Axe.")
    elif class_choice == "3":
        player.weapon = wand
        print()
        print("You are a Mage. You start with a Wand.")
    scenes = setup_scenes()
    current_scene = scenes["Cave Entrance"]
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
        elif current_scene.name == "Skull Chamber":
            print()
            current_scene.enter(player)
            print()
            print("You see a distant figure scurry away among the shadows near the giant skull.")
            print("Would you like to chase after it?")
            print("1: Yes")
            print("2: No")
            print("Type 'quit' to exit.")
            chase_choice = input("Choose an option: ").strip().lower()
            if chase_choice == "quit":
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
                # Restrict exits to only 'forward'
                current_scene.exits = {"forward": "Primitive Village"}
                while True:
                    print()
                    print("You can only move forward now.")
                    print("1: Move forward")
                    print("Type 'quit' to exit.")
                    cmd = input("Choose an option: ").strip().lower()
                    if cmd == "quit":
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
        elif current_scene.name == "Primitive Village":
            print()
            print("You step into the heart of the primitive village. Crude huts made of bone and hide cluster around a central fire pit, where embers glow and smoke drifts into the cavernous air. Strange symbols are painted on the rocks, and you hear the distant chatter of unseen creatures. Paths lead off in several directions: a shadowy alley, a fortified armory, and a large chief's house adorned with trophies.")
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
                    current_scene = next_scene
                else:
                    print("That exit doesn't lead anywhere.")
            elif choice == "3":
                next_scene = scenes.get("Cave People Chief House")
                if next_scene:
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


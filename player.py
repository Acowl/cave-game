# player.py
class Player:
    def __init__(self):
        self.health = 100
        self.strength = 5
        self.intelligence = 5
        self.agility = 5
        self.level = 1
        self.inventory = []
        self.weapon = None
    
    def level_up(self):
        self.level += 1
        print("You leveled up! Choose an attribute to increase.")
        # logic for increasing attributes

    def attack(self):
        # damage = base + scaling
        pass

# scene.py
class Scene:
    def __init__(self, name, description, exits, locked=False, key=None):
        self.name = name
        self.description = description
        self.exits = exits  # e.g., {'north': 'Engineering Bay'}
        self.locked = locked
        self.key = key  # name of key that unlocks

    def enter(self, player):
        if self.locked and not player.inventory.has_item(self.key):
            print("The door is locked. You need the key.")
            return False
        print(f"You enter the {self.name}. {self.description}")
        return True
    def unlock(self, player):
        if self.locked and player.inventory.has_item(self.key):
            self.locked = False
            print(f"You unlock the {self.name} with the {self.key}.")
        else:
            print("You can't unlock this door.")

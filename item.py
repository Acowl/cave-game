
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, base_damage, scale_attr):
        super().__init__(name, description)
        self.base_damage = base_damage
        self.scale_attr = scale_attr  # 'agility', 'strength', 'intelligence'

    def get_damage(self, player):
        scale = getattr(player, self.scale_attr, 0)
        return self.base_damage + scale

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to inventory.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item.name} from inventory.")
                return True
        print(f"Item {item_name} not found.")
        return False

    def list_items(self):
        for item in self.items:
            print(f"{item.name}: {item.description}")

# Example weapons
dagger = Weapon(
    name="Dagger",
    description="A sharp blade that favors agility.",
    base_damage=5,
    scale_attr="agility"
)
axe = Weapon(
    name="Axe",
    description="A heavy axe that favors strength.",
    base_damage=8,
    scale_attr="strength"
)
wand = Weapon(
    name="Wand",
    description="A magical wand that favors intelligence.",
    base_damage=6,
    scale_attr="intelligence"
)


class Scene:
    def __init__(self, name, description, exits, locked=False, key=None):
        self.name = name
        self.description = description
        self.exits = exits  # e.g., {'north': 'Engineering Bay'}
        self.locked = locked
        self.key = key  # name of key that unlocks

    def _has_key(self, player):
        inventory = getattr(player, 'inventory', None)
        if inventory is None:
            return False
        # Support both list and Inventory object
        if isinstance(inventory, list):
            return self.key in inventory
        if hasattr(inventory, 'items'):
            return any(getattr(item, 'name', None) == self.key for item in inventory.items)
        return False

    def enter(self, player):
        if self.locked and not self._has_key(player):
            print("The door is locked. You need the key.")
            return False
        print(f"You enter the {self.name}. {self.description}")
        return True

    def unlock(self, player):
        if self.locked and self._has_key(player):
            self.locked = False
            print(f"You unlock the {self.name} with the {self.key}.")
        else:
            print("You can't unlock this door.")


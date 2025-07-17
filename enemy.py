
class Enemy:
    def __init__(self, name, health, exp_reward):
        self.name = name
        self.health = health
        self.exp_reward = exp_reward

    def is_defeated(self):
        return self.health <= 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

def gain_experience(player, exp):
    if not hasattr(player, 'experience'):
        player.experience = 0
    if not hasattr(player, 'attribute_points'):
        player.attribute_points = 0
    # Level up threshold: 100 * current level
    player.experience += exp
    while player.experience >= player.level * 100:
        player.experience -= player.level * 100
        player.level_up()
        # Award 3 attribute points per level up
        player.attribute_points += 3
        print(f"You gained 3 attribute points! Total: {player.attribute_points}")

def allocate_attribute(player, attribute):
    if not hasattr(player, 'attribute_points') or player.attribute_points <= 0:
        print("No attribute points to allocate.")
        return
    if attribute not in ['vitality', 'agility', 'strength', 'intelligence']:
        print("Invalid attribute.")
        return
    if not hasattr(player, 'vitality'):
        player.vitality = 5
    if attribute == 'vitality':
        player.vitality += 1
    elif attribute == 'agility':
        player.agility += 1
    elif attribute == 'strength':
        player.strength += 1
    elif attribute == 'intelligence':
        player.intelligence += 1
    player.attribute_points -= 1
    print(f"Allocated 1 point to {attribute}. Remaining: {player.attribute_points}")


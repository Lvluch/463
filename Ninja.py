import random
from Character import Character

def roll_chance(probability):
    return random.randint(1, 100) < probability
class Ninja(Character):
    max_health = 100

    def __init__(self, name, health=100, damage=5, defence=0):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = self.health

    def attack(self, target):
        if roll_chance(30):
            real_damage = 0
        else:
            real_damage = self.damage

        return target.take_damage(real_damage)
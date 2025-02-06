#Rogue, Wizzard
class Character:
    def __init__(self, strength: int = 2, accuracy: int = 2, speed: int = 2, endurance: int = 2, stamina: int = 100, mana: int = 100, hp: int = 100):
        self.strength = strength
        self.accuracy = accuracy
        self.speed = speed
        self.endurance = endurance
        self.stamina = stamina
        self.mana = mana
        self.hp = hp





class attack:
    def __init__(self, name: str = "Error NULL", damage: int = 1, stamina: int = 0, mana: int = 0, cooldown: int = 0):
        self.name = name
        self.damage = damage
        self.stamina = stamina
        self.mana = mana
        self.cooldown = cooldown


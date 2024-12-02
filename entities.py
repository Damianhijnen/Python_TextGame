#Rogue, Wizzard
class Character:
    def __init__(self, hp: int = 100, strength: int = 1):
        self.hp = hp
        self.strength = strength


tatstst = {"name" : "gerard"}

tatstst["name"]

character = Character()
character.hp


class character:
    strength = 1
    speed = 1
    accuracy = 1
    endurance = 1
    hp: int

    def __init__(self, hp: int) -> None:
        self.hp = hp

import random
from core.entities import attack
from core.function import inpInt, sInput, nobreak_line, line

#attacks list
attackMoves = {
    "1" : attack("stab", 1, 0, 0),
    "2" : attack("slash", 2, 1, 0)
}

aM = attackMoves


class Enemy:
    def __init__(self, name = "unnamed", dificulty: int = 1):
        if name == "goblin":
            self.name = name
            self.strength = 1 * (dificulty / 2)
            self.speed = 5 * (dificulty / 2)
            self.accuracy = 3 * (dificulty / 2)
            self.endurance = 1 * (dificulty / 2)
            self.hp = 10 * dificulty
            self.attack = attack(name)

        if name == "golem":
            self.name = name
            self.strength = 2 * (dificulty / 2)
            self.speed = 1 * (dificulty / 2)
            self.accuracy = 2 * (dificulty / 2)
            self.endurance = 3 * (dificulty / 2)
            self.hp = 10 * dificulty
            self.combat = combat(name)

class combat:
    def __init__(self, name) -> None:
        self.name = name
        if name == "golem":
            self.attacks = [aM["1"], aM["1"], aM["2"]]
        else:
            self.attacks = [aM["1"], aM["1"], aM["2"]]


    def attack(self):
        if self.name == "special":
            pass
        else:
            attID = random.randint(1, len(self.attacks)) - 1
            attack = self.attacks[attID] 

            line(self.name + " attacks you with " + attack.name + "for " + str(attack.damage) + " dmg")

            return attack.damage
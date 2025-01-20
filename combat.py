import random
import testData

# testSession = testData.constructSession()
#Nodig voor main mischien verplaatsen??

class Golem:
    name = "Golem"
    strength = 4
    speed = 1
    accuracy = 2
    endurance = 2
    hp = 10

class Enemy:
    def __init__(self, name = "unnamed", strength: int = 1, speed: int = 1, accuracy: int = 1, endurance: int = 1, hp: int = 10, dificulty: int = 1):
        self.name = name
        self.strength = strength * (dificulty / 4)
        self.speed = speed * (dificulty / 4)
        self.accuracy = accuracy * (dificulty / 4)
        self.endurance = endurance * (dificulty / 4)
        self.hp = hp * dificulty

def combat(inp, session):
    character = session.character 
    return ""


## Hier 
def senarioGenerator(chance, dificulty, location, range):
    enemies = []
    #range[0] = min, range[1] = max
    amount = random.randint(range[0], range[1])
    if chance < random.randint(1, 100):
        for i in range(amount):
            if location.main == "starter":
                enemyGenerator(dificulty, ["golem"])
    return enemies


def enemyGenerator(dificulty, enemyTypes):
    enemyType = enemyTypes[random.randint(0, len(enemyTypes)-1)]
    # Hier is de type defined
    if enemyType == "goblin":
        return Enemy("goblin", 1, 5, 3, 1, 10, dificulty)
    if enemyType == "golem":
        return Enemy("golem", 2, 1, 2, 3, 100, dificulty)
    if enemyType == "golem":
        return Enemy("golem", 2, 1, 2, 3, 100, dificulty)
       
en1 = enemyGenerator(1, ["golem", "goblin"])                
en2 = enemyGenerator(1, ["goblin", "golem"])
en3 = enemyGenerator(1, ["golem"])

print(str(en1.name) + " str: " + str(en1.strength))
print(str(en2.name) + " str: " + str(en2.strength))
print(str(en3.name) + " str: " + str(en3.strength))


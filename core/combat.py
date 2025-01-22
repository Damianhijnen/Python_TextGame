import random
import re
from core.enemies.enemies import Enemy
from core.entities import attack
# testSession = testData.constructSession()
# Nodig voor main mischien verplaatsen??

attacks = [attack("stab", 1, 0, 0), attack("slash", 2, 1, 0)]

def combat(inp, session):
    character = session.character
    enemies = session.enemies
    print("Your being attacked:")
    while True:
        for enemy in enemies:
            print(enemy.name + " " +  str(enemy.hp))
        inp = input("Action \n 1. Attack \n Choose action: ")
        if inp == "end":
            print("you ended the senario")
            break
        # start attack
        elif inp == "1":
            print("Your attacking \n")
            # Attack player fase
            while True:
                # Choosing attack
                for attack in attacks:
                    print(attack.name + " dmg: " + str(attack.damage))
                inp = int(re.sub("[^0-9]", "", input("Choose Attack: ")))
                if inp != "":
                    att = attacks[inp-1]
                    # Selecting enemy
                    for index, enemy in enumerate(enemies):
                        print(str(index+1) + " " + enemy.name + " " +  str(enemy.hp))
                    inp = int(re.sub("[^0-9]", "", input("\nChoose enemy: ")))
                    if inp >= 1 and inp <= len(enemies):
                        inp -= 1
                        print("Attacking " + enemies[inp].name)
                        enemies[inp].hp = enemies[inp].hp - att.damage
                        print("You " + att.name + " " + enemies[inp].name + " for " + str(att.damage) + " dmg")
                        break
    session.state = "travel"
    return session


def senarioGenerator(chance, dificulty, session, rangeArr):
    location = session.location
    session.enemies = []
    # range[0] = min, range[1] = max
    amount = random.randint(rangeArr[0], rangeArr[1]) 
    if chance >= random.randint(1, 100):
        for i in range(amount):
            if location.main == "veritas":
                session.enemies.append(enemyGenerator(dificulty, ["golem"]))
        session.state = "combat"
    return session


def enemyGenerator(dificulty, enemyTypes):
    enemyType = enemyTypes[random.randint(0, len(enemyTypes)-1)]
    # Hier is de type defined
    return Enemy(enemyType, dificulty)


def test():
    en1 = enemyGenerator(1, ["golem", "goblin"])                
    en2 = enemyGenerator(1, ["goblin", "golem"])
    en3 = enemyGenerator(1, ["golem"])

    print(str(en1.name) + " str: " + str(en1.strength))
    print(str(en2.name) + " str: " + str(en2.strength))
    print(str(en3.name) + " str: " + str(en3.strength))



#test()
import random
from core.enemies.enemies import Enemy
# testSession = testData.constructSession()
# Nodig voor main mischien verplaatsen??


def combat(inp, session):
    character = session.character
    enemies = session.enemies
    print("Your being attacked:")
    while True:
        for enemy in enemies:
            print(enemy.name + " " +  str(enemy.hp))
        inp = input("Action: ")
        if inp == "end":
            print("you ended the senario")
            break
        elif inp == "1":
            print("attack")
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
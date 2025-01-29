import sys
import time

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
    line("Your being attacked by:")
    while True:
        for enemy in enemies:
            line(" " + enemy.name + " " +  str(enemy.hp))
        inp = sInput("\nAction \n 1. Attack \n Choose action: ")
        if inp == "end":
            line("you ended the senario")
            break
        # start attack
        elif inp == "1":
            line("\nYour attacking \n\nAttacks:")
            # Attack player fase
            while True:
                # Choosing attack
                for attack in attacks:
                    line(" " + attack.name + " dmg: " + str(attack.damage))
                inp = inpInt(sInput("\nChoose Attack: "))
                if inp != "" and inp != 0:
                    att = attacks[inp-1]
                    # Selecting enemy
                    for index, enemy in enumerate(enemies):
                        line(str(index+1) + " " + enemy.name + " " +  str(enemy.hp))
                    inp = inpInt(input("\nChoose enemy: "))
                    if inp >= 1 and inp <= len(enemies):
                        inp -= 1
                        line("Attacking " + enemies[inp].name)
                        enemies[inp].hp = enemies[inp].hp - att.damage
                        line("You " + att.name + " " + enemies[inp].name + " for " + str(att.damage) + " dmg")
                        if enemies[inp].hp <= 0:
                            line(enemies[inp].name + " was slain")
                            enemies.pop()
                        break
                    else:
                        line("You " + att.name + " the air for 0 dmg")
                else:
                    line("Wrong input must be a number")
        # all enemies defeated
        if len(enemies) == 0:
            line("you defeated all enemies")
            break
    session.character = character
    session.state = "travel"
    session.enemies = []
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

    line(str(en1.name) + " str: " + str(en1.strength))
    line(str(en2.name) + " str: " + str(en2.strength))
    line(str(en3.name) + " str: " + str(en3.strength))



def inpInt(inp):
    inp = re.sub("[^0-9]", "", inp)
    if inp != "":
        return int(inp)
    else:
        return 0
#test()
def sInput(msg):
    nobreak_line(msg)
    return input(" ")


def nobreak_line(inp):
    for letter in inp:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

def line(inp):
    for letter in inp:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")
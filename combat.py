import random
import testData

testSession = testData.constructSession()
#Nodig voor main mischien verplaatsen??
def construct(inp, session):
    class character:
        strength = 1
        speed = 1
        accuracy = 1
        endurance = 1
        hp = 100
    return character

def combat(inp, session):
    charachter = session.character 
    return ""


#Concept
#
#enemieName
#   name: "Golem"
#   speed: 1
#   attack: 2
#   endurance: 3
#   hp: 10
#   
def enemyGenerator(inp, session):
    enemies = []
    if session.location.main == "starter":
        amount = random.randint(1, 3)
        
        for i in range(amount):
                enemies.append('golem')
    return enemies

print(enemyGenerator("", testSession))
print(enemyGenerator("", testSession))
print(enemyGenerator("", testSession))


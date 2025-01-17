import core.combat as combat
import core.travel as t

def test_enemyGenerator():
    result1 = combat.enemyGenerator(1, ["golem", "goblin"])
    result2 = combat.enemyGenerator(1, ["golem", "goblin"])
    result3 = combat.enemyGenerator(1, ["golem", "goblin"])

    print(result1.name + " hp: " + str(result1.hp))
    print(result2.name + " hp: " + str(result2.hp))
    print(result3.name + " hp: " + str(result3.hp))

def test_senarioGenerator():
    result1 = combat.senarioGenerator(1, 1, t.Location(), [1, 3])
    result2 = combat.senarioGenerator(100, 1, t.Location(), [1, 3])

    print(result1)
    print(result2)



test_enemyGenerator()
test_senarioGenerator()
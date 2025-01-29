import core.game as game
import core.travel as travel
import core.entities as entities


class session:
    location = travel.Location()
    msg = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
    state = "travel"
    character = entities.Character()


def menu():
    while True:
        inp = input("\n1. start 2. check stats\n")
        if inp == "1":
            game.main(session)
            break
        elif inp == "2":
            char = session.character
            print("Strength: " + str(char.strength))
            print("Speed: " + str(char.speed))
            print("Accuracy: " + str(char.accuracy))
            print("Endurance: " + str(char.endurance))
            print("Hp: " + str(char.hp))
        elif inp == "3" or "end":
            break

def test():
    game.main(session)
test()
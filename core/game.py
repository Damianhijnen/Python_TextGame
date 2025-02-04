import core.travel as travel
import core.entities as entities
import core.combat as combat

print("Game start\n")
class testsession:
    location = travel.Location()
    msg = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
    state = "travel"
    character = entities.Character()


def main(session):
    inp = ""
    while True:
        if session.state == "travel":
            session = travel.main(inp, session)
        if session.state == "combat":
            session = combat.combat(inp, session)
        if session.state == "defeated":
            print("You where defeated")
            break
        inp = ""
        inp = str(input(str(session.msg) + " \n"))
        if inp == "end":
            print("ending")
            break


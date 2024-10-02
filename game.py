import travel
print("Game start\n")
class session:
    location = travel.construct()
    msg = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
    state = "travel"

class character:
    strength = 1
    speed = 1
    accuracy = 1
    endurance = 1

    

inp = "empty"
while True:
    if session.state == "travel":
        session = travel.main(inp, session)


    inp = ""
    inp = str(input(str(session.msg) + " \n"))
    if inp == "end":
        print("ending")
        break

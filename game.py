import travel
location = travel.construct()
state = "travel"
class character:
    strength = 1
    speed = 1
    accuracy = 1
    endurance = 1


inp = "empty"
while True:
    if state == "travel":
        location = travel.main(inp, location)

    if inp == "kill":
        break
    inp = str(input(msg))

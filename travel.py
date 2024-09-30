
def construct():
    class location:
        main = "starter"
        sub = "townSquare"
    return location

def main(inp, location):
    print("input:", inp, "location:", location.main, location.sub)
    if location.main == "starter":
        if location.sub == "townSquare":
            inp = input("You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: ")
            print(inp)
            if inp == "1":
                location.sub = "townHall"
                return location
            else:
                location.sub = "forrest"
                return location
        if location.sub == "townHall":
            inp = input("You are in the Town hall.\n 1. Go outside ")
            if inp == "1":
                location.sub = "townSquare"
                return location
        if location.sub == "forrest":
            inp = input("You are in the forrest.\n 1. Go back ")
    return [location, msg]

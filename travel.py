
def construct():
    class location:
        main = "starter"
        sub = "townSquare"
    return location

def main(inp, main):
    #print("input:", inp, "location:", main.location.main, main.location.sub)
    class msg:
        pass
    if main.location.main == "starter":
        msg.townSquare = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
        msg.townHall = "You are in the Town hall.\n 1. Go outside "
        msg.forrest = "You are in the forrest.\n 1. Go back "
        if main.location.sub == "townSquare":
            if inp == "1":
                main.msg = msg.townHall
                main.location.sub = "townHall"
                return main
            elif inp == "2":
                main.msg = msg.forrest
                main.location.sub = "forrest"
                return main
            else:
                main.msg = msg.townSquare
        if main.location.sub == "townHall":
            if inp == "1":
                main.msg = msg.townSquare
                main.location.sub = "townSquare"
                return main
            else:
                main.msg = msg.townHall
        if main.location.sub == "forrest":
            main.msg = msg.forrest
            if inp == "1":
                main.msg = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
                main.location.sub = "townSquare"
                return main
    return main

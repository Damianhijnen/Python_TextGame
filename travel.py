
def construct():
    class location:
        main = "starter"
        sub = "townSquare"
        strength = 1
    return location

def main(inp, main):
    #print("input:", inp, "location:", main.location.main, main.location.sub)
    class msg:
        pass
    if main.location.main == "starter":
        msg.townSquare = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
        msg.townHall = "You are in the Town hall.\n 1. Go outside "
        msg.forest = "You are in the forest.\n 1. Go back 2. Go deeper"
        msg.deepForest = "You are deep in the forest.\n 1. Go back 2. Go deeper"
        if main.location.sub == "townSquare":
            if inp == "1":
                main.msg = msg.townHall
                main.location.sub = "townHall"
                return main
            elif inp == "2":
                main.msg = msg.forest
                main.location.sub = "forest"
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
        #Forrest###########
        if main.location.sub == "forest":
            main.msg = msg.forest
            if inp == "1":
                main.msg = msg.townSquare
                main.location.sub = "townSquare"
                return main
            if inp == "2":
                main.msg = msg.forest
                main.location.sub = "forest2"
                return main
        if main.location.sub == "forest2":
            if inp == "1":
                main.msg = msg.forest
                main.location.sub = "forest"
                return main
            if inp == "2":
                main.msg = msg.deepForest
                main.location.sub = "deepForest"
                return main
        if main.location.sub == "deepForest":
            if inp == "1":
                main.msg = msg.deepForest
                main.location.sub = "forest"
                return main
            if inp == "2":
                main.msg = "You are deep in the forest, you see the end of the tree lines in the distance \n 1. Go back 2. Leave the forest"
                main.location.sub = "deepForest2"
                return main
        if main.location.sub == "deepForest2":
            if inp == "1":
                main.msg = msg.deepForest
                main.location.sub = "forest"
                return main
            if inp == "2":
                main.msg =  "You have left the forest"
                main.location.sub = "forest2"
                return main
    return main

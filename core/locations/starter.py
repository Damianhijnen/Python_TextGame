import core.combat as combat


def location(inp, main):
        class msg:
            townSquare = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
            townHall = "You are in the Town hall.\n 1. Go outside "
            forest = "You are in the forest.\n 1. Go back 2. Go deeper"
            deepForest = "You are deep in the forest.\n 1. Go back 2. Go deeper"
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
            #combat.senarioGenerator(100, 1, main, [1, 3])
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
            #combat.senarioGenerator(100, 1, main, [1, 3])
            if inp == "1":
                main.msg = msg.forest
                main.location.sub = "forest"
                return main
            if inp == "2":
                main.msg = msg.deepForest
                main.location.sub = "deepForest"
                return main
        if main.location.sub == "deepForest":
            #combat.senarioGenerator(100, 1, main, [1, 3])
            if inp == "1":
                main.msg = msg.forest
                main.location.sub = "forest"
                return main
            if inp == "2":
                main.msg = msg.deepForest
                main.location.sub = "deepForest2"
                return main
        if main.location.sub == "deepForest2":
            #combat.senarioGenerator(100, 1, main, [1, 3])
            if inp == "1":
                main.msg = msg.deepForest
                main.location.sub = "forest"
                return main
            if inp == "2":
                main.msg = msg.deepForest
                main.location.sub = "deepForest3"
                return main
        if main.location.sub == "deepForest3":
            #combat.senarioGenerator(100, 1, main, [1, 3])
            if inp == "1":
                main.msg = msg.deepForest
                main.location.sub = "forest"
                return main
            if inp == "2":
                main.msg = "You are deep in the forest, you see the end of the tree lines in the distance \n 1. Go back 2. Leave the forest"
                main.location.sub = "planes"
                return main
        if main.location.sub == "planes":
            if inp == "1":
                main.msg = msg.deepForest
                main.location.sub = "deepForest3"
                return main
            if inp == "2":
                main.msg =  "You have entered the great planes, you see a sign saying that you are on the west side \n 1. Go back West back into the forrest 2. Go East further into the planes"
                main.location.main = "great_planes"
                main.location.sub = "westPlanes"
                return main
        return main
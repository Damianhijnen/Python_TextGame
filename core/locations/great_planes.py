import core.combat as combat


def location(inp, main):
        class msg:
            townSquare = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
            southPlanes = "You are in the planes \n 1. Go North 2. Go South"
            westPlanes = "You are in the planes \n 1. Go West 2. Go East"
            centralPlane = "You in the center of the planes \n 1. Go West 2. Go East 3. Go North 4. Go South"
        

        if main.location.sub == "westPlanes":
            if inp == "1":
                main.msg = "You are back on the edge of the forrest\n 1. Go into the forrest 2. Go back into the planes"
                main.location.main = "veritas"
                main.location.sub = "planes"
                return main
            elif inp == "2":
                main.msg = msg.westPlanes
                main.location.sub = "westPlanes1"
                return main
            else:
                main.msg = msg.townSquare
        # Planes
        if main.location.sub == "westPlanes1":
            #combat.senarioGenerator(100, 1, main, [1, 3])
            main.msg = msg.westPlanes
            if inp == "1":
                main.msg = msg.westPlanes
                main.location.sub = "westPlanes"
                return main
            if inp == "2":
                main.msg = msg.westPlanes
                main.location.sub = "westPlanes2"
                return main
        if main.location.sub == "westPlanes2":
            #combat.senarioGenerator(100, 1, main, [1, 3])
            if inp == "1":
                main.msg = msg.westPlanes
                main.location.sub = "westPlanes1"
                return main
            if inp == "2":
                main.msg = msg.centralPlane
                main.location.sub = "centralPlane"
                return main
            
        # Central planes
        if main.location.sub == "centralPlane":
            # "You in the center of the planes \n 1. Go West 2. Go East 3. Go North 4. Go South"
            # combat.senarioGenerator(100, 1, main, [1, 3])
            if inp == "1":
                main.msg = msg.westPlanes
                main.location.sub = "westPlanes1"
                return main
            if inp == "2":
                main.msg = "East"
                main.location.sub = "centralPlane"
                return main
            if inp == "3":
                main.msg = "North"
                main.location.sub = "centralPlane"
                return main
            if inp == "4":
                main.msg = "South"
                main.location.sub = "southPlane"
                return main



        # South Route
        if main.location.sub == "southPlane":
            if inp == "1":
                main.msg = msg.centralPlane
                main.location.sub = "centralPlane"
                return main
            if inp == "2":
                main.msg = msg.southPlanes
                main.location.sub = "southPlane1"
                return main
        if main.location.sub == "southPlane1":
            if inp == "1":
                main.msg = msg.centralPlane
                main.location.sub = "southPlane"
                return main
            if inp == "2":
                main.msg = msg.southPlanes
                main.location.sub = "southPlane2"
                return main
        if main.location.sub == "southPlane2":
            if inp == "1":
                main.msg = msg.centralPlane
                main.location.sub = "southPlane1"
                return main
            if inp == "2":
                main.msg = "You see a town in the distance"
                main.location.sub = "southPlane3"
                return main
        if main.location.sub == "southPlane3":
            if inp == "1":
                main.msg = "You are leaving the town in the distance and go north"
                main.location.sub = "southPlane2"
                return main
            if inp == "2":
                main.msg = "You are you are getting close to a gate"
                main.location.sub = "southPlane3"
                return main

        
        
        return main
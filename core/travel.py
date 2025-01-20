import core.locations.starter as starter
import core.combat as combat

class Location:
    def __init__(self, main: str = "starter", sub = "townSquare", strength = 1) -> None:
        self.main = main
        self.sub = sub
        self.strength = strength

def main(inp, main):
    #print("input:", inp, "location:", main.location.main, main.location.sub)
    class msg:
        pass
    if main.location.main == "starter":
        main = starter.location(inp, main, combat)
    return main

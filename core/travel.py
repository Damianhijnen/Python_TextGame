import core.locations.starter as starter
import core.locations.great_planes as great_planes

class Location:
    def __init__(self, main: str = "veritas", sub = "townSquare", strength = 1) -> None:
        self.main = main
        self.sub = sub
        self.strength = strength

def main(inp, session):
    #print("input:", inp, "location:", main.location.main, main.location.sub)
    class msg:
        pass
    if session.location.main == "veritas":
        session = starter.location(inp, session)
    elif session.location.main == "great_planes":
        session = great_planes.location(inp, session)
    return session

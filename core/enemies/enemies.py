class Enemy:
    def __init__(self, name = "unnamed", dificulty: int = 1):
        if name == "goblin":
            self.name = name
            self.strength = 1 * (dificulty / 4)
            self.speed = 5 * (dificulty / 4)
            self.accuracy = 3 * (dificulty / 4)
            self.endurance = 1 * (dificulty / 4)
            self.hp = 10 * dificulty

        if name == "golem":
            self.name = name
            self.strength = 2 * (dificulty / 4)
            self.speed = 1 * (dificulty / 4)
            self.accuracy = 2 * (dificulty / 4)
            self.endurance = 3 * (dificulty / 4)
            self.hp = 10 * dificulty

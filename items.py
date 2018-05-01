class Rock:
    def __init__(self):
        self.name = "Rock"
        self.description = "A rock, I could do some damage if I hit someone with this..."
        self.damage = 5

    def __str__(self):
        return self.name

class Dagger:
    def __init__(self):
        self.name = "Dagger"
        self.description = "I can stabby stab with this"
        self.damage = 7

    def __str__(self):
        return self.name


class RustySword:
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword must be old...it'l work though"
        self.damage = 20

    def __str__(self):
        return self.name
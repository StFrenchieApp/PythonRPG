class Armor:
    def __init__(self):
        raise notImplementedError("Do not create raw Armor objects.")
    
    def __str__(self):
        return self.name

class Bandages(Armor):
    def __init__(self):
        self.name = "Bandages"
        self.description = "Bandages might protect me?"
        self.health = 5
        self.value = 1

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Pebble(Weapon):
    def __init__(self):
        self.name = "Pebble"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                           "Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 20


class Sword(Weapon):
    def __init__(self):
        self.name = "sword"
        self.description = "This sword is showing its age, " \
                           "but still has some fight in it."
        self.damage = 20
        self.value = 100


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Apple(Consumable):
    def __init__(self):
        self.name = "Apple"
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [Apple(),
                      Apple(),
                      Apple(),
                      HealingPotion(),
                      HealingPotion(),
                      Sword()]

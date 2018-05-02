import map
import os
import objects

class Player:
    def __init__(self):
        self.inventory = [objects.Pebble(),
                          objects.Dagger(),
                          objects.Apple()]
        self.x = map.start_tile_location[0]
        self.y = map.start_tile_location[1]
        self.hp = 1000 
        self.gold = 5
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        print("Gold: {}".format(self.gold))

    def heal(self):
        consumables = [objects for objects in self.inventory
                       if isinstance(objects, objects.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

   # def best_armor(self):
   #     max_health = 0
   #     best_armor = None
   #     for item in self.inventory:
   #         try:
   #             if item.health > max_health:
   #                 best_armor = item
   #                 max_health = item.damage
   #         except AttributeError:
   #             pass
   #         
   #         self.hp = self.hp + max_health
   #         return best_armor            

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = map.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def trade(self):
        room = map.tile_at(self.x, self.y)
        room.check_if_trade(self)

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Easy(Enemy):
    def __init__(self):
        self.name = "Spider"
        self.hp = 10
        self.damage = 2


class Medium(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 100
        self.damage = 6


class Hard(Enemy):
    def __init__(self):
        self.name = "Colony of bats"
        self.hp = 30
        self.damage = 4


class Boss(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15



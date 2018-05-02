import sys
from collections import OrderedDict
from player import Player
import player
import map

user_n = input("What is your name?: ")
user_e = input("What color are your eyes?: ")
user_h = input("What color is your hair?: ")

def mir():
        print("I can see my pefect {} eyes and flawless {} hair".format(user_e, user_h))

def quit():
    sys.exit()


def print_map():
        print("EN = enemy, VT = victory, FG = gold, TT = trade")
        print("|EN|EN|VT|EN|EN|")
        print("|EN|  |  |  |EN|")
        print("|EN|FG|EN|  |TT|")
        print("|TT|  |ST|FG|EN|")
        print("|FG|  |EN|  |FG|")   

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play():

    print("{} you must escape from the pyramid".format(user_n))
    map.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = map.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("You didnt make it out...")


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    ran = 1
    if ran == 1:
        action_adder(actions, 'm', mir, "Look at yourself")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Inventory")
    if ran == 1:
        action_adder(actions, 'p', print_map, "Print map (for cheaters)")
    if isinstance(room, map.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if ran == 1:
        action_adder(actions, 'c', clear, "Clear the screen")
    if isinstance(room, map.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    if ran == 1:
        action_adder(actions, 'q', quit, "quit without saving!")
    else:
        if map.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Move north")
        if map.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Move south")
        if map.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Move east")
        if map.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Move west")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")
       
    
    

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()

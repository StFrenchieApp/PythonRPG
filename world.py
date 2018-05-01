class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):
    def intro_text(self):
        return """
        You're in a cave scurrying around
        you can barley see four paths,
        ...choose wisely
        """

class BoringTile(MapTile):
    def intro_text(self):
        return """
        Seems like theres nothing to 
        do here...
        """

class VictoryTile(MapTile):
    def intro_text(self):
        return """
        is that sunglight???
        You run to the sun as you escape the cave

        You won!
        """

world_map = [
    [None, VictoryTile(1,0),None],
    [None, BoringTile(1,1), None],
    [BoringTile(0,2), StartTile(1,2),BoringTile(2,2)],
    [None, BoringTile(1,3),None]
    
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None




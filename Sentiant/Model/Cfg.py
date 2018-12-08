
class Cfg:
    def __init__(self):
        pass

    HPMAX = 2
    FOV=7
    HPRADIUS = 5
    WIDTH=42
    HEIGHT=42

    UP = { 'x': 0, 'y': -1 }
    DOWN = { 'x': 0, 'y': 1 }
    RIGHT = { 'x': 1, 'y': 0 }
    LEFT = { 'x': -1, 'y': 0 }
    NULL = "null"

    MOVE = "move"
    DIG = "dig"
    DROP = "drop"
    PICKUP = "pickup"
    ATTACK = "attack"
    SLEEP = "sleep"
    PHERO = "phero" # Attention à ne pas faire phero sur un rocher mdr




    def parseDirection (self, direction):

        direction = direction.lower()
        if(direction == "up"):
            return self.UP
        elif direction == "down":
            return self.DOWN
        elif direction == "right":
            return self.RIGHT
        elif direction == "left":
            return self.LEFT
        return self.NULL

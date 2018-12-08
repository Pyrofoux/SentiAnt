from Sentiant.Model import *

class Cfg:
    def __init__(self):
        pass

    HPMAX = 2
    FOV=7
    HPRADIUS = 5
    WIDTH=42
    HEIGHT=42

    UP = {"x": 0, "y": -1}
    DOWN = {"x": 0, "y": 1}
    RIGHT = {"x": 1, "y": 0}
    LEFT = {"x": -1, "y":0}
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

        # TODO : Log Error

        return self.NULL



    def addDirection(self, coords, direction):

        direction = self.parseDirection(direction)

        #TODO : Check coords valides ?
        if (direction == self.UP):
            return [coords[0], coords[1] - 1]
        elif (direction == self.DOWN):
            return [coords[0], coords[1] + 1]
        elif (direction == self.RIGHT):
            return [coords[0] + 1, coords[1]]
        elif (direction == self.LEFT):
            return [coords[0] - 1, coords[1]]

        #TODO : Log Error de direction
        return self.NULL





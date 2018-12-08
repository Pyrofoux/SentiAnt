from Sentiant.Model import Point

class Cfg:
    def __init__(self):
        pass

    HPMAX    = 2
    FOV      = 7
    HPRADIUS = 5
    WIDTH    = 42
    HEIGHT   = 42

    UP    = Point(0, -1)
    DOWN  = Point(0, 1)
    RIGHT = Point(1, 0)
    LEFT  = Point(-1, 0)
    NULL  = "null"

    MOVE   = "move"
    DIG    = "dig"
    DROP   = "drop"
    PICKUP = "pickup"
    ATTACK = "attack"
    SLEEP  = "sleep"
    PHERO  = "phero" # Attention à ne pas faire phero sur un rocher mdr
                     # (c pa possib' zi on peu pa marcher sur 1 rocher lolz)


    def parseDirection (self, direction):
        direction = direction.lower()

        if(direction == "up"):
            return UP
        elif direction == "down":
            return DOWN
        elif direction == "right":
            return RIGHT
        elif direction == "left":
            return LEFT

        # TODO : Log Error
        return NULL


    def addDirection(self, coords, direction):
        direction = self.parseDirection(direction)

        if direction in [UP, DOWN, RIGTH, LEFT]:
            nextPos = coords + direction

            #TODO : Check coords valides!
            #if layerSolid.walkable(nextPos):
            return nextPos

        #TODO : Log Error de direction
        return self.NULL

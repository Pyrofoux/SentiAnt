from .Point import Point

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
    ACTIONS = [MOVE, DIG, DROP, PICKUP, ATTACK, SLEEP, PHERO]

    ANT = "ant"
    QUEEN = "queen"
    DIRT = "dirt"
    ROCK = "rock"
    BREAD = "bread"
    COOKIE = "cookie"




    def parseDirection (self, direction):
        global UP, DOWN, RIGHT, LEFT, NULL
        direction = direction.lower()

        if(direction == "up"):
            return self.UP
        elif direction == "down":
            return self.DOWN
        elif direction == "right":
            return self.RIGHT
        elif direction == "left":
            return self.LEFT

        #TODO : Log Error

        return self.NULL



    def addDirection(self, coords, direction):
        direction = self.parseDirection(direction)

        if direction in [self.UP, self.DOWN, self.RIGTH, self.LEFT]:
            nextPos = coords + direction

            #TODO : Check coords valides!
            #if layerSolid.walkable(nextPos):
            return nextPos

        #TODO : Log Error de direction
        return self.NULL

    def EntityToType(self, ref):

        if type(ref) is Ant:
            return self.ANT
        if type(ref) is QueenTile:
            return self.QUEEN

        if type(ref) is Dirt:
            return self.DIRT
        if type(ref) is Rock:
            return self.ROCK


        if type(ref) is Bread:
            return self.BREAD
        if type(ref) is Cookie:
            return self.COOKIE

        return self.NULL



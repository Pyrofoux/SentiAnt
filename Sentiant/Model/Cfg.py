from .Point import Point
from .Ant import Ant
from .QueenTile import QueenTile
from .Dirt import Dirt
from .Rock import Rock
from .Bread import Bread
from .Cookie import Cookie

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



    @staticmethod
    def parseDirection (direction):
        global UP, DOWN, RIGHT, LEFT, NULL
        direction = direction.lower()

        if(direction == "up"):
            return Cfg.UP
        elif direction == "down":
            return Cfg.DOWN
        elif direction == "right":
            return Cfg.RIGHT
        elif direction == "left":
            return Cfg.LEFT

        #TODO : Log Error

        return Cfg.NULL


    @staticmethod
    def addDirection(coords, direction):
        direction = Cfg.parseDirection(direction)

        if direction in [Cfg.UP, Cfg.DOWN, Cfg.RIGHT, Cfg.LEFT]:
            nextPos = coords + direction

            #TODO : Check coords valides!
            #if layerSolid.walkable(nextPos):
            return nextPos

        #TODO : Log Error de direction
        return Cfg.NULL

    @staticmethod
    def EntityToType(ref):

        if type(ref) is Ant:
            return Cfg.ANT
        if type(ref) is QueenTile:
            return Cfg.QUEEN

        if type(ref) is Dirt:
            return Cfg.DIRT
        if type(ref) is Rock:
            return Cfg.ROCK


        if type(ref) is Bread:
            return self.BREAD
        if type(ref) is Cookie:
            return self.COOKIE

        return self.NULL



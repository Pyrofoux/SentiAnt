from Sentiant.Model.Point import Point

class Cfg:
    def __init__(self):
        pass

    HPMAX    = 2
    FOV      = 3
    HPRADIUS = 5
    WIDTH    = 42
    HEIGHT   = 42

    UP         = Point(0, -1)
    DOWN       = Point(0, 1)
    RIGHT      = Point(1, 0)
    LEFT       = Point(-1, 0)
    DIRECTIONS = (UP, DOWN, RIGHT, LEFT)

    NULL  = None

    MOVE    = "move"
    DIG     = "dig"
    DROP    = "drop"
    PICKUP  = "pickup"
    ATTACK  = "attack"
    SLEEP   = "sleep"
    PHERO   = "phero" # Attention à ne pas faire phero sur un rocher mdr
    ACTIONS = (MOVE, DIG, DROP, PICKUP, ATTACK, SLEEP, PHERO)

    ANT = "ant"
    QUEEN = "queen"
    DIRT = "dirt"
    ROCK = "rock"
    BREAD = "bread"
    COOKIE = "cookie"
    UNKNOWN = "X"
    EMPTY = " "

    NEST_RADIUS = 3
    MIN_SPAWN_QUEEN_RADIUS = 5

    QUEEN_SLEEP = "sleep"
    QUEEN_SPAWN_ANT = "spawn"



    @staticmethod
    def ParseDirection(direction):
        if isinstance(direction, Point) and direction.StepDistance() <= 1:
            return direction

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
    def AddDirection(coords, direction):
        direction = Cfg.parseDirection(direction)

        if direction in [Cfg.UP, Cfg.DOWN, Cfg.RIGHT, Cfg.LEFT]:
            nextPos = coords + direction
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
            return Cfg.BREAD
        if type(ref) is Cookie:
            return Cfg.COOKIE

        return Cfg.EMPTY

# Please avoid cyclic imports.
from Sentiant.Model.Ant import Ant
from Sentiant.Model.QueenTile import QueenTile
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Rock import Rock
from Sentiant.Model.Bread import Bread
from Sentiant.Model.Cookie import Cookie

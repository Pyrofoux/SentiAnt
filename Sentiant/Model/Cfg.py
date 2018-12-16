from Sentiant.Model.Point import Point

class Cfg:
    def __init__(self):
        pass

    HPMAX    = 2
    FOV      = 3
    HPRADIUS = 5
    WIDTH    = 42
    HEIGHT   = 42

    UP         = Point(-1, 0)
    DOWN       = Point(1, 0)
    RIGHT      = Point(0, 1)
    LEFT       = Point(0, -1)
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

    NEST_RADIUS = 3 #rayon du cercle libéré (pas de terre) autour de la reine
    MIN_SPAWN_QUEEN_RADIUS = 5 #distance minimale éloignée du cookie par rapport à laquelle la reine peut spawn

    QUEEN_SLEEP = "sleep"
    QUEEN_SPAWN_ANT = "spawn"



    @staticmethod
    def ParseDirection(direction):
        if isinstance(direction, Point) and direction.StepDistance() <= 1:
            return direction

        direction = direction.lower()

        if direction == "up":
            return Cfg.UP
        elif direction == "down":
            return Cfg.DOWN
        elif direction == "right":
            return Cfg.RIGHT
        elif direction == "left":
            return Cfg.LEFT

        return Cfg.NULL


    @staticmethod
    def AddDirection(coords, direction):
        direction = Cfg.parseDirection(direction)

        if direction in [Cfg.UP, Cfg.DOWN, Cfg.RIGHT, Cfg.LEFT]:
            nextPos = coords + direction

            return nextPos

        return Cfg.NULL

    @staticmethod
    def EntityToType(ref):

        if isinstance(ref,Ant):
            return Cfg.ANT
        if isinstance(ref,QueenTile):
            return Cfg.QUEEN

        if isinstance(ref,Dirt):
            return Cfg.DIRT
        if isinstance(ref,Rock):
            return Cfg.ROCK


        if isinstance(ref,Bread):
            return Cfg.BREAD
        if isinstance(ref,Cookie):
            return Cfg.COOKIE

        return Cfg.EMPTY

# Please avoid cyclic imports.
from Sentiant.Model.Ant import Ant
from Sentiant.Model.QueenTile import QueenTile
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Rock import Rock
from Sentiant.Model.Bread import Bread
from Sentiant.Model.Cookie import Cookie

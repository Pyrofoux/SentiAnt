from tkinter import PhotoImage

class ImageManager:
    def __init__(self):
        pass

    EMPTY           = None

    ANT             = None
    BREAD           = None
    COOKIE          = None
    PHEROMONE       = None
    ROCK            = None

    ANT_N_BREAD     = None
    ANT_N_COOKIE    = None
    ANT_N_PHEROMONE = None

    QUEEN_PART_1 = None
    QUEEN_PART_2 = None
    QUEEN_PART_3 = None
    QUEEN_PART_4 = None

    COLOR_EMPTY = "NavajoWhite2"
    COLOR_WALL  = "NavajoWhite4"

    @staticmethod
    def LoadImages(imgSize, dr="Sentiant/View/assets/"):
        global EMPTY, ANT, BREAD, COOKIE, PHEROMONE, ROCK, \
               ANT_N_BREAD, ANT_N_COOKIE, ANT_N_PHEROMONE, QUEEN_PART_1\
            , QUEEN_PART_2, QUEEN_PART_3, QUEEN_PART_4
        r = 300 // imgSize[0]

        EMPTY           = PhotoImage(file=dr+"empty.png").subsample(r)

        ANT             = PhotoImage(file=dr+"ant.png").subsample(r)
        BREAD           = PhotoImage(file=dr+"bread.png").subsample(r)
        COOKIE          = PhotoImage(file=dr+"cookie.png").subsample(r)
        PHEROMONE       = PhotoImage(file=dr+"pheromone.png").subsample(r)
        ROCK            = PhotoImage(file=dr+"rock.png").subsample(r)

        ANT_N_BREAD     = PhotoImage(file=dr+"ant_n_bread.png").subsample(r)
        ANT_N_COOKIE    = PhotoImage(file=dr+"ant_n_cookie.png").subsample(r)
        ANT_N_PHEROMONE = PhotoImage(file=dr+"ant_n_pheromone.png").subsample(r)

        QUEEN_PART_1 = PhotoImage(file=dr+"queen_part_001.png").subsample(r)
        QUEEN_PART_2 = PhotoImage(file=dr + "queen_part_002.png").subsample(r)
        QUEEN_PART_3 = PhotoImage(file=dr + "queen_part_003.png").subsample(r)
        QUEEN_PART_4 = PhotoImage(file=dr + "queen_part_004.png").subsample(r)

    @staticmethod
    def GetContent(tileSolid, tileFloor, tilePheromone, metadata = 0):
        img = EMPTY
        bgc = ImageManager.COLOR_WALL if isinstance(tileSolid, (Dirt, Rock)) \
              else ImageManager.COLOR_EMPTY

        if isinstance(tileSolid, Ant):
            if isinstance(tilePheromone, Pheromone):
                img = ANT_N_PHEROMONE
            elif isinstance(tileFloor, Bread):
                img = ANT_N_BREAD
            elif isinstance(tileFloor, Cookie):
                img = ANT_N_COOKIE
            else:
                img = ANT

        elif isinstance(tileSolid, Rock):
            img = ROCK

        elif isinstance(tileSolid, QueenTile):
            if metadata == 0:
                img = QUEEN_PART_1
            elif metadata == 2:
                img = QUEEN_PART_2
            elif metadata == 1:
                img = QUEEN_PART_3
            elif metadata == 3:
                img = QUEEN_PART_4


        else:
            if isinstance(tilePheromone, Pheromone):
                img = PHEROMONE
            elif isinstance(tileFloor, Bread):
                img = BREAD
            elif isinstance(tileFloor, Cookie):
                img = COOKIE

        return img, bgc

from Sentiant.Model.Ant import Ant
from Sentiant.Model.Pheromone import Pheromone
from Sentiant.Model.Bread import Bread
from Sentiant.Model.Cookie import Cookie
from Sentiant.Model.Rock import Rock
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model import QueenTile

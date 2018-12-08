from tkinter import PhotoImage
from Sentiant.Model import Ant, Pheromone, Bread, Cookie, Rock, Dirt

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

    COLOR_EMPTY = "NavajoWhite2"
    COLOR_WALL  = "NavajoWhite4"

    @staticmethod
    def LoadImages(imgSize, dir="assets/"):
        global EMPTY, ANT, BREAD, COOKIE, PHEROMONE, ROCK, ANT_N_BREAD, ANT_N_COOKIE, ANT_N_PHEROMONE


        EMPTY           = PhotoImage(file=dir + "empty.png").subsample(300//imgSize[0])

        ANT             = PhotoImage(file=dir + "ant.png").subsample(300//imgSize[0])
        BREAD           = PhotoImage(file=dir + "bread.png").subsample(300//imgSize[0])
        COOKIE          = PhotoImage(file=dir + "cookie.png").subsample(300//imgSize[0])
        PHEROMONE       = PhotoImage(file=dir + "pheromone.png").subsample(300//imgSize[0])
        ROCK            = PhotoImage(file=dir + "rock.png").subsample(300//imgSize[0])

        ANT_N_BREAD     = PhotoImage(file=dir + "ant_n_bread.png").subsample(300//imgSize[0])
        ANT_N_COOKIE    = PhotoImage(file=dir + "ant_n_cookie.png").subsample(300//imgSize[0])
        ANT_N_PHEROMONE = PhotoImage(file=dir + "ant_n_pheromone.png").subsample(300//imgSize[0])

    @staticmethod
    def GetImage(tileSolid, tileFloor, tilePheromone):
        global EMPTY, ANT, BREAD, COOKIE, PHEROMONE, ROCK, ANT_N_BREAD, ANT_N_COOKIE, ANT_N_PHEROMONE

        img = EMPTY

        bgc = ImageManager.COLOR_WALL if isinstance(tileSolid, Dirt) else \
              ImageManager.COLOR_EMPTY

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
        else:
            if isinstance(tilePheromone, Pheromone):
                img = PHEROMONE
            elif isinstance(tileFloor, Bread):
                img = BREAD
            elif isinstance(tileFloor, Cookie):
                img = COOKIE

        return img, bgc

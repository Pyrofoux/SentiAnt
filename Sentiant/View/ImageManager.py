from tkinter import PhotoImage
from Sentiant.Model import *

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

    COLOR_EMPTY = "White"
    COLOR_WALL  = "Black"

    @staticmethod
    def LoadImages(imgSize, dir="assets/"):
        global EMPTY, ANT, BREAD, COOKIE, PHEROMONE, ROCK, ANT_N_BREAD, ANT_N_COOKIE, ANT_N_PHEROMONE


        EMPTY           = PhotoImage(file=dir + "empty.png").zoom(imgSize[0], imgSize[1])

        ANT             = PhotoImage(file=dir + "ant.png").zoom(imgSize[0], imgSize[1])
        BREAD           = PhotoImage(file=dir + "bread.png").zoom(imgSize[0], imgSize[1])
        COOKIE          = PhotoImage(file=dir + "cookie.png").zoom(imgSize[0], imgSize[1])
        PHEROMONE       = PhotoImage(file=dir + "pheromone.png").zoom(imgSize[0], imgSize[1])
        ROCK            = PhotoImage(file=dir + "rock.png").zoom(imgSize[0], imgSize[1])

        ANT_N_BREAD     = PhotoImage(file=dir + "ant_n_bread.png").zoom(imgSize[0], imgSize[1])
        ANT_N_COOKIE    = PhotoImage(file=dir + "ant_n_cookie.png").zoom(imgSize[0], imgSize[1])
        ANT_N_PHEROMONE = PhotoImage(file=dir + "ant_n_pheromone.png").zoom(imgSize[0], imgSize[1])

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

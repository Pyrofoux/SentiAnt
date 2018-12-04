from tkinter import PhotoImage
from Sentiant.Model import *

class ImageManager:
    def __init__(self):
        pass

    # temps
    dir = "/assets/"
    rz = .5

    EMPTY           = PhotoImage(file=dir + "empty.png").subsample(rz)

    ANT             = PhotoImage(file=dir + "ant.png").subsample(rz)
    BREAD           = PhotoImage(file=dir + "bread.png").subsample(rz)
    COOKIE          = PhotoImage(file=dir + "cookie.png").subsample(rz)
    PHEROMONE       = PhotoImage(file=dir + "pheromone.png").subsample(rz)
    ROCK            = PhotoImage(file=dir + "rock.png").subsample(rz)

    ANT_N_BREAD     = PhotoImage(file=dir + "ant_n_bread.png").subsample(rz)
    ANT_N_COOKIE    = PhotoImage(file=dir + "ant_n_cookie.png").subsample(rz)
    ANT_N_PHEROMONE = PhotoImage(file=dir + "ant_n_pheromone.png").subsample(rz)

    COLOR_EMPTY = "White"
    COLOR_WALL = "Black"

    def GetImage(self, tileSolid, tileFloor, tilePheromone):
        img = ImageManager.EMPTY
        bgc = ImageManager.COLOR_WALL if isinstance(tileSolid, Dirt) else \
            ImageManager.COLOR_EMPTY

        if isinstance(tileSolid, Ant):
            if isinstance(tilePheromone, Pheromone):
                img = ImageManager.ANT_N_PHEROMONE
            elif isinstance(tileFloor, Bread):
                img = ImageManager.ANT_N_BREAD
            elif isinstance(tileFloor, Cookie):
                img = ImageManager.ANT_N_COOKIE
            else:
                img = ImageManager.ANT
        elif isinstance(tileSolid, Rock):
            img = ImageManager.ROCK
        else:
            if isinstance(tilePheromone, Pheromone):
                img = ImageManager.PHEROMONE
            elif isinstance(tileFloor, Bread):
                img = ImageManager.BREAD
            elif isinstance(tileFloor, Cookie):
                img = ImageManager.COOKIE
        return (img, bgc)

from tkinter import PhotoImage

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

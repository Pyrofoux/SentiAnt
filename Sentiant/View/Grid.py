from tkinter import Frame, Button, Tk

from Sentiant.Model import Map, Ant, Rock, Pheromone, Dirt, Cookie, Bread
from Sentiant import Cfg
from Sentiant.View import ImageManager

class Grid(Frame):

    def __init__(self, map, boss):
        self.buttons = []

        # init Frame
        Frame.__init__(self, boss)

        # property
        self.map = map

        # create buttons
        for i in range(map.layerFloor.GetWidth()):
            self.buttons.append([])

            for j in range(map.layerFloor.GetHeight()):
                b = Button(self, text="" + i + ", " + j)
                b.grid(row=i, column=j)
                self.buttons[-1].append(b)

    def Update(self, x, y):
        tileSolid = self.map.layerSolid[i, j]
        tilePheromone = self.map.layerPheromone[i, j]
        tileFloor = self.map.layerFloor[i, j]

        img = ImageManager.EMPTY
        bgc = ImageManager.COLOR_WALL if isinstance(tileSolid, Dirt) else \
              ImageManager.COLOR_EMPTY

        if isinstance(tileSolid, Ant):
            if isinstance(tilePheromone, Pheromone):
                img = ImageManager.ANT_N_PHEROMONE
            elif isinstance(tileFloor Bread):
                img = ImageManager.ANT_N_BREAD
            elif isinstance(tileFloor Cookie):
                img = ImageManager.ANT_N_COOKIE
            else:
                img = ImageManager.ANT
        elif isinstance(tileSolid, Rock):
            img = ImageManager.ROCK
        else:
            if isinstance(tilePheromone, Pheromone):
                img = ImageManager.PHEROMONE
            elif isinstance(tileFloor Bread):
                img = ImageManager.BREAD
            elif isinstance(tileFloor Cookie):
                img = ImageManager.COOKIE

        self.buttons[i][j].config(image=img, bg=bgc)

    def UpdateAll(self):
        for i in range(Cfg.WIDTH):
            for j in range(Cfg.HEIGHT):
                self.Update(i, j)


if __name__ == "__main__":
    root = Tk.__init__()

    map = Map(width = 10, height = 10)

    grid = Grid(boss = root, map = map)

    root.mainloop()

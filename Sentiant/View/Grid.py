from tkinter import Frame, Button, Tk

from Sentiant.Model import Map, Ant, Rock, Pheromone, Dirt, Cookie, Bread
from Sentiant.View import ImageManager
from Sentiant import Cfg

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
        tileSolid = self.map.layerSolid[x, y]
        tilePheromone = self.map.layerPheromone[x, y]
        tileFloor = self.map.layerFloor[x, y]

        (img, bgc) = ImageManager.GetImage(tileSolid, tileFloor, tilePheromone)

        self.buttons[x][y].config(image=img, bg=bgc)

    def UpdateAll(self):
        for i in range(Cfg.WIDTH):
            for j in range(Cfg.HEIGHT):
                self.Update(i, j)


if __name__ == "__main__":
    root = Tk()

    map = Map()

    grid = Grid(boss = root, map = map)
    grid.pack()

    root.mainloop()

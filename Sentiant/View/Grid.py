from tkinter import Frame, Button, Tk

from Sentiant.Model import Map, Ant, Rock, Pheromone, Dirt, Cookie, Bread
from Sentiant.View.ImageManager import ImageManager
from Sentiant.Model import Cfg

class Grid(Frame):

    def __init__(self, map, boss, size):
        self.buttons = []

        # init Frame
        Frame.__init__(self, boss)
        self.config(width= size[0], height=[1])

        # property
        self.map = map

        # create buttons
        for i in range(map.layerFloor.GetWidth()):
            self.buttons.append([])

            for j in range(map.layerFloor.GetHeight()):
                b = Button(self, text="{0}, {1}".format(i, j))
                b.grid(row=i, column=j)
                self.buttons[-1].append(b)

        ImageManager.LoadImages((5, 5))

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
    import os

    print(os.getcwd())
    root = Tk()

    map = Map(w=10, h=10)

    grid = Grid(boss = root, map = map, size = (50, 50))
    grid.pack()

    grid.UpdateAll()

    root.mainloop()

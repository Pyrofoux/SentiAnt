from tkinter import Frame, Button, Tk

from Sentiant.View.ImageManager import ImageManager

class Grid(Frame):

    def __init__(self, map, boss, size):
        self.buttons = []

        # init Frame
        Frame.__init__(self, boss)
        self.config(width= size[0], height= size[1])

        # property
        self.map = map

        ImageManager.LoadImages((size[0]//map.layerFloor.GetWidth(), size[1]//map.layerFloor.GetHeight()))

        # create buttons
        for i in range(map.layerFloor.GetWidth()):
            self.buttons.append([])

            for j in range(map.layerFloor.GetHeight()):
                b = Button(self)#, text="{0}, {1}".format(i, j))
                b.config(width=size[0]//map.layerFloor.GetWidth(), height = size[1]//map.layerFloor.GetHeight())
                b.grid(row=i, column=j)
                self.buttons[-1].append(b)
        self.UpdateAll()


    def Update(self, x, y):
        tileSolid = self.map.layerSolid[x, y]
        tilePheromone = self.map.layerPheromone[x, y]
        tileFloor = self.map.layerFloor[x, y]

        (img, bgc) = ImageManager.GetImage(tileSolid, tileFloor, tilePheromone)

        self.buttons[x][y].config(image=img, bg=bgc)

    def UpdateAll(self):
        for i in range(self.map.layerFloor.GetWidth()):
            for j in range(self.map.layerFloor.GetHeight()):
                self.Update(i, j)


if __name__ == "__main__":
    import os
    from Sentiant.Model import Point
    from Sentiant.Model import Ant, Bread,Map

    root = Tk()

    map = Map(w=10, h=10)

    map.layerSolid.Append(Ant(1, "test", "test"), Point(5, 5))
    map.layerFloor.Append(Bread(1), Point(5,5))

    grid = Grid(boss = root, map = map, size = (500, 500))
    grid.pack()

    root.mainloop()

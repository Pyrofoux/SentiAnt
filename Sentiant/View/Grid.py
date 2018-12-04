from tkinter import Frame, Button, Tk
from Sentiant.Model import Map

class Grid(Frame):

    def __init__(self, map, boss):

        # init Frame
        Frame.__init__(self, boss)

        # property
        self.map = map

        # create buttons
        for i in range(map.layerFloor.GetWidth()):
            for j in range(map.layerFloor.GetHeight()):
                Button(self, text = "{0}, {1}".format(str(i), str(j)))\
                    .grid(row = i, column = j)

if __name__ == "__main__":
    root = Tk.__init__()

    map = Map(width = 10, height = 10)

    grid = Grid(boss = root, map = map)

    root.mainloop()


from tkinter import Tk
from .Grid import Grid

class MainView(Tk):
    def __init__(self, map):

        # Init Window
        Tk.__init__(self)

        # property
        self.Map = map

        self.grid = Grid(self.Map, self, (500, 500))
        self.grid.pack()



    def Run(self):
        self.mainloop()

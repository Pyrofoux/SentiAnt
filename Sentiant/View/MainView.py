from tkinter import Tk, Button
from .Grid import Grid

class MainView(Tk):
    def __init__(self, map, turnmanager):

        # Init Window
        Tk.__init__(self)

        # property
        self.Map = map
        self.TurnManager = turnmanager

        self.grid = Grid(self.Map, self, (500, 500))
        self.grid.pack()

        self.bNextTurn = Button(self, text = "Next Turn", command=self.TurnManager.NextTurn())
        self.bNextTurn.pack()



    def Run(self):
        self.mainloop()

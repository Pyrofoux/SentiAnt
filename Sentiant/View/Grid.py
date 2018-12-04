from tkinter import Frame

class Grid(Frame):

    def __init__(self, grille, boss = None):

        # init Frame
        Frame.__init__(self, boss)

        # property
        self.grille = grille

        # create buttons
        for i in range()
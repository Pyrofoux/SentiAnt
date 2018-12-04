
from tkinter import Tk

class MainView(Tk):
    def __init__(self, map):

        # Init Window
        Tk.__init__(self)

        # property
        self.Map = map



    def run(self):
        self.mainloop()

from tkinter import Tk, Button, VERTICAL, HORIZONTAL, N, S, E, W, Scrollbar, Canvas
from .Grid import Grid

class MainView(Tk):
    def __init__(self, map, turnmanager = None, size= 500):
        # Init Window
        Tk.__init__(self)

        # property
        self.Map = map
        self.TurnManager = turnmanager

        # scrollbars
        vsb = Scrollbar(self, orient=VERTICAL)
        vsb.grid(row=0, column=1, sticky=N+S)

        hsb = Scrollbar(self, orient=HORIZONTAL)
        hsb.grid(row=1, column=0, sticky=E+W)

        canvas = Canvas(self, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        canvas.grid(row=0, column=0, sticky="news")

        vsb.config(command=canvas.yview)
        hsb.config(command=canvas.xview)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid = Grid(self.Map, canvas, size=(size, size))
        self.grid.pack()

        if turnmanager is not None:
            self.bNextTurn = Button(self, text="Next Turn", command=self.TurnManager.NextTurn)
            self.bNextTurn.grid(row=2, column=0)#.pack()

        canvas.create_window(0, 0, window=self.grid)
        self.grid.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        self.bind_all("<MouseWheel>", lambda e: self.Scroll(canvas, e))

    def Scroll(self, canvas, event):
        if event.state & 4:
            global tileSize
            tileSize+= event.delta // 120

            for row in grid:
                for it in row:
                    it.configure(width=tileSize, height=tileSize)

            canvas.update_idletasks()
            root.update_idletasks()

        elif event.state & 1:
            canvas.xview_scroll(-event.delta // 120, "units")
        else:
            canvas.yview_scroll(-event.delta // 120, "units")

    def Run(self):
        self.mainloop()

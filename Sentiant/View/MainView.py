from tkinter import  VERTICAL, HORIZONTAL, N, S, E, W, Scrollbar, Canvas
from tkinter import Toplevel, Button, StringVar, Label
from Sentiant.Model import Ant
from .Grid import Grid

class MainView(Toplevel):
    def __init__(self, map, turnmanager = None, size= 500):
        # Init Window
        Toplevel.__init__(self)

        # property
        self.Map = map
        self.TurnManager = turnmanager
        self.startFlag = False

        # scrollbars
        vsb = Scrollbar(self, orient=VERTICAL)
        vsb.grid(row=0, column=2, rowspan = 10, sticky=N+S)

        hsb = Scrollbar(self, orient=HORIZONTAL)
        hsb.grid(row=11, column=1, sticky=E+W)

        self.canvas = Canvas(self, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.canvas.config(width=size + 100)
        self.canvas.grid(row=0, column=1, rowspan = 10, sticky="news")

        vsb.config(command=self.canvas.yview)
        hsb.config(command=self.canvas.xview)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid = Grid(self.Map, self.canvas, size=(size, size), master=self)
        self.grid.pack()

        if turnmanager is not None:
            self.bNextTurn = Button(self, text = "Next Turn", command=self.NextTurnBind) #uses a method here so it can easily checks a possible win
            self.bNextTurn.grid(column = 3, row = 0)

            self.bStart = Button(self, text="Start", command=self.Start)
            self.bStart.grid(column = 3, row = 1)
            self.bStop = Button(self, text="Stop", command=self.Stop)
            self.bStop.grid(column = 3, row = 2)

            self.bind("<space>", lambda e : self.NextTurnBind())

        self.lbl1 = StringVar()
        Label(self, textvariable=self.lbl1).grid(column = 0, row =0)

        self.canvas.create_window(0, 0, window=self.grid)
        self.grid.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.bind_all("<MouseWheel>", lambda e: self.Scroll(self.canvas, e))

    def Update(self):
        pos = self.grid.currentSelect
        ant = self.Map.layerSolid[pos[0], pos[1]]
        floor=self.Map.layerFloor[pos[0],pos[1]]
        pheromone=self.Map.layerPheromone[pos[0],pos[1]]
        self.UpdateLabel(ant,floor,pheromone)

    def UpdateLabel(self, ant,floor,pheromone):
        if isinstance(ant, Ant):
            self.lbl1.set(str(ant) + str(self.grid.currentSelect)) #displays attributes and position of the clicked ant
        #if it isn't an ant, displays what is on the cell
        else:
            self.lbl1.set("cellPosition :" + str(self.grid.currentSelect)+"\n"+\
                          "floor :" + str(floor)+"\n"+\
                          "solid :" + str(ant)+"\n"+\
                          "pheromone :" + str(pheromone))


        self.update_idletasks()


    def Scroll(self, canvas, event):
        if event.state & 4:
            global tileSize
            tileSize+= event.delta // 120

            for row in self.grid:
                for it in row:
                    it.configure(width=tileSize, height=tileSize)

            canvas.update_idletasks()
            self.update_idletasks()

        elif event.state & 1:
            canvas.xview_scroll(-event.delta // 120, "units")
        else:
            canvas.yview_scroll(-event.delta // 120, "units")

    def Win(self):
        self.canvas.delete("all")
        self.bNextTurn.destroy()
        self.canvas.configure(bg='forest green')
        self.canvas.create_text(0,0,fill = 'orange',font='systemfixed 14 bold', text="Game's over !\
         Congratulations to the winning" + self.TurnManager.winningTeam + " player !")

    def NextTurnBind(self):
        if not self.startFlag:
            self.NextTurn()

    def NextTurn(self):

        #each time the NextTurn button is pressed, it checks wether the game is ended or not
        if self.TurnManager.winAchieved==True:
            self.Win()
        else :
            self.TurnManager.NextTurn()

    def Run(self):
        self.mainloop()

    def Start(self):
        self.startFlag = True
        self.LoopTurn()

    def Stop(self):
        self.startFlag = False

    def LoopTurn(self):
        if self.startFlag:
            self.NextTurn()
            self.after(100, self.LoopTurn)



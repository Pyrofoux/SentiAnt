from tkinter import Tk
from Sentiant.DataAccess.BotImport import BotImport

class ImportView(Tk):

    queens = []

    def __init__(self):
        Tk.__init__(self)
    def __init__(self, Prout):
        Tk.__init__(self)

        self.Prout = Prout

        self.bot = BotImport(self, "Sentiant\\Player", self.BotImportHandler)
        self.bot.LoadAll()
        self.bot.pack()

    def Run(self):
        self.mainloop()

    def BotImportHandler(self, p):
        self.queens = p
        self.Prout(p)

from tkinter import Toplevel
from Sentiant.DataAccess.botImport import BotImport

class ImportView(Toplevel):

    queens = []

    def __init__(self):
        Toplevel.__init__(self)


        self.bot = BotImport(self, "Sentiant\\Player", self.BotImportHandler)
        self.bot.LoadAll()
        self.bot.pack()

    def Run(self):
        self.mainloop()

    def BotImportHandler(self, p):
        self.queens = p
        self.quit()
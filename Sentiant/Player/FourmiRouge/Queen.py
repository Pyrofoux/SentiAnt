from Sentiant.Model import *
from Sentiant.bot.FourmiRouge.FourmiRouge import FourmiRouge

class QueenRouge(Queen):
    def newTurn(self):
        self.SpawnAnt("test", FourmiRouge, self.SPAWN4)
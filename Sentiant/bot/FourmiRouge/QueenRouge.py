from Sentiant.Model import *
from Sentiant.bot.FourmiRouge.FourmiRouge import FourmiRouge

class QueenRouge(Queen):
    def newTurn(self,FOV):
        self.SpawnAnt("fourmiRouge1", FourmiRouge, self.SPAWN4)


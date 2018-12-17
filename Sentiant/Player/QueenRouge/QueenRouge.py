from Sentiant.Model import *
from Sentiant.Player.QueenRouge.FourmiRouge import FourmiRouge

class QueenRouge(Queen):
    def newTurn(self, fov):
        self.SpawnAnt("test", FourmiRouge, self.SPAWN4)
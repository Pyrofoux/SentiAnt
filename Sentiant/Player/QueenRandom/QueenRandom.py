from Sentiant.Model import Queen
from Sentiant.Player.QueenRandom.AntRandom import AntRandom
from random import *

class QueenRandom(Queen):

    def newTurn(self,fov):
        r=randrange(len(self.SPAWNS))
        n=randrange(99999)
        self.SpawnAnt(str(n),AntRandom, self.SPAWNS[r])


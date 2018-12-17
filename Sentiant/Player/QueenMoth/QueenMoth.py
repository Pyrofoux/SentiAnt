from Sentiant.Model import *
from Sentiant.Player.QueenMoth.Moth import Moth


# Spawn moths, whenever possible

class QueenMoth(Queen):

    moths = 0

    def newTurn(self, fov):

        spawn = None
        for i in range(len(fov[1])):
            if not(fov[1][i] is None) and fov[1][i] != fov[0][i]:
                spawn = fov[1][i]

        if not(spawn is None):
            self.SpawnAnt("Moth" + str(self.moths), Moth, spawn)
            self.moths += 1




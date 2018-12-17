from Sentiant.Model import *
from random import randrange

# Goal : Dig the map and bring resources eventually
class WorkerBee(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)
        self.direction = Cfg.DIRECTIONS[randrange(len(Cfg.DIRECTIONS))]

    def newTurn(self, FOV, Pheros):
        print(Cfg.FOV, self.direction.x, self.direction.y)
        FOVSolidFace = FOV[0][Cfg.FOV + self.direction.x][Cfg.FOV + self.direction.y]
        FOVFloorFace = FOV[1][Cfg.FOV + self.direction.x][Cfg.FOV + self.direction.y]
        FOVFloorHere = FOV[1][Cfg.FOV][Cfg.FOV]

        IsQueenAround = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if  i * j == 0 and (IsQueenAround or FOV[1][Cfg.FOV + i][Cfg.FOV + j] == Cfg.QUEEN):
                    IsQueenAround = True

        if FOVFloorFace == Cfg.COOKIE:
            if not(self._holding is None):
                self.Drop()
            else:
                self.Move(self.direction)

        elif not(FOVFloorHere  == Cfg.EMPTY) and self._holding is None and not(IsQueenAround):
            self.Pickup()

        elif IsQueenAround and not(self._holding is None) :
            self.Drop()

        elif FOVSolidFace == Cfg.EMPTY:
            self.Move(self.direction)

        elif FOVSolidFace == Cfg.DIRT:
            self.Dig(self.direction)

        # Ajouter une condition si fourmi ennemie
        else:
            self.direction = Cfg.DIRECTIONS[randrange(len(Cfg.DIRECTIONS))]
            self.Move(self.direction)

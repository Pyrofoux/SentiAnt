from Sentiant.Model import *
from random import randrange

# Goal : Dig the map
class DiggerBee(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)
        self.direction = Cfg.DIRECTIONS[randrange(len(Cfg.DIRECTIONS))]

    def newTurn(self, FOV, Pheros):
        print(Cfg.FOV, self.direction.x, self.direction.y)
        FOVface = FOV[0][Cfg.FOV + self.direction.x][Cfg.FOV + self.direction.y]
        WhatIsHere = FOV[1][Cfg.FOV][Cfg.FOV]

        if WhatIsHere == Cfg.BREAD:
            self.Phero(30)
        elif WhatIsHere == Cfg.COOKIE:
            self.Phero(32)

        if FOVface == Cfg.EMPTY:
            self.Move(self.direction)
        elif FOVface == Cfg.DIRT:
            self.Dig(self.direction)

        # Ajouter une condition si fourmi ennemie
        else:
            self.direction = Cfg.DIRECTIONS[randrange(len(Cfg.DIRECTIONS))]
            self.Move(self.direction)

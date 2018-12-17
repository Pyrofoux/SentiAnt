from Sentiant.Model import *
from random import randrange

class FourmiRouge(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)

    def newTurn(self, FOV, pheromones):
        if randrange(2) == 0:
            self.Phero(randrange(10))
        else :
            self.Move(Cfg.DIRECTIONS[randrange(len(Cfg.DIRECTIONS))])

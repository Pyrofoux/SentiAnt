from Sentiant.Model import *


class FourmiRouge(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)

    def newTurn(self):
        #self.Move(Cfg.DOWN)
        self.Phero(2)

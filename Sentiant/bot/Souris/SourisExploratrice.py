from Sentiant.Model import *

class SourisExploratrice(Ant):
    def __init__(self, id, name, team):
        super().__init__(id, name, team)

    def newTurn(self, FOV,pheromone):
        self.Move("UP")


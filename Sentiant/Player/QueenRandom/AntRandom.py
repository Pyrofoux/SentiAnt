from Sentiant.Model import Ant
from random import *

class AntRandom(Ant):

    def newTurn(self,fov,pheromone):
        self.directions = ["up", "down", "right", "left"]

        self.possibleActions = {
            0: self.Move,
            1: self.Attack,
            2: self.Dig,
            3: self.Phero,
            # below are the actions that don't need any argument
            4: self.Sleep,
            5: self.Drop,
            6: self.Pickup
        }

        r=randrange(4)
        a=randrange(7)
        s=randrange(31)

        if a<3:
            self.possibleActions[a](self.directions[r])
        elif a==3:
            self.possiblesActions[a](s)
        else:
            self.possibleActions[a]()


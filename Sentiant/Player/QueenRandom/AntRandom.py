from Sentiant.Model import Ant
from random import randrange

class AntRandom(Ant):

    def newTurn(self,fov,pheromone):
        self.directions = ["up", "down", "right", "left"]
        self.possibleActions = {
            0: self.Move,
            1: self.Move,
            2: self.Move,
            3: self.Phero,
            # below are the actions that don't need any argument
            4: self.Sleep,
            5: self.Drop,
            6: self.Pickup
        }
        r=randrange(4)
        a=0#randrange(7)
        s=randrange(31)

        if fov[0][0][0]=="Cookie":
            self.Pickup()
        elif self.getHolding()=="Cookie" and fov[0][-1][0]=="Queen":
            self.Drop()

        else :
            if a<3:
                self.possibleActions[a](self.directions[r])
            elif a==3:
                self.possibleActions[a](s)
            else:
                self.possibleActions[a]()


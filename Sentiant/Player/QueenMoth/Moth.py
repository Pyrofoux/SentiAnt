from Sentiant.Model import *
from random import randrange

# Goal : Dig the map and bring resources eventually
class Moth(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)

        self.pathLength = round((Cfg.WIDTH+Cfg.HEIGHT)/2)+1
        self.path = self.generatePath()
        self.forward = True
        self.step = -1
        self.ignoreNextPick = False
        self.path2dir = {
            True:["up","right","down","left"],
            False:["down","left","up","right"]
        }

    def generatePath(self):
        return [randrange(4) for i in range(0,self.pathLength) ]


    def nextStep(self):

        endOfPath = False
        if(self.forward):
            self.step += 1
        else:
            self.step -= 1

        if self.step >= len(self.path):
            self.step = len(self.path)-1
            self.forward = False
        elif self.step < 0:
            endOfPath = True


        if(not endOfPath):

            nextDir = self.path2dir[self.forward][self.path[self.step]]



            self.Move(nextDir)
        else:
            self.newPath()

    def newPath(self):

        self.path = self.generatePath()
        self.step = 0
        self.forward = True

        if self.getHolding() != Cfg.EMPTY:
            self.Drop()
            #Make a move in order to stupidly pick up the same bread over and over...
            self.ignoreNextPick = True


    def newTurn(self, FOV, Pheros):

        if (self.step == -1): #Booting...
            self.nextStep()
            return True

        direc =  self.path2dir[self.forward][self.path[self.step]]
        direction = Cfg.ParseDirection(direc)

        facing = FOV[0][Cfg.FOV + direction.x][Cfg.FOV + direction.y]
        here = FOV[1][Cfg.FOV][Cfg.FOV]

        if here != Cfg.EMPTY and self.getHolding() == Cfg.EMPTY:

            if(self.ignoreNextPick):

                self.ignoreNextPick = False
                self.nextStep()
            else :
                self.Pickup()
                if(self.forward):
                    self.forward = False

        elif facing == Cfg.DIRT:
            self.Dig(direc)
        elif facing == Cfg.ANT:
            #self.nextStep(True)
            if(randrange(0,6) == 0):
                self.nextStep()
        else :
            self.nextStep()
from .Cfg import Cfg
from .Ant import Ant

class TurnManager:

    currentTurn = 0
    layerSolid = None
    layerFloor = None
    layerPheromone = None

    def __init__(self, _layerSolid, _layerFloor, _layerPheromone):

        self.currentTurn = 0
        self.layerSolid = _layerSolid
        self.layerFloor = _layerFloor
        self.layerPheromone = _layerPheromone


    def nextTurn(self, ):
        self.currentTurn += 1

        allAnts = self.layerSolid.ToList(Ant)
        sorted = {}

        sorted[Cfg.SLEEP] = []
        sorted[Cfg.ATTACK] = []
        sorted[Cfg.DIG] = []
        sorted[Cfg.PICKUP] = []
        sorted[Cfg.DROP] = []
        sorted[Cfg.PHERO] = []
        sorted[Cfg.MOVE] = []


        for ant in allAnts :

            if ant._nextAction in Cfg.ACTIONS  :
                sorted[ant._nextAction].append(ant)

        self.execSleep(sorted[Cfg.Cfg.SLEEP])



    def execSleep(self, ants):
        pass

    def execPhero(self,ants):
        pass

    def execAttack(self,ants):
        pass

    def execMove(self,ants):
        pass

    def execDig(self,ants):

        for ant in ants:

            posAnt = self.layerSolid.GetXYByRef(ant)
            dir = ant._nextActionArg
            posCible = posAnt + dir

           # if  self.layerSolid[posCible.x, posCible.y] instanceof Dirt


        pass

    def execPickup(self):
        pass

    def execDrop(self):
        pass


if __name__ == '__main__':
    "sup"
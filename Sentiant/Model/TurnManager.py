from .Cfg import Cfg
from .Layer import LayerSolid
from .Layer import LayerFloor
from .Layer import LayerPheromone
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




    def execSleep(self):
        pass

    def execPhero(self):
        pass

    def execAttack(self):
        pass

    def execMove(self):
        pass

    def execDig(self):
        pass

    def execPickup(self):
        pass

    def execDrop(self):
        pass



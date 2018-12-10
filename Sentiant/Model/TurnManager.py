from .Cfg import Cfg
from .Ant import Ant
from .Dirt import Dirt
from .Bread import Bread
from .Cookie import Cookie
from .Pheromone import Pheromone

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

        #Checker l'ordre des actions depuis le doc
        self.execSleep(sorted[Cfg.Cfg.SLEEP])
        self.execPhero(sorted[Cfg.Cfg.PHERO])
        self.execAttack(sorted[Cfg.Cfg.ATTACK])
        self.execMove(sorted[Cfg.Cfg.MOVE])
        self.execDig(sorted[Cfg.Cfg.DIG])
        self.execPICKUP(sorted[Cfg.Cfg.PICKUP])
        self.execDROP(sorted[Cfg.Cfg.DROP])



    def execSleep(self, ants):
        pass

    def execPhero(self,ants):

        for ant in ants:
            self.layerPheromone.Place(ant, ant._nextActionArg)


    def execAttack(self,ants):
        pass

    def execMove(self,ants):
        pass

    def execDig(self,ants):

        for ant in ants:

            posAnt = self.layerSolid.GetXYByRef(ant)
            dir = ant._nextActionArg
            posCible = posAnt + dir
            cible = self.layerSolid[posCible.x, posCible.y]

            if  cible is Dirt:
                self.layerSolid.Remove(cible)

    def execPickup(self, ants):

        for ant in ants:

            posAnt = self.layerSolid.GetXYByRef(ant)
            cible = self.layerFloor[posAnt.x, posAnt.y]


            if ant._holding is None :

                if  cible is  Bread :
                    self.layerFloor.Remove(cible)
                    ant._holding = Bread(cible.id)

                elif cible is  Cookie :
                    self.layerFloor.Remove(cible)
                    ant._holding = Cookie(cible.id)


    def execDrop(self, ants):

        for ant in ants:
            posAnt = self.layerSolid.GetXYByRef(ant)


            if ant._holding is Bread :

                self.layerFloor.Append(Bread(ant._holding.id))
                ant._holding = None

            if ant._holding is Cookie :

                self.layerFloor.Append(Cookie(ant._holding.id))
                ant._holding = None


if __name__ == '__main__':
    "sup"
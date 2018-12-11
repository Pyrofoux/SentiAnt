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


    def NextTurn(self):
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
        self.ExecSleep(sorted[Cfg.Cfg.SLEEP])
        self.ExecPhero(sorted[Cfg.Cfg.PHERO])
        self.ExecAttack(sorted[Cfg.Cfg.ATTACK])
        self.ExecMove(sorted[Cfg.Cfg.MOVE])
        self.ExecDig(sorted[Cfg.Cfg.DIG])
        self.ExecPICKUP(sorted[Cfg.Cfg.PICKUP])
        self.ExecDROP(sorted[Cfg.Cfg.DROP])



    def ExecSleep(self, ants):
        pass

    def ExecPhero(self,ants):

        for ant in ants:
            self.layerPheromone.Place(ant, ant._nextActionArg)


    def ExecAttack(self,ants):
        pass

    def ExecMove(self,ants):
        pass

    def ExecDig(self,ants):

        for ant in ants:

            posAnt = self.layerSolid.GetXYByRef(ant)
            dir = ant._nextActionArg
            posCible = posAnt + dir
            cible = self.layerSolid[posCible.x, posCible.y]

            if  cible is Dirt:
                self.layerSolid.Remove(cible)

    def ExecPickup(self, ants):

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


    def ExecDrop(self, ants):

        for ant in ants:
            posAnt = self.layerSolid.GetXYByRef(ant)


            if ant._holding is Bread :

                self.layerFloor.Append(Bread(ant._holding.id))
                ant._holding = None

            if ant._holding is Cookie :

                self.layerFloor.Append(Cookie(ant._holding.id))
                ant._holding = None

from Sentiant.Model.Cfg import Cfg
from Sentiant.Model.Ant import Ant
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Bread import Bread
from Sentiant.Model.Cookie import Cookie
from Sentiant.Model.Pheromone import Pheromone

if __name__ == '__main__':
    print("sup")

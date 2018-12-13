class TurnManager:
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
        self.ExecSleep (sorted[Cfg.SLEEP])
        self.ExecPhero (sorted[Cfg.PHERO])
        self.ExecAttack(sorted[Cfg.ATTACK])
        self.ExecMove  (sorted[Cfg.MOVE])
        self.ExecDig   (sorted[Cfg.DIG])
        self.ExecPickup(sorted[Cfg.PICKUP])
        self.ExecDrop  (sorted[Cfg.DROP])

    def ExecSleep(self, ants):
        pass

    def ExecPhero(self, ants):
        for ant in ants:
            self.layerPheromone.Place(ant, ant._nextActionArg)

    def ExecAttack(self, ants):
        pass

    def ExecMove(self, ants):
        pass

    def ExecDig(self, ants):
        for ant in ants:
            posAnt = self.layerSolid.GetXYByRef(ant)
            dir = ant._nextActionArg
            posCible = posAnt + dir
            cible = self.layerSolid[posCible]

            if isinstance(cible, Dirt):
                self.layerSolid.Remove(cible)

    def ExecPickup(self, ants):
        for ant in ants:
            posAnt = self.layerSolid.GetXYByRef(ant)
            cible = self.layerFloor[posAnt]

            if ant._holding is None and isinstance(cible, (Bread, Cookie)):
                    self.layerFloor.Remove(cible)
                    ant.__setattr__('_holding', type(cible)(cible.id), "legit")

    def ExecDrop(self, ants):
        for ant in ants:
            posAnt = self.layerSolid.GetXYByRef(ant)

            if isinstance(ant._holding, (Bread, Cookie)):
                self.layerFloor.Append(type(ant._holding)(ant._holding.id))
                ant._holding = None


from Sentiant.Model.Cfg import Cfg
from Sentiant.Model.Ant import Ant
from Sentiant.Model.QueenTile import QueenTile
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Bread import Bread
from Sentiant.Model.Cookie import Cookie
from Sentiant.Model.Pheromone import Pheromone
from Sentiant.Model.Point import Point

if __name__ == '__main__':
    from Sentiant.Model.MapManager import MapManager

    mapGen = MapManager(width=16, height=16)
    mapGen.RegisterQueen(QueenTile(1, "team"), Point(4, 4))

    map = mapGen.Generate()

    a1, a2 = Ant(1, "name", "team"), Ant(1, "name", "team")
    map.layerSolid.Append(a1, Point(6, 7))
    map.layerSolid.Append(a2, Point(5, 3))

    tm = TurnManager(map.layerSolid, map.layerFloor, map.layerPheromone)

    a1.Move(Cfg.UP)
    a2.Pickup()
    tm.NextTurn()

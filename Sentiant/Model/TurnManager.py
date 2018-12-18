class TurnManager:
    def __init__(self, map, queenManager=None):
        self.currentTurn = 0

        self.map = map

        self.layerSolid = map.layerSolid
        self.layerFloor = map.layerFloor
        self.layerPheromone = map.layerPheromone

        self.queenManager = queenManager

        self.winAchieved=False #is used to stop the game when won by a team + travail non fini
        self.winningTeam=None

    def NextTurn(self):

        LogsManager.Info("NextTurn()")

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

        LogsManager.Info("All ants =  " + str(allAnts))
        for ant in allAnts :
            LogsManager.Info("Examining " + ant._name)
            ant.newTurn(self.map.GetFOV(ant), self.map.layerPheromone.DetectFromPos(ant))
            LogsManager.Info(ant._name+" wants to " + ant._nextAction)

            if ant._nextAction in Cfg.ACTIONS:
                sorted[ant._nextAction].append(ant)

        #Checker l'ordre des actions depuis le doc
        self.ExecSleep (sorted[Cfg.SLEEP])
        self.ExecPhero (sorted[Cfg.PHERO])
        self.ExecAttack(sorted[Cfg.ATTACK])
        self.ExecMove  (sorted[Cfg.MOVE])
        self.ExecDig   (sorted[Cfg.DIG])
        self.ExecPickup(sorted[Cfg.PICKUP])
        self.ExecDrop  (sorted[Cfg.DROP])

        if self.queenManager is not None:
            self.queenManager.NextTurn(self.currentTurn, self.map)

    def ExecSleep(self, ants):
        pass

    def ExecPhero(self, ants):
        for ant in ants:
            self.layerPheromone.Place(ant, ant._nextActionArg)

    def ExecAttack(self, ants):

        #toPunish = []

        for ant in ants:
            posAnt = self.layerSolid.GetXYByRef(ant)
            dir = ant._nextActionArg
            posCible = posAnt + dir
            cible = self.layerSolid[posCible]

            if isinstance(cible, Ant):
                self.Remove1HP(cible)

    def ExecMove(self, ants):

        movingAnts = []
        initialPositions = []
        desiredDestinations = []

        for ant in ants:
            #self.layerSolid.MoveEntity(ant, ant._nextActionArg)

            posAnt = self.layerSolid.GetXYByRef(ant)
            dir = ant._nextActionArg
            posCible = posAnt + dir
            cible = self.layerSolid[posCible]

            if cible is None or isinstance(cible, Ant): #Check les Ants qui rentrent pas dans un mur
                movingAnts.append(ant)
                initialPositions.append(posAnt)
                desiredDestinations.append(posCible)

        if len(movingAnts) > 0:
            punished = MoveManager.calculatePunished(initialPositions, desiredDestinations)
            indexToMove = []
            for i in range(0,len(movingAnts)):

                if i in punished: #
                    self.Remove1HP(movingAnts[i])
                else:
                    indexToMove.append(i)

            for i in range(0, len(indexToMove)):
                self.layerSolid.Remove(movingAnts[indexToMove[i]])
                self.layerSolid.Append(movingAnts[indexToMove[i]], desiredDestinations[indexToMove[i]])


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
                    ant.__setattr__('_holding', cible, "legit")

    def ExecDrop(self, ants):
        for ant in ants:
            posAnt = self.layerSolid.GetXYByRef(ant)

            if isinstance(ant._holding, (Bread, Cookie)) and self.layerFloor.IsNone(posAnt):
                self.layerFloor.Append(type(ant._holding)(ant._holding.id), self.map.layerSolid.GetXYByRef(ant))
                ant._holding = None
                #every time an ant drops a Cookie, it checks if there is a QueenTile next to the ant, because it means a win
                if (isinstance(ant._holding,Cookie) and (isinstance(posAnt+Cfg.UP,QueenTile) \
                                                        or isinstance(posAnt+Cfg.DOWN,QueenTile) \
                                                            or isinstance(posAnt + Cfg.LEFT, QueenTile) \
                                                                or isinstance(posAnt + Cfg.RIGHT, QueenTile))) :
                    self.winAchieved = True
                    self.winningTeam=ant._team
            else :
                pass
                # TODO : cancel ant action

    def Remove1HP(self, cible):

            # cible dead
            if cible._HP == 1:
                self.layerSolid.Remove(cible)
            # cible still alive
            else:
                cible._HP -= 1

from Sentiant.Model.Cfg import Cfg
from Sentiant.Model.Ant import Ant
from Sentiant.Model.QueenTile import QueenTile
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Bread import Bread
from Sentiant.Model.Cookie import Cookie
from Sentiant.Model.Pheromone import Pheromone
from Sentiant.Model.Point import Point
from Sentiant.Model.LogsManager import LogsManager
from Sentiant.Model.MoveManager import MoveManager

if __name__ == '__main__':
    from Sentiant.Model.MapManager import MapManager
    from Sentiant.View import MainView
    from Sentiant.Model import Cfg
    import os
    from tkinter import Button


    def DoAttack():
        print(a1)
        a2.Attack(Cfg.RIGHT)
        tm.NextTurn()
        print(a1)

    def DoMove():
        a1.Move(Cfg.LEFT)
        a2.Move(Cfg.RIGHT)


    os.chdir("..\\..\\")

    Cfg.NEST_RADIUS = 20

    mapGen = MapManager(width=16, height=16, breadAmount=0, rockRatio=0)
    mapGen.RegisterQueen(QueenTile(1, "team"), Point(8, 8))

    map = mapGen.Generate()

    a1, a2 = Ant(1, "name", "team"), Ant(2, "name", "team")
    map.layerSolid.Append(a1, Point(5, 5))
    map.layerSolid.Append(a2, Point(5, 4))

    tm = TurnManager(map)

    view = MainView(map, tm, (500, 500))
    Button(view, text="Attaque", command=lambda : DoAttack()).pack()
    Button(view, text="Move", command=lambda: DoMove()).pack()
    view.Run()

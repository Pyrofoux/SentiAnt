from Sentiant.Model.Point import Point
from Sentiant.Model import Cfg
from Sentiant.Model.QueenTile import QueenTile
from Sentiant.Model.Queen import Queen
from Sentiant.Model.Bread import Bread
import math, random


class QueensManager:


    def __init__(self, nbQueen, teamsName, queensType, mapManager = None):
        self.queens = {}
        self.nbQueen = nbQueen
        self.mapManager = mapManager

        self.SpawnQueens(teamsName, queensType)


    def SpawnQueens(self, teamsName, queensType):
        positions = self.GenerateQueenPosition()

        for i in range(self.nbQueen):
            position = positions.__next__()
            self.queens[str(position)] = queensType[i](teamsName[i])
            self.mapManager.RegisterQueen(QueenTile(1, teamsName[i]), position)


    def GenerateQueenPosition(self):
        partCircle = 2*math.pi/self.nbQueen

        radius = random.randrange(Cfg.MIN_SPAWN_QUEEN_RADIUS,round(self.mapManager.map.width / 2 * (1 - 1 / 4)) )
        increment = random.random() * 2*math.pi / 10

        for i in range(self.nbQueen):
            yield Point(round(self.mapManager.map.width//2 + radius*math.cos(i*partCircle + increment)),
            round(self.mapManager.map.height//2 + radius* math.sin(i * partCircle + increment)))

    def NextTurn(self, numTour, map):

        print("Queens turn")

        queensWhoWantSpawn = {}

        for i in self.queens.keys():
            self.queens[i].newTurn()
            if self.queens[i]._order == Cfg.QUEEN_SPAWN_ANT:
                queensWhoWantSpawn[i] = self.queens[i]

        self.SpawnAnt(queensWhoWantSpawn, map)
        print("Turn end")

    def SpawnAnt(self, queens, map):
        for q in queens.keys():
            point = Point.StringToPoint(q) + queens[q]._positionOrder
            if map.layerSolid.IsNone(point) and isinstance(map.layerFloor[point], Bread):
                map.layerSolid.Append(
                    queens[q]._spawnType(map.layerSolid.GetNewId(), queens[q]._nameSpawn, queens[q]._team),
                    point)
                map.layerFloor[point] = None
            queens[q]._order = Cfg.SLEEP
            queens[q]._positionOrder = None
            queens[q]._spawnType = None
            queens[q]._nameSpawn = ""

    def GetQueenPosition(self):
        result = []
        for k in self.queens.keys():
            result.append(k)
        return result







if __name__ == '__main__':
    from Sentiant.Model import MapManager, Ant
    from Sentiant.View import MainView
    import os
    from tkinter import Button

    class QueenTest(Queen):

        def newTurn(self):
            self.SpawnAnt("test", Ant, self.SPAWN1)

    def SpawnRess(map, position):
        map.layerFloor[position] = Bread(map.layerFloor.GetNewId())

    os.chdir("..\\..\\")

    mapGen = MapManager()

    qM = QueensManager(3, ["1", "2", "3"], [QueenTest, QueenTest, QueenTest] , mapGen)

    map = mapGen.Generate()

    view = MainView(map , size = (500, 500))

    position = Point.StringToPoint(qM.GetQueenPosition()[0]) + Queen.SPAWN1

    Button(view, command = lambda : SpawnRess(map, position)).pack()
    Button(view, text = "NextTurn", command=lambda : qM.NextTurn(1, map)).pack()

    view.Run()













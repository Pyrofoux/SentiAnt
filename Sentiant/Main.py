from Sentiant.Model import MapManager, QueenTile, Point
from Sentiant.View import MainView
from Sentiant.Model import TurnManager
import os


if __name__ == '__main__':

    os.chdir("..\\")

    mapGen = MapManager(width=10, height=10)
    mapGen.RegisterQueen(QueenTile(1, "team"), Point(1, 1))

    map = mapGen.Generate()



    turnmanager = TurnManager(map)

    view = MainView(map, turnmanager)


    view.Run();

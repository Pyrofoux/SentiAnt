from Sentiant.Model import MapManager, QueenTile, Point
from Sentiant.View import MainView
import os


if __name__ == '__main__':

    os.chdir("..\\")

    mapGen = MapManager(width=10, height=10)
    mapGen.RegisterQueen(QueenTile(1, "team"), Point(4, 4))

    map = mapGen.Generate()

    view = MainView(map)

    view.Run();

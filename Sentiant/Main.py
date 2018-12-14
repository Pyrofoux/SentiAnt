from Sentiant.Model import MapManager, QueenTile, Point
from Sentiant.View import MainView
from Sentiant.Model import TurnManager
from Sentiant.bot.FourmiRouge.FourmiRouge import FourmiRouge
import os


if __name__ == '__main__':

    #os.chdir("..\\")

    mapGen = MapManager(width=10, height=10)
    mapGen.RegisterQueen(QueenTile(1, "team1"), Point(1, 1))

    map = mapGen.Generate()

    #Ajout de la fourmi d'essai
    roger = FourmiRouge(0,"ROGER","red")
    map.layerSolid.Append(roger,Point(3,3))
    turnmanager = TurnManager(map)

    view = MainView(map, turnmanager, (500, 500))
    view.Run();

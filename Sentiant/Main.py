from Sentiant.Model import MapManager, QueenTile, Point, QueensManager, Queen
from Sentiant.View import MainView
from Sentiant.Model import TurnManager
from Sentiant.bot.FourmiRouge.FourmiRouge import FourmiRouge
from Sentiant.bot.FourmiRouge.QueenRouge import QueenRouge
import os


if __name__ == '__main__':

    os.chdir("..\\")

    mapGen = MapManager(width=25, height=25)

    qM = QueensManager(3, [1, 2, 3], [QueenRouge, QueenRouge, QueenRouge], mapGen)
    map = mapGen.Generate()

    turnmanager = TurnManager(map, qM)

    view = MainView(map, turnmanager, 500)
    view.Run()

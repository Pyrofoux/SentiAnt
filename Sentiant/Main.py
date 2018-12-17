from Sentiant.Model import MapManager, QueenTile, Point, QueensManager, Queen
from Sentiant.View import MainView
from Sentiant.Model import TurnManager
from Sentiant.bot.Bees.QueenBee import QueenBee
from Sentiant.bot.FourmiRouge.QueenRouge import QueenRouge
from Sentiant.bot.Souris.SourisReine import SourisReine
import os


if __name__ == '__main__':

    os.chdir("..\\")

    mapGen = MapManager()
    #bi=BotImpoir

    qM = QueensManager(3, [1, 2, 3], [QueenBee, QueenBee, QueenBee], mapGen)
    map = mapGen.Generate()

    turnmanager = TurnManager(map, qM)

    view = MainView(map, turnmanager, 500)
    view.Run()

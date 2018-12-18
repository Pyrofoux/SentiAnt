from Sentiant.Model import MapManager, QueenTile, Point, QueensManager, Queen
from Sentiant.View import MainView, ImportView
from Sentiant.Model import TurnManager, LogsManager
from Sentiant.bot.FourmiRouge.FourmiRouge import FourmiRouge
from Sentiant.bot.FourmiRouge.QueenRouge import QueenRouge
import os


if __name__ == '__main__':

    os.chdir("..\\")

    gen=open(LogsManager.finalPathGen,"w")
    use=open(LogsManager.finalPathUse,"w")
    gen.close()
    use.close() #automatically cleans the existing logs from a previous execution


    importBot = ImportView()
    importBot.Run()

    LogsManager.Info("Queens imported :\nnbqueens : {0}\nqueens :{1}"
                     .format(len(importBot.queens),
                             "\n".join(["{0} : {1}".format(i[1], i[0]) for i in importBot.queens])))

    mapgen = MapManager()

    qM = QueensManager(len(importBot.queens)
                       , [i[1] for i in importBot.queens]
                       , [i[0] for i in importBot.queens]
                       , mapgen)
    map = mapgen.Generate()

    turnmanager = TurnManager(map, qM)

    view = MainView(map, turnmanager, 500)
    view.Run()



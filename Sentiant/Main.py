from Sentiant.Model import MapManager, QueenTile, Point, QueensManager, Queen
from Sentiant.View import MainView, ImportView
from Sentiant.Model import TurnManager, LogsManager
from Sentiant.bot.FourmiRouge.FourmiRouge import FourmiRouge
from Sentiant.bot.FourmiRouge.QueenRouge import QueenRouge
import os

def Prout(bla):
    LogsManager.Info("Queens imported :\nnbqueens : {0}\nqueens :{1}" \
                     .format(len(bla), \
                             "\n".join(["{0}: {1}".format(i[1], i[0]) for i in bla])))

    mapgen = MapManager()

    qM = QueensManager(len(bla), \
                       [i[1] for i in bla], \
                       [i[0] for i in bla], \
                       mapgen)
    map = mapgen.Generate()

    turnmanager = TurnManager(map, qM)

    importBot.destroy()

    view = MainView(map, turnmanager, 500)
    view.Run()


if __name__ == '__main__':

    #os.chdir("..\\")

    gen = open(LogsManager.finalPathGen, "w")
    use = open(LogsManager.finalPathUse, "w")
    gen.close()
    use.close() #automatically cleans the existing logs from a previous execution


    importBot = ImportView(Prout)
    importBot.Run()

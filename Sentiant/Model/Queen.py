from Sentiant.Model import Cfg
from Sentiant.Model.Point import Point

class Queen:

    SPAWN1 = Point(0, -1)
    SPAWN2 = Point(1, -1)
    SPAWN3 = Point(-1, 0)
    SPAWN4 = Point(2, 0)
    SPAWN5 = Point(-1, 1)
    SPAWN6 = Point(2, 1)
    SPAWN7 = Point(0, 2)
    SPAWN8 = Point(1, 2)



    def __init__(self, team):

        #property
        self._team = team
        self._order = Cfg.SLEEP
        self._positionOrder = None
        self._spawnType = None
        self._nameSpawn = ""

    def SpawnAnt(self, name, type, position):


        self._order = Cfg.QUEEN_SPAWN_ANT
        self._positionOrder = position
        self._spawnType = type
        self._nameSpawn = name

    def newTurn(self, FOV):
        pass






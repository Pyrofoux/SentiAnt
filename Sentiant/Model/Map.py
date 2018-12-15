
from Sentiant.Model.Cfg import Cfg
from Sentiant.Model.Point import Point
import numpy as np

class Map:
    def __init__(self, w = Cfg.WIDTH, h = Cfg.HEIGHT):
        self.width = w
        self.height = h

        self.layerSolid = LayerSolid(w = self.width, h = self.height, map=self) # ants & blocks
        self.layerPheromone = LayerPheromone(w = self.width, h = self.height, map=self)
        self.layerFloor = LayerFloor(w = self.width, h = self.height, map=self) # cookies & bread

    def SetView(self, view):
        self.layerFloor.SetView(view)
        self.layerPheromone.SetView(view)
        self.layerSolid.SetView(view)

    def GetFOV(self, ref):
        """Renvoie deux arrays, le premier concerne les floor entities le second les solid"""
        coords = self.layerSolid.GetXYByRef(ref)

        FOVSolid = np.zeros(Cfg.FOV, Cfg.FOV)
        FOVFloor = np.zeros(Cfg.FOV, Cfg.FOV)

        for i in range(-3,3) : #TODO: A changer, ça peut tester en dehors de la map
            for j in range(-3,3):

                distance = abs(i) + abs(j)
                if distance <= 3 and self.IsDestinationVisible(coords, Point(coords.x + i, coords.y + j)):

                    if not(self.layerSolid[coords[0] + i, coords[1] + j] is None):
                        FOVSolid[i, j] = Cfg.EntityToType(self.layerSolid[coords[0] + i, coords[1] + j])

                    if not(self.layerFloor[coords[0] + i, coords[1] + j] is None):
                        FOVFloor[i, j] = Cfg.EntityToType(self.layerFloor[coords[0] + i, coords[1] + j])

        return [FOVSolid, FOVFloor]

    def IsDestinationVisible(self, coordsDebut, coordsFin):  # Fonction testée, elle fonctionne inchallah

        incrX = coordsFin.x - coordsDebut.x
        if incrX != 0:
            incrX = int(incrX / abs(incrX))

        incrY = coordsFin.y - coordsDebut.y
        if incrY != 0:
            incrY = int(incrY / abs(incrY))

        LogsManager.Info(incrX)
        LogsManager.Info(incrY)
        LogsManager.Info(self.layerSolid[coordsDebut.x + incrX, coordsDebut.y])
        LogsManager.Info(self.layerSolid[coordsDebut.x, coordsDebut.y + incrY])

        # Si on arrive à la case voulue, il existe un moyen de voir cette case à partir de caseDebut : on retourne True
        if coordsDebut == coordsFin :
            return True

        # Sinon, si on est pas sur la même colonne, qu'il n'y a pas d'objet bloquant la vision sur la colonne d'à côté, on teste la fonction en se plaçant sur la colonne d'à côté
        elif incrX != 0 and self.layerSolid[coordsDebut.x + incrX, coordsDebut.y] is None and self.IsDestinationVisible(Point(coordsDebut.x + incrX, coordsDebut.y), coordsFin):
            return True
        elif incrY != 0 and self.layerSolid[coordsDebut.x, coordsDebut.y + incrY] is None and self.IsDestinationVisible(Point(coordsDebut.x, coordsDebut.y + incrY), coordsFin):
            return True
        return False

# Please avoid cyclic imports.
from Sentiant.Model.Layer.LayerFloor import LayerFloor
from Sentiant.Model.Layer.LayerPheromone import LayerPheromone
from Sentiant.Model.Layer.LayerSolid import LayerSolid

if __name__ == '__main__':
    from Sentiant.Model.Ant import Ant
    from Sentiant.Model.MapManager import MapManager
    from Sentiant.Model.LogsManager import LogsManager
    from Sentiant.View.MainView import MainView
    from Sentiant.Model.QueenTile import QueenTile
    import os

    ant = Ant(0, "name", "team")

    os.chdir("..\\..\\")

    mapGen = MapManager(width=16, height=16)
    mapGen.RegisterQueen(QueenTile(1, "team1"), Point(1, 1))
    map = mapGen.Generate()

    map.layerSolid.Append(ant, Point(3, 3))

    antCoords = Point(3, 3)

    #print(map.IsDestinationVisible(antCoords, Point(4, 3)))
    #print(map.IsDestinationVisible(antCoords, Point(3, 4)))
    #print(map.IsDestinationVisible(antCoords, Point(2, 3)))

    view = MainView(map, size = (500, 500))
    view.Run();

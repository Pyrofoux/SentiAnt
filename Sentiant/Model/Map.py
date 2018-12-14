
from Sentiant.Model.Cfg import Cfg
import numpy as np
from Sentiant.Model.Point import Point

class Map:
    def __init__(self, w = Cfg.WIDTH, h = Cfg.HEIGHT):

        self.width = w
        self.height = h

        self.layerSolid = LayerSolid(w = self.width, h = self.height, map=self) # ants & blocks
        self.layerPheromone = LayerPheromone(w = self.width, h = self.height, map=self)
        self.layerFloor = LayerFloor(w = self.width, h = self.height, map=self) # cookies & bread

    def SetView(self, view):
        self.layerFloor.setView(view)
        self.LayerPheromone.setView(view)
        self.LayerSolid.setView(view)

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

    def IsDestinationVisible(self, coordsDebut, coordsFin):#TODO: Tester la fonction

        incrX = coordsDebut.x - coordsFin.x
        if incrX != 0:
            incrX = int(incrX / abs(incrX))
        incrY = coordsDebut.y - coordsFin.y
        if incrY != 0:
            incrY = int(incrY / abs(incrY))
        print(incrX)
        print(incrY)
        print(self.layerSolid[coordsDebut.x + incrX, coordsDebut.y])
        print(self.layerSolid[coordsDebut.x, coordsDebut.y + incrY])

        # Si on arrive à la case voulue, il existe un moyen de voir cette case à partir de caseDebut : on retourne True
        if coordsDebut.x == coordsFin.x and coordsDebut.y == coordsFin:
            return True

        # Sinon, si on est pas sur la même colonne, qu'il n'y a pas d'objet bloquant la vision sur la colonne d'à côté, on teste la fonction en se plaçant sur la colonne d'à côté
        elif incrX != 0 and self.layerSolid[coordsDebut.x + incrX, coordsDebut.y] is None and self.IsDestinationVisible( Point(coordsDebut.x + incrX, coordsDebut.y), coordsFin):
            return True

        # La même pour les lignes
        elif incrY != 0 and self.layerSolid[coordsDebut.x, coordsDebut.y + incrY] is None and self.IsDestinationVisible( Point(coordsDebut.x, coordsDebut.y + incrY), coordsFin):
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
    from Sentiant.Model.TurnManager import TurnManager

    ant = Ant(0, "name", "team")
    mapGen = MapManager(width=16, height=16)

    map = mapGen.Generate()

    map.layerSolid.Append(ant, Point(3, 3))
    LogsManager.Info(ant)

    print(map.layerSolid)
    print(map.IsDestinationVisible(Point(8, 3), Point(4, 3)))
    print(map.IsDestinationVisible(Point(8, 3), Point(3, 4)))
    print(map.IsDestinationVisible(Point(8, 3), Point(2, 3)))
    print(map.IsDestinationVisible(Point(8, 3), Point(3, 2)))

    turnmanager = TurnManager(map)
#Tacos
    view = MainView(map, turnmanager)

    view.Run();



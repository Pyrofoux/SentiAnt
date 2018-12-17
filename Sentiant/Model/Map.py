from Sentiant.Model.Cfg import Cfg
from Sentiant.Model.Point import Point

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

        fov = Cfg.FOV
        size = fov * 2 + 1

        FOVSolid = [[0 for i in range(size)] for i in range(size)]
        FOVFloor = [[0 for i in range(size)] for i in range(size)]

        for i in range(-fov, fov + 1) :
            for j in range(-fov, fov + 1):

                distance = abs(i) + abs(j)
                if coords[0] + i < 0 or coords[0] + i >= self.layerSolid.GetWidth() or\
                    coords[1] + j < 0 or coords[1] + j >= self.layerSolid.GetHeight():
                    FOVSolid[i + fov][j + fov] = Cfg.ROCK
                    FOVFloor[i + fov][j + fov] = Cfg.UNKNOWN
                elif distance <= fov and self.IsDestinationVisible(coords, Point(coords.x + i, coords.y + j)):


                    FOVSolid[i + fov][ j + fov] = Cfg.EntityToType(self.layerSolid[coords[0] + i, coords[1] + j])


                    FOVFloor[i + fov][ j + fov] = Cfg.EntityToType(self.layerFloor[coords[0] + i, coords[1] + j])

                else:
                    FOVSolid[i + fov][ j + fov] = Cfg.UNKNOWN
                    FOVFloor[i + fov][ j + fov] = Cfg.UNKNOWN

        return [FOVSolid, FOVFloor]

    def IsDestinationVisible(self, coordsDebut, coordsFin):  # Fonction testée, elle fonctionne inchallah

        incrX = coordsFin.x - coordsDebut.x
        if incrX != 0:
            incrX = int(incrX / abs(incrX)) #sens du déplacement en X : 1 ou -1

        incrY = coordsFin.y - coordsDebut.y
        if incrY != 0:
            incrY = int(incrY / abs(incrY)) #sens du déplacement en Y : 1 ou -1

        # Si on arrive à la case voulue, il existe un moyen de voir cette case à partir de caseDebut : on retourne True
        if coordsDebut == coordsFin:
            return True

        # Sinon, si on est pas sur la même colonne, qu'il n'y a pas d'objet bloquant la vision sur la colonne d'à côté, on teste la fonction en se plaçant sur la colonne d'à côté
        # Don't touch this, c'est dégueu mais ça fonctionne
        #j'adore le récursif
        if incrX != 0 and \
                ((Point(coordsDebut.x + incrX, coordsDebut.y) == coordsFin ) or \
                (self.layerSolid[coordsDebut.x + incrX, coordsDebut.y] is None and \
                 self.IsDestinationVisible(Point(coordsDebut.x + incrX, coordsDebut.y), coordsFin))):
            return True
        elif incrY != 0 and \
                ((Point(coordsDebut.x, coordsDebut.y + incrY) == coordsFin) or \
                (self.layerSolid[coordsDebut.x, coordsDebut.y + incrY] is None and \
                 self.IsDestinationVisible(Point(coordsDebut.x, coordsDebut.y + incrY), coordsFin))):
            return True
        return False

# Please avoid cyclic imports.
from Sentiant.Model.Layer.LayerFloor import LayerFloor
from Sentiant.Model.Layer.LayerPheromone import LayerPheromone
from Sentiant.Model.Layer.LayerSolid import LayerSolid

if __name__ == '__main__':
    from Sentiant.Model.Ant import Ant
    from Sentiant.Model.MapManager import MapManager
    from Sentiant.View.MainView import MainView
    from Sentiant.Model.QueenTile import QueenTile
    import os
    from Sentiant.Model import Cfg

    ant = Ant(0, "name", "team")

    Cfg.NEST_RADIUS = 20
    Cfg.FOV = 2

    os.chdir("..\\..\\")
    mapGen = MapManager(width=10, height=10)
    mapGen.RegisterQueen(QueenTile(1, "team1"), Point(5, 5))
    map = mapGen.Generate()

    map.layerSolid.Append(ant, Point(3, 3))

    #print(map.IsDestinationVisible(antCoords, Point(4, 3)))
    #print(map.IsDestinationVisible(antCoords, Point(7, 7)))
    #print(map.IsDestinationVisibe(antCoords, Point(2, 5)))
    print(map.GetFOV(ant))

    view = MainView(map, size = (500, 500))
    view.Run()

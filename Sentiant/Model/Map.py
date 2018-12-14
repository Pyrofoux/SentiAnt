from .Layer.LayerFloor import LayerFloor
from .Layer.LayerPheromone import LayerPheromone
from .Layer.LayerSolid import LayerSolid
from .Cfg import Cfg
import numpy as np



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

        for i in range(-3,3) :
            for j in range(-3,3):

                distance = abs(i) + abs(j)
                if (distance <= 3 and self.IsDestinationVisible(coords, [coords.x + i, coords.y + j])): #TODO: Ajouter une fonction pour vérifier si c'est pas caché

                    if not(self.layerSolid[coords[0] + i, coords[1] + j] is None):
                        FOVSolid[i, j] = Cfg.EntityToType(self.layerSolid[coords[0] + i, coords[1] + j])

                    if not(self.layerFloor[coords[0] + i, coords[1] + j] is None):
                        FOVFloor[i, j] = Cfg.EntityToType(self.layerFloor[coords[0] + i, coords[1] + j])

        return [FOVSolid, FOVFloor]

    def IsDestinationVisible(self, x, y):


        if x == 0 and y == 0:
            return True
        else if x != 0 and LayerSolid[x -1, y] is None :
            self.IsDestinationVisible(x-1, y)
        else if y!= 0 and LayerSolid[x, y -1 ] is None :
            self.IsDestinationVisible(x, y- 1)

    return False


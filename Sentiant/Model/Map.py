from .Layer.LayerFloor import LayerFloor
from .Layer.LayerPheromone import LayerPheromone
from .Layer.LayerSolid import LayerSolid
from .Cfg import Cfg

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

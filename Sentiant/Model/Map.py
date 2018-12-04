from Sentiant.Model.Layer import LayerPheromone, LayerFloor, LayerSolid
from Sentiant.Model import Cfg

class Map:
    def __init__(self):
        self.width = Cfg.WIDTH
        self.height = Cfg.HEIGHT

        self.layerSolid = LayerSolid() # ants & blocks
        self.layerPheromone = LayerPheromone()
        self.layerFloor = LayerFloor() # cookies & bread

    def SetView(self, view):
        self.layerFloor.setView(view)
        self.LayerPheromone.setView(view)
        self.LayerSolid.setView(view)

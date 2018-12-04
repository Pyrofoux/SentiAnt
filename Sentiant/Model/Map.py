from Sentiant.Model.Layer import LayerPheromone, LayerFloor, LayerSolid, _

class Map:
    def __init__(self):
        self.width = _.WIDTH
        self.height = _.HEIGHT

        self.layerSolid = LayerSolid() # ants & blocks
        self.layerPheromone = LayerPheromone()
        self.layerFloor = LayerFloor() # cookies & bread

    def SetView(self, view):
        self.layerFloor.setView(view)
        self.LayerPheromone.setView(view)
        self.LayerSolid.setView(view)

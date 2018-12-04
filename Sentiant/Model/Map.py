from Sentiant.Model.Layer import LayerPheromone, LayerFloor, LayerSolid, _

class Map:
    def __init__(self):
        self.width = _.width
        self.height = _.height

        self.layerSolid = LayerSolid() # ants & blocks
        self.layerPheromone = LayerPheromone()
        self.layerFloor = LayerFloor() # cookies & bread

    def SetView(self, view):
        self.layerFloor.setView(view)
        self.LayerPheromone.setView(view)
        self.LayerSolid.setView(view)

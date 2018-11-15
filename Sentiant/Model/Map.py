from Sentiant.Model.Layer import LayerPheromone, LayerFloor, LayerSolid

class Map:
    def __init__(self, width=42, height=42):
        self.width = width
        self.height = height

        self.layerSolid = LayerSolid() # ants & blocks
        self.layerPheromone = LayerPheromone()
        self.layerFloor = LayerFloor() # cookies

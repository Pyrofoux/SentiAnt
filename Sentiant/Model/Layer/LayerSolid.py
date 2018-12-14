from Sentiant.Model.Layer.Layer import Layer
from Sentiant.Model.Dirt import Dirt

class LayerSolid(Layer):

    def DiggyDiggyHole(self, coords):

        if type(self[coords.x, coords.y]) is Dirt:
            self[coords.x, coords.y] = None

        pass #TODO: log error


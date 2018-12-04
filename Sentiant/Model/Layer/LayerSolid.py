from .Layer import Layer
from Sentiant import *


class LayerSolid(Layer):

    def IsWall(self, coords):

        if not(self[coords] is None):
            return True

        return False

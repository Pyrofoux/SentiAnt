from .Layer import Layer

class LayerSolid(Layer):
    def IsWallNorth(self, ref):
        return False

    def IsWallSouth(self, ref):
        return False

    def IsWallEast(self, ref):
        return False

    def IsWallWeast(self, ref):
        return False

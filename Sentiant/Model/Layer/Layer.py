import numpy as np
from Sentiant.Model.Entity import Entity


class Layer(np.ndarray):

    LastId = 0

    view = None

    def __new__(cls,  w, h, *arg, **kwargs):
        return np.zeros((w, h)).view(cls)

    def __init__(self, w, h, map):
        super().__init__()
        self.viewGrid = None
        self.Map = map

    def __getitem__(self, item):
        if self.viewGrid is not None:
            self.viewGrid.Update(item[0], item[1])
        return super().__getitem__(item)

    def SetViewGrid(self, viewGrid):
        self.viewGrid = viewGrid

    def Append(self, entity, coord):
        """Append an entity (entity) on this Layer in position (x, y)"""
        if self[coord.x, coord.y] is None:
            self[coord.x, coord.y] = entity

    def ToList(self, eClass=None):
        """Get a list of all the entities on the layer"""
        return [it for it in self if it and (not eClass or type(it) == eClass)]

    def Remove(self, ref):
        """Remove an entity by reference (ref)"""
        coord = self.GetXYByRef(ref)
        self[coord.x, coord.y] = None

    def Pop(self, ref):
        """Pop an entity out of the layer by ref"""
        coord = self.GetXYByRef(ref)
        self.Remove(ref)
        return coord.x, coord.y

    def GetXYByRef(self, ref):
        """ Get position of an entity by reference (ref)"""
        for i in range(len(self)):
            for j in range(len(self[0])):
                if self[i][j] == ref:
                    return [i, j]

    def MoveEntity(self, ref, direction):
        coord=self.Pop(ref)
        self.Append(ref, coord.x + direction.x, coord.y + direction.y)

    def Count(self):
        """Get the number of entity on layer"""
        return len(self.ToList())

    def __iter__(self):
        """Get an iterator of this layer"""
        for i in range(self.width):
            for j in range(self.height):
                yield self[i, j]

    def ForEach(self, f):
        """Apply a function (f) to all entities of this layer"""
        for e in self:
            f(e)

    def GetWidth(self):
        return self.shape[0]

    def GetHeight(self):
        return self.shape[1]

    @staticmethod
    def GetNewId():
        """Get new id of entity for this layer"""
        Layer.LastId += 1
        return Layer.LastId

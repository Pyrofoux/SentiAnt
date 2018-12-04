import numpy as np
from Sentiant.Model.Entity import Entity


class Layer(np.ndarray):

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

    def Append(self, entity, x, y): #TODO : Mettre un seul objet coords plutôt que x et y ? / Log Errors
        """Append an entity (entity) on this Layer in position (x, y)"""
        if self[x, y] is None:
            self[x, y] = entity

    def ToList(self):
        """Get a list of all the entities on the layer"""
        return [it for it in self if it]  # This code is bad and you should feel bad

    def Remove(self, ref):
        """Remove an entity by reference (ref)"""
        coord = self.GetXYByRef(ref)
        self[coord[0], coord[1]] = None

    def Pop(self, coords):
        """Pop an entity out of the layer by ref"""
        ref = self[coords]
        self.Remove(self[coords])
        return ref

    def GetXYByRef(self, ref):
        """ Get position of an entity by reference (ref)"""
        for i in range(self.width):
            for j in range(self.height):
                if self[i][j]==ref:
                    return [i, j]

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

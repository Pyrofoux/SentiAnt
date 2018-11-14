from numpy import array

import Entity

class Layer(array):
    def __init__(self, w, h):
        self.width = w
        self.height = h

        super().__init__(self, (w, h), type=Entity)

    def Append(self, entity, x, y):
        self[x, y] = entity

    def ToList(self):
        return [it for it in self if it]

    def Remove(self, ref):
        pass

    def Pop(self, x, y):
        return None

    def GetXYByRef(self, ref):
        return [it for it in self if it is ref][0]

    def Count(self):
        return len(self.ToList())

    def __iter__(self):
        for i in range(self.width):
            for j in range(self.height):
                yield self[i, j]

    def ForEach(self, f):
        for e in self:
            f(e)

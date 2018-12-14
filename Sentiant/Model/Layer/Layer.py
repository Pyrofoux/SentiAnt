from Sentiant.Model.Point import Point

class Layer():

    LastId = 0

    def __init__(self, w, h, map = None):
        """Constructor
        w : Width
        h : Height
        map : ref of map"""
        self.viewGrid = None
        self.Map = map

        self.grid = [[None for j in range(w)] for i in range(h)]

    def __getitem__(self, item):
        return self.grid[item[0]][item[1]]

    def __setitem__(self, key, value):
        if self.viewGrid is not None:
            self.viewGrid.Update(key[0], key[1])
        self.grid[key[0]][key[1]] = value

    def SetViewGrid(self, viewGrid):
        """Add viewGrid reference"""
        self.viewGrid = viewGrid

    def Append(self, entity, coord):
        """Append an entity (entity) on this Layer in position (x, y)
        if there is already an entity in coord, do nothin and return false"""
        if self[coord.x, coord.y] is None:
            self[coord.x, coord.y] = entity
            return True
        return False

    def ToList(self, eClass=None):
        """Get a list of all the entities on the layer"""
        return [it for it in self if it and (not eClass or type(it) == eClass)]

    def Remove(self, ref):
        """Remove an entity by reference (ref)"""
        coord = self.GetXYByRef(ref)
        self[coord.x, coord.y] = None
        if self.viewGrid is not None:
            self.viewGrid.Update(coord[0], coord[1])

    def Pop(self, ref):
        """Pop an entity out of the layer by ref"""
        coord = self.GetXYByRef(ref)
        self.Remove(ref)
        return ref

    def Contain(self, ref):
        """return true if this layer contains ref"""
        c = 0
        while (c < len(self.ToList()) and self.ToList()[c] != ref) or c == len(self.ToList()):
            c += 1
        if c == len(self.ToList()):
            return False
        else :
            return True


    def GetXYByRef(self, ref):
        """ Get position of an entity by reference (ref)"""
        for i in range(self.GetWidth()):
            for j in range(self.GetHeight()):
                if self[i, j]==ref:
                    coord = Point(i, j)
                    return coord

    def MoveEntity(self, ref, direction):
        """Move an entity ref to direction"""
        coord=self.GetXYByRef(ref)
        self.Remove(ref)
        self.Append(ref, Point(coord.x + direction.x, coord.y + direction.y))

    def Count(self):
        """Get the number of entity on layer"""
        return len(self.ToList())

    def __iter__(self):
        """Get an iterator of this layer"""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                yield self[i, j]

    def ForEach(self, f):
        """Apply a function (f) to all entities of this layer"""
        for e in self:
            f(e)

    def GetWidth(self):
        return len(self.grid)

    def GetHeight(self):
        return len(self.grid[0])

    @staticmethod
    def GetNewId():
        """Get new id of entity for this layer"""
        Layer.LastId += 1
        return Layer.LastId

    def IsNone(self, coord):
        return self[coord] is None

if __name__ == '__main__':
    from Sentiant.Model.Entity import Entity
    from Sentiant.Model.Point import Point

    layer = Layer(10, 10)

    print(layer.GetHeight())
    print(layer.GetWidth())

    entity = Entity()

    layer.Append(entity, Point(0,0))

    print(layer[Point(0,0)])
    print(layer[0,0])

    print(layer.Append(entity, Point(0,0)))

    layer.Append(Entity(2), Point(5,5))
    print(layer.ToList())

    print(layer.GetXYByRef(entity).x)
    print(layer.GetXYByRef(entity).y)

    layer.Remove(entity)

    print(layer.ToList())

    layer.Append(entity, Point(0, 0))

    print(layer.Pop(entity))

    print(layer.ToList())

    layer.Append(entity, Point(0, 0))

    layer.MoveEntity(entity, Point(1,1))

    print(layer.GetXYByRef(entity).x)
    print(layer.GetXYByRef(entity).y)

    print(layer.ToList())
    print(layer.Count())

    layer.Append(Entity(Layer.GetNewId()), Point(9, 9))

    for v in layer:
        pass
    print(v)

    def IDPlusOne(e):
        if isinstance(e, Entity):
            e.id += 1
    print(entity.id)
    layer.ForEach(IDPlusOne)
    print(entity.id)

    print(layer.Contain(entity))

    print(layer.IsNone(Point(6,6)))

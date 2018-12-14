from Sentiant.Model.Layer.Layer import Layer

class LayerFloor(Layer):

    def Gather(self, ref):
        """Ant (ref) gather an entity on his case"""
        # TODO : Log d'erreurs
        if self.IsResourceBelow(ref):
            coords = self.Map.layerSolid.GetXYByRef(ref)
            ref._holding = self.Map.layerFloor.Pop(self.Map.layerFloor[coords])

    def Drop(self, ref):
        """Ant (ref) drop an entity on his case"""
        #TODO : Log d'erreurs

        if not(ref._holding is None):
            coords = self.Map.layerSolid.GetXYByRef(ref)
            self.Append(ref._holding, coords)
            ref._holding = None

    def IsResourceBelow(self, ref):
        """Is Ressource below Ant(ref)"""

        coords = self.Map.layerSolid.GetXYByRef(ref)
        if not(self[coords.x, coords.y] is None):
            return True
        return False

if __name__ == '__main__':
    from Sentiant.Model.Map import Map
    from Sentiant.Model.Ant import Ant
    from Sentiant.Model.Point import Point
    from Sentiant.Model.Bread import Bread

    map = Map(10, 10)

    ant = Ant(1, "", "")
    point = Point(5,5)

    bread = Bread(0)

    map.layerSolid.Append(ant, point)
    map.layerFloor.Append(bread, point)

    map.layerFloor.Gather(ant)

    print(ant)

    map.layerFloor.Drop(ant)

    print(ant)

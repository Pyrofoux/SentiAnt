from .Layer import Layer

class LayerFloor(Layer):

    def Gather(self, ref):
        """Ant (ref) gather an entity on his case"""
        # TODO : Log d'erreurs
        if self.IsResourceBelow(ref):
            coords = self.Map.LayerSolid.GetXYByRef(ref)
            ref.pickup(self[coords.x, coords.y])
            self.Remove(self[coords.x, coords.y])

        pass

    def Drop(self, ref):
        """Ant (ref) drop an entity on his case"""
        #TODO : Log d'erreurs

        if not(ref.holding is None):
            coords = self.Map.LayerSolid.GetXYByRef(ref)

            self.Append(ref.holding, coords.x, coords.y)
            ref.drop()

        pass

    def IsResourceBelow(self, ref):
        """Is Ressource below Ant(ref)"""

        coords = self.Map.LayerSolid.GetXYByRef(ref)
        if not(self[coords.x, coords.y] is None):
            return True
        return False

from .Layer import Layer

class LayerFloor(Layer):

    def Gather(self, ref):
        """Ant (ref) gather an entity on his case"""
        # TODO : Log d'erreurs
        if self.IsResourceBelow(ref):
            coords = self.Map.LayerSolid.GetXYByRef(ref)
            ref.pickup(self[coords])
            self.Remove(self[coords])

        pass

    def Drop(self, ref):
        """Ant (ref) drop an entity on his case"""
        #TODO : Log d'erreurs

        if not(ref.holding is None):
            coords = self.Map.LayerSolid.GetXYByRef(ref)

            self.Append(ref.holding, coords[0], coords[1])
            ref.drop()

        pass

    def IsResourceBelow(self, ref):
        """Is Ressource below Ant(ref)"""

        coords = self.Map.LayerSolid.GetXYByRef(ref)
        if not(self[coords] is None):
            return True
        return False

from .Layer import Layer

class LayerFloor(Layer):

    def Gather(self, ref):
        """Ant (ref) gather an entity on his case"""
        pass

    def Drop(self, ref):
        """Ant (ref) drop an entity on his case"""
        pass

    def IsResourceBelow(self, ref):
        """Is Ressource below Ant(ref)"""
        return False

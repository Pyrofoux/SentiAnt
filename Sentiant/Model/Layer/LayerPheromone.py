import Layer
from Sentiant.Model.Pheromone import *

class LayerPheromone(Layer):
    def Place(self, ref, phéro):
        """Ant(ref) place a pheromone"""
        coords = self.Map.LayerSolid.GetXYByRef(ref)
        self[coords] = phéro

        pass

    def DetectFromPos(self, ref):
        """Ant(ref) detect pheromones"""
        coords = self.Map.LayerSolid.GetXYByRef(ref)

        phéros = []

        for phéro in self:
            coordsPhéro = self.GetXYByRef(phéro)
            distance = abs(coords[0] - coordsPhéro[0]) + abs(coords[1] - coordsPhéro[1])
            if (distance < phéro.hp):
                phéros.append(phéro)

        return phéros

from .Layer import Layer
from Sentiant.Model.Pheromone import *

class LayerPheromone(Layer):
    def Place(self, ref, scent):
        """Ant(ref) place a pheromone"""
        coords = self.Map.LayerSolid.GetXYByRef(ref)
        self[coords.x, coords.y] = Pheromone(scent, coords)

        pass

    def DetectFromPos(self, ref):
        """Ant(ref) detect pheromones"""
        coords = self.Map.LayerSolid.GetXYByRef(ref)

        phéros = []

        for phéro in self:
            coordsPhéro = phéro.baseLocation
            distance = abs(coords.x - coordsPhéro.x) + abs(coords.y - coordsPhéro.y)
            if (distance < phéro.hp):
                phéros.append(phéro)

        return phéros

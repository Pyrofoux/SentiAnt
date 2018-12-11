from Sentiant.Model.Layer.Layer import Layer

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
            # Bien les noms de var avec des accents...
            coordsPhéro = phéro.baseLocation
            distance = abs(coords.x - coordsPhéro.x) + abs(coords.y - coordsPhéro.y)
            if (distance < phéro.hp):
                phéros.append(phéro)

        return phéros

from Sentiant.Model.Pheromone import Pheromone

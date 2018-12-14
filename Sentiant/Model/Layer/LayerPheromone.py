from Sentiant.Model.Layer.Layer import Layer
from Sentiant.Model.Pheromone import Pheromone

class LayerPheromone(Layer):
    def Place(self, ref, scent):
        """Ant(ref) place a pheromone"""
        coords = self.Map.layerSolid.GetXYByRef(ref)
        self[coords.x, coords.y] = Pheromone(scent, coords)

        pass

    def DetectFromPos(self, ref):
        """Ant(ref) detect pheromones"""
        coords = self.Map.layerSolid.GetXYByRef(ref)

        phéros = []

        for phéro in self.ToList():
            # Bien les noms de var avec des accents...
            coordsPhéro = phéro.baseLocation
            distance = abs(coords.x - coordsPhéro.x) + abs(coords.y - coordsPhéro.y)
            if distance <= phéro.hpRadius:
                phéros.append(phéro)

        return phéros

if __name__ == '__main__':
    from Sentiant.Model.Map import Map
    from Sentiant.Model.Ant import Ant
    from Sentiant.Model.Point import Point

    map = Map(10, 10)

    ant = Ant(0, "", "")
    point = Point(5,5)

    map.layerSolid.Append(ant, point)

    map.layerPheromone.Place(ant, 0)

    print(map.layerPheromone.DetectFromPos(ant))

    ant2 = Ant(1, "", "")
    map.layerSolid.Append(ant2, Point(0,0))

    print(map.layerPheromone.DetectFromPos(ant2))

    ant2 = Ant(2, "", "")
    map.layerSolid.Append(ant2, Point(3, 2))

    print(map.layerPheromone.DetectFromPos(ant2))







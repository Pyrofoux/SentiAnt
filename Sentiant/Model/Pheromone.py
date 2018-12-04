from .Entity import Entity

class Pheromone(Entity):

    def __init__(self, id, baseLocation):
        self.hpRadius = Cfg.HPRADIUS
        self.id = id
        (self.baseLocationX, self.baseLocationY) = baseLocation

        pass

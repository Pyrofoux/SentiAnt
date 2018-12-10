from .Entity import Entity
from .Cfg import Cfg

class Pheromone(Entity):

    def __init__(self, scent, baseLocation):
        self.hpRadius = Cfg.HPRADIUS
        self.scent = scent
        self.baseLocation = baseLocation

        pass

    def __str__(self):
        return "Phero ["+self.scent+"] ("+self.baseLocation+")"
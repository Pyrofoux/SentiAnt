from Sentiant.Model.Entity import Entity

class Pheromone(Entity):

    def __init__(self, scent, baseLocation):
        self.hpRadius = Cfg.HPRADIUS
        self.scent = scent
        self.baseLocation = baseLocation

        pass

    def __str__(self):
        return "Phero ["+str(self.scent) +"] ("+str(self.baseLocation)+")"

from Sentiant.Model.Cfg import Cfg

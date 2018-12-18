from Sentiant.Model.Entity import Entity
from Sentiant.Model.Cfg import Cfg

class Pheromone(Entity):

    def __init__(self, scent, baseLocation):
        self.hpRadius = Cfg.HPRADIUS
        self.scent = scent
        self.baseLocation = baseLocation

        pass

    def __repr__(self):
        return self.__str__()

    def DegradePhero(self):
        self.hpRadius = self.hpRadius-1

    def __str__(self):
        return "Phero ["+str(self.scent) +"] ("+str(self.baseLocation)+")" + "HP :" + str(self.hpRadius)

from Sentiant.Model import *

class Pheromone:

    def __init__(self, id, baseLocation):
        self.hpRadius = Cfg.HPRADIUS
        self.id = id
        (self.baseLocationX, self.baseLocationY) = baseLocation

        pass

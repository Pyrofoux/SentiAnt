from Sentiant.Model import *


# Goal : bring resources from warehouse to tha queen
class NurseBee(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)
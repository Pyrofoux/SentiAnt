from Sentiant.Model import *


# Goal : Bring resources to the warehouse
class ResourceBee(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)
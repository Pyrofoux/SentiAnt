from Sentiant.Model.FloorEntity import FloorEntity
from Sentiant.Model.Cfg import Cfg

class Dirt(FloorEntity):

    removable = True

    def __init__(self, id):
        super().__init__(id)

    def __str__(self):
        return Cfg.DIRT

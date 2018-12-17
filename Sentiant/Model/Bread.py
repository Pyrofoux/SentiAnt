from Sentiant.Model.FloorEntity import FloorEntity
from Sentiant.Model.Cfg import Cfg

class Bread(FloorEntity):

    def __init__(self, id):
        super().__init__(id)

    def __str__(self):
        return Cfg.BREAD

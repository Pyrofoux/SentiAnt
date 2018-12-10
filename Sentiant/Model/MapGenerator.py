from random import Random

from Sentiant.Model.Layer import *
from Sentiant.Model.Cfg import Cfg

class MapGenerator:
    def __init__(self):
        super().__init__(self)

        self.map = None
        self.rockRatio = .06
        self.breadAmount = 42

    def settings(width=Cfg.WIDTH, height=Cfg.HEIGHT, \
                 rockRatio=.06, breadAmount=42):
        self.map = Map(w=width, h=height)
        self.rockRatio = rockRatio
        self.breadAmount = breadAmount

    def generate(self):
        """Generate and returns maps according to settings"""
        return self.map

from Sentiant.Model import *


class Ant(SolidEntity):

    def __init__(self, id, name, team):
        super().__init__(self, id)
        self._name = name # id of the ant, string of 5 chars
        self._team = team
        self._holding = None # by default, the ant doesn't carry anything
        self._HP = Cfg.HPMAX  # number of hits the ant can take before dying
        self._FoV = Cfg.FOV # Field Of View : number of cells the ant can view, center being itself

        self._nextAction = Cfg.SLEEP # next Action, will be read by Turn Manager
        self._nextActionArg = Cfg.NULL


    def move(self, direction):
        pass

    def pickup(self,entity):
        """Store the picked up entity in Ant.holding"""
        if (self.holding is None):
            self.holding = entity

    def drop(self):
        """Empty the Ant.holding if it isn't None """
        if (self.holding is None)== False:
            self.holding = None








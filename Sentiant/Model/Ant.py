from Sentiant.Model import SolidEntity
from Sentiant.Model import _


class Ant(SolidEntity):

    def __init__(self, id, name, team):
        super().__init__(self,id)
        self._name = name #id of the ant, string of 5 chars
        self._team = team
        self.holding = None #by default, the ant doesn't carry anything
        self.HP = _.HPMax  #number of hits the ant can take before dying
        self._FoV= _.FoV  #Field Of View : number of cells the ant can view, center being itself

    def pickup(self,entity):
        """Store the picked up entity in Ant.holding"""
        if (self.holding is None):
            self.holding = entity

    def drop(self):
        """Empty the Ant.holding if it isn't None """
        if (self.holding is None)== False:
            self.holding = None






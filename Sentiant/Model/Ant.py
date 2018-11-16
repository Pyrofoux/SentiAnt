from Sentiant.Model import SolidEntity

class Ant(SolidEntity):

    HP = 2

    def __init__(self,id,name,team):
        super().__init__(self,id)
        self.name = name
        self.team = team
        self.holding=None

    def pickup(entity):
        if (self.holding is None):
            self.holding=entity

    def drop(self.holding):
        if (self.holding is None)== False:
            self.holding=None






        pass


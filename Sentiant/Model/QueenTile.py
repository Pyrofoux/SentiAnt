from .SolidEntity import SolidEntity

class QueenTile(SolidEntity):

    def __init__(self, id, team):
        SolidEntity.__init__(id)
        self.team = team
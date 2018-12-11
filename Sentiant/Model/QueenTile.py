from Sentiant.Model.SolidEntity import SolidEntity

class QueenTile(SolidEntity):

    def __init__(self, id, team):
        super().__init__(id)
        self.team = team

    def __str__(self):
        return "QueenTile #" + str(self.id)

from Sentiant.Model import *


# Goal : Manage the stocks (phero donnant cb de ressources en stock etc)
class WarehouseBee(Ant):

    def __init__(self, id, name, team):
        super().__init__(id, name, team)
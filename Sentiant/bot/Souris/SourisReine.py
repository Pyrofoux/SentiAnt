from Sentiant.Model import *
from Sentiant.bot.Souris.SourisExploratrice import SourisExploratrice

class SourisReine(Queen):
    def newTurn(self):
        self.SpawnAnt("Polyvalente", SourisExploratrice, self.SPAWN5)
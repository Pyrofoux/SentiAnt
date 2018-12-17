from Sentiant.Model import *
from Sentiant.bot.Bees.DiggerBee import DiggerBee
from Sentiant.bot.Bees.NurseBee import NurseBee
from Sentiant.bot.Bees.ResourceBee import ResourceBee
from Sentiant.bot.Bees.SoldierBee import SoldierBee
from Sentiant.bot.Bees.WarehouseBee import WarehouseBee

# Goal : spawn bees when possible

class QueenBee(Queen):

    NbResourceBees = 0
    NbDiggerBees = 0
    NbNurseBees = 0
    NbWarehouseBees = 0
    NbSoldierBees = 0

    def newTurn(self): # Peut-être checker un jour si une ressource est dispo, ce serait intelligent x)



        if self.NbWarehouseBees == 0:
            self.SpawnAnt("Warehouse" + str(self.NbWarehouseBees), DiggerBee, self.SPAWN4)
            self.NbWarehouseBees += 1
        elif self.NbNurseBees == 0:
            self.SpawnAnt("Nurse" + str(self.NbNurseBees), NurseBee, self.SPAWN4)
            self.NbNurseBees += 1
        elif self.NbDiggerBees <= self.NbSoldierBees * 2:
            self.SpawnAnt("Digger" + str(self.NbDiggerBees), DiggerBee, self.SPAWN4)
            self.NbDiggerBees += 1
        elif self.NbResourceBees <= self.NbSoldierBees * 2:
            self.SpawnAnt("Resource" + str(self.NbResourceBees), ResourceBee, self.SPAWN4)
            self.NbResourceBees += 1
        else:
            self.SpawnAnt("Soldier" + str(self.NbSoldierBees), SoldierBee, self.SPAWN4)
            self.NbSoldierBees += 1



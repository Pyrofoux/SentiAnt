from Sentiant.Model import *
from Sentiant.bot.Bees.WorkerBee import WorkerBee
from Sentiant.bot.Bees.NurseBee import NurseBee
from Sentiant.bot.Bees.ResourceBee import ResourceBee
from Sentiant.bot.Bees.SoldierBee import SoldierBee
from Sentiant.bot.Bees.WarehouseBee import WarehouseBee

# Goal : spawn bees when possible

class QueenBee(Queen):



    NbResourceBees = 0
    NbWorkerBees = 0
    NbNurseBees = 0
    NbWarehouseBees = 0
    NbSoldierBees = 0

    def newTurn(self, fov):

        spawn = None
        for i in range(len(fov[1])):
            if not(fov[1][i] is None) and fov[1][i] != fov[0][i]:
                spawn = fov[1][i]

        if not(spawn is None):
            self.SpawnAnt("Worker" + str(self.NbWorkerBees), WorkerBee, spawn)
            self.NbWorkerBees += 1
"""
            if self.NbWarehouseBees == 0:
                self.SpawnAnt("Warehouse" + str(self.NbWarehouseBees), DiggerBee, spawn)
                self.NbWarehouseBees += 1
            elif self.NbNurseBees == 0:
                self.SpawnAnt("Nurse" + str(self.NbNurseBees), NurseBee, spawn)
                self.NbNurseBees += 1
            elif self.NbDiggerBees <= self.NbSoldierBees * 2:
                self.SpawnAnt("Digger" + str(self.NbDiggerBees), DiggerBee, spawn)
                self.NbDiggerBees += 1
            elif self.NbResourceBees <= self.NbSoldierBees * 2:
                self.SpawnAnt("Resource" + str(self.NbResourceBees), ResourceBee, spawn)
                self.NbResourceBees += 1
            else:
                self.SpawnAnt("Soldier" + str(self.NbSoldierBees), SoldierBee, spawn)
                self.NbSoldierBees += 1"""



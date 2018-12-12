from Sentiant.Model.SolidEntity import SolidEntity
from Sentiant.Model.Cfg import Cfg

class Ant(SolidEntity):

    def __init__(self, id, name, team):
        super().__init__(id)
        self._name = name # id of the ant, string of 5 chars
        self._team = team
        self._holding = None # by default, the ant doesn't carry anything
        self._HP = Cfg.HPMAX # number of hits the ant can take before dying
        self._FoV = Cfg.FOV # Field Of View : number of cells the ant can view, center being itself

        self._nextAction = Cfg.SLEEP # next Action, will be read by Turn Manager
        self._nextActionArg = Cfg.NULL

    def __str__(self):
        return "Name: {0}\nTeam: {1}\nHolding: {2}\nHp: {3}\nFov: {4}\nNextAction: {5}\nNextActionArg: {6}\n"\
            .format(self._name, self._team, self._holding, self._HP, self._FoV, self._nextAction, self._nextActionArg)

    def Move(self, direction):
        """Set Action of ant to move
        direction : 'up', 'left', ..."""
        direc = Cfg.ParseDirection(direction)

        if(direc != Cfg.NULL):
            self._nextAction = Cfg.MOVE
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "déplacement")

    def Attack(self, direction):
        """Set Action of to attack
        direction : 'up', 'left', ..."""
        direc = Cfg.ParseDirection(direction)

        if (direc != Cfg.NULL):
            self._nextAction = Cfg.ATTACK
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "attaque")

    def Dig(self, direction):
        """Set Action of to dig
        direction : 'up', 'left', ..."""
        direc = Cfg.ParseDirection(direction)

        if (direc != Cfg.NULL):
            self._nextAction = Cfg.DIG
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "creuser")

    def Pickup(self):
        """Set Action of to pick up"""
        self._nextAction = Cfg.PICKUP
        self._nextActionArg = Cfg.NULL

    def Drop(self):
        """Set Action of to drop"""
        self._nextAction = Cfg.DROP
        self._nextActionArg = Cfg.NULL

    def Sleep(self):
        """Set Action of to sleep"""
        self._nextAction = Cfg.SLEEP
        self._nextActionArg = Cfg.NULL

    def Phero(self):
        """Set Action of to Phero"""
        self._nextAction = Cfg.PHERO
        self._nextActionArg = Cfg.NULL
        #TO DO : gérer les phéromones invalides et rajouter un argument

# Please avoid cyclic imports.
from Sentiant.Model.LogsManager import LogsManager

if __name__ == '__main__':

    ant = Ant(0, "name", "team")
    LogsManager.Info(ant)

    ant.Move("up")
    LogsManager.Info(ant)

    ant.Move("")
    LogsManager.Info(ant)

    ant.Attack("up")
    LogsManager.Info(ant)

    ant.Dig("up")
    LogsManager.Info(ant)

    ant.Pickup()
    LogsManager.Info(ant)

    ant.Drop()
    LogsManager.Info(ant)

    ant.Sleep()
    LogsManager.Info(ant)

    ant.Phero()
    LogsManager.Info(ant)

from Sentiant.Model.SolidEntity import SolidEntity
from Sentiant.Model import Cfg
from Sentiant.Model.LogsManager import LogsManager

class Ant(SolidEntity):

    def __init__(self, id, name, team):
        super().__init__(id)
        self._name = name # id of the ant, string of 5 chars
        self._team = team
        self._holding = None # by default, the ant doesn't carry anything
        self._HP = Cfg.Cfg.HPMAX  # number of hits the ant can take before dying
        self._FoV = Cfg.Cfg.FOV # Field Of View : number of cells the ant can view, center being itself

        self._nextAction = Cfg.Cfg.SLEEP # next Action, will be read by Turn Manager
        self._nextActionArg = Cfg.Cfg.NULL

    def __str__(self):
        return "Name:{0}\nTeam:{1}\nHolding:{2}\nHp:{3}\nFov:{4}\nNextAction:{5}\nNextActionArg:{6}"\
            .format(self._name, self._team, self._holding, self._HP, self._FoV, self._nextAction, self._nextActionArg)

    def Move(self, direction):
        """Set Action of ant to move
        direction : 'up', 'left', ..."""
        direc = Cfg.Cfg.ParseDirection(direction)

        if(direc != Cfg.Cfg.NULL):
            self._nextAction = Cfg.Cfg.MOVE
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "déplacement")

    def Attack(self, direction):
        """Set Action of to attack
        direction : 'up', 'left', ..."""
        direc = Cfg.Cfg.ParseDirection(direction)

        if (direc != Cfg.Cfg.NULL):
            self._nextAction = Cfg.Cfg.ATTACK
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "attaque")

    def Dig(self, direction):
        """Set Action of to dig
        direction : 'up', 'left', ..."""
        direc = Cfg.Cfg.ParseDirection(direction)

        if (direc != Cfg.Cfg.NULL):
            self._nextAction = Cfg.Cfg.DIG
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "creuser")

    def Pickup(self):
        """Set Action of to pick up"""
        self._nextAction = Cfg.Cfg.PICKUP
        self._nextActionArg=Cfg.Cfg.NULL

    def Drop(self):
        """Set Action of to drop"""
        self._nextAction = Cfg.Cfg.DROP
        self._nextActionArg=Cfg.Cfg.NULL

    def Sleep(self):
        """Set Action of to sleep"""
        self._nextAction=Cfg.Cfg.SLEEP
        self._nextActionArg=Cfg.Cfg.NULL

    def Phero(self):
        """Set Action of to Phero"""
        self._nextAction=Cfg.Cfg.PHERO
        self._nextActionArg=Cfg.Cfg.NULL
        #TO DO : gérer les phéromones invalides et rajouter un argument



if __name__ == '__main__':

    ant = Ant(0, "test", "test")

    print(ant)

    ant.Move("up")

    print(ant)

    ant.Move("")

    print(ant)

    ant.Attack("up")

    print(ant)

    ant.Dig("up")

    print(ant)

    ant.Pickup()

    print(ant)

    ant.Drop()

    print(ant)

    ant.Sleep()

    print(ant)

    ant.Phero()

    print(ant)



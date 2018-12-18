from Sentiant.Model.SolidEntity import SolidEntity
from Sentiant.Model.Cookie import Cookie
from Sentiant.Model.Bread import Bread

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

    def __setattr__(self, name, value, secu=None):
        if not name in dir(self):
            super().__setattr__(name, value)
            return

        # Traitement des variables constantes.
        if name in ('_name', '_team', '_FoV'):
            LogsManager.PrivateVariableError(self._name, self._team, name, value)
            return

        # Impossible de se donner plus de vie.
        if name == '_HP' and value > getattr(self, name):
            LogsManager.PrivateVariableError(self._name, self._team, name, value)
            return

        # Empeche le /give de ressources.
        if name == '_holding' and value and secu != "legit":
            LogsManager.PrivateVariableError(self._name, self._team, name, value)
            return

        super().__setattr__(name, value)

    def newTurn(self, FOV, pheromones):
        pass

    def __str__(self):
        return "Name: {0}\nTeam: {1}\nHolding: {2}\nHp: {3}\nFov: {4}\nPreviousAction: {5}\nPreviousActionArg: {6}\n"\
            .format(self._name, self._team, self._holding, self._HP, self._FoV, self._nextAction, self._nextActionArg)

    def getHP(self):
        return self._HP

    def getHolding(self):
        if isinstance(self._holding, Bread):
            return Cfg.BREAD
        elif isinstance(self._holding, Cookie):
            return Cfg.COOKIE
        else:
            return Cfg.EMPTY
    def getFOV(self):
        return self._FOV

    def Move(self, direction):
        """Set Action of ant to move
        direction : 'up', 'left', ..."""
        direc = Cfg.ParseDirection(direction)

        if direc != Cfg.NULL:
            self._nextAction = Cfg.MOVE
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "déplacement")

    def Attack(self, direction):
        """Set Action of to attack
        direction : 'up', 'left', ..."""
        direc = Cfg.ParseDirection(direction)

        if direc != Cfg.NULL:
            self._nextAction = Cfg.ATTACK
            self._nextActionArg = direc
        else :
            self.Sleep()
            LogsManager.NotADirectionError(self._name, self._team, direc, "attaque")

    def Dig(self, direction):
        """Set Action of to dig
        direction : 'up', 'left', ..."""
        direc = Cfg.ParseDirection(direction)

        if direc != Cfg.NULL:
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

    def Phero(self, scent):
        """Set Action of to Phero"""
        if (scent>=0) and (scent <=31):
            self._nextAction = Cfg.PHERO
            self._nextActionArg = scent
        else :
            self._nextAction = Cfg.SLEEP
            self._nextActionArg = Cfg.NULL
            LogsManager.NotAPheromoneError(self._name,self._team,scent)

# Please avoid cyclic imports.
from Sentiant.Model.LogsManager import LogsManager
from Sentiant.Model.Cfg import Cfg

if __name__ == '__main__':
    import os

    os.chdir("../../")

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


    ant._HP-= 1 # pas d'erreur
    ant._HP+= 1 # erreur
    LogsManager.Info(ant)

    ant._name = "coucou" # erreur
    LogsManager.Info(ant)

    from Sentiant.Model.Bread import Bread
    ant._holding = Bread(-1) # erreur
    LogsManager.Info(ant)

    ant.__setattr__('_holding', Bread(-1), "legit") # pas d'erreur
    LogsManager.Info(ant)

    ant._holding = None # pas d'erreur
    LogsManager.Info(ant)

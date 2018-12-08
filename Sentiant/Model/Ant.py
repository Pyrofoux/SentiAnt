from .SolidEntity import SolidEntity
from .Cfg import Cfg
from .LogsManager import LogsManager


class Ant(SolidEntity):

    def __init__(self, id, name, team):
        super().__init__(id)
        self._name = name # id of the ant, string of 5 chars
        self._team = team
        self._holding = None # by default, the ant doesn't carry anything
        self._HP = Cfg.HPMAX  # number of hits the ant can take before dying
        self._FoV = Cfg.FOV # Field Of View : number of cells the ant can view, center being itself

        self._nextAction = Cfg.SLEEP # next Action, will be read by Turn Manager
        self._nextActionArg = Cfg.NULL

    def move(self, direction):

        direc = Cfg.parseDirection(direction)

        if(direc != Cfg.NULL):
            self._nextAction = Cfg.MOVE
            self._nextActionArg = direc
        else :
            self.sleep()
            LogsManager.notADirectionErrror(self.id,self.team,direc,"déplacement")

    def attack(self, direction):

        direc = Cfg.parseDirection(direction)

        if (direc != Cfg.NULL):
            self._nextAction = Cfg.ATTACK
            self._nextActionArg = direc
        else :
            self.sleep()
            LogsManager.notADirectionErrror(self.id,self.team,direc,"attaque")

    def dig(self, direction):

        direc = Cfg.parseDirection(direction)

        if (direc != Cfg.NULL):
            self._nextAction = Cfg.DIG
            self._nextActionArg = direc
            self.nextActionArg = direc
        else :
            self.sleep()
            LogsManager.notADirectionErrror(self.id,self.team,direc,"creuser")

    def pickup(self):
        self._nextAction = Cfg.PICKUP
        self._nextActionArg=NULL

    def drop(self):
        self._nextAction = Cfg.DROP
        self._nextActionArg=NULL

    def sleep(self):
        self._nextAction=Cfg.SLEEP
        self._nextAction=Cfg.NULL

    def phero(self):
        self._nextAction=Cfg.PHERO
        self._nextActionArg=NULL

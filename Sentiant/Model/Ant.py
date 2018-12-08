from .SolidEntity import SolidEntity
from .Cfg import Cfg
from .LogsManager import LogsManager


class Ant(SolidEntity):


    #Initialise ici pour pouvoir els utilsier ailleurs, comme dans TurnManager
    _name = None
    _team = None
    _holding = None
    _HP = None
    _FOV = None
    _nextAction = None
    _nextActionArg = None


    def __init__(self, id, name, team):
        super().__init__(id)
        _name = name # id of the ant, string of 5 chars
        _team = team
        _holding = None # by default, the ant doesn't carry anything
        _HP = Cfg.HPMAX  # number of hits the ant can take before dying
        _FoV = Cfg.FOV # Field Of View : number of cells the ant can view, center being itself

        _nextAction = Cfg.SLEEP # next Action, will be read by Turn Manager
        _nextActionArg = Cfg.NULL


    def move(self, direction):

        direc = Cfg.parseDirection(direction)

        if(direc != Cfg.NULL):
            _nextAction = Cfg.MOVE
            _nextActionArg = direc
        else :
            _nextAction = Cfg.SLEEP
            _nextActionArg = Cfg.NULL
            LogsManager.notADirectionErrror(self.id,self.team,direc,"déplacement")


    def attack(self, direction):

        direc = Cfg.parseDirection(direction)

        if (direc != Cfg.NULL):
            _nextAction = Cfg.ATTACK
            _nextActionArg = direc
        else :
            _nextAction = Cfg.SLEEP
            _nextActionArg = Cfg.NULL
            LogsManager.notADirectionErrror(self.id,self.team,direc,"attaque")


    def dig(self, direction):

        direc = Cfg.parseDirection(direction)

        if (direc != Cfg.NULL):
            _nextAction = Cfg.DIG
            _nextActionArg = direc
            self.nextActionArg = direc
        else :
            _nextAction = Cfg.SLEEP
            _nextActionArg = Cfg.NULL
            LogsManager.notADirectionErrror(self.id,self.team,direc,"creuser")

    def pickup(self):
        _nextAction = Cfg.PICKUP


    def drop(self):
        _nextAction = Cfg.DROP

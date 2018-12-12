from os import path
from datetime import datetime

class LogsManager :
    def __init__(self):
        pass

    @staticmethod
    def timeString():
        return datetime.now().strftime("%H:%M:%S.%f")[:-3]

    #scriptPath = os.path.abspath(__file__)
    #scriptDir = os.path.split(scriptPath)[0]
    #scriptDirDir = os.path.dirname(scriptDir)

    BASE = "Sentiant/Logs/"
    EXT = ".log"

    generals = open(BASE + "generals" + EXT, "w")
    users    = open(BASE + "users"    + EXT, "w")

    @staticmethod
    def StdOut(type, msg, isUser=False, end="\n"):
        pre = "["+type+"] ("+LogsManager.timeString()+")> "
        out = pre + str(msg).replace("\n", "\n" + " " * len(pre)) + end
        print(out)

        LogsManager.generals.write(out)
        if isUser:
            LogsManager.users.write(out)

    @staticmethod
    def Error(details, userFailure=False):
        LogsManager.StdOut("Error", details, userFailure)

    @staticmethod
    def Warning(details):
        """Not for user usage"""
        LogsManager.StdOut("Warning", details)

    @staticmethod
    def Info(info, isUser=False):
        LogsManager.StdOut("Info", info, isUser)

    @staticmethod
    def Debug(msg, isUser=True):
        """Recomended for user usage"""
        LogsManager.StdOut("Debug", msg, isUser)

    @staticmethod
    def NotADirectionError(antId, antTeam, direction, action):
        """Writes in generals and users text files
           when a non-valid direction is given to an Ant
        """
        details = ("Une erreur a eu lieu car la direction '{direction}' " \
                + "donnée à la fourmi '{antId}' 'de l'équipe '{antTeam}' " \
                + "pour l'action '{action}' n'est pas une direction valide") \
                .format(antId=antId, antTeam=antTeam, direction=direction, action=action)
        LogsManager.Error(details, True)

    @staticmethod
    def NotAPheromoneError(antId, antTeam, pheromone):
        """Writes in generals and users text files
           when a non-valid pheromone is given to an Ant
        """
        details = ("Une erreur a eu lieu car la phéromone '{pheromone}' " \
                + "qu'a essayé de poser la fourmi '{antId}' de l'équipe " \
                + "'{antTeam}' n'est pas une valeur de phéromone valide") \
                .format(antId=antId, antTeam=antTeam, pheromone=pheromone)
        LogsManager.Error(details, True)

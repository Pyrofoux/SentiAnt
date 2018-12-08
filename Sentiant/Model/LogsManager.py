import os, datetime


class LogsManager :
    def __init__(self):
        pass

    def time():
        return datetime.datetime.now()

    scriptPath = os.path.abspath(__file__)
    scriptDir = os.path.split(scriptPath)[0]
    scriptDirDir = os.path.dirname(scriptDir)

    BASE = os.path.join(scriptDirDir, "Logs" + os.pathsep)
    EXT = ".log"

    generals = open(BASE + "generals" + EXT, "w")
    users = open(BASE + "users" + EXT, "w")

    def StdOut(type, msg, isUser=False):
        out = "[" + type + "] @" + LogsManager.time().strftime("%H:%M") + "> " + msg
        LogsManager.generals.write(out)
        if isUser:
            LogsManager.users.write(out)

    def Error(details, usersFailure=False):
        LogsManager.Stdout("Error", details, LogsManager.userFailure)

    def Warning(details):
        """Not for user usage"""
        LogsManager.Stdout("Warning", details)

    def Infos(infos, isUser=False):
        LogsManager.Stdout("Infos", infos, isUser)

    def Debug(msg, isUser=True):
        """Recomended for user usage"""
        LogsManager.Stdout("Debug", msg, isUser)

    def NotADirectionError(antId, antTeam, direction, action):
        details = f"Une erreur a eu lieu car la direction <{direction}> " \
                + f"donnée à la fourmi <{antId}> de l'équipe <{antTeam}> " \
                + f"pour l'action <{action}> n'est pas une direction valide"
        LogsManager.Error(details, True)

    def NotAPheromoneError(jsp, antTeam, pheromone):
        details = f"Une erreur a eu lieu car la phéromone <{pheromone}> " \
                + f"qu'a essayé de poser la fourmi <{antId}> de l'équipe <{antTeam}> " \
                + "n'est pas une valeur de phéromone valide"
        LogsManager.Error(details, True)

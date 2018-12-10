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

    def Stdout(type, msg, isUser=False):
        out = "[" + type + "] @" + time().strftime("%H:%M") + "> " + msg
        generals.write(out)
        if isUser:
            users.write(out)

    def Error(details, usersFailure=False):
        Stdout("Error", details, userFailure)

    def Warning(details):
        """Not for user usage"""
        Stdout("Warning", details)

    def Infos(infos, isUser=False):
        Stdout("Infos", infos, isUser)

    def Debug(msg, isUser=True):
        """Recomended for user usage"""
        Stdout("Debug", msg, isUser)


    def NotADirectionError(antId, antTeam, direction, action):
        details = ("Une erreur a eu lieu car la direction {direction} " \
                + "donnée à la fourmi {antId} de l'équipe {antTeam} " \
                + "pour l'action {action} n'est pas une direction valide") \
.format(antId=antId, antTeam=antTeam, direction=direction, action=action)
        Error(details, True)

    def NotAPheromoneError(jsp, bla, coucou):
        details = 42

        Error(details, True)

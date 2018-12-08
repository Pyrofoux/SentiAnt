import os, datetime


class LogsManager :
    def __init__(self):
        self.now = datetime.datetime.now()
        pass

    scriptPath=os.path.abspath(__file__)
    scriptDir=os.path.split(scriptPath)[0]
    scriptDirDir=os.path.dirname(scriptDir)
    relativePath="Logs\logs.txt"
    finalPath=os.path.join(scriptDirDir,relativePath)


    def notADirectionError(self,antId,antTeam,direction,action):
         with open(self.finalPath,'w+') as logs:
                logs.write((self.now.strftime("%Y-%m-%d %H:%M") +
                f" Une erreur a eu lieu car la direction <{direction}> donnée à la fourmi <{antId}> de l'équipe <{antTeam}> pour l'action <{action}> n'est pas une direction valide"))
import os, datetime

class LogsManager :
    def __init__(self):
        self.scriptPath=os.path.abspath(__file__)
        self.scriptDir=os.path.split(self.scriptPath)[0]
        self.scriptDirDir=os.path.dirname(self.scriptDir)
        self.relativePath="Logs\logs.txt"
        self.finalPath=os.path.join(self.scriptDirDir,self.relativePath)

     def notADirectionErrror(self,id,direction,action):
         with open(self.finalPath,'w+') as logs:
                logs.write((datetime.datetime.now().time) + " : erreur") #TO DO : compléter le message pour l'action, l'id etc +appeler la méthode dans Ant
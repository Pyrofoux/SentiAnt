import os

def LoadAllFrom(rootDir, mainFile='queen.py'):
    """ Load players alorithms from the specified directory `rootDir`.

        For every sub-directories:
        * If it finds a 'queen.py' (default - use argument `mainFile` to
            change it), loads it and appends its reference ;
        * Else aborts.

        Return a list of references `ref` to the loaded modules alongs with the
        directory's `name` it was found in:
            ``` [(ref, name), (ref, name), ..] ```
    """
    r = []
    prev = os.getcwd()
    os.chdir(rootDir)

    for dir in os.scandir():
        if dir.is_dir() and os.path.exists(dir.path + "/" + mainFile):
            LogsManager.Info("Importing algorithm from '" + dir.name +  "'... ")

            try:
                queen = __import__(dir.name + "." + mainFile[:-3],
                                   fromlist=[mainFile[:-3]])
                r.append( (queen, dir.name) )
            except ImportError as e:
                LogsManager.Error("\tcould'n gather module because:\n" + str(e))
            else:
                LogsManager.Info("\tdone!")
        else:
            LogsManager.Warning("No main file in '{}', abort loading.".format(dir.name))

    os.chdir(prev)
    return r


from Sentiant.Model.LogsManager import LogsManager

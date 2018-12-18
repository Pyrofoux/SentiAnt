import os
from tkinter import Frame, Checkbutton, Button, IntVar

class BotImport(Frame):
    def __init__(self, root, directory, onOk, mainFileName='Queen.py'):
        super().__init__(root)

        self.dir = directory
        self.mainFile = mainFileName
        self.onOk = onOk

        self.isSelected = []
        self.queens = []
        self.names = []

    def Done(self):
        self.onOk([(self.queens[k], self.names[k]) \
                   for k in range(len(self.names)) if self.isSelected[k].get()])

    def pack(self):
        for k in range(len(self.names)):
            self.isSelected.append(IntVar())
            c = Checkbutton(self, text=self.names[k], variable=self.isSelected[k])
            c.grid(row=k)

        Button(self, text="OK!", command=self.Done).grid(row=len(self.names))

        super().pack()

    def LoadAll(self):
        """ OUT OF DATE!

            Load players alorithms from the specified directory `rootDir`.

            For every sub-directories:
            * If it finds a 'QueenBee.py' (default - use argument `mainFile` to
                change it), loads it and appends its reference ;
                ``` from directory.Queen import Queen ```
            * Else aborts.

            Return a list of references `ref` to the loaded modules alongs with the
            directory's `name` it was found in:
                ``` [(ref, name), (ref, name), ..] ```
        """
        r = []

        for directory in os.scandir(path=self.dir):
            if directory.is_dir() and os.path.exists(directory.path + "/" + directory.name + ".py"):

                LogsManager.Info("Importing algorithm from '" + directory.name +  "'... ")

                try:
                    q = __import__("Sentiant.Player."+directory.name + "." + directory.name, \
                                   fromlist=[directory.name])
                    q = eval("q." + directory.name)
                    self.queens.append(q)
                    self.names.append(directory.name)
                except ImportError as e:
                    LogsManager.Error("    could'n gather module because:\n" + str(e))
                else:
                    LogsManager.Info("    done!")
            else:
                LogsManager.Warning("No main file in '{}', abort loading.".format(directory.name))
        return r


from Sentiant.Model.LogsManager import LogsManager

if __name__ == '__main__':
    root = Tk()

    e = BotImport( root, "Sentiant/Player", \
                   lambda p: print("\n".join([n + " - " + str(q()) for q, n in p])) )
    e.LoadAll()
    e.pack()

    root.mainloop()

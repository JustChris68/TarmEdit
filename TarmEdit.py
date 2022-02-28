import tkinter as tk
from TEActions import TActions
from TEConfig import TConfig
from TEFileHandlers import TFilehandlers
from TEMenus import menupop


class App(tk.Tk, TConfig, menupop, TActions, TFilehandlers):
    def __init__(self):
        super(App, self).__init__()
        self.title("Menus")
        self.minsize(1800, 1000)
        # self.wm_iconbitmap('icon.ico')
        configdata = self.getJSONFile('config.json')

        configset = TConfig()
        Tconf = configset.getTConfig()
        print(Tconf)
        self.createMenu()
        print(configdata)

    def TECommand(self, action, source):
        print(action)
        self.RunFunc(action, source)


app = App()
app.mainloop()

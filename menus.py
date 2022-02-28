import tkinter as tk
from tkinter import ttk
from tkinter import Menu



class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Menus")
        self.minsize(600,400)
        # self.wm_iconbitmap('icon.ico')

        self.createMenu()





    def createMenu(self):
        menuBar = Menu(self)
        self.config(menu = menuBar)

        file_menu = Menu(menuBar, tearoff = 0)

        menuBar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label='New')
        file_menu.add_command(label='Exit')
        file_menu.add_separator()
        file_menu.add_command(label="Open")

        # Add Another Menu to Menbar
        help_menu = Menu(menuBar, tearoff = 0)
        menuBar.add_cascade(label = 'Help', menu = help_menu)
        help_menu.add_command(label = 'About')



app = App()
app.mainloop()
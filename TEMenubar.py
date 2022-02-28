import tkinter as tk
from tkinter import ttk
from tkinter import Menu



class menuhelper(object):
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























# import tkinter as tk
#
#
#
#
#
# def createMenu(self):
#     menuBar = Menu(self)
#     self.config(menu = menuBar)
#
#     file_menu = Menu(menuBar, tearoff = 0)
#
#     menuBar.add_cascade(label="File", menu=file_menu)
#     file_menu.add_command(label='New')
#     file_menu.add_command(label='Exit')
#     file_menu.add_separator()
#     file_menu.add_command(label="Open")
#
#     # Add Another Menu to Menbar
#     help_menu = Menu(menuBar, tearoff = 0)
#     menuBar.add_cascade(label = 'Help', menu = help_menu)
#     help_menu.add_command(label = 'About')  
#
# def createmenus(menulist = None):
#     if menulist == None:
#         #call menueditor
#         pass
#     else:
#         for items in menulist:
#             #menu json iterator here
#             pass
#     #temp code to test basic menucreation
#
#
#
#
#     menubar = tk.Menu()
#
#     filemenu = tk.Menu(menubar)
#     filemenu.add_command(label="Open")
#     filemenu.add_command(label="Save")
#     filemenu.add_command(label="Exit")
#
#     menubar.add_cascade(label="File", menu=filemenu)
#
#
#
#
#     # config(menu=menubar)
#     return True
#
# def client_exit():
#         exit()



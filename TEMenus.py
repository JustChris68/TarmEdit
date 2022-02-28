import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from TEActions import *
from TEConfig import TConfig
from wx import MenuBar
    
class menupop():
    def createMenu(self):
        #TODO: UPDATE: put in imported module to keep code cleaner
        #menugenerator code here
        menuBar = Menu(self)
        self.config(menu = menuBar)
        #file menu
        file_menu = Menu(menuBar, tearoff = 1)
        menuBar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label='New', command = lambda: self.TECommand('New', 'Filemenu New'))
        file_menu.add_command(label='Exit', command =lambda:  self.TECommand('Quit', 'filemenu exit'))
        file_menu.add_separator()
        file_menu.add_command(label="Open", command =lambda: self.TECommand('Open', 'Filemenu Open'))
        file_menu.add_command(label='AddVar', command =lambda: self.TECommand('AddVar', 'filemenu addvar'))
        #edit menu
        edit_menu = Menu(menuBar, tearoff = 1)
        menuBar.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='Copy', command =lambda: self.TECommand('Copy', 'EditMenu Copy'))
        edit_menu.add_command(label='Cut', command = lambda: self.TECommand('Cut', 'Editmenu Cut'))
        edit_menu.add_command(label='Paste', command = lambda: self.TECommand('Paste', 'Editmenu Paste'))
        #asset menu
        asset_menu = Menu(menuBar, tearoff = 1)
        menuBar.add_cascade(label='Assets', menu=asset_menu)
        asset_menu.add_command(label='Asset Browser', command = lambda: self.TECommand('AssetBrowser', 'Assetmenu Asset Browser'))
        asset_menu.add_command(label='Import Asset', command = lambda: self.TECommand('ImportAsset', 'Assetmenu Import Asset'))
        asset_menu.add_command(label='Edit Asset', command = lambda: self.TECommand('EditAsset', 'Assetmenu Edit Asset'))  
        #layer menu
        layer_menu = Menu(menuBar, tearoff = 1)
        menuBar.add_cascade(label='Layers', menu=layer_menu)
        layer_menu.add_command(label='layer Browser', command = lambda: self.TECommand('LayerBrowser', 'LayersMenu Layer Browser'))
        layer_menu.add_command(label='Add layer', command = lambda: self.TECommand('AddLayer', 'LayersMenu Add Layer'))
        layer_menu.add_command(label='Edit layer', command = lambda: self.TECommand('EditLayer', 'LayersMenu Edit Layer'))
        layer_menu.add_command(label='Delete Layer layer', command = lambda: self.TECommand('DeleteLayer', 'LayersMenu Delete Layer'))
        #collection menu
        collection_menu = Menu(menuBar, tearoff = 1)
        menuBar.add_cascade(label='Collections', menu=collection_menu)
        collection_menu.add_command(label='Collection Browser', command = lambda: self.TECommand('CollectBrowser', 'CollectionsMenu Collections Browser'))
        collection_menu.add_command(label='New collection', command = lambda: self.TECommand('NewCollect', 'CollectionsMenu New Collection'))
        collection_menu.add_command(label='Edit collection', command = lambda: self.TECommand('EditCollect', 'CollectionsMenu Edit Collection'))
        collection_menu.add_command(label='Delete collection', command = lambda: self.TECommand('DeleteCollect', 'CollectionsMenu Delete Collection'))
    
    
        #help menu
        help_menu = Menu(menuBar, tearoff = 1)
        menuBar.add_cascade(label = 'Help', menu = help_menu)
        help_menu.add_command(label = 'About', command = lambda: self.TECommand('About', 'HelpMenu About'))
    
    
    

 
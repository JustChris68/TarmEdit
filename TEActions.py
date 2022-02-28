import tkinter as tk
from tkinter import simpledialog
from TEConfig import TConfig




class TActions():            
    def RunFunc(self, action, source):
        #TODO: add logging for clean exit
        print('it worked, ' + action + ' passed as argument by ' + source)
        if action == 'Quit':
            self.destroy()
        elif action == 'AddVar':
            print('Add Variable Key And Value')
            
            
            
            
            
            
            
        # elif action == 'AddVar':
        #     print('Add System Variable')
        #     newKey = simpledialog.askstring(title="New Variable Name",
        #                           prompt="Variable Name?:")
        #     newValue = simpledialog.askstring(title="New Variable Value",
        #               prompt="Variable Value?:")
        #     # application_window = tk.Tk()
        #     # newKey = simpledialog.askstring("Key", "New Var Name",
        #     #                     parent=application_window)
        #     # newValue = simpledialog.askstring("Value", "New Var Value",
        #     #         parent=application_window)
        #     print(newKey + ' ' + newValue)
        #     # return [newKey, newValue]
        #     self.updateSet(newKey, newValue)
        elif action == 'New':
            print('Create New Map Object')            
        elif action == 'Save':
            print('Save Map Object')
        elif action =='SaveAs':
            print('SaveAS')
        elif action =='Copy':
            print('Copy')
        elif action == 'Cut':
            print('Cut')
        elif action == 'Paste':
            print('Paste')
        elif action == 'AddLayer':
            print('Add Layer')
        elif action == 'EditLayer':
            print('EditLayer')
        elif action == 'LayerBrowser':
            print('LayerBrowser')
        elif action == 'DeleteLayer':
            print('Delete Layer')
        elif action == 'CollectBrowser':
            print('Collection Browser')
        elif action == 'EditCollect':
            print('Edit Collection')
        elif action == 'AddCollect':
            print('Add Collection')
        elif action == 'DeleteCollect':
            print('Delete Collection')
        elif action == 'About':
            print('About')
        elif action == 'NewCollect':
            print('New Collection')
        elif action == 'EditAsset':
            print('Edit Asset')
        elif action == 'AssetBrowser':
            print('Asset Browser')
        elif action == 'ImportAsset':
            print('Import Asset')
        
        
        else:
            print('Command Not Found')
        
            
    
import os.path
import json



class TFilehandlers():
    def getJSONFile(self,file):
        print('JSON FileHandler Called')
        if os.path.exists(file):
            with open(file) as json_file:
                configdata = json.load(json_file)
            return configdata
        else:
            self.createConfig()
        
        





#
#
# class TFiles():
#     def __init__(self):
#         pass
#
#
# class TFileHandler():
#     #class to wrap basic standard operations to be used, actions include
#     #new, save, saveas, open txt, open json and load images, check 
#     #if file exists.
#     # def __init__(self, action, contents = None, fname = None, flocation = None , owrite = None):
#     def __init__(self):
#         #set placeholder values for operations
#         self.ftype = 'unknown'      #file type
#         self.ffilter = '*.*'        #file extension
#         self.isfsaved = False         #hase file been saved
#
#     def test_class(self):
#         print(self.ftype)
#         print(self.ffilter)
#         print(self.isfsaved)
import os
import json
# from TEConfig import TConfig

class TConfig():
    def __init__(self):
        print('TConfig called succesfully')
        #TODO: on init, open config file, fallback to default if there is a problem, double fallback if that is bad too
        
    def getTConfig(self):
        print('getTConfig Called Correctly')
        return 'configuration'
    
    def getTset(self, TSet):
        #retrieve setting from settings dictionary
        print('Requested Setting Name: ' + TSet)
        return TSet
    
    def createConfig(self):
        defaultdict = {'lastWD': os.getcwd(), 'userconf': 'config.json'}
        f = open("config.json", "w")
        json.dump(defaultdict, f)
        f.close()
        print('config created')
    
    def chooseConfig(self):
        #choose and apply a config file
        #TODO: create filehandler for old config files
        pass
    
    def updateSet(self, TSet, TValue = None):
        print('updateSet function called')
        configdata[TSet] = TValue
        applyConfig(configdata)
        print('config data dictionary updated')
    
    def compareConfigs(self):
        #compare current and prior configurations to see what changed when and by what process
        pass
    
    def applyConfig(self, configdata):
        defaultdict = {'lastWD': os.getcwd(), 'userconf': 'config.json'}
        f = open("config.json", "w")
        json.dump(configdata, f)
        f.close()
        print('config.data file updated')
        
    def editConfig(self):
        #directly edit configuration settings
        pass
    
    def writeDefault(self):
        defaultdict = {'lastWD': os.getcwd(), 'userconf': 'config.json'}
        f = open("config.json", "w")
        json.dump(defaultdict, f)
        f.close()
        print('default config.json created')
        
        
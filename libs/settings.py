#!/usr/bin/python
import ConfigParser

#Constants

VERSION = 0.1 # Versionsstring of the Software
ENABLE_DEBUG = 1 # Defines if Debugging is enabled
CONFIG_FILE='./amv.config'
VERSION = '0'
APPNAME = ''

class appsettings():
    def __init__(self):
        self.config=ConfigParser.RawConfigParser()
        self.id=0
    def initapp(self):
        print('\n\n************************************************************************\n')
        if (self.readsettings()):
            print (APPNAME)
            print('Version: ' + VERSION)
            if(ENABLE_DEBUG):
                print('Debugging is enabled')
            else:
                print('Debugging not enabled')
            print('App initialised\n\n')
            
            print('************************************************************************\n')
            return True
        else:
            print('An Error occured: Application terminated\n\n')
            print('************************************************************************\n')
            return False
        
        

    def readsettings(self):
        global APPNAME,  ENABLE_DEBUG, VERSION
        try:
            self.config.read(CONFIG_FILE)
            if self.config.getboolean('MainSection', 'ENABLE_DEBUG'):
                ENABLE_DEBUG = 1
            else:
                ENABLE_DEBUG = 0
                print("Debugging disabled")
            if self.config.get('MainSection', 'version'):
                VERSION = self.config.get('MainSection', 'version')
                
            if self.config.get('MainSection', 'appname'):
                APPNAME=self.config.get('MainSection', 'appname')
                
            return True
        except:
            print("Could not read config file")
            return False
            
    def writesetting(self, section, string,  val):
        global CONFIG_FILE
        self.config.set(section, string , val)
        with open(CONFIG_FILE, 'wb') as configfile:
            self.config.write(configfile)

    def getsetting(self, section, setting):
        global CONFIG_FILE
        try:
            self.config.read(CONFIG_FILE)
            return self.config.get(section, setting)
        except:
            return "Unset"
        
    def getversion(self):
        return self.getsetting('MainSection', 'version')
        
    def getappname(self):
        return self.getsetting('MainSection', 'appname')

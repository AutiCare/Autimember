#!/usr/bin/python
import ConfigParser
import helper
#Constants

VERSION = 0.1 # Versionsstring of the Software
ENABLE_DEBUG = 1 # Defines if Debugging is enabled
CONFIG_FILE='./amv.config'
VERSION = '0'
APPNAME = ''

def initapp():
    print('\n\n************************************************************************\n')
    if (readsettings()):
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
    
    

def readsettings():
    global APPNAME,  ENABLE_DEBUG, VERSION
    config = ConfigParser.ConfigParser()
    try:
        config.read(CONFIG_FILE)
        if config.getboolean('MainSection', 'ENABLE_DEBUG'):
            ENABLE_DEBUG = 1
        else:
            ENABLE_DEBUG = 0
            print("Debugging disabled")
        if config.get('MainSection', 'version'):
            VERSION = config.get('MainSection', 'version')
            
        if config.get('MainSection', 'appname'):
            APPNAME=config.get('MainSection', 'appname')
            
        return True
    except:
        print("Could not read config file")
        return False
        
def writesettings():
    config = ConfigParser.RawConfigParser()
    config.add_section('Section1')
    config.set('Section1', "ENABLE_DEBUG", '1')
    with open('amv.config', 'wb') as configfile:
        config.write(configfile)


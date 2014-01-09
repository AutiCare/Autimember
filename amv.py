#!/usr/bin/python
from libs import settings
from libs import helper
from PyQt4 import QtCore,  QtGui
from ui.MainWindow import MainWindow
#Init the application before loading the interface

def main():
    mainapp = settings.appsettings()
    if(mainapp.initapp()):
        print('Hello')
    else:
        exit(0)
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow(mainapp)
    ui.pushButton.setText("Hallo")
    ui.setWindowTitle(settings.APPNAME + " Version: " + str(settings.VERSION))
    ui.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

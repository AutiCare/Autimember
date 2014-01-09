#!/usr/bin/python
from libs import settings
from libs import helper
from PyQt4.QtGui import QApplication
from ui.MainWindow import MainWindow
#Init the application before loading the interface
def main():
    if(settings.initapp()):
        print('Hello')
    else:
        exit(0)
    import sys
    app = QApplication(sys.argv)
    wnd = MainWindow
    wnd.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

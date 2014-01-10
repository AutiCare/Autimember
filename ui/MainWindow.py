# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QApplication
from .Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, mainapp, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        self.mainapp = mainapp
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("nix")
        
    
    @pyqtSignature("")
    def on_actionQuit_activated(self):
        QApplication.quit()
        
    @pyqtSignature("")
    def on_actionEinstellungen_activated(self):
        from SettingsDialog import Dialog 
        settingsDialog = Dialog(self.mainapp)
        settingsDialog.exec_()

    @pyqtSignature("")
    def on_actionTest_activated(self):
        from testwindow import testwindow
        testWindow = testwindow(self.mainapp)
        testWindow.exec_()

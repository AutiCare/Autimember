# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from .Ui_SettingsDialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mainapp, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        self.mainapp=mainapp
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.lineEdit.setText(mainapp.getversion())
        
    
    @pyqtSignature("")
    def on_cancelBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
    
    @pyqtSignature("")
    def on_saveBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.mainapp.writesetting('MainSection', 'version', self.lineEdit.text())
        self.close()

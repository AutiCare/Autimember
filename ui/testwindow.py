# -*- coding: utf-8 -*-

"""
Module implementing testwindow.
"""

from PyQt4.QtCore import pyqtSignature,  Qt
from PyQt4.QtGui import QDialog,  QPainter,  QPen, QBrush, QGraphicsScene 
from PyQt4 import QtCore
import random
from .Ui_testwindow import Ui_Dialog
import qrcode
import qrcode.image.svg


class testwindow(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mainapp, parent=None):
        self.mainapp = mainapp
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_closeBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
    
    @pyqtSignature("")
    def on_execBtn_clicked(self):
        self.drawPoints()
        
        
    def drawPoints(self):
        img = qrcode.make('TestCode 001',image_factory=qrcode.image.svg.SvgImage )
        type(img)
        gitem =  QGraphicsScene()
        self.graphicsView.setScene(gitem)
        #gitem.addLine(0, 0, 2, 2)
        qbrush = QBrush()
        qbrush.setStyle(Qt.SolidPattern)
        qbrush.setColor(Qt.black)
        gitem.addRect(0, 0, 2, 2, brush=qbrush )
        self.graphicsView.show()

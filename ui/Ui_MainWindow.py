# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/marco/Development/mitgliederverwaltung/Autimember/ui/MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 440, 88, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuDatei = QtGui.QMenu(self.menuBar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        self.menuDebug = QtGui.QMenu(self.menuBar)
        self.menuDebug.setObjectName(_fromUtf8("menuDebug"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionEinstellungen = QtGui.QAction(MainWindow)
        self.actionEinstellungen.setObjectName(_fromUtf8("actionEinstellungen"))
        self.actionTest = QtGui.QAction(MainWindow)
        self.actionTest.setObjectName(_fromUtf8("actionTest"))
        self.menuDatei.addAction(self.actionEinstellungen)
        self.menuDatei.addAction(self.actionQuit)
        self.menuDebug.addAction(self.actionTest)
        self.menuBar.addAction(self.menuDatei.menuAction())
        self.menuBar.addAction(self.menuDebug.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei", None))
        self.menuDebug.setTitle(_translate("MainWindow", "Debug", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionEinstellungen.setText(_translate("MainWindow", "Einstellungen", None))
        self.actionTest.setText(_translate("MainWindow", "test", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/marco/Development/mitgliederverwaltung/Autimember/ui/testwindow.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.closeBtn = QtGui.QPushButton(Dialog)
        self.closeBtn.setGeometry(QtCore.QRect(300, 260, 88, 25))
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))
        self.execBtn = QtGui.QPushButton(Dialog)
        self.execBtn.setGeometry(QtCore.QRect(10, 260, 88, 25))
        self.execBtn.setObjectName(_fromUtf8("execBtn"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 361, 221))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.closeBtn.setText(_translate("Dialog", "Close", None))
        self.execBtn.setText(_translate("Dialog", "Execute", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


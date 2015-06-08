# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sat May 31 18:33:40 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
def open_source_code():
	os.system("gnome-open source.pdf")
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(606, 413)
        Form.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 139, 139, 255));\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.0909091, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(172, 255, 232, 255));"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 431, 51))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Serif\";\n"
"font: 18pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(480, 50, 101, 21))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: italic 14pt \"Sans Serif\";\n"
"font: italic 12pt \"Sans Serif\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 161, 31))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 85, 0);\n"
"font: 12pt \"Serif\";\n"
"background-color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 110, 171, 81))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(80, 241, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.322275, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(172, 255, 232, 255));"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 300, 98, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(87, 179, 255, 255));\n"
"color: rgb(0, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 266, 331, 21))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 68, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), open_source_code)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "   Image-Processing Controlled Bot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "  ITSP 2014", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "  Tech-No-Logic :  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "   Yash Bhalgat\n"
"   Sudhir Kumar\n"
"   Sheel Nidhan\n"
"   Akshay Sinha", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Source code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Press the button below to view the \"source-code\"", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


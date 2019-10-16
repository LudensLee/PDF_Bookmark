# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddContens.ui',
# licensing of 'AddContens.ui' applies.
#
# Created: Wed Mar 13 15:56:10 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 315)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.Start = QtWidgets.QPushButton(self.groupBox)
        self.Start.setObjectName("Start")
        self.gridLayout.addWidget(self.Start, 3, 2, 1, 1)
        self.lb_ConPath = QtWidgets.QLabel(self.groupBox)
        self.lb_ConPath.setObjectName("lb_ConPath")
        self.gridLayout.addWidget(self.lb_ConPath, 0, 0, 1, 1)
        self.lb_Path = QtWidgets.QLabel(self.groupBox)
        self.lb_Path.setObjectName("lb_Path")
        self.gridLayout.addWidget(self.lb_Path, 2, 0, 1, 1)
        self.lb_FilePath = QtWidgets.QLabel(self.groupBox)
        self.lb_FilePath.setObjectName("lb_FilePath")
        self.gridLayout.addWidget(self.lb_FilePath, 1, 0, 1, 1)
        self.FilePath = QtWidgets.QLineEdit(self.groupBox)
        self.FilePath.setObjectName("FilePath")
        self.gridLayout.addWidget(self.FilePath, 1, 1, 1, 2)
        self.PutPath = QtWidgets.QLineEdit(self.groupBox)
        self.PutPath.setObjectName("PutPath")
        self.gridLayout.addWidget(self.PutPath, 2, 1, 1, 2)
        self.Select = QtWidgets.QPushButton(self.groupBox)
        self.Select.setObjectName("Select")
        self.gridLayout.addWidget(self.Select, 3, 1, 1, 1)
        self.ContensPath = QtWidgets.QLineEdit(self.groupBox)
        self.ContensPath.setText("")
        self.ContensPath.setObjectName("ContensPath")
        self.gridLayout.addWidget(self.ContensPath, 0, 1, 1, 2)
        self.Contens = QtWidgets.QPushButton(self.groupBox)
        self.Contens.setObjectName("Contens")
        self.gridLayout.addWidget(self.Contens, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.Start.setText(QtWidgets.QApplication.translate("Form", "START", None, -1))
        self.lb_ConPath.setText(QtWidgets.QApplication.translate("Form", "ContensPath:", None, -1))
        self.lb_Path.setText(QtWidgets.QApplication.translate("Form", "OutPath:", None, -1))
        self.lb_FilePath.setText(QtWidgets.QApplication.translate("Form", "FilePath:", None, -1))
        self.Select.setText(QtWidgets.QApplication.translate("Form", "SELECT FILE", None, -1))
        self.Contens.setText(QtWidgets.QApplication.translate("Form", "SELECT CONTENS", None, -1))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginforum.ui',
# licensing of 'loginforum.ui' applies.
#
# Created: Thu Nov 28 03:17:30 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(310, 290, 231, 21))
        self.user_name.setObjectName("user_name")
        self.user_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.user_pass.setGeometry(QtCore.QRect(310, 350, 231, 21))
        self.user_pass.setText("")
        self.user_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_pass.setPlaceholderText("")
        self.user_pass.setObjectName("user_pass")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(240, 450, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        self.btn_login.setFont(font)
        self.btn_login.setAutoFillBackground(False)
        self.btn_login.setObjectName("btn_login")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QtWidgets.QApplication.translate("LoginWindow", "MainWindow", None, -1))
        self.btn_login.setText(QtWidgets.QApplication.translate("LoginWindow", ".", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("LoginWindow", "Schedule System", None, -1))


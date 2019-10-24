# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportG.ui',
# licensing of 'reportG.ui' applies.
#
# Created: Wed Oct 23 12:19:20 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 30, 101, 31))
        self.label_3.setObjectName("label_3")
        self.id_user = QtWidgets.QLineEdit(self.centralwidget)
        self.id_user.setGeometry(QtCore.QRect(150, 40, 113, 20))
        self.id_user.setObjectName("id_user")
        self.loginB = QtWidgets.QPushButton(self.centralwidget)
        self.loginB.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.loginB.setObjectName("loginB")
        self.massge_id = QtWidgets.QLabel(self.centralwidget)
        self.massge_id.setGeometry(QtCore.QRect(180, 70, 151, 16))
        self.massge_id.setText("")
        self.massge_id.setObjectName("massge_id")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 130, 431, 201))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label.setObjectName("label")
        self.list_product = QtWidgets.QComboBox(self.groupBox)
        self.list_product.setGeometry(QtCore.QRect(100, 30, 291, 22))
        self.list_product.setObjectName("list_product")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 51, 21))
        self.label_2.setObjectName("label_2")
        self.lis_problem = QtWidgets.QComboBox(self.groupBox)
        self.lis_problem.setGeometry(QtCore.QRect(100, 80, 291, 22))
        self.lis_problem.setObjectName("lis_problem")
        self.send = QtWidgets.QPushButton(self.groupBox)
        self.send.setGeometry(QtCore.QRect(300, 160, 75, 23))
        self.send.setObjectName("send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "username :", None, -1))
        self.loginB.setText(QtWidgets.QApplication.translate("MainWindow", "GO", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "products :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Problem :", None, -1))
        self.send.setText(QtWidgets.QApplication.translate("MainWindow", "send", None, -1))


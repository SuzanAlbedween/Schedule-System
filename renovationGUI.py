# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renovationGUI.ui',
# licensing of 'renovationGUI.ui' applies.
#
# Created: Mon Nov 25 17:03:20 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.renovation_button_tech = QtWidgets.QPushButton(self.centralwidget)
        self.renovation_button_tech.setGeometry(QtCore.QRect(170, 450, 101, 41))
        self.renovation_button_tech.setObjectName("renovation_button_tech")
        self.table_tech = QtWidgets.QTableWidget(self.centralwidget)
        self.table_tech.setGeometry(QtCore.QRect(90, 110, 551, 291))
        self.table_tech.setRowCount(1000)
        self.table_tech.setColumnCount(5)
        self.table_tech.setObjectName("table_tech")
        self.table_tech.setColumnCount(5)
        self.table_tech.setRowCount(1000)
        self.table_tech.horizontalHeader().setVisible(True)
        self.table_tech.horizontalHeader().setCascadingSectionResizes(False)
        self.table_tech.horizontalHeader().setHighlightSections(True)
        self.table_tech.horizontalHeader().setSortIndicatorShown(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 61, 31))
        self.label.setObjectName("label")
        self.nametech_label = QtWidgets.QLabel(self.centralwidget)
        self.nametech_label.setGeometry(QtCore.QRect(110, 30, 61, 31))
        self.nametech_label.setObjectName("nametech_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 21, 21))
        self.label_3.setObjectName("label_3")
        self.id_techlabel = QtWidgets.QLabel(self.centralwidget)
        self.id_techlabel.setGeometry(QtCore.QRect(80, 60, 71, 21))
        self.id_techlabel.setObjectName("id_techlabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.renovation_button_tech.setText(QtWidgets.QApplication.translate("MainWindow", "Rennovation", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Welcome  ", None, -1))
        self.nametech_label.setText(QtWidgets.QApplication.translate("MainWindow", "T", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "ID :", None, -1))
        self.id_techlabel.setText(QtWidgets.QApplication.translate("MainWindow", "id", None, -1))


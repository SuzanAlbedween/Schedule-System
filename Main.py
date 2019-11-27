import sys
import openpyxl
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import  QtGui,QtCore
from PyQt5.QtCore import *

from login_forum import Ui_LoginWindow
from reportG import Ui_Dialog_Client
from report_problem import Problem
from product import Product
from clientCls import Client
from techns import Techn

class main_login(QMainWindow,Ui_LoginWindow,Problem,Ui_Dialog_Client,Techn,Product):

    def __init__(self):
        Problem.__init__(self)
        Product.__init__(self)
        Client.__init__(self)
        Techn.__init__(self)
        QMainWindow.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)








if __name__=="__main__":
    app=QApplication(sys.argv)
    window=main_login()
    window.show()
    sys.exit(app.exec_())

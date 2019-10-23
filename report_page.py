import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import  QtGui,QtCore
from PyQt5.QtCore import *
from reportG import Ui_MainWindow
from report_problem import Problem

class MyApp(QMainWindow,Ui_MainWindow,Problem ):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        Problem.__init__(self)
        self.setupUi(self)
        self.groupBox.hide()
        self.loginB.clicked.connect(self.login)
        self.list_product.currentTextChanged.connect(self.select_product)
        self.lis_problem.currentTextChanged.connect(self.select_problem)
        self.send.clicked.connect(self.send_data)



    def login(self):
        id_client=int(self.id_user.text())
        if(self.is_client_exist(id_client)):
            self.massge_id.hide()
            self.groupBox.show()
            self.report_p(id_client)
        else:
            self.massge_id.setText("The user does not exist in the system, try again ")


    def report_p(self,id_client):
        proud_lst=list(self.get_client_product(id_client))
        prob_lst=list(self.get_problems_types())
        for i in proud_lst:
            self.list_product.addItem(i[1])
        for j in prob_lst:
            self.lis_problem.addItem(j)



    def select_product(self):
        choice_product=self.list_product.currentText()
        return choice_product
       # choice_product=self.list_product.currentText()
    def select_problem(self):
        choice_problem=self.lis_problem.currentText()
        return choice_problem
    def send_data(self):
        id=self.id_user.text()
        ch_product=self.select_product()
        ch_problem=self.select_problem()
        self.add_problem_to_file(ch_product,id,ch_problem)
        print(id,ch_problem,ch_product)
        #self.add_problem_to_file(choice_product,id_client,choice_problem)


#######################run app#######################################
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())
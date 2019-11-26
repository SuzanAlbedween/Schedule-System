import sys
import openpyxl
from PyQt5.QtWidgets import *
from techns import Techn
from PyQt5 import  QtGui
from PyQt5.QtCore import *
#from qtgui import *
from PyQt5.uic.properties import QtWidgets

from renovationGUI import Ui_MainWindow



class renovation_App(QMainWindow,Ui_MainWindow,Techn):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.CreatTabel()
        #self.Load_Renovation_PerOneTechn(1)
        self.RenovationForAll()




    def CreatTabel(self):
       Names=["ID Scheduling","Details","Time","Location","Status"]
       for i in range(len(Names)):
           item = QTableWidgetItem()
           item.setText(Names[i])
           self.table_tech.setHorizontalHeaderItem(i, item)


    def Load_Renovation_PerOneTechn(self,index_tech):
        file = openpyxl.load_workbook('excel_files\\scheduling.xlsx')
        sheet = file['sheet1']
        rows = sheet.max_row
        self.id_techlabel.setText(str(sheet.cell(row=1, column=index_tech).value))
        name=self.Get_TechName(sheet.cell(row=1, column=index_tech).value)
        print(name)
        self.nametech_label.setText(name)
        for i in range(rows):
            idproblem =str(sheet.cell(row=2 + i, column=index_tech).value)
            self.table_tech.setItem(i, 0, QTableWidgetItem( idproblem))
           # details=self.Get_Details(idproblem) problemdetails
            self.table_tech.setItem(i, 1, QTableWidgetItem("abc  cbbgg"))
           # time=Get_Time(id_problem,location)
            self.table_tech.setItem(i, 2, QTableWidgetItem("60"))
           # idclient=self.Get_idClient(id_problem)
            #location=self.Get_Location(id_cilent)
            self.table_tech.setItem(i, 3, QTableWidgetItem("7,7"))
            combo = QComboBox()
            combo.addItem("Non")
            combo.addItem("Don")
            combo.addItem("Convert To Regular")
            self.table_tech.setCellWidget(i, 4,combo)
    def RenovationForAll(self):
        file = openpyxl.load_workbook('excel_files\\scheduling.xlsx')
        sheet = file['sheet1']
        cols = sheet.max_column
        for i in range(1,cols):
            self.Load_Renovation_PerOneTechn(i)











#######################run app#######################################
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=renovation_App()
    window.show()
    sys.exit(app.exec_())


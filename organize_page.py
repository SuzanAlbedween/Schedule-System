import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import  QtGui,QtCore
from PyQt5.QtCore import *
from OrganizedGUI import Ui_MainWindow
from product import Product
from clientCls import Client
from techns import Techn


class organize_app(QMainWindow,Ui_MainWindow,Product, Client,Techn):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        Product.__init__(self)
        Client.__init__(self)
        Techn.__init__(self)
        self.setupUi(self)

        self.off()
        self.add_clientB.clicked.connect(self.addclient)
        self.add_productB.clicked.connect(self.addproduct)
        self.add_techB.clicked.connect(self.addtech)
        self.push_product.clicked.connect(self.pushproduct)
        self.push_client.clicked.connect(self.pushClent)
        self.push_tech.clicked.connect(self.pushtech)




    def off(self):
        self.groupBox1.hide()
        self.groupBox2.hide()
        self.groupBox3.hide()
    def addclient(self):
        self.off()
        self.groupBox1.show()
    def addproduct(self):
        self.off()
        self.groupBox2.show()
        self.groupBox2.setGeometry(400, 20, 281, 221)
    def addtech(self):
        self.off()
        self.groupBox3.show()
        self.groupBox3.setGeometry(400, 20, 281, 221)
    def pushproduct(self):
        name=self.product_name.text()
        id_client=self.id_pclient.text()
        self.add_product(name,id_client)
    def pushClent(self):
        n=self.client_name.text()
        lo=self.client_location.text()
        print(n,lo)
        self.add_client_to_excel(n,lo)



    def pushtech(self):
        name=self.tech_name.text()
        username=self.tech_username.text()
        password=self.tech_pass.text()
        self.add_tech(name,username,password)





#######################run app#######################################
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=organize_app()
    window.show()
    sys.exit(app.exec_())
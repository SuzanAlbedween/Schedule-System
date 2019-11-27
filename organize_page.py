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
        self.groupBox2.setGeometry(400, 20, 471, 431)
    def addtech(self):
        self.off()
        self.groupBox3.show()
        self.groupBox3.setGeometry(400, 20, 471, 431)

    def pushproduct(self):
        name=self.product_name.text()
        tname=self.Checking_Length(name)
        self.label_nameproduct.setText("The name contains only lower or upper case letters"+"\n"+" and is less than 30 characters long")
        if(tname==False):
            self.label_nameproduct.show()
        else:
            self.label_nameproduct.hide()
        id_client=self.id_pclient.text()
        print(id_client)
        print(tname,self.is_id_exist(id_client))
        if(self.is_id_exist(id_client)==True and name!=None and id_client !=None):
            print(name,id_client)
            self.add_product(name,id_client)
        else:
            self.labe_idclient.setText("The client does not exist")

    def pushClent(self):
        n=self.client_name.text()
        testname=self.Checking_Name(n)
        self.mesge_labelName.setText( "The name contains only lower or upper case letters"+"\n"+" and is less than 30 characters long")
        self.templetlabellocation.setText( "The location structure contains only two numbers start and end numbers" + "\n" + " and is larger than -1 also in this format" + "\n" + " < number,number>")
        if(testname==False):
            self.mesge_labelName.show()
        else:
            self.mesge_labelName.hide()

        lo=self.client_location.text()
        testlocation=self.Testing_Location(lo)
        print(n, lo)
        print(testlocation)
        print(testname)
        if(testlocation==False):
            self.templetlabellocation.show()
        else:
            self.templetlabellocation.hide()

        if(testlocation==True and testname==True and lo !=None and n !=None):
           self.add_client_to_excel(n,lo)





    def pushtech(self):
        name=self.tech_name.text()
        self.msagelabel_username.setText("The username contains only 8  characters"+"\n"+"also the first character is letter"+"\n "+"also without any space")
        self.labelnameof_masgetech.setText("The name contains only lower or upper case letters"+"\n"+" and is less than 30 characters long")
        testname=self.Checking_Name(name)
        print(testname)
        if(testname==False):
            self.labelnameof_masgetech.show()
        else:
            self.labelnameof_masgetech.hide()
        username=self.tech_username.text()
        testuser=self.Checking_UserName(username)
        print(testuser)
        if(testuser==False):
            self.msagelabel_username.show()
        else:
            self.msagelabel_username.hide()
        password=self.tech_pass.text()
        testpass=self.Checking_Length(password)
        print(testpass)
        if(testname==True and testuser==True and password !=None and name!=None and username !=None ):
            self.add_tech(name,username,password)
            print(name,username,password)
        else:
            print("no details")









#######################run app#######################################
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=organize_app()
    window.show()
    sys.exit(app.exec_())

import openpyxl
import random

class Client:


    def is_id_exist(self,client_id):
        clientfile = openpyxl.load_workbook('clients.xlsx')
        clientsheet = clientfile['clients']
        row_s=clientsheet.max_row
        for i in range(2,row_s+1):
            if((clientsheet.cell(row=i,column=2).value)==(client_id)):
                return True
            return False

    def client_random_id(self):
        client_id=random.randrange(1000,99999)
        if(self.is_id_exist(client_id) is True):
                self.client_random_id()
        return client_id


    def add_client_to_excel(self,client_name,client_location):
        print(client_name,client_location)
        client_file=openpyxl.load_workbook('clients.xlsx')
        client_sheet=client_file['clients']
        maxrow=client_sheet.max_row
        id=(self.client_random_id())
        print(id)
        client_sheet['A'+str((maxrow+1))]=client_name
        client_sheet['B'+str(maxrow+1)]=id
        client_sheet['C'+str(maxrow+1)]=client_location
        client_file.save('clients.xlsx')


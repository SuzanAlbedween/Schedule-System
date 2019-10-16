import openpyxl
<<<<<<< HEAD
class Problem:
    def report(self):
        print("Enter your id:")
    # return  list of problems_types from problems_types file
    def get_problems_types(self):
        lsproblems=[]
        f=openpyxl.load_workbook('problems_types.xlsx')
        sheet1 = f.get_sheet_by_name('types')
        row = sheet1.max_row + 1
        for i in range(2,row):
            lsproblems.append(sheet1.cell(row=i, column=2).value)
        return lsproblems
=======

class Problem:
    def report(self):
        print("Enter your id:")
    def get_client_product(self, client_id):
        ans = []
        wb = openpyxl.load_workbook('products.xlsx')
        sheet1 = wb.get_sheet_by_name('products')
        for i in range(2, sheet1.max_column + 1):
            if sheet1.cell(row=i, column=3).value == client_id:
                ans.append((sheet1.cell(row=i, column=1).value,sheet1.cell(row=i, column=2).value))
        print(ans)




    def is_client_exist(self, client_id):
        client_file = openpyxl.load_workbook('clients.xlsx')
        client_sheet = client_file.get_sheet_by_name('clients')
        rows = client_sheet.max_row
        for i in range (2, rows +1):
            if(client_sheet.cell(row=i, column=2).value == client_id):
               return True

        return False
>>>>>>> 3d605e802450d12a6bce31470f501922f7bd8b89




new_report=Problem()
<<<<<<< HEAD
new_report.report()
print(new_report.get_problems_types())
=======
<<<<<<< HEAD
new_report.report()
print(new_report.is_client_exist(12355589))
=======
new_report.reporgitt()
new_report.get_client_product(123456789)
>>>>>>> 767be3bbec9a5dd84db0c023f104614d4ea3feb6
>>>>>>> 3d605e802450d12a6bce31470f501922f7bd8b89

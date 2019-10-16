import openpyxl

class Problem:
    def report(self):
        print("Enter your id:")

    def is_client_exist(self, client_id):
        client_file = openpyxl.load_workbook('clients.xlsx')
        client_sheet = client_file.get_sheet_by_name('clients')
        rows = client_sheet.max_row
        for i in range (2, rows +1):
            if(client_sheet.cell(row=i, column=2).value == client_id):
               return True

        return False




new_report=Problem()
new_report.report()
print(new_report.is_client_exist(12355589))

import openpyxl

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




new_report=Problem()
new_report.reporgitt()
new_report.get_client_product(123456789)
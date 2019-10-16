import openpyxl
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




new_report=Problem()
new_report.report()
print(new_report.get_problems_types())
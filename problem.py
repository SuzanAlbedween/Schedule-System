import openpyxl

class Problem:

    #written by Suzan added by Abeer
    def GetAllProblemByType(self, type):
        problems = list()
        file = openpyxl.load_workbook('excel_files\\problems.xlsx')
        sheet = file[type]
        rows = sheet.max_row
        for i in range(2, rows + 1):
            detailsproblem = list()
            for j in range(1, 6):
                detailsproblem.append(sheet.cell(row=i, column=j).value)
            problems.append(detailsproblem)
        return problems

    def get_list_id_time(self,type):
        problems = list()
        problems_file = openpyxl.load_workbook('excel_files\\problems.xlsx')
        problems_types_file = openpyxl.load_workbook('excel_files\\problems_types.xlsx')
        all_problems = problems_file[type]
        rows = all_problems.max_row
        return [[123,10],[111,10],[222,20],[321,225]]
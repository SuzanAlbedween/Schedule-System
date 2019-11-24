import openpyxl


class Problem:

    # written by Suzan added by Abeer
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

    def get_list_id_time(self, type_of_problem):
        problems = []
        problems_file = openpyxl.load_workbook('excel_files\\problems.xlsx')
        problems_types_file = openpyxl.load_workbook('excel_files\\problems_types.xlsx')
        all_problems = problems_file[type_of_problem]
        problem_types = problems_types_file['types']
        p_rows = all_problems.max_row
        t_rows = problem_types.max_row
        print(p_rows)
        for i in range(2, p_rows + 1):
            data = [all_problems.cell(row=i, column=1).value]
            description=all_problems.cell(row=i, column=5).value
            for j in range(2,t_rows+1):
                if type_of_problem == problem_types.cell(row=j,column=1).value:
                    if description == problem_types.cell(row=j,column=2).value:
                        data.append(problem_types.cell(row=j,column=3).value)
                        break
            problems.append(data)
        return problems
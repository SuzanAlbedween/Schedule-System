import openpyxl
import math
velocity = 30
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

    def get_problem_time(self, type_of_problem, description):
        problems_types_file = openpyxl.load_workbook('excel_files\\problems_types.xlsx')
        problem_types = problems_types_file['types']
        t_rows = problem_types.max_row
        for j in range(2, t_rows + 1):
            if type_of_problem == problem_types.cell(row=j, column=1).value:
                if description == problem_types.cell(row=j, column=2).value:
                    return problem_types.cell(row=j, column=3).value
        return 0

    def get_travel_time(self,client_id):
        clients_file = openpyxl.load_workbook('excel_files\\clients.xlsx')
        clients = clients_file['clients']
        c_rows = clients.max_row
        for i in range(2,c_rows+1):
            if int(clients.cell(row=i, column=2).value)== int(client_id):
                location = clients.cell(row=i, column=3).value
                location = [int(i) for i in location.split(',')]
                distance = math.sqrt(location[0] ** 2 + location[1] ** 2)
                return distance//velocity
        return 0

    def get_total_time(self, type_of_problem, description, client_id):
        problem_time = self.get_problem_time(type_of_problem, description)
        travel_time = self.get_travel_time(client_id)
        return problem_time + travel_time

    def get_list_id_time(self, type_of_problem):
        problems = []
        problems_file = openpyxl.load_workbook('excel_files\\problems.xlsx')
        all_problems = problems_file[type_of_problem]
        p_rows = all_problems.max_row
        for i in range(2, p_rows + 1):
            data = [all_problems.cell(row=i, column=1).value]
            description = all_problems.cell(row=i, column=5).value
            client_id = all_problems.cell(row=i, column=2).value
            data.append(self.get_total_time(type_of_problem, description, client_id))
            problems.append(data)
        return problems

    def delet_Row(self, problem_id, type):
        wb = openpyxl.load_workbook('excel_files\\problems.xlsx')
        sheet = wb[type]
        rows = sheet.max_row
        print(rows)
        for i in range(2, rows + 1):
            print(sheet.cell(row=i, column=1).value)
            if (problem_id == str(sheet.cell(row=i, column=1).value)):
                sheet.delete_rows(i, amount=1)
        wb.save('excel_files\\problems.xlsx')

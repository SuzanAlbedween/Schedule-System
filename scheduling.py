import openpyxl
import random

class Scheduling:

   def return_problem_duration(self, name_pm):
        wb = openpyxl.load_workbook('problems_types.xlsx')
        tp_sheet = wb['types']
        rows=tp_sheet.max_row
        for i in range(2, rows + 1):
            if (tp_sheet.cell(row=i, column=2).value == name_pm):
                return tp_sheet.cell(row=i, column=3).value

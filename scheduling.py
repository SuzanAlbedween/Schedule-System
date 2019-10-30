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


   def list_of_lists(self):
        clientfile = openpyxl.load_workbook('clients.xlsx')
        clientsheet = clientfile['clients']
        maxrw = clientsheet.max_row      #maxrow is the number of tech
        listoflists = []
        for i in range(2, maxrw+10):
            sublist=[0,0]
            listoflists.append(sublist)
        return listoflists



import openpyxl
import random

from techns import Techn


class Scheduling(Techn):
    schedule = list()
    techns_ids = list()
    times = list()

    def return_problem_duration(self, name_pm):
        wb = openpyxl.load_workbook('problems_types.xlsx')
        tp_sheet = wb['types']
        rows = tp_sheet.max_row
        for i in range(2, rows + 1):
            if (tp_sheet.cell(row=i, column=2).value == name_pm):
                return tp_sheet.cell(row=i, column=3).value

    def list_of_lists(self):
        clientfile = openpyxl.load_workbook('excel_files\clients.xlsx')
        clientsheet = clientfile['clients']
        maxrw = clientsheet.max_row  # maxrow is the number of tech
        listoflists = []
        for i in range(2, maxrw + 10):
            sublist = [0, 0]
            listoflists.append(sublist)
        return listoflists

    def init_empty_schedule(self, length_of_schedule):
        self.schedule = [[] for i in range(length_of_schedule)]
        return

    def init_times(self, length_of_schedule):
        self.times = [60*8 for i in range(length_of_schedule)]
        return
    def init_techn_ids(self):
        t=Techn()
        t.get_all_ids()
        ids_of_tech =t.techID
        return ids_of_tech

    def critical_problems_schedule(self):
        all_critical_problems = [[123,10],[111,15],[222,10],[333,10],[221,20],[212,10],[232,25]]  # get_all_critical_problems()
        all_techns_id = self.init_techn_ids()
        num_of_techns=len(all_techns_id)
        self.init_empty_schedule(len(all_techns_id))
        self.init_times(num_of_techns)
        current_techn = 0
        for problem in all_critical_problems:
            test = 0
            has_time = True  # hasTime(all_techns_id[current_techn])
            while not has_time :
                current_techn = (current_techn + 1)%num_of_techns
                test += 1
                if test == num_of_techns:
                    break
                has_time = True  # hasTime(all_techns_id[current_techn])
            if has_time:
                self.schedule[current_techn].append(problem)
                current_techn = (current_techn + 1) % num_of_techns
        # save_schedule()
        # report_errors()

    def main_schedule(self):
        self.critical_problems_schedule()



s=Scheduling()
s.critical_problems_schedule()
print(s.schedule)
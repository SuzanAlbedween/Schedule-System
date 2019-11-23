import openpyxl
import random


from . import techns


class Scheduling:
    schedule = list()
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
        self.times = [[] for i in range(length_of_schedule)]
        return

    def critical_problems_schedule(self):
        all_critical_problems = []  # get_all_critical_problems()
        tech = techns.Techn()
        all_techns_id = tech.get_all_ids()
        num_of_techns=len(all_techns_id)
        self.init_empty_schedule(self, len(all_techns_id))
        self.init_times(self, num_of_techns)
        current_techn = 0
        for problem in all_critical_problems:
            test = 0
            has_time = True  # hasTime(all_techns_id[current_techn])
            while not has_time :
                current_techn = (current_techn + 1)%num_of_techns
                test += 1
                if test == num_of_techns:
                    # report_error(problem)
                    break
                has_time = True  # hasTime(all_techns_id[current_techn])
            if has_time:
                self.schedule[current_techn].append(problem)
        # save_schedule()
        # report_errors()

    def main_schedule(self):
        self.critical_problems_schedule()




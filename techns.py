import random
import openpyxl


class Techn:
    def gene_tech_id(self):
        tech_id = random.randrange(100000, 999999)
        if (self.is_tech_exist(tech_id) is True):
            self.gene_tech_id()
        return tech_id

    def is_tech_exist(self, tech_id):
        tech_file = openpyxl.load_workbook('techns.xlsx')
        tc_sheet = tech_file['techns']
        rows = tc_sheet.max_row
        for i in range(2, rows + 1):
            if (tc_sheet.cell(row=i, column=1).value == tech_id):
                return True

        return False


import random
import openpyxl


class Techn:
    techID = list()
    def gene_tech_id(self):
        tech_id = random.randrange(100000, 999999)
        if (self.is_tech_exist(tech_id) is True):
            self.gene_tech_id()
        return tech_id

    def is_tech_exist(self, tech_id):
        tech_file = openpyxl.load_workbook('excel_files\\techns.xlsx')
        tc_sheet = tech_file['techns']
        rows = tc_sheet.max_row
        for i in range(2, rows + 1):
            if (tc_sheet.cell(row=i, column=1).value == tech_id):
                return True
        return False


    def add_tech(self, tech_name, username, pwd):
        wb = openpyxl.load_workbook('excel_files\\techns.xlsx')
        tc_sheet = wb['techns']
        mxrow = tc_sheet.max_row
        id = self.gene_tech_id()
        tc_sheet['A' + str(mxrow + 1)] = id
        tc_sheet['B' + str(mxrow + 1)] = tech_name
        tc_sheet['C' + str(mxrow + 1)] = username
        tc_sheet['D' + str(mxrow + 1)] = pwd
        wb.save('techns.xlsx')

    def get_all_ids(self):
        wb = openpyxl.load_workbook('excel_files\\techns.xlsx')
        tc_sheet = wb['techns']
        mxrow = tc_sheet.max_row
        for i in range(2, mxrow + 1):
            self.techID.append(tc_sheet.cell(row=i, column=1).value)
        wb.save('excel_files\\techns.xlsx')

import openpyxl
from datetime import datetime
class Product:
    def generate_random_id(self):
        return '1111'

    def get_date(self):
        return str(datetime.date(datetime.now()).day) + "/" + str(datetime.date(datetime.now()).month) + "/" + str(
            datetime.date(datetime.now()).year)

    def add_product(self, product_name, client_id):
        products_file = openpyxl.load_workbook('products.xlsx')
        products_sheet = products_file['products']
        mxrow = products_sheet.max_row
        products_sheet['A' + str(mxrow + 1)] = self.generate_random_id()  # adding id as str
        products_sheet['B' + str(mxrow + 1)] = product_name
        products_sheet['C' + str(mxrow + 1)] = client_id  # adding id as str
        products_sheet['D' + str(mxrow + 1)] = self.get_date()
        products_file.save('products.xlsx')

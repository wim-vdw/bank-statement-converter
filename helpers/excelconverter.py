from openpyxl import Workbook
from openpyxl.styles import Alignment


class ExcelConverter:
    def __init__(self, filename, data):
        self.filename = filename
        self.workbook = Workbook()
        self.data = data

    def create_file(self):
        new_sheet = self.workbook.active
        counter = 1
        new_sheet[f'A{counter}'].value = 10
        for statement in self.data:
            new_sheet[f'A{counter}'].value = statement.number
            new_sheet[f'B{counter}'].value = statement.date
            new_sheet[f'C{counter}'].value = statement.description
            new_sheet[f'D{counter}'].value = statement.value_date
            new_sheet[f'E{counter}'].value = statement.amount
            new_sheet[f'F{counter}'].value = statement.currency
            new_sheet[f'G{counter}'].value = statement.detail_in_text
            new_sheet[f'G{counter}'].alignment = Alignment(wrapText=True)
            counter += 1
        self.workbook.save(self.filename)

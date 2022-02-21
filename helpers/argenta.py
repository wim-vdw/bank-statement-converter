from PyPDF3 import PdfFileReader
from helpers.bankstatement import BankStatement


class ArgentaConverter:
    def __init__(self, input_file, start_number=1):
        self.input_file = input_file
        self.start_number = start_number

    def get_text_lines(self):
        pdf_data = PdfFileReader(self.input_file)
        text_lines = []
        for page in range(pdf_data.getNumPages()):
            page_text = pdf_data.getPage(page).extractText()
            text_lines += page_text.split('\n')
        return text_lines

    @staticmethod
    def process_detail(detail):
        detail_text = []
        for detail_line in detail:
            if detail_line and not str(detail_line).startswith('Saldo op'):
                detail_text.append(detail_line)
            else:
                break
        return detail_text

    def convert(self):
        number = None
        date = None
        description = None
        value_date = None
        data = []
        text_lines = self.get_text_lines()
        counter = self.start_number
        counter_line_item = 0
        new_found = False
        detail = []
        for line in text_lines:
            if line == str(counter):
                number = line
                new_found = True
                counter_line_item = 0
                if detail:
                    data[counter - 2 - self.start_number + 1].detail = self.process_detail(detail)
                detail = []
                counter += 1
            if new_found:
                counter_line_item += 1
            if counter_line_item == 2:
                date = line
            if counter_line_item == 3:
                description = line
            if counter_line_item == 4:
                value_date = line
            if counter_line_item == 5:
                amount = line
                bank_statement = BankStatement(number, date, description, value_date, amount)
                data.append(bank_statement)
            if counter_line_item > 5:
                detail.append(line)
        if detail and data:
            data[len(data) - 1].detail = self.process_detail(detail)
        return data

from PyPDF3 import PdfFileReader


class BNPConverter:
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

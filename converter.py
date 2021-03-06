from helpers.argenta import ArgentaConverter
from helpers.bnp import BNPConverter
from helpers.excelconverter import ExcelConverter

INPUT_FILE_ARGENTA = '/Users/wim/Documents/Boechout/Documenten voor notaris/Uitgaven sinds 01-04-2019/Argenta/Argenta-2022.pdf'
INPUT_FILE_BNP = '/Users/wim/Documents/Boechout/Documenten voor notaris/Uitgaven sinds 01-04-2019/BNP/2019/BE97230000284249-EX-2019-4.pdf'
TARGET_FILE = '/Users/wim/Downloads/Argenta-2022.xlsx'

if __name__ == '__main__':
    argenta = ArgentaConverter(INPUT_FILE_ARGENTA, 1)
    bnp = BNPConverter(INPUT_FILE_BNP, 1)
    xlsx = ExcelConverter(TARGET_FILE, argenta.convert())
    xlsx.create_file()

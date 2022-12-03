from helpers.argenta import ArgentaConverter
from helpers.bnp import BNPConverter
from helpers.excelconverter import ExcelConverter

INPUT_FILE_ARGENTA = './Argenta-example.pdf'
INPUT_FILE_BNP = './BNP-example.pdf'
TARGET_FILE = './Argenta-result.xlsx'

if __name__ == '__main__':
    argenta = ArgentaConverter(INPUT_FILE_ARGENTA, 1)
    bnp = BNPConverter(INPUT_FILE_BNP, 1)
    xlsx = ExcelConverter(TARGET_FILE, argenta.convert())
    xlsx.create_file()

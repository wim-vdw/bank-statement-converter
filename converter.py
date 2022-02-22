from helpers.argenta import ArgentaConverter
from helpers.bnp import BNPConverter

INPUT_FILE_ARGENTA = '/Users/wim/Documents/Boechout/Documenten voor notaris/Uitgaven sinds 01-04-2019/Argenta/Argenta-2022.pdf'
INPUT_FILE_BNP = '/Users/wim/Documents/Boechout/Documenten voor notaris/Uitgaven sinds 01-04-2019/BNP/2020/BE97230000284249-EX-2020-12.pdf'

if __name__ == '__main__':
    argenta = ArgentaConverter(INPUT_FILE_ARGENTA, 1)
    bnp = BNPConverter(INPUT_FILE_BNP, 1)
    for line in bnp.get_text_lines():
        print(line)

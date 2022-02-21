from helpers.argenta import ArgentaConverter

INPUT_FILE = '/Users/wim/Documents/Boechout/Documenten voor notaris/Uitgaven sinds 01-04-2019/Argenta/Argenta-2022.pdf'

if __name__ == '__main__':
    argenta = ArgentaConverter(INPUT_FILE, 1)
    result = argenta.convert()
    for i in result:
        print(i.number, i.date, i.description, i.value_date, i.amount)
        print(i.detail)
        print()

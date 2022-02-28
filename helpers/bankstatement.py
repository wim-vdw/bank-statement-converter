class BankStatement:
    def __init__(self, number, date, description, value_date, amount, currency='EUR'):
        self.number = number
        self.date = date
        self.description = description
        self.value_date = value_date
        self.amount = amount
        self.currency = currency
        self.detail = None

    @property
    def detail_in_text(self):
        return '\n'.join(self.detail)

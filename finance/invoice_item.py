class InvoiceItem:

    def __init__(self):

        self._description = ""

        self._quantity = 0

        self._unit_price = None

        self._line_total = None

        self._sku = ""

        self._category = ""

    def set_description(self, text):

        self._description = text

    def get_description(self):

        return self._description

    def set_quantity(self, quantity):

        self._quantity = quantity

    def get_quantity(self):

        return self._quantity

    def set_unit_price(self, price):

        self._unit_price = price

    def get_unit_price(self):

        return self._unit_price

    def set_line_total(self, total):

        self._line_total = total

    def get_line_total(self):

        return self._line_total

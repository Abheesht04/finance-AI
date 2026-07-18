class InvoiceTotals:

    def __init__(self):

        self._subtotal = None

        self._discount = None

        self._shipping = None

        self._tax = None

        self._total = None

        self._balance_due = None

    def set_subtotal(self, value):

        self._subtotal = value

    def get_subtotal(self):

        return self._subtotal

    def set_discount(self, value):

        self._discount = value

    def get_discount(self):

        return self._discount

    def set_shipping(self, value):

        self._shipping = value

    def get_shipping(self):

        return self._shipping

    def set_total(self, value):

        self._total = value

    def get_total(self):

        return self._total

    def set_balance_due(self, value):

        self._balance_due = value

    def get_balance_due(self):

        return self._balance_due

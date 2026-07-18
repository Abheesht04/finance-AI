class InvoiceHeader:

    def __init__(self):

        self._vendor = ""

        self._invoice_number = ""

        self._invoice_type = ""

        self._invoice_date = ""

    # ------------------------------

    def set_vendor(self, vendor):

        self._vendor = vendor

    def get_vendor(self):

        return self._vendor

    # ------------------------------

    def set_invoice_number(self, number):

        self._invoice_number = number

    def get_invoice_number(self):

        return self._invoice_number

    # ------------------------------

    def set_invoice_type(self, invoice_type):

        self._invoice_type = invoice_type

    def get_invoice_type(self):

        return self._invoice_type

    # ------------------------------

    def set_invoice_date(self, date):

        self._invoice_date = date

    def get_invoice_date(self):

        return self._invoice_date

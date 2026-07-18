from finance.invoice_header import InvoiceHeader
from finance.vendor import Vendor
from finance.customer import Customer
from finance.invoice_totals import InvoiceTotals
from finance.invoice_items import ItemCollection

class Invoice:

    def __init__(self):
        self._header = InvoiceHeader()
        self._vendor = Vendor()
        self._customer = Customer()
        self._totals = InvoiceTotals()
        self._items = []
        self._notes = ""
        self._terms = ""
        self._order_id = ""
        self._confidence = 0.0
        self._items = ItemCollection()

    # ---------------------------------
    def get_header(self):
        return self._header

    def get_vendor(self):
        return self._vendor

    def get_customer(self):
        return self._customer

    def get_totals(self):
        return self._totals

    # ---------------------------------
    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items

    # ---------------------------------
    def set_notes(self, notes):
        self._notes = notes

    def set_terms(self, terms):
        self._terms = terms

    def set_order_id(self, order_id):
        self._order_id = order_id

    def items(self):

        return self._items

    def print_summary(self):
        print()
        print("=" * 50)
        print("INVOICE")
        print("=" * 50)
        print()
        print("Vendor           :", self.get_vendor().get_name())
        print("Invoice Type     :", self.get_header().get_invoice_type())
        print("Invoice Number   :", self.get_header().get_invoice_number())
        print("Invoice Date     :", self.get_header().get_invoice_date())
        print()
        
        totals = self.get_totals()
        print("Subtotal         :", totals.get_subtotal())
        print("Shipping         :", totals.get_shipping())
        print("Balance Due      :", totals.get_balance_due())
        print("Total            :", totals.get_total())

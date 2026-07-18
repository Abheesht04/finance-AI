from finance.invoice import Invoice
from builders.header_builder import HeaderBuilder
from builders.totals_builder import TotalsBuilder
from builders.item_builder import ItemBuilder

class InvoiceBuilder:

    def build(self, document):

        print("========== INVOICE BUILDER ==========")

        invoice = Invoice()

        print("Calling HeaderBuilder...")
        HeaderBuilder().build(document, invoice)

        print("Calling TotalsBuilder...")
        TotalsBuilder().build(document, invoice)

        print("calling ItemBuilder")

        ItemBuilder().build(document,invoice)

        print("InvoiceBuilder Finished")

        return invoice

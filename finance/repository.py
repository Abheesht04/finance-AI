from finance.invoice import Invoice


# =====================================================
# Duplicate Result
# =====================================================

class DuplicateResult:

    def __init__(self):

        self._duplicate = False

        self._matched_invoice = None

        self._reason = ""

    # ----------------------------

    def set_duplicate(self, value):

        self._duplicate = value

    def is_duplicate(self):

        return self._duplicate

    # ----------------------------

    def set_reason(self, value):

        self._reason = value

    def get_reason(self):

        return self._reason

    # ----------------------------

    def set_invoice(self, invoice):

        self._matched_invoice = invoice

    def get_invoice(self):

        return self._matched_invoice


# =====================================================
# Invoice Repository
# =====================================================

class InvoiceRepository:

    def __init__(self):

        self._invoices = []

    # -------------------------------------------------

    def add(self, invoice):

        self._invoices.append(invoice)

    # -------------------------------------------------

    def clear(self):

        self._invoices.clear()

    # -------------------------------------------------

    def count(self):

        return len(self._invoices)

    # -------------------------------------------------

    def get_all(self):

        return self._invoices

    # -------------------------------------------------

    def find_duplicate(self, invoice):

        result = DuplicateResult()

        for existing in self._invoices:

            #
            # Invoice Number
            #

            if (

                existing.get_header().get_invoice_number()

                ==

                invoice.get_header().get_invoice_number()

            ):

                result.set_duplicate(True)

                result.set_reason(

                    "Invoice Number already exists."

                )

                result.set_invoice(existing)

                return result

            #
            # Vendor + Total
            #

            if (

                existing.get_vendor().get_name()

                ==

                invoice.get_vendor().get_name()

                and

                existing.get_totals().get_total()

                ==

                invoice.get_totals().get_total()

            ):

                result.set_duplicate(True)

                result.set_reason(

                    "Vendor and Total match."

                )

                result.set_invoice(existing)

                return result

        return result

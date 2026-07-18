from finance.rules.validation_rule import ValidationRule


class InvoiceNumberRule(ValidationRule):

    def validate(self, invoice, result):

        number = invoice.get_header().get_invoice_number()

        if number == "":

            result.fail("Invoice number missing.")

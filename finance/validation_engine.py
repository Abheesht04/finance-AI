from finance.validation_result import ValidationResult

from finance.rules.total_rule import TotalRule
from finance.rules.date_rule import DateRule
from finance.rules.currency_rule import CurrencyRule
from finance.rules.invoice_number_rule import InvoiceNumberRule


class ValidationEngine:

    def __init__(self):

        self._rules = [

            TotalRule(),

            DateRule(),

            CurrencyRule(),

            InvoiceNumberRule()

        ]

    # -------------------------------------

    def validate(self, invoice):

        result = ValidationResult()

        for rule in self._rules:

            rule.validate(

                invoice,

                result

            )

        return result

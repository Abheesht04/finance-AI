from finance.rules.validation_rule import ValidationRule


class CurrencyRule(ValidationRule):

    def validate(self, invoice, result):

        result.add_info("Currency validation skipped.")

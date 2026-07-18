from finance.rules.validation_rule import ValidationRule


class DateRule(ValidationRule):

    def validate(self, invoice, result):

        result.add_info("Date validation skipped.")

from finance.rules.validation_rule import ValidationRule


class TotalRule(ValidationRule):

    def _money(self, text):

        if text is None:

            return 0.0

        text = text.replace("$", "")

        text = text.replace(",", "")

        return float(text)

    # ---------------------------------------

    def validate(self, invoice, result):

        totals = invoice.get_totals()

        subtotal = self._money(

            totals.get_subtotal()

        )

        shipping = self._money(

            totals.get_shipping()

        )

        discount = self._money(

            totals.get_discount()

        )

        total = self._money(

            totals.get_total()

        )

        calculated = subtotal - discount + shipping

        if abs(calculated - total) > 0.01:

            result.fail(

                f"Totals do not match. "

                f"Expected {calculated:.2f} "

                f"but invoice has {total:.2f}"

            )

        else:

            result.add_info(

                "Totals verified."
            )

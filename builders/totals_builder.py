from finance.invoice import Invoice


class TotalsBuilder:

    def build(self, document, invoice):


        print("new Totals Builder")

        page = document.get_page(0)

        totals = invoice.get_totals()

        for kv in page.get_key_values():

            key = kv.get_key()
            value = kv.get_value()

            if key == "Subtotal":
                totals.set_subtotal(value)

            elif key == "Shipping":
                totals.set_shipping(value)

            elif key == "Balance Due":
                totals.set_balance_due(value)

            elif key == "Total":
                totals.set_total(value)

            elif key.startswith("Discount"):
                totals.set_discount(value)

        totals = invoice.get_totals()

        
        print("Subtotal :", totals.get_subtotal())
        print("Shipping :", totals.get_shipping())
        print("Balance  :", totals.get_balance_due())
        print("Total    :", totals.get_total())

from finance.invoice_items import InvoiceItem
from scripts.row_type import RowType
from finance.money import CurrencyConverter


class ItemBuilder:

    def __init__(self):

        self._converter = CurrencyConverter()

    # --------------------------------------------------

    def build(self, document, invoice):

        page = document.get_page(0)

        for row in page.get_layout_rows():

            if row.get_type() != RowType.TABLE_ROW:
                continue

            item = self._build_item(row)

            if item is not None:
                invoice.items().add(item)

    # --------------------------------------------------

    def _build_item(self, row):

        tokens = row.get_text().split()

        #
        # Find quantity
        #

        quantity_index = -1

        for i, token in enumerate(tokens):

            if token.isdigit():

                quantity_index = i

                break

        if quantity_index == -1:

            return None

        #
        # Need at least:
        # Qty  Rate  Total
        #

        if quantity_index + 2 >= len(tokens):

            return None

        #
        # Description
        #

        description = " ".join(tokens[:quantity_index])

        #
        # Quantity
        #

        quantity = int(tokens[quantity_index])

        #
        # Unit Price
        #

        unit_price = self._converter.parse_money(

            tokens[quantity_index + 1]

        )

        #
        # Line Total
        #

        line_total = self._converter.parse_money(

            tokens[quantity_index + 2]

        )

        #
        # Build InvoiceItem
        #

        item = InvoiceItem()

        item.set_description(description)

        item.set_quantity(quantity)

        item.unit_price().set_amount(

            unit_price.get_amount()

        )

        item.unit_price().currency().set_type(

            unit_price.currency().get_type()

        )

        item.unit_price().currency().set_symbol(

            unit_price.currency().get_symbol()

        )

        item.line_total().set_amount(

            line_total.get_amount()

        )

        item.line_total().currency().set_type(

            line_total.currency().get_type()

        )

        item.line_total().currency().set_symbol(

            line_total.currency().get_symbol()

        )

        return item

class AddressBuilder:

    def build(self, document, invoice):

        page = document.get_page(0)

        rows = page.get_layout_rows()

        collecting = False

        address = []

        for row in rows:

            text = row.get_text()

            if text.startswith("Ship To"):

                collecting = True

                continue

            if collecting:

                if row.get_type().name == "KEY_VALUE":

                    break

                address.append(text)

        invoice.customer().set_shipping_address(

            "\n".join(address)

        )

class CustomerBuilder:

    def build(self, document, invoice):

        page = document.get_page(0)

        rows = page.get_layout_rows()

        for i, row in enumerate(rows):

            if row.get_text().startswith("Bill To"):

                if i + 1 < len(rows):

                    invoice.customer().set_name(

                        rows[i + 1].get_text()

                    )

                break

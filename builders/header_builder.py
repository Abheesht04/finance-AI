class HeaderBuilder:

    def build(self, document, invoice):

        print("\n========== HEADER BUILDER ==========")

        print("Pages:", document.get_page_count())

        page = document.get_page(0)

        rows = page.get_layout_rows()

        print("Rows:", len(rows))

        if len(rows) == 0:
            return

        first = rows[0]

        print("First row:", first.get_text())

        columns = first.get_columns()

        print("Columns:", len(columns))

        for i, column in enumerate(columns):
            print(f"Column {i}: {column.get_text()}")

        if len(columns) >= 1:
            invoice.get_vendor().set_name(columns[0].get_text())

        if len(columns) >= 2:
            invoice.get_header().set_invoice_type(columns[1].get_text())

        if len(rows) >= 2:
            invoice.get_header().set_invoice_number(
                rows[1].get_text().replace("#", "").strip()
            )

        for kv in page.get_key_values():
            if kv.get_key() == "Date":
                invoice.get_header().set_invoice_date(kv.get_value())
                break

        print("Vendor =", invoice.get_vendor().get_name())
        print("Type   =", invoice.get_header().get_invoice_type())
        print("Number =", invoice.get_header().get_invoice_number())
        print("Date   =", invoice.get_header().get_invoice_date())

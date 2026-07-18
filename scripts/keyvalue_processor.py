from scripts.key_value import KeyValue
from scripts.row_type import RowType


class KeyValueProcessor:

    def process(self, document):

        print("\n========== KEYVALUE PROCESSOR ==========\n")

        for page in document.get_pages():

            for row in page.get_layout_rows():

                print("--------------------------------")
                print("ROW :", row.get_text())
                print("TYPE:", row.get_type())

                if row.get_type() != RowType.KEY_VALUE:
                    print("Skipped")
                    continue

                print("Processing")

                self._process_row(page, row)

    # ----------------------------------------------------

    def _process_row(self, page, row):

        columns = row.get_columns()

        print("Columns:", len(columns))

        if len(columns) == 1:

            text = columns[0].get_text()

            print("TEXT =", text)

            if ":" not in text:

                print("No colon")
                return

            key_text, value_text = text.split(":", 1)

            kv = KeyValue()

            kv.set_key(key_text.strip())

            kv.set_value(value_text.strip())

            print("ADDING", kv)

            page.add_key_value(kv)

            return

        if len(columns) == 2:

            kv = KeyValue()

            kv.set_key(columns[0].get_text().replace(":", "").strip())

            kv.set_value(columns[1].get_text().strip())

            print("ADDING", kv)

            page.add_key_value(kv)

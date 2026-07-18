from scripts.row_type import RowType


class RowClassifier:

    def process(self, document):

        for page in document.get_pages():

            for row in page.get_layout_rows():

                self._classify(row)

    # -------------------------------------

    def _classify(self, row):

        columns = row.get_columns()

        text = row.get_text().strip()

        # -----------------------------
        # Empty
        # -----------------------------

        if text == "":

            row.set_type(RowType.UNKNOWN)

            return

        # -----------------------------
        # Two headings
        # Bill To:   Ship To:
        # -----------------------------

        if len(columns) == 2:

            left = columns[0].get_text().strip()

            right = columns[1].get_text().strip()

            if left.endswith(":") and right.endswith(":"):

                row.set_type(RowType.SECTION_HEADER)

                return

        # -----------------------------
        # Single key:value
        # Date: Mar 07
        # Total: $100
        # -----------------------------

        if ":" in text:

            row.set_type(RowType.KEY_VALUE)

            return

        # -----------------------------
        # Table Header
        # -----------------------------

        lower = text.lower()

        if (
            "item" in lower and
            "quantity" in lower
        ):

            row.set_type(RowType.TABLE_HEADER)

            return

        # -----------------------------
        # Invoice Header
        # -----------------------------

        if "invoice" in lower:

            row.set_type(RowType.HEADER)

            return

        # -----------------------------
        # Table Row
        # -----------------------------

        if len(columns) >= 2:

            row.set_type(RowType.TABLE_ROW)

            return

        # -----------------------------
        # Everything else
        # -----------------------------

        row.set_type(RowType.TEXT)

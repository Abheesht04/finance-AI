class Table:

    def __init__(self):

        self._rows = []

    def add_row(self, row):

        self._rows.append(row)

    def get_rows(self):

        return self._rows

    def get_row_count(self):

        return len(self._rows)

    def __str__(self):

        return f"Rows : {len(self._rows)}"

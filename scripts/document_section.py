class DocumentSection:

    def __init__(self):

        self._name = ""

        self._rows = []

    # -----------------------------------

    def set_name(self, name):

        self._name = name

    def get_name(self):

        return self._name

    # -----------------------------------

    def add_row(self, row):

        self._rows.append(row)

    def get_rows(self):

        return self._rows

    # -----------------------------------

    def __str__(self):

        return f"{self._name} ({len(self._rows)} rows)"

from scripts.row_type import RowType


class LayoutRow:

    def __init__(self):

        self._y = 0.0

        self._blocks = []

        self._columns = []

        self._type = RowType.UNKNOWN

    # -------------------------------------------------
    # Y Coordinate
    # -------------------------------------------------

    def set_y(self, y):

        self._y = y

    def get_y(self):

        return self._y

    # -------------------------------------------------
    # Text Blocks
    # -------------------------------------------------

    def add_block(self, block):

        self._blocks.append(block)

    def get_blocks(self):

        return self._blocks

    # -------------------------------------------------
    # Columns
    # -------------------------------------------------

    def add_column(self, column):

        self._columns.append(column)

    def get_columns(self):

        return self._columns

    # -------------------------------------------------
    # Classification
    # -------------------------------------------------

    def set_type(self, row_type):

        self._type = row_type

    def get_type(self):

        return self._type

    # -------------------------------------------------
    # Sorting
    # -------------------------------------------------

    def sort(self):

        self._blocks.sort(
            key=lambda block: block.get_bbox()[0]
        )

    # -------------------------------------------------
    # Text Helpers
    # -------------------------------------------------

    def get_text(self):

        if len(self._columns) > 0:

            return " ".join(

                column.get_text()

                for column in self._columns

            )

        return " ".join(

            block.get_text()

            for block in self._blocks

        )

    # -------------------------------------------------

    def __str__(self):

        return self.get_text()

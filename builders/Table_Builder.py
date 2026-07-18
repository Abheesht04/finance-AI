from scripts.row_type import RowType


class TableBuilder:

    def build(self, document):

        page = document.get_page(0)

        rows = page.get_layout_rows()

        tables = []

        current_table = []

        inside_table = False

        for row in rows:

            #
            # Table starts
            #

            if row.get_type() == RowType.TABLE_HEADER:

                inside_table = True

                current_table = [row]

                continue

            #
            # Table rows
            #

            if inside_table:

                #
                # Invoice usually ends table when totals begin
                #

                if row.get_type() == RowType.KEY_VALUE:

                    tables.append(current_table)

                    current_table = []

                    inside_table = False

                    continue

                current_table.append(row)

        if len(current_table):

            tables.append(current_table)

        return tables

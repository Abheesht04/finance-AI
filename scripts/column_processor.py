from scripts.column import Column


class ColumnProcessor:

    GAP_THRESHOLD = 80.0

    def process(self, document):

        for page in document.get_pages():

            for row in page.get_layout_rows():

                self._process_row(row)

    # --------------------------------------------

    def _process_row(self, row):

        blocks = row.get_blocks()

        if len(blocks) == 0:

            return

        blocks.sort(

            key=lambda b: b.get_bbox()[0]

        )

        column = Column()

        previous = None

        for block in blocks:

            x0, _, _, _ = block.get_bbox()

            if previous is not None:

                _, _, px1, _ = previous.get_bbox()

                gap = x0 - px1

                if gap > self.GAP_THRESHOLD:

                    row.add_column(column)

                    column = Column()

            column.add_block(block)

            previous = block

        row.add_column(column)

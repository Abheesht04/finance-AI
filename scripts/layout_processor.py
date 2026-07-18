from collections import defaultdict

from scripts.layout_row import LayoutRow


class LayoutProcessor:

    ROW_TOLERANCE = 4.0

    def process(self, document):

        for page in document.get_pages():

            self._process_page(page)

    # -------------------------------------------------

    def _process_page(self, page):

        buckets = defaultdict(LayoutRow)

        for block in page.get_text_blocks():

            _, y0, _, _ = block.get_bbox()

            key = round(y0 / self.ROW_TOLERANCE)

            row = buckets[key]

            if row.get_y() == 0.0:
                row.set_y(y0)

            row.add_block(block)

        rows = list(buckets.values())

        rows.sort(
            key=lambda row: row.get_y()
        )

        for row in rows:

            row.sort()

            page.add_layout_row(row)

from scripts.page_region import PageRegion


class GeometryProcessor:

    def process(self, document):

        for page in document.get_pages():

            self._process(page)

    # ----------------------------------

    def _process(self, page):

        width = page._width

        left = PageRegion()
        center = PageRegion()
        right = PageRegion()

        left.set_name("LEFT")
        center.set_name("CENTER")
        right.set_name("RIGHT")

        a = width / 3
        b = 2 * width / 3

        for block in page.get_text_blocks():

            x0, y0, x1, y1 = block.get_bbox()

            cx = (x0 + x1) * 0.5

            if cx < a:

                left.add_block(block)

            elif cx < b:

                center.add_block(block)

            else:

                right.add_block(block)

        page.add_region(left)
        page.add_region(center)
        page.add_region(right)

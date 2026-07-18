import fitz

from scripts.text_block import TextBlock


class TextProcessor:

    def process(self, document, pdf_document):

        for page_index in range(len(pdf_document)):

            pdf_page = pdf_document[page_index]

            page = document.get_page(page_index)

            self._process_page(page, pdf_page)

    # -------------------------------------

    def _process_page(self, page, pdf_page):

        data = pdf_page.get_text("dict")

        for block in data["blocks"]:

            if block.get("type", 0) != 0:
                continue

            self._process_block(page, block)

    # -------------------------------------

    def _process_block(self, page, block):

        for line in block["lines"]:

            for span in line["spans"]:

                tb = TextBlock()

                tb.set_text(span["text"])

                tb.set_page(page.get_page_number())

                x0, y0, x1, y1 = span["bbox"]

                tb.set_bbox(x0, y0, x1, y1)

                tb.set_font(
                    span["font"],
                    span["size"]
                )

                page.add_text_block(tb)

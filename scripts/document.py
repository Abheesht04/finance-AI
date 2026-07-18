from typing import List

from scripts.page import Page
from scripts.metadata import Metadata


class Document:

    def __init__(self, file_name):

        self._file_name = file_name

        self._pages: List[Page] = []

        self._metadata = Metadata()

    # -------------------------------------------------

    def add_page(self, page: Page):

        self._pages.append(page)

    # -------------------------------------------------

    def get_page(self, index):

        return self._pages[index]

    # -------------------------------------------------

    def get_pages(self):

        return self._pages

    # -------------------------------------------------

    def get_page_count(self):

        return len(self._pages)

    # -------------------------------------------------

    def set_metadata(self, metadata):

        self._metadata = metadata

    # -------------------------------------------------

    def get_metadata(self):

        return self._metadata

    # -------------------------------------------------

    def get_file_name(self):

        return self._file_name

    # -------------------------------------------------

    def __str__(self):

        output = []

        output.append("")
        output.append("========================================")
        output.append("              DOCUMENT")
        output.append("========================================")
        output.append(f"File   : {self._file_name}")
        output.append(f"Pages  : {self.get_page_count()}")
        output.append("")
        output.append("Metadata")
        output.append("----------------------------------------")
        output.append(str(self._metadata))
        output.append("")
        output.append("Pages")
        output.append("----------------------------------------")

        for page in self._pages:

            output.append(str(page))
            output.append("----------------------------------------")

        return "\n".join(output)

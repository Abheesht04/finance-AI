import fitz

from scripts.document import Document
from scripts.page import Page
from scripts.metadata import Metadata
from scripts.text_processor import TextProcessor
from scripts.layout_processor import LayoutProcessor
from scripts.column_processor import ColumnProcessor
from scripts.keyvalue_processor import KeyValueProcessor
from scripts.row_classifier import RowClassifier
from builders.invoice_builder import InvoiceBuilder
from finance.invoice import Invoice





class PdfAdapter:

    def __init__(self):

        self._pdf = None

    # -----------------------------------------------------
    # Public
    # -----------------------------------------------------

    def parse(self, filename: str):

        

        self._pdf = fitz.open(filename)

        document = Document(filename)

       

        self._read_metadata(document)

        self._read_pages(document)

        processor = TextProcessor()

        processor.process(document,self._pdf)

        layout = LayoutProcessor()

        layout.process(document)

        column = ColumnProcessor()

        column.process(document)

        classifier = RowClassifier()
        classifier.process(document)

        key = KeyValueProcessor()

        key.process(document)


    

       










        return document

    # -----------------------------------------------------
    # Private
    # -----------------------------------------------------

    def _read_metadata(self, document: Document):

        info = self._pdf.metadata

        metadata = Metadata()

        metadata.set_title(info.get("title", ""))

        metadata.set_author(info.get("author", ""))

        metadata.set_creator(info.get("creator", ""))

        metadata.set_producer(info.get("producer", ""))

        metadata.set_creation_date(info.get("creationDate", ""))

        metadata.set_modification_date(info.get("modDate", ""))

        document.set_metadata(metadata)

    # -----------------------------------------------------

    def _read_pages(self, document: Document):

        for index in range(len(self._pdf)):

            pdf_page = self._pdf[index]

            page = Page(index + 1)

            rect = pdf_page.rect

            page.set_size(rect.width, rect.height)

            page.set_rotation(pdf_page.rotation)

            document.add_page(page)

from scripts.table import Table
from scripts.text_block import TextBlock
from scripts.image import Image
from scripts.layout_row import LayoutRow
from scripts.key_value import KeyValue
from scripts.keyvalue_processor import KeyValueProcessor
from scripts.document_section import DocumentSection

class Page:

    def __init__(self, number):

        self._page_number = number

        self._width = 0

        self._height = 0

        self._rotation = 0

        self._text_blocks = []

        self._tables = []

        self._images = []

        self._layout_rows = []

        self._columns = []

        self._key_values = []

        self._sections = []

        self._regions = []






    # ----------------------------

    def set_size(self, width, height):

        self._width = width
        self._height = height

    def set_rotation(self, rotation):

        self._rotation = rotation

    # ----------------------------

    def add_text_block(self, block):

        self._text_blocks.append(block)

    def add_table(self, table):

        self._tables.append(table)

    def add_image(self, image):

        self._images.append(image)

    # ----------------------------

    def get_text_blocks(self):

        return self._text_blocks

    def get_tables(self):

        return self._tables

    def get_images(self):

        return self._images


    def get_page_number(self):

        return self._page_number


    def add_layout_row(self,row):

        self._layout_rows.append(row)


    def get_layout_rows(self):

        return self._layout_rows

    def add_column(self,column):

        self._columns.append(column)

    def get_columns(self):

        return self._columns

    def add_key_value(self,kv):

        self._key_values.append(kv)

    def get_key_values(self):

        return self._key_values

    def add_section(self,section):

        self._sections.append(section)

    def get_sections(self):

        return self._sections

    def add_region(self,region):

        self._regions.append(region)

    def get_regions(self):

        return self._regions






    # ----------------------------

    def __str__(self):

        return (
            f"Page {self._page_number}\n"
            f"Width       : {self._width:.2f}\n"
            f"Height      : {self._height:.2f}\n"
            f"Rotation    : {self._rotation}\n"
            f"TextBlocks  : {len(self._text_blocks)}\n"
            f"Tables      : {len(self._tables)}\n"
            f"Images      : {len(self._images)}"
        )

class PageRegion:

    def __init__(self):

        self._name = ""

        self._blocks = []

    # --------------------------

    def set_name(self, value):

        self._name = value

    def get_name(self):

        return self._name

    # --------------------------

    def add_block(self, block):

        self._blocks.append(block)

    def get_blocks(self):

        return self._blocks

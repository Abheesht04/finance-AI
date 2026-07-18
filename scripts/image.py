class Image:

    def __init__(self):

        self._index = 0

        self._width = 0

        self._height = 0

        self._color_space = ""

        self._bits_per_component = 0

        self._file_name = ""

    # -------------------------

    def set_index(self, index):

        self._index = index

    def get_index(self):

        return self._index

    # -------------------------

    def set_size(self, width, height):

        self._width = width
        self._height = height

    def get_width(self):

        return self._width

    def get_height(self):

        return self._height

    # -------------------------

    def set_color_space(self, color):

        self._color_space = color

    def get_color_space(self):

        return self._color_space

    # -------------------------

    def set_bits(self, bits):

        self._bits_per_component = bits

    def get_bits(self):

        return self._bits_per_component

    # -------------------------

    def set_file_name(self, name):

        self._file_name = name

    def get_file_name(self):

        return self._file_name

    # -------------------------

    def __str__(self):

        return (
            f"Image {self._index}\n"
            f"{self._width}x{self._height}"
        )

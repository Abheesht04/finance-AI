class TextBlock:

    def __init__(self):

        self._text = ""

        self._page = 0

        self._x0 = 0.0
        self._y0 = 0.0

        self._x1 = 0.0
        self._y1 = 0.0

        self._font_name = ""

        self._font_size = 0.0

    # --------------------------

    def set_text(self, text):

        self._text = text

    def get_text(self):

        return self._text

    # --------------------------

    def set_page(self, page):

        self._page = page

    def get_page(self):

        return self._page

    # --------------------------

    def set_bbox(self, x0, y0, x1, y1):

        self._x0 = x0
        self._y0 = y0

        self._x1 = x1
        self._y1 = y1

    def get_bbox(self):

        return (
            self._x0,
            self._y0,
            self._x1,
            self._y1
        )

    # --------------------------

    def set_font(self, name, size):

        self._font_name = name
        self._font_size = size

    def get_font_name(self):

        return self._font_name

    def get_font_size(self):

        return self._font_size

    # --------------------------

    def __str__(self):

        return (
            f"{self._text}\n"
            f"BBox : ({self._x0:.2f}, {self._y0:.2f}) -> ({self._x1:.2f}, {self._y1:.2f})\n"
            f"Font : {self._font_name} ({self._font_size})"
        )

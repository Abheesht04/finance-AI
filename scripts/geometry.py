class Geometry:

    def __init__(self):

        self._x0 = 0.0
        self._y0 = 0.0

        self._x1 = 0.0
        self._y1 = 0.0

    # -----------------------------------

    def set_bbox(self, x0, y0, x1, y1):

        self._x0 = x0
        self._y0 = y0

        self._x1 = x1
        self._y1 = y1

    # -----------------------------------

    def width(self):

        return self._x1 - self._x0

    def height(self):

        return self._y1 - self._y0

    def area(self):

        return self.width() * self.height()

    # -----------------------------------

    def center_x(self):

        return (self._x0 + self._x1) * 0.5

    def center_y(self):

        return (self._y0 + self._y1) * 0.5

    # -----------------------------------

    def left(self):

        return self._x0

    def right(self):

        return self._x1

    def top(self):

        return self._y0

    def bottom(self):

        return self._y1

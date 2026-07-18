class Column:

    def __init__(self):

        self._blocks = []

        self._x0 = 0.0
        self._x1 = 0.0

    # -----------------------------

    def add_block(self, block):

        self._blocks.append(block)

    # -----------------------------

    def get_blocks(self):

        return self._blocks

    # -----------------------------

    def compute_bounds(self):

        if not self._blocks:
            return

        xs = []

        for block in self._blocks:

            x0, _, x1, _ = block.get_bbox()

            xs.append(x0)
            xs.append(x1)

        self._x0 = min(xs)
        self._x1 = max(xs)

    # -----------------------------

    def get_bounds(self):

        return (self._x0, self._x1)

    # -----------------------------

    def get_text(self):

        return " ".join(
            block.get_text()
            for block in self._blocks
        )

    # -----------------------------

    def __str__(self):

        return self.get_text()

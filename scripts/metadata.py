class Metadata:

    def __init__(self):

        self._title = ""
        self._author = ""
        self._creator = ""
        self._producer = ""
        self._creation_date = ""
        self._modification_date = ""

    # -------------------------
    # Setters
    # -------------------------

    def set_title(self, value):
        self._title = value

    def set_author(self, value):
        self._author = value

    def set_creator(self, value):
        self._creator = value

    def set_producer(self, value):
        self._producer = value

    def set_creation_date(self, value):
        self._creation_date = value

    def set_modification_date(self, value):
        self._modification_date = value

    # -------------------------
    # Getters
    # -------------------------

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_creator(self):
        return self._creator

    def get_producer(self):
        return self._producer

    def get_creation_date(self):
        return self._creation_date

    def get_modification_date(self):
        return self._modification_date

    # -------------------------

    def __str__(self):

        return (
            f"Title      : {self._title}\n"
            f"Author     : {self._author}\n"
            f"Creator    : {self._creator}\n"
            f"Producer   : {self._producer}\n"
            f"Created    : {self._creation_date}\n"
            f"Modified   : {self._modification_date}"
        )

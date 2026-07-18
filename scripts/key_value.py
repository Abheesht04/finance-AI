class KeyValue:

    def __init__(self):

        self._key = ""

        self._value = ""

    def set_key(self, key):

        self._key = key

    def set_value(self, value):

        self._value = value

    def get_key(self):

        return self._key

    def get_value(self):

        return self._value

    def __str__(self):

        return f"{self._key:20} -> {self._value}"

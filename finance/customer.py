class Customer:

    def __init__(self):

        self._name = ""

        self._address = []

    def set_name(self, name):

        self._name = name

    def get_name(self):

        return self._name

    def add_address_line(self, line):

        self._address.append(line)

    def get_address(self):

        return self._address

class Vendor:

    def __init__(self):

        self._name = ""

        self._vendor_id = ""

        self._country = ""

        self._confidence = 1.0

    def set_name(self, name):

        self._name = name

    def get_name(self):

        return self._name

    def set_vendor_id(self, vendor_id):

        self._vendor_id = vendor_id

    def get_vendor_id(self):

        return self._vendor_id

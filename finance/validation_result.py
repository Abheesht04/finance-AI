class ValidationResult:

    def __init__(self):

        self._passed = True

        self._messages = []

    # -------------------------

    def fail(self, message):

        self._passed = False

        self._messages.append(message)

    # -------------------------

    def add_info(self, message):

        self._messages.append(message)

    # -------------------------

    def passed(self):

        return self._passed

    # -------------------------

    def get_messages(self):

        return self._messages

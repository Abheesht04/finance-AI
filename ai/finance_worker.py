from ai.adpater_ai import FinanceEngineAI

class FinanceWorker:

    def __init__(self):

        self._engine = FinanceEngineAI()

        self._document = None

        self._invoice = None

    # --------------------------------------------------

    def load_document(self, document):

        self._document = document

    # --------------------------------------------------

    def load_invoice(self, invoice):

        self._invoice = invoice

    # --------------------------------------------------

    def ask(self, question):

        return self._engine.answer(

            self._document,

            self._invoice,

            question

        )

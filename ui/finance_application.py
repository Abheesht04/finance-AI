from adapters.pdf_adapter import PdfAdapter
from builders.invoice_builder import InvoiceBuilder
from ai.finance_worker import FinanceWorker

import os


class FinanceApplication:

    def __init__(self):

        self.worker = FinanceWorker()

        self.document = None
        self.invoice = None
        self.current_pdf = None

    def load_pdf(self, pdf_path):

        adapter = PdfAdapter()

        document = adapter.parse(pdf_path)

        builder = InvoiceBuilder()

        invoice = builder.build(document)

        self.worker.load_document(document)

        self.worker.load_invoice(invoice)

        self.document = document

        self.invoice = invoice

        self.current_pdf = os.path.basename(pdf_path)

        return invoice

    def ask(self, question):

        if self.invoice is None:

            raise RuntimeError("No PDF has been loaded.")

        return self.worker.ask(question)

    def reset(self):

        self.worker = FinanceWorker()

        self.document = None

        self.invoice = None

        self.current_pdf = None

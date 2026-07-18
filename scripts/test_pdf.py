import sys
import os
import traceback
from tkinter import Tk, filedialog

# Dynamically add the project root to sys.path so 'adapters' can be found
# Assuming your project root is D:\Clara_ai\FinanceWorker\Python\api
project_root = r"D:\Clara_ai\FinanceWorker\Python\api"
if project_root not in sys.path:
    sys.path.append(project_root)


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now we can import the module correctly
from adapters.pdf_adapter import PdfAdapter
from finance.invoice import Invoice
from builders.invoice_builder import InvoiceBuilder
from finance.validation_engine import ValidationEngine
from finance.repository import InvoiceRepository
from SectionProcessor import SectionProcessor
from TableProcessor import TableProcessor
from scripts.GeometryProcessor import GeometryProcessor
from ai.finance_worker import FinanceWorker
from ai.finance_worker import FinanceWorker
from ai.adpater_ai import ClaraConsole




def open_pdf_dialog() -> str:
    """Opens a file dialog to select a PDF and returns the path."""
    root = Tk()
    root.withdraw()  # Hide the main Tk window
    root.attributes("-topmost", True)  # Keep dialog on top

    filename = filedialog.askopenfilename(
        title="Select a PDF Invoice",
        filetypes=[
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        ]
    )

    root.destroy()
    return filename

def main():
    pdf_path = open_pdf_dialog()

    if not pdf_path:
        print("No file selected. Exiting.")
        return

    try:

        print("===== TEST PDF STARTED =====")
        # Initialize and run the adapter
        adapter = PdfAdapter()
        document = adapter.parse(pdf_path)

        builder = InvoiceBuilder()

        print("pages:",document.get_page_count())

        print("Rows on page 0:",len(document.get_page(0).get_layout_rows()))

        print("KeyValues:",len(document.get_page(0).get_key_values()))


        print("calling the build ")

        invoice = builder.build(document)

        worker = FinanceWorker()

        worker.load_document(document)

        worker.load_invoice(invoice)

        console = ClaraConsole()

        console.run(worker)

        prompt = worker.ask("Summarize this invoice.")

        print()

        print("="*80)
        print("PROMPT SENT TO AI")

        print("="*80)

        print(prompt)


        repo = InvoiceRepository()

        duplicate = repo.find_duplicate(invoice)

        print()

        print("="*50)


        print(
                duplicate.is_duplicate(), 
                duplicate.get_reason()


                )
        repo.add(invoice)

        print()

        print(
                "Repo size:", repo.count()
                )

        validator = ValidationEngine()
        validation = validator.validate(invoice)

        print()
        print("="*50)
        print("VALIDATION")
        print("="*50)

        print("passed:",validation.passed())

        for message in validation.get_messages():
            print("-",message)

        invoice.print_summary()
        print()
        print("="*50)
        print("ITEMS")
        print("="*50)

        for item in invoice.items().get_all():
            print("Description :",item.get_description())
            print("Quantity :",item.get_quantity())
            print("Unit Price :",item.unit_price())
            print("Line Total :",item.line_total())
            print()


        geometry = GeometryProcessor()
        geometry.process(document)

        print()
        print("="*60)
        print("PAGE REGIONS")
        print("="*60)

        for page in document.get_pages():

            for region in page.get_regions():

                print()
                print(region.get_name())

                for block in region.get_blocks():

                    print(" ",block.get_text())



        section = SectionProcessor()
        section.process(document)
        table = TableProcessor()
        table.process(document)
      

        print()

        print("="*60)
        print("SECTIONS")
        print("="*60)

        for page in document.get_pages():
            for section in page.get_sections():

                print()
                print(section.get_name())

                for row in section.get_rows():
                    print(" ",row.get_text())

        print("the return valuse of the build")


        
        # Display the result
        print(document)

        for page in document.get_pages():

            print()

            print("="*70)

            print("PAGE",page.get_page_number())

            print("="*70)

            for row in page.get_layout_rows():

                print()

                for column in row.get_columns():

                    print(

                "[",

                column.get_text(),

                "]",

                end=" "

            )

        print()

        print("="*70)
        print("KEY VALUE PAIRS")
        print("="*70)

        for page in document.get_pages():

            print()

            for kv in page.get_key_values():
                print(f"{kv.get_key():20}->{kv.get_value()}")

        print()
        print("="*70)
        print("ROW CLASSIFIER")
        print("="*70)

        for page in document.get_pages():

            for row in page.get_layout_rows():

                print(f"[{row.get_type().name:15}] {row.get_text()}")



        





        









            


        
    except Exception:

        traceback.print_exc()
        

if __name__ == "__main__":
    main()

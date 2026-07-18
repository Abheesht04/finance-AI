from tkinter import Tk
from tkinter import filedialog


def open_pdf():

    root = Tk()

    root.withdraw()

    root.attributes("-topmost", True)

    filename = filedialog.askopenfilename(
        title="Open PDF",
        filetypes=[("PDF", "*.pdf")]
    )

    root.destroy()

    return filename

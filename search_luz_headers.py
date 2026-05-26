import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(50, 100):
            text = reader.pages[i].extract_text()
            if text:
                if "Capítulo" in text or "CAPÍTULO" in text:
                    header = text[:100].replace('\n', ' ')
                    print("Page {}: {}".format(i+1, header))

except Exception as e:
    print("Error: {}".format(e))

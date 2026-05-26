import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(70, 150):
            page_text = reader.pages[i].extract_text()
            if "Capítulo 8" in page_text or "Capítulo VIII" in page_text or "CAPÍTULO 8" in page_text:
                print(f"Page {i+1} mentions Cap 8")
                # print a snippet
                print(page_text[:100])
except Exception as e:
    print(f"Error: {e}")

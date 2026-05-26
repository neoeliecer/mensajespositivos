import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(132, 165):
        text = pdf.pages[i].extract_text()
        if text and ("Parte tres" in text or "RESPIRACI" in text):
            print(f"Found something on page {i+1}")
            print(text)

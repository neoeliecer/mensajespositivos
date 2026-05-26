import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(110, 150):
        text = pdf.pages[i].extract_text()
        if text and ("Siete" in text and "Masticar" in text):
            print(f"Found Chapter 7 on page {i+1}")
            print(text[:200])
            break

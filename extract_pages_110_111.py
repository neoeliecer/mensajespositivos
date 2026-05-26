import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(109, 111):
        text = pdf.pages[i].extract_text()
        print(f"--- Page {i+1} ---")
        print(text)
        print("-" * 30)

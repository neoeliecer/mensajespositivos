import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(109, 115):
        text = pdf.pages[i].extract_text()
        print(f"--- Page {i+1} ---")
        print(text[:1000] if text else "EMPTY PAGE")
        print("-" * 20)

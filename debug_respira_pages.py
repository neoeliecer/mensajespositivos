import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(70, 85):
        text = pdf.pages[i].extract_text()
        if text:
            lines = text.splitlines()
            if lines:
                print(f"P{i+1}: {lines[0]}")
        else:
            print(f"P{i+1}: EMPTY")

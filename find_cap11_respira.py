import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(220, 260):
        text = pdf.pages[i].extract_text()
        if text and ("Once" in text or "ONCE" in text or "Parte IV" in text or "PARTE IV" in text):
            print(f"Potential Chapter 11 on page {i+1}")
            print(text[:300])

import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(132, 170):
        text = pdf.pages[i].extract_text()
        if text and ("Parte tres" in text or "RESPIRACI" in text or "Ocho" in text):
            if "Ocho" in text:
                print(f"Potential Chapter 8 on page {i+1}")
                print(text[:300])

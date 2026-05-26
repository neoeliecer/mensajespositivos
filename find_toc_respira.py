import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(0, 30):
        text = pdf.pages[i].extract_text()
        if text and ("ndice" in text or "CONTENIDO" in text or "Indice" in text):
            print(f"Found TOC on page {i+1}")
            print(text)
            break

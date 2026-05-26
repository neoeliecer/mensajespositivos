import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(73, 150):
        text = pdf.pages[i].extract_text()
        if text and "Cinco" in text[:50]:
            print(f"Capítulo 5 empieza en P{i+1}")
            break
        if text and "CINCO" in text[:50]:
            print(f"Capítulo 5 empieza en P{i+1}")
            break

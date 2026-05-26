import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(175, 220):
        text = pdf.pages[i].extract_text()
        if text and ("Nueve" in text):
            print(f"Potential Chapter 9 on page {i+1}")
            print(text[:300])

import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(132, 170):
        text = pdf.pages[i].extract_text()
        if text and ("Ocho" in text and "Ms, de vez en cuando" in text):
            print(f"Found Chapter 8 on page {i+1}")
            print(text[:200])
            break

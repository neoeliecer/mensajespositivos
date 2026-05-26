import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    # Let's peek at pages 109 to 130 to find Chapter 6
    for i in range(108, 130):
        text = pdf.pages[i].extract_text()
        if text and ("Capítulo 6" in text or "CAPÍTULO 6" in text or "CAPITULO 6" in text):
            print(f"Found Chapter 6 on page {i+1}")
            print(text[:200])
        if text and ("Capítulo 7" in text or "CAPÍTULO 7" in text or "CAPITULO 7" in text):
            print(f"Found Chapter 7 on page {i+1}")
            print(text[:200])

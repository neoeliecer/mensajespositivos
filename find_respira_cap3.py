import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(50, 100):
        text = pdf.pages[i].extract_text()
        if text:
            if "CAPÍTULO" in text.upper() or "PARTE" in text.upper() or "3" in text:
                print(f"--- PÁGINA {i+1} ---")
                print(text[:200])
                print("-" * 20)

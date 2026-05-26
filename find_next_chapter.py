import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with open("ch11_clean.txt", "w", encoding="utf-8") as out:
    with pdfplumber.open(pdf_path) as pdf:
        for i in range(221, 260):
            text = pdf.pages[i].extract_text()
            if text:
                lines = text.split('\n')[:3]
                out.write(f"Page {i+1}: {lines[0]}\n")

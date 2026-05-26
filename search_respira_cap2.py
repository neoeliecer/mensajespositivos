import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i in range(10, min(100, len(pdf.pages))):
        text = pdf.pages[i].extract_text()
        if text:
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            for j, line in enumerate(lines[:10]): # Check first few lines of the page
                if "Dos" in line or "DOS" in line or "Capítulo 2" in line or "Respirar por la boca" in line:
                    print(f"Page {i+1} might be start of chapter 2:")
                    print("\n".join(lines[:5]))
                    print("---")
                if "Tres" in line or "TRES" in line or "Nariz" in line:
                    print(f"Page {i+1} might be start of chapter 3:")
                    print("\n".join(lines[:5]))
                    print("---")

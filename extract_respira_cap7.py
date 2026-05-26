import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'
output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_respira_cap7.txt'

with pdfplumber.open(pdf_path) as pdf:
    with open(output_path, 'w', encoding='utf-8') as f:
        # Chapter 7: pages 133 to 170 (indices 132 to 169)
        for i in range(132, 170):
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                f.write(text)
                f.write("\n\n")

print(f"Extraction complete: {output_path}")

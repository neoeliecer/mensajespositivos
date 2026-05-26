import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'
output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_respira_cap10.txt'

with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for i in range(220, 240): # Page 221 to 240
        page = pdf.pages[i]
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)

print(f"Extracted Chapter 10 to {output_path}")

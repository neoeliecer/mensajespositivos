import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'
output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_respira_cap6.txt'

with pdfplumber.open(pdf_path) as pdf:
    chapter_text = []
    
    # Chapter 6: P111 (index 110) to P132 (index 131)
    for i in range(110, 132):
        try:
            text = pdf.pages[i].extract_text()
            if text:
                chapter_text.append(f"\n--- PÁGINA {i+1} ---\n")
                chapter_text.append(text)
        except Exception as e:
            print(f"Error extracting page {i}: {e}")
    
    full_text = '\n'.join(chapter_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"Extraído {len(full_text)} caracteres del Capítulo 6 de Respira")

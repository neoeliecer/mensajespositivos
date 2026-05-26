import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'
output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_respira_cap5.txt'

with pdfplumber.open(pdf_path) as pdf:
    chapter_text = []
    
    # Chapter 5: P92 (index 91) to P109 (index 108)
    for i in range(91, 109):
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
    
    print(f"Extraído {len(full_text)} caracteres del Capítulo 5")

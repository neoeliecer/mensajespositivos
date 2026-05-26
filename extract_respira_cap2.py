import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'
output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_respira_cap2.txt'

with pdfplumber.open(pdf_path) as pdf:
    # Page index in pdfplumber is 0-based.
    # Page 38 in extracto_respira_cap1.txt corresponds to i=37 in pdfplumber.
    # But let's check what `i` was in extract_respira_cap1.py.
    # extract_respira_cap1.py had `for i in range(20, 60): ... chapter_text.append(f"\n--- PÁGINA {i+1} ---\n")`
    # So "--- PÁGINA 38 ---" means i=37.
    
    chapter_text = []
    
    # Let's extract from i=37 to i=70
    for i in range(37, 70):
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
    
    print(f"Extraído {len(full_text)} caracteres")

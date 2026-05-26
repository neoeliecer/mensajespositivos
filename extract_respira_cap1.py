import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\respira-james-nestor-3-pdf-free.pdf'
output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_respira_cap1.txt'

with pdfplumber.open(pdf_path) as pdf:
    total = len(pdf.pages)
    # Chapter 1 starts at page 21 (index 20), "Uno"
    # Let's find where chapter 2 starts to know the end
    # From the scan: page 38 is "Respirar por la boca" which might be chapter 2
    # Let's extract pages 20-54 and check
    chapter_text = []
    
    for i in range(20, 60):  # pages 21-60 to capture ch1
        text = pdf.pages[i].extract_text()
        if text:
            chapter_text.append(f"\n--- PÁGINA {i+1} ---\n")
            chapter_text.append(text)
    
    full_text = '\n'.join(chapter_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"Extraído {len(full_text)} caracteres")
    print("Primeros 500 chars:")
    print(full_text[:500])

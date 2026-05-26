import PyPDF2

pdf_path = r'C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf'
output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_luz_cap13.txt'

start_page = 134
end_page = 146

with open(pdf_path, 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    extracted_text = []
    
    # Extraer las páginas del capítulo 13
    for i in range(start_page, end_page + 1):
        if i < len(reader.pages):
            text = reader.pages[i].extract_text()
            if text:
                extracted_text.append(text)
                
with open(output_path, 'w', encoding='utf-8') as out_f:
    out_f.write('\n\n'.join(extracted_text))
    
print(f"Extraction complete! Saved to {output_path}")

import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    for i in range(num_pages):
        text = reader.pages[i].extract_text()
        if text:
            if "efecto placebo en el cuerpo" in text.lower() and i > 50:
                print(f"Found 'efecto placebo en el cuerpo' on page {i}")
                print(text[:200])
                print("-" * 20)
            
            # Let's also look for words like "Capítulo 4" or "4." at the beginning or something
            lines = text.split('\n')
            for line in lines[:5]:
                if re.match(r'^\s*4\.\s+', line) or re.match(r'^\s*5\.\s+', line):
                    print(f"Potential chapter heading on page {i}: {line}")

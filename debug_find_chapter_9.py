import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        # Search range based on previous chapters (Chapter 8 likely ended around page 150-180?)
        # Let's search a broad range to be safe.
        for i in range(100, num_pages):
            page = reader.pages[i]
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines[:10]: # check first few lines
                 if "9." in line or "CAPÍTULO 9" in line.upper() or "CAPÍTULO IX" in line.upper() or "CAPITULO 9" in line.upper():
                     print(f"Possible Chapter 9 match on page {i+1}: {line.strip()}")
            
except Exception as e:
    print(f"Error: {e}")

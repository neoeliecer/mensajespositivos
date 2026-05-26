import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        # Search from Chapter 9 start (221)
        for i in range(220, num_pages):
            page = reader.pages[i]
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines[:10]: # check first few lines
                 if "10." in line or "CAPÍTULO 10" in line.upper() or "CAPÍTULO X" in line.upper() or "CAPITULO 10" in line.upper():
                     print(f"Possible Chapter 10 match on page {i+1}: {line.strip()}")
            
except Exception as e:
    print(f"Error: {e}")

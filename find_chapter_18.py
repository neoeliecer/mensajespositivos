
import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")
        
        # Start searching from page 339 where Chapter 17 starts
        start_page = 338
        print(f"Searching from page {start_page}...")

        for i in range(start_page, num_pages):
            page = reader.pages[i]
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines[:10]: # check first few lines
                 if "18." in line or "CAPÍTULO 18" in line.upper() or "CAPÍTULO XVIII" in line.upper(): 
                     print(f"Possible Chapter 18 match on page {i+1}: {line.strip()}")
            
except Exception as e:
    print(f"Error: {e}")

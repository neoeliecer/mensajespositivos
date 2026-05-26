
import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")
        
        # Start searching from page 300 since Chapter 11 ended around 270
        start_page = 300
        print(f"Searching from page {start_page}...")

        for i in range(start_page, num_pages):
            if i % 10 == 0:
                print(f"Processing page {i}...")
            
            page = reader.pages[i]
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines[:10]: # check first few lines of each page
                 if "17." in line or "CAPÍTULO 17" in line.upper() or "CAPÍTULO XVII" in line.upper() or "Reconquista tu vida" in line:
                     print(f"Possible Chapter 17 match on page {i+1}: {line.strip()}")
            
except Exception as e:
    print(f"Error: {e}")

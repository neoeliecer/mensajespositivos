
import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        for i in range(140, min(200, num_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines[:5]: # check first few lines
                 if "6." in line or "CAPÍTULO 6" in line.upper() or "CAPÍTULO VI" in line.upper():
                     print(f"Possible Chapter 6 match on page {i+1}: {line.strip()}")
            
            for line in lines[:5]:
                 if "7." in line or "CAPÍTULO 7" in line.upper() or "CAPÍTULO VII" in line.upper():
                     print(f"Possible Chapter 7 match on page {i+1}: {line.strip()}")

except Exception as e:
    print(f"Error: {e}")

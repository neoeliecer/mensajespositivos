import PyPDF2
import re

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        print(f"Total pages: {num_pages}")
        
        # Regex to find chapter headings
        # Looking for "Capítulo 12" or "12." or similar
        
        found_chapters = []

        for i in range(num_pages):
            text = reader.pages[i].extract_text()
            lines = text.split('\n')
            for line in lines:
                if "capítulo" in line.lower() and "12" in line:
                     print(f"Match on page {i+1} (index {i}): {line.strip()}")
                     found_chapters.append((i, line.strip()))
                elif "12" in line and "cerebro" in line.lower(): # Title might be "12. Cuando el cerebro no piensa"
                     print(f"Match on page {i+1} (index {i}): {line.strip()}")
                     found_chapters.append((i, line.strip()))

    print("\nSummary of potential chapters:")
    for page, line in found_chapters:
        print(f"Page {page+1}: {line}")

except Exception as e:
    print(f"Error: {e}")

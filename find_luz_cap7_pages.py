import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        for i in range(num_pages):
            page_text = reader.pages[i].extract_text()
            if page_text:
                # Look for "Capítulo 7" or "Capítulo VII"
                if re.search(r'(?i)Cap[ií]tulo\s+7', page_text) or re.search(r'(?i)Cap[ií]tulo\s+VII', page_text):
                    # Check if it looks like a chapter header (not just a reference)
                    # Usually chapter headers are on their own line or near the top
                    lines = page_text.split('\n')
                    for line in lines[:5]: # Check first few lines
                        if re.search(r'(?i)Cap[ií]tulo\s+7', line) or re.search(r'(?i)Cap[ií]tulo\s+VII', line):
                            print(f"FOUND Chapter 7 header on page {i+1}")
                            print(f"Line: {line}")
            
            # Also search for Chapter 8 to find the end
            if i > 50: # Skip early pages
                if re.search(r'(?i)Cap[ií]tulo\s+8', page_text) or re.search(r'(?i)Cap[ií]tulo\s+VIII', page_text):
                    lines = page_text.split('\n')
                    for line in lines[:5]:
                        if re.search(r'(?i)Cap[ií]tulo\s+8', line) or re.search(r'(?i)Cap[ií]tulo\s+VIII', line):
                            print(f"FOUND Chapter 8 header on page {i+1}")
                            print(f"Line: {line}")

except Exception as e:
    print(f"Error: {e}")
